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

## R01 — question H2

**Before the purchase, you need manager approval and travel-office approval. Advance finance approval is not needed. Afterward, finance must be notified within 24 hours.**

**Before purchase:**

1. **Manager approval is required.**
   - The purchase is on or after July 1, 2025, so the $2,500 threshold applies (AMD-2, DEF-3).
   - $801 is under $2,500, so the ordinary manager-approval rule applies (EXP-1). Airfare is held to the Expense Policy threshold as well as the Travel Policy (EXP-3, TRV-2).
   - The emergency exception does not remove this. EMG-1 says "Manager approval remains required before proceeding" (also EXP-3, EMG-3).

2. **Travel-office approval is required.**
   - $801 is above $800, so it needs advance travel-office approval (TRV-1). Thresholds use the total amount including taxes and fees (EXP-4), so I've treated $801 as the full total.
   - EMG-1 says the emergency exception "does not waive any applicable travel-office approval."
   - Travel-office approval does not replace manager approval (TRV-2).

3. **Advance finance approval is not required.**
   - At $801, finance approval wouldn't apply under EXP-1 anyway. Separately, EMG-1 waives advance finance approval for an emergency purchase of $5,000 or less from an approved vendor (EXP-3).

**After purchase:**

4. **Finance must be notified within 24 hours.** This is required by EMG-1. It is only a notification after the purchase, not an approval (DEF-2).

**Vendor:** The vendor is approved (VEN-3), so the prohibited-vendor rules and compliance-officer authorization don't apply (VEN-1, VEN-2, EMG-2).

**Assumption:** I've taken "qualifying emergency" as given. The policy requires an immediate operational or safety risk that can't reasonably wait for normal approval (DEF-1); calling it "urgent" isn't enough (EMG-3). If that standard isn't actually met, the finance notification duty wouldn't arise. Manager and travel-office approval would still be required either way.

## R02 — question H7

Under the Meridian Works policy files, you need **manager approval before the purchase** and you must **notify finance within 24 hours after it**. No advance finance approval and no travel-office approval are needed.

**Required:**
1. **Manager approval before the purchase.** An emergency never waives manager approval (EMG-1, EMG-3, EXP-3).
2. **Finance notification within 24 hours after the purchase** (EMG-1). This is a notice after the fact, not an approval (DEF-2).

**Not required:**
- **Advance finance approval.** On its own, $4,200 is above the $2,500 limit that has applied since July 1, 2025 (EXP-2, AMD-2), so manager and finance approval would normally both be needed. The emergency exception waives the finance approval here because:
  - the purchase qualifies as an emergency (DEF-1);
  - $4,200 is within the $5,000 emergency cap (EMG-1);
  - the vendor is prohibited, but the exception can still apply because the written compliance-officer authorization specifically covers this transaction (EMG-2, VEN-2). That authorization must be the specific written one; it can't be assumed from manager or finance approval (VEN-2).
- **Travel-office approval.** This isn't an airfare purchase, so TRV-1 doesn't apply.

## R03 — question H5

**You need manager approval only, before the purchase. Finance approval is not required.**

1. **The older threshold applies (AMD-1, AMD-2, DEF-3).** June 30, 2025 is the day before the $2,500 threshold took effect. That change does not apply to earlier transactions (AMD-2), and the Amendments Policy decides which threshold applies to a given date (DEF-3). So the rules from before July 1, 2025 govern this one.
2. **$2,000 falls in the lower tier (AMD-1, EXP-4).** Under the older rule, routine purchases of "$2,000 or less" need manager approval, and only amounts *above* $2,000 also need finance approval. "Or less" includes the limit itself (EXP-4), so exactly $2,000 needs manager approval only. The threshold is measured on the total amount, including taxes and fees (EXP-4).
3. **No other approvals are triggered:**
   - **Travel office (TRV-1, TRV-2):** Not needed because this isn't a travel purchase.
   - **Emergency rules (EMG-1–3, DEF-1):** They don't apply because nothing in the facts describes an emergency. Even if they did, they could only remove finance approval, which isn't required here anyway, and manager approval would still be needed.

**One thing to check:** the question doesn't say whether the vendor is approved or prohibited. Vendor restrictions always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without written authorization from the compliance officer (VEN-1, VEN-2). Manager approval does not count as that authorization.

## R04 — question H1

**Before you buy:** only manager approval is needed. **After you buy:** notify finance within 24 hours.

