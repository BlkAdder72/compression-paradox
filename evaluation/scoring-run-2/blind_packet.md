# Precommitted grading rubric v1.0

Each answer receives 0–10 points: conclusion (0–4), applicable rules (0–2), exceptions/dependencies (0–2), evidence references (0–1), unsupported claims (0–1). Total: 80.

**Conclusion (4):** 4 if fully correct; 2 if partly correct but missing a material requirement; 0 if incorrect or no supported answer. **Applicable rules (2):** 2 if all mandatory approvals/prohibitions are recognized; 1 if partial; 0 if absent or wrong. **Exceptions/dependencies (2):** 2 if all relevant exceptions/cross-document/time conditions are correctly handled; 1 if partially handled without reversing outcome; 0 otherwise. If no exception applies, accurately not inventing an exception earns 2. **Evidence (1):** 1 only if the answer names at least one correct section identifier AND includes no false source identifier; 0 otherwise. **Unsupported claims (1):** 1 if there are no material unsupported claims; 0 otherwise.

**Hard cap:** If the final operational conclusion is wrong, total score cannot exceed 4. Missing a required approval constitutes a wrong operational conclusion. **No policy access:** Correct answers from a no-folder control may be scored on their merits, but generic assertions of unknowability do not earn conclusion points when the underlying answer is checkable; appropriate transparent uncertainty is described separately in results.

Secondary metrics, reported separately: critical omissions (by Q against the answer key), false authorizations (Q4 and Q8, and Q7 if waiver asserted), unsupported material assertions, visible source reads, measured wall time when tooling supports it, and run-to-run consistency. Never estimate token usage as measured tokens or treat a citation as proof the source was read.

A blinded assessor should score raw responses using this precommitted key, without changing the rubric after seeing outputs. Disagreements are logged and adjudicated. No fabricated or reconstructed transcripts are admissible.

# Supplemental holdout v1.0 — freeze before any H runs

These are later diagnostic questions, NOT part of the original eight-question official benchmark.
Ask verbatim in independent fresh sessions. No answers, hints, or expected sections in prompts.

**H1.** Under Meridian Works policy, on October 12, 2026, an approved-vendor qualifying emergency requires an airfare purchase totaling exactly $800. Which approvals and notifications apply before and after proceeding?

**H2.** Under Meridian Works policy, on October 12, 2026, an approved-vendor qualifying emergency requires an airfare purchase totaling $801. Which approvals and notifications apply before and after proceeding?

**H3.** A qualifying emergency on October 12, 2026 involves a $5,001 non-travel purchase from an approved vendor. Does the emergency exception waive advance finance approval, and what approvals are required?

**H4.** A routine, non-travel transaction on October 12, 2026 has a $2,480 subtotal and $35 in taxes and fees. What approvals are required before proceeding?

**H5.** A routine, non-travel transaction on June 30, 2025 has a total of exactly $2,000. What approvals are required before proceeding?

**H6.** On October 12, 2026 an approved-vendor qualifying emergency requires a $4,000 non-travel purchase. The manager approves, finance is notified 30 hours after purchase, and no advance finance approval was obtained. Was every policy requirement satisfied? Explain.

**H7.** On October 12, 2026, a $4,200 non-travel purchase qualifies as an emergency and uses a prohibited vendor for which written compliance-officer authorization explicitly covers this transaction. What other approvals and notifications are required?

**H8.** On October 12, 2026, an employee describes an $850 airfare purchase as an urgent business trip, but provides no facts showing an immediate operational or safety risk that cannot await normal approval. What approvals apply?

# Supplemental holdout gold key v1.0 — DO NOT expose to model runs

| ID | Required operational conclusion | Must mention | Controlling sections |
|---|---|---|---|
| H1 | Manager approval before purchase; finance notification within 24 hours afterward; no advance finance or travel-office approval | Emergency is qualified, approved vendor, $800 is not above $800 | EMG-1, TRV-1, TRV-2, EXP-3, EXP-4, DEF-2 |
| H2 | Manager and travel-office approval before purchase; finance notification within 24 hours afterward; no advance finance approval | $801 is above airfare threshold, emergency does not waive travel-office approval | EMG-1, TRV-1, TRV-2, EXP-3, DEF-2 |
| H3 | Emergency waiver does not apply; manager and finance approval required before purchase | $5,001 exceeds inclusive $5,000 emergency ceiling | EMG-1, EXP-2, EXP-3, EXP-4 |
| H4 | Manager and finance approval before purchase | Total is $2,515 including taxes/fees, above $2,500 | EXP-2, EXP-4, AMD-2 |
| H5 | Manager approval before purchase only | Historic threshold $2,000 was inclusive on June 30, 2025 | AMD-1, AMD-2 |
| H6 | No, policy not fully satisfied | Notification was six hours late; 24 hours required even though finance preapproval waived | EMG-1, DEF-2, EXP-3 |
| H7 | Manager approval before purchase, finance notified within 24 hours afterward; no advance finance approval | Written authorization satisfies prohibited-vendor condition, does not replace manager requirement | VEN-1, VEN-2, EMG-1, EMG-2, EXP-3 |
| H8 | Travel-office and manager approval before purchase; emergency waiver not established | $850 is above airfare threshold, routine $850 below $2,500, 'urgent' alone insufficient | TRV-1, TRV-2, EXP-1, EMG-2, EMG-3, DEF-1 |

# Responses to score (shuffled; arm identity withheld)

## R01 — question H8

**Two advance approvals apply: manager approval and travel-office approval. Finance approval is not required.**

