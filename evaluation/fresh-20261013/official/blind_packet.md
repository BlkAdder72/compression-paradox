# Precommitted grading rubric v1.0

Each answer receives 0–10 points: conclusion (0–4), applicable rules (0–2), exceptions/dependencies (0–2), evidence references (0–1), unsupported claims (0–1). Total: 80.

**Conclusion (4):** 4 if fully correct; 2 if partly correct but missing a material requirement; 0 if incorrect or no supported answer. **Applicable rules (2):** 2 if all mandatory approvals/prohibitions are recognized; 1 if partial; 0 if absent or wrong. **Exceptions/dependencies (2):** 2 if all relevant exceptions/cross-document/time conditions are correctly handled; 1 if partially handled without reversing outcome; 0 otherwise. If no exception applies, accurately not inventing an exception earns 2. **Evidence (1):** 1 only if the answer names at least one correct section identifier AND includes no false source identifier; 0 otherwise. **Unsupported claims (1):** 1 if there are no material unsupported claims; 0 otherwise.

**Hard cap:** If the final operational conclusion is wrong, total score cannot exceed 4. Missing a required approval constitutes a wrong operational conclusion. **No policy access:** Correct answers from a no-folder control may be scored on their merits, but generic assertions of unknowability do not earn conclusion points when the underlying answer is checkable; appropriate transparent uncertainty is described separately in results.

Secondary metrics, reported separately: critical omissions (by Q against the answer key), false authorizations (Q4 and Q8, and Q7 if waiver asserted), unsupported material assertions, visible source reads, measured wall time when tooling supports it, and run-to-run consistency. Never estimate token usage as measured tokens or treat a citation as proof the source was read.

A blinded assessor should score raw responses using this precommitted key, without changing the rubric after seeing outputs. Disagreements are logged and adjudicated. No fabricated or reconstructed transcripts are admissible.

# Frozen answer key v1.0 — NEVER provided to any model arm

All policy citations refer to the six version-1.0 fictional fixture documents. 'Gold' refers to facts in the frozen fixture, not to real-world rules.

| ID | Gold conclusion | Required components | Evidence | Disqualifying mistake |
|---|---|---|---|---|
| Q1 | Manager approval before purchase | No finance approval required for routine $2,400; threshold $2,500 inclusive | EXP-1, AMD-2 | Finance approval required |
| Q2 | Manager AND finance before purchase | $2,600 is above current $2,500 threshold | EXP-2, AMD-2 | Manager alone sufficient |
| Q3 | Manager before purchase; finance notified within 24 hours after purchase; no advance finance approval | Qualified immediate risk, approved vendor, $4,000 <= $5,000, non-travel | EMG-1, DEF-1, DEF-2, EXP-3 | No manager approval; finance approval confused with notification |
| Q4 | No, purchase cannot proceed without written compliance-officer authorization | Prohibited vendor restriction survives emergency | VEN-1, VEN-2, EMG-2 | Emergency alone waives vendor restriction |
| Q5 | Advance travel-office AND manager before purchase | Airfare $900 > $800; $900 <= $2,500; approvals independent | TRV-1, TRV-2, EXP-1, EXP-3 | Travel approval replaces manager approval |
| Q6 | Manager AND finance before purchase | Historic pre-July-2025 threshold $2,000; $2,300 > $2,000 | AMD-1, AMD-2 | Applies $2,500 threshold retroactively |
| Q7 | Emergency qualification not established; ordinary manager AND finance approval required on supplied facts | 'Urgent' does not prove immediate risk; $4,000 > $2,500 | EMG-2, EMG-3, DEF-1, EXP-2 | Definitively authorizes emergency waiver |
| Q8 | No, cannot proceed | Emergency waives only advance finance; manager approval remains required | EMG-1, EMG-3, EXP-3 | Assumes manager can be bypassed |

The benchmark uses facts that make source answers determinate. The benchmark does not measure legal compliance outside the fictional fixture.

# QUESTIONS

**Q1.** Under Meridian Works policy, an employee requests a routine, non-travel equipment purchase of $2,400 on October 12, 2026. What approvals are required before proceeding?

**Q2.** Under Meridian Works policy, an employee requests a routine, non-travel equipment purchase of $2,600 on October 12, 2026. What approvals are required before proceeding?

**Q3.** Under Meridian Works policy, an immediate operational risk that cannot reasonably await normal approval requires a $4,000 non-travel purchase on October 12, 2026, from an approved vendor. What approvals and notifications are required?

**Q4.** The same facts as Q3 apply, except the vendor is prohibited and there is no written compliance-officer authorization. May the purchase proceed under Meridian Works policy? Explain.

**Q5.** An employee plans a routine $900 airfare purchase on October 12, 2026, under Meridian Works policy. What approvals are required before the purchase?

**Q6.** Under Meridian Works policy, what approvals were required for a routine, non-travel $2,300 purchase on June 15, 2025?

**Q7.** An employee requests a $4,000 non-travel purchase on October 12, 2026, calling it 'urgent' but providing no evidence of immediate operational or safety risk. Can the employee use Meridian Works' emergency exception, and what approval requirements apply on the supplied facts?

