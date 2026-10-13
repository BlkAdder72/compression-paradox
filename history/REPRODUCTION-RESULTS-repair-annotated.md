> Repair clarification (2026-10-13): This is an imported earlier-run report, not a run executed in the current repair. Score arithmetic and capture structure were rechecked; provider provenance and assessor independence were not independently established. The Windows hazards described at the end are historical and are fixed in the release. Original bytes are preserved at `history/REPRODUCTION-RESULTS-original.md`. (2026-10-13 verification: moved from the repository root so that `results.md` is the only root results report; a mechanical RESULTS→results rename that had garbled item 5(b) was reverted for that sentence.)

# Reproduction results — official A/B rerun (A_REPRO_1, B_REPRO_1)

**Executed 2026-10-13 · fresh clone of d85a8b8 · Claude Code CLI 2.1.288 · `claude-opus-5-5` · unmodified runners · one run per arm · scored blind against the original frozen key and rubric.** Run manifests: `control/run-manifest-A_REPRO_1.md`, `treatment/run-manifest-B_REPRO_1.md`. Raw captures committed (610ec2a) before scoring.

| Arm | Original run | Original score | Reproduction run | Reproduction score | Correct conclusions | False authorizations |
|---|---|---|---|---|---|---|
| A — no-folder control | A2 | 11 | A_REPRO_1 | **11** | 0 / 8 | 0 |
| B — specialist folder | B1 | 80 | B_REPRO_1 | **80** | 8 / 8 | 0 |

Per question (capped totals):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|---|---|---|---|---|---|---|---|---|
| A2 (original) | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 1 |
| A_REPRO_1 | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 1 |
| B1 (original) | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| B_REPRO_1 | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |

- **The imported records report a matching official result.** B vs A: 8 wins, 0 ties, 0 losses, identical to the original. Every question score matches the original run.
- **Same caveat as the original.** A has no policy text and B does. This difference confirms that supplying sources plus structure helps. On its own, it does not isolate the value of the folder's structure (see the source-only arm C in `results.md`).
- **A behaviour.** Every A response said it lacked the Meridian Works policy and invented no thresholds (all 8 marked transparent uncertainty). On Q7, A again reasoned conditionally that "urgent" alone probably would not qualify, which earned partial credit (capped 4). This is the same pattern and the same judgement call as A2.
- **B behaviour.** All 8 answers were fully correct and cited real section IDs. No omissions, regressions or false authorizations.

## Secondary metrics (measured from captures)
| | Original | Reproduction |
|---|---|---|
| A mean wall time (`duration_ms`) | ≈ 13.8 s | ≈ 12.9 s |
| B mean wall time | ≈ 26.0 s | ≈ 26.1 s |
| A files read | 0 | 0 |
| A sessions with blocked out-of-workspace searches | 7 of 8 | 4 of 8 (5 denials) |
| B files read | 10 files in 7 of 8 sessions | 7–10 per session, specialist files only |
| B permission denials | 1 of 8 sessions | 0 |

## Scoring and disclosures
1. **Assessor.** One independent subagent (same model family as the tested model) read only `evaluation/scoring-repro-1/blind_packet.md`: rubric, key, questions and 16 shuffled responses with directory paths stripped. Unblinding uses `blind_key.json` (seed 20261013). Scores are in `assessor-scores.json`. There was no second assessor.
2. **Blinding is limited for A.** A responses are recognisable by content (they say no policy is available), and several mention their working directory name (`A_REPRO_1-Qn`) or the parent scratchpad. Responses were not edited.
3. **Assessor judgement calls.**
   - A's "policy unavailable" answers got 1 point (unsupported = 1, no invented rules). A stricter reading would give 0.
   - A Q7 got 4 (conditional partial credit). A stricter reading of the "No policy access" clause would give 2.
   - These match how A2 was scored, so the comparison is like-for-like.
   - The assessor could not confirm EXP-4 and AMD-3 from the packet. Both exist in the fixture and were used correctly (EXP-4: thresholds and "up to" are inclusive), so no change.
4. **Reproduction limits.**
   - Same machine, account, CLI build and user-level Claude Code configuration as the original. This is not a clean-machine or different-account reproduction.
   - The server-side model revision is not observable, and temperature is not controllable.
   - One run per arm.
5. **Fresh-clone hazards found (Windows).**
   - (a) The system Git config sets `core.autocrlf=true`, which rewrites prompts and policy files to CRLF on clone. The run used `git clone -c core.autocrlf=false`. `REPRODUCE.md` should say so.
   - (b) The repository tracked both `RESULTS.md` and `results.md`. On case-insensitive filesystems only one is checked out, so `git status` is never clean and `verify_submission.py`'s clean-tree check fails. For this reason these results are recorded in this separate file rather than in either `RESULTS.md` or `results.md`.