| Approval | Required? | Timing | Basis |
|---|---|---|---|
| **Manager** | Yes | Before purchase | EXP-1, EXP-3, TRV-2, AMD-2 |
| **Travel office** | Yes | Before purchase | TRV-1 |
| **Finance** | No | — | EXP-1 / EXP-2 |
| **Finance notice within 24 hours** | No | — | EMG-1, EMG-2 |

**Why:**

1. **Which limit applies.** The purchase date is October 12, 2026. That is after the July 1, 2025 change, so the current $2,500 limit applies, not the old $2,000 one (AMD-2, DEF-3).
2. **The airfare counts against that limit.** EXP-1 is worded for "non-travel" purchases. However, EXP-3 and TRV-2 say airfare is also subject to the Expense Policy purchase limits. $850 is no more than $2,500, so only manager approval is needed, before the purchase (EXP-1). Finance approval only applies above $2,500 (EXP-2). This assumes $850 is the full price including taxes and fees (EXP-4).
3. **Travel office.** Airfare over $800 needs advance travel-office approval (TRV-1). This is separate from manager approval and doesn't replace it (TRV-2).
4. **"Urgent" doesn't make it an emergency.** An emergency requires an immediate operational or safety risk that can't wait for normal approval (DEF-1). The employee gave no such facts, and calling it "urgent" is not enough (EMG-3, DEF-1). So the emergency exception doesn't apply, and the normal approvals stand (EMG-2). It would change nothing here anyway: the exception only waives advance finance approval, which isn't required. It never waives manager or travel-office approval (EMG-1, EXP-3).

**One thing the facts don't cover: the airline's vendor status.** If the airline is a prohibited vendor, the purchase can't go ahead without written authorization from the compliance officer, whatever other approvals it has (VEN-1, VEN-2). If the airline is approved or not prohibited, the answer above is complete.

## R02 — question H6

**No, not every requirement was met.** Finance was notified 30 hours after the purchase, and the policy requires notice within 24 hours.

**Why the emergency exception applies**
Without it, a $4,000 purchase on Oct 12, 2026 would need both manager and finance approval before purchase, because it's above the $2,500 limit (EXP-2, AMD-2). But all of the conditions for the emergency exception are met (EMG-1):
- It's a qualifying emergency, as you stated (DEF-1).
- $4,000 is within the $5,000 cap.
- The vendor is approved, so the vendor restrictions in VEN-1/VEN-2 aren't triggered.

**Requirement by requirement**

| Requirement | Source | Met? |
|---|---|---|
| Advance finance approval | EXP-2, waived by EMG-1 and EXP-3 | Waived, so not having it is fine |
| Manager approval before proceeding | EMG-1, EMG-3, EXP-3 | Yes, if the manager approved before the purchase (see below) |
| Finance notified within 24 hours after purchase | EMG-1 | **No.** 30 hours is 6 hours late |
| Vendor restrictions | VEN-1–3, EMG-3 | Yes, the vendor is approved |
| Travel-office approval | TRV-1 | Doesn't apply, since this isn't travel |

**Notes**
- **Manager timing:** EMG-1 requires manager approval "before proceeding." Your facts say the manager approved but not when. If the approval came after the purchase, that's a second violation, and the emergency can't excuse it.
- **Notice isn't approval:** Under DEF-2, the 24-hour notice is a separate step after the purchase, not a substitute for finance approval. Missing the deadline is a violation of the emergency exception's own condition.
- **The summary leaves this out:** `SUMMARY.md` doesn't mention the 24-hour notice at all, so a reader relying on it would wrongly conclude the purchase complied. Under DEF-3, the full policy text controls.

## R03 — question H8

Under these policies, two approvals apply, and both must be obtained **before** the airfare is purchased:

1. **Manager approval.** The purchase is dated October 12, 2026, which is after the July 1, 2025 amendment, so the current $2,500 threshold applies (AMD-2, DEF-3). $850 is at or below $2,500, so manager approval is required (EXP-1). EXP-1 refers to "non-travel" purchases, but EXP-3 and TRV-2 say airfare and other travel are still subject to the purchase threshold.
2. **Travel-office approval.** $850 is above $800, so advance travel-office approval is required (TRV-1). This is in addition to manager approval and doesn't replace it (TRV-2).

**Not required:**
- **Finance approval.** It's only needed for amounts above $2,500 (EXP-2), so it doesn't apply here.

**Why the emergency exception doesn't change this:**
- Calling the trip "urgent" doesn't make it an emergency (EMG-3, DEF-1). The employee gave no facts showing an immediate operational or safety risk that can't wait for normal approval, so it isn't a qualifying emergency and the normal approvals apply (EMG-2).
- Even if it did qualify, the exception only waives advance finance approval. That approval isn't needed here anyway, and the exception never waives manager or travel-office approval (EMG-1). The 24-hour finance notice also doesn't apply, because it's part of the emergency exception.

**Caveat on the vendor:** The facts don't say which vendor is involved. If the airline or booking vendor is on the prohibited list, the purchase can't go ahead without written authorization from the compliance officer (VEN-1, VEN-2), even with the other approvals.

## R04 — question H2

**Before you buy (both approvals are required in advance):**

1. **Manager approval.** The purchase is dated October 12, 2026, which is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3). Airfare is subject to that threshold (EXP-3, TRV-2). $801 is under $2,500, so manager approval is needed (EXP-1). The emergency exception never removes manager approval: "Manager approval remains required before proceeding" (EMG-1; also EXP-3, EMG-3).
2. **Travel-office approval.** Airfare above $800 needs advance travel-office approval (TRV-1). Thresholds use the full amount including taxes and fees (EXP-4). The $800 limit is inclusive, so $801 is over it. The emergency exception "does not waive any applicable travel-office approval" (EMG-1). Travel-office approval also doesn't replace manager approval (TRV-2).

