# Precommitted grading rubric v1.0

Each answer receives 0–10 points: conclusion (0–4), applicable rules (0–2), exceptions/dependencies (0–2), evidence references (0–1), unsupported claims (0–1). Total: 80.

**Conclusion (4):** 4 if fully correct; 2 if partly correct but missing a material requirement; 0 if incorrect or no supported answer. **Applicable rules (2):** 2 if all mandatory approvals/prohibitions are recognized; 1 if partial; 0 if absent or wrong. **Exceptions/dependencies (2):** 2 if all relevant exceptions/cross-document/time conditions are correctly handled; 1 if partially handled without reversing outcome; 0 otherwise. If no exception applies, accurately not inventing an exception earns 2. **Evidence (1):** 1 only if the answer names at least one correct section identifier AND includes no false source identifier; 0 otherwise. **Unsupported claims (1):** 1 if there are no material unsupported claims; 0 otherwise.

**Hard cap:** If the final operational conclusion is wrong, total score cannot exceed 4. Missing a required approval constitutes a wrong operational conclusion. **No policy access:** Correct answers from a no-folder control may be scored on their merits, but generic assertions of unknowability do not earn conclusion points when the underlying answer is checkable; appropriate transparent uncertainty is described separately in results.

Secondary metrics, reported separately: critical omissions (by Q against the answer key), false authorizations (Q4 and Q8, and Q7 if waiver asserted), unsupported material assertions, visible source reads, measured wall time when tooling supports it, and run-to-run consistency. Never estimate token usage as measured tokens or treat a citation as proof the source was read.

A blinded assessor should score raw responses using this precommitted key, without changing the rubric after seeing outputs. Disagreements are logged and adjudicated. No fabricated or reconstructed transcripts are admissible.

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

# QUESTIONS

**H1.** Under Meridian Works policy, on October 12, 2026, an approved-vendor qualifying emergency requires an airfare purchase totaling exactly $800. Which approvals and notifications apply before and after proceeding?

**H2.** Under Meridian Works policy, on October 12, 2026, an approved-vendor qualifying emergency requires an airfare purchase totaling $801. Which approvals and notifications apply before and after proceeding?

**H3.** A qualifying emergency on October 12, 2026 involves a $5,001 non-travel purchase from an approved vendor. Does the emergency exception waive advance finance approval, and what approvals are required?

**H4.** A routine, non-travel transaction on October 12, 2026 has a $2,480 subtotal and $35 in taxes and fees. What approvals are required before proceeding?

**H5.** A routine, non-travel transaction on June 30, 2025 has a total of exactly $2,000. What approvals are required before proceeding?

**H6.** On October 12, 2026 an approved-vendor qualifying emergency requires a $4,000 non-travel purchase. The manager approves, finance is notified 30 hours after purchase, and no advance finance approval was obtained. Was every policy requirement satisfied? Explain.

**H7.** On October 12, 2026, a $4,200 non-travel purchase qualifies as an emergency and uses a prohibited vendor for which written compliance-officer authorization explicitly covers this transaction. What other approvals and notifications are required?

**H8.** On October 12, 2026, an employee describes an $850 airfare purchase as an urgent business trip, but provides no facts showing an immediate operational or safety risk that cannot await normal approval. What approvals apply?

# RESPONSES TO SCORE (shuffled; arm identity withheld; directory paths stripped)

## R01 — answers H7

Advance finance approval is waived. Two things are still required: **manager approval before the purchase** and **notifying finance within 24 hours after it**.

**Required**
1. **Manager approval in advance.** It must come before the transaction goes ahead. The emergency exception never waives it (EMG-1, EMG-3, EXP-3), and "advance" means before the transaction proceeds (DEF-2).
2. **Finance notified within 24 hours after the purchase** (EMG-1). This is a notice after the fact, not an approval (DEF-2).

**Not required**
- **Advance finance approval.** On its own, $4,200 would need finance approval: the date is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3), and $4,200 is above it (EXP-2, EXP-4). EMG-1 waives that approval here because:
  - you've stated the emergency qualifies under DEF-1;
  - $4,200 is under the $5,000 emergency cap;
  - the vendor is prohibited, but EMG-2 lets the emergency exception apply when there's written compliance-officer authorization under VEN-2. VEN-2 requires that authorization to name the specific transaction, and you said it covers this one.
- **Travel-office approval.** It only applies to airfare over $800 (TRV-1), and this is a non-travel purchase.

**Compliance-officer authorization**
You already have it, so nothing more is needed. It's still a separate requirement: without it the purchase couldn't go ahead, emergency or not (VEN-1, EMG-3). Manager or finance approval can't stand in for it (VEN-2).

One caveat: EMG-1 is written for purchases "from an approved vendor." I've read EMG-2 as extending the exception to a prohibited vendor once VEN-2 authorization is in place. If that reading were rejected, the exception wouldn't apply, and the default rule (EXP-2) would require both manager and finance approval in advance.

## R02 — answers H4

**You need both manager approval and finance approval, and both must be in place before the purchase.**

