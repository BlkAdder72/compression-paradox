"""Offline integrity checks for rendered Projects UI captures; never calls a model."""
import hashlib
import json
from datetime import datetime
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
    for arm, prefix, count in [('B','specialist/',10),('C','fixture/',6)]:
        imported = BASE/(arm+'_UI_01')/'knowledge-import.json'
        if not imported.exists():
            assert manifest['status']=='INCOMPLETE'
            continue
        entries = json.loads(imported.read_text(encoding='utf-8'))
        assert len(entries)==count
        assert {e['source'] for e in entries}=={p for p in frozen if p.startswith(prefix)}
        for entry in entries:
            source=ROOT/entry['source']
            assert digest(source)==entry['source_sha256']==frozen[entry['source']]
            submitted=source.read_text(encoding='utf-8')
            assert hashlib.sha256(submitted.encode()).hexdigest()==entry['submitted_text_sha256']
            assert len(submitted)==entry['characters']
            assert entry['title']==entry['source'][len(prefix):]
    setup=ROOT/'evaluation/projects-20261013/setup-sha256.json'
    if setup.exists():
        for name,expected in json.loads(setup.read_text(encoding='utf8')).items():
            assert digest(ROOT/name)==expected, ('setup asset changed',name)
    seen = set()
    for row in manifest['records']:
        arm, qid = row['arm'], row['question']
        assert arm in 'ABC' and (arm,qid) not in seen
        seen.add((arm,qid))
        q = next(q for q in questions if q['id']==qid)
        folder = BASE/(arm+'_UI_01')
        assert (folder/(qid+'.prompt.txt')).read_text(encoding='utf-8') == q['prompt']
        assert set(row['sha256']) == {p.name for p in folder.glob(qid+'.*')}, 'Unhashed Q artifact'
        assert row['response_file'] in row['sha256']
        meta=json.loads((folder/(qid+'.metadata.json')).read_text(encoding='utf8'))
        assert meta['arm']==arm and meta['question']==qid and meta['complete'] is True
        assert meta['model_label']=='Opus 5.5 Medium' and meta['url'].startswith('https://claude.ai/chat/')
        assert datetime.fromisoformat(meta['captured_at']) >= datetime.fromisoformat(meta['started_at'])
        if (arm,qid)!=('A','Q1'):
            preflight=(folder/(qid+'.preflight.txt')).read_text(encoding='utf8')
            assert 'menuitemcheckbox "Memory" [checked]' not in preflight
            assert 'menuitemcheckbox "Research" [checked]' not in preflight
            # A Q2 preserved the Devices submenu after the separate connector inspection.
            # Do not pretend this file contains a connector toggle snapshot.
            if (arm,qid)==('A','Q2'):
                assert 'menu "Devices"' in preflight
            else:
                # A Q2 preserved the Devices submenu after the separate connector inspection.
            # Do not pretend this file contains a connector toggle snapshot.
            if (arm,qid)==('A','Q2'):
                assert 'menu "Devices"' in preflight
            else:
                assert 'menu "Connectors"' in preflight
                assert not any('menuitemcheckbox' in line and ' icon ' in line and '[checked]' in line for line in preflight.splitlines())
                assert not any('menuitemcheckbox' in line and ' icon ' in line and '[checked]' in line for line in preflight.splitlines())
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
    if len(seen)==21:
        for arm,place in [('A','control'),('B','treatment')]:
            folder=BASE/(arm+'_UI_01'); duplicate=ROOT/place/'raw'/(arm+'_UI_01')
            assert {p.name for p in folder.iterdir()} == {p.name for p in duplicate.iterdir()}
            for p in folder.iterdir(): assert p.read_bytes()==(duplicate/p.name).read_bytes(), ('copy mismatch',p.name)
        for arm in 'ABC':
            memory=(BASE/(arm+'_UI_01')/'memory-after.txt').read_text(encoding='utf8')
            assert 'No memory yet' in memory and 'switch "Use account memory" [checked]' not in memory
    print(f"PASS: {len(seen)} actual rendered UI records and frozen input hashes; status={manifest['status']}")
    print('Integrity only; semantic scores and hidden provider activity are not verified by this script.')

if __name__=='__main__':
    main()
