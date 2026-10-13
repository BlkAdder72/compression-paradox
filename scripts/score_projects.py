"""Check committed UI assessment arithmetic and evidence identity; no semantic grading."""
import hashlib,json,subprocess,sys
from pathlib import Path
from verify_projects import main as verify_raw
ROOT=Path(__file__).resolve().parents[1]
IDS=['Q1','Q2','Q3','Q5','Q6','Q7','Q8']
CATS={'conclusion':4,'rules':2,'exceptions':2,'evidence':1,'unsupported':1}
def main():
 verify_raw()
 folder=ROOT/'evaluation/projects-20261013'
 a=json.loads((folder/'assessment-codex.json').read_text(encoding='utf8'))
 assert a['rubric_sha256']==hashlib.sha256((ROOT/'evaluation/scoring-rubric.md').read_bytes()).hexdigest()
 scores=a['scores']; assert len(scores)==21 and {(s['arm'],s['q']) for s in scores}=={(x,q) for x in 'ABC' for q in IDS}
 raw_manifest=subprocess.check_output(['git','show',a['raw_commit']+':evidence/projects-20261013/manifest.json'],cwd=ROOT)
 assert json.loads(raw_manifest)['status']=='COMPLETE_UNGRADED'
 report=dict(benchmark=a['benchmark'],maximum_per_arm=70,assessor=a['assessor'],raw_commit=a['raw_commit'],arms={},pairwise={})
 for arm in 'ABC':
  per={};full=0;false=[]
  for q in IDS:
   s=next(s for s in scores if s['arm']==arm and s['q']==q)
   assert all(type(s[k]) is int and 0<=s[k]<=m for k,m in CATS.items()) and s['conclusion'] in (0,2,4)
   assert type(s['conclusion_wrong']) is bool and type(s['false_authorization']) is bool and s['rationale'].strip()
   total=sum(s[k] for k in CATS); total=min(total,4) if s['conclusion_wrong'] else total
   assert total==s['capped_total'] and not(s['conclusion']==4 and s['conclusion_wrong'])
   raw=ROOT/s['raw_file']; assert raw.is_relative_to(ROOT/'evidence/projects-20261013'/(arm+'_UI_01'))
   assert hashlib.sha256(raw.read_bytes()).hexdigest()==s['raw_sha256']
   committed=subprocess.check_output(['git','show',a['raw_commit']+':'+s['raw_file']],cwd=ROOT)
   assert committed==raw.read_bytes(), 'Raw was not preserved before assessment'
   per[q]=total;full+=s['conclusion']==4
   if s['false_authorization']:false.append(q)
  report['arms'][arm]=dict(total=sum(per.values()),per_question=per,fully_correct_conclusions=full,false_authorizations=false)
 for x,y in [('B','A'),('C','A'),('B','C')]:
  pairs=[(report['arms'][x]['per_question'][q],report['arms'][y]['per_question'][q]) for q in IDS]
  report['pairwise'][x+' vs '+y]=dict(wins=sum(a>b for a,b in pairs),ties=sum(a==b for a,b in pairs),losses=sum(a<b for a,b in pairs))
 target=folder/'summary.json'
 if '--check' in sys.argv: assert json.loads(target.read_text(encoding='utf8'))==report
 else:target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf8',newline='\n')
 print(json.dumps(report,indent=2))
 print('PASS: UI score arithmetic and pre-assessment raw hashes; semantic judgments remain reviewable')
if __name__=='__main__':main()
