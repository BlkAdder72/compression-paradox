# Results — seven original questions, fresh execution

Runs A_SEVEN_01, B_SEVEN_01 and C_SEVEN_01, executed 2026-10-13 at 4f0c0b8: seven fresh independent sessions per arm, same Claude Code 2.1.288 and observed claude-opus-5-5. These are NEW responses to the exact submitted seven questions, not subsets of old run scores. Raw evidence was committed at 2df7042 before assessment. No statistical significance is claimed.

| Arm | Score /70 | Fully correct conclusions | False authorizations | Mean session time |
|---|---:|---:|---:|---:|
| A — no folder | 10 | 0/7 | 0 | 13.6 s |
| B — specialist folder | 70 | 7/7 | 0 | 18.5 s |
| C — sources only | 70 | 7/7 | 0 | 15.4 s |

| Arm | Q1 | Q2 | Q3 | Q5 | Q6 | Q7 | Q8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 1 | 1 | 1 | 1 | 1 | 4 | 1 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| C | 10 | 10 | 10 | 10 | 10 | 10 | 10 |

- **B vs A: 7 wins / 0 ties / 0 losses.** C vs A is also 7/0/0.
- **B vs C: 0 wins / 7 ties / 0 losses.** The folder adds no measured accuracy advantage over sources alone on this set.
- **Slower:** B averaged 18.512 seconds versus C 15.3717 seconds, about 3.1 seconds longer per session. A averaged 13.5823 seconds but did not supply the policy answers. These are observed single-round session durations, not established speed effects.
- **Source availability:** A had no policy documents. A/B therefore tests the whole folder including information access; it does not isolate architecture.

## Scoring and uncertainty
The unchanged per-question rubric awards conclusion 0–4, applicable rules 0–2, exceptions/dependencies 0–2, evidence 0–1 and unsupported claims 0–1. With seven questions the maximum is 70; the frozen original rubric's 80-point total describes its original eight-item set.

B and C received 4/2/2/1/1 on every question. A received 0/0/0/0/1 except Q7: 2/0/1/0/1, capped at 4. A recognized that urgency probably did not justify the exception but did not identify both required approvers. All A answers disclosed unavailable policy access; no false authorization was asserted. Appropriate uncertainty is not the same as a correct policy answer under the frozen rubric.

This round was assessed by one Codex assistant with prior experiment knowledge. It is not independent human review, effective blinding or two-assessor agreement. [All category scores and answer-specific rationales](evaluation/seven-20261013/assessment-codex.json) bind to raw transcript hashes. `scripts/score_seven.py --check` checks arithmetic and capture identity, not semantic grading.

Reviewable judgment calls: B Q6 notes that AMD-1 does not restate timing; it still supplies the two gold-required approvers and correct historical threshold. C Q6's advance-approval wording is consistent with AMD-3 changing only the threshold. C Q3 applies the stated October 12 scenario to an October 13 notice deadline, implicitly treating the purchase as completed; no deduction was made because its relative deadline and required approvals remain correct. These judgments are explicitly exposed for moderator review.

## Raw evidence and access review
Current raw A/B captures, stderr, manifests and checksums are directly under control/raw/A_SEVEN_01/ and treatment/raw/B_SEVEN_01/. Identical copies plus C are under evidence/seven-20261013/. Seven exact prompt files are in control/prompts-seven/. Only one copy of each answer is scored.

All 21 sessions completed on first attempt, exit 0. Session files matched the arm allowlists exactly: A zero, B ten, C six files per session. B and C passed automated access review. A retains automated REVIEW: Q3 attempted to read a per-session Claude memory file outside its working directory. The tool returned is_error=true and "File does not exist"; no content was acquired. Other outside searches were denied or returned nothing. The manual disposition accepted this run before grading with the flag disclosed, rather than replacing it to hide the attempt. See [review disposition](evidence/seven-20261013/REVIEW-DISPOSITION.md) and tool-access-review.json. Do not call all three automated verdicts CLEAN.

## Chronology and Q4 exclusion
Every retained prompt and expected-answer row is unchanged from df36e7d, before original control da56555 and specialist 3d9be31. Original expected answers lived in evaluation/expected-answers.md. Current consolidated questions.md and the execution plan were committed and pushed at 4f0c0b8 before these fresh calls.

The seven-item selection happened after earlier results, solely to exclude Q4's cross-question dependency and later amendment. This is not an originally preregistered seven-item selection. Q4 and every old attempt, including failures and exclusions, remain in the historical evidence. No history was rewritten. Original separate-key packaging still requires moderator interpretation; new runs do not rewrite that fact.

## Supplementary separate-session U1–U8 — earlier run, not rerun here
| Arm | Score /80 | Fully correct conclusions |
|---|---:|---:|
| A — no folder | 8 | 0/8 |
| B — specialist | 77 | 7/8; U8 partial |
| C — sources only | 80 | 8/8 |

| Arm | U1 | U2 | U3 | U4 | U5 | U6 | U7 | U8 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 7 |
| C | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |

B beats A on all eight; B vs C is **0 wins / 7 ties / 1 loss**. B lost U8 by three points for stating only the restrictive reading of an ambiguous authorized-prohibited-vendor branch when the frozen criterion required both readings. It did not falsely authorize a purchase. U mean session times were A13.6/B21.7/C22.6 seconds.

U questions were generated in a separate Claude session using the primary documents, according to the supplied authoring note. Same-family authors/assessors and operator exposure are disclosed. Human or cross-family independence and moderator acceptance are not claimed. Their two-assessor records remain in evaluation/unseen-20261013/; that assessment method is not attributed to the new seven-question run.

## What changed in the folder because of the findings
**Nothing:** the specialist remains frozen and unchanged. This revision changes the official question selection, runner suite and reporting, not the specialist. A candidate future improvement is to require both supported readings when provisions conflict; it would need a new specialist version and new unseen tests. We did not tune the specialist against U8 or erase its loss.

## Limits and history
One fresh round in fixed A/B/C order on the same machine/account, inherited user configuration, Claude Code CLI rather than the Projects walkthrough, no controllable temperature or observable server model revision, and a small near-ceiling set. Exact future answers and totals are not guaranteed. The U8 result cannot establish a causal compression failure.

[Complete earlier v1/v2/H/U results](history/results-before-seven.md) retain all original question-level scores, timing, failures, exclusions and hypotheses. Historical v2 totals remain A14/B80/C80 and were not relabeled. Frozen historical files retain their original paths/status descriptions. Current reproduction instructions are in REPRODUCE.md.
