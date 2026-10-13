#!/usr/bin/env python3
"""Read-only validation of frozen separate-session author inputs; no model calls."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evaluation/unseen-20261013'
manifest = json.loads((BASE / 'input-manifest.json').read_text(encoding='utf-8'))
for group in ('inputs', 'fixture', 'specialist'):
    for name, digest in manifest[group].items():
        path = BASE / name if group == 'inputs' else ROOT / name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'Input drift: {name}'
assert hashlib.sha256((ROOT / 'evaluation/scoring-rubric.md').read_bytes()).hexdigest() == manifest['rubric_sha256']
data = json.loads((BASE / 'external-questions.json').read_text(encoding='utf-8'))
assert set(data) == {'provenance', 'questions'}
assert [q['id'] for q in data['questions']] == [f'U{i}' for i in range(1, 9)]
sections = set()
for path in (ROOT / 'fixture').glob('*.md'):
    sections.update(re.findall(r'^## ([A-Z]{3}-\d+)', path.read_text(encoding='utf-8'), re.M))
for q in data['questions']:
    assert set(q) == {'id', 'prompt', 'gold', 'critical_requirements'}
    assert q['critical_requirements'] and all(isinstance(x, str) for x in q['critical_requirements'])
    assert not re.search(r'\bU[1-8]\b|previous question|same facts as', q['prompt'], re.I)
    cited = set(re.findall(r'\b[A-Z]{3}-\d+\b', q['gold'] + ' '.join(q['critical_requirements'])))
    assert cited and cited <= sections
from run_trials import prompts
rows = prompts('challenge', BASE / 'external-questions.json')
assert all(b == (q['prompt'] + '\n').encode('utf-8') for (_, b), q in zip(rows, data['questions']))
print('PASS: 8 standalone author questions, valid sections, exact prompt-only extraction, all frozen input hashes')
print('PENDING: real A/B/C execution and grading. Separate-session authorship is self-reported, not independent human review.')
