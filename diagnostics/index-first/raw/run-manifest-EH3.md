# Run manifest — Arm E / H-series run EH3 (clean repeat; replaces excluded run 2)

- Status: **EXECUTED** (single run, no retries, no failures; all 8 sessions exit=0)
- Git commit at execution: b3d2417 (arm folders restored to frozen contents; preflight rejects extra files). Preflight gates passed immediately before running: `verify_stage3.py`, `preflight_stage4.py`, `bash -n scripts/run_holdout_cli.sh`.
- Prompts: diagnostics/holdout-prompts/H1–H8.txt, SHA256-verified against manifest.json by preflight; delivered as exact bytes on stdin, no added instructions.
- Provider / interface: Anthropic first-party, Claude Code CLI **2.1.288** (bundled with the Claude desktop app, Windows 11; same build as Stage 2), print mode, claude.ai OAuth login. Runner: `scripts/run_holdout_cli.sh` (unmodified).
- Model: `claude-opus-5-5` requested with `--model`; confirmed in every init event and every assistant message. Server-side revision unavailable. Temperature not adjustable; effort CLI default; fast mode off.
- Tools: Read, Glob, Grep only; `--strict-mcp-config` (no MCP); permission mode default; `--no-session-persistence`. Permission denials: **none** in any of the 8 sessions.
- Source exposure: README.md (index) and reference/ (six byte-identical fixture copies) copied from `diagnostics/index-first` into each fresh empty session directory (`<scratchpad>/stage4/EH3-Hn`, outside the repository). No answer key, no repository, no prior raw output.
- Session strategy: eight fresh independent sessions, H1–H8 in order, run sequentially (D, then E, then C).
- Timestamps (UTC): per-question start/end in `EH3-run-log.txt`.
- Raw captures: `EH3-Hn.stream.jsonl`, `EH3-Hn.stderr.txt` (all stderr empty); checksums in `EH3-SHA256SUMS.txt`. `verify_stage4_capture.py --arm E --run-id EH3`: PASS.
- Inaccessible: Claude Code default system prompt text (not included in stream-json).