1. **Use the full total.** Thresholds are measured on the total amount including taxes and fees (EXP-4). $2,480 + $35 = **$2,515**.
2. **The $2,500 threshold applies.** The transaction is dated October 12, 2026, which is after July 1, 2025, so the current threshold is used. The older $2,000 limit applied only before that date (AMD-1, AMD-2).
3. **$2,515 is above $2,500,** so both approvals are needed before purchase (EXP-2, `reference/01-expense-policy.md:8`).

The subtotal alone ($2,480) is under the threshold, so it's easy to conclude that only a manager needs to approve. That's wrong: the $35 in taxes and fees pushes the total over $2,500.

**Other conditions:**
- **Vendor:** You didn't say who the vendor is. If it's on the prohibited list, you also need written authorization from the compliance officer. Manager or finance approval doesn't replace that (VEN-1, VEN-2).
- **Emergency waiver:** The emergency rule can waive advance finance approval, but it doesn't apply here. The purchase is routine, and calling something "urgent" doesn't make it an emergency (DEF-1).
- **Travel policy:** This isn't a travel purchase, so the travel rules don't apply.

## R03 — answers H3

**No. The emergency exception does not apply, so advance finance approval is still required.**

**Why the exception doesn't apply**
- EMG-1 (`reference/03-emergency-policy.md:4`) waives advance finance approval only for a qualifying emergency purchase "totaling **$5,000 or less**" from an approved vendor.
- $5,001 is over that limit. EXP-4 (`reference/01-expense-policy.md:14`) says thresholds use the total amount including taxes and fees, and "or less" includes the limit itself. So $5,000.00 would qualify, but $5,001 does not.
- The emergency qualifying and the vendor being approved don't change this. The dollar limit is a separate condition, and all of them must be met.

**Approvals required: the normal routine rules**
- The purchase date is October 12, 2026, which is after the July 1, 2025 amendment. So the current $2,500 threshold applies (AMD-2, `reference/05-policy-amendments.md:7`), not the old $2,000 one.
- Under EXP-2 (`reference/01-expense-policy.md:8`), a non-travel purchase over $2,500 needs **both manager approval and finance approval before the purchase**.
- **Travel-office approval:** not needed, because this isn't travel or airfare (TRV-1).
- **Compliance-officer authorization:** not needed, because the vendor is approved (VEN-1/VEN-3).
- **24-hour finance notification:** this requirement comes from the emergency exception, so it doesn't apply here. Finance has to approve in advance instead.

**A note on SUMMARY.md:** its line "Emergencies up to $5,000: finance preapproval waived" is consistent with this answer. But the summary leaves out conditions like the approved-vendor requirement and the 24-hour notice. Under DEF-3, the full policy documents control, and that's what this answer is based on.

**Bottom line:** Get manager and finance approval before buying. The emergency exception can't be used for $5,001. If the total could be brought down to $5,000 or less, the exception would apply. Then only manager approval would be needed beforehand, and finance would have to be notified within 24 hours after the purchase.

## R04 — answers H1

Here is what applies, based on the policy files in `reference/`.

## Before the purchase
**Manager approval is the only approval needed in advance.**

- **Manager approval: required.** The purchase is on October 12, 2026, so the current $2,500 limit applies (AMD-2, DEF-3). The policy calls $2,500 the "routine non-travel" limit. However, EXP-3 and TRV-2 say airfare and all travel expenses still follow the purchase threshold. Thresholds count the full amount including taxes and fees, and "or less" includes the limit itself (EXP-4). $800 is under $2,500, so manager approval is needed before buying (EXP-1). The emergency exception does not remove this requirement (EXP-3, EMG-1, EMG-3).
- **Travel-office approval: not required.** It is only needed for airfare **above** $800. Amounts of "$800 or less" are exempt, so exactly $800 is exempt (TRV-1). If the total were even slightly over $800, this approval would be needed before buying. The emergency exception would not waive it (EMG-1).
- **Finance approval: not required.** At $800 it isn't triggered (EXP-1 vs. EXP-2). In any case, a qualifying emergency purchase of $5,000 or less from an approved vendor waives advance finance approval (EMG-1).
- **Compliance-officer authorization: not required.** The vendor is approved (VEN-3). VEN-1 and VEN-2 only cover prohibited vendors.

## After the purchase
- **Notify finance within 24 hours** (EMG-1). This is only a notification after the fact, not an approval (DEF-2).

## Caveat
The emergency conclusions assume the situation really meets DEF-1: an immediate operational or safety risk that can't reasonably wait for normal approval. Calling it "urgent" isn't enough (EMG-3). If it doesn't qualify, the ordinary rules apply (EMG-2). Manager approval beforehand would still be needed, but the 24-hour finance notice under EMG-1 would not apply.

## R05 — answers H4

**You need both manager approval and finance approval before the purchase goes ahead.**

1. **Total amount:** $2,480 + $35 = **$2,515**. Thresholds are based on the total including taxes and fees (EXP-4), not the subtotal.
2. **Which threshold applies:** The transaction is dated October 12, 2026, which is after the July 1, 2025 amendment. So the $2,500 threshold applies (AMD-2, DEF-3), not the older $2,000 one.
3. **The rule:** A routine non-travel purchase above $2,500 needs both manager and finance approval before purchase (EXP-2). $2,515 is above that limit.

