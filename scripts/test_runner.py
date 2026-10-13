#!/usr/bin/env python3
"""Local regression tests only. Test stubs are NOT Claude model evidence."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import contextlib
import io
from unittest.mock import patch
import run_trials as runner

class RunnerTests(unittest.TestCase):
    def test_official_excludes_only_q4(self):
        current = runner.prompts('official')
        legacy = dict(runner.prompts('legacy'))
        corrected = dict(runner.prompts('official-v2'))
        self.assertEqual([q for q, _ in current], ['Q1','Q2','Q3','Q5','Q6','Q7','Q8'])
        self.assertEqual(len(corrected), 8)
        for q, prompt in current:
            self.assertEqual(prompt, legacy[q])
            self.assertEqual(prompt, corrected[q])
        self.assertNotEqual(legacy['Q4'], corrected['Q4'])

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

    def test_capture_success_failure_timeout_and_malformed(self):
        # In-memory process stub only; temporary files are deleted by TemporaryDirectory.
        # These are runner regression tests, never saved as competition evidence.
        for mode in ['success', 'failed', 'timeout', 'malformed']:
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as folder:
                base = Path(folder)
                args = ['runner', '--arm', 'A', '--run-id', 'UNIT_TEST_ONLY', '--workspace', str(base / 'sessions'), '--output', str(base / 'out')]
                def check_output(command, **kwargs):
                    if '--version' in command:
                        return 'UNIT TEST STUB'
                    if 'status' in command:
                        return b''
                    return 'UNIT_TEST_REVISION'
                def process(command, **kwargs):
                    self.assertEqual(list(Path(kwargs['cwd']).iterdir()), [])
                    if mode == 'timeout':
                        kwargs['stdout'].write(b'{"type":"UNIT_TEST_ONLY"}\n')
                        raise subprocess.TimeoutExpired(command, 1)
                    payload = b'NOT JSON' if mode == 'malformed' else json.dumps({'type': 'result', 'subtype': 'success' if mode == 'success' else 'error', 'is_error': mode != 'success', 'result': 'UNIT TEST ONLY'}).encode() + b'\n'
                    kwargs['stdout'].write(payload)
                    return subprocess.CompletedProcess(command, 0 if mode != 'failed' else 1)
                with patch.object(sys, 'argv', args), patch.object(runner.shutil, 'which', return_value='UNIT_TEST_STUB'), patch.object(runner.subprocess, 'check_output', side_effect=check_output), patch.object(runner.subprocess, 'run', side_effect=process), contextlib.redirect_stdout(io.StringIO()):
                    if mode == 'success':
                        runner.main()
                    else:
                        with self.assertRaises(SystemExit):
                            runner.main()
                out = base / 'out' / 'UNIT_TEST_ONLY'
                manifest = json.loads((out / 'manifest.json').read_text())
                self.assertEqual(manifest['status'], 'COMPLETE_UNGRADED' if mode == 'success' else 'FAILED_OR_INTERRUPTED')
                self.assertEqual(len(manifest['records']), 7 if mode == 'success' else 1)
                self.assertTrue((out / 'Q1.stream.jsonl').exists())
                self.assertTrue((out / 'SHA256SUMS.txt').exists())

if __name__ == '__main__':
    unittest.main()