**Before proceeding**
- **Manager approval is required.** Airfare follows the normal purchase threshold (EXP-3, TRV-2). On October 12, 2026 that threshold is $2,500, because it took effect July 1, 2025 (AMD-2). $800 is under it, so manager approval applies (EXP-1). The emergency rule says plainly that it does not waive manager approval (EMG-1, EMG-3, EXP-3).
- **Advance finance approval is waived.** The emergency exception applies to a qualifying emergency of $5,000 or less from an approved vendor (EMG-1). This purchase meets all three conditions. It wouldn't need finance approval anyway, because $800 is under $2,500.
- **No travel-office approval.** That is only required for airfare *above* $800. The policy says "$800 or less do not require travel-office approval" (TRV-1), and amounts include taxes and fees (EXP-4). At exactly $800 it doesn't apply. The emergency rule doesn't waive travel-office approval, but here it isn't triggered in the first place.
- **No compliance-officer authorization.** That is only needed for a prohibited vendor (VEN-1/VEN-2), and this vendor is approved.

**After proceeding**
- **Notify finance within 24 hours of the purchase** (EMG-1). This is a notice, not an approval (DEF-2).

I've taken "qualifying emergency" as given in your question. In practice, the record should show an immediate operational or safety risk that couldn't wait for normal approval (DEF-1). Calling it "urgent" isn't enough (EMG-3). If that can't be shown, the emergency waiver and the 24-hour notice drop out. For $800 the result is nearly the same: manager approval only, with no finance or travel-office approval.

I checked the conclusions in SUMMARY.md against the full policy files in `reference/`. The summary leaves out the 24-hour finance notice and the fact that exactly $800 doesn't need travel-office approval.

## R05 — question H2

I checked this against the full policy texts in `reference/`, not just the short summary.

## Before buying (both are required)

1. **Manager approval.** $801 is under the $2,500 routine threshold, which has applied since July 1, 2025 (`reference/01-expense-policy.md:5`, `reference/05-policy-amendments.md:7`). Emergency status never removes manager approval (`reference/03-emergency-policy.md:4`, `:10`; `reference/01-expense-policy.md:11`).
2. **Travel-office approval.** Airfare over $800 needs it in advance, and $801 is over (`reference/02-travel-policy.md:4`). The emergency exception does not waive it (`reference/03-emergency-policy.md:4`). Manager approval is still needed as well (`reference/02-travel-policy.md:7`).

## Not required

- **Finance approval in advance.** The emergency exception waives it for a qualifying emergency of $5,000 or less from an approved vendor (`reference/03-emergency-policy.md:4`). At $801 it wouldn't be needed anyway, since that's under the $2,500 routine threshold.
- **Compliance-officer authorization.** That's only needed for prohibited vendors, and this vendor is approved (`reference/04-vendor-policy.md:4-9`).

## After buying

- **Tell finance within 24 hours.** The emergency exception requires this. It's a notice, not an approval (`reference/03-emergency-policy.md:4`; `reference/06-definitions.md:7`).

**One caveat:** this assumes the situation really meets the definition of a qualifying emergency: an immediate operational or safety risk that can't wait for normal approval. Calling it "urgent" isn't enough (`reference/06-definitions.md:4`; `reference/03-emergency-policy.md:7`, `:10`). If it doesn't qualify, the normal rules apply. You'd still need manager and travel-office approval beforehand, and finance approval still wouldn't be needed at $801. Only the 24-hour notice to finance would no longer be required.

## R06 — question H4

You need **both manager approval and finance approval**, and both must be in place before the purchase goes through.

**Why:**

1. **Use the total, not the subtotal.** Thresholds count the full amount including taxes and fees (EXP-4). The total is $2,480 + $35 = **$2,515**.
2. **The current threshold applies.** The transaction date is October 12, 2026, which is after July 1, 2025. So the $2,500 threshold applies (AMD-2, DEF-3), not the older $2,000 one.
3. **The total is over the threshold.** $2,515 is above $2,500, so EXP-2 applies: a routine non-travel purchase over $2,500 needs **both manager and finance approval before purchase**. Judged on the $2,480 subtotal alone, it would wrongly look like manager approval was enough.

**Not triggered:**
- **Travel-office approval:** not needed, because this isn't airfare or travel (TRV-1).
- **Emergency waiver:** doesn't apply. The purchase is described as routine, so it isn't a qualifying emergency (DEF-1, EMG-2). Even in an emergency, the waiver would only remove advance finance approval, never manager approval.

**One open point:** You didn't say which vendor this is. Vendor restrictions always apply (EXP-3). If the vendor is on the prohibited list, the purchase also needs specific written authorization from the compliance officer (VEN-1, VEN-2). Manager or finance approval does not replace that authorization.

## R07 — question H4

**You need both manager approval and finance approval before the purchase goes ahead.**

**Why:**
1. **Use the full total.** Thresholds are measured on the total amount including taxes and fees (`reference/01-expense-policy.md:14`, EXP-4). That's $2,480 + $35 = **$2,515**.
2. **The current threshold applies.** The transaction is dated October 12, 2026, which is after the July 1, 2025 amendment, so the limit is $2,500, not the old $2,000 (`reference/05-policy-amendments.md:7`, AMD-2).
3. **$2,515 is over $2,500.** For a routine non-travel purchase above $2,500, both manager and finance approval are needed before purchase (`reference/01-expense-policy.md:8`, EXP-2).

