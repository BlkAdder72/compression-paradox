"""Offline integrity checks for rendered Projects UI captures; never calls a model."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'evidence/projects-20261013'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    frozen = json.loads((ROOT/'evaluation/projects-20261013/input-manifest.json').read_text(encoding='utf-8-sig'))
    for name, expected in frozen.items():
        assert digest(ROOT/name) == expected, ('changed input', name)
    questions = json.loads((ROOT/'evaluation/seven-20261013/questions.json').read_text(encoding='utf-8'))['questions']
    manifest = json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
    assert manifest['capture_format'] == 'rendered-ui', 'Not API raw streams'
    seen = set()
    for row in manifest['records']:
        arm, qid = row['arm'], row['question']
        assert arm in 'ABC' and (arm,qid) not in seen
        seen.add((arm,qid))
        q = next(q for q in questions if q['id']==qid)
        folder = BASE/(arm+'_UI_01')
        assert (folder/(qid+'.prompt.txt')).read_text(encoding='utf-8') == q['prompt']
        for name, expected in row['sha256'].items():
            assert Path(name).name == name
            assert digest(folder/name) == expected, (arm,qid,name)
        visible = (folder/(qid+'.visible-ui.txt')).read_text(encoding='utf-8')
        assert q['prompt'] in visible and 'Memory is off for this chat' in visible
        assert 'Opus 5.5 Medium' in visible
        assert 'Claude finished the response' in visible
        assert (folder/row['response_file']).stat().st_size > 0
    if manifest['status']=='COMPLETE_UNGRADED' or manifest['status']=='COMPLETE_ASSESSED':
        assert seen=={(a,q['id']) for a in 'ABC' for q in questions}
    else:
        assert manifest['status']=='INCOMPLETE'
    print(f"PASS: {len(seen)} actual rendered UI records and frozen input hashes; status={manifest['status']}")
    print('Integrity only; semantic scores and hidden provider activity are not verified by this script.')

if __name__=='__main__':
    main()
