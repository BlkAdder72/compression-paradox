#!/usr/bin/env bash
# Delegate to the cross-platform capture runner; existing evidence is never overwritten.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
exec "${PYTHON_BIN:-python}" "$ROOT/scripts/run_trials.py" --arm "${ARM:?set ARM to C D or E}" --suite holdout --run-id "${RUN_ID:?required}" --workspace "${SANDBOX_BASE:?required}" --output "${OUTPUT_BASE:?required}" --claude "${CLAUDE_BIN:-claude}" --model "${MODEL:-claude-opus-5-5}" "$@"
