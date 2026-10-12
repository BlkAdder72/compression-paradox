# Reproduce the official Competition #14 experiment

## Prerequisites

- A fresh Git clone of the committed repository and a Bash-compatible shell (Git Bash or WSL on Windows).
- Python 3.9+ and authenticated **Claude Code CLI 2.1.288**, if available. The original sessions identify model `claude-opus-5-5`. Model aliases may resolve to changed server weights or be unavailable at re-test time.
- An empty absolute run workspace **outside** the repository; no repository files or prior prompts mounted in the control workspace.
- The same model identifier, session flags and access permissions in A and B. The recorded CLI default system prompt and sampling parameters are not fully exportable or controllable; see `protocol.md` and `results.md`.

## Verify before any model call

```bash
python scripts/verify_stage3.py
python scripts/preflight_stage4.py
python scripts/verify_control_capture.py
python scripts/verify_stage4_capture.py --arm C --run-id CH1
python scripts/verify_stage4_capture.py --arm D --run-id DH1
python scripts/verify_stage4_capture.py --arm E --run-id EH1
```

`verify_fixture.py` is a historical *Stage 1-only* guard: it deliberately rejects repositories containing the completed specialist folder. Run it at commit `df36e7d`, not at HEAD. `verify_submission.py` is the final-state guard.

## Original A/B rerun, without overwriting original captures

The supplied scripts write directly under tracked `control/raw/` and `treatment/raw/`. **Use distinct new run IDs** and a clean clone for the rerun. Never reuse `A2`, `B1`, or any existing run ID; check that the output names do not exist before starting. Use a workspace directory containing no reference files for A.

```bash
export CLAUDE_BIN="$(command -v claude)"
export MODEL=claude-opus-5-5
export SANDBOX_BASE="$(mktemp -d)/sessions"
RUN_ID=A_REPRO_1 bash scripts/run_control_cli.sh
RUN_ID=B_REPRO_1 SRC_DIR=specialist OUT_DIR=treatment/raw bash scripts/run_arm_cli.sh
```

Both runners take Q1–Q8 in their listed order using isolated fresh CLI sessions with the same flags and user prompts. Their recorded output includes JSONL tool traces and stderr, but exact provider hidden prompts are not available. Save CLI version (`claude --version`), UTC timestamp, `git rev-parse HEAD`, and environment details separately. Do not edit output files. The runners currently log exit status but do **not** fail the entire script on a failed single question; inspect every run-log line and retain all failures.

**Warning:** A model may attempt external reads or rely on hidden environment context. Use the same tool permissions and record denials; reproduce from the repository root only where required, with per-question sessions starting inside isolated copied workspaces. If CLI aliases or access are different, report a reproduction limitation rather than claiming exact replication.

## Independent evaluation

Use `evaluation/scoring-rubric.md`, `evaluation/expected-answers.md`, and the raw output streams. Grade each response independently, ideally blind to arm labels, record the 0–10 category scores, and summarize wins, ties, losses, caveats, and disagreements. A scripted transcript integrity check is **not** an independently graded model reproduction. Distinguish B/A improvement from B/C incremental architecture benefit; A lacks source documents while B has them.

## Independently written unseen question

Have a third party who did **not** create the original questions or specialist inspect only the six primary `fixture/` documents, write one or more checkable questions and gold answers, and commit them **before** running the frozen treatment and control. Record authorship, hash, commit, time and any grader conflict. Do not call the existing H1–H8 'independent unseen questions'; they were written after initial A/B/C analysis.
