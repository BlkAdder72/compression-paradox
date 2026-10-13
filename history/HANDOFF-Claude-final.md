# Handoff to Codex — corrected official v2 and U1–U8 execution (2026-10-13)

## Input and exact revisions
- **Received:** `compression-paradox-unseen-ready-2026-10-13B.zip`.
  - SHA-256 `6ff1ffb2103fde5f46e143b1583cf446e2b14706a664bce91bba788dad8ddf75`, which matches the expected value. The filename carries a "B" suffix.
  - HEAD `4b499ac1018c0c7c364f6319f8c96cfb177a3085`, as expected, with a clean tree.
  - The original ZIP is preserved unchanged.
- **Model runs executed at:** `ef4450074e4d53ce532791b25b61bbec4e23eb8a`, the pre-registration commit, from a fresh `git clone --no-local` with a clean tree.
- **Final verified commit:** `0799b6c2a6dcbb20c3370ac8d939438533226b76`, all checks run in three fresh clones.
- **Returned HEAD:** the next commit, which adds only this file and `verification/2026-10-13B/`. It was re-checked in place and from the extracted return ZIP. Run `git log -1` to see it.
- No history was rewritten. All earlier raw evidence, failed or excluded attempts, authoring files and historical reports are unchanged.

## Pre-run verification (on 4b499ac; logs in `verification/2026-10-13B/received-4b499ac/`)
- The 8 integrity checks and 2 regression suites returned rc=0: `verify_submission`, `verify_stage3`, `preflight_stage4`, `verify_control_capture` (v1 and v2 prompts), **`verify_unseen`** (specialist, fixture, rubric and authored inputs match frozen hashes), `audit_evidence`, `test_runner`, `test_blind_packet`.
- `score_fresh summary`, `git fsck --full` and the clean-tree check also passed.
- 30 of 30 tracked JSON files parsed as single documents.
- The specialist is unchanged since 3d9be31. CLI 2.1.288 was confirmed, with the same binary hash as the earlier fresh runs.

## Commits added
| Commit | Content |
|---|---|
| `ef44500` | `evaluation/v2-20261013/PLAN.md`: run IDs, order, paths, contamination rule and scoring for both sets, committed before any call. Frozen U inputs untouched. |
| `c7afda4` | Raw evidence for A/B/C_V2_01 and A/B/C_U_01 (stdout with tool traces, stderr, manifests, checksums), contamination reviews, session listings, run records, root `control/README.md` and `treatment/README.md`. Committed **before** packets and scores. |
| `c5250f1` | `scripts/prepare_v2_packet.py`, the v2 blind packet and key, the U packet via `prepare_blind.py`, and U assessor instructions quoting the frozen rules. |
| `7b5f474` | Two assessors per set, disagreements, written adjudications, `scripts/score_v2_u.py`, `evaluation/v2-u-summary.json`. |
| `0799b6c` | `results.md` headline and v2/U sections, `README.md`, `RELEASE-READINESS.md`, `REPRODUCE.md` (executed commands), `CHANGELOG.md`, `competition/SPEC-CHECK.md`. |
| (HEAD) | `verification/2026-10-13B/` and this handoff. |

## Execution (actual)
- **Runs:** 6 runs, 48/48 sessions, executed 20:37:45–20:54:36 UTC.
- **CLI and model:** Claude Code 2.1.288, native `claude.exe` (SHA-256 `84304f7d…0ab91`) at its real MSIX path. Requested and **observed** model `claude-opus-5-5` in every init event and assistant message. Same flags for every arm.
- **Arms:** A had no files, B the frozen 10-file specialist, C the six primary sources. Prompts were question-only and unchanged, in identical order, one fresh session per question.
- **Outcome:** all exits 0, stderr empty, no failures and no retries.
- **Contamination:** all six runs CLEAN.
  - Session folders held exactly the allowlisted files; nothing else was read.
  - A's parent-folder searches were denied: 7 in v2, 8 in U.
  - A's own auto-memory-folder searches were permitted, but every one returned nothing: 5 in v2, 1 in U.

