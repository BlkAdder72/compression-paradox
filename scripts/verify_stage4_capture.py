#!/usr/bin/env python3
"""Verify existence/JSON framing/hashes of real H-series captures, never simulate responses."""
from pathlib import Path
import argparse,hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--arm',choices=['D','E','C'],required=True)
parser.add_argument('--run-id',required=True)
a=parser.parse_args()
assert re.fullmatch(r'[A-Za-z0-9_-]+',a.run_id), 'unsafe run ID'
folder={'D':'aggressive-summary','E':'index-first','C':'source-only'}[a.arm]
base=ROOT/'diagnostics'/folder/'raw'
missing=[];hashes=[];errors=[]
for i in range(1,9):
    stem=f'{a.run_id}-H{i}'
    for suffix in ['.stream.jsonl','.stderr.txt']:
        p=base/(stem+suffix)
        if not p.is_file(): missing.append(str(p.relative_to(ROOT)));continue
        hashes.append((hashlib.sha256(p.read_bytes()).hexdigest(),str(p.relative_to(ROOT))))
        if suffix=='.stream.jsonl':
            try:
                lines=p.read_text().splitlines()
                if not lines: errors.append(f'{stem}: empty stream')
                for ln,line in enumerate(lines,1):
                    if line.strip():json.loads(line)
            except (ValueError,UnicodeError) as e: errors.append(f'{stem}: malformed JSON stream: {e}')
if missing or errors:
    print(json.dumps({'status':'INCOMPLETE','missing':missing,'errors':errors},indent=2))
    sys.exit(1)
log=base/f'{a.run_id}-run-log.txt'
if not log.exists():errors.append('missing run log')
else:
    records=log.read_text().splitlines()
    if len(records)!=8:errors.append(f'expected 8 log lines; got {len(records)}')
    for line in records:
        if 'exit=0' not in line:errors.append(f'nonzero/unknown exit: {line}')
if errors:
    print(json.dumps({'status':'INCOMPLETE','errors':errors},indent=2));sys.exit(1)
print('PASS: 8 raw transcript streams and stderr files, valid JSON framing, 8 logged successful exits')
print('NOTE: This checks structure, not provenance, correctness, or model identity.')
for digest,path in hashes:print(digest+'  '+path)
