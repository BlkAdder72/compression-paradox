# U1–U8 acceptance and prospective run plan

Status: accepted as separately authored Claude challenge inputs; no model calls, scores or demonstrated advantage yet. Both supplied files are retained byte-for-byte. Provenance is the author's self-report, not independently authenticated: separate source-only Claude session, configured claude-opus-5-5, unrelated account-profile context disclosed. No human or cross-family independent review is claimed.

## Input review before testing

All eight questions have unique IDs and complete standalone scenarios; no Q4-style cross-question dependency. JSON schema, all cited sections, arithmetic, threshold dates and approval dependencies were checked against the six fixture documents. All 18 section headings exist. Only prompt fields go to model sessions; gold answers and critical requirements remain evaluator-only.

U1/U2/U3/U4/U5/U7 have determinate policy answers as written. U6 and the authorized-prohibited-vendor branch of U8 deliberately test a textual tension: EMG-1 requires an approved vendor, VEN-3 defines that designation, while EMG-2 describes compliance authorization as an exception to the prohibited-vendor restriction. The author requires both readings and consequences rather than silently choosing one. This differs from some earlier benchmark judgments. It is a new challenge criterion, not a retroactive revision of old scores.

U8's gold omits an explicit restatement of 24-hour notice in its authorized-prohibited-vendor branch. Under the permissive reading, EMG-1 still requires that notice; under the restrictive reading, advance finance approval remains necessary. This evaluator clarification is frozen here before any U-series run; the original authored files remain unchanged. Conservative advice to obtain finance approval must be distinguished from an assertion that the policy unambiguously requires it.

The author's statement that every category is covered at least twice is broader than the scenarios support: only U2 directly contrasts the historical and current thresholds. Treat the coverage table as descriptive; do not infer balanced difficulty or statistical power.

## Frozen evaluation rules

Use the existing 0–10 rubric per question (maximum 80 per arm), applied to all subparts. Conclusion 0–4; applicable rules 0–2; exceptions/dependencies 0–2; evidence 0–1; unsupported claims 0–1. An omitted mandatory approval or false authorization makes the operational conclusion wrong and caps the total at 4. Evidence credit requires an existing, correctly used policy section ID and no false section ID; a file:line reference alone is insufficient.

For U6 and U8's disputed branch, a fully correct answer must acknowledge both supported readings and their consequences. An unjustifiably definitive interpretation loses relevant conclusion/exception credit; it is not automatically a false authorization when the stated interpretation is textually supported. Failure to require manager approval, required travel-office approval or written compliance authorization is a material error regardless of the disputed finance waiver. Report ambiguity-related deductions separately.

Use two blinded assessors if available, disclose their model family and conflicts, preserve both score sets, record every disagreement and written adjudication. Each score must include U-ID, category scores, capped total, conclusion_wrong, false_authorization, critical omissions and explanatory notes. No comparison score has been produced by this acceptance review.

## Freeze and execution

The specialist is unchanged. `input-manifest.json` binds its files, fixture, author files and rubric. Commit this plan and inputs before any call. Do not tune the specialist after reading U1–U8. The operator/reviewer has now seen the questions; that does not make the specialist independently authored or conceal operator exposure.

Run one round in A, B, C order, one fresh session per U-question, identical model/CLI/flags. A has no documents; B the specialist; C primary sources only. Record fixed-order limitation; later repetitions should counterbalance order. Stop on failure, retain the attempted capture directory, and use a new run ID for any retry. Commit raw evidence before assessor packets or scores. Copy captures byte-for-byte into `evidence/unseen-20261013/` and add root control/treatment pointers for judges. Inspect outside reads and record exclusions before grading.

From a clean committed checkout with authenticated Claude CLI:

```text
python scripts/verify_unseen.py
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm A --run-id A_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures --dry-run
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm A --run-id A_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm B --run-id B_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm C --run-id C_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures
python scripts/prepare_blind.py --questions evaluation/unseen-20261013/external-questions.json --run A=C:/paradox-u-captures/A_U_01 --run B=C:/paradox-u-captures/B_U_01 --run C=C:/paradox-u-captures/C_U_01 --output C:/paradox-u-grading/U_01
```

Supply an accessible native CLI path using `--claude` if necessary. Replace example directories with writable absolute paths. Give assessors packet.md, the rubric and these frozen scoring clarifications; withhold mapping.json. Note recognizable arms and source-availability confounding. B/C is the incremental architecture comparison. Report per-question wins, losses, ties, latency and failures. Do not describe a folder advantage until observed.

The corrected official v2 A/B/C runs remain a separate pending requirement. The public GitHub repository and submission are still pending. Moderator acceptance of same-family separately generated questions is not guaranteed by this review.
