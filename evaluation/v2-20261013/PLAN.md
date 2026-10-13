# Corrected official v2 and U-series execution — pre-registration (committed before any call)

This plan covers two **separate evidence sets** run in this session. Nothing below is changed after outputs are seen; deviations are recorded as deviations. It does not alter the frozen U inputs or `evaluation/unseen-20261013/REVIEW-AND-RUN-PLAN.md`, which governs U-series scoring.

## Inputs (SHA-256 at freeze; verified by `verify_control_capture.py`, `verify_unseen.py`)
- v2 questions: `questions.md` `81df6185…4fe9`. Prompts: `control/prompt-manifest-v2.json` `79c94fa1…0ca4`.
  - Q4 is self-contained; Q1–Q3 and Q5–Q8 are byte-identical to v1.
  - **v2 was corrected after the original folder existed.** It is not original pre-registration.
- v2 key: `evaluation/expected-answers.md` `f67c927a…b832` (identical table to the root `questions.md`; Q4 gold unchanged).
- Rubric: `evaluation/scoring-rubric.md` `925dee9b…8d90`.
- U questions: `evaluation/unseen-20261013/external-questions.json` `b229c9fe…b2ae`.
- Specialist, fixture and rubric hashes are in `evaluation/unseen-20261013/input-manifest.json`. The specialist is unchanged since 3d9be31.

## Runs, order and tooling
Run sequentially, one attempt each, with `scripts/run_trials.py` from a fresh `git clone --no-local` of this commit (clean tree enforced). Each session sees only prompt bytes; gold answers, notes, plans, previous responses and scores never enter a session.

| Order | Set | Arm | Run ID | Command suffix |
|---|---|---|---|---|
| 1 | official v2 | A | `A_V2_01` | `--suite official` |
| 2 | official v2 | B | `B_V2_01` | `--suite official` |
| 3 | official v2 | C | `C_V2_01` | `--suite official` |
| 4 | U1–U8 | A | `A_U_01` | `--suite challenge --questions evaluation/unseen-20261013/external-questions.json` |
| 5 | U1–U8 | B | `B_U_01` | same |
| 6 | U1–U8 | C | `C_U_01` | same |

- **Arms:** A receives no files, B the frozen 10-file specialist, C only the six primary sources.
- **CLI:** Claude Code 2.1.288, native `claude.exe` SHA-256 `84304f7d…0ab91`. It is passed with `--claude` at its real MSIX path (see `REPRODUCE.md`).
- **Model:** `claude-opus-5-5` requested; observed IDs are taken from the captures. Flags are identical across arms (runner default).
- **Paths:**
  - v2: workspace `C:/paradox-v2-sessions`, output `C:/paradox-v2-captures`.
  - U: workspace `C:/paradox-u-sessions`, output `C:/paradox-u-captures`.
- **Order:** fixed (A, B, C) and not counterbalanced. This is disclosed as a limitation.
- **Failures:** the runner stops on any failure. The failed run folder is retained and committed, and a retry uses a new ID (`_02`). Every attempt is reported, and only complete attempts are scored.

## Before scoring
1. Run `scripts/review_fresh_captures.py` on every run. A session is excluded if it read any file outside its session folder or off its allowlist, or if any outside search returned content. Denied attempts and permitted-but-empty searches are reported, not excluded. Observed model IDs must equal the requested ID, or the deviation is disclosed.
2. Copy captures byte-for-byte to `evidence/v2-20261013/<RUN>/` and `evidence/unseen-20261013/<RUN>/`, checksum-verify them, and add root `control/README.md` / `treatment/README.md` pointers. Commit raw evidence and the review **before** any assessor packet exists.

## Scoring (frozen)
- **Official v2:**
  - Frozen rubric and v2 key. Evidence item uses the same rule as `evaluation/fresh-20261013/PLAN.md`: primary means any real section ID used correctly with no false ID (a `file:line` citation alone does not count); strict means a key-listed ID only. Both are reported.
  - False authorization is as defined by the rubric (Q4, Q8, and Q7 if a waiver is asserted).
  - Packet: shuffled, paths stripped, with mapping in a separate key file.
- **U-series:**
  - Exactly the "Frozen evaluation rules" of `REVIEW-AND-RUN-PLAN.md`, including the prospective U6/U8 both-readings criterion and the U8 24-hour-notice clarification.
  - Packet: `scripts/prepare_blind.py` (as the committed plan specifies).
  - Assessors receive `packet.md`, the rubric and the verbatim frozen-rules text. `mapping.json` is withheld.
  - Ambiguity-related deductions are recorded in a separate field.
- **Both sets:**
  - Two blinded assessor subagents per set, each seeing only its packet and instructions. Conflict disclosed: same model family as the tested model, the U-question author and the orchestrator.
  - Both score sets are preserved. Every disagreement is listed and adjudicated in writing against the rubric text.
  - Each score includes the category scores, capped total, conclusion_wrong, false_authorization, critical omissions, subpart notes and evidence_strict.
- **Reporting:**
  - Per-question category scores, totals, wins/ties/losses, false authorizations, omissions, ambiguity deductions, latency, failures and recognisable-arm disclosures.
  - A/B (folder vs no folder) and B/C (structure beyond sources) are kept distinct.
  - v1, v2 and U are separate evidence sets.
  - U1–U8 are described as generated in a separate Claude session from the primary documents (per the authoring note). There is no human, cross-family or moderator-accepted independence.