**Things to watch:**
- If you only compare the $2,480 subtotal to the limit, it looks like manager approval alone is enough. That's wrong. The $35 in taxes and fees pushes it over.
- The emergency waiver of advance finance approval doesn't apply. This is a routine transaction, and "urgent" alone doesn't count as a qualifying emergency (`reference/06-definitions.md:4`).
- No vendor was named. If the vendor turns out to be prohibited, you'd also need written authorization from the compliance officer. Manager or finance approval doesn't cover that (`reference/04-vendor-policy.md:4-7`).

## R08 — question H8

Two approvals apply, and both must be obtained **before the purchase**:

1. **Manager approval.** The purchase is dated October 12, 2026, so the current $2,500 limit applies (AMD-2, effective July 1, 2025). $850 is under that limit, so manager approval is the purchase-level approval required (EXP-1). EXP-1 is written for "non-travel" purchases, but EXP-3 and TRV-2 both say airfare is still subject to the purchase limits in the Expense Policy.
2. **Travel-office approval.** Airfare above $800 needs travel-office approval in advance (TRV-1). $850 is over $800. This approval is in addition to the manager's and doesn't replace it (TRV-2).

**Finance approval is not required.** $850 is under the $2,500 limit (EXP-2), so this has nothing to do with any emergency waiver.

**The emergency exception doesn't apply.** Calling the trip "urgent" isn't enough (DEF-1, EMG-3). The employee gave no facts showing an immediate operational or safety risk that can't wait for normal approval, so it isn't a qualifying emergency (EMG-2), and ordinary rules apply. Because of that, the 24-hour finance notification in EMG-1 is also not triggered. Even if the trip did qualify, the exception would only waive finance pre-approval. It would not waive manager or travel-office approval (EMG-1, EXP-3).

**Vendor status is unknown.** The facts don't say who the airfare vendor is. If it's a prohibited vendor, the purchase can't go ahead without specific written authorization from the compliance officer (VEN-1, VEN-2). Manager or travel-office approval can't stand in for that.

**Answer:** Get manager approval and travel-office approval before buying. Finance approval is not needed.

## R09 — question H5

**You need manager approval only, obtained before the purchase. Finance approval is not required.**

**Why:**

1. **The old limit applies.** The transaction is dated June 30, 2025, which is before the July 1, 2025 change. Under AMD-1, routine purchases of **$2,000 or less** need manager approval, and purchases **above $2,000** need both manager and finance approval. AMD-2 says the new $2,500 limit does not apply to earlier transactions, and DEF-3 says the Amendments Policy decides which limit applies based on the transaction date. EXP-1 and EXP-2 only cover purchases on or after July 1, 2025, so they don't apply here.
2. **$2,000 counts as "$2,000 or less."** EXP-4 says "or less" includes the stated amount. The total also includes taxes and fees.
3. **Manager approval comes first.** Under EXP-1, manager approval is needed "before purchase." DEF-2 defines "advance" as before the transaction proceeds.
4. **No other approvals are triggered:**
   - **Travel office:** not needed. The purchase isn't for travel, so TRV-1 doesn't apply.
   - **Emergency waiver:** not relevant. The purchase is described as routine, and the emergency exception only waives finance approval, which isn't needed anyway.

**One thing to check:** the vendor's status isn't given. Vendor rules always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without written authorization from the compliance officer (VEN-1, VEN-2). Manager approval doesn't count as that authorization.

## R10 — question H7

You need **manager approval before the purchase** and a **notice to finance within 24 hours after it**. Advance finance approval is waived, and no travel-office approval is needed.

**Why**

1. **The emergency exception applies.** The purchase is $4,200, under the $5,000 emergency cap (EMG-1). The vendor is normally prohibited, but EMG-2 lets the exception cover a prohibited vendor that has written compliance-officer authorization under VEN-2. You have that, and it covers this specific transaction (VEN-2), so the vendor requirement is met (VEN-1).

2. **Manager approval is required before proceeding.** An emergency never waives this (EMG-1, EMG-3, EXP-3). The manager's approval also does not stand in for the compliance authorization (VEN-2).

3. **Advance finance approval is waived.** Without the emergency, a $4,200 purchase on or after July 1, 2025 would need both manager and finance approval, because it is over $2,500 (EXP-2, AMD-2). The emergency exception removes the finance step (EMG-1, EXP-3).

4. **Finance must be notified within 24 hours after the purchase** (EMG-1). This is only a notice after the fact. It is not a finance approval (DEF-2).

5. **No travel-office approval is needed** because this isn't a travel purchase (TRV-1).

