#!/usr/bin/env python3
"""Create an assessor packet from real completed challenge captures; does not grade."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import secrets

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--questions', type=Path, required=True)
    ap.add_argument('--run', action='append', required=True, help='ARM=absolute capture directory')
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    data = json.loads(a.questions.read_text(encoding='utf-8'))
    file_hash = hashlib.sha256(a.questions.read_bytes()).hexdigest()
    rows, arms = [], set()
    for entry in a.run:
        arm, folder = entry.split('=', 1)
        assert arm not in arms, 'Duplicate arm'
        arms.add(arm)
        base = Path(folder)
        manifest = json.loads((base / 'manifest.json').read_text(encoding='utf-8'))
        assert manifest['status'] == 'COMPLETE_UNGRADED' and manifest['arm'] == arm
        assert manifest['question_file_sha256'] == file_hash
        for line in (base / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
            digest, name = line.split('  ', 1)
            assert Path(name).name == name
            assert hashlib.sha256((base / name).read_bytes()).hexdigest() == digest
        for q in data['questions']:
            events = [json.loads(line) for line in (base / (q['id'] + '.stream.jsonl')).read_text(encoding='utf-8').splitlines() if line.strip()]
            results = [e for e in events if e.get('type') == 'result']
            assert len(results) == 1 and results[0].get('subtype') == 'success' and not results[0].get('is_error')
            assert isinstance(results[0].get('result'), str) and results[0]['result'].strip()
            rows.append((arm, q['id'], results[0]['result']))
    seed = secrets.randbits(64)
    random.Random(seed).shuffle(rows)
    packet = ['# Assessor packet', data.get('provenance', 'Authorship not verified'), 'Do not infer provenance from this packet. Score using the frozen rubric.']
    for q in data['questions']:
        packet += [f'## {q["id"]}', q['prompt'], 'Gold: ' + q['gold'], 'Critical requirements: ' + '; '.join(q['critical_requirements'])]
    mapping = {'seed': seed, 'questions_sha256': file_hash, 'responses': {}}
    for i, (arm, q, response) in enumerate(rows, 1):
        label = f'R{i:03}'
        mapping['responses'][label] = {'arm': arm, 'question': q}
        packet += [f'## {label} ({q})', response]
    a.output.mkdir(parents=True, exist_ok=False)
    (a.output / 'packet.md').write_text('\n\n'.join(packet) + '\n', encoding='utf-8', newline='\n')
    (a.output / 'mapping.json').write_text(json.dumps(mapping, indent=2) + '\n', encoding='utf-8', newline='\n')
    print('Prepared ungraded packet. Keep mapping.json hidden from assessors. Blinding may leak through response content.')

if __name__ == '__main__':
    main()
