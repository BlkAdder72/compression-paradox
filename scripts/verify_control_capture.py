#!/usr/bin/env python3
"""Verify prompt integrity and existence of authentic capture artifacts; never synthesize transcripts."""
from pathlib import Path
import json,re,hashlib,sys
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'control/prompt-manifest.json').read_text(encoding='utf-8'))
q_source=(root/'history/questions-v1.md').read_bytes()
assert hashlib.sha256(q_source).hexdigest()==manifest['question_sha256'], 'Frozen question file changed'
assert len(manifest['prompts'])==8
expected=dict((('Q'+n),p) for n,p in re.findall(r'^\*\*Q([1-8])\.\*\* (.*)$',q_source.decode(),re.M))
for item in manifest['prompts']:
    p=root/item['filename']
    assert p.read_text(encoding='utf-8')==expected[item['id']]+'\n',f'Prompt changed: {item["id"]}'
    assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
print('PASS: all 8 legacy control prompts match archived v1 benchmark exactly')
current=json.loads((root/'control/prompt-manifest-v2.json').read_text(encoding='utf-8'))
source=(root/'questions.md').read_bytes()
assert hashlib.sha256(source).hexdigest()==current['question_sha256']
expected_v2=dict((('Q'+n),p) for n,p in re.findall(r'^\*\*Q([1-8])\.\*\* (.*)$',source.decode(),re.M))
assert len(current['prompts']) == len(expected_v2) == 8
for item in current['prompts']:
    p=root/item['filename']
    assert p.read_bytes()==(expected_v2[item['id']]+'\n').encode('utf-8')
    assert hashlib.sha256(p.read_bytes()).hexdigest()==item['sha256']
    if item['id']!='Q4': assert expected_v2[item['id']]==expected[item['id']]
assert 'same facts as Q3' not in expected_v2['Q4']
assert '## Expected answers' in source.decode()
print('PASS: v2 self-contained Q4, seven unchanged questions, expected answers and isolated prompts')
raw=list((root/'control/raw').glob('*'))
if not raw:
    print('PENDING: no authentic control captures. No inference or scoring performed.')
    sys.exit(0)
print(f'CAPTURES PRESENT: {len(raw)} (existence is NOT proof of genuine provider execution)')
