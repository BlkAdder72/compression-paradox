# Run manifest — Arm B (treatment, specialist folder), reproduction run B_REPRO_1

- Status: **EXECUTED** (single run, no retries; all 8 sessions exit=0, is_error=false; stderr empty)
- Reproduction of: the official Stage 2 A/B run, following `REPRODUCE.md` ("Original A/B rerun"). Original captures (A1, A2, B1) untouched.
- Repository state: fresh `git clone` of this repository at **d85a8b8** (d85a8b81a9a54285dfcb4f2e3c5e007caf09a4c2) into a scratch directory outside the Dropbox folder. Sessions ran from that clone. Raw files were then copied into this repository and checked against their SHA256 list.
- **Clone line endings:** Git for Windows here sets `core.autocrlf=true` system-wide. A default clone converted every text file to CRLF, and `verify_stage3.py` failed. The clone used for the run was made with `git clone -c core.autocrlf=false`, so prompts, fixture and specialist files are byte-identical to the committed versions. Gates passed in that clone: `verify_stage3.py`, `preflight_stage4.py`, `verify_control_capture.py` (8 prompts match frozen hashes), and `verify_stage4_capture.py` for CH1/DH1/EH1.
- **Case collision:** the repository tracks both `RESULTS.md` and `results.md`. On this case-insensitive filesystem only one can be checked out. This does not affect any file used by the runs.
- Provider / interface: Anthropic first-party, Claude Code CLI **2.1.288** (same build as A2/B1, bundled with the Claude desktop app, Windows 11), print mode, claude.ai OAuth login. Runners: unmodified `scripts/run_control_cli.sh` / `scripts/run_arm_cli.sh`.
- Model: `claude-opus-5-5` requested with `--model`; confirmed in every init event and every assistant message. Server-side revision unavailable. Temperature not adjustable; effort CLI default.
- Tools / flags: Read, Glob, Grep only; `--strict-mcp-config`; permission mode default; `--no-session-persistence`; one fresh session per question, Q1–Q8 in order, exact prompt bytes from `control/prompts/Qn.txt` on stdin.
- "Fresh environment" scope: each question ran in a new, non-persisted CLI session in a new directory under a newly created, previously nonexistent sandbox base (`<scratchpad>/repro-sessions/`). User-level Claude Code settings, plugins and skills were present, as in A2/B1 (listed in each init event). A separate Claude config directory was not used, because the bundled CLI then has no login (see A1). This is therefore not a clean-machine or clean-account reproduction.
- Environment: Windows 11 Pro 10.0.26300 · Git Bash (MINGW64, bash 5.3.15) · Python 3.13.14 · git 2.55.0.windows.1.
- Wall clock (UTC): A and B ran back to back, 2026-10-13T13:22:28Z–13:28:29Z. Per-question times are in the run log.
- Inaccessible: Claude Code default system prompt text (not in stream-json).
- Source exposure: `specialist/` (identity, rules, examples, README index and six reference copies) copied into each fresh session directory. No answer key, no repository.
- Observed tool behaviour: no permission denials. Files read were confined to the 10 specialist files (7–10 per session).
- Raw captures: `treatment/raw/B_REPRO_1-Qn.stream.jsonl`, `B_REPRO_1-Qn.stderr.txt`, `B_REPRO_1-run-log.txt`; checksums in `treatment/raw/B_REPRO_1-SHA256SUMS.txt`.
- Not yet scored.