**One wording conflict:** EMG-1 says the exception covers an "approved vendor," but EMG-2 explicitly extends it to prohibited vendors with compliance authorization. I've read the two together so the exception applies here. If your organization reads EMG-1 strictly, the exception wouldn't apply, and you would need advance finance approval in addition to manager approval (EXP-2).

**Keep on file:** the compliance officer's written authorization, the manager's approval obtained before the purchase, the facts showing an immediate operational or safety risk (DEF-1; calling it "urgent" isn't enough), and proof you notified finance within 24 hours.

## R11 — question H6

**No. The 24-hour finance notification requirement was not met.** The rest of the purchase fits within the emergency exception, but notifying finance at 30 hours breaks one of the exception's conditions.

**What the policy requires**

1. **Normal approval rule (EXP-2, AMD-2, EXP-4).** The purchase date is after July 1, 2025, so the $2,500 routine threshold applies. A $4,000 non-travel purchase is over that threshold, so normally it needs both manager and finance approval before purchase.

2. **The emergency exception applies (EMG-1, DEF-1, VEN-3).** All three conditions are met:
   - The question says it is a qualifying emergency, which DEF-1 requires.
   - $4,000 is within the $5,000-or-less cap.
   - The vendor is approved.

   So **advance finance approval is waived**. Not getting it was allowed (EXP-3, EMG-1).

3. **Manager approval: met, if it came before the purchase (EMG-1, EMG-3, EXP-3).** The emergency exception never waives manager approval, and it must come "before proceeding." The facts say the manager approved but not when. If that approval came after the purchase, this is a second violation.

4. **Finance notification: not met (EMG-1, DEF-2).** Finance must be told within 24 hours after the purchase. This is a separate after-the-fact requirement, not a form of finance approval. Notice at 30 hours is 6 hours late.

5. **Requirements that don't apply:**
   - **Travel-office approval (TRV-1, TRV-2):** this is not a travel or airfare purchase.
   - **Vendor restrictions (VEN-1, VEN-2, EMG-2):** these only matter for prohibited vendors, and this vendor is approved.

**Summary**

| Requirement | Source | Status |
|---|---|---|
| Correct threshold for the date | AMD-2, EXP-2 | $2,500 applies; purchase is over it |
| Advance finance approval | EXP-2, EMG-1, EXP-3 | Waived by the emergency exception |
| Manager approval before purchase | EMG-1, EMG-3 | Met, assuming approval came first |
| Finance notified within 24 hours | EMG-1, DEF-2 | **Not met (30 hours)** |
| Vendor restrictions | VEN-1–3 | Not triggered (approved vendor) |
| Travel-office approval | TRV-1 | Not applicable |

The policy doesn't say whether a late notice cancels the finance-approval waiver after the fact. All it supports is that this requirement was violated.

## R12 — question H3

**No. The emergency exception doesn't apply, so advance finance approval is not waived.** The purchase needs **both manager approval and finance approval before it proceeds.**

**Why the exception doesn't apply**
- The exception covers only qualifying emergency purchases "totaling **$5,000 or less**" from an approved vendor (`reference/03-emergency-policy.md:4`).
- "Or less" includes $5,000 itself, and the limit applies to the full transaction amount including taxes and fees (`reference/01-expense-policy.md:14`).
- $5,001 is over the limit. The exception has no partial or pro-rated version, so it doesn't apply even though the emergency qualifies and the vendor is approved.

**The ordinary approval rules apply instead**
- The purchase date is October 12, 2026, which is after the July 1, 2025 amendment. So the current routine limit of $2,500 applies, not the old $2,000 limit (`reference/05-policy-amendments.md:7`, `reference/06-definitions.md:11`).
- A non-travel purchase above $2,500 needs **both manager and finance approval before purchase** (`reference/01-expense-policy.md:8`).

**Other requirements**
- **Vendor:** The vendor is approved, so no compliance-officer authorization is needed (`reference/04-vendor-policy.md`).
- **Travel:** This isn't a travel purchase, so travel-office approval doesn't apply.
- **24-hour finance notice:** The rule to notify finance within 24 hours after purchase belongs only to the emergency exception (`03-emergency-policy.md:4`). It doesn't apply here, and it would never replace advance finance approval anyway (`06-definitions.md:7`).

**One warning:** The short guide in `SUMMARY.md` says "Emergencies up to $5,000: finance preapproval waived." That's consistent with the full policy here, but it's easy to misread as covering any emergency near $5,000. Where they differ, the full policy controls (`06-definitions.md:10`).

If the total could be brought to $5,000 or less, including taxes and fees, the exception would apply. Advance finance approval would then be waived, but manager approval before purchase and notice to finance within 24 hours after purchase would still be required.

## R13 — question H7

**Two more things are required: manager approval before the purchase, and a notice to finance within 24 hours after it.** Advance finance approval is waived, and travel-office approval doesn't apply.

| Requirement | Required? | When | Source |
|---|---|---|---|
| Manager approval | **Yes** | **Before** the purchase | EMG-1, EMG-3, EXP-3 |
| Finance approval | **No, waived** | n/a | EMG-1, EXP-3 |
| Finance notification | **Yes** | **Within 24 hours after** the purchase | EMG-1, DEF-2 |
| Compliance-officer written authorization | Already in hand (it explicitly covers this transaction) | Before the purchase | VEN-1, VEN-2 |
| Travel-office approval | **No** (not a travel purchase) | n/a | TRV-1, EMG-1 |

**Why:**

1. **Which threshold applies.** The purchase is dated October 12, 2026, which is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3). At $4,200, a routine purchase would need both manager and finance approval in advance (EXP-2).
2. **The emergency exception applies.** EMG-1 covers a qualifying emergency of $5,000 or less from an approved vendor. This vendor is prohibited, but EMG-2 lets the exception apply anyway when there is written compliance-officer authorization under VEN-2. You've stated that authorization exists and explicitly covers this transaction, so the vendor restriction is satisfied (VEN-1).
3. **What the exception changes.** It waives only *advance finance approval* (EMG-1, EXP-3).
4. **What it doesn't change.** Manager approval is still required before the purchase (EMG-1, EMG-3, EXP-3). Finance must be notified within 24 hours afterward. That notice is not the same as finance approval (DEF-2).