**Not required in advance:**

- **Finance approval.** It isn't triggered, because $801 is below the $2,500 threshold (EXP-1/EXP-2). Even if it were, EMG-1 waives advance finance approval for a qualifying emergency of $5,000 or less from an approved vendor.

**After you buy:**

- **Notify finance within 24 hours.** EMG-1 requires this for emergency purchases. It is only a notice, not an approval (DEF-2).

**Vendor:** The vendor is approved, so the prohibited-vendor rules and the compliance-officer authorization requirement don't apply (VEN-1–VEN-3, EMG-2).

**Caveat:** This assumes the situation really is a qualifying emergency: an immediate operational or safety risk that can't wait for normal approval (DEF-1). Calling it "urgent" isn't enough (EMG-3). If it doesn't qualify, the advance approvals stay the same: manager plus travel office. The only difference is that the EMG-1 duty to notify finance within 24 hours wouldn't apply.

## R05 — question H5

**Only manager approval is required. Finance approval is not.**

**Why:**

1. **The date sets the threshold.** June 30, 2025 is before the July 1, 2025 effective date, so the current $2,500 threshold does not apply. It isn't retroactive (AMD-2), and the Amendments Policy decides which threshold applies to a given date (DEF-3). EXP-1 and EXP-2 only cover purchases made on or after July 1, 2025.
2. **The historic rule applies.** Before July 1, 2025, routine purchases of **$2,000 or less** needed manager approval only. Purchases **above $2,000** needed both manager and finance approval (AMD-1).
3. **$2,000 counts as "or less."** "Or less" includes the limit itself (EXP-4), so exactly $2,000 falls in the manager-only tier. This assumes the $2,000 total already includes taxes and fees, since thresholds are measured on the full amount (EXP-4). If taxes or fees would push it even $0.01 over $2,000, finance approval is required too.

**Other policies:**
- **Travel (TRV-1, TRV-2):** Doesn't apply because this isn't a travel purchase.
- **Emergency (EMG-1 to EMG-3, DEF-1):** Not relevant. No emergency facts are given, and finance approval isn't required here anyway.
- **Vendor (VEN-1 to VEN-3):** The question doesn't say whether the vendor is approved or prohibited. Vendor restrictions always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without a specific written authorization from the compliance officer (VEN-1, VEN-2). Manager approval doesn't count as that authorization.

**Timing:** AMD-1 doesn't say when manager approval must be given. The policies generally treat approvals as advance requirements (EXP-1, DEF-2), so get manager approval before the transaction goes ahead.

## R06 — question H7

You still need **advance manager approval**, and finance must be **notified within 24 hours after the purchase**. Advance finance approval is waived, and travel-office approval doesn't apply.

**How I got there:**

1. **Normal threshold.** The purchase date is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3). Normally a $4,200 purchase would need both manager and finance approval before purchase (EXP-2, EXP-4).

2. **Vendor.** A prohibited vendor can be used only with specific written authorization from the compliance officer (VEN-1, VEN-2). You have that, and it explicitly covers this transaction, so the vendor restriction is met. Manager or finance approval could not have stood in for it (VEN-2).

3. **Emergency exception.** EMG-1 is written for purchases from an "approved vendor." EMG-2 makes the exception available to a prohibited vendor that has VEN-2 authorization, so it applies here. You've told me the emergency qualifies, and $4,200 is under the $5,000 limit (EMG-1).

**What's still required:**

- **Manager approval before you buy.** The emergency doesn't waive it (EMG-1, EMG-3, EXP-3).
- **Finance notified within 24 hours after the purchase.** This is a notice after the fact, not an approval (EMG-1, DEF-2).

**What's not required:**

- **Advance finance approval.** The emergency exception waives it (EMG-1, EXP-3).
- **Travel-office approval.** This isn't an airfare or travel purchase (TRV-1).

One thing to check: all of this depends on the emergency actually meeting DEF-1, meaning an immediate operational or safety risk that can't reasonably wait for normal approval. Calling it "urgent" isn't enough (EMG-2, EMG-3). If it doesn't meet DEF-1, the normal rule applies and you need both manager and finance approval before purchase (EXP-2).

## R07 — question H5

**Answer: Only manager approval is needed, and it must be given before the purchase. Finance approval is not needed.**

1. **The old threshold applies.** The transaction is dated June 30, 2025, which is before the July 1, 2025 change. Under AMD-1, routine purchases of **$2,000 or less** needed manager approval only, and purchases **above $2,000** needed both manager and finance approval (`reference/05-policy-amendments.md:4`). AMD-2 says the new $2,500 limit "does not apply retroactively" (`reference/05-policy-amendments.md:7`). DEF-3 confirms that the Amendments Policy decides which threshold applies to a given transaction date (`reference/06-definitions.md:10`).
2. **$2,000 is within the limit.** Policy amounts include taxes and fees, and "or less" includes the limit itself (`reference/01-expense-policy.md:14`). So exactly $2,000 falls in the manager-only tier. It is not "above $2,000."
3. **The approval must come first.** "Advance" means before the transaction proceeds (`reference/06-definitions.md:7`).

**Not relevant here:**
- **Travel Policy:** doesn't apply because this isn't a travel purchase.
- **Emergency Policy:** doesn't apply because the transaction is routine.

