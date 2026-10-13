# Release repair changelog — 2026-10-13

Input: latest `compression-paradox.zip` attachment exposed by the referenced chat. SHA-256: `0622f1ba2ad322f218ac32117fb6ca0cc6c1a4f24f817ea3cdf238d84f16855d`. Original HEAD: `4392931`. Original archive and synced project sources were not modified.

1. Restored lowercase `results.md` from Git and moved uppercase report unchanged to `history/RESULTS-original.md`. Retained history without rewriting. Checked unique case-folded paths and clean tree.
2. Enforced LF for ordinary text; preserved raw/historical bytes. Added explicit UTF-8 reads and ran offline guards.
3. Replaced unsafe runners with portable Python capture and Bash wrappers: no overwrite, source allowlists, timeout/failure preservation, result validation and metadata/checksums. Dry-preflighted all arms, checked shell syntax and added regression tests. Test stubs are not model evidence.
4. Audited stored checksums, scored result records and arithmetic. Reconciled root results with imported A/B rerun; corrected 48-versus-32 C/E response count and stale Stage 3 status. Original score files and historical reports retained.
5. Added four generated, explicitly non-independent, unexecuted questions; external-author protocol; capture and blinded-packet kit. No new model results or external authorship claimed.
6. Rewrote prerequisites, core.autocrlf guidance, fresh-run commands and limits.

See the accompanying verification report for executed checkout, history, script, evidence and ZIP checks. See `RELEASE-READINESS.md` for unresolved external gates.

# Verification pass — 2026-10-13 (Claude Code)

Input: `compression-paradox-release-2026-10-13.zip`, SHA-256 `02d126059be7b9e7df05f8215bf898254d41996117f0dcc9da9cda8e2c5f8b58`, HEAD `c12af4a`. History is preserved, with nothing rewritten or overwritten.

1. `02bb445`: fix, `results.md` is the only root results report. The annotated A_REPRO_1/B_REPRO_1 report moved to `history/`, and a guard was added to `verify_submission.py`.
2. `7122334`: docs, the Stage 3 README points to `results.md`.
3. `9e79e0e`: pre-registration of fresh runs (IDs, order, contamination review, frozen scoring), plus `evidence/** -text`.
4. `c810226`: `scripts/review_fresh_captures.py`, a read-only tool-access and provenance review.
5. `64b3ca9`: raw evidence of six fresh runs, review, run record and retained failed attempt (committed before scoring).
6. `a941589`: `scripts/prepare_fresh_packets.py` and the blinded packets.
7. `07e2cbe`: two assessors per set, adjudication, and `scripts/score_fresh.py` summary.
8. Documentation: results, readiness, the MSIX CLI path in `REPRODUCE.md`, verification logs and `HANDOFF-TO-CODEX.md`.

## Spec-aware follow-up repair
- Fixed disagreements.json and its generator to emit one JSON array; archived original malformed bytes.
- Archived exact original questions and created version 2 with self-contained Q4; seven other prompts unchanged.
- Embedded expected answers in root questions.md; model runner uses question-only files.
- Default official suite now v2; explicit legacy suite preserves reproduction of all existing Q scores.
- Added supplied competition spec and requirement check; public repo not yet created, unseen-question and corrected-run checks pending.

## Separate-session author input acceptance
- Preserved external-questions.json and AUTHORING-NOTE.md byte-for-byte.
- Validated U1–U8 schema, citations, self-containment, arithmetic and source-policy support; froze source, specialist, rubric and plan hashes.
- Added prospective ambiguity grading and A/B/C run instructions plus verify_unseen.py. No tested-folder changes or model calls.

