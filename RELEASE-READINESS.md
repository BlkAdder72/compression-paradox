# Release readiness — updated 2026-10-13 (verification pass)

Verdict: **locally verified research package with fresh model evidence; NOT certified as a submitted public competition entry.** Two external gates remain open (rules/deadline source, public repository). See `HANDOFF-TO-CODEX.md`.

## Completed in the verification pass
- **Fresh Claude tests: DONE.** Six new runs (A/B/C official and C/D/E H-series) at `9e79e0e`, 48/48 sessions on CLI 2.1.288 with actual model `claude-opus-5-5`. All runs were clean under the pre-registered tool-access review, and evidence was committed before scoring. Two blinded assessors per set scored them, with one adjudicated item. Results are in `results.md`, under "Fresh verification runs". The rejected pre-execution attempt is retained.
- **Offline gates, regression tests and `git fsck --full`:** pass on the received release, on fresh clones (default `autocrlf=true` and documented `autocrlf=false`) and in a genuinely case-sensitive directory (NTFS per-directory case sensitivity). Logs are in `verification/2026-10-13/`.
- **Defects fixed** (one at a time, retested after each):
  - (1) A second root results report was moved to `history/`, with a guard added to `verify_submission.py`.
  - (2) A stale `RESULTS.md` pointer in the Stage 3 README was corrected.
  - (3) The undocumented MSIX CLI-path failure is now documented in `REPRODUCE.md`.
  - (4) A garbled sentence from the earlier mechanical rename was fixed in the moved report.

## Open blockers
1. **Independent unseen questions: PENDING (no external author available).** No genuinely external author was accessible; a fresh subagent does not qualify. G1–G4 remain generated, non-independent and unexecuted. Follow `evaluation/challenge/PROTOCOL.md` when an external author is available.
2. **Official rules and deadline: PENDING.** No authoritative Competition #14 rules URL, requirement text or deadline/timezone could be identified from the repository, local files or web search. The user must supply the link. No requirement or deadline is assumed.
3. **Public GitHub: UNVERIFIED / not published.**
   - No Git remote is configured, and no `gh` CLI or GitHub authentication is available.
   - Unauthenticated GitHub commit search for `df36e7d`, `4392931` and `c12af4a` returned 0 results. The search index is not exhaustive.
   - Nothing was pushed. Publication requires the user's explicit authorization and repository URL.

## Scientific limits retained
- A/B confounds source availability with architecture. Fresh B vs C is 0/8/0.
- The H-series are post-analysis questions, with ceiling effects. There are now four scored H rounds.
- Assessors are the same model family as the tested model. Provider authenticity and server revision are not independently established.
- Each set was run as one round in a fixed order.
- Failed and excluded raw attempts are retained.