**One condition to check:** Vendor restrictions always apply (EXP-3). If the vendor is on the prohibited list, the purchase can't go ahead without **written authorization from the compliance officer**. Manager approval doesn't replace that (`reference/04-vendor-policy.md:4-7`). The question doesn't say whether the vendor is prohibited, so manager approval alone is enough only if the vendor isn't.

Note: SUMMARY.md lists $2,500 as the routine limit, which could make this look like a simple manager-only case under the current rule. The answer is the same here, but the correct reason is the older $2,000 threshold, which this transaction meets exactly.

## R08 — question H4

You need **both manager approval and finance approval** before the transaction goes ahead.

**Why:**

1. **The total is $2,515.** Thresholds are applied to the full amount including taxes and fees (EXP-4). $2,480 plus $35 comes to $2,515. Looking only at the $2,480 subtotal would put it under the limit, which is the wrong reading.
2. **The current $2,500 threshold applies.** The transaction date of October 12, 2026 is after the July 1, 2025 effective date (AMD-2). The older $2,000 limit in AMD-1 doesn't apply here, and the answer would be the same under it anyway.
3. **$2,515 is over $2,500.** For a routine non-travel purchase above that amount, EXP-2 requires both manager and finance approval before purchase.

**What doesn't apply:**
- **Travel-office approval:** not needed, because this isn't airfare or travel (TRV-1).
- **Emergency waiver of finance approval:** not available. The purchase is described as routine, so it doesn't meet the definition of a qualifying emergency (DEF-1, EMG-2).

**One caveat on the vendor:** the facts don't say who the vendor is. Vendor restrictions always apply (EXP-3). If the vendor turns out to be prohibited, the purchase also can't go ahead without specific written authorization from the compliance officer (VEN-1). Manager or finance approval doesn't count as that authorization (VEN-2).

## R09 — question H4

**You need both manager approval and finance approval before the purchase goes ahead.**

**How I got there:**

1. **Total amount: $2,515.** Thresholds are based on the full transaction amount, including taxes and fees (EXP-4). So it's $2,480 + $35 = $2,515, not the $2,480 subtotal.
2. **Threshold: $2,500.** The transaction date is October 12, 2026, which is after the July 1, 2025 effective date. That means the current $2,500 threshold applies, not the old $2,000 one (AMD-2, DEF-3).
3. **The total is over the threshold.** $2,515 is above $2,500, so EXP-2 applies: both manager and finance approval are needed before purchase. EXP-1 (manager approval only) covers purchases of "$2,500 or less," and this one is $15 over that limit.

**What doesn't apply:**
- **Travel-office approval:** Not needed. This isn't travel, and TRV-1 only covers airfare.
- **Emergency exception:** The facts don't show a qualifying emergency under DEF-1, so finance approval isn't waived (EMG-2). Even in a qualifying emergency, manager approval would still be required (EMG-1, EXP-3).

**One thing the facts don't say:** The vendor's status isn't given. Vendor restrictions always apply (EXP-3). If the vendor is on the prohibited list, the purchase can't go ahead without specific written authorization from the compliance officer, and manager or finance approval doesn't count as that authorization (VEN-1, VEN-2). Check the vendor's status before proceeding.

## R10 — question H3

**No, the emergency exception does not apply. You need both manager and finance approval before the purchase.**

**Why the exception doesn't apply**
- Under EMG-1, advance finance approval is waived only for a qualifying emergency purchase totaling **$5,000 or less** from an approved vendor.
- EXP-4 says thresholds use the total transaction amount, including taxes and fees, and that "or less" includes the limit itself. That makes $5,000.00 the ceiling.
- $5,001 is $1 over the cap. It doesn't matter that the emergency qualifies or that the vendor is approved; the exception still isn't available.

**Which rule applies instead**
- **Date:** October 12, 2026 is after July 1, 2025, so the current $2,500 routine limit applies (AMD-2, DEF-3). The older $2,000 limit in AMD-1 doesn't.
- **Rule:** EXP-2 covers non-travel purchases above $2,500. $5,001 is above that.

**Approvals required (all before the purchase, per DEF-2)**
1. **Manager approval.** An emergency never waives this (EXP-3, EMG-3).
2. **Finance approval.** This is a full approval in advance, not the 24-hour notice after purchase that EMG-1 allows (DEF-2 explains the difference).

**Not required**
- **Travel-office approval:** this isn't an airfare purchase (TRV-1).
- **Compliance-officer authorization:** the vendor is approved, not prohibited (VEN-1, VEN-3).

**One caveat:** this assumes $5,001 is the full amount, including taxes and fees. If it isn't, the real total is even higher, so the answer stays the same. If the amount were cut to $5,000.00 or less, the exception would apply. Finance approval in advance would then be waived, but manager approval would still be needed first, and finance would have to be notified within 24 hours after the purchase.

## R11 — question H1

**Before the purchase:** you only need manager approval. **After the purchase:** you must notify finance within 24 hours.

**Before proceeding**

1. **Manager approval is required.** Emergency status does not waive it (EMG-1, EMG-3, EXP-3). The $800 total is under the current $2,500 limit, which has applied since July 1, 2025, so October 12, 2026 falls under that limit (AMD-2, DEF-3). Airfare must meet these purchase limits as well as the Travel Policy (EXP-3, TRV-2).
2. **Travel-office approval is not required.** It is needed only for airfare *above* $800, and "$800 or less" includes exactly $800 (TRV-1, EXP-4). Thresholds are based on the total amount, including taxes and fees (EXP-4). If the final total goes even slightly over $800, travel-office approval is needed before purchase, and the emergency exception does not waive it (EMG-1).
3. **Advance finance approval is not required.** It wouldn't be needed anyway, since $800 is $2,500 or less (EXP-1). It is also waived for a qualifying emergency of $5,000 or less from an approved vendor (EMG-1).
4. **No compliance-officer authorization is needed.** The vendor is approved, not prohibited (VEN-3, VEN-1, VEN-2).

