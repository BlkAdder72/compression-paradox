# Fresh verification runs 2026-10-13 — pre-registration (frozen before any model call)

Committed before any fresh model call in this verification pass. Nothing below is changed after outputs are seen. Any deviation is recorded as a deviation.

## Distinguish from imported records
These runs are **new**. They are not the imported `A_REPRO_1` / `B_REPRO_1` records, nor any earlier A1/A2/B1/C1/CH*/DH*/EH* run. Those remain unchanged. New evidence lives only under `evidence/fresh-20261013/<RUN_ID>/`.

## Runs, order and tooling
Run sequentially in this order, one attempt each, using `scripts/run_trials.py` from a fresh `git clone --no-local` of this commit:

| Order | Suite | Arm | Run ID | Exposure |
|---|---|---|---|---|
| 1 | official Q1–Q8 | A | `A_FRESH_20261013_01` | no files |
| 2 | official Q1–Q8 | B | `B_FRESH_20261013_01` | 10 specialist files |
| 3 | official Q1–Q8 | C | `C_FRESH_20261013_01` | 6 fixture sources |
| 4 | holdout H1–H8 | C | `CH_FRESH_01` | 6 fixture sources |
| 5 | holdout H1–H8 | D | `DH_FRESH_01` | README + SUMMARY + 6 references |
| 6 | holdout H1–H8 | E | `EH_FRESH_01` | index README + 6 references |

- CLI: the installed, authenticated Claude Code CLI, a native Windows executable passed with `--claude`. Model requested: `claude-opus-5-5` (runner default). The actual CLI version and model IDs are taken from the captures.
- Session workspace: `C:/paradox-sessions-20261013`. Raw output: `C:/paradox-captures-20261013`. Both are outside the repository and are separate roots.
- One round only, so order is not counterbalanced. This is disclosed as a limitation.
- **Failure handling:** if a run stops (non-zero exit, timeout or missing success event), its folder is retained unedited and committed. One retry may be made under the suffix `_02`. Both attempts are reported, and only a complete attempt is scored.

## Contamination review (before scoring)
For every session, list every tool call, read path and permission denial. A session is excluded if it read any file other than its arm's allowlisted copies, or if any outside access succeeded. Denied attempts are reported but do not exclude a session. Actual model IDs must be `claude-opus-5-5` in the init event and every assistant message, or the deviation is disclosed.

## Evidence before scoring
The raw run folders (stdout streams, stderr, `manifest.json`, `SHA256SUMS.txt`) are copied byte-for-byte into `evidence/fresh-20261013/`, checksum-verified, and committed **before** any assessor packet is built.

## Scoring (frozen)
- Rubric and keys, unchanged, with SHA-256 at freeze:
  - `evaluation/scoring-rubric.md` `925dee9b17d61cfc21ae30ff5f44a625d85c52f0f32627013131079dc46a8d90`
  - `evaluation/expected-answers.md` `f67c927a339fa7e149e2ceaf281270e1ae746fa14988b3472d2777d53688b832`
  - `evaluation/holdout/expected-answers.md` `744258cc2f6584603d0c48b383616bb3569c1cc707ea5dd418c71abcf2de0e3f`
  - Questions: `questions.md` `f00c77be…5f41` and `evaluation/holdout/questions.md` `336657ae…3d94`.
- **Evidence item (ambiguity resolved before scoring).** Earlier assessors read "correct section identifier" differently. For this pass:
  - **Primary:** any section ID that exists in the fixture and is used correctly, as long as no false ID appears. A `file:line` citation alone is not a section identifier.
  - **Strict:** only IDs from the key's evidence or controlling list. Strict totals are reported alongside.
- **H-series false authorization:** the same mapping as Stage 4. A response is flagged if it omits a required pre-purchase approval, or wrongly asserts a waiver or that compliance was achieved.
- **Packets:** two blinded packets, official (24 responses: A/B/C) and holdout (24 responses: C/D/E). Each is shuffled with a seed recorded in its key, and directory paths are stripped from response text. The arm mapping is kept outside the assessor's view.
- **Assessors:** two independent assessor subagents per packet, each seeing only the packet. Disclosed conflict: both are the same model family as the tested model and as the orchestrating agent. They are not independent humans. Every disagreement is listed and adjudicated by the orchestrating agent against the rubric text, with written reasons, and both raw score sets are kept.
- **Reporting:** per-question category scores, totals, wins/ties/losses (B vs A, C vs A, B vs C on the official set; pairwise on H), critical omissions, false authorizations, transparent uncertainty, recognisable-arm disclosures and exclusions. A/B is reported as confounded by source availability, and B/C is the architecture comparison.

## Not in scope of this pass
- G1–G4 (`evaluation/challenge/`) are not executed. They remain generated and non-independent.
- No external author is available, so no independent unseen questions exist.
