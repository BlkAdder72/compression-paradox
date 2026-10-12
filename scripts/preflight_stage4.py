#!/usr/bin/env python3
"""Read-only preflight for the supplemental H-series experiments."""
import hashlib, json, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
checks=['questions.md','protocol.md','evaluation/holdout/questions.md','evaluation/holdout/expected-answers.md','diagnostics/holdout-prompts/manifest.json']
for f in checks:
    assert (ROOT/f).is_file(),f'missing {f}'
manifest=json.loads((ROOT/'diagnostics/holdout-prompts/manifest.json').read_text())
for i in range(1,9):
    name=f'H{i}'
    p=ROOT/'diagnostics/holdout-prompts'/f'{name}.txt'
    assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==manifest['prompts'][name]
for arm in ['aggressive-summary','index-first']:
    base=ROOT/'diagnostics'/arm
    assert (base/'README.md').is_file()
    for f in (ROOT/'fixture').glob('*.md'):
        assert (base/'reference'/f.name).read_bytes()==f.read_bytes()
print('PASS: preflight input fingerprints, required files, reference byte identity')
print('MODEL EXECUTION: Not performed by this script')