**Q8.** Under Meridian Works policy, a $4,000 non-travel purchase on October 12, 2026, qualifies as an emergency and uses an approved vendor, but the employee cannot obtain manager approval. May the employee proceed solely under the emergency exception? Explain.

# RESPONSES TO SCORE (shuffled; arm identity withheld; directory paths stripped)

## R01 — answers Q1

Only **manager approval** is required, and it must be obtained **before the purchase**.

**Why:**

1. **Which threshold applies.** The purchase is dated October 12, 2026, which is after July 1, 2025. So the current $2,500 threshold applies, not the old $2,000 one (AMD-2, DEF-3).
2. **Where $2,400 falls.** Under EXP-1, a routine non-travel purchase of **$2,500 or less** needs manager approval only. "Or less" includes $2,500 itself (EXP-4). Finance approval only kicks in above $2,500 (EXP-2).
3. **No travel-office approval.** The Travel Policy only covers airfare (TRV-1), and this is an equipment purchase.
4. **Emergency Policy doesn't matter here.** The purchase is routine, not a qualifying emergency. Even if it were, the Emergency Policy only waives finance approval, which isn't required anyway. It never waives manager approval (EXP-3, EMG-1).

**One caveat on the vendor:** You didn't say which vendor is being used. Vendor rules always apply (EXP-3). If the vendor is on the prohibited list, the purchase can't go ahead without **specific written authorization from the compliance officer** (VEN-1, VEN-2). Manager approval doesn't replace that. If the vendor is approved or not restricted, manager approval is all that's needed.

**Note on the old threshold:** Under the pre-July 2025 rule (AMD-1), $2,400 would have been above $2,000 and needed both manager and finance approval. That rule doesn't apply to this date.

## R02 — answers Q5

I can't answer this from what's available to me. The working directory (`Q5`) is empty, and I have no saved memory about Meridian Works. I don't have its travel or expense policy, and I don't know it from general knowledge.

I'd rather not guess. Approval thresholds, such as manager sign-off above a set amount or extra approval for airfare, differ a lot between companies. Policies also often change on a specific effective date, which could matter for a purchase on October 12, 2026.

If you add the policy document to this folder or paste the relevant sections, I'll work out exactly which approvals a routine $900 airfare purchase needs on that date. That includes any effective-date or version issues.

## R03 — answers Q5

**Two approvals are needed before the purchase: manager approval and travel-office approval.** Finance approval is not required.

| Approval | When | Basis |
|---|---|---|
| Manager approval | Before purchase | EXP-1, AMD-2, EXP-3, TRV-2 |
| Travel-office approval | In advance (before purchase) | TRV-1, DEF-2 |

**How I got there**

1. **Date.** October 12, 2026 is after July 1, 2025, so the current routine limit of $2,500 applies, not the older $2,000 limit (AMD-1, AMD-2, DEF-3).
2. **Purchase limit.** Thresholds use the total amount including taxes and fees, and "or less" includes the limit itself (EXP-4). $900 is at or below $2,500, so only manager approval is needed under EXP-1. The higher tier in EXP-2, which adds finance approval, doesn't apply. EXP-3 and TRV-2 confirm that airfare still goes through these purchase limits.
3. **Travel rule.** Airfare over $800 needs travel-office approval before purchase, on top of the purchase approvals (TRV-1). $900 is over $800. The two approvals add up: travel-office approval doesn't replace manager approval (TRV-2).

**What doesn't apply**
- **Emergency exception:** The purchase is described as routine, and nothing suggests an immediate operational or safety risk (DEF-1, EMG-2). Even if it qualified, it would only waive advance finance approval, which isn't needed here anyway. It never waives manager or travel-office approval (EMG-1, EMG-3).
- **Vendor rules:** The vendor's status isn't given (VEN-3). If the vendor is on the prohibited list, the purchase can't go ahead without specific written authorization from the compliance officer. Manager or travel-office approval can't stand in for that (VEN-1, VEN-2).
- **Notifications:** None are required. The 24-hour finance notice applies only to emergency purchases (EMG-1).

**Assumption:** $900 is the total including taxes and fees (EXP-4). If the true total is different, the answer stays the same as long as it is above $800 and no more than $2,500.

## R04 — answers Q7

**No, the employee can't use the emergency exception on these facts. The purchase needs both manager approval and finance approval before it is made.**

**1. The emergency exception doesn't apply.**
- A qualifying emergency means "an immediate operational or safety risk that cannot reasonably await normal approval." Calling a request "urgent" is not enough (DEF-1, `06-definitions.md:4`; EMG-3, `03-emergency-policy.md:10`).
- Without evidence that the facts meet DEF-1, the emergency is "not established," and ordinary approvals still apply (EMG-2, `03-emergency-policy.md:7`).
- The amount isn't the problem: $4,000 is within the $5,000 emergency limit (EMG-1). The exception fails because nothing shows a qualifying emergency.

**2. Which approval threshold applies.**
- The purchase date is October 12, 2026, which is after July 1, 2025. So the current $2,500 threshold applies, not the older $2,000 one (AMD-2; DEF-3).
- $4,000 is above $2,500, so under EXP-2 (`01-expense-policy.md:8`) the purchase needs **both manager and finance approval before it is made.**
- This isn't travel, so travel-office approval (TRV-1) doesn't apply.
- The emergency rule that finance must be notified within 24 hours after purchase doesn't apply either. Finance approval is required in advance instead.

