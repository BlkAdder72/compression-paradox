# Competition #14 — supplied-spec check

Source: [user-supplied text](spec-user-supplied-2026-10-13.txt). Original post URL was not supplied; this is an artifact comparison, not moderator certification.

| Requirement | Current evidence / qualification |
|---|---|
| Five specialist components | All present in specialist/: identity.md, rules.md, examples.md, reference/, README.md. |
| 5–10 questions with expected answers | Eight root v2 questions with answer table; Q4 is self-contained. |
| Questions before folder and runs | Original df36e7d has questions and separate evaluation/expected-answers.md; control da56555 precedes specialist 3d9be31. Literal same-file packaging differs. v2 correction 504bae1 follows folder creation but precedes execution ef44500; cannot claim v2 preceded the folder. Moderator interpretation remains a risk. |
| Same model, questions and order in A/B | v2 and U records support identical question order and observed model claude-opus-5-5, CLI 2.1.288. Claude Code CLI differs from the Projects UI walkthrough; this is disclosed. |
| Root control/ and treatment/ raw evidence | Original captures plus README pointers to exact current evidence and prompts. Unedited evidence c7afda4 precedes grading. Failed/excluded earlier runs retained. |
| results.md wins, ties, losses, slower cases, changes | Question-level scores and timings present. B/C v2 ties all eight; U ties seven and loses U8. Folder unchanged to preserve frozen testing; prospective change identified. |
| Advantage on a question entrant did not write | Separate Claude-session U questions: B beats A on all eight, but loses U8 to C. Same-family generation, authoring-note provenance and operator exposure disclosed. No human/cross-family independence; moderator acceptance unconfirmed. |
| Reproduction | Executable capture and scoring kit; full history; exact prompts and sources preserved. See REPRODUCE.md. Future provider availability and exact output are not guaranteed. |
| Public GitHub link and 2–3 sentence entry comment | Pending. No actual repository URL supplied or publication performed. See SUBMISSION-COMMENT.md. |
| Premium/VIP membership | User confirmation pending. |
| Deadline | Supplied wording: Tuesday, October 13th, 11:59 PM EST. Submit before 11:59 PM Eastern local time as a conservative interpretation of the timezone label. |

The supplied spec asks for a question the entrant did not write; it does not expressly require a human author. Separate-session AI authorship is disclosed, not certified as independent. Historical chronology cannot be repaired retroactively, and this release does not conceal it.
