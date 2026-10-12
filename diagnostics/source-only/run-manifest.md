# Run manifest — Arm C / source-only diagnostic

- Status: **EXECUTED** (run C1, single run, no retries, no failures)
- Git commit at execution: 0bcffb9 (specialist committed at 3d9be31; arm C predefined at 0bcffb9)
- Frozen questions SHA256: f00c77be592a206fd2bbf2d1dfd574168eaa2bfa203e44745b69c5e542675f41
- Provider / interface / model / settings / tools / session strategy: **identical to Arm A run A2** (see control/run-manifest.md): Claude Code CLI 2.1.288 print mode, `claude-opus-5-5`, tools Read/Glob/Grep only, no MCP, permission mode default, `--no-session-persistence`, one fresh session per question, exact prompt bytes on stdin. Runner: scripts/run_arm_cli.sh.
- Source exposure: the six fixture/*.md files only, copied into each fresh session directory; no specialist files, no answer key, no repository.
- Timestamp: 2026-10-12, start/end per question (UTC) in diagnostics/source-only/raw/C1-run-log.txt. Arms B and C ran concurrently.
- Raw captures: diagnostics/source-only/raw/C1-Qn.stream.jsonl, C1-Qn.stderr.txt; checksums in diagnostics/source-only/raw/SHA256SUMS.txt.
- Permission denials: Q4 attempted one Glob of the parent directory; denied. No other denials.
- Inaccessible: Claude Code system prompt text (not in stream-json).
