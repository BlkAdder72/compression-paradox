# Competition #14 — current supplied-spec matrix

Source: spec-user-supplied-2026-10-13.txt. No original post URL, separate full judging rubric or later moderator clarifications were supplied. This is an evidence comparison, not moderator certification.

| Requirement | Current evidence and qualification |
|---|---|
| Five specialist components | Present under specialist/, unchanged. |
| Five–ten questions and expected answers at root | Seven in questions.md, original IDs Q1–Q3,Q5–Q8. |
| Questions/answers before runs | Exact retained content at df36e7d before original control; combined root file and new plan at 4f0c0b8 before all fresh seven-question calls. |
| Questions before folder | All seven retained prompts and gold rows predate specialist 3d9be31. The seven-item selection itself occurred after prior results and is explicitly disclosed. |
| Literal original same-file expected answers | Original key was evaluation/expected-answers.md at df36e7d, not inside questions.md. Current file consolidates them before fresh runs; original packaging cannot be rewritten and remains a moderator interpretation risk. |
| Same model, questions, order | UI A/B/C_UI_01: same displayed Opus 5.5 Medium / Manual, exact seven prompts/order, fresh chat per question; raw 5f52b52 before assessment. Separate CLI runs retain observed claude-opus-5-5 / CLI 2.1.288. |
| Raw control/ and treatment/ | UI captures and exact prompts are directly in control/raw/A_UI_01 and treatment/raw/B_UI_01, plus C under evidence/projects-20261013. Earlier CLI, Q4 and failed/excluded records remain intact. |
| Results, ties/losses, slower cases, changes | UI A13/B64/C70: B/C six ties and one timing-dependent loss, with B70 sensitivity disclosed. No reliable UI timing. Separate CLI A10/B70/C70 retains slower B mean; U8 loss retained. Specialist unchanged. |
| Question entrant did not write | Earlier U1–U8 generated in separate Claude session from sources: B beats A on all eight; B loses U8 to C. Same-family authoring and operator exposure disclosed. Judges' own unseen test remains theirs to perform. |
| Reproduction | Executable current seven-run suite and exact inputs. Public cloning previously verified; final verification accompanies this release. Future model behavior not guaranteed. |
| Claude Projects workflow | Actual Projects UI calls now complete. Separate clean projects A then B then C; Add text content imports. This differs from literal add/remove in one project and binary folder upload; moderator interpretation unconfirmed. |
| Public GitHub | https://github.com/BlkAdder72/compression-paradox; full history published. |
| Comment with link and 2–3 sentences | Entrant reported comment posted; not independently inspected. SUBMISSION-COMMENT.md is an optional updated three-sentence draft; no posted-text edit claimed. |
| Premium/VIP eligibility | VIP membership confirmed by the entrant on October 13, 2026; not independently checked against a membership service. |
| Deadline | Supplied wording: Tuesday, October 13th, 11:59 PM EST. Use 11:59 PM Eastern local time as conservative target. Judges pin the last commit before their cutoff. |

The test is the deliverable: B/A demonstrates the folder including sources beats no folder; C asks whether architecture adds anything. A sources-only tie is relevant honest evidence, not grounds to conceal it. Reporting no specialist change preserves the measured artifact; a future change would require new tests. Do not claim independent human grading or an originally preregistered seven-item selection.
