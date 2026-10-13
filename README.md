# The Compression Paradox — Competition #14: The Control

Our folder beat no folder. Then we tested it against the same primary documents without specialist instructions or an index: the sources-only arm matched it, with a shorter mean session time in this round. Supplementary questions exposed one case where the folder did worse. No incremental accuracy benefit from our architecture was demonstrated; this is not a general claim that context folders fail.

## Current official entry: seven original questions, freshly rerun
| Arm | Score /70 | Fully correct conclusions | Mean session time |
|---|---:|---:|---:|
| A — no folder | 10 | 0/7 | 13.6 s |
| B — specialist folder | 70 | 7/7 | 18.5 s |
| C — same sources only | 70 | 7/7 | 15.4 s |

B beats A on all seven questions and ties C on all seven. In the separate-session U1–U8 supplementary test, A scored 8/80, B 77/80 and C 80/80: B tied C on seven and lost U8 for treating an ambiguous policy branch as settled. These are separate evidence sets, not pooled results.

## What the specialist does
The folder answers purchasing-policy questions for fictional Meridian Works. Its five required components are in [specialist/](specialist/): identity.md, rules.md, examples.md, reference/ and README.md. The six primary documents make the answers checkable. The index points to source provisions rather than replacing them.

## Judge quick start
1. Read [questions.md](questions.md): seven prompts and their original expected answers. Original IDs Q1–Q3 and Q5–Q8 are retained for traceability.
2. Inspect [control/](control/README.md) and [treatment/](treatment/README.md): current raw transcripts are directly under their raw/ directories. Exact prompts are in control/prompts-seven/.
3. Read [results.md](results.md): per-question results, ties/losses, timing, provenance and unchanged specialist.
4. Follow [REPRODUCE.md](REPRODUCE.md): the default official suite runs exactly the seven submitted questions, in separate fresh sessions. Never give a tested model the whole repository or answer key.
5. Check the [frozen run plan](evaluation/seven-20261013/PLAN.md) and [spec matrix](competition/SPEC-CHECK.md).

## Chronology and limits
All seven prompts AND gold answers are unchanged from df36e7d, before original control da56555 and specialist 3d9be31. Gold answers were originally a separate file. The current combined root file and fresh-run plan were committed and pushed at 4f0c0b8 before the new calls; raw evidence 2df7042 preceded grading. The seven-item selection happened after earlier results to exclude Q4's context dependency and later amendment. Every Q4 version, score and transcript remains available. We do not claim this exact subset was originally preregistered or guarantee moderator interpretation of original file placement.

Testing uses Claude Code CLI, not the Projects UI. The fresh seven-question scores have one disclosed, unblinded Codex assessor. Earlier two-assessor results remain supplementary; same-family U authoring is not human independence. One fixed-order round, inherited account configuration and ceiling effects limit inference. A failed attempt to read a nonexistent Claude memory file is retained and disclosed in results.md.

Public repository: https://github.com/BlkAdder72/compression-paradox. VIP membership was confirmed by the entrant on October 13, 2026. Entry-comment posting remains unverified; use the current draft in SUBMISSION-COMMENT.md.

## License
[Competition Evaluation and Non-Commercial Review License](LICENSE), copyright 2026 Matthew Mazur. Judges may clone, run, locally modify for evaluation and retain reasonable copies. Commercial use requires separate permission.
