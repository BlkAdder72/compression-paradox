#!/usr/bin/env python3
"""Build blinded assessor packets for the 2026-10-13 fresh runs (official A/B/C, holdout C/D/E).

Reads terminal result text from committed run_trials.py captures. It verifies their
checksums and refuses to overwrite. Packets contain the frozen rubric, key, questions
and shuffled responses with directory paths stripped; the arm mapping is written to a
separate key file. It does not grade.
"""
import hashlib
import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVID = ROOT / 'evidence' / 'fresh-20261013'
OUT = ROOT / 'evaluation' / 'fresh-20261013'
SETS = {
    'official': {'runs': {'A': 'A_FRESH_20261013_01', 'B': 'B_FRESH_20261013_01', 'C': 'C_FRESH_20261013_01'},
                 'prefix': 'Q', 'questions': 'questions.md', 'key': 'evaluation/expected-answers.md', 'seed': 2026101301},
    'holdout': {'runs': {'C': 'CH_FRESH_01', 'D': 'DH_FRESH_01', 'E': 'EH_FRESH_01'},
                'prefix': 'H', 'questions': 'evaluation/holdout/questions.md', 'key': 'evaluation/holdout/expected-answers.md', 'seed': 2026101302},
}


def strip_paths(text):
    text = re.sub(r'[A-Za-z]:[\\/][^\s)`\'"]*[\\/]', '', text)
    return re.sub(r'/c/[^\s)`\'"]*/', '', text)


def build(name, spec):
    target = OUT / name
    if (target / 'blind_packet.md').exists():
        raise SystemExit(f'refusing to overwrite {target}')
    rows = []
    for arm, run in spec['runs'].items():
        base = EVID / run
        for line in (base / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
            digest, fname = line.split('  ', 1)
            assert hashlib.sha256((base / fname).read_bytes()).hexdigest() == digest, f'checksum {run}/{fname}'
        for n in range(1, 9):
            q = f"{spec['prefix']}{n}"
            ev = [json.loads(l) for l in (base / f'{q}.stream.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
            res = [e for e in ev if e.get('type') == 'result']
            assert len(res) == 1 and res[0].get('subtype') == 'success' and not res[0].get('is_error')
            rows.append((arm, q, res[0]['result']))
    random.Random(spec['seed']).shuffle(rows)
    qtext = (ROOT / spec['questions']).read_text(encoding='utf-8')
    qs = re.findall(rf"^\*\*{spec['prefix']}[1-8]\.\*\* .*$", qtext, re.M)
    assert len(qs) == 8
    parts = [(ROOT / 'evaluation/scoring-rubric.md').read_text(encoding='utf-8'),
             (ROOT / spec['key']).read_text(encoding='utf-8'),
             '# QUESTIONS\n\n' + '\n\n'.join(qs) + '\n',
             '# RESPONSES TO SCORE (shuffled; arm identity withheld; directory paths stripped)\n']
    key = {'seed': spec['seed'], 'runs': spec['runs'], 'responses': {}}
    for i, (arm, q, text) in enumerate(rows, 1):
        rid = f'R{i:02d}'
        key['responses'][rid] = {'arm': arm, 'q': q}
        parts.append(f'## {rid} — answers {q}\n\n{strip_paths(text)}\n')
    target.mkdir(parents=True, exist_ok=True)
    (target / 'blind_packet.md').write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    (target / 'blind_key.json').write_text(json.dumps(key, indent=1) + '\n', encoding='utf-8', newline='\n')
    print(name, len(rows), 'responses ->', target.relative_to(ROOT))


if __name__ == '__main__':
    for name, spec in SETS.items():
        build(name, spec)
