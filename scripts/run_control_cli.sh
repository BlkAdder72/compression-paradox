#!/usr/bin/env bash
# Arm A (no-folder control) runner. Each question = one fresh, non-persisted Claude Code
# print-mode session started in its own EMPTY directory outside the repository.
# Raw stdout (stream-json events) and stderr are saved unedited. Never edit outputs.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE="${CLAUDE_BIN:?set CLAUDE_BIN to claude executable}"
MODEL="${MODEL:-claude-opus-5-5}"
SANDBOX_BASE="${SANDBOX_BASE:?set SANDBOX_BASE to an empty dir outside the repo}"
RUN_ID="${RUN_ID:-A1}"
for n in 1 2 3 4 5 6 7 8; do
  q="Q$n"; dir="$SANDBOX_BASE/$RUN_ID-$q"; mkdir -p "$dir"
  out="$ROOT/control/raw/$RUN_ID-$q.stream.jsonl"; err="$ROOT/control/raw/$RUN_ID-$q.stderr.txt"
  start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  ( cd "$dir" && "$CLAUDE" -p --model "$MODEL" --output-format stream-json --verbose \
      --tools "Read,Glob,Grep" --strict-mcp-config --no-session-persistence \
      --permission-mode default < "$ROOT/control/prompts/$q.txt" ) > "$out" 2> "$err"
  rc=$?
  echo "$RUN_ID $q start=$start end=$(date -u +%Y-%m-%dT%H:%M:%SZ) exit=$rc" | tee -a "$ROOT/control/raw/$RUN_ID-run-log.txt"
done
