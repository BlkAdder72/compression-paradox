#!/usr/bin/env python3
"""Temporary, explicitly synthetic regression fixtures; never model evidence."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

class PacketTests(unittest.TestCase):
    def test_packet_and_tamper_rejection(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            q = base / 'UNIT_TEST_QUESTIONS.json'
            q.write_text(json.dumps({'provenance': 'SYNTHETIC UNIT TEST ONLY', 'questions': [{'id': 'T1', 'prompt': 'UNIT TEST', 'gold': 'UNIT TEST', 'critical_requirements': ['UNIT TEST']}]}), encoding='utf-8')
            run = base / 'UNIT_TEST_RUN'
            run.mkdir()
            stream = run / 'T1.stream.jsonl'
            stream.write_text(json.dumps({'type': 'result', 'subtype': 'success', 'is_error': False, 'result': 'SYNTHETIC UNIT TEST ONLY'}) + '\n', encoding='utf-8')
            (run / 'manifest.json').write_text(json.dumps({'status': 'COMPLETE_UNGRADED', 'arm': 'B', 'question_file_sha256': hashlib.sha256(q.read_bytes()).hexdigest()}), encoding='utf-8')
            (run / 'SHA256SUMS.txt').write_text(''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n' for p in [stream, run / 'manifest.json']), encoding='utf-8')
            command = [sys.executable, str(Path(__file__).with_name('prepare_blind.py')), '--questions', str(q), '--run', 'B=' + str(run), '--output', str(base / 'packet')]
            result = subprocess.run(command, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn('SYNTHETIC UNIT TEST ONLY', (base / 'packet' / 'packet.md').read_text())
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0, 'Must refuse existing output')
            stream.write_text('tampered', encoding='utf-8')
            command[-1] = str(base / 'tampered-packet')
            self.assertNotEqual(subprocess.run(command, capture_output=True).returncode, 0, 'Must reject tampered capture')
            self.assertFalse((base / 'tampered-packet').exists())

if __name__ == '__main__':
    unittest.main()