**Assumptions:**
- The $4,200 is the total amount including taxes and fees (EXP-4). If the all-in total is over $5,000, the emergency exception doesn't apply. You'd then need advance finance approval as well as manager approval.
- I've taken it as given that the purchase meets the DEF-1 definition of an emergency: an immediate operational or safety risk that can't reasonably wait for normal approval. Calling it "urgent" alone wouldn't be enough (EMG-3).
- The compliance officer's authorization can't be inferred from manager or finance approval. It has to be its own written document (VEN-2).

## R14 — question H1

**Before the purchase:** you only need manager approval. **After the purchase:** finance must be notified within 24 hours. Travel-office approval and finance approval are not required.

**Before proceeding**
- **Manager approval is required.** The purchase date is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, EXP-1). Airfare counts against that threshold (EXP-3, TRV-2). $800 is at or below $2,500, so manager approval is needed. The emergency exception never removes this step (EMG-1, EMG-3, EXP-3).
- **Travel-office approval is not required.** It only applies to airfare *above* $800, and "$800 or less" includes exactly $800 (TRV-1, EXP-4). This assumes the $800 is the full amount including taxes and fees, which is how thresholds are measured (EXP-4).
- **Finance approval is not required.** An $800 purchase is under the threshold that would trigger it (EXP-2). Even if it weren't, a qualifying emergency of $5,000 or less from an approved vendor waives advance finance approval (EMG-1).
- **Compliance-officer authorization is not required.** The vendor is approved, not prohibited (VEN-1–VEN-3, EMG-2).

**After proceeding**
- **Finance must be notified within 24 hours** of the purchase (EMG-1). This is a notice after the fact, not an approval (DEF-2).

**Caveat:** this answer takes your word that the situation is a qualifying emergency. That means an immediate operational or safety risk that can't reasonably wait for normal approval (DEF-1). Calling it "urgent" isn't enough (EMG-3). If it doesn't qualify, ordinary rules apply (EMG-2): you'd still need manager approval only. On a strict reading, the 24-hour finance notice is tied to using the emergency exception, so it might not apply in that case.

## R15 — question H6

**No, not every requirement was met.** Finance was notified 6 hours late. Everything else complied, assuming the manager approved before the purchase.

**Which rules apply**
- The purchase is on Oct 12, 2026, which is after July 1, 2025, so the current $2,500 routine threshold applies (AMD-2, DEF-3). At $4,000, a routine purchase would normally need **both manager and finance approval in advance** (EXP-2).
- The Emergency Policy can waive advance finance approval only (EXP-3). Its exception in EMG-1 has three conditions, and all are met:
  - The facts state it is a qualifying emergency, so DEF-1 is satisfied and EMG-2 doesn't block it.
  - The total is $4,000, which is within the $5,000 limit.
  - The vendor is approved, so the prohibited-vendor rules (VEN-1/VEN-2) don't come into play.

**Requirement by requirement**

| Requirement | Source | Status |
|---|---|---|
| Advance finance approval | EXP-2, waived by EMG-1 | ✅ Not needed, so not getting it is fine |
| Manager approval before proceeding | EMG-1, EXP-3, EMG-3 | ✅ Met, as long as the manager approved before the purchase (see note) |
| Notify finance within 24 hours after purchase | EMG-1, DEF-2 | ❌ **Not met.** Notice came at 30 hours |
| Vendor restrictions | VEN-1–3 | ✅ Approved vendor |
| Travel-office approval | TRV-1 | ✅ Doesn't apply because this isn't a travel purchase |