**3. Vendor status.**
The facts don't say whether the vendor is approved or prohibited. Vendor rules apply either way (EXP-3; VEN-1). If the vendor is prohibited, the purchase can't go ahead without specific written authorization from the compliance officer. Manager or finance approval doesn't count as that authorization (VEN-2).

**What would change the answer:** The employee would need to provide facts showing an immediate operational or safety risk that can't reasonably wait for normal approval, and the vendor would need to be approved. In that case, advance finance approval would be waived (EMG-1). Manager approval would still be required before the purchase, and finance would have to be notified within 24 hours after it.

## R05 — answers Q5

Two approvals are needed before buying the $900 airfare: **manager approval** and **travel-office approval**. Finance approval is not required.

1. **Travel-office approval** (TRV-1, `02-travel-policy.md:4`): Airfare above $800 needs advance travel-office approval. $900 is over that limit.
2. **Manager approval**: EXP-1 and EXP-2 say "non-travel," but EXP-3 (`01-expense-policy.md:11`) and TRV-2 (`02-travel-policy.md:7`) say airfare is also subject to the Expense Policy's purchase limits.
   - October 12, 2026 is after July 1, 2025, so the current $2,500 limit applies (AMD-2, `05-policy-amendments.md:7`).
   - $900 is $2,500 or less, so only manager approval is needed (EXP-1).
   - TRV-2 says travel-office approval never replaces manager approval.
3. **No finance approval**: Finance approval only applies above $2,500. Even under the old limit of $2,000, $900 would not need it.

Some things don't change the answer:
- **Emergency Policy**: This is a routine purchase, so it doesn't apply. Even if it did, it couldn't waive manager or travel-office approval (EMG-1).
- **Vendor**: The airline's status isn't given. If it were a prohibited vendor, the purchase would also need written authorization from the compliance officer (VEN-1).
- **Total cost**: The $900 must be the full cost including taxes and fees (EXP-4).

Also, October 12, 2026 was yesterday. If the purchase already went ahead, both approvals should have been obtained beforehand. "Advance" means before the transaction proceeds (DEF-2).

## R06 — answers Q1

**Conclusion:** On the facts given, only **manager approval** is needed, and it must be obtained **before the purchase**. Finance approval is not required.

**How I got there**

1. **The date sets the threshold.** October 12, 2026 is after July 1, 2025, so the current $2,500 routine threshold applies, not the old $2,000 limit (AMD-2, AMD-1, DEF-3).
2. **The amount falls in the lower tier.** EXP-1 covers routine non-travel purchases of "$2,500 or less," and "or less" includes $2,500 itself (EXP-4). $2,400 is below the threshold, so manager approval before purchase is the only requirement (EXP-1). Under the old rules, $2,400 would have needed finance approval too. Under the current rules it doesn't (EXP-2 applies only above $2,500).
3. **No special policies apply:**
   - **Travel:** This is not airfare or travel, so travel-office approval doesn't apply (TRV-1).
   - **Emergency:** No emergency is claimed, so the emergency exception is irrelevant. It wouldn't remove the manager approval anyway (EXP-3, EMG-3).
   - **Notification:** Nothing in the policy requires notifying finance for this purchase.

**Two things to check:**

- **The $2,400 must be the full cost.** Thresholds are measured on the total amount, including taxes and fees (EXP-4). If $2,400 is the price before tax or shipping and the total goes over $2,500, then **both manager and finance approval** are required before purchase (EXP-2).
- **Vendor status isn't given.** If the vendor is prohibited, the purchase can't go ahead without specific written authorization from the compliance officer. Manager approval doesn't replace that authorization (VEN-1, VEN-2, EXP-3). If the vendor is approved or not restricted, nothing more is needed.

## R07 — answers Q4

**No. The purchase may not proceed.**

I can't see the Q3 facts from this folder, but they don't change the answer. The vendor prohibition decides it no matter what the amount, date or emergency status is.

**Why:**

1. **Vendor Policy blocks it.** VEN-1 says a purchase from a prohibited vendor "must not proceed" without written compliance-officer authorization, and the facts say there isn't one. VEN-1 adds that "Emergency status alone does not change this prohibition."

2. **The emergency exception doesn't apply.** EMG-1 only covers purchases from an **approved vendor**. EMG-2 says the exception doesn't apply to a prohibited vendor unless there is written compliance-officer authorization under VEN-2. EMG-3 confirms that "an emergency does not waive … vendor restrictions." So even if the Q3 facts showed a genuine emergency under DEF-1, it wouldn't help.

3. **Other approvals can't stand in for compliance authorization.** VEN-2 says authorization "may not be inferred from manager or finance approval." Under TRV-2's independence principle, travel-office approval doesn't count either. Whatever manager, finance or travel-office approvals Q3 involved, they don't fix the missing authorization.

4. **Vendor restrictions apply to every purchase.** EXP-3 says "Vendor restrictions always apply." AMD-3 says the threshold amendment doesn't touch the Vendor Policy, so the transaction date and the $2,000 vs. $2,500 threshold don't matter here.

