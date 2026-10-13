# Current Claude Projects UI control

Actual rendered UI captures and exact prompts: [raw/A_UI_01/](raw/A_UI_01/). Complete ungraded evidence was committed at 5f52b52 before assessment. Identical copies live in evidence/projects-20261013/A_UI_01; each response is scored once. These are visible UI captures, not provider stream-json. See root results.md and the UI completion record for recovery and access limits.

The following section indexes the separate earlier CLI evidence; its stream-json descriptions apply to CLI files only.

---

# Current seven-question control

Current raw run: [`raw/A_SEVEN_01/`](raw/A_SEVEN_01/), including unedited stream-json, stderr, manifest and checksums. Exact prompts: `control/prompts-seven/` from repository root (Q1,Q2,Q3,Q5,Q6,Q7,Q8). These are byte-identical to the original pre-folder prompts. See root questions.md, results.md and REPRODUCE.md. Default --suite official executes seven; --suite official-v2 is the historical corrected eight-question set.

The identical evidence copy is evidence/seven-20261013/A_SEVEN_01/. Only one copy is scored. The following index preserves earlier evidence; references there to current v2 describe the earlier release, not the current seven-question benchmark.

---

# control/ — where the raw control evidence is

Arm A — no folder (control). Every transcript is the unedited Claude Code `stream-json` stdout: init event with model and tools, every tool call and result, and the final answer. Next to each are stderr, `manifest.json` (prompt and source hashes, revision, CLI version, command, timestamps, exits) and `SHA256SUMS.txt`. Scores and comparisons are in the root `results.md`.

| Run ID | Location | Questions | Note |
|---|---|---|---|
| A1 | `control/raw/A1-Q*` | v1 | Failed: CLI not logged in (retained) |
| A2 | `control/raw/A2-Q*` | v1 | Original official control, scored 11/80 |
| A_REPRO_1 | `control/raw/A_REPRO_1-Q*` | v1 | Imported rerun, 11/80 |
| A_FRESH_20261013_01 | `evidence/fresh-20261013/A_FRESH_20261013_01/` | v1 | Fresh rerun, 16/80 |
| A_V2_01 | `evidence/v2-20261013/A_V2_01/` | v2 (historical) | Corrected official v2 |
| A_U_01 | `evidence/unseen-20261013/A_U_01/` | U1–U8 | Separate-session questions |

**Exact prompts.**
- Historical v2: `control/prompts-v2/Q1–Q8.txt`, hashed in `control/prompt-manifest-v2.json`, and the text of the root `questions.md`.
- Original v1: `control/prompts/`, hashed in `control/prompt-manifest.json`, archived in `history/questions-v1.md`.
- U-series: the `prompt` fields of `evaluation/unseen-20261013/external-questions.json`.
- Every new-run `manifest.json` also records the SHA-256 of each prompt actually sent.

**Re-run:** see `REPRODUCE.md`. Example: `python scripts/run_trials.py --suite official --arm A --run-id <new ID> --workspace <abs dir> --output <abs dir> --claude <claude.exe>`. The source-only diagnostic arm C is under `evidence/*/C_*` and `diagnostics/source-only/raw/`.
