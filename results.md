# Results — actual Claude Projects UI replication

All 21 calls completed in A_UI_01/B_UI_01/C_UI_01 with displayed Opus 5.5 Medium / Manual, the same seven prompts and order, and a fresh chat per question. The frozen UI plan at 1318b4b preceded calls. Complete raw evidence was committed and pushed at **5f52b52 before assessment**. The ungraded capture manifest stays frozen; assessment is a separate file. These are actual rendered UI responses, not CLI results relabeled as Projects.

| Arm | Q1 | Q2 | Q3 | Q5 | Q6 | Q7 | Q8 | Total /70 | Full conclusions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| A — no files | 1 | 1 | 1 | 1 | 1 | 4 | 4 | 13 | 0/7 |
| B — specialist | 10 | 10 | 10 | 10 | 4 | 10 | 10 | 64 | 6/7 |
| C — sources only | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 70 | 7/7 |

- B vs A and C vs A: **7 wins / 0 ties / 0 losses** each.
- B vs C: **0 wins / 6 ties / 1 loss**, on Q6's before-purchase timing.
- False authorizations: none observed in any UI arm.
- UI speed: **not measured reliably**. Start/capture timestamps include automation, waits and interruptions; no UI slower/faster inference or token count is claimed. Earlier CLI durations below are a separate measure.

## UI scoring judgments and sensitivity
One unblinded Codex assessor, with prior experiment knowledge, applied the unchanged 0/2/4 conclusion, 0–2 rules, 0–2 exceptions, 0/1 evidence and 0/1 unsupported-claims categories. Missing a mandatory approval condition invokes the operational four-point cap. This is not independent human grading or two-assessor agreement. [Per-answer rationales and raw hashes](evaluation/projects-20261013/assessment-codex.json) and [computed summary](evaluation/projects-20261013/summary.json) are checked by `python scripts/score_projects.py --check`; the script verifies arithmetic/provenance, not semantic judgments.

**B Q6 is the material judgment.** It correctly names both manager and finance and the historic $2,000 threshold, but says: “I can’t confirm from the text that they had to be obtained in advance.” The frozen gold explicitly says both before purchase. Scores are 2/1/1/1/1, capped at 4 for the missing timing requirement. This is cautious refusal to confirm timing, not authorization to proceed. AMD-1 alone omits timing; AMD-3 says only the threshold changed. C supplies both approvals before purchase and receives full credit.

The earlier CLI assessment below accepted a similar B Q6 caveat as fully correct. That historical judgment is preserved and this stricter UI application is made explicit. **Sensitivity:** accepting the caveat in this UI answer restores B to 70 and produces seven B/C ties. The six-point loss should therefore not be presented as a robust causal compression failure. Under either treatment, the added specialist architecture shows no accuracy advantage over sources alone.

A Q1/Q2/Q3/Q5/Q6 transparently decline without policy access: 0/0/0/0/1. This sensible uncertainty does not provide the checkable policy answers. A Q7 identifies probable nonqualification and ordinary approval but omits both approvers: 2/0/1/0/1, capped at 4. A Q8 predicts probably no and conditionally preserves manager approval: 2/1/1/0/0 = 4. Its claim that the employee would still owe retroactive approval/documentation introduces an unsupported requirement. It does not authorize bypassing the manager. B's other six and all C answers earn 4/2/2/1/1.

C Q3's calendar illustration is conditional on the purchase having occurred; its relative 24-hour notice and approval requirements are correct. Statements about no triggered vendor restriction on unspecified routine facts were not treated as permission to use a known prohibited vendor. These are exposed judgment calls, not hidden adjudication.

## UI evidence, access and workflow
Exact prompt, complete response article, main DOM, model label and chat URL are retained for each question. A/B direct copies in control/raw/A_UI_01 and treatment/raw/B_UI_01 match evidence/projects-20261013; each answer is scored once. A Q1's zero-byte clipboard file remains, and its same-original-chat recovered article is the selected response. The original interruption STATUS.md remains historical; COMPLETION.md records completion.

A had zero project files. B imported ten unchanged specialist texts; C imported only six unchanged fixture texts. Original bytes and submitted text hashes were checked. B/C used Add text content with path/filename titles because file upload was unavailable; no hidden-storage equivalence is claimed. Separate clean projects in A/B/C order differ from literally adding and removing a folder in one project. Account memory was off, per-chat Memory off, and final project memory empty. Research/external connectors were visibly off. A still searched empty knowledge and discovered a connector directory; no outside policy content was observed. A Q2's saved preflight shows the Devices submenu; its connector-off inspection is described in the pre-Q2 resume record rather than saved in that same snapshot. Desktop-connected availability prevents claiming complete hidden isolation. A Q1 used Chrome, later calls Edge; the clean-context continuation resumed only the remaining B3/C7.

The captures are not provider raw streams, hidden traces, token measurements or proof of a fixed backend revision. B/C's use of section IDs is not by itself proof of individual document reads. One fixed-order round and a small near-ceiling set limit inference. No specialist changes were made after results: a future timing-clarity or ambiguity-handling revision would require a new version and fresh tests.

The original separate key, post-results seven-question selection, same-family supplementary authoring and all previous attempts remain disclosed below. This experiment provides reviewable evidence, not a promise of moderator acceptance.

---

# Earlier CLI results — seven original questions, fresh execution

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