**Conclusion**
The emergency exception correctly removed the need for advance finance approval. However, EMG-1 also requires finance to be notified within 24 hours, and 30 hours misses that deadline. Under DEF-2, this notice is its own after-purchase requirement, separate from finance approval.

**Note:** The facts say "the manager approves" without saying when. EMG-1 requires approval *before proceeding*. If the manager approved only after the purchase, that would be a second violation.

## R16 — question H4

**You need both manager approval and finance approval before the purchase.**

**Why:**

1. **Total amount is $2,515.** Thresholds are based on the full transaction amount, including taxes and fees (EXP-4). So it's $2,480 + $35 = $2,515.
2. **The current threshold applies.** The transaction date, October 12, 2026, is after the July 1, 2025 amendment, so the routine threshold is $2,500 (AMD-2, DEF-3). The older $2,000 limit in AMD-1 doesn't apply.
3. **$2,515 is over the threshold.** Routine non-travel purchases above $2,500 need both manager and finance approval in advance (EXP-2). The manager-only rule covers only amounts of $2,500 or less (EXP-1).
4. **"In advance" means before the transaction goes ahead** (DEF-2).

**Rules that don't change the answer:**

- **Travel Policy:** It doesn't apply because this is a non-travel transaction (EXP-3).
- **Emergency exception:** It doesn't apply. The transaction is described as routine, and nothing shows an immediate operational or safety risk (DEF-1, EMG-2). Even a qualifying emergency would only waive *advance finance* approval. Manager approval would still be required (EMG-1, EXP-3).
- **Vendor:** The facts don't say who the vendor is. Vendor restrictions always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without specific written authorization from the compliance officer. That requirement is in addition to the other approvals, and manager or finance approval can't stand in for it (VEN-1, VEN-2). Check the vendor's status before proceeding.

## R17 — question H3

**No, the emergency exception doesn't apply.** You need both manager approval and finance approval before the purchase.

**Why the exception doesn't apply**
- Under EMG-1, the exception only covers a qualifying emergency purchase that totals **$5,000 or less** and comes from an approved vendor. "Or less" includes $5,000 itself (EXP-4).
- The amount is measured as the full transaction total in US dollars, including taxes and fees (EXP-4).
- $5,001 is over the $5,000 limit. So even though the emergency qualifies and the vendor is approved, the purchase falls outside the exception. Advance finance approval is **not** waived.

**Which normal rule applies instead**
- The purchase is on October 12, 2026, which is after July 1, 2025. The current $2,500 routine threshold therefore applies (AMD-2, DEF-3).
- $5,001 is above $2,500. Under EXP-2, a non-travel purchase that size needs **both manager and finance approval before purchase**.

**Approvals required (all before the purchase)**
1. Manager approval (EXP-2). This is required in any case, since the emergency policy never waives manager approval (EXP-3, EMG-1, EMG-3).
2. Finance approval in advance (EXP-2). "Advance" means before the transaction proceeds (DEF-2).

**Approvals not required**
- **Travel-office approval:** this isn't airfare, so TRV-1 doesn't apply.
- **Compliance-officer authorization:** the vendor is approved, not prohibited, so VEN-1 and VEN-2 don't apply.
- **Finance notification within 24 hours:** EMG-1 requires this only when the exception applies. Here, finance approves in advance instead. A post-purchase notice is not a substitute for that approval (DEF-2).

## R18 — question H1

**Before the purchase:** you need manager approval, and nothing else.

**After the purchase:** you must notify finance within 24 hours.

**Why:**

1. **Manager approval is required before proceeding.** EMG-1 says manager approval "remains required before proceeding." EXP-3 and EMG-3 add that an emergency never waives it. The amount alone would also require it: $800 is under the $2,500 limit that has applied since July 1, 2025 (EXP-1, AMD-2).

2. **Travel-office approval is not required.** TRV-1 only requires it for airfare *above* $800, and says "$800 or less do not require travel-office approval." EXP-4 says "or less" includes the amount itself, so exactly $800 is under the line. The emergency exception doesn't waive travel-office approval (EMG-1), but here it simply doesn't apply.

3. **Advance finance approval is not required.** It's waived because the purchase is a qualifying emergency of $5,000 or less from an approved vendor (EMG-1). Even without the emergency, $800 is below the $2,500 limit where finance approval would kick in (EXP-1/EXP-2, TRV-2).

4. **Finance must be notified within 24 hours after the purchase.** This comes from EMG-1. It is only a notice after the fact, not an approval (DEF-2).

5. **No compliance-officer authorization is needed.** That only applies to prohibited vendors (VEN-1/VEN-2), and this vendor is approved.