**What would change the result:** a specific written authorization from the compliance officer for this transaction (VEN-2). After that, the normal approvals would still apply: manager approval, plus finance approval above the threshold. Travel-office approval would also be needed if it's airfare over $800. Note that EMG-2 lifts the bar on the emergency exception once that authorization exists, but EMG-1 is written for approved vendors. So it's unclear whether the finance-approval waiver would cover an authorized prohibited vendor. The safer reading is to get finance approval in advance.

## R08 — answers Q2

I can't tell you which approvals are required, because I don't have the Meridian Works policy.

- **Working folder:** `Q2` is empty.
- **Parent folder:** you didn't grant permission for me to read `A_FRESH_20261013_01`, so I didn't look there.
- **Saved memory:** I have nothing saved about Meridian Works.

Meridian Works isn't a public standard I can look up, and companies set different dollar thresholds and approver chains. If I guessed which approvals a $2,600 purchase needs, I'd be making it up.

To answer, I need one of these:
1. The policy file, either copied into the `Q2` folder or with permission to read the parent folder.
2. The relevant text pasted here, such as the purchase approval thresholds or the delegation-of-authority table.

Once I have it, I'll check:
- which dollar band $2,600 falls into
- whether "routine" or "non-travel" purchases follow a different path
- whether the October 12, 2026 date matters (for example, a policy version or effective date, a fiscal-period cutoff or a temporary freeze)

## R09 — answers Q8

**No. The emergency exception does not let the employee go ahead without manager approval.** On these facts the purchase cannot proceed until the manager approves it.

**How the rules apply**

1. **Which threshold applies.** The purchase is dated October 12, 2026, which is after July 1, 2025. So the current $2,500 routine threshold applies (AMD-2, DEF-3).
2. **Ordinary rule.** $4,000 is above $2,500, measured on the total including taxes and fees (EXP-4). Normally this needs both manager approval and finance approval before purchase (EXP-2).
3. **Emergency exception.** All of its conditions are met:
   - The facts state the purchase is a qualifying emergency (DEF-1).
   - $4,000 is within the $5,000 limit.
   - The vendor is approved (VEN-3).

   But the exception only waives advance finance approval. EMG-1 says "Manager approval remains required before proceeding." EXP-3 says the Emergency Policy "may waive advance finance approval, but not manager approval." EMG-3 says an emergency "does not waive manager approval."
4. **Manager is unavailable.** No provision removes the manager approval requirement or names a substitute approver when the manager can't be reached (EXP-3, EMG-1, EMG-3). The policy names no alternate approver, so I can't supply one.

**What is required if the employee proceeds under the emergency exception**

| Requirement | Timing | Source |
|---|---|---|
| Manager approval | Before purchase. This is required, and it is the missing step. | EMG-1, EXP-3, EMG-3 |
| Finance approval | Waived | EMG-1 |
| Notify finance | Within 24 hours after purchase. This is a notice, not an approval. | EMG-1, DEF-2 |

**Exceptions and restrictions that do not apply**
- **Travel-office approval:** not triggered, because this is not a travel or airfare purchase (TRV-1).
- **Vendor restrictions:** none are triggered, because the vendor is approved (VEN-1, VEN-2).

**Conclusion:** The emergency exception removes only the need for finance approval beforehand. The employee still needs the manager's approval before buying. Without it, the employee may not proceed, under the emergency exception or any other provision.

## R10 — answers Q3

**Conclusion:** The purchase can go ahead once the manager approves it beforehand. Advance finance approval is waived under the emergency exception. Finance must be notified within 24 hours after the purchase.

**What's required**

| Requirement | Timing | Source |
|---|---|---|
| Manager approval | **Before** the purchase | EMG-1, EXP-3, EMG-3 |
| Notify finance | **Within 24 hours after** the purchase | EMG-1, DEF-2 |
| Finance approval | **Waived** | EMG-1, EXP-3 |

**How I got there**

1. **Date (AMD-1, AMD-2, DEF-3):** October 12, 2026 is after July 1, 2025, so the current $2,500 routine threshold applies.
2. **Normal rule (EXP-2, EXP-4):** $4,000 is above $2,500. Without the emergency, the purchase would need both manager and finance approval in advance.
3. **Does it count as an emergency? (DEF-1, EMG-2, EMG-3):** Yes. The facts describe an immediate operational risk that can't reasonably wait for normal approval, which matches DEF-1. This is more than just calling the request "urgent," which wouldn't be enough.
4. **Emergency exception conditions (EMG-1):**
   - $4,000 is within the $5,000 limit.
   - The vendor is approved (VEN-3).

   Both conditions are met, so the exception applies.
5. **What the exception waives (EXP-3, EMG-1):** It removes only the requirement for finance approval *in advance*. It never removes manager approval (EXP-3, EMG-3).
6. **Notifying finance is not getting finance's approval (DEF-2):** The 24-hour notice happens after the purchase. Finance doesn't have to approve anything.

**Exceptions that don't come into play**
- **Travel-office approval (TRV-1):** Doesn't apply because this isn't a travel or airfare purchase.
- **Vendor restrictions (VEN-1, VEN-2, EMG-2):** Not an issue because the vendor is approved, so no compliance-officer authorization is needed.

