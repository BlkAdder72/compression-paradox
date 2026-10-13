# treatment/ — where the raw treatment evidence is

Arm B — `specialist/` folder (treatment). Every transcript is the unedited Claude Code `stream-json` stdout: init event with model and tools, every tool call and result, and the final answer. Next to each are stderr, `manifest.json` (prompt and source hashes, revision, CLI version, command, timestamps, exits) and `SHA256SUMS.txt`. Scores and comparisons are in the root `results.md`.

| Run ID | Location | Questions | Note |
|---|---|---|---|
| B1 | `treatment/raw/B1-Q*` | v1 | Original official treatment, 80/80 |
| B_REPRO_1 | `treatment/raw/B_REPRO_1-Q*` | v1 | Imported rerun, 80/80 |
| B_FRESH_20261013_01 | `evidence/fresh-20261013/B_FRESH_20261013_01/` | v1 | Fresh rerun, 80/80 |
| B_V2_01 | `evidence/v2-20261013/B_V2_01/` | **v2 (current)** | Corrected official v2 |
| B_U_01 | `evidence/unseen-20261013/B_U_01/` | U1–U8 | Separate-session questions |

**Exact prompts.**
- Current v2: `control/prompts-v2/Q1–Q8.txt`, hashed in `control/prompt-manifest-v2.json`, and the text of the root `questions.md`.
- Original v1: `control/prompts/`, hashed in `control/prompt-manifest.json`, archived in `history/questions-v1.md`.
- U-series: the `prompt` fields of `evaluation/unseen-20261013/external-questions.json`.
- Every new-run `manifest.json` also records the SHA-256 of each prompt actually sent.

**Re-run:** see `REPRODUCE.md`. Example: `python scripts/run_trials.py --suite official --arm B --run-id <new ID> --workspace <abs dir> --output <abs dir> --claude <claude.exe>`. The source-only diagnostic arm C is under `evidence/*/C_*` and `diagnostics/source-only/raw/`.
