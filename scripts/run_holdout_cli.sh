#!/usr/bin/env bash
# Supplemental H-series runs, saved verbatim. Requires genuine Claude CLI access.
# e.g. CLAUDE_BIN="$(command -v claude)" SANDBOX_BASE=/tmp/paradox MODEL=claude-opus-5-5 \
#      RUN_ID=DH1 SRC_DIR=diagnostics/aggressive-summary OUT_DIR=diagnostics/aggressive-summary/raw \
#      bash scripts/run_holdout_cli.sh
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLAUDE="${CLAUDE_BIN:?required}"; MODEL="${MODEL:-claude-opus-5-5}"
SANDBOX_BASE="${SANDBOX_BASE:?required}"; RUN_ID="${RUN_ID:?required}"
SRC_DIR="${SRC_DIR:?required}"; OUT_DIR="${OUT_DIR:?required}"
case "$SRC_DIR" in
  diagnostics/aggressive-summary|diagnostics/index-first|fixture) ;;
  *) echo "Unsupported source directory: $SRC_DIR" >&2; exit 2 ;;
esac
case "$OUT_DIR" in
  diagnostics/*/raw) ;;
  *) echo "Unsupported output directory: $OUT_DIR" >&2; exit 2 ;;
esac
mkdir -p "$ROOT/$OUT_DIR" "$SANDBOX_BASE"
for n in 1 2 3 4 5 6 7 8; do
  q="H$n"; dir="$SANDBOX_BASE/$RUN_ID-$q"
  if [ -e "$dir" ]; then echo "REFUSE existing session directory $dir" >&2; exit 3; fi
  mkdir -p "$dir"
  cp -r "$ROOT/$SRC_DIR/." "$dir/"
  # Never expose staged answer keys or raw previous model outputs.
  rm -rf "$dir/raw"
  out="$ROOT/$OUT_DIR/$RUN_ID-$q.stream.jsonl"
  err="$ROOT/$OUT_DIR/$RUN_ID-$q.stderr.txt"
  if [ -e "$out" ] || [ -e "$err" ]; then echo "REFUSE overwrite $out" >&2; exit 4; fi
  start=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  ( cd "$dir" && "$CLAUDE" -p --model "$MODEL" --output-format stream-json --verbose \
       --tools "Read,Glob,Grep" --strict-mcp-config --no-session-persistence \
       --permission-mode default < "$ROOT/diagnostics/holdout-prompts/$q.txt" ) > "$out" 2> "$err"
  rc=$?
  printf '%s %s start=%s end=%s exit=%s\n' "$RUN_ID" "$q" "$start" \
    "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$rc" >> "$ROOT/$OUT_DIR/$RUN_ID-run-log.txt"
  if [ "$rc" -ne 0 ]; then echo "Model run failed at $q (exit $rc), preserving raw records" >&2; exit "$rc"; fi
done
