# Run record — corrected official v2 (new runs; separate from v1, fresh v1 rerun and imported records)

Questions: root `questions.md` v2 (Q4 self-contained; Q1–Q3, Q5–Q8 byte-identical to v1), prompts `control/prompts-v2/`. v2 was corrected after the original folder existed.

- Revision executed: **ef4450074e4d53ce532791b25b61bbec4e23eb8a** (pre-registration `evaluation/v2-20261013/PLAN.md`), from a fresh `git clone --no-local` with a clean tree (enforced by the runner). Received package HEAD was `4b499ac`; preflight checks, `verify_unseen.py`, `git fsck --full` and JSON validation all passed on it before any call.
- Runner: unmodified `scripts/run_trials.py`. Per session: `claude -p --model claude-opus-5-5 --output-format stream-json --verbose --tools Read,Glob,Grep --strict-mcp-config --no-session-persistence --permission-mode default`, prompt bytes on stdin. Prompt and source SHA-256 values are in each `manifest.json`.
- CLI: Claude Code **2.1.288**, native Windows `claude.exe` (SHA-256 `84304f7d4b0cd0ebcbe8318695a260151b48991a6659c3366fdd5da290c0ab91`), passed at its real MSIX path. Authenticated claude.ai login. This is the same binary and configuration for every arm, and the same as the 2026-10-13 fresh runs.
- **Model:** requested `claude-opus-5-5`; **observed `claude-opus-5-5`** in every init event and every assistant message. The server revision is not observable.
- Environment: Windows 11 Pro 10.0.26300, NTFS, Python 3.13.14, Git 2.55.0.windows.1, Git Bash.
- **Failures and retries:** none. Every run completed on its first attempt (all exits 0, 8/8 success events, stderr empty). Order was fixed, A then B then C, and not counterbalanced.
- Raw evidence (stdout streams with full tool traces, stderr, manifest, checksums) was copied byte-for-byte from the external output folder and checksum-verified. It was committed **before** any assessor packet or score.
- **Inherited configuration (disclosed):** user-level Claude Code settings, plugins and skills were present, as listed in init events. Directory separation is not OS isolation.

| Run | Arm | Files per session | UTC | Exits | Mean wall time | Reads/session |
|---|---|---|---|---|---|---|
| A_V2_01 | A (no folder) | 0 | 20:37:45–20:39:58 | all 0 | 13.1 s | 0 |
| B_V2_01 | B (specialist) | 10 | 20:39:59–20:42:57 | all 0 | 18.9 s | 7–10 |
| C_V2_01 | C (sources only) | 6 | 20:42:58–20:45:28 | all 0 | 15.3 s | 6 |

## Contamination review (`tool-access-review.txt`): all three runs CLEAN
- Only allowlisted files were present (`session-workspace-listing.txt`: A 0, B 80, C 48) and read.
- **A:** 7 denied searches of its run folder `C:/paradox-v2-sessions/A_V2_01` (Q2–Q8), all blocked. In 5 sessions, A also globbed Claude Code's own per-session auto-memory folder. This was permitted, returned "No files found", and gave no content.
- **B and C:** no denials, no notes.
