# Competition #14: The Control — supplied-spec check

Source: `spec-user-supplied-2026-10-13.txt`, supplied by the user; original post URL not supplied. This is a check against that text, not independent website authentication.

| Requirement | Evidence / current status |
|---|---|
| Five specialist components | Present under specialist/: identity.md, rules.md, examples.md, reference/, README.md |
| 5–10 checkable questions with expected answers in root questions.md | Eight questions and expected-answer table now present. v2 Q4 contains all facts. |
| Questions before runs; questions before folder | Original v1 history retained. Expected answers were originally separate. v2 is explicitly a later correction; must be committed before corrected runs and cannot claim original preregistration. |
| Same model/questions/order, raw A/B committed | Legacy v1 records retained. Corrected v2 A/B rerun PENDING; no old scores relabeled. |
| Root control/ and treatment/ with prompts/raw evidence | Original v1 present. New corrected captures should be committed with manifests and clear root-directory pointers before submission. |
| results.md includes ties/losses and what changed | Original and fresh comparisons retained, including B/C ties. Folder unchanged by this repair; JSON and benchmark corrected. No unsupported architecture benefit claimed. |
| Advantage on a question you did not write | Not yet tested. Separate Claude authoring session can provide unseen-to-folder questions, but same-family AI provenance must be disclosed. Human/external independence is not established by a new chat alone. |
| Public GitHub repository and comment with 2–3 sentences | User confirms no repository yet. Creation/publication/comment submission PENDING. Nothing published here. |
| Premium or VIP membership | User must confirm eligibility. |
| Deadline | Supplied wording: Tuesday, October 13th, 11:59 PM EST. Preserve exact wording. EST vs Eastern daylight-time intent is ambiguous; submit before 11:59 PM Eastern local time as the conservative target. |

The spec explicitly judges a question the entrant did not write; it does not expressly require a human author. Do not promise moderators will treat a separate Claude session as independent. Preserve the original authoring output, context disclosure and source-only input hashes, freeze the specialist, and test before making a generalization claim.

## Status update after execution (2026-10-13)
| Requirement | Status |
|---|---|
| Same model, questions and order; raw A/B committed | **Done for corrected v2** (A/B/C_V2_01) and U1–U8 (A/B/C_U_01): `claude-opus-5-5`, CLI 2.1.288, fixed order, unedited transcripts committed before scoring. |
| Root control/ and treatment/ with prompts and raw evidence | **Done**: `control/README.md` and `treatment/README.md` index every run and the exact prompt files. |
| results.md reports losses and ties | **Done**: B vs C ties 8/8 on v2 and 7/8 on U, with **one loss (U8)**. No structure advantage is claimed. Folder unchanged, with the reason stated. |
| Advantage on a question you did not write | **Tested** on separate-session U1–U8: folder beats no folder 8/8, but versus sources alone it tied 7 and lost 1. Same-family AI authorship is disclosed. |
| Public GitHub repo, comment, eligibility | **PENDING (user)**. Nothing published. |
