#!/usr/bin/env python3
"""Build the blinded assessor packet for corrected official v2 runs (A_V2_01, B_V2_01, C_V2_01).

Reads terminal result text from committed run_trials.py captures under evidence/v2-20261013/,
verifies their checksums, refuses to overwrite, strips directory paths, and writes the
arm mapping to a separate key file. It does not grade.
"""
import hashlib
import json
import random
import re
from pathlib import Path

from prepare_fresh_packets import strip_paths

ROOT = Path(__file__).resolve().parents[1]
RUNS = {'A': 'A_V2_01', 'B': 'B_V2_01', 'C': 'C_V2_01'}
SEED = 2026101321
OUT = ROOT / 'evaluation' / 'v2-20261013' / 'official'


def main():
    if (OUT / 'blind_packet.md').exists():
        raise SystemExit('refusing to overwrite existing packet')
    rows = []
    for arm, run in RUNS.items():
        base = ROOT / 'evidence' / 'v2-20261013' / run
        manifest = json.loads((base / 'manifest.json').read_text(encoding='utf-8'))
        assert manifest['status'] == 'COMPLETE_UNGRADED' and manifest['benchmark_version'] == 'v2' and manifest['arm'] == arm
        for line in (base / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
            digest, fname = line.split('  ', 1)
            assert hashlib.sha256((base / fname).read_bytes()).hexdigest() == digest, f'checksum {run}/{fname}'
        for n in range(1, 9):
            ev = [json.loads(l) for l in (base / f'Q{n}.stream.jsonl').read_text(encoding='utf-8').splitlines() if l.strip()]
            res = [e for e in ev if e.get('type') == 'result']
            assert len(res) == 1 and res[0].get('subtype') == 'success' and not res[0].get('is_error')
            rows.append((arm, f'Q{n}', res[0]['result']))
    random.Random(SEED).shuffle(rows)
    prompts = [(ROOT / 'control' / 'prompts-v2' / f'Q{n}.txt').read_text(encoding='utf-8').strip() for n in range(1, 9)]
    parts = [(ROOT / 'evaluation/scoring-rubric.md').read_text(encoding='utf-8'),
             (ROOT / 'evaluation/expected-answers.md').read_text(encoding='utf-8'),
             '# QUESTIONS (corrected v2; Q4 is self-contained)\n\n' + '\n\n'.join(f'**Q{n}.** {p}' for n, p in enumerate(prompts, 1)) + '\n',
             '# RESPONSES TO SCORE (shuffled; arm identity withheld; directory paths stripped)\n']
    key = {'seed': SEED, 'runs': RUNS, 'responses': {}}
    for i, (arm, q, text) in enumerate(rows, 1):
        rid = f'R{i:02d}'
        key['responses'][rid] = {'arm': arm, 'q': q}
        parts.append(f'## {rid} — answers {q}\n\n{strip_paths(text)}\n')
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / 'blind_packet.md').write_text('\n'.join(parts), encoding='utf-8', newline='\n')
    (OUT / 'blind_key.json').write_text(json.dumps(key, indent=1) + '\n', encoding='utf-8', newline='\n')
    print('official v2:', len(rows), 'responses ->', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