**What doesn't apply:**
- **Travel-office approval:** Not needed, because this isn't an airfare or travel purchase (TRV-1).
- **Emergency waiver:** The purchase is described as routine, so it isn't a qualifying emergency (DEF-1, EMG-2). Advance finance approval is not waived.
- **Vendor restrictions:** The facts don't say who the vendor is. If it's on the prohibited list, the purchase can't go ahead without written authorization from the compliance officer (VEN-1). Manager and finance approval don't count as that authorization (VEN-2).

Using the $2,480 subtotal alone would wrongly put this under the threshold, where only manager approval is needed.

## R06 — answers H5

**Answer: You need manager approval before the purchase proceeds. Finance approval isn't required.**

**Which threshold applies:** June 30, 2025 is one day before the threshold increase took effect.
- The $2,500 limit in EXP-1 and EXP-2 only covers purchases "incurred on or after July 1, 2025." AMD-2 says it "does not apply retroactively."
- DEF-3 says the Amendments Policy decides which threshold applies based on the transaction date. So the earlier rule in AMD-1 governs this purchase.

**How the old rule applies:** Under AMD-1, before July 1, 2025, "routine purchases of $2,000 or less required manager approval." Only purchases "above $2,000" also needed finance approval.
- EXP-4 says "or less" includes the amount itself, so exactly $2,000 falls in the manager-only tier.
- EXP-4 also says thresholds use the total amount including taxes and fees. The question gives the total as exactly $2,000, so it qualifies.

**Approval timing:** EXP-1 says approval comes "before purchase." DEF-2 defines "advance" as before the transaction proceeds.

**What else was checked:**
- **Travel (TRV-1, TRV-2):** Doesn't apply, since this isn't travel or airfare, so no travel-office approval is needed.
- **Emergency (EMG-1 to EMG-3, DEF-1):** No emergency is described, and it wouldn't matter anyway. The emergency rule only waives finance approval, and none is needed here.
- **Vendor (VEN-1, VEN-2):** The vendor's status isn't given. If the vendor is prohibited, the purchase also needs written authorization from the compliance officer before it can proceed. Manager approval doesn't replace that. I can't say whether this applies without the vendor's status.

If the purchase were even slightly over $2,000 on that date, it would need both manager and finance approval (AMD-1).

## R07 — answers H5

**You only need manager approval, and you need it before the purchase.**

**Why:**

1. **The old threshold applies.** The transaction date is June 30, 2025, one day before the threshold changed on July 1, 2025. The new $2,500 limit "does **not** apply retroactively" (`05-policy-amendments.md:7`). The Amendments Policy decides which threshold applies to a given date (`06-definitions.md:10`). That makes AMD-1 the rule here, not EXP-1 or EXP-2, which only cover purchases on or after July 1, 2025.
2. **$2,000 counts as "$2,000 or less."** Under AMD-1, routine purchases of **$2,000 or less** need manager approval only (`05-policy-amendments.md:4`). The policy says "or less" includes the amount itself (`01-expense-policy.md:14`), so exactly $2,000 is under the limit. Finance approval is only needed above $2,000.
3. **Nothing else applies.**
   - **Travel:** It isn't travel, so travel-office approval isn't needed.
   - **Emergency:** No emergency facts are given, so the emergency policy doesn't come into play (`03-emergency-policy.md:7`).
   - **Vendor:** No vendor is named. If the vendor were on the prohibited list, written approval from the compliance officer would also be needed (`04-vendor-policy.md:4`).

**One thing to check:** the $2,000 must be the full amount including taxes and fees (`01-expense-policy.md:14`). If anything pushes the total even slightly above $2,000, finance approval is also required.

## R08 — answers H5

**Only manager approval is needed before purchase.** Finance approval is not required.

**Why:**

1. **The older limit applies.** The transaction is dated June 30, 2025, one day before the July 1, 2025 change. Under `reference/05-policy-amendments.md:4` (AMD-1), purchases before that date use the old $2,000 limit. AMD-2 (`:7`) says the new $2,500 limit "does not apply retroactively." DEF-3 (`reference/06-definitions.md:10`) confirms that the Amendments Policy decides which limit applies for a given date. EXP-1 and EXP-2 only cover purchases made on or after July 1, 2025, so they don't apply here.
2. **$2,000 is within the limit.** AMD-1 sets "$2,000 or less" for manager approval only, and finance approval starts "above $2,000." EXP-4 (`reference/01-expense-policy.md:14`) says the "or less" wording includes the limit itself, so exactly $2,000 counts. Note that the amount is the full total, including taxes and fees.

**Other policies:**
- **Travel and emergency policies:** neither applies, because the purchase is a routine non-travel transaction.
- **Vendor policy:** this applies to every purchase (EXP-3). If the vendor is on the prohibited list, the purchase also needs written authorization from the compliance officer (VEN-1, `reference/04-vendor-policy.md:4`). Manager approval can't stand in for that. The question doesn't say what kind of vendor it is, so this only matters if the vendor is prohibited.

