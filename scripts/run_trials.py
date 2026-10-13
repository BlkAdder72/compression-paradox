#!/usr/bin/env python3
"""Real Claude CLI capture runner. Never generates or scores model responses."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {'A': None, 'B': 'specialist', 'C': 'fixture',
           'D': 'diagnostics/aggressive-summary', 'E': 'diagnostics/index-first'}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def source_files(arm):
    source = SOURCES[arm]
    if source is None:
        return []
    base = ROOT / source
    expected = ([p.name for p in (ROOT / 'fixture').glob('*.md')] if arm == 'C' else
                ['README.md'] + ['reference/' + p.name for p in (ROOT / 'fixture').glob('*.md')])
    if arm == 'B':
        expected += ['identity.md', 'rules.md', 'examples.md']
    if arm == 'D':
        expected += ['SUMMARY.md']
    return [(base / name, name) for name in sorted(expected)]

def prompts(suite, question_file=None):
    if suite == 'challenge':
        data = json.loads(Path(question_file).read_text(encoding='utf-8'))
        rows = [(q['id'], q['prompt'].encode('utf-8') + b'\n') for q in data['questions']]
    else:
        prefix, folder = {'official': ('Q', 'control/prompts-v2'), 'legacy': ('Q', 'control/prompts'), 'holdout': ('H', 'diagnostics/holdout-prompts')}[suite]
        rows = [(f'{prefix}{i}', (ROOT / folder / f'{prefix}{i}.txt').read_bytes()) for i in range(1, 9)]
    if not rows or len({q for q, _ in rows}) != len(rows) or any(not re.fullmatch(r'[A-Za-z0-9_-]+', q) for q, _ in rows):
        raise ValueError('Empty, duplicate or unsafe question IDs')
    return rows

def successful_stream(path):
    events = [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]
    results = [e for e in events if e.get('type') == 'result']
    return len(results) == 1 and results[0].get('subtype') == 'success' and not results[0].get('is_error', False)

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--arm', choices=SOURCES, required=True)
    ap.add_argument('--suite', choices=['official', 'legacy', 'holdout', 'challenge'], default='official')
    ap.add_argument('--questions', help='Challenge JSON, kept outside model workspace')
    ap.add_argument('--run-id', required=True)
    ap.add_argument('--workspace', required=True, type=Path)
    ap.add_argument('--output', required=True, type=Path, help='Parent output directory; a new run directory is created')
    ap.add_argument('--claude', default=os.environ.get('CLAUDE_BIN', 'claude'))
    ap.add_argument('--model', default=os.environ.get('MODEL', 'claude-opus-5-5'))
    ap.add_argument('--timeout', type=int, default=600)
    ap.add_argument('--dry-run', action='store_true', help='Validate inputs only; no Claude invocation or capture files')
    a = ap.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9_-]+', a.run_id):
        ap.error('Unsafe run ID')
    ws, out = a.workspace.resolve(), a.output.resolve() / a.run_id
    if ws.is_relative_to(ROOT) or ROOT.is_relative_to(ws):
        ap.error('Workspace must be outside and must not contain the repository')
    if out.is_relative_to(ws) or ws.is_relative_to(out):
        ap.error('Workspace and output must be separate')
    sessions = ws / a.run_id
    if out.exists() or sessions.exists():
        ap.error('Run ID already exists; never overwrite or resume captures')
    if a.suite == 'challenge' and not a.questions:
        ap.error('--questions required')
    rows = prompts(a.suite, a.questions)
    files = source_files(a.arm)
    for p, _ in files:
        if not p.is_file() or p.is_symlink():
            ap.error('Missing or symlink source: ' + str(p))
    manifest = {'status': 'DRY_RUN' if a.dry_run else 'STARTED', 'arm': a.arm, 'suite': a.suite,
                'model_requested': a.model, 'run_id': a.run_id, 'benchmark_version': 'v2' if a.suite == 'official' else ('v1' if a.suite == 'legacy' else a.suite),
                'commit': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
                'sources': {name: sha(p) for p, name in files},
                'prompts': {q: hashlib.sha256(b).hexdigest() for q, b in rows},
                'question_file_sha256': sha(Path(a.questions)) if a.questions else None,
                'limitations': 'Directory separation is not OS isolation. Review tool reads and permission denials. Model alias and external authorship are not authenticated by this runner.',
                'records': []}
    if a.dry_run:
        print(json.dumps(manifest, indent=2)); return
    if subprocess.check_output(['git', 'status', '--porcelain'], cwd=ROOT).strip():
        ap.error('Commit inputs and start from a clean checkout')
    exe = shutil.which(a.claude)
    if not exe:
        ap.error('Claude CLI unavailable; no model execution performed')
    manifest['cli_version'] = subprocess.check_output([exe, '--version'], text=True, timeout=30).strip()
    manifest['started_utc'] = datetime.now(timezone.utc).isoformat()
    out.mkdir(parents=True, exist_ok=False)
    sessions.mkdir(parents=True, exist_ok=False)
    def save():
        (out / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8', newline='\n')
    save()
    failed = False
    try:
        for q, prompt in rows:
            session = sessions / q
            session.mkdir()
            for src, name in files:
                target = session / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, target)
            command = [exe, '-p', '--model', a.model, '--output-format', 'stream-json', '--verbose',
                       '--tools', 'Read,Glob,Grep', '--strict-mcp-config', '--no-session-persistence',
                       '--permission-mode', 'default']
            stdout, stderr = out / f'{q}.stream.jsonl', out / f'{q}.stderr.txt'
            record = {'question': q, 'start_utc': datetime.now(timezone.utc).isoformat(), 'command': command}
            try:
                with stdout.open('xb') as so, stderr.open('xb') as se:
                    result = subprocess.run(command, input=prompt, cwd=session, stdout=so, stderr=se, timeout=a.timeout)
                record['exit'] = result.returncode
                record['success_event'] = successful_stream(stdout)
                failed = result.returncode != 0 or not record['success_event']
            except Exception as exc:
                record['error'] = str(exc); failed = True
            record['end_utc'] = datetime.now(timezone.utc).isoformat()
            manifest['records'].append(record); save()
            if failed:
                break
    finally:
        manifest['status'] = 'COMPLETE_UNGRADED' if not failed and len(manifest['records']) == len(rows) else 'FAILED_OR_INTERRUPTED'
        save()
        (out / 'SHA256SUMS.txt').write_text(''.join(f'{sha(p)}  {p.name}\n' for p in sorted(out.iterdir()) if p.is_file() and p.name != 'SHA256SUMS.txt'), encoding='utf-8', newline='\n')
    if manifest['status'] != 'COMPLETE_UNGRADED':
        sys.exit('Incomplete model run; evidence retained; do not score as a complete run')
    print('Captured real CLI output; ungraded and pending tool-access review:', out)

if __name__ == '__main__':
    main()