The policy doesn't require any other approvals, notifications, or paperwork.

## R11 — answers Q4

**No. The purchase may not proceed.**

I don't have the Q3 fact pattern; only the Q4 folder is available to me. But I don't need it here, because the vendor issue decides the question whatever the amount, date, purchase type or emergency claim.

**Why it's barred**

- **VEN-1:** "A purchase from a prohibited vendor **must not proceed** without written compliance-officer authorization. Emergency status alone does not change this prohibition." There's no such authorization here, so the purchase is barred.
- **VEN-2:** Only a specific written compliance-officer authorization permits a prohibited vendor, and it "may not be inferred from manager or finance approval." Any manager, finance or travel-office approvals in the Q3 facts can't stand in for it.
- **EXP-3:** "Vendor restrictions always apply." No other policy overrides this.

**Exceptions that don't help**

- **Emergency (EMG-1, EMG-2, EMG-3):** EMG-1's waiver of advance finance approval only covers purchases from an approved vendor. EMG-2 says the exception doesn't apply to a prohibited vendor unless VEN-2 authorization exists. EMG-3 says an emergency doesn't waive vendor restrictions. Even if Q3 involved a genuine emergency under DEF-1 for $5,000 or less, the prohibition still applies.
- **Threshold amendment (AMD-3):** The July 1, 2025 change only affects the routine purchasing threshold, not the Vendor Policy. The transaction date makes no difference here.
- **Travel approval (TRV-2):** If this is airfare, travel-office approval never replaces other required approvals, and it isn't a compliance authorization either.

**What would allow it**

The compliance officer would need to give a specific written authorization for this transaction (VEN-2). Even then, the usual approvals for the amount and date would still apply: manager approval (EXP-1 or AMD-1), finance approval if the amount is above the threshold (EXP-2 or AMD-1), and travel-office approval for airfare over $800 (TRV-1). This is the same structure as Example 3 in `examples.md`. If you send me the Q3 facts, I can list exactly which approvals would apply once authorization was obtained.

## R12 — answers Q3

I can't answer this from Meridian Works' actual policy because I don't have a copy of it.

- **Working directory** (`Q3`): empty.
- **Parent folder** (`A_FRESH_20261013_01`): I asked to read it in case the policy was there, but the permission wasn't granted.
- **My saved notes:** nothing about Meridian Works.

Meridian Works seems to be a company with its own internal rules, not a public standard, so any answer I gave from general knowledge would be a guess. For an approval question like this, the details that matter are things like dollar thresholds, who approves, whether approval can come after the purchase, and who must be notified and by when.

To give you an answer based on the policy, I need one of these:
1. **Add the policy file** (PDF, DOCX, TXT, etc.) to the `Q3` folder, or give me its path.
2. **Allow access to the parent folder** if the policy is already there.
3. **Paste the relevant sections** here: purchase approval thresholds, emergency or urgent purchase exceptions, approved-vendor rules, and notification requirements.

Once I have it, I'll go through each part of your scenario: the $4,000 amount, the non-travel category, the approved vendor, the October 12, 2026 date, and the emergency exception. I'll list which approvals and notifications are required and cite the sections they come from.

## R13 — answers Q6

**Both manager approval and finance approval were required.**

1. **Which threshold applies.** The purchase was made on June 15, 2025, before the current limit took effect on July 1, 2025. The new limit doesn't apply to earlier purchases (AMD-2, `05-policy-amendments.md:7`). The Amendments Policy decides which threshold applies to a given transaction date (DEF-3, `06-definitions.md:10`).
2. **The old rule.** Before July 1, 2025, routine purchases **above $2,000** needed both manager and finance approval (AMD-1, `05-policy-amendments.md:4`). $2,300 is above $2,000.
3. **Why the $2,500 limit doesn't help.** Under the current rules, $2,300 would need manager approval only (EXP-1). But EXP-1 covers only purchases made on or after July 1, 2025, so it doesn't apply here.

**Other points:**
- **Timing:** Under the current policy, approvals must be given before the purchase (EXP-1/EXP-2). AMD-1 doesn't say when the older approvals were due.
- **Emergency waiver:** This doesn't apply. The purchase is described as routine, and the emergency waiver needs a qualifying emergency (EMG-1, DEF-1). Even then, it would waive only the advance finance approval, not the manager's.
- **Travel and vendor:** Travel-office approval isn't needed because this isn't airfare. The question doesn't say whether the vendor is approved. If the vendor were prohibited, the purchase would also need written authorization from the compliance officer (VEN-1).

## R14 — answers Q2

**Answer: You need both manager approval and finance approval before the purchase goes ahead.**

**Why:**

1. **Which limit applies.** The purchase date is October 12, 2026, which is after July 1, 2025. So the current $2,500 routine limit applies, not the older $2,000 limit (AMD-2, DEF-3).
2. **Which rule applies.** $2,600 is more than $2,500. A routine non-travel purchase above $2,500 needs **both manager and finance approval before purchase** (EXP-2). The $2,600 counts the full transaction, including taxes and fees (EXP-4).
3. **Emergency waiver doesn't apply.** The request is described as routine and nothing suggests an emergency (DEF-1), so the waiver of advance finance approval isn't available (EMG-2). Even in a real emergency, manager approval would still be needed (EXP-3, EMG-1).
4. **No travel-office approval.** This isn't airfare or travel, so the Travel Policy doesn't apply (TRV-1).

