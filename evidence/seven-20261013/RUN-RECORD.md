# Fresh seven-question execution — 2026-10-13

Input commit: 4f0c0b806547c33da45c5f986479b0718493f287, committed and pushed before calls. Runs A_SEVEN_01, B_SEVEN_01, C_SEVEN_01, fixed A/B/C order; 7 sessions per run, exact retained question IDs and prompt bytes in manifest. CLI 2.1.288; requested and observed claude-opus-5-5. 21/21 success events, exit 0, no retries. Same native CLI/account configuration and flags in all arms. Working directory separation is not OS isolation; inherited user configuration persists.

Session root: C:/Users/mmazu/AppData/Local/Temp/cp14-seven-sessions-20261013
Capture root: C:/Users/mmazu/AppData/Local/Temp/cp14-seven-captures-20261013

Each run used python scripts/run_trials.py --suite official --arm ARM --run-id ARM_SEVEN_01 --workspace SESSION_ROOT --output CAPTURE_ROOT --claude the native executable recorded in manifest. Exact commands, prompt/source hashes, UTC timestamps and exits are captured. Tool-review JSON and actual session file hashes accompany the untouched captures. A's failed nonexistent-memory read is disclosed in REVIEW-DISPOSITION.md.

Copies in root control/raw/A_SEVEN_01 and treatment/raw/B_SEVEN_01 are byte-identical to these evidence copies. Only one copy per answer is scored. Raw evidence is committed before any grading; no scores are part of this capture commit. Seven-item benchmark and answer key were frozen in 4f0c0b8; original content dates to df36e7d. No specialist changes. Original Q4 and all old runs remain untouched.
