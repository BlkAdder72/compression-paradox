# The Compression Paradox — Competition #14: The Control

Our folder beat no folder. Then we added a harder control: the same primary documents without the specialist instructions or index. That control tied the folder on the corrected benchmark and outscored it on the separately authored set. These runs demonstrate no incremental accuracy benefit from our architecture; they do not show that context folders generally fail.

## What the folder does
The specialist answers purchasing-policy questions for fictional Meridian Works. Its identity, rules, examples, six-document reference directory and README index are in [specialist/](specialist/). Compressed navigation points to the primary rules.

## Current recorded results
| Separate evidence set | A: no folder | B: specialist | C: sources only | B vs A W/T/L | B vs C W/T/L |
|---|---:|---:|---:|---|---|
| Corrected v2 Q1–Q8 | 14/80 | 80/80 | 80/80 | 8/0/0 | 0/8/0 |
| Separate-session U1–U8 | 8/80 | 77/80 | 80/80 | 8/0/0 | 0/7/1 |

The folder lost U8 by three points for giving only one reading of an ambiguous provision. It has seven fully correct U conclusions and one partial conclusion; no false authorization was recorded. A had no policy text, so A/B cannot isolate the benefit of structure. The specialist remains frozen; a possible future ambiguity-handling change would need new unseen tests.

## Judge quick start
1. Read [questions.md](questions.md) and [results.md](results.md), including per-question scores, timings, losses and limitations.
2. Inspect [control/README.md](control/README.md) and [treatment/README.md](treatment/README.md) for exact prompts and raw transcripts. Failed/excluded historical attempts are retained.
3. Follow [REPRODUCE.md](REPRODUCE.md) for offline checks and fresh model runs. Full Git history is included in the release ZIP.
4. Read the [supplied-spec matrix](competition/SPEC-CHECK.md) and [release readiness](RELEASE-READINESS.md) for unresolved submission gates.

## Provenance and limits
Original questions and a separate answer key preceded the original control and specialist. Current v2 fixes Q4 after the folder existed, but before the corrected runs; it is a disclosed amendment, not original preregistration. The executed v2 source is archived unchanged; current questions.md changes only status prose.

U questions were generated from the six sources in a separate Claude session according to the supplied authoring note. Human or cross-family independence is not claimed; the operator saw them before execution. Tested model, author and assessors share a model family. CLI execution differs from the competition's Projects walkthrough. One fixed-order round per current set, inherited account configuration and ceiling effects limit inference. No significance or general causal claim is made.

Current results and earlier v1/H results are separate. Historical documents and frozen pre-run manifests retain their original wording. No new model calls were made for this documentation and metric-label revision. Public GitHub publication, entry-comment submission and Premium/VIP eligibility remain unconfirmed.