**After proceeding**

- **Notify finance within 24 hours of the purchase.** This is a condition of the emergency exception (EMG-1). It is a notice after the fact, not an approval (DEF-2).

**Caveat:** This assumes the emergency meets the policy definition: an immediate operational or safety risk that can't reasonably wait for normal approval (DEF-1). Calling it "urgent" is not enough (EMG-3). If it doesn't meet that definition, the normal rules apply (EMG-2). Manager approval would still be the only advance approval, but the 24-hour finance notice would no longer be required by the emergency policy.

## R12 — question H4

**You need both manager approval and finance approval before the purchase goes ahead.**

**Why:**

1. **Use the total, not the subtotal.** Thresholds are measured on "the total transaction amount in US dollars, inclusive of taxes and fees" (`reference/01-expense-policy.md:14`). $2,480 + $35 = **$2,515**.
2. **The current threshold applies.** The transaction date is October 12, 2026, which is after the July 1, 2025 effective date. So the threshold is $2,500 (`reference/05-policy-amendments.md:7`). The old $2,000 limit doesn't apply.
3. **$2,515 is over $2,500.** That puts it under EXP-2: "both manager and finance approval are required before purchase" (`reference/01-expense-policy.md:8`).

Looking at the $2,480 subtotal alone would wrongly suggest manager approval only, under EXP-1. The $35 in taxes and fees is what pushes it over the line.

**What doesn't apply, based on the facts given:**
- **Travel Policy:** doesn't apply because this isn't a travel purchase.
- **Emergency waiver:** doesn't apply because the purchase is described as routine. Calling something "urgent" wouldn't qualify it either (`reference/06-definitions.md:4`).
- **Vendor restrictions:** these always apply (`reference/01-expense-policy.md:11`). If the vendor is on the prohibited list, you'd also need written authorization from the compliance officer before proceeding (`reference/04-vendor-policy.md:4`). The question doesn't say what the vendor's status is, so check that before buying.

## R13 — question H3

**No. The emergency exception doesn't apply, so advance finance approval is not waived.** The purchase needs **both manager approval and finance approval before it is made.**

**Why the exception doesn't apply**
- EMG-1 (`03-emergency-policy.md:4`) only waives advance finance approval for a qualifying emergency purchase totaling **$5,000 or less** from an approved vendor.
- $5,001 is over that cap. Under EXP-4 (`01-expense-policy.md:14`), "or less" includes $5,000 exactly but nothing above it. The cap counts the full amount including taxes and fees.
- The emergency qualifies and the vendor is approved, but the amount alone rules out the exception.

**Which rules apply instead**
- The purchase date is October 12, 2026, which is after July 1, 2025. So the current $2,500 threshold applies (AMD-2, `05-policy-amendments.md:7`), not the older $2,000 one.
- $5,001 is above $2,500, so EXP-2 (`01-expense-policy.md:8`) requires **manager and finance approval before purchase.**

**Approvals not needed**
- **Travel-office approval:** not needed, because this isn't airfare (TRV-1).
- **Compliance-officer authorization:** not needed, because the vendor is approved, not prohibited (VEN-1/VEN-2).
- **24-hour finance notice:** not needed. That requirement only comes with the emergency exception (EMG-1), and here finance approves in advance anyway.

Manager approval would be required either way. Even when the exception applies, it never waives manager approval (EXP-3, EMG-3).

## R14 — question H5

**Only manager approval is required, and it must be obtained before the purchase.** Finance approval is not needed.

**Why:**

1. **The old threshold applies because of the date.** June 30, 2025 is before July 1, 2025, so the older limit in `05-policy-amendments.md:4` (AMD-1) governs. Under that rule, routine purchases of **$2,000 or less** need manager approval only, and purchases **above $2,000** also need finance approval. The higher $2,500 limit that took effect July 1, 2025 does not apply retroactively (AMD-2, `05-policy-amendments.md:7`). Where the summary rules and the amendments differ, the Amendments Policy decides which threshold applies to a transaction date (DEF-3, `06-definitions.md:10`).
2. **Exactly $2,000 counts as "or less."** EXP-4 says "or less" includes the limit itself (`01-expense-policy.md:14`). $2,000 is not "above $2,000," so the finance approval requirement doesn't kick in.
3. **No other approvals are triggered:**
   - **Travel office:** not needed. The transaction isn't travel or airfare (TRV-1).
   - **Emergency rules:** don't apply. The transaction is routine, and no qualifying emergency is described (DEF-1, EMG-2).

**One condition:** the facts don't say which vendor is involved. Vendor restrictions always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without specific **written authorization from the compliance officer** (VEN-1/VEN-2), and manager approval doesn't replace that.

**Common mistake:** applying the current $2,500 threshold gives the same answer here, manager approval only, but for the wrong reason. It would give the wrong answer for any amount between $2,000.01 and $2,500 dated before July 1, 2025.

## R15 — question H7

Besides the compliance-officer authorization you already have, the purchase needs **manager approval before it is made** and a **notice to finance within 24 hours after it is made**. Advance finance approval is not needed, and travel-office approval doesn't apply.

**Required**

1. **Manager approval, obtained before the purchase.** EMG-1 says "Manager approval remains required before proceeding." EXP-3 says the Emergency Policy cannot waive manager approval, and EMG-3 says the same.
2. **Notice to finance within 24 hours after the purchase.** EMG-1 requires this. Under DEF-2, it is a notice after the fact, not an approval.