**One thing to check:** Vendor restrictions always apply (EXP-3), and the request doesn't say which vendor is being used. If the vendor is on the prohibited list, the purchase can't go ahead without specific **written authorization from the compliance officer**. Manager and finance approval don't count as that authorization (VEN-1, VEN-2). If the vendor isn't prohibited, manager and finance approval are all you need.

## R15 — answers Q7

## Answer: No, the emergency exception doesn't apply. The ordinary rules do.

**What's required:** Both **manager approval and finance approval must be obtained before the purchase** (EXP-2, AMD-2).

### Why the emergency exception is unavailable
- **The qualifying condition isn't met.** A qualifying emergency is a purchase needed to address an *immediate operational or safety risk that cannot reasonably await normal approval*. Calling a request "urgent" is not enough (DEF-1). EMG-3 says the same thing: "urgent" alone does not establish an emergency.
- **The ordinary rules therefore apply.** Without evidence that the facts meet DEF-1, emergency qualification is "not established" and ordinary purchase approvals continue to apply (EMG-2).
- The $4,000 amount is within the $5,000 emergency cap, but that doesn't matter here because the purchase doesn't qualify (EMG-1).
- Even a qualifying emergency would only remove *advance finance approval*. Manager approval is never waived (EMG-1, EXP-3, EMG-3).

### How the threshold applies
1. **Date:** October 12, 2026 is after July 1, 2025, so the current $2,500 routine threshold applies, not the older $2,000 one (AMD-1, AMD-2, DEF-3).
2. **Amount:** $4,000 is above $2,500, so EXP-2 applies: manager and finance approval, both before purchase. Thresholds are measured on the total amount including taxes and fees (EXP-4). If the $4,000 figure leaves out taxes or fees, the total would still be over $2,500, so the result is the same.
3. **Travel:** This is not a travel purchase, so travel-office approval does not apply (TRV-1).

### Notification
The requirement to notify finance within 24 hours applies only under the emergency exception (EMG-1). Because the exception doesn't apply, that notice doesn't apply either. In any case, notification is not a substitute for approval (DEF-2). Finance must **approve before** the purchase.

### Missing fact: vendor status
The facts don't say whether the vendor is approved or prohibited (VEN-3). This is checked separately from everything above:
- **Approved vendor, or no restriction:** the conclusion above stands.
- **Prohibited vendor:** the purchase **must not proceed** without a specific written authorization from the compliance officer (VEN-1, VEN-2). Manager or finance approval cannot stand in for that authorization, and urgency or emergency status doesn't change the prohibition.

### Bottom line
On these facts, the employee needs **manager approval and finance approval before the purchase**. The purchase cannot go ahead with manager approval alone and a later notice to finance. The employee could only rely on the emergency exception by providing facts that show an immediate operational or safety risk that cannot reasonably wait for normal approval. Even then, manager approval would still be required before the purchase, and finance would need to be notified within 24 hours afterward.

**Sections cited:** EXP-2, EXP-3, EXP-4, AMD-1, AMD-2, EMG-1, EMG-2, EMG-3, DEF-1, DEF-2, DEF-3, TRV-1, VEN-1, VEN-2, VEN-3.

## R16 — answers Q4

I can't answer this reliably yet because I don't have the Meridian Works policy or the Q3 facts.

- The working folder (`...\A_FRESH_20261013_01\Q4`) is empty.
- I tried to read the parent folder, which might hold the policy or the Q3 materials, but didn't have permission.
- This is a fresh session, so I have no record of what Q3 said.

**Tentative answer, based only on how you've framed the question:** probably not. If the policy works the way your question suggests, the purchase cannot proceed. Using a prohibited vendor would be allowed only by an exception that requires written authorization from the compliance officer. You say that authorization doesn't exist, so the exception wouldn't apply and the default ban would control. Verbal or informal approval, or approval from someone else such as a manager or procurement lead, would not satisfy a written-authorization requirement.

I haven't been able to confirm any of the following, and each could change the answer:
- Whether the policy actually bans prohibited vendors outright, or has some other route to an exception (such as an emergency or sole-source rule, or approval from someone other than the compliance officer).
- Whether getting the authorization after the purchase is allowed, or whether it must come first.
- Which Q3 facts carry over, such as the purchase amount, any urgency, or who approved it, and whether any of them triggers a different rule.

To give you a firm answer with citations to specific sections, I need one of these:
1. Permission to read `A_FRESH_20261013_01`, or
2. The relevant policy text and the Q3 facts pasted here.

## R17 — answers Q2

**Before the purchase, the employee needs both manager approval and finance approval.**

**How I got there**

