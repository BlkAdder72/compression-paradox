#!/usr/bin/env python3
"""Validate and aggregate actual seven-question captures and human-readable assessment.
No model calls or automatic semantic grading. --check validates the saved summary.
"""
import hashlib
import json
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
IDS = ['Q1','Q2','Q3','Q5','Q6','Q7','Q8']
CATS = {'conclusion':4, 'rules':2, 'exceptions':2, 'evidence':1, 'unsupported':1}

def main():
    folder = ROOT / 'evaluation/seven-20261013'
    assessment = json.loads((folder / 'assessment-codex.json').read_text(encoding='utf-8'))
    scores = assessment['scores']
    assert len(scores) == 21
    assert {(s['arm'],s['q']) for s in scores} == {(a,q) for a in 'ABC' for q in IDS}
    report = {'benchmark':'seven-original', 'maximum_per_arm':70, 'ids':IDS,
              'assessor':assessment['assessor'], 'arms':{}, 'pairwise':{}}
    for arm in 'ABC':
        base = ROOT / 'evidence/seven-20261013' / (arm+'_SEVEN_01')
        manifest = json.loads((base / 'manifest.json').read_text(encoding='utf-8'))
        assert manifest['status'] == 'COMPLETE_UNGRADED'
        assert manifest['arm'] == arm and manifest['benchmark_version'] == 'seven-original'
        assert [x['question'] for x in manifest['records']] == IDS
        assert all(x['exit']==0 and x['success_event'] for x in manifest['records'])
        assert manifest['question_file_sha256'] == hashlib.sha256((folder/'questions.json').read_bytes()).hexdigest()
        for q in IDS:
            prompt = (ROOT / 'control/prompts-seven' / (q+'.txt')).read_bytes()
            assert hashlib.sha256(prompt).hexdigest() == manifest['prompts'][q]
        if arm in 'AB':
            duplicate = ROOT / ('control' if arm == 'A' else 'treatment') / 'raw' / (arm+'_SEVEN_01')
            assert {p.name for p in duplicate.iterdir()} == {p.name for p in base.iterdir()}
            for p in base.iterdir():
                assert (duplicate/p.name).read_bytes() == p.read_bytes()
        for line in (base/'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
            digest, name = line.split('  ',1)
            assert Path(name).name==name
            assert hashlib.sha256((base/name).read_bytes()).hexdigest()==digest
        per = {}; times = []; full = []; false = []
        for q in IDS:
            s = next(s for s in scores if s['arm']==arm and s['q']==q)
            assert all(type(s[k]) is int and 0<=s[k]<=v for k,v in CATS.items())
            assert s['conclusion'] in (0,2,4)
            assert type(s['conclusion_wrong']) is bool and type(s['false_authorization']) is bool
            assert s['rationale'].strip()
            total = sum(s[k] for k in CATS)
            if s['conclusion_wrong']: total=min(total,4)
            assert total==s['capped_total'], (arm,q,'arithmetic')
            assert not (s['conclusion']==4 and s['conclusion_wrong'])
            per[q]=total
            if s['conclusion']==4:full.append(q)
            if s['false_authorization']:false.append(q)
            stream=base/(q+'.stream.jsonl')
            assert hashlib.sha256(stream.read_bytes()).hexdigest()==s['raw_sha256']
            events=[json.loads(x) for x in stream.read_text(encoding='utf-8').splitlines() if x.strip()]
            result=[e for e in events if e.get('type')=='result']
            assert len(result)==1 and result[0]['subtype']=='success' and not result[0]['is_error']
            times.append(result[0]['duration_ms'])
        report['arms'][arm]={'run_id':arm+'_SEVEN_01','total':sum(per.values()),'per_question':per,
                            'fully_correct_conclusions':len(full),'false_authorizations':false,
                            'mean_duration_seconds':sum(times)/len(times)/1000}
    for a,b in [('B','A'),('C','A'),('B','C')]:
        pairs=[(report['arms'][a]['per_question'][q],report['arms'][b]['per_question'][q]) for q in IDS]
        report['pairwise'][a+' vs '+b]={'wins':sum(x>y for x,y in pairs),'ties':sum(x==y for x,y in pairs),'losses':sum(x<y for x,y in pairs)}
    target=folder/'summary.json'
    if '--check' in sys.argv:
        assert json.loads(target.read_text(encoding='utf-8'))==report
        print('PASS: 21 captured responses, score arithmetic, raw hashes and seven-question summary')
    else:
        target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps(report,indent=2))

if __name__=='__main__': main()