## Corrected v2 and U1–U8 execution — 2026-10-13 (Claude Code)
Input: `compression-paradox-unseen-ready-2026-10-13B.zip`, SHA-256 `6ff1ffb2103fde5f46e143b1583cf446e2b14706a664bce91bba788dad8ddf75`, HEAD `4b499ac` (verified). History is preserved and not rewritten.
- `ef44500` prereg: `evaluation/v2-20261013/PLAN.md` (run IDs, order, paths, contamination rule, scoring for both sets) before any call.
- `c7afda4` evidence: six runs (v2 and U, A/B/C), contamination review, run records, root `control/README.md` and `treatment/README.md` pointers. Committed before scoring.
- `c5250f1` scoring prep: `scripts/prepare_v2_packet.py`, the v2 packet, the U packet via `prepare_blind.py`, and U assessor instructions with the frozen rules verbatim.
- `7b5f474` scored: two assessors per set, two written adjudications, `scripts/score_v2_u.py`, `evaluation/v2-u-summary.json`.
- Docs: `results.md` headline and v2/U sections, `README.md` status, `RELEASE-READINESS.md`, `REPRODUCE.md` executed commands, `competition/SPEC-CHECK.md`, `HANDOFF-TO-CODEX.md`, and verification logs in `verification/2026-10-13B/`.
- No change to the specialist, fixture, rubric, keys or frozen U inputs.

# Submission documentation and metric revision — 2026-10-13

- Reconciled current README, spec matrix, questions status, readiness and reproduction instructions; archived prior landing page, reproduction instructions and handoff unchanged.
- Preserved exact executed v2 question source and manifest. Verifier now guards both its frozen hash and equality of every published question/expected answer.
- Replaced the ambiguous derived correct-conclusions field with explicit full-credit, partial-credit and no-disqualifying-conclusion counts. B U8 remains 7/10 and U total remains 77/80; raw scores and adjudications are unchanged. Archived previous summary.
- Led with the sources-only control finding and U8 loss; added a three-sentence submission draft and explicit moderator-interpretation qualifications.
- No new model execution, external author, GitHub publication or submission claimed. All original evidence and full Git ancestry preserved.

## License addition — 2026-10-13

Added the LICENSE from the prior PrepMe_Sim entry unchanged, and linked it from the judges' README. No test inputs, scores, scripts or raw evidence changed.

## Fresh seven-question release — 2026-10-13
- Retained seven exact original prompts and gold answers (Q1–Q3,Q5–Q8); excluded amended Q4 with all original evidence retained. Disclosed post-results selection and original separate-key placement.
- Committed/pushed combined questions.md and plan at 4f0c0b8 before 21 fresh Claude calls. Raw evidence and access review committed/pushed at 2df7042 before grading.
- New scores A10/B70/C70 under unchanged per-item rubric; one disclosed unblinded Codex assessor. Detailed rationales and a raw-hash-bound arithmetic validator added. No old scores regraded.
- Default official runner now selects seven; official-v2 explicitly preserves corrected eight-question reproduction. Added exact original-content/chronology verifier and runner regression.
- Placed current raw A/B files directly under root control/ and treatment/; preserved identical evidence copies, all Q4 records and full history. A's nonexistent-memory read retains its automated review flag and no-content manual disposition.
- Reconciled current README/results/reproduction/spec/readiness/publication statements and submission comment. Archived earlier current-status documents. Specialist, fixture and original rubric unchanged.

## Current-status cleanup — 2026-10-13
- Recorded entrant-confirmed VIP membership in current README, readiness, handoff, spec matrix and verification status.
- Reconciled the handoff with completed GitHub publication/public-clone checks.
- Synchronized SUBMISSION-COMMENT.md with the approved three-sentence comment, including why a separate Claude session authored the additional questions.
- Comment posting remains unverified. Dated frozen plans, archived documents, raw evidence, scoring and specialist files are unchanged.


## Actual Projects UI completion and assessment — 2026-10-13
- Frozen UI plan 1318b4b; original A Q1 interruption retained. Edge recovery, pre-B text import adaptation and clean-context continuation preserved.
- Complete ungraded A7/B7/C7 rendered captures committed/pushed at 5f52b52. No completed calls regenerated. A/B raw copies and C source-import hashes included.
- One unblinded Codex assessment: UI A13/B64/C70, B/A seven wins, B/C six ties/one loss. Q6 timing interpretation and B70 sensitivity explicitly distinguish current judgment from earlier CLI treatment.
- Added UI score/provenance verifier and reconciled README/results/reproduction/spec/readiness/control/treatment/comment draft. Preserved historical reports, CLI/U scores, frozen inputs and specialist unchanged.
- Entrant reports comment posted; no independent check or Skool edit claimed. Full-history release and fresh-clone checks documented separately for the final revision.
