#!/usr/bin/env python3
"""Recompute stored score arithmetic and verify evidence hashes, without regrading."""
import hashlib
import json
from pathlib import Path
import re
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
RUNS = {'scoring-run-1': {'A': ('control/raw', 'A2', 'Q'), 'B': ('treatment/raw', 'B1', 'Q'), 'C': ('diagnostics/source-only/raw', 'C1', 'Q')},
        'scoring-repro-1': {'A': ('control/raw', 'A_REPRO_1', 'Q'), 'B': ('treatment/raw', 'B_REPRO_1', 'Q')},
        'scoring-run-2': {'C': ('diagnostics/source-only/raw', 'CH1', 'H'), 'D': ('diagnostics/aggressive-summary/raw', 'DH1', 'H'), 'E': ('diagnostics/index-first/raw', 'EH1', 'H')},
        'scoring-run-3': {'C': ('diagnostics/source-only/raw', 'CH2', 'H'), 'D': ('diagnostics/aggressive-summary/raw', 'DH3', 'H'), 'E': ('diagnostics/index-first/raw', 'EH3', 'H')}}

def audit():
    report = {'scope': 'Stored evidence integrity and arithmetic only; no new model execution, independent authorship verification or independent grading.', 'scores': {}, 'hash_entries_checked': 0}
    for manifest in ROOT.glob('**/*SHA256SUMS.txt'):
        for line in manifest.read_text(encoding='utf-8-sig').splitlines():
            if not line.strip():
                continue
            match = re.fullmatch(r'([0-9a-fA-F]{64})\s+\*?(.+)', line)
            assert match, f'Malformed hash record: {manifest}'
            digest, name = match.groups()
            candidates = [ROOT / name, manifest.parent / name, manifest.parent / Path(name).name]
            path = next((p for p in candidates if p.is_file()), None)
            assert path and path.resolve().is_relative_to(ROOT), f'Missing hash target: {name}'
            assert hashlib.sha256(path.read_bytes()).hexdigest() == digest.lower(), f'Hash mismatch: {path}'
            report['hash_entries_checked'] += 1
    limits = {'conclusion': 4, 'rules': 2, 'exceptions': 2, 'evidence': 1, 'unsupported': 1}
    for folder, arms in RUNS.items():
        base = ROOT / 'evaluation' / folder
        scores = json.loads((base / 'assessor-scores.json').read_text(encoding='utf-8'))
        keys = json.loads((base / 'blind_key.json').read_text(encoding='utf-8'))
        assert len(scores) == len(keys) == 8 * len(arms)
        assert len({s['id'] for s in scores}) == len(scores)
        result = defaultdict(dict)
        for score in scores:
            key = keys[score['id']]
            assert key['q'] == score['q']
            assert all(type(score[k]) is int and 0 <= score[k] <= top for k, top in limits.items())
            total = sum(score[k] for k in limits)
            if score['conclusion_wrong']:
                total = min(total, 4)
            assert total == score['capped_total'], f'Arithmetic mismatch {folder} {score["id"]}'
            assert key['q'] not in result[key['arm']]
            result[key['arm']][key['q']] = total
        arm_reports = {}
        for arm, (path, run, prefix) in arms.items():
            assert set(result[arm]) == {f'{prefix}{n}' for n in range(1, 9)}
            durations = []
            for n in range(1, 9):
                events = [json.loads(s) for s in (ROOT / path / f'{run}-{prefix}{n}.stream.jsonl').read_text(encoding='utf-8').splitlines() if s.strip()]
                final = [e for e in events if e.get('type') == 'result']
                assert len(final) == 1 and final[0].get('subtype') == 'success' and not final[0].get('is_error')
                durations.append(final[0]['duration_ms'])
            arm_reports[arm] = {'run': run, 'total': sum(result[arm].values()), 'per_question': dict(sorted(result[arm].items())), 'mean_duration_ms': sum(durations) / 8}
        report['scores'][folder] = arm_reports
    return report

if __name__ == '__main__':
    print(json.dumps(audit(), indent=2))
