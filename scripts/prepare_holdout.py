#!/usr/bin/env python3
"""Generate exact H1-H8 prompt files from frozen holdout questions; refuse silent drift."""
from pathlib import Path
import re,hashlib
ROOT=Path(__file__).resolve().parents[1]
q=ROOT/'evaluation/holdout/questions.md'
raw=q.read_text(encoding='utf-8')
hits=re.findall(r'^\*\*H(\d+)\.\*\* (.+)$',raw,re.M)
assert [int(n) for n,_ in hits]==list(range(1,9)), "expected H1-H8 in order"
out=ROOT/'diagnostics/holdout-prompts'
out.mkdir(exist_ok=True,parents=True)
for n,s in hits:
 p=out/f'H{n}.txt'
 data=(s+'\n').encode('utf-8')
 if p.exists() and p.read_bytes()!=data:
  raise SystemExit(f"REFUSE overwrite changed prompt {p}")
 p.write_bytes(data)
manifest={"holdout_questions_sha256":hashlib.sha256(q.read_bytes()).hexdigest(),
          "prompts":{f"H{n}":hashlib.sha256((s+'\n').encode()).hexdigest() for n,s in hits}}
manifestpath=out/'manifest.json'
if manifestpath.exists() and __import__("json").loads(manifestpath.read_text(encoding='utf-8'))!=manifest:
 raise SystemExit("REFUSE changed prompt manifest")
manifestpath.write_text(__import__('json').dumps(manifest,indent=2)+'\n')
print("PASS: eight immutable holdout prompts extracted")