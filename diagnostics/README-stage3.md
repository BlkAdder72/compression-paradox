# Stage 3 pre-registered compression ablation (supplemental, not official A/B)

Status: constructed in Stage 3; **executed in Stage 4 (DH1, EH1, CH1), see `RESULTS.md`**. Historical A/B/C transcript scores remain unchanged.

- **D — aggressive-summary**: short threshold-oriented `SUMMARY.md` and permissive `README.md` plus byte-identical full source documents. The short summary intentionally omits qualifications; source can still be consulted.
- **E — index-first**: an index that identifies topic-to-section locations, emphasizes primary source verification and exact citations, plus byte-identical full source documents.
- **C — source-only**: six unchanged fixture documents. Its original C1 single-run result is 78/80; an H-series source-only diagnostic is needed for a fair holdout comparison.

Hypothesis, registered before any D/E or H runs: E will preserve condition coverage more consistently than D on boundary and cross-policy cases, but may take longer or open more files. This may be falsified by results. No improvement is claimed before running the model.

All H1–H8 questions, expected answers, and source citations live in `evaluation/holdout/`. They were authored after initial A/B/C results, so are **not independent blind holdouts**. Call them *supplemental post-analysis challenge questions*; an independently authored, later committed blind set is still desirable. Their answers must not be shown to the model.

## Execution and controls

Before runs, verify `python scripts/verify_stage3.py` and `bash -n scripts/run_holdout_cli.sh`. In a Claude Code environment with the same executable/model/settings as Stage 2, set:
```
export CLAUDE_BIN="$(command -v claude)"
export MODEL=claude-opus-5-5
export SANDBOX_BASE=/tmp/compression-paradox-stage3
RUN_ID=DH1 SRC_DIR=diagnostics/aggressive-summary OUT_DIR=diagnostics/aggressive-summary/raw bash scripts/run_holdout_cli.sh
RUN_ID=EH1 SRC_DIR=diagnostics/index-first OUT_DIR=diagnostics/index-first/raw bash scripts/run_holdout_cli.sh
RUN_ID=CH1 SRC_DIR=fixture OUT_DIR=diagnostics/source-only/raw bash scripts/run_holdout_cli.sh
```
Use unique `CH1-*` filenames; existing `C1-*` captures remain untouched. Each run must be assigned an empty source-isolated session directory and a unique run ID.

C and D/E H runs must use the same eight exact prompts and independent fresh sessions. Capture model alias/version, CLI, permission behavior, start/end time, and all raw outputs. Running the original eight Q questions for D/E is optional and must be labeled post-hoc because variants were developed after seeing those answers.

Only score after transcripts exist, using frozen answer key and rubric. Report question-level wins/ties/losses and all failures/denials, not just totals.

## Stage 4 safety gates (added after the Stage 3 precommit)

Run the following before calling Claude:

```bash
python scripts/verify_stage3.py
python scripts/preflight_stage4.py
bash -n scripts/run_holdout_cli.sh
```

After each genuine run, run the matching capture verifier:

```bash
python scripts/verify_stage4_capture.py --arm D --run-id DH1
python scripts/verify_stage4_capture.py --arm E --run-id EH1
python scripts/verify_stage4_capture.py --arm C --run-id CH1
```

These checks validate files, JSON framing and recorded process exits; they do **not** independently prove model identity or adjudicate response accuracy. Verify the runner's real model alias and permission behavior before publication. Do not share answer-key files with the model during runs. Preserve any unsuccessful model output, record the error, and do not replace it under the same run ID.
