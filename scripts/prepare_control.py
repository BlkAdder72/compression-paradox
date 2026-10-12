#!/usr/bin/env python3
"""Export verbatim, independently testable control prompts from frozen questions."""
from pathlib import Path
import hashlib, json, re
ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'questions.md'
text = source.read_text(encoding='utf-8')
found = re.findall(r'^\*\*Q([1-8])\.\*\* (.*)$', text, re.M)
assert [q for q,_ in found] == list('12345678'), 'Expected exactly Q1 through Q8'
assert not (ROOT / 'specialist').exists(), 'Do not prepare control after specialist creation'
out = ROOT / 'control' / 'prompts'
out.mkdir(parents=True, exist_ok=True)
items=[]
for n,prompt in found:
    file = out / f'Q{n}.txt'
    file.write_text(prompt + '\n', encoding='utf-8')
    items.append({'id':f'Q{n}','filename':f'control/prompts/Q{n}.txt','sha256':hashlib.sha256(file.read_bytes()).hexdigest()})
manifest={'question_source':'questions.md','question_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'instructions':'Use each text file verbatim, one fresh no-folder Claude session per question. No attached sources, no repository, no gold key. Save unedited provider transcript into control/raw/.','prompts':items}
(ROOT / 'control' / 'prompt-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print('PASS: exported 8 unchanged prompts; source sha256',manifest['question_sha256'])