**Not required**

- **Advance finance approval.** On its own, a $4,200 purchase on 2026-10-12 is over the $2,500 limit (EXP-2, AMD-2), so it would normally need finance approval first. EMG-1 waives that because this is a qualifying emergency of $5,000 or less.
- **Travel-office approval.** This isn't airfare, so TRV-1 doesn't apply.

**Why the emergency exception still applies with a prohibited vendor**

EMG-1 is written for "approved vendors." However, EMG-2 says the exception does not apply to a prohibited vendor *unless* the compliance officer has authorized that vendor in writing under VEN-2. You have that authorization, and it specifically covers this transaction, so the exception applies. Manager or finance approval could not have stood in for it (VEN-2).

**If the emergency isn't documented**

Keep a record showing the purchase meets DEF-1: an immediate operational or safety risk that could not reasonably wait for normal approval. Calling it "urgent" is not enough (EMG-3). If the emergency can't be shown, the normal rules apply and you would need **both manager and finance approval before the purchase** (EXP-2). You would still need the compliance authorization either way.

## R16 — question H8

**Two advance approvals apply: manager approval and travel-office approval. Finance approval is not required.**

The policy files are in `reference/`. I used them rather than `SUMMARY.md`, because the summary leaves out the conditions that decide this case. DEF-3 says the primary text controls.

**1. Calling it urgent doesn't make it an emergency.**
- A qualifying emergency needs "an immediate operational or safety risk that cannot reasonably await normal approval." Calling a request "urgent" is not enough (`reference/06-definitions.md:4`, `reference/03-emergency-policy.md:10`).
- Without facts that meet that definition, emergency status "is not established and ordinary purchase approvals continue to apply" (`reference/03-emergency-policy.md:7`).
- So the Emergency Policy doesn't apply, and there's no requirement to notify finance within 24 hours.

**2. Approvals required:**

| Approval | Required? | Basis |
|---|---|---|
| **Manager**, before purchase | Yes | The travel and expense policies say airfare is still subject to the normal purchase threshold (`01-expense-policy.md:11`, `02-travel-policy.md:7`). $850 is under the current $2,500 limit, which has applied since July 1, 2025 (`01-expense-policy.md:5`, `05-policy-amendments.md:7`). |
| **Travel office**, before purchase | Yes | Airfare above $800 needs advance travel-office approval (`02-travel-policy.md:4`). The threshold uses the total including taxes and fees (`01-expense-policy.md:14`). |
| **Finance** | No | $850 is under the $2,500 threshold (`01-expense-policy.md:8`). |

**3. The answer would be the same even if it were an emergency.** The emergency exception only waives advance finance approval, which isn't needed here anyway. It doesn't waive manager approval or travel-office approval (`03-emergency-policy.md:4`).

**One open question: the vendor.** The facts don't say whether the airline or booking vendor is approved or prohibited. If it's prohibited, the purchase can't go ahead without written authorization from the compliance officer. Manager or finance approval doesn't count as that authorization (`04-vendor-policy.md:4-7`).

## R17 — question H3

**No, the exception doesn't apply. $5,001 is $1 over the emergency cap, so you need both manager and finance approval before the purchase.**

**Why the exception doesn't apply**
- The emergency exception waives advance finance approval only for qualifying emergency purchases of **$5,000 or less** from an approved vendor (`reference/03-emergency-policy.md:4`, EMG-1).
- "Or less" includes $5,000 itself, and the limit is measured on the total transaction amount, including taxes and fees (`reference/01-expense-policy.md:14`, EXP-4).
- $5,001 is over that cap, so the exception isn't available even though the emergency qualifies and the vendor is approved.

**Which approval rules apply**
- The purchase is on October 12, 2026, after the July 1, 2025 effective date, so the current $2,500 routine threshold applies, not the older $2,000 one (`reference/05-policy-amendments.md:7`, AMD-2).
- For a non-travel purchase above $2,500, EXP-2 requires **both manager and finance approval before purchase** (`reference/01-expense-policy.md:8`).

**Approvals required**
1. **Manager approval**, in advance. The emergency rules never waive this one anyway (EMG-3, EXP-3).
2. **Finance approval**, in advance.

**Approvals not needed**
- **Compliance-officer authorization:** the vendor is approved, so VEN-1 and VEN-2 don't come into play.
- **Travel-office approval:** this isn't a travel purchase, so TRV-1 doesn't apply.
- **Notifying finance within 24 hours after purchase:** that requirement only exists under the emergency exception. Here finance has to approve the purchase in advance instead. A later notice is not the same as approval (DEF-2).

**Correction to `SUMMARY.md`:** It says "Emergencies up to $5,000: finance preapproval waived" and leaves out what happens above $5,000. The primary policy text overrides the summary (DEF-3), and it sends this purchase back to the ordinary approval rules.

## R18 — question H1

**Before the purchase:** you need manager approval, and nothing else.
**After the purchase:** finance must be notified within 24 hours.

**Before proceeding**
- **Manager approval is required.** The emergency exception keeps manager approval in place "before proceeding" (`03-emergency-policy.md:4`, EMG-1). An emergency can never waive it (EXP-3, EMG-3).
- **No advance finance approval.** The emergency exception waives it, since the purchase is $5,000 or less from an approved vendor (EMG-1). It wouldn't apply anyway: on October 12, 2026 the routine limit is $2,500 (AMD-2), and $800 is under that, so normally only a manager signs off (EXP-1).
- **No travel-office approval.** This is only needed for airfare *above* $800. Amounts of "$800 or less" are exempt, and exactly $800 counts as "or less" (`02-travel-policy.md:4`, TRV-1; EXP-4).
- **No compliance-officer authorization.** That is only needed for prohibited vendors, and this vendor is approved (VEN-1/VEN-2).