`SUMMARY.md` says purchases "Up to $2,500" need only a manager. That gives the same answer here, but only by chance, because it ignores the date. The full policy documents take priority over the summary.

## R09 — answers H6

**No, not every requirement was met.** Finance was notified 30 hours after the purchase, and the policy requires notice within 24 hours.

**What was satisfied**
- **The emergency exception applies.** The purchase is a qualifying emergency from an approved vendor, and $4,000 is under the $5,000 cap. Totals include taxes and fees (EMG-1, EXP-4, VEN-3).
- **Advance finance approval was not needed.** Normally a non-travel purchase over $2,500 on or after July 1, 2025 needs both manager and finance approval in advance (EXP-2, AMD-2). The emergency exception waives the finance approval, so not getting it was fine (EMG-1, EXP-3).
- **There are no vendor or travel issues.** The vendor is approved, not prohibited (VEN-1, EMG-2), and this isn't airfare, so travel-office approval doesn't apply (TRV-1).

**What failed**
- **Finance notice was late.** EMG-1 requires finance to be notified within 24 hours after the purchase, and 30 hours is outside that window. Notice after the purchase is a separate requirement from advance approval, and it isn't waived (DEF-2).

**Not enough information**
- **Timing of the manager's approval.** EMG-1 and EXP-3 require manager approval *before* the purchase, and DEF-2 defines "advance" as before the transaction proceeds. The facts say the manager approved but not when. If the approval came after the purchase, that is a second violation.

The exception correctly removed the need for advance finance approval, but the late notice means the transaction did not fully comply.

## R10 — answers H6

**No, not every requirement was met.** Finance was notified 30 hours after the purchase, and the policy allows at most 24.

**Requirements that were met**

| Requirement | Source | Status |
|---|---|---|
| The purchase is a qualifying emergency | EMG-1, DEF-1 | ✅ The facts say it is a qualifying emergency, so this isn't just an "urgent" label (EMG-3). |
| The total is $5,000 or less | EMG-1, EXP-4 | ✅ $4,000 |
| The vendor is approved | EMG-1, VEN-3 | ✅ The facts say the vendor is approved, so the prohibited-vendor rules (VEN-1/2) don't apply. |
| Advance finance approval | EXP-2, EXP-3, EMG-1 | ✅ Waived. Normally a $4,000 purchase needs it, because it's above the $2,500 limit that has applied since July 1, 2025 (AMD-2). The emergency exception removes that requirement, so not getting it isn't a violation. |
| Travel-office approval | TRV-1 | ✅ Doesn't apply, because this isn't a travel purchase. |
| Manager approval before the purchase | EMG-1, EXP-3 | ✅ Probably met. The manager approved, but the facts don't say when. The policy requires approval *before proceeding*, so if it came after the purchase, this would be a second violation. |

**Requirement that was not met**

- **Notifying finance within 24 hours of the purchase (EMG-1)**: ❌ Notice came at 30 hours, 6 hours late. DEF-2 says this notice is a separate requirement that applies after the purchase. It isn't the same thing as finance approval, so waiving the approval doesn't excuse a late notice.

**Conclusion:** The purchase qualified for the emergency exception, so skipping advance finance approval was allowed. But the late notice means the policy wasn't fully followed. That's true regardless of when the manager approved; early manager approval only rules out a second problem.

## R11 — answers H1

**Before the purchase: manager approval only. After the purchase: notify finance within 24 hours.**

**Before proceeding**
- **Manager approval is required.** The emergency exception never removes it (`reference/03-emergency-policy.md:4`, `reference/01-expense-policy.md:11`, `reference/03-emergency-policy.md:10`).
- **Advance finance approval is not required.** The purchase qualifies for the emergency exception: it's a qualifying emergency, it totals $5,000 or less ($800), and the vendor is approved (`reference/03-emergency-policy.md:4`). It wouldn't be needed in any case, because $800 is under the $2,500 routine threshold that applies to purchases on or after July 1, 2025 (`reference/01-expense-policy.md:5`, `reference/05-policy-amendments.md:7`).
- **Travel-office approval is not required.** It applies only to airfare *above* $800. "Amounts of $800 or less do not require travel-office approval" (`reference/02-travel-policy.md:4`). The total includes taxes and fees (`reference/01-expense-policy.md:14`), so this holds only if $800 is the full amount. If fees push it even a cent higher, travel-office approval is needed, and the emergency exception doesn't waive it.
- **No compliance-officer authorization is needed,** because the vendor is approved (`reference/04-vendor-policy.md:4-10`).

**After proceeding**
- **Notify finance within 24 hours of the purchase.** This is a notice, not an approval (`reference/03-emergency-policy.md:4`, `reference/06-definitions.md:7`).

**Caveats**
- This assumes the emergency really meets DEF-1: an immediate operational or safety risk that can't reasonably wait for normal approval. Calling it "urgent" isn't enough (`reference/06-definitions.md:4`).
- Today is October 13, 2026. If the purchase was made on October 12, the 24-hour window to notify finance is closing or may already have passed, so send the notice now.

## R12 — answers H8

Two advance approvals apply: **manager approval** and **travel-office approval**, both before the airfare is purchased. Finance approval is not required.

