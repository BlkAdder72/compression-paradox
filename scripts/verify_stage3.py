#!/usr/bin/env python3
"""Non-model checks for compression ablation and holdout. Does not grade LLM answers."""
from pathlib import Path
import hashlib, re, json, subprocess
ROOT=Path(__file__).resolve().parents[1]
fixture=sorted((ROOT/'fixture').glob('*.md'))
assert len(fixture)==6
sections=set()
for src in fixture:
 sections.update(re.findall(r'^## ([A-Z]{3}-\d+)',src.read_text(),re.M))
for arm in ('aggressive-summary','index-first'):
 target=ROOT/'diagnostics'/arm
 assert (target/'README.md').exists()
 copied=sorted((target/'reference').glob('*.md'))
 assert [p.name for p in copied]==[p.name for p in fixture]
 for src,dst in zip(fixture,copied):
  assert src.read_bytes()==dst.read_bytes(),f"{arm}: primary source drift {src.name}"
q=(ROOT/'evaluation/holdout/questions.md').read_text()
ids=re.findall(r'^\*\*H(\d+)\.\*\*',q,re.M)
assert ids==list('12345678'),ids
gold=(ROOT/'evaluation/holdout/expected-answers.md').read_text()
rows=re.findall(r'^\| H([1-8]) \|',gold,re.M)
assert rows==ids,(rows,ids)
for row in gold.splitlines():
 if re.match(r'^\| H[1-8] \|',row):
  for s in re.findall(r'\b[A-Z]{3}-\d+\b',row):
   assert s in sections,f"unknown primary section {s}"
manifest=json.loads((ROOT/'diagnostics/holdout-prompts/manifest.json').read_text())
assert manifest["holdout_questions_sha256"]==hashlib.sha256((ROOT/'evaluation/holdout/questions.md').read_bytes()).hexdigest()
for n in range(1,9):
 p=ROOT/f'diagnostics/holdout-prompts/H{n}.txt'
 assert hashlib.sha256(p.read_bytes()).hexdigest()==manifest["prompts"][f"H{n}"]
 assert p.read_text().strip() == re.search(rf'^\*\*H{n}\.\*\* (.+)$',q,re.M).group(1)
print("PASS: 8 holdouts, valid source IDs, exact prompts, all 12 primary document copies identical")
