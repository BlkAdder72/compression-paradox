#!/usr/bin/env python3
"""Check original chronology, retained prompt/gold identity and frozen seven-run inputs."""
import hashlib
import json
from pathlib import Path
import re
import subprocess
from run_trials import prompts

ROOT = Path(__file__).resolve().parents[1]
IDS = ['Q1', 'Q2', 'Q3', 'Q5', 'Q6', 'Q7', 'Q8']

def original(path):
    return subprocess.check_output(['git', 'show', 'df36e7d:' + path], cwd=ROOT).decode('utf-8')

def questions(text):
    return dict(re.findall(r'^\*\*(Q\d)\.\*\* (.*)$', text, re.M))

def answers(text):
    return {line.split('|')[1].strip(): line for line in text.splitlines() if line.startswith('| Q')}

def main():
    current = (ROOT / 'questions.md').read_text(encoding='utf-8')
    old_questions = questions(original('questions.md'))
    old_answers = answers(original('evaluation/expected-answers.md'))
    assert list(questions(current)) == list(answers(current)) == IDS
    for q in IDS:
        assert questions(current)[q] == old_questions[q], q + ' prompt changed'
        assert answers(current)[q] == old_answers[q], q + ' gold changed'
    rows = json.loads((ROOT / 'evaluation/seven-20261013/questions.json').read_text(encoding='utf-8'))['questions']
    assert [q['id'] for q in rows] == IDS
    for row in rows:
        columns = [x.strip() for x in old_answers[row['id']].split('|')[1:-1]]
        assert row['prompt'] == old_questions[row['id']]
        assert row['gold'] == columns[1]
        assert row['critical_requirements'] == [columns[2], 'Evidence sections: ' + columns[3], 'Disqualifying mistake: ' + columns[4]]
    assert prompts('official') == [(q, (old_questions[q] + '\n').encode()) for q in IDS]
    manifest = json.loads((ROOT / 'evaluation/seven-20261013/input-manifest.json').read_text(encoding='utf-8'))
    for name, digest in manifest['sha256'].items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    for later in ['da56555', '3d9be31']:
        subprocess.run(['git', 'merge-base', '--is-ancestor', 'df36e7d', later], cwd=ROOT, check=True)
    print('PASS: seven exact original questions AND gold answers predate control/folder; frozen inputs intact.')
    print('DISCLOSURE: original key was a separate file; seven-item selection occurred after earlier results.')

if __name__ == '__main__':
    main()
