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
