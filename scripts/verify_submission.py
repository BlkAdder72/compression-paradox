#!/usr/bin/env python3
"""Offline, read-only structural competition audit; cannot establish model provenance or behavioral reproducibility."""
from pathlib import Path
import hashlib, subprocess, json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(cond, explanation):
    print(('PASS' if cond else 'FAIL')+': '+explanation)
    if not cond: errors.append(explanation)
def git(*args):
    return subprocess.run(['git',*args],cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip()
check(all((ROOT/p).is_file() for p in ['README.md','questions.md','results.md','protocol.md','specialist/identity.md','specialist/rules.md','specialist/examples.md','specialist/README.md','evaluation/expected-answers.md','evaluation/scoring-rubric.md']), 'required files present')
check(len(list((ROOT/'specialist/reference').glob('*.md')))==6, 'reference corpus present')
check('df36e7d' in git('log','--oneline'), 'original preregistration commit still in history')
commits=git('rev-list','--reverse','HEAD').splitlines()
qidx=next((i for i,x in enumerate(commits) if x.startswith('df36e7d')),None)
aidx=next((i for i,x in enumerate(commits) if x.startswith('da56555')),None)
bidx=next((i for i,x in enumerate(commits) if x.startswith('3d9be31')),None)
check(None not in (qidx,aidx,bidx) and qidx<aidx<bidx, 'questions precede recorded control and specialist commits')
for arm,prefix,run in [('A','control/raw','A2'),('B','treatment/raw','B1'),('C','diagnostics/source-only/raw','C1')]:
    check(all((ROOT/prefix/f'{run}-Q{i}.stream.jsonl').is_file() for i in range(1,9)),f'{arm} original eight raw streams retained')
for arm,folder,runs in [('C','source-only',['CH1','CH2']),('D','aggressive-summary',['DH1','DH3']),('E','index-first',['EH1','EH3'])]:
    for run in runs:
        check(all((ROOT/f'diagnostics/{folder}/raw/{run}-H{i}.stream.jsonl').is_file() for i in range(1,9)),f'{arm} {run}: 8 raw challenge streams retained')
check((ROOT/'diagnostics/aggressive-summary/raw/run-manifest-DH2.md').is_file() and (ROOT/'diagnostics/index-first/raw/run-manifest-EH2.md').is_file(),'excluded attempts disclosed in preserved run manifests')
check(git('status','--porcelain')=='','working tree clean')
check('missing primary documents' in (ROOT/'results.md').read_text(encoding='utf8').lower() or 'source' in (ROOT/'results.md').read_text(encoding='utf8').lower(),'results includes source-only limitations')
print('LIMITATION: Passing offline checks does NOT prove provider authenticity, correct scoring or fresh-model reproducibility.')
if errors:
    print(f'FAILED {len(errors)} check(s)');sys.exit(1)
print('PASS: offline submission integrity checks')