## Results (frozen rubric; two blinded assessors per set; 23 of 24 items agreed in each set; 2 written adjudications)
| Set | A | B | C | B vs A | B vs C |
|---|---|---|---|---|---|
| Corrected official v2 | 14 | 80 | 80 | 8/0/0 | 0/8/0 |
| U1–U8 (separate Claude session) | 8 | 77 | 80 | 8/0/0 | **0/7/1** |

- **False authorizations:** none in any arm.
- **Omissions:** A misses every question, because it has no policy access and said so on all 16. B misses one U8 branch.
- **Ambiguity-related deductions:** B U8 lost 3 points under the frozen both-readings criterion. B and C each scored 10 on U6.
- **Adjudications:**
  - v2 A Q4 was capped at 4, because it left an emergency override of the vendor ban open.
  - U8 B was scored 7, following the rubric's wording on conclusion and exceptions.
- **Deviations from plan:** none for the runs.
  - The first case-sensitive re-check failed checkout because the deep scratchpad path exceeded Windows `MAX_PATH`. It was repeated in a short case-sensitive folder (`C:\Users\mmazu\pcs13`), where everything passed.
  - Log filenames were shortened when copied into the repository.
- **Disclosures:**
  - The assessors are the same model family as the tested model, the U author and the orchestrator.
  - A is recognisable by content and folder names.
  - The run order was fixed.
  - User-level Claude Code configuration was inherited.
  - U1–U8 are described as generated in a separate Claude session from the primary documents. No human, cross-family or moderator-accepted independence is claimed.
  - v2 is described as a post-folder correction.

## Final verification (on 0799b6c; logs in `verification/2026-10-13B/final-0799b6c/`)
- **Fresh clones:** default `autocrlf=true`, documented `autocrlf=false`, and a genuinely case-sensitive NTFS directory (`fsutil setCaseSensitiveInfo`, confirmed by a probe and inherited by subdirectories).
- **Each clone:** all 8 checks and 2 regression suites, `score_fresh` and `score_v2_u` aggregation (tree unchanged afterwards), contamination reviews of the committed evidence (6/6 CLEAN), 46/46 JSON files valid, `git fsck --full`, clean tree and no case-folded path collisions all passed.
- **Case-sensitive extra:** historical `4392931` checks out with both `RESULTS.md` and `results.md` present.
- **Return ZIP:** integrity and an extracted copy are re-checked after the ZIP is built (see the final message for its SHA-256).

## Remaining blockers (user action; nothing was published)
1. **Public GitHub repository: PENDING.**
   - Create the repository, push the full history including this HEAD, and verify signed-out access.
   - Confirm the published HEAD equals the returned HEAD.
   - The repository must be published before the cutoff, since judges pin the last commit before the deadline.
2. **Competition comment: PENDING.** Post the link plus the 2–3 sentences below.
3. **Premium/VIP eligibility: PENDING.** Confirm membership.
4. **Deadline:** the supplied text says "Tuesday, October 13th, 11:59 PM EST". Target 11:59 PM Eastern local time, which is 03:59 UTC on October 14 (EDT).
5. **Windows extraction:** extract to a short path, because some `.git` and log paths can exceed `MAX_PATH` under deep folders.

## Draft submission comment (supported by `results.md`)
> A Meridian Works purchasing-policy specialist (identity, rules, examples, six-document reference/ and a README index) tested against a no-folder control and a sources-only arm on `claude-opus-5-5`, with raw transcripts and blinded two-assessor scoring committed for the corrected questions and for eight questions generated in a separate Claude session. The folder beat no folder on every question (80 vs 14 on the corrected set, 77 vs 8 on the separately written set), but it only matched the bare source documents, never beating them. Most surprising line in results.md: "It **lost U8** by 3 points: it treated a genuinely ambiguous vendor branch as settled, where the frozen criterion required both readings."