1. **Date.** The purchase is on October 12, 2026, which is after July 1, 2025. So the current routine limit of $2,500 applies (AMD-2, DEF-3). The older $2,000 limit in AMD-1 covers only purchases before that date, and the new limit doesn't apply to earlier ones.
2. **Amount.** Limits are measured on the total amount in US dollars, including taxes and fees (EXP-4). $2,600 is above $2,500, so the higher-value rule applies: both manager and finance approval, before purchase (EXP-2). The lower rule that needs only a manager covers $2,500 or less, so it doesn't fit (EXP-1).
3. **Travel.** This isn't airfare, so travel-office approval doesn't apply (TRV-1).
4. **Emergency.** No emergency is claimed, and the facts don't show an immediate operational or safety risk that can't wait for normal approval (DEF-1). The emergency exception therefore doesn't apply, and the normal approvals stand (EMG-2). Even if it did apply, it would waive only *advance finance* approval, never manager approval (EMG-1, EXP-3).
5. **Vendor.** The vendor's status isn't given. Vendor rules apply regardless of anything else (EXP-3). If the vendor were prohibited, the purchase could not go ahead without a specific written authorization from the compliance officer (VEN-1). That would be in addition to manager and finance approval, and can't be assumed from them (VEN-2). On the facts given, no vendor requirement applies.

**Result:** Get manager and finance approval before buying (EXP-2, AMD-2, EXP-4). No notification after the purchase is required, because the 24-hour finance notice applies only under the emergency exception.

## R18 — answers Q8

I can't answer this from the actual Meridian Works policy, because I don't have it. Your working directory (`Q8`) is empty. When I tried the parent folder, the permission request was declined, so I didn't look there. I also don't know of any public "Meridian Works" purchasing policy, and I won't make up its terms.

What decides the answer is how the emergency exception relates to the manager-approval rule. Check the policy for these points:

1. **What the exception waives.** Many policies say an emergency only waives competitive bidding or the approved-vendor rule, not approval. If so, the employee still needs manager approval, and the emergency exception alone isn't enough.
2. **Whether there's a fallback approver.** Look for wording that lets someone else approve when the manager is unavailable, such as the manager's manager, a department head, finance or a delegate. If it exists, the employee has to use that route rather than skip approval.
3. **Whether approval can come afterwards.** Some exceptions let the employee buy first and get approval within a set time, often 24–72 hours, with written documentation. If so, the employee may go ahead but must get approval afterwards.
4. **Dollar limits on the exception.** Check whether $4,000 is within any cap on emergency purchases or on what one person may approve alone. A higher tier might need extra sign-off.
5. **Dates.** Check that the version of the policy in force on October 12, 2026 is the one being applied, including any amendments or effective dates.

**Most likely answer:** policies like this usually treat the emergency exception as changing *how* the purchase is approved, not *whether* it is. If that's true here, the employee can't rely on the emergency exception alone. They would need to use the backup approver or get approval afterwards, depending on what the policy says. I'm inferring that from common practice, not from the Meridian text.

If you paste the policy here, or allow access to the folder where it's saved, I'll give you a definite answer that cites the relevant sections.

## R19 — answers Q7

I can't answer this from Meridian Works' actual policy, because I don't have the policy text.

- **Working folder:** `Q7` is empty.
- **Parent folders:** reading them needs permission that wasn't granted, so I couldn't check for policy files there.

I won't guess Meridian Works' dollar thresholds, approver roles or exception criteria. Those rules vary a lot between organizations, and a made-up answer could lead to a purchase being approved wrongly.

**What I can say from the facts alone:** emergency exceptions in procurement policies usually depend on objective conditions, such as an immediate operational or safety risk. Calling a request "urgent" usually isn't enough. If Meridian's exception works this way, this request probably doesn't qualify. In that case the normal approval rules for a $4,000 non-travel purchase would apply, whatever they are. I can't confirm either point without the document.

**To get a definitive answer, you can do either of these:**
1. Paste the relevant policy sections here: the emergency exception, the approval thresholds or tiers, and any rules on effective dates or versions.
2. Allow access to the parent folder, or tell me where the policy file is, and I'll read it.

Once I have the text, I'll check:
- whether the exception's conditions are met,
- which approval tier covers $4,000,
- whether a version of the policy took effect around October 12, 2026, and
- any rules on documentation or ratifying the purchase afterwards.

## R20 — answers Q3

**Answer:** You need manager approval before buying. Finance does not need to approve in advance, but finance must be notified within 24 hours after the purchase. No other approvals are required.

**Why:**

1. **Normal rule:** The purchase is after July 1, 2025, so the $2,500 threshold applies (AMD-2). At $4,000, a routine purchase would need both manager and finance approval in advance (EXP-2).
2. **It counts as an emergency:** The facts describe "an immediate operational risk that cannot reasonably await normal approval." That matches the definition of a qualifying emergency in DEF-1. It doesn't rely only on calling the purchase "urgent," which EMG-3 says isn't enough.
3. **The emergency exception applies (EMG-1):** The purchase is $5,000 or less and the vendor is approved, so:
   - **Advance finance approval is waived.**
   - **Manager approval is still required before the purchase** (EMG-1, EXP-3, EMG-3).
   - **Finance must be notified within 24 hours after the purchase.** This is only a notice after the fact, not an approval (DEF-2).
4. **Not needed here:**
   - **Travel-office approval:** this isn't a travel or airfare purchase (TRV-1).
   - **Compliance-officer authorization:** the vendor is approved, not prohibited (VEN-1/VEN-2).

