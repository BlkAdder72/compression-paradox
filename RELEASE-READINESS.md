# Release readiness — 2026-10-13 (after corrected v2 and U1–U8 execution)

Verdict: **model testing and scoring complete and locally verified. Not yet a submitted entry: the public GitHub repository, publication and the competition comment are PENDING (user action), and Premium/VIP eligibility must be confirmed by the user.**

## Done (evidence in the repository)
- **Corrected official v2:** A/B/C_V2_01 executed at `ef44500` (pre-registered), 24/24 sessions, all runs clean. Scored by two blinded assessors with one written adjudication. **A 14, B 80, C 80; B vs C 0/8/0.**
- **Separate-session U1–U8:** A/B/C_U_01 executed under the frozen run plan, 24/24 sessions, all runs clean. Two blinded assessors with one written adjudication. **A 8, B 77, C 80; B vs C 0/7/1 (folder lost U8 on the frozen both-readings criterion).**
- Raw evidence and the contamination review were committed before packets and scores. Root `control/README.md` and `treatment/README.md` point to every raw transcript and exact prompt.
- The specialist is unchanged (hashes verified by `verify_unseen.py`). Results report ties and the loss, plus what was and was not changed in the folder.
- Offline checks, regression tests, score aggregation, JSON validation, `git fsck --full`, clean-tree checks, fresh-clone checks and ZIP re-checks pass. Logs are in `verification/2026-10-13B/`.

## Pending / blockers
1. **Public GitHub repository: PENDING.**
   - The user has not created it. Nothing was published, pushed or submitted.
   - After creation: push the full history, check signed-out access, and confirm that the published HEAD equals the tested final commit (see `HANDOFF-TO-CODEX.md`).
2. **Competition comment submission: PENDING (user).** Post the repository link plus 2–3 sentences. A draft is in `HANDOFF-TO-CODEX.md`.
3. **Eligibility: PENDING (user).** Premium/VIP membership.
4. **Deadline:** the supplied text says "Tuesday, October 13th, 11:59 PM EST". The EST label is ambiguous in October (EDT is in effect), so target 11:59 PM Eastern local time, which is 03:59 UTC on October 14.
5. **Unseen-question independence:** U1–U8 were generated in a separate Claude session of the same model family. This is not human or cross-family independence, and moderator acceptance is not guaranteed.

## Scientific limits
- A/B confounds source availability with structure; B/C is the structure test (ties, plus one loss).
- One round per arm in a fixed order, not counterbalanced.
- Assessors are the same model family as the tested model.
- Inherited user-level Claude Code configuration; server-side model revision unobservable.
- Small question sets near ceiling.
