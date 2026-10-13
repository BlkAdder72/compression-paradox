#!/usr/bin/env python3
"""Local regression tests only. Test stubs are NOT Claude model evidence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import run_trials as runner

class RunnerTests(unittest.TestCase):
    def test_exact_sources(self):
        for arm, expected in [('A', 0), ('B', 10), ('C', 6), ('D', 8), ('E', 7)]:
            files = runner.source_files(arm)
            self.assertEqual(len(files), expected)
            self.assertTrue(all(p.is_file() and 'raw' not in name and 'expected' not in name for p, name in files))

    def test_terminal_result_validation(self):
        with tempfile.TemporaryDirectory() as folder:
            p = Path(folder) / 'UNIT-TEST-ONLY.jsonl'
            for events, expected in [([], False), ([{'type': 'result', 'subtype': 'error', 'is_error': True}], False), ([{'type': 'result', 'subtype': 'success', 'is_error': False}], True)]:
                p.write_text('\n'.join(json.dumps(e) for e in events), encoding='utf-8')
                self.assertEqual(runner.successful_stream(p), expected)

    def test_refuse_existing_run_and_invalid_id(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / 'out' / 'EXISTS').mkdir(parents=True)
            for run_id in ['EXISTS', '../unsafe']:
                p = subprocess.run([sys.executable, str(Path(runner.__file__)), '--arm', 'A', '--run-id', run_id,
                                    '--workspace', str(base / 'sessions'), '--output', str(base / 'out'), '--dry-run'], capture_output=True)
                self.assertNotEqual(p.returncode, 0)
            self.assertFalse((base / 'sessions').exists())

    def test_dry_run_never_calls_provider(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            args = ['runner', '--arm', 'B', '--run-id', 'TEST', '--workspace', str(base / 'sessions'), '--output', str(base / 'out'), '--dry-run']
            with patch.object(sys, 'argv', args), patch.object(runner.shutil, 'which', side_effect=AssertionError('provider called')):
                runner.main()
            self.assertFalse((base / 'out').exists())

if __name__ == '__main__':
    unittest.main()
