#!/usr/bin/env python3
"""Static fixture sanity checks; does not pretend to evaluate LLM output."""
from pathlib import Path
import re, hashlib
root=Path(__file__).resolve().parents[1]
q=(root/'questions.md').read_text(encoding='utf-8')
items=re.findall(r'^\*\*Q([1-8])\.\*\*',q,re.M)
assert items==list('12345678'),f'Expected Q1..Q8 in order, found {items}'
gold=(root/'evaluation/expected-answers.md').read_text(encoding='utf-8')
rows=re.findall(r'^\| Q([1-8]) \|',gold,re.M)
assert rows==list('12345678'),f'Gold key mismatch: {rows}'
fixture=sorted((root/'fixture').glob('*.md'))
assert len(fixture)==6,f'Expected exactly 6 source documents, found {len(fixture)}'
sections=set()
for f in fixture:
    s=f.read_text(encoding='utf-8')
    assert 'Fictional Meridian Works' in s,f'Fixture is not clearly fictional: {f.name}'
    for section in re.findall(r'^## ([A-Z]{3}-\d+)',s,re.M):
        assert section not in sections,f'Duplicate section ID: {section}'
        sections.add(section)
for row in gold.splitlines():
    if re.match(r'^\| Q[1-8] \|',row):
        for token in re.findall(r'\b[A-Z]{3}-\d+\b',row):
            assert token in sections,f'Answer key cites missing section: {token}'
assert not (root/'specialist').exists(),'Stage 1 must not contain a specialist folder'
print('PASS: 8 benchmark questions, 8 answer rows, 6 fixture files, valid source IDs, no specialist')
print('questions.sha256:',hashlib.sha256((root/'questions.md').read_bytes()).hexdigest())
