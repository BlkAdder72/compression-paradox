#!/usr/bin/env python3
"""Read-only tool-access and provenance review of run_trials.py capture folders.

For each session it reports the init and assistant model IDs, every tool call, and
permission denials. It flags any Read outside the session directory, any read of a
file that is not on the arm's source allowlist (the manifest's `sources`), any
non-denied Glob/Grep whose path leaves the session directory, and missing success
events. It never edits captures and never grades answers.
"""
import argparse
import hashlib
import json
from pathlib import Path, PureWindowsPath, PurePosixPath


def norm(p):
    return str(p).replace('\\', '/').rstrip('/').casefold()


def review(run_dir, sessions_root):
    run_dir = Path(run_dir)
    m = json.loads((run_dir / 'manifest.json').read_text(encoding='utf-8'))
    allow = {norm(k) for k in m['sources']}
    out = {'run_id': m['run_id'], 'arm': m['arm'], 'suite': m['suite'], 'status': m['status'],
           'commit': m['commit'], 'cli_version': m.get('cli_version'), 'model_requested': m['model_requested'],
           'checksums_ok': True, 'sessions': {}, 'violations': [], 'notes': []}
    for line in (run_dir / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        digest, name = line.split('  ', 1)
        if hashlib.sha256((run_dir / name).read_bytes()).hexdigest() != digest:
            out['checksums_ok'] = False
            out['violations'].append(f'checksum mismatch {name}')
    for rec in m['records']:
        q = rec['question']
        session = norm(Path(sessions_root) / m['run_id'] / q)
        ev = [json.loads(l) for l in (run_dir / f'{q}.stream.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
        init = next((e for e in ev if e.get('type') == 'system' and e.get('subtype') == 'init'), {})
        res = [e for e in ev if e.get('type') == 'result']
        models = sorted({e['message'].get('model') for e in ev if e.get('type') == 'assistant'})
        results = {}
        for e in ev:
            content = e.get('message', {}).get('content') if e.get('type') == 'user' else None
            for c in content if isinstance(content, list) else []:
                if c.get('type') == 'tool_result':
                    txt = c.get('content')
                    results[c.get('tool_use_id')] = txt if isinstance(txt, str) else json.dumps(txt)
        calls, reads = [], []
        for e in ev:
            if e.get('type') != 'assistant':
                continue
            for c in e['message'].get('content', []):
                if c.get('type') != 'tool_use':
                    continue
                inp = c.get('input', {})
                target = inp.get('file_path') or inp.get('path') or ''
                calls.append({'tool': c['name'], 'target': target, 'pattern': inp.get('pattern'),
                              'result_head': (results.get(c.get('id')) or '')[:160]})
                if c['name'] == 'Read':
                    t = norm(target)
                    inside = t.startswith(session + '/')
                    rel = t[len(session) + 1:] if inside else t
                    reads.append(rel)
                    if not inside:
                        out['violations'].append(f'{q}: Read outside session: {target}')
                    elif rel not in allow:
                        out['violations'].append(f'{q}: Read of non-allowlisted file: {rel}')
        denials = (res[0].get('permission_denials') or []) if res else []
        denied_targets = {norm(d.get('tool_input', {}).get('path') or d.get('tool_input', {}).get('file_path') or '') for d in denials}
        for c in calls:
            if c['tool'] in ('Glob', 'Grep') and c['target']:
                t = norm(c['target'])
                if not (t == session or t.startswith(session + '/')) and t not in denied_targets:
                    if c['result_head'].strip() in ('No files found', 'No matches found'):
                        out['notes'].append(f'{q}: {c["tool"]} outside session permitted but returned nothing: {c["target"]}')
                    else:
                        out['violations'].append(f'{q}: {c["tool"]} outside session returned content: {c["target"]}')
        ok = len(res) == 1 and res[0].get('subtype') == 'success' and not res[0].get('is_error')
        if not ok:
            out['violations'].append(f'{q}: no single successful result event')
        if init.get('model') != m['model_requested'] or models != [m['model_requested']]:
            out['violations'].append(f'{q}: model mismatch init={init.get("model")} assistant={models}')
        out['sessions'][q] = {'exit': rec.get('exit'), 'init_model': init.get('model'), 'assistant_models': models,
                              'tools_available': init.get('tools'), 'mcp_servers': init.get('mcp_servers'),
                              'permission_mode': init.get('permissionMode'),
                              'duration_ms': res[0].get('duration_ms') if res else None,
                              'reads': reads, 'tool_calls': calls,
                              'denials': [{'tool': d.get('tool_name'), 'input': d.get('tool_input')} for d in denials]}
    out['verdict'] = 'CLEAN' if not out['violations'] and m['status'] == 'COMPLETE_UNGRADED' else 'REVIEW'
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sessions-root', required=True, help='--workspace used for the run')
    ap.add_argument('run_dirs', nargs='+')
    a = ap.parse_args()
    reports = [review(d, a.sessions_root) for d in a.run_dirs]
    print(json.dumps(reports, indent=2))
    for r in reports:
        n_den = sum(len(s['denials']) for s in r['sessions'].values())
        print(f"# {r['run_id']}: {r['verdict']} status={r['status']} cli={r['cli_version']} sessions={len(r['sessions'])} denials={n_den} violations={len(r['violations'])} notes={len(r['notes'])}")
