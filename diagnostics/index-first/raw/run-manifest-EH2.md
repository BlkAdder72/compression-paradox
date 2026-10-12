# Run manifest — Arm E / H-series run EH2 (repeat run 2)

- Status: **EXECUTED but EXCLUDED from scoring: source-exposure deviation** (all 8 sessions exit=0; records retained unedited)
- Git commit at execution: 15e239c (after Stage 4 run-1 scoring; runner, prompts and arm folders unchanged since 206da8e). Preflight gates passed immediately before running: `verify_stage3.py`, `preflight_stage4.py`, `bash -n scripts/run_holdout_cli.sh`.
- Prompts: diagnostics/holdout-prompts/H1–H8.txt, SHA256-verified against manifest.json by preflight; delivered as exact bytes on stdin, no added instructions.
- Provider / interface: Anthropic first-party, Claude Code CLI **2.1.288** (bundled with the Claude desktop app, Windows 11; same build as Stage 2), print mode, claude.ai OAuth login. Runner: `scripts/run_holdout_cli.sh` (unmodified).
- Model: `claude-opus-5-5` requested with `--model`; confirmed in every init event and every assistant message. Server-side revision unavailable. Temperature not adjustable; effort CLI default; fast mode off.
- Tools: Read, Glob, Grep only; `--strict-mcp-config` (no MCP); permission mode default; `--no-session-persistence`. Permission denials: **none** in any of the 8 sessions.
- Source exposure: README.md (index) and reference/ (six byte-identical fixture copies) copied from `diagnostics/index-first` into each fresh empty session directory (`<scratchpad>/stage4/EH2-Hn`, outside the repository). No answer key, no repository, no prior raw output.
- Session strategy: eight fresh independent sessions, H1–H8 in order, run sequentially (D, then E, then C).
- Timestamps (UTC): per-question start/end in `EH2-run-log.txt`.
- Raw captures: `EH2-Hn.stream.jsonl`, `EH2-Hn.stderr.txt` (all stderr empty); checksums in `EH2-SHA256SUMS.txt`. `verify_stage4_capture.py --arm E --run-id EH2`: PASS.
- Inaccessible: Claude Code default system prompt text (not included in stream-json).
- Verifier note: `verify_stage4_capture.py` initially reported CH2-H6 as malformed because it decoded files with the Windows default code page (cp1252). The capture is valid UTF-8 (PASS with PYTHONUTF8=1). The verifier was fixed to read UTF-8 explicitly; all six H-series runs pass. Raw files were not touched.
- **Deviation (operator error):** the run-1 manifest `run-manifest-EH1.md` had been saved inside the arm folder, which the runner copies into every session. Sessions opened it (see the Read calls in the stream). It contained run settings only, with no answers, gold key or scores. Exposure still differed from run 1, so this run is not a valid repeat and is not scored. Manifests now live in `raw/` (stripped by the runner), and `preflight_stage4.py` rejects any extra file in arm folders. The clean repeat is run EH3.
