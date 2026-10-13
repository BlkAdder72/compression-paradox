# Assessor instructions — U1–U8 (frozen before scoring)

Score the responses in `packet/packet.md`. Use only that file and this file. Do not open the mapping, evidence folders, policy files or other assessors' output, and do not try to infer which arm produced a response.

## Rubric (verbatim, `evaluation/scoring-rubric.md`)

# Precommitted grading rubric v1.0

Each answer receives 0–10 points: conclusion (0–4), applicable rules (0–2), exceptions/dependencies (0–2), evidence references (0–1), unsupported claims (0–1). Total: 80.

**Conclusion (4):** 4 if fully correct; 2 if partly correct but missing a material requirement; 0 if incorrect or no supported answer. **Applicable rules (2):** 2 if all mandatory approvals/prohibitions are recognized; 1 if partial; 0 if absent or wrong. **Exceptions/dependencies (2):** 2 if all relevant exceptions/cross-document/time conditions are correctly handled; 1 if partially handled without reversing outcome; 0 otherwise. If no exception applies, accurately not inventing an exception earns 2. **Evidence (1):** 1 only if the answer names at least one correct section identifier AND includes no false source identifier; 0 otherwise. **Unsupported claims (1):** 1 if there are no material unsupported claims; 0 otherwise.

**Hard cap:** If the final operational conclusion is wrong, total score cannot exceed 4. Missing a required approval constitutes a wrong operational conclusion. **No policy access:** Correct answers from a no-folder control may be scored on their merits, but generic assertions of unknowability do not earn conclusion points when the underlying answer is checkable; appropriate transparent uncertainty is described separately in results.

Secondary metrics, reported separately: critical omissions (by Q against the answer key), false authorizations (Q4 and Q8, and Q7 if waiver asserted), unsupported material assertions, visible source reads, measured wall time when tooling supports it, and run-to-run consistency. Never estimate token usage as measured tokens or treat a citation as proof the source was read.

A blinded assessor should score raw responses using this precommitted key, without changing the rubric after seeing outputs. Disagreements are logged and adjudicated. No fabricated or reconstructed transcripts are admissible.

## Frozen U-series evaluation rules (verbatim from `evaluation/unseen-20261013/REVIEW-AND-RUN-PLAN.md`, committed before any run)

## Frozen evaluation rules

Use the existing 0–10 rubric per question (maximum 80 per arm), applied to all subparts. Conclusion 0–4; applicable rules 0–2; exceptions/dependencies 0–2; evidence 0–1; unsupported claims 0–1. An omitted mandatory approval or false authorization makes the operational conclusion wrong and caps the total at 4. Evidence credit requires an existing, correctly used policy section ID and no false section ID; a file:line reference alone is insufficient.

For U6 and U8's disputed branch, a fully correct answer must acknowledge both supported readings and their consequences. An unjustifiably definitive interpretation loses relevant conclusion/exception credit; it is not automatically a false authorization when the stated interpretation is textually supported. Failure to require manager approval, required travel-office approval or written compliance authorization is a material error regardless of the disputed finance waiver. Report ambiguity-related deductions separately.

Use two blinded assessors if available, disclose their model family and conflicts, preserve both score sets, record every disagreement and written adjudication. Each score must include U-ID, category scores, capped total, conclusion_wrong, false_authorization, critical omissions and explanatory notes. No comparison score has been produced by this acceptance review.

U8's gold omits an explicit restatement of 24-hour notice in its authorized-prohibited-vendor branch. Under the permissive reading, EMG-1 still requires that notice; under the restrictive reading, advance finance approval remains necessary. This evaluator clarification is frozen here before any U-series run; the original authored files remain unchanged. Conservative advice to obtain finance approval must be distinguished from an assertion that the policy unambiguously requires it.

## Recording rules (operational, set before scoring)
- Max 10 per question. Every lettered subpart counts toward the single per-question score. Missing or wrong subparts reduce conclusion, rules or exceptions as the rubric directs.
- The policy's real section IDs are EXP-1–4, TRV-1–2, EMG-1–3, VEN-1–3, AMD-1–3 and DEF-1–3. Any other section ID is false.
- **evidence:** 1 if at least one real ID is used correctly and no false ID appears.
- **evidence_strict:** 1 only if at least one cited ID appears in that question's gold or critical requirements, and no false ID appears. `capped_total` uses `evidence`.
- **ambiguity_deduction:** points lost only because of the U6 / U8-prohibited-branch both-readings criterion. 0 elsewhere.
- **false_authorization:** true if the response permits proceeding while omitting a mandatory approval (manager, travel office where required, written compliance authorization). Asserting a textually supported finance-waiver reading is not by itself a false authorization.
