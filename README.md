# The Compression Paradox — Competition #14: The Control

Our specialist folder beat no folder. The same policy sources without the specialist instructions or index did at least as well. Actual Claude Projects testing is now complete: 21 captured responses, committed before grading. This is a test of whether the added architecture earns its place, not a general claim that folders fail.

## Actual Claude Projects results — seven unchanged questions
| Arm | Score /70 | Fully correct conclusions |
|---|---:|---:|
| A — no knowledge files | 13 | 0/7 |
| B — ten specialist files | 64 | 6/7 |
| C — six primary sources only | 70 | 7/7 |

**B vs A: seven wins. B vs C: six ties and one loss.** B Q6 names both historical approvers but declines to confirm before-purchase timing required by the frozen gold. That judgment is disclosed with a sensitivity: accepting its timing caveat gives B70/C70 and seven ties. No incremental accuracy benefit from the specialist architecture appears under either reading. No false authorization was observed. UI capture timestamps are not model-speed measurements.

Separate earlier Claude Code CLI evidence remains A10/B70/C70, with B/C seven ties and B averaging 18.5 seconds versus C15.4. Supplementary U questions remain A8/B77/C80, with B losing U8 for treating an ambiguous branch as settled. These sets and assessments are not pooled.

## Judge quick start
1. [questions.md](questions.md): seven prompts and original expected answers, with original IDs Q1–Q3,Q5–Q8.
2. [control/raw/A_UI_01/](control/raw/A_UI_01/) and [treatment/raw/B_UI_01/](treatment/raw/B_UI_01/): exact prompts and unedited rendered response/main-DOM captures. C and the manifest are in [evidence/projects-20261013/](evidence/projects-20261013/).
3. [results.md](results.md): per-question scores, losses, timing limitations, assessment judgments and historical results.
4. [REPRODUCE.md](REPRODUCE.md): actual Projects workflow and separate CLI commands. Never give the tested model the answer key or whole repository.
5. [Frozen UI plan](evaluation/projects-20261013/PLAN.md), [assessment](evaluation/projects-20261013/assessment-codex.json), [spec matrix](competition/SPEC-CHECK.md) and [readiness](RELEASE-READINESS.md).

## What the folder does
The specialist answers purchasing-policy questions for fictional Meridian Works. Its five required components are [identity.md, rules.md, examples.md, reference/ and README.md](specialist/). Six primary documents make the answers checkable. The folder and source corpus remain unchanged; no tuning against the observed losses occurred.

## Chronology and limitations
All seven retained prompts and gold rows existed at df36e7d, before original control da56555 and specialist 3d9be31. The original key was separate; the combined root file and fresh CLI plan were committed at 4f0c0b8. The seven-item subset was selected after earlier results to remove Q4's dependency/later amendment. This exact subset was not originally preregistered. All earlier Q4 attempts remain preserved.

The UI plan was frozen at 1318b4b; complete ungraded UI evidence was published at 5f52b52 before this assessment. UI testing used separate clean projects in A/B/C order, each question in a new chat, displayed Opus 5.5 Medium / Manual. B/C used verified **Add text content** imports, not binary folder upload. Memory was off; visible external connectors and Research were off. A's empty-project searches and connector-directory discovery remain captured. A connected-desktop header means hidden tool isolation is not proven. A Q1's original empty clipboard file and same-chat recovery are both preserved. Browser changes and a clean-context continuation are disclosed.

One unblinded Codex assessor graded this UI round. The prior CLI assessment accepted a similar Q6 timing caveat; its historical score remains labeled separately, and the UI sensitivity exposes the effect. Original packaging, post-results selection, text import, workflow order and same-family supplementary authorship remain moderator interpretation risks. Hosted-model behavior can change; passing checks does not certify moderation or future outputs.

Public repository: https://github.com/BlkAdder72/compression-paradox. The entrant confirmed VIP membership and reported the entry comment posted; posting was not independently inspected. [SUBMISSION-COMMENT.md](SUBMISSION-COMMENT.md) is an updated optional three-sentence draft, not a claim that the posted text was edited.

## License
[Competition Evaluation and Non-Commercial Review License](LICENSE), copyright 2026 Matthew Mazur. Judges may clone, run, locally modify for evaluation and retain reasonable copies. Commercial use requires separate permission.