**1. Manager approval (in advance)**
- The purchase date is October 12, 2026, which is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3).
- $850 is $2,500 or less, so manager approval is required before purchase (EXP-1).
- EXP-1 says "routine non-travel purchase," but EXP-3 and TRV-2 say airfare and all travel expenses are still subject to the purchase threshold. So the manager-approval tier applies.

**2. Travel-office approval (in advance)**
- Airfare above $800 needs advance travel-office approval (TRV-1). $850 is over that line.
- This is separate from manager approval and doesn't replace it (TRV-2).

**3. Finance approval: not required**
- $850 is under the $2,500 level where finance approval starts (EXP-2).

**4. The emergency exception doesn't apply**
- Calling the trip "urgent" isn't enough (EMG-3, DEF-1). There are no facts showing an immediate operational or safety risk that can't wait for normal approval, so it isn't a qualifying emergency and the normal approvals apply (EMG-2).
- Because there's no emergency, the 24-hour post-purchase finance notice doesn't apply either (EMG-1, DEF-2).
- Even if it had qualified, the emergency exception only waives finance approval. It never waives manager or travel-office approval (EMG-1, EXP-3). The answer would be the same.

**5. Vendor status: not stated**
- Vendor restrictions always apply (EXP-3). If the airline or booking agent is a prohibited vendor, the purchase can't go ahead without specific written authorization from the compliance officer (VEN-1, VEN-2).

## R13 — answers H8

**Two advance approvals apply: manager approval and travel-office approval. Finance approval is not required.**

**1. Manager approval, before purchase**
- EXP-1 sets the manager-only tier for purchases of $2,500 or less made on or after July 1, 2025. AMD-2 makes the $2,500 threshold the current one, and an October 12, 2026 purchase falls under it.
- EXP-1 itself says "non-travel," but EXP-3 and TRV-2 apply the purchase threshold to airfare and all travel expenses too.
- $850 is well under $2,500, so EXP-2's finance tier does not apply. EXP-4 says thresholds use the total amount including taxes and fees, so I'm assuming $850 is the full total.

**2. Travel-office approval, before purchase**
- TRV-1 requires advance travel-office approval for airfare above $800, and $850 is above $800.
- Under TRV-2, travel-office approval is separate from manager approval. One does not replace the other.

**Why calling it "urgent" doesn't change this**
- Calling a request "urgent" doesn't make it an emergency (DEF-1, EMG-3). The employee gave no facts showing an immediate operational or safety risk that can't wait for normal approval. Under EMG-2, that means emergency status is not established, and the ordinary approvals above apply.
- Even if it were a qualifying emergency, the result would be the same. EMG-1 only waives advance finance approval, which isn't needed at this amount. It keeps manager approval and does not waive travel-office approval (EMG-1, EXP-3). Since the exception doesn't apply, the 24-hour finance notice (DEF-2) isn't required either.

**What the facts don't say**
- **Vendor:** The vendor isn't identified. If the airline or booking agent is a prohibited vendor, the purchase can't go ahead without specific written authorization from the compliance officer (VEN-1, VEN-2). Manager approval doesn't count as that authorization.
- **Timing:** All approvals must be obtained before the ticket is bought (DEF-2).

## R14 — answers H2

**Before buying:** manager approval and travel-office approval. **After buying:** notify finance within 24 hours. Advance finance approval is not required.

**Before the purchase (both approvals are needed):**

1. **Manager approval.** This is required because the emergency exception never waives manager approval (EMG-1, EMG-3, EXP-3). Airfare also falls under the normal purchase thresholds (EXP-3, TRV-2), and EXP-1 requires manager approval for $2,500 or less.
2. **Travel-office approval.** $801 is above the $800 airfare limit in TRV-1, and only amounts of $800 or less are exempt. EMG-1 says the emergency exception "does not waive any applicable travel-office approval." Travel-office approval also doesn't replace manager approval (TRV-2).

**Finance approval in advance is not required.** EMG-1 waives it for a qualifying emergency of $5,000 or less from an approved vendor. Even without the emergency, it wouldn't apply: the purchase is dated after July 1, 2025, so the $2,500 threshold applies (AMD-2, DEF-3), and $801 is below it (EXP-1, EXP-2).

**After the purchase:**

3. **Notify finance within 24 hours** (EMG-1). This is a notice after the purchase, not an approval (DEF-2).

**Not required:** written authorization from the compliance officer. The vendor is approved, not prohibited (VEN-1–VEN-3, EMG-2).

**Assumptions:**
- I treated "qualifying emergency" as a given fact. It counts only if the purchase addresses an immediate operational or safety risk that can't reasonably wait for normal approval (DEF-1). Calling it "urgent" is not enough (EMG-3).
- If it doesn't qualify, finance still needs no advance approval or notice, because $801 is under $2,500. Manager and travel-office approval are still required (EMG-2, EXP-1, TRV-1).
- The thresholds use the full $801, including taxes and fees (EXP-4).

## R15 — answers H7

Besides the compliance-officer authorization you already have, two things are required:

