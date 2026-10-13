# Competition #14 — current supplied-spec matrix

Source: spec-user-supplied-2026-10-13.txt. No original post URL, separate full judging rubric or later moderator clarifications were supplied. This is an evidence comparison, not moderator certification.

| Requirement | Current evidence and qualification |
|---|---|
| Five specialist components | Present under specialist/, unchanged. |
| Five–ten questions and expected answers at root | Seven in questions.md, original IDs Q1–Q3,Q5–Q8. |
| Questions/answers before runs | Exact retained content at df36e7d before original control; combined root file and new plan at 4f0c0b8 before all fresh seven-question calls. |
| Questions before folder | All seven retained prompts and gold rows predate specialist 3d9be31. The seven-item selection itself occurred after prior results and is explicitly disclosed. |
| Literal original same-file expected answers | Original key was evaluation/expected-answers.md at df36e7d, not inside questions.md. Current file consolidates them before fresh runs; original packaging cannot be rewritten and remains a moderator interpretation risk. |
| Same model, questions, order | New A/B/C_SEVEN_01: same observed claude-opus-5-5, CLI 2.1.288, seven exact prompts in same order, separate fresh sessions; raw committed before grading. |
| Raw control/ and treatment/ | New actual raw captures are directly in control/raw/A_SEVEN_01 and treatment/raw/B_SEVEN_01; exact prompts in control/prompts-seven. All old Q4 and failed/excluded records retained. |
| Results, ties/losses, slower cases, changes | A10/B70/C70; B/C seven ties and B longer mean session duration. Supplementary U8 loss retained. Specialist unchanged; prospective improvement identified without tuning against known tests. |
| Question entrant did not write | Earlier U1–U8 generated in separate Claude session from sources: B beats A on all eight; B loses U8 to C. Same-family authoring and operator exposure disclosed. Judges' own unseen test remains theirs to perform. |
| Reproduction | Executable current seven-run suite and exact inputs. Public cloning previously verified; final verification accompanies this release. Future model behavior not guaranteed. |
| Claude Projects workflow | Actual calls use Claude Code CLI, not Projects. Interface difference disclosed; moderator interpretation unconfirmed. |
| Public GitHub | https://github.com/BlkAdder72/compression-paradox; full history published. |
| Comment with link and 2–3 sentences | Updated draft in SUBMISSION-COMMENT.md; actual posting not verified. |
| Premium/VIP eligibility | User confirmation required. |
| Deadline | Supplied wording: Tuesday, October 13th, 11:59 PM EST. Use 11:59 PM Eastern local time as conservative target. Judges pin the last commit before their cutoff. |

The test is the deliverable: B/A demonstrates the folder including sources beats no folder; C asks whether architecture adds anything. A sources-only tie is relevant honest evidence, not grounds to conceal it. Reporting no specialist change preserves the measured artifact; a future change would require new tests. Do not claim independent human grading or an originally preregistered seven-item selection.