This assumes the facts actually meet the emergency definition in DEF-1: an immediate operational or safety risk that can't wait for normal approval. Calling it "urgent" isn't enough (EMG-2/EMG-3). If it doesn't qualify, the approvals before purchase stay the same (manager only), but the 24-hour finance notice no longer applies, because that rule comes only from the emergency exception.

## R19 — question H3

**No. The emergency exception doesn't apply, so advance finance approval is still required.** Both manager and finance approval are needed before the purchase.

**Why the exception doesn't apply**
- Under EMG-1 (`03-emergency-policy.md:4`), advance finance approval is waived only for a qualifying emergency purchase "totaling **$5,000 or less**" from an approved vendor.
- EXP-4 (`01-expense-policy.md:14`) says thresholds use the total transaction amount, including taxes and fees, and that "or less" includes the limit itself. $5,001 is over $5,000, so the purchase falls outside the exception even though it is a qualifying emergency and the vendor is approved.

**Which rules apply instead**
- **Threshold:** The purchase date is October 12, 2026, which is after the amendment took effect on July 1, 2025. So the current $2,500 routine threshold applies (AMD-2, DEF-3).
- **Approvals:** $5,001 is above $2,500, so EXP-2 (`01-expense-policy.md:8`) requires **both manager and finance approval before purchase**.

**Required approvals**
1. **Manager approval before purchase.** This would be required even if the exception applied (EXP-3, EMG-3).
2. **Finance approval before purchase.** It is not waived because the amount is over the $5,000 cap.

**Not required**
- **Travel-office approval:** The purchase isn't travel, so TRV-1 doesn't apply.
- **Compliance-officer authorization:** The vendor is approved, not prohibited (VEN-1/VEN-2).
- **24-hour finance notification:** This post-purchase step belongs to the emergency exception, so it doesn't apply here. Finance has to approve in advance, which is a stronger requirement (DEF-2).

## R20 — question H8

**Two advance approvals apply: manager approval and travel-office approval.** Finance approval is not required, and the emergency exception does not apply.

**1. Manager approval, before purchase**
- The purchase is on October 12, 2026, which is after the July 1, 2025 effective date. So the current $2,500 threshold applies, not the older $2,000 one (AMD-2, DEF-3).
- EXP-1 is written for "non-travel" purchases. But EXP-3 and TRV-2 say airfare and all travel expenses still fall under the applicable purchase threshold in the Expense Policy.
- $850 is at or below $2,500, so manager approval is required before purchase (EXP-1, EXP-4).

**2. Travel-office approval, before purchase**
- Airfare above $800 needs advance travel-office approval (TRV-1). $850 is above $800.
- This approval is in addition to manager approval and does not replace it (TRV-2).

**Finance approval is not required.** The amount is under the $2,500 threshold, so EXP-2 does not apply.

**The emergency exception does not apply:**
- Calling the trip "urgent" is not enough to make it a qualifying emergency (DEF-1, EMG-3).
- The employee gave no facts showing an immediate operational or safety risk that can't wait for normal approval. Without those facts, emergency status is not established and the normal approvals apply (EMG-2).
- Even a real emergency would not change the outcome here. The exception only waives advance finance approval, which isn't needed at this amount anyway. It never waives manager approval or travel-office approval (EMG-1, EXP-3).
- Because the exception doesn't apply, there is no 24-hour notice to finance either. That notice is only required for emergency purchases (EMG-1, DEF-2).

**What isn't known:** the question doesn't say who the airline or vendor is. If it is a prohibited vendor, the purchase can't go ahead without specific written authorization from the compliance officer, whether or not other approvals are in place (VEN-1, VEN-2, EXP-3). The facts given aren't enough to rule this out.

## R21 — question H5

**You only need manager approval, and you need it before the purchase.** Finance approval is not required.

The date is what decides this. June 30, 2025 is one day before the threshold changed, so the older rule applies:

- **The older rule (AMD-1, `reference/05-policy-amendments.md:4`):** Before July 1, 2025, a routine purchase of **$2,000 or less** needed manager approval only. Finance approval was added only for purchases **above** $2,000.
- **"Or less" includes the limit itself (EXP-4, `reference/01-expense-policy.md:14`):** The total counts taxes and fees, so a total of exactly $2,000 falls in the manager-only tier.
- **The $2,500 limit doesn't apply here (AMD-2, `reference/05-policy-amendments.md:7`):** It started on July 1, 2025 and does not reach back to earlier dates. DEF-3 says the Amendments Policy controls which limit applies to a given transaction date.
- **"Before" means before the purchase (EXP-1 and DEF-2):** The approval has to come before the transaction goes ahead.

Under either limit, $2,000 needs only manager approval. The date matters because if the total were even slightly above $2,000, say $2,000.01, a June 30 transaction would also need finance approval.