**Note on timing:** The purchase date was October 12, 2026, so the finance notice is due within 24 hours of when the purchase was made. That is roughly by the same time on October 13, 2026, which is today.

## R21 — answers Q8

**No.** The employee may not go ahead with the purchase on the emergency exception alone. That exception waives only *advance finance approval*. Manager approval is still required before the purchase, and the employee doesn't have it.

**Analysis**

1. **Ordinary rule.** The purchase was made on October 12, 2026, which is after the July 1, 2025 amendment, so the current $2,500 threshold applies (AMD-2, DEF-3). Because $4,000 is above $2,500, a routine purchase would need **both manager and finance approval** in advance (EXP-2).

2. **Emergency exception.** The facts meet each condition of EMG-1:
   - it is a qualifying emergency (as given, meeting DEF-1),
   - the total is $5,000 or less ($4,000),
   - the vendor is approved (VEN-3).

   So **advance finance approval is waived**.

3. **What the exception doesn't waive.** The policy says this in three places:
   - EMG-1: "Manager approval remains required before proceeding."
   - EMG-3: "An emergency does not waive manager approval…"
   - EXP-3: the Emergency Policy "may waive advance finance approval, but not manager approval."

   "Before proceeding" means before the transaction happens (DEF-2). Getting manager approval after the fact doesn't meet the requirement.

4. **Other requirements.** If manager approval is obtained and the purchase goes ahead, finance must be **notified within 24 hours after the purchase** (EMG-1). That notice is a separate step and is not the same as finance approval (DEF-2). This isn't travel, so travel-office approval doesn't apply (TRV-1). The vendor is approved, so the vendor restrictions in VEN-1 and VEN-2 don't come into play.

**Conclusion:** The emergency status removes the need for advance finance approval, but nothing in the policy removes the need for manager approval before the purchase. Until the employee gets manager approval, the purchase may not proceed.

## R22 — answers Q6

I couldn't find any Meridian Works policy documents, so I can't tell you which approvals that purchase needed.

The working directory (`Q6`) is empty, and I have no saved notes about Meridian Works. I also don't know their internal procurement policy from general knowledge, and I won't guess at approval thresholds.

Your question turns on the date (June 15, 2025), which suggests the thresholds may have changed over time. To answer it, I'd need:
- The procurement or spending-approval policy, including any amendments or superseding versions.
- The effective date of each version, so I can confirm which one applied on June 15, 2025.

If you add those files to this directory or paste the text here, I'll find the version in effect on that date and list the approvals it required for a routine, non-travel $2,300 purchase.

## R23 — answers Q1

I can't tell you what approvals are required, because I don't have the Meridian Works policy.

Here's what I checked:
- **Working directory (`...\Q1`)**: it's empty, so there are no policy files to read.
- **Parent folder (`...\A_FRESH_20261013_01`)**: I asked for read access and it wasn't granted, so I didn't look there.
- **My saved notes from past sessions**: there are none.

I don't know Meridian Works' policy from my own knowledge, either. It's not a public standard. If I gave you approval thresholds without the document, I'd be making them up.

To get you an answer, you can:
1. **Paste the relevant policy text** here, such as the procurement or approval-authority section.
2. **Put the policy file in `Q1`**, or give me read access to the parent folder.
3. **Tell me where the policy lives** if it's somewhere else on disk.

Once I have it, I'll check the $2,400 routine, non-travel equipment purchase against it. That includes the dollar thresholds, any date-based rules (for example, whether a version effective before or after October 12, 2026 applies), and any category exceptions. I'll cite the specific sections.

## R24 — answers Q6

**Answer:** The purchase needed both **manager approval and finance approval**, and both had to be given **before the purchase**.

**Why:**

1. **The date decides the threshold.** The $2,500 threshold only applies from July 1, 2025, and it does not apply to earlier purchases (AMD-2). June 15, 2025 is before that date, so the older rule in AMD-1 applies. DEF-3 confirms that the Amendments Policy decides which threshold applies on a given date.
2. **Under AMD-1**, routine purchases above $2,000 needed both manager and finance approval. Purchases of $2,000 or less needed only manager approval.
3. **The amount is above $2,000.** Thresholds are measured on the total amount, including taxes and fees (EXP-4). $2,300 is over $2,000, so it falls in the higher tier.
4. **Approval comes before the purchase.** AMD-1 doesn't say when approval must happen. The current expense rules require approval before the purchase (EXP-1, EXP-2), and AMD-3 says the amendment changed only the dollar amount, not the approval steps.

**What doesn't apply:**
- **The current $2,500 rule (EXP-1).** Under it, $2,300 would need only manager approval, but it didn't apply yet in June 2025 (AMD-2).
- **Travel rules.** This wasn't a travel purchase.
- **Emergency rules.** The purchase was routine, so it doesn't meet the definition of an emergency (DEF-1). The emergency waiver can't remove finance approval here (EXP-3).
- **Vendor rules.** No vendor status was given. Vendor restrictions apply no matter what (EXP-3), so if the vendor was prohibited, that would need to be checked separately.

Sources: AMD-1, AMD-2, AMD-3, DEF-3, EXP-1, EXP-2, EXP-3, EXP-4, DEF-1.
