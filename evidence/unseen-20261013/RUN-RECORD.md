# Run record — U1–U8 (new runs)

Questions: `evaluation/unseen-20261013/external-questions.json` (SHA-256 `b229c9fe…b2ae`, frozen). Only each `prompt` field is sent; gold answers and critical requirements stay evaluator-only. U1–U8 were generated in a separate Claude session using the primary documents (per `AUTHORING-NOTE.md`). This is not independent human or cross-family authorship.

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
| A_U_01 | A (no folder) | 0 | 20:45:29–20:47:46 | all 0 | 13.6 s | 0 |
| B_U_01 | B (specialist) | 10 | 20:47:47–20:51:07 | all 0 | 21.7 s | 6–10 |
| C_U_01 | C (sources only) | 6 | 20:51:08–20:54:36 | all 0 | 22.6 s | 6 |

## Contamination review (`tool-access-review.txt`): all three runs CLEAN
- Only allowlisted files were present (`session-workspace-listing.txt`: A 0, B 80, C 48) and read.
- **A:** 8 denied searches of its run folder `C:/paradox-u-sessions/A_U_01` (one per question), all blocked. In U8, A also globbed Claude Code's own per-session auto-memory folder; it was permitted, returned "No files found", and gave no content.
- **B and C:** no denials, no notes.