**One condition:** this assumes the vendor isn't on the prohibited list. If it is, the purchase also needs written authorization from the compliance officer before it can go ahead (VEN-1). Manager approval doesn't replace that. Since this isn't travel or an emergency, those policies don't apply.

## R22 — question H6

**No, not every requirement was met.** Finance was notified 30 hours after the purchase, and the Emergency Policy requires notice within 24 hours. Everything else checks out.

**Requirement by requirement**

| Requirement | Source | Met? |
|---|---|---|
| Qualifying emergency (an immediate operational or safety risk that can't wait for normal approval) | EMG-1, DEF-1 | ✅ Yes, the question says it qualifies |
| Total of $5,000 or less | EMG-1, EXP-4 | ✅ Yes, $4,000 |
| Approved vendor | EMG-1, VEN-3 | ✅ Yes |
| Advance finance approval | EXP-2 would normally require it, since $4,000 is over the $2,500 limit | ✅ Not needed: EMG-1 and EXP-3 waive it for qualifying emergencies |
| Manager approval **before the purchase** | EMG-1, EXP-3, EMG-3 | ✅ Probably. The question says the manager approved but not when. It only counts if the approval came before the purchase. |
| Travel-office approval | TRV-1 | ✅ Not needed, because this isn't a travel purchase |
| Finance notified **within 24 hours after the purchase** | EMG-1 | ❌ **No, notice came at 30 hours, 6 hours late** |

**Why the missing finance approval isn't the problem**

The current $2,500 limit applies because the purchase date, October 12, 2026, is after July 1, 2025 (AMD-2, DEF-3). At $4,000, a routine purchase would need both manager and finance approval in advance. The emergency exception removes only the advance finance approval. It keeps manager approval and adds the 24-hour notice rule (EMG-1). DEF-2 says that notice rule is a separate step taken after the purchase, not a form of finance approval. So skipping finance approval was allowed, but the late notice still breaks the rule.

**Caveat:** The policies don't say what happens when notice is late, such as whether the exception is lost. I'd treat it as a compliance failure and not guess at the penalty.

## R23 — question H2

**Before buying:**
1. **Manager approval.** This is always required, even in an emergency (EMG-1, EMG-3, EXP-3).
2. **Travel-office approval.** $801 is over the $800 airfare limit (TRV-1), and the emergency exception does not remove this requirement (EMG-1).

**After buying:**
3. **Notify finance within 24 hours.** This is a notice only, not an approval (EMG-1, DEF-2).

**Not required:**
- **Advance finance approval.** The emergency exception waives it for approved-vendor purchases of $5,000 or less (EMG-1). Finance approval wouldn't be needed anyway: the purchase date is after July 1, 2025, so the current $2,500 limit applies (AMD-2), and $801 is under it (EXP-1).
- **Compliance-officer authorization.** That is only needed for prohibited vendors (VEN-1, VEN-2), and this vendor is approved.

All of this assumes the situation really is a qualifying emergency: an immediate operational or safety risk that can't wait for normal approval (DEF-1). Calling it "urgent" isn't enough. If it doesn't qualify, the normal rules apply, which here means the same two approvals beforehand and no finance notice afterward.

## R24 — question H8

Two advance approvals apply: **manager approval** and **travel-office approval**, both before the ticket is bought. Finance approval is not needed.

**1. Calling the trip "urgent" doesn't make it an emergency**
- A qualifying emergency needs "an immediate operational or safety risk that cannot reasonably await normal approval" (DEF-1). Merely calling a request urgent isn't enough (DEF-1, EMG-3).
- Without facts that meet DEF-1, the emergency exception doesn't apply and the normal approvals do (EMG-2).

**2. Manager approval is required in advance**
- The purchase is on October 12, 2026, after July 1, 2025, so the current $2,500 limit applies (AMD-2, DEF-3).
- Airfare is still subject to the purchase limits in the Expense Policy (EXP-3, TRV-2). $850 is at or under $2,500, so the manager must approve before purchase (EXP-1).
- Finance approval isn't needed because $850 is under the $2,500 limit (EXP-2).

**3. Travel-office approval is required in advance**
- Airfare over $800 needs advance travel-office approval on top of the purchase approvals (TRV-1). $850 is over $800, and the $800 limit includes taxes and fees (EXP-4).
- Travel-office approval doesn't replace manager approval (TRV-2).

**4. The answer would be the same if it were an emergency**
- The emergency exception only waives advance finance approval, which isn't required here anyway. It never waives manager approval or travel-office approval (EMG-1, EXP-3).
- No finance notification within 24 hours is required, because that rule only applies to a qualifying emergency (EMG-1).

**Vendor caveat:** The question doesn't say whether the airline is a prohibited vendor. If it is, the purchase can't go ahead without written authorization from the compliance officer (VEN-1, VEN-2). Manager and travel-office approval don't count as that authorization.