1. **Manager approval before the purchase is made.** No policy waives this (EXP-3, EMG-1, EMG-3).
2. **A notice to finance within 24 hours after the purchase** (EMG-1). This is only a notice, not an approval (DEF-2).

Advance finance approval is not needed, and travel-office approval doesn't apply.

**Why:**
- **Normal rule:** The purchase date is after July 1, 2025, so the $2,500 threshold applies (AMD-2). A routine $4,200 purchase would need both manager and finance approval in advance (EXP-2).
- **Emergency exception:** For a qualifying emergency of $5,000 or less, the emergency policy drops the advance finance approval (EMG-1). $4,200 is under that limit.
- **Prohibited vendor:** The exception normally covers only approved vendors. However, it does apply to a prohibited vendor that has specific written compliance-officer authorization (EMG-2, VEN-2). Your authorization explicitly covers this transaction, so it meets that requirement. It also satisfies the rule that a prohibited vendor can't be used without that authorization (VEN-1).
- **Travel office:** This isn't a travel purchase, so travel-office approval (TRV-1) doesn't apply.

**Caveats:**
- This assumes the purchase really meets the emergency definition: an immediate operational or safety risk that can't reasonably wait for normal approval (DEF-1). Calling it "urgent" isn't enough. If it doesn't qualify, finance approval is required in advance again (EMG-2, EXP-2).
- Manager or finance approval can never stand in for the compliance-officer authorization (VEN-2).

## R16 — answers H1

**Before the purchase:** you need manager approval, and nothing else.
**After the purchase:** finance must be notified within 24 hours.

**Why:**

1. **Manager approval is required beforehand.** The purchase date is after July 1, 2025, so the current $2,500 limit applies (AMD-2). An $800 purchase is under that limit, so it needs manager approval in advance (EXP-1). The emergency exception never removes manager approval: "Manager approval remains required before proceeding" (EMG-1; also EXP-3, EMG-3).

2. **Advance finance approval is not required.** This is a qualifying emergency purchase of $5,000 or less from an approved vendor, so EMG-1 waives advance finance approval. At $800 it wouldn't have been needed anyway, since finance approval only applies above $2,500 (EXP-2).

3. **Travel-office approval is not required.** That approval is only needed for airfare *above* $800. Amounts of $800 or less are explicitly exempt (TRV-1), and "or less" includes exactly $800 (EXP-4). EMG-1 says the emergency exception doesn't waive travel-office approval, but here it simply doesn't apply.

4. **Compliance-officer authorization is not required.** The vendor is approved, so the prohibited-vendor rules (VEN-1/VEN-2) don't come into play.

5. **Finance must be notified within 24 hours after the purchase.** This comes from the emergency exception (EMG-1). It's a notification after the fact, not an approval (DEF-2).

One caveat: all of this assumes the emergency actually meets the DEF-1 test, meaning an immediate operational or safety risk that can't wait for normal approval. Calling it "urgent" isn't enough (EMG-3). If the emergency doesn't qualify, the ordinary rules apply. You'd still need manager approval before buying, but the 24-hour finance notice would no longer be required by the emergency policy.

## R17 — answers H2

**Before proceeding:**
1. **Manager approval.** The purchase was on or after July 1, 2025 and is $2,500 or less, so manager approval is required (EXP-1, AMD-2). The emergency exception never waives it (EXP-3, EMG-1, EMG-3).
2. **Travel-office approval.** $801 is above the $800 airfare threshold, so travel-office approval is required in advance (TRV-1). The emergency exception says it does not waive this approval (EMG-1). Travel-office approval also doesn't replace manager approval (TRV-2).

**After proceeding:**
3. **Notify finance within 24 hours of the purchase.** This is a condition of the emergency exception (EMG-1). It is a notification only, not an approval (DEF-2).

**Not required:**
- **Advance finance approval.** It wouldn't be needed anyway, because $801 is below the $2,500 threshold (EXP-2). It would also be waived because this is a qualifying emergency of $5,000 or less from an approved vendor (EMG-1).
- **Compliance-officer authorization.** That only applies to prohibited vendors (VEN-1, VEN-2), and this vendor is approved.