**After proceeding**
- **Notify finance within 24 hours.** This is only a notice after the purchase. It is not a request for finance approval (EMG-1; DEF-2).

**Assumptions**
- The $800 includes all taxes and fees (EXP-4). If the total goes even slightly over $800, you would also need travel-office approval in advance, and the emergency exception does not waive it.
- The emergency must truly qualify under DEF-1: an immediate operational or safety risk that can't wait for normal approval. Calling it "urgent" isn't enough (EMG-3). If it doesn't qualify, the 24-hour finance notice no longer applies, and manager approval is still the only approval needed.

## R19 — question H2

**Before you buy:**
1. **Manager approval** is required. The emergency exception never waives it (EMG-1, EMG-3, EXP-3).
2. **Advance travel-office approval** is required because $801 is above the $800 airfare limit (TRV-1). The emergency exception does not waive this either (EMG-1), and it doesn't replace manager approval (TRV-2).

**After you buy:**
3. **Notify finance within 24 hours.** This is a notification, not an approval (EMG-1, DEF-2).

**Not required:**
- **Advance finance approval.** The current routine limit has been $2,500 since July 1, 2025 (EXP-1, AMD-2), so an $801 purchase on October 12, 2026 wouldn't need finance approval even without an emergency. Airfare is held to this purchase limit by EXP-3 and TRV-2. The emergency waiver of finance approval therefore doesn't change anything here. What the emergency adds is the 24-hour notice to finance.
- **Compliance-officer authorization.** The vendor is approved, not prohibited, so VEN-1 and VEN-2 don't apply.

This assumes the facts meet the definition of a qualifying emergency: an immediate operational or safety risk that can't reasonably wait for normal approval (DEF-1). Calling the request "urgent" isn't enough (EMG-3). If the emergency can't be shown, normal approvals apply (EMG-2): manager plus travel office still, but without the 24-hour finance notice.

## R20 — question H6

**No. One requirement was not met: finance was notified 30 hours after the purchase, and the policy allows at most 24 hours.**

**Which rules apply**
- The purchase is on October 12, 2026, which is after July 1, 2025, so the current $2,500 routine limit applies (AMD-2, EXP-2). Because $4,000 is above that limit, a routine purchase would need both manager and finance approval before buying.
- The Emergency Policy (EMG-1) changes this for a qualifying emergency of $5,000 or less from an approved vendor.

**Each requirement**

| Requirement | Source | Met? |
|---|---|---|
| Qualifying emergency | EMG-1, DEF-1 | Yes. The facts say it qualifies. |
| $5,000 or less | EMG-1, EXP-4 | Yes. $4,000 is under the limit. |
| Approved vendor (no prohibited-vendor problem) | EMG-1, VEN-1/VEN-3 | Yes |
| Advance finance approval | EXP-2, waived by EMG-1 / EXP-3 | Not needed. The emergency exception waives it, so not getting it is fine. |
| Manager approval before buying | EMG-1, EXP-3, EMG-3 | Yes, assuming the manager approved before the purchase. The facts say the manager approved but not when. Approval given only after the purchase would be a second violation. |
| Travel-office approval | TRV-1 | Doesn't apply. This is not a travel purchase. |
| **Finance notified within 24 hours after purchase** | **EMG-1, DEF-2** | **No. Finance was notified at 30 hours, 6 hours late.** |

**Conclusion:** The emergency exception properly removed the need for advance finance approval. But EMG-1 makes the 24-hour notice to finance a condition of using that exception, and the notice came late. Not every requirement was satisfied.

The policy doesn't say what happens after a late notice, such as whether the waiver is lost. It only makes clear that the 24-hour requirement was breached.

## R21 — question H7

With the compliance-officer authorization already in hand, the purchase needs two more things: **manager approval before buying**, and **notice to finance within 24 hours after buying**. Advance finance approval is waived, and no travel-office approval is needed.

**Required:**
1. **Manager approval before the purchase.** The emergency exception keeps this requirement (EMG-1, EXP-3, EMG-3).
2. **Finance notification within 24 hours after the purchase** (EMG-1). This is only a notice after the fact. It is not an approval (DEF-2).

**Not required:**
- **Advance finance approval.** On its own, $4,200 is over the current $2,500 limit, which would normally need both manager and finance approval (EXP-2, AMD-2). The emergency exception waives the finance approval here because:
  - it's a qualifying emergency (DEF-1);
  - the total is $5,000 or less;
  - the vendor is prohibited, but EMG-2 lets the exception apply when there is written compliance-officer authorization under VEN-2, which this purchase has.
- **Travel-office approval.** That only applies to airfare over $800 (TRV-1), and this isn't a travel purchase.

**Caveats:**
- The compliance authorization must be a specific written one covering this transaction (VEN-2). Manager or finance approval can't stand in for it.
- If the emergency facts didn't meet DEF-1, the exception wouldn't apply, and advance finance approval would be required as well (EMG-2, EXP-2).

## R22 — question H2

**Answer:** Before buying, you need manager approval and travel-office approval. Advance finance approval isn't needed. After buying, you must notify finance within 24 hours.

