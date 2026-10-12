#!/usr/bin/env bash
# Generic arm runner (treatment / diagnostics). Identical CLI flags to run_control_cli.sh;
# the ONLY difference is that each fresh session's empty directory is first populated with
# a copy of $SRC_DIR (e.g. specialist/ or fixture/). Raw outputs saved unedited.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE="${CLAUDE_BIN:?}"; MODEL="${MODEL:-claude-opus-5-5}"
SANDBOX_BASE="${SANDBOX_BASE:?}"; RUN_ID="${RUN_ID:?}"; SRC_DIR="${SRC_DIR:?}"; OUT_DIR="${OUT_DIR:?}"
mkdir -p "$ROOT/$OUT_DIR"
for n in 1 2 3 4 5 6 7 8; do
  q="Q$n"; dir="$SANDBOX_BASE/$RUN_ID-$q"; mkdir -p "$dir"; cp -r "$ROOT/$SRC_DIR/." "$dir/"
  out="$ROOT/$OUT_DIR/$RUN_ID-$q.stream.jsonl"; err="$ROOT/$OUT_DIR/$RUN_ID-$q.stderr.txt"
  start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  ( cd "$dir" && "$CLAUDE" -p --model "$MODEL" --output-format stream-json --verbose \
      --tools "Read,Glob,Grep" --strict-mcp-config --no-session-persistence \
      --permission-mode default < "$ROOT/control/prompts/$q.txt" ) > "$out" 2> "$err"
  rc=$?
  echo "$RUN_ID $q start=$start end=$(date -u +%Y-%m-%dT%H:%M:%SZ) exit=$rc" | tee -a "$ROOT/$OUT_DIR/$RUN_ID-run-log.txt"
done