**Note:** I've treated the emergency as qualifying because you said it was. If it doesn't meet DEF-1 (an immediate operational or safety risk that can't reasonably wait for normal approval), the emergency exception doesn't apply (EMG-2). Manager and travel-office approval would still be required in advance. The 24-hour finance notification would no longer be required because it comes from the emergency exception.

## R18 — answers H3

**No. The emergency exception does not apply, so advance finance approval is not waived.** The purchase needs **both manager approval and finance approval before it is made.**

**Why the exception doesn't apply**
- **EMG-1** waives advance finance approval only for a qualifying emergency purchase "totaling **$5,000 or less**" from an approved vendor.
- At $5,001, this purchase is $1 over that cap. It doesn't matter that the emergency qualifies under DEF-1 or that the vendor is approved (VEN-3). The amount alone rules out the exception.
- **EXP-4** says thresholds use the total transaction amount, including taxes and fees. I've assumed $5,001 is that all-in total. If $5,001 is the pre-tax price, the total is even higher, and the answer stays the same.

**Which approval threshold applies**
- The purchase date is October 12, 2026, which is after the July 1, 2025 effective date. That means the current $2,500 routine threshold applies (**AMD-2**, **DEF-3**), not the older $2,000 one (AMD-1).
- $5,001 is above $2,500, so **EXP-2** applies: **both manager and finance approval are required before purchase.** "Before" means before the purchase goes ahead (**DEF-2**).

**What is not required**
- **Travel-office approval:** not needed, because this isn't a travel purchase (TRV-1).
- **Compliance-officer authorization:** not needed, because the vendor is approved, not prohibited (VEN-1, VEN-2).
- **24-hour finance notification:** this rule in EMG-1 only exists as part of the emergency exception. Since the exception doesn't apply, the notice doesn't replace finance approval. Finance has to approve beforehand.

Manager approval would have been needed in advance either way. Even when the exception applies, it never waives manager approval (EXP-3, EMG-1, EMG-3).

## R19 — answers H7

## Answer

Besides the compliance-officer authorization you already have, the purchase needs two things:

1. **Manager approval before the purchase.** The emergency exception never waives this (EMG-1, EMG-3, EXP-3).
2. **Notify finance within 24 hours after the purchase.** This is a notice after the fact, not an approval (EMG-1, DEF-2).

**Advance finance approval is not required.** The emergency exception waives it.

No travel-office approval is needed because this isn't a travel purchase (TRV-1).

## Why

- **Normal rule:** The purchase is dated October 12, 2026, so the current $2,500 limit applies (AMD-2). At $4,200, a routine purchase would need both manager and finance approval in advance (EXP-2).
- **Emergency exception:** For a qualifying emergency of $5,000 or less, advance finance approval is waived (EMG-1). That exception normally covers only approved vendors. However, EMG-2 lets it apply to a prohibited vendor when there is written compliance-officer authorization under VEN-2. A specific written authorization covering this transaction meets that condition (VEN-2).
- **Vendor rule still applies:** The written authorization must exist before the purchase goes ahead (VEN-1). Manager approval can't replace it, and neither can finance approval (VEN-2).

## Caveats

- **Short guide is incomplete:** `SUMMARY.md` leaves out the requirement to notify finance within 24 hours. The full policy text controls where they differ (DEF-3).
- **The emergency must truly qualify:** It has to involve an immediate operational or safety risk that can't wait for normal approval. Calling it "urgent" is not enough (DEF-1, EMG-3). If it doesn't qualify, the normal rule applies: manager plus advance finance approval, as well as the compliance authorization.

## R20 — answers H2

Under the primary policy text in `reference/`, two approvals are needed before the purchase and one notification after it.

**Before the purchase:**
1. **Manager approval.** Still required even in a qualifying emergency (`reference/03-emergency-policy.md:4` EMG-1, `reference/03-emergency-policy.md:10` EMG-3, `reference/01-expense-policy.md:11` EXP-3).
2. **Travel-office approval.** $801 is above the $800 airfare limit, so this approval is required (`reference/02-travel-policy.md:4` TRV-1). The emergency exception does not waive it (EMG-1: "does not waive any applicable travel-office approval"). It also doesn't replace manager approval (TRV-2).

**Waived:**
- **Finance approval before the purchase.** The emergency exception applies because the purchase is a qualifying emergency, from an approved vendor, and $5,000 or less (EMG-1). Without the emergency, finance approval still wouldn't apply, because $801 is under the $2,500 routine limit in effect since July 1, 2025 (EXP-1, AMD-2).

**After the purchase:**
- **Tell finance within 24 hours.** This is a notification, not an approval (EMG-1; `reference/06-definitions.md:7` DEF-2).

**Not needed:**
- **Compliance-officer authorization.** The vendor is approved, not prohibited (VEN-1, VEN-3).

`SUMMARY.md` leaves out two of these points: the 24-hour finance notification, and the fact that the emergency exception doesn't waive travel-office approval. The primary policy controls where the two differ (DEF-3).

This all assumes the facts really meet the definition of a qualifying emergency: an immediate operational or safety risk that can't wait for normal approval (DEF-1). Calling a purchase "urgent" isn't enough (EMG-3). If it doesn't qualify, the result is the same here, except that finance doesn't need to be notified within 24 hours.

## R21 — answers H4

**You need both manager approval and finance approval, and both must be in place before the purchase goes ahead.**

1. **The threshold applies to the full amount.** Taxes and fees count toward it (EXP-4), so the total is $2,480 + $35 = **$2,515**.
2. **The $2,500 limit applies to this date.** The routine limit rose from $2,000 to $2,500 on July 1, 2025 (AMD-2), and the amendment rules decide which limit applies (DEF-3). October 12, 2026 is after that change.
3. **$2,515 is over the limit.** A routine non-travel purchase above $2,500 needs **both manager and finance approval before purchase** (EXP-2). The manager-only rule covers $2,500 or less (EXP-1), so it doesn't apply here. The subtotal of $2,480 is under the limit, but the subtotal isn't what counts.

**Other policies that don't change the answer:**
- **Travel policy:** This isn't a travel or airfare purchase, so travel-office approval isn't needed (TRV-1).
- **Emergency policy:** The transaction is described as routine, so nothing shows it's a qualifying emergency. Advance finance approval is still required (EMG-2, DEF-1).
- **Vendor policy:** The vendor's status isn't stated. If the vendor turns out to be prohibited, you would also need **specific written authorization from the compliance officer** before proceeding. Manager or finance approval can't stand in for it (VEN-1, VEN-2).

## R22 — answers H8

Two approvals apply, and both must be obtained before the ticket is bought:

1. **Manager approval.** The policy for ordinary purchases (EXP-1) covers non-travel purchases, but airfare is pulled back under the same dollar limits by two other rules (EXP-3 and TRV-2). The purchase date is October 12, 2026, which is after the July 1, 2025 change, so the current $2,500 limit applies (AMD-2, DEF-3). $850 is under that limit, so only the manager is needed at this level, not finance.
2. **Travel-office approval in advance.** Airfare over $800 needs it, and $850 is over that line (TRV-1). This approval adds to the manager's; it doesn't replace it (TRV-2).

**The emergency exception doesn't apply.** Calling the trip "urgent" isn't enough. The definition of an emergency (DEF-1) requires an immediate operational or safety risk that can't reasonably wait for normal approval, and the employee hasn't described one. Without those facts, emergency status isn't established and the normal approvals stay in place (EMG-2, EMG-3). Even a real emergency would only waive advance finance approval, which isn't needed here anyway. It never waives manager approval or travel-office approval (EMG-1, EXP-3).

**Finance:** no approval is needed because $850 is under $2,500. The rule about notifying finance within 24 hours applies only to qualifying emergencies, so it doesn't come into play.

**Vendor:** the facts don't say which vendor is involved. If it's a prohibited vendor, the purchase also needs written authorization from the compliance officer (VEN-1, VEN-2).

## R23 — answers H3

**No. The emergency exception doesn't apply because $5,001 is over its $5,000 cap. Both manager approval and finance approval are required before the purchase.**

**Why the exception doesn't apply**
- EMG-1 (`03-emergency-policy.md:4`) waives advance finance approval only for a qualifying emergency purchase "totaling **$5,000 or less**" from an approved vendor.
- Under EXP-4 (`01-expense-policy.md:14`), thresholds use the full transaction amount, including taxes and fees, and "or less" is inclusive. $5,001 is above the cap, so the waiver isn't available even though the emergency qualifies and the vendor is approved.

**Which rules apply instead**
- The purchase date is October 12, 2026, which is after the July 1, 2025 amendment. So the current $2,500 routine threshold applies (AMD-2, `05-policy-amendments.md:7`), not the old $2,000 one.
- $5,001 is above $2,500, so EXP-2 (`01-expense-policy.md:8`) requires both manager and finance approval before purchase.

**Required approvals**
1. **Manager approval before purchase.** Even an emergency never waives this (EXP-3, EMG-3).
2. **Finance approval before purchase.** Under DEF-2, "advance" means before the transaction proceeds.

**Not required**
- **The 24-hour notice to finance.** This is part of the EMG-1 exception, which doesn't apply. It's a post-purchase notice, not an approval, so it couldn't replace advance finance approval anyway (DEF-2).
- **Travel-office approval.** This isn't a travel purchase.
- **Compliance-officer authorization.** The vendor is approved, not prohibited.

If the total were $5,000 or less, advance finance approval would be waived. Manager approval would still be needed before purchase, and finance would have to be notified within 24 hours afterward.

## R24 — answers H6

**No. The 24-hour finance notification requirement was not met.** Everything else was satisfied, assuming the manager approved before the purchase.

| Requirement | Source | Met? |
|---|---|---|
| A qualifying emergency | EMG-1, DEF-1 | ✅ The question says it qualifies. |
| Total of $5,000 or less | EMG-1, EXP-4 | ✅ $4,000 is under the limit, assuming it includes taxes and fees. |
| Approved vendor | EMG-1, VEN-3 | ✅ Yes, so the prohibited-vendor rules don't apply. |
| Advance finance approval | EXP-2, EXP-3, EMG-1 | ✅ Waived. $4,000 is above the $2,500 limit, so this would normally be required, but the emergency exception removes it. |
| Manager approval before purchase | EMG-1, EXP-3, EMG-3 | ✅ The manager approved. The emergency never waives this. |
| Finance notified within 24 hours after purchase | EMG-1, DEF-2 | ❌ Finance was told after 30 hours, 6 hours late. |
| Travel-office approval | TRV-1 | Not needed, because this isn't a travel purchase. |

**Why the waiver doesn't cover the late notice:** The emergency exception only waives finance approval *before* the purchase. It doesn't remove the duty to tell finance within 24 hours *after* it. DEF-2 treats these as separate requirements. Having no advance finance approval was allowed; telling finance after 30 hours was not.

**One assumption:** The question says the manager approved but not when. EMG-1 requires manager approval "before proceeding." If the manager approved only after the purchase, that's a second violation.

The short guide (SUMMARY.md) leaves out the 24-hour notice rule. Read on its own, it would suggest the purchase was fully compliant. The full policies take precedence over the summary (DEF-3), and they include the notice rule.