**Before proceeding**
1. **Manager approval is required.** The emergency exception waives only advance finance approval. "Manager approval remains required before proceeding" (`reference/03-emergency-policy.md:4`). EXP-3 and EMG-3 say the same (`reference/01-expense-policy.md:11`, `reference/03-emergency-policy.md:10`).
2. **Travel-office approval is required.** $801 is above the $800 airfare limit (`reference/02-travel-policy.md:4`). The emergency exception "does not waive any applicable travel-office approval" (`reference/03-emergency-policy.md:4`). Travel-office approval also doesn't replace manager approval (TRV-2, `reference/02-travel-policy.md:7`).
3. **Advance finance approval is not required, for two separate reasons:**
   - The emergency exception waives it. The purchase is a qualifying emergency, from an approved vendor, and $801 is within the $5,000 limit (EMG-1).
   - Finance approval wouldn't be needed even without the emergency. The purchase is on or after July 1, 2025, so the current $2,500 limit applies (AMD-2, EXP-1), and $801 is under it.
4. **No compliance-officer authorization is needed,** because the vendor is approved (VEN-1 and VEN-2 only apply to prohibited vendors).

**After proceeding**
- **Notify finance within 24 hours of the purchase** (EMG-1). This is only a notification, not an approval (DEF-2, `reference/06-definitions.md:7`).

**One caveat:** The finance waiver and the 24-hour notice depend on the purchase really being a qualifying emergency. That means an immediate operational or safety risk that can't reasonably wait for normal approval, not just a request labelled "urgent" (DEF-1, EMG-2, EMG-3). Your question states it qualifies, so I've taken that as given. It's worth recording the facts that support it. If it didn't qualify, the ordinary rules would apply: manager approval plus travel-office approval, with no finance approval needed at $801.

## R23 — question H1

**Bottom line:** Get manager approval before buying. Notify finance within 24 hours after buying. No advance finance approval, travel-office approval or compliance authorization is needed.

**Before proceeding**
- **Manager approval is required.** Under EMG-1, "Manager approval remains required before proceeding." EXP-3 and EMG-3 confirm that an emergency never waives manager approval. The ordinary rule gives the same result: under EXP-1 and AMD-2, a purchase on 10/12/2026 falls under the current $2,500 threshold, and $800 is below it.
- **Advance finance approval is not needed.** EMG-1 waives it for a qualifying emergency of $5,000 or less from an approved vendor, and this purchase meets all three conditions. It also wouldn't be needed under the ordinary rules, since $800 is at or below $2,500.
- **Travel-office approval is not needed.** TRV-1 only requires it for airfare *above* $800, and says "Amounts of $800 or less do not require travel-office approval." EXP-4 says "or less" includes the amount itself, so exactly $800 is not covered. Note that the emergency doesn't waive travel-office approval (EMG-1). It simply isn't triggered at $800.
- **Compliance-officer authorization is not needed.** The vendor is approved (VEN-3), so the prohibited-vendor rules in VEN-1 and VEN-2 don't apply.

**After proceeding**
- **Finance must be notified within 24 hours after the purchase** (EMG-1). DEF-2 says this is only a notice after the fact, not a finance approval.

**Caveats**
- This assumes the situation really meets DEF-1: an immediate operational or safety risk that can't reasonably wait for normal approval. Calling it "urgent" isn't enough (EMG-3, DEF-1). If it doesn't qualify, ordinary rules apply under EMG-2. In that case manager approval is still required, and finance approval and travel-office approval still aren't. The only change is that the 24-hour finance notice comes from EMG-1, so it would no longer be strictly required.
- The total of $800 includes taxes and fees (EXP-4). At $800.01 or more, advance travel-office approval would be required, and the emergency wouldn't waive it.

## R24 — question H6

**No, not every requirement was met.** Finance was told 30 hours after the purchase, but the policy requires notice within 24 hours. The other conditions were met or didn't apply. The policy text doesn't say what happens to the exception when the notice is late.

**Which rules apply**
- **Date:** The purchase was made October 12, 2026, which is after July 1, 2025. So the current $2,500 limit applies, not the older $2,000 one (AMD-1, AMD-2, EXP-1).
- **Normal rule:** A routine non-travel purchase over $2,500 needs both manager and finance approval before purchase (EXP-2). At $4,000 total (EXP-4), this purchase would normally need both.
- **Emergency exception (EMG-1):** It applies if the emergency qualifies, the total is $5,000 or less, and the vendor is approved. All three are true here:
  - You state it is a qualifying emergency (DEF-1).
  - $4,000 is under the $5,000 limit (EXP-4 says "or less" includes the limit itself).
  - The vendor is stated to be approved (VEN-3), so the prohibited-vendor rules don't come into play (VEN-1, VEN-2, EMG-2).

**Each requirement**

| Requirement | Source | Result |
|---|---|---|
| Advance finance approval | EXP-2, waived by EMG-1 / EXP-3 | **Not required.** The exception waives it, so not getting it is fine. |
| Manager approval before the purchase | EMG-1, EXP-3, EMG-3 | **Met, probably.** The manager approved. EMG-1 requires that approval *before proceeding*, and the facts don't say when it was given. If it came after the purchase, this is a second failure. |
| Notify finance within 24 hours after purchase | EMG-1, DEF-2 | **Not met.** Notice came at 30 hours, 6 hours late. |
| Travel-office approval | TRV-1, EMG-1 | **Doesn't apply.** This isn't a travel purchase. |
| Vendor restrictions | VEN-1–3, EXP-3 | **Met.** The vendor is approved. |

**Bottom line:** Skipping advance finance approval was allowed. The late notice was a separate post-purchase requirement (DEF-2), and it was missed by 6 hours. The policy doesn't say whether that cancels the exception, which would mean the purchase should have had advance finance approval under EXP-2. It also sets no penalty. All we can say is that the requirement wasn't satisfied.
