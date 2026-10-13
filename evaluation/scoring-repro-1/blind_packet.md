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

# RESPONSES TO SCORE (shuffled; arm identity withheld)

## R01 — answers Q5

I can't tell you which approvals are needed, because the Meridian Works policy isn't available to me. Your working directory is empty, and a search for "Meridian" found nothing. I don't have the policy from any other source, and I won't guess at approval thresholds.

If you share the travel or expense policy (paste it in or put the file in the working directory), I'll answer from its actual text. These are the parts I'd check for a $900 routine airfare purchased on October 12, 2026:

- **Effective dates and versions:** whether a policy version or amendment in effect on that date changed the thresholds.
- **Approval tiers by dollar amount:** for example, manager approval above one amount and director or finance approval above another.
- **Airfare-specific rules:** pre-trip authorization, use of a designated booking tool or agency, and fare class limits.
- **What "routine" means in the policy:** whether routine purchases follow a lighter approval path than non-routine ones.

## R02 — answers Q3

I can't answer this yet because I don't have the Meridian Works policy. The working directory (`A_REPRO_1-Q3`) is empty. I tried to search the parent scratchpad folder for it, but that needs a read permission that hasn't been granted. Meridian Works' internal policy isn't something I know on my own, so if I listed approvers, dollar thresholds or notification deadlines, I'd be making them up.

To get you an answer, I need one of these:
- **Paste the relevant policy sections** (purchasing/procurement approval thresholds, the emergency or urgent purchase exception, approved-vendor rules, and any notification or after-the-fact documentation requirements), or
- **Give me the file path** of the policy document, or allow access to the parent scratchpad folder if it's there.

Once I have the text, I'll work through your facts:
- **Amount:** a $4,000 non-travel purchase, and which approval tier that falls into.
- **Emergency exception:** whether an immediate operational risk that can't wait for normal approval qualifies, and who can authorize the purchase under it.
- **Approved vendor:** whether buying from an approved vendor waives or changes any requirement, such as competitive quotes.
- **Notifications:** who must be told after the fact, and the deadline. The purchase was on October 12, 2026 and today is October 13, so I'll also check whether any notification window is already running or has closed.

## R03 — answers Q8

**No. The employee may not go ahead under the emergency exception alone.** The exception removes only the need for advance finance approval. Manager approval is still required before the purchase, so without it the purchase cannot proceed.

**Steps applied:**

1. **Date and threshold.** October 12, 2026 is after July 1, 2025, so the current $2,500 routine threshold applies (AMD-2, DEF-3). $4,000 is above it, so ordinarily the purchase would need both manager and finance approval before purchase (EXP-2, EXP-4).
2. **Emergency exception (EMG-1).** All of its conditions are met:
   - The facts state the purchase is a qualifying emergency (DEF-1).
   - $4,000 is within the $5,000 cap. The cap is inclusive under EXP-4.
   - The vendor is approved (VEN-3).
   
   So **advance finance approval is waived**. But EMG-1 says outright that "Manager approval remains required before proceeding."
3. **No provision removes the manager.** EXP-3 says the Emergency Policy "may waive advance finance approval, but not manager approval." EMG-3 says "An emergency does not waive manager approval." Nothing in the policies names a substitute approver or excuses the requirement when the manager can't be reached. A provision waives only what it expressly names, so the requirement stands.
4. **Vendor.** The vendor is approved, so the vendor restrictions don't block the purchase (VEN-1, EMG-2).

**If manager approval is obtained, the requirements are:**

| Requirement | Timing | Source |
|---|---|---|
| Manager approval | Before purchase | EMG-1, EXP-3, EMG-3 |
| Finance approval | Waived | EMG-1 |
| Notify finance | Within 24 hours after purchase. This is a notice, not an approval. | EMG-1, DEF-2 |

Until the manager approves, the employee must not proceed.

## R04 — answers Q3

## The answer

You need **manager approval before the purchase**, and you must **notify finance within 24 hours after the purchase**. Advance finance approval is waived. Nothing else applies.

## How the rules apply

1. **Date (AMD-1, AMD-2, DEF-3):** October 12, 2026 is after July 1, 2025, so the current $2,500 routine limit applies, not the older $2,000 one.
2. **Normal rule (EXP-2, EXP-4):** $4,000 is over $2,500. Without an emergency, this purchase would need both manager and finance approval before buying. The $4,000 must be the total, including taxes and fees.
3. **Does it count as an emergency? (DEF-1, EMG-2, EMG-3):** Yes. The facts describe an immediate operational risk that can't reasonably wait for normal approval, which matches DEF-1's wording. This isn't just a request labelled "urgent."
4. **Emergency exception (EMG-1):** It applies because the purchase is a qualifying emergency, it is $5,000 or less, and the vendor is approved. Under EMG-1:
   - Advance finance approval is **waived**.
   - **Manager approval is still required before proceeding.** EXP-3 and EMG-3 both say an emergency never waives manager approval.
   - Finance must be **notified within 24 hours after purchase**.
5. **Vendor (VEN-1, VEN-3):** The vendor is approved, so no compliance-officer authorization is needed.

## Not affected

- **Travel-office approval (TRV-1/TRV-2):** Doesn't apply, because this isn't a travel purchase.
- **Finance notice vs. approval (DEF-2):** The 24-hour notice is only a notification after the purchase. It doesn't mean finance has to approve it.

## Two cautions

- If the total including taxes and fees goes over $5,000, the emergency exception no longer applies. You would then need both manager and finance approval before buying (EXP-2).
- Today is October 13. If the purchase was made on October 12, the 24-hour window to notify finance may close today, depending on the time of purchase.

## R05 — answers Q6

**Answer: you needed both manager approval and finance approval.**

**Why**
- **The date decides the threshold.** The purchase was on June 15, 2025, before the July 1, 2025 change. The new $2,500 limit doesn't apply to earlier purchases (AMD-2, DEF-3).
- **The rule in force then:** before July 1, 2025, routine purchases of $2,000 or less needed only manager approval. Anything above $2,000 needed both manager and finance approval (AMD-1).
- **The amount is over that limit:** $2,300 is more than $2,000, so both approvals applied. Thresholds are measured on the total amount including taxes and fees (EXP-4).
- **The current rule doesn't apply.** Under today's EXP-1, $2,300 would need manager approval only. But EXP-1 covers only purchases made on or after July 1, 2025, so it doesn't reach this one.

**Timing:** AMD-1 says both approvals were "required" but doesn't say whether they had to come before the purchase. The current rules (EXP-1/EXP-2) do say "before purchase," but they only cover purchases from July 1, 2025 onward. Applying the current timing rule to this purchase is a reasonable assumption, not something AMD-1 states.

**Exceptions that don't apply**
- **Emergency waiver (EMG-1):** Nothing in the facts says this was an emergency, so the finance-approval waiver doesn't apply (EMG-2, DEF-1). Even in an emergency, manager approval would still be required.
- **Travel policy:** This was a non-travel purchase, so the travel rules don't apply.
- **Vendor rules (VEN-1):** The facts don't say who the vendor was. If it was a prohibited vendor, the purchase would also have needed written authorization from the compliance officer (VEN-1, VEN-2). Manager or finance approval doesn't count as that authorization.

## R06 — answers Q5

**You need two approvals, and both must be in place before the purchase:**

1. **Manager approval**, before purchase (EXP-1).
2. **Travel-office approval**, in advance (TRV-1).

Finance approval is not required, and nothing needs to be reported afterwards.

**Why**

- **Date:** The purchase is on October 12, 2026, which is after July 1, 2025. That means the current routine limit of $2,500 applies, not the older $2,000 limit (AMD-2, AMD-1, DEF-3).
- **Amount:** $900 total, including taxes and fees, is within the $2,500 limit. So only manager approval is needed under the spending rules, not finance approval (EXP-1, EXP-2, EXP-4).
- **Airfare:** Airfare over $800 needs travel-office approval beforehand, on top of the normal spending approval. $900 is over $800, so it applies (TRV-1, EXP-3). Travel-office approval doesn't replace manager approval (TRV-2).

**Exceptions**

- **Emergency exception (EMG-1):** Doesn't apply. The purchase is described as routine, so it isn't an emergency (DEF-1, EMG-2). Even in an emergency, this exception would only remove the need for finance approval. It would never remove manager or travel-office approval.
- **Vendor rules:** You didn't say whether the vendor is approved or banned. If it's a banned vendor, the purchase can't go ahead without a specific written approval from the compliance officer. Manager or travel-office approval can't stand in for it (VEN-1, VEN-2). If the vendor isn't banned, the two approvals above are all you need.

## R07 — answers Q1

**Only manager approval is required, and it must be obtained before the purchase.** Finance approval is not required.

**How I got there**

1. **Date first:** The purchase is dated October 12, 2026, which is after July 1, 2025. That means the current $2,500 routine threshold applies, not the older $2,000 limit. The amendment does not apply backwards. (AMD-1, AMD-2, DEF-3)
2. **Tier:** $2,400 is at or below $2,500, so it falls in the ordinary tier. That tier requires manager approval before purchase. (EXP-1)
   - Thresholds are measured on the total transaction amount, including taxes and fees. If $2,400 is the full total, this tier applies. If taxes or fees would push the total above $2,500, the purchase moves to EXP-2, which requires both manager and finance approval before purchase. (EXP-4, EXP-2)
   - Under the old pre-July 2025 limit, this purchase would have needed finance approval too. Because of the date, it doesn't.
3. **Other features checked:**
   - **Travel:** This isn't a travel or airfare purchase, so no travel-office approval is needed. (TRV-1)
   - **Emergency:** No emergency is claimed. The emergency exception would only waive advance finance approval anyway, and finance approval isn't required here. Manager approval can never be waived. (EXP-3, EMG-1, EMG-3)
   - **Notifications:** No notification requirement applies. The rule to notify finance within 24 hours only applies to emergency purchases. (EMG-1, DEF-2)
   - **Vendor:** The facts don't say whether the vendor is approved or prohibited. If it is prohibited, the purchase cannot go ahead without a specific written authorization from the compliance officer. That authorization would be needed in addition to manager approval, and manager approval cannot stand in for it. (VEN-1, VEN-2, EXP-3)

**Citations:** EXP-1, EXP-2, EXP-3, EXP-4, AMD-1, AMD-2, DEF-2, DEF-3, TRV-1, EMG-1, EMG-3, VEN-1, VEN-2.

## R08 — answers Q1

I can't answer this from the Meridian Works policy because I don't have a copy of it.

- **The working directory is empty.** It contains no policy documents.
- **The parent scratchpad folder is off-limits.** I tried to search it for "Meridian", but the permission request was declined, so I didn't look there.

I don't know Meridian Works' approval thresholds, so I won't guess. Any answer about who must sign off at $2,400 would be made up.

To get an answer, do one of these:
1. Paste the relevant policy section (purchase or expense approvals) here.
2. Put the policy file in the working directory, or give me its path and allow read access.

Once I have the text, I'll check the $2,400 amount and the October 12, 2026 date against it. That includes any thresholds, rules for routine vs. non-routine or travel vs. non-travel purchases, and any policy versions or effective dates that change the rules around that date.

## R09 — answers Q7

I couldn't find Meridian Works' policy, so I can't give you a reliable answer.

**What I checked:**
- The working directory (`...\repro-sessions\A_REPRO_1-Q7`) is empty. It has no policy, handbook or other files.
- I tried to search the parent scratchpad folder for "Meridian", but the permission prompt was declined, so I didn't look there.

**Why I'm not answering from general knowledge:** your question depends on Meridian Works' own rules. That means how its emergency exception defines "emergency," what proof it requires, the approval thresholds that apply to a $4,000 non-travel purchase, and any rules tied to dates (such as a policy effective date, or quarter-end or fiscal-year rules near October 12, 2026). These differ from one organization to the next, so any thresholds or approvers I named would be made up.

**What I can say from your facts alone:** emergency exceptions usually require an immediate operational or safety risk, not just a label of "urgent." If Meridian's policy works that way, a request with no evidence of that risk probably wouldn't qualify, and the normal approval process for a $4,000 purchase would apply. I can't confirm that or name the specific approvals without the text.

**To get a proper answer, either:**
1. Put the policy file(s) in the working directory, or paste the relevant sections here, or
2. Approve read access to the parent scratchpad folder if the policy is there, and I'll search it.

Once I have the text, I'll point to the exact provisions that apply, including any effective-date or version issues for the October 12, 2026 date.

## R10 — answers Q2

I can't answer this from Meridian Works policy, because no policy is available here. The working directory (`...\repro-sessions\A_REPRO_1-Q2`) is empty, and searching it for "Meridian" found nothing. I also have no outside knowledge of Meridian Works' internal approval rules.

I won't guess at the approvals. The answer depends on details only the policy has:

- **Dollar thresholds:** which approval tier a $2,600 purchase falls into, for example manager only versus manager plus Finance.
- **Effective dates:** whether a version of the policy in effect on October 12, 2026 changed the thresholds or approvers.
- **Category rules:** any separate approval path for equipment or IT purchases, as opposed to travel or other spending.
- **Extra conditions:** things like a competitive quote requirement, budget-holder sign-off, or a pre-approval deadline.

If you put the policy document (or the procurement and approval sections) in this folder or paste it here, I'll tell you exactly which approvals this purchase needs and cite the sections.

## R11 — answers Q8

I couldn't find any Meridian Works policy, so I can't answer this yet. The working directory is empty, and I don't know of a public "Meridian Works" policy to rely on.

Whether an emergency can override the manager-approval requirement depends on the policy's exact wording. Some things that would change the answer:

- **How the emergency exception is written.** It might fully replace the approval requirement. Or it might only change the timing, so approval can come after the purchase.
- **Dollar limits.** The exception might only apply up to a cap, and $4,000 could be over it. There might also be a separate limit for non-travel purchases.
- **Other approvers.** The policy might name someone else, such as a skip-level manager or someone in finance, when the manager can't be reached.
- **Dates.** A version of the policy or an amendment could take effect around October 12, 2026.
- **Paperwork afterward.** The policy might require written documentation or a report within a set time.

If you share the policy, by pasting it or putting it in the working directory, I'll go through the relevant sections and give you a reasoned answer with citations.

## R12 — answers Q6

I couldn't answer this from your files because the working directory (`A_REPRO_1-Q6`) is empty. I found no policy documents, amendments or other files there to look up Meridian Works' purchase approval rules.

I also don't have reliable outside knowledge of Meridian Works' internal policies, so any approval thresholds I gave you would be made up.

To answer it, I need the policy text in effect on June 15, 2025. That means the base purchasing or approval policy plus any amendments, memos or revision history from around that date, since thresholds often change mid-year. You can either put those files in this directory or tell me where they are, and I'll work out which approvals a routine, non-travel $2,300 purchase needed on that date.

## R13 — answers Q4

**No, the purchase may not go ahead.** Under VEN-1, a purchase from a prohibited vendor "must not proceed" without written authorization from the compliance officer. You've told me there is no such authorization, so the purchase is barred.

One note first: Q3's facts aren't in this folder or this session, so I don't have its amount, date or emergency details. That doesn't change the answer, because the vendor bar applies whatever those facts are.

**Why no other approval or exception gets around it**

- **The vendor rule is checked on its own.** EXP-3 says "Vendor restrictions always apply."
- **The emergency exception doesn't help.** Even if Q3 involved a qualifying emergency under DEF-1, EMG-2 says the exception "does not apply to a prohibited vendor unless the vendor has received written compliance-officer authorization under VEN-2." VEN-1 adds that "Emergency status alone does not change this prohibition," and EMG-3 says an emergency does not waive vendor restrictions.
- **Manager or finance approval can't stand in for the authorization.** VEN-2 says no compliance-officer authorization "may be inferred from manager or finance approval." Having every purchase-tier approval under EXP-1 or EXP-2 still leaves the purchase barred.
- **Travel-office approval can't either.** If the purchase is airfare, TRV-2 limits travel-office approval to its own role, and nothing in TRV-1 or TRV-2 lifts a vendor restriction.
- **The transaction date doesn't matter here.** AMD-3 says the threshold change affects only the routine purchasing threshold, not the Vendor Policy. The ban applies on either side of July 1, 2025.

**What would let it go ahead**

The only route is a specific written authorization from the compliance officer for this transaction (VEN-2). That would add to the normal approvals, not replace them:
- **Purchase-tier approval before purchase:** EXP-1 or EXP-2 based on amount and date, or AMD-1 if the purchase is dated before July 1, 2025.
- **If it qualifies as an emergency** under DEF-1 and totals $5,000 or less, EMG-1 would waive advance finance approval. Manager approval would still be required before purchase, and finance would have to be notified within 24 hours after the purchase (DEF-2).
- **If it is airfare over $800,** travel-office approval would also be required in advance (TRV-1).

Which of these apply depends on Q3's facts. If you send them, I can set out the exact approvals that would be needed once authorization is obtained.

## R14 — answers Q2

**You need both manager approval and finance approval, and both must be in place before the purchase.**

**How I got there**

1. **Which limit applies.** The purchase date is October 12, 2026. That is after July 1, 2025, so the current $2,500 routine limit applies, not the older $2,000 one (AMD-2, AMD-1, DEF-3). The change only affected the routine limit (AMD-3).
2. **Comparing the amount.** Limits are measured on the total transaction amount, including taxes and fees (EXP-4). $2,600 is over $2,500, so the higher-value rule applies: both manager and finance approval before purchase (EXP-2). The lower tier, manager approval alone, covers only purchases of $2,500 or less (EXP-1).

**Exceptions that don't apply**

- **Travel:** This is a non-travel equipment purchase, so travel-office approval isn't needed (EXP-3).
- **Emergency:** You described the purchase as routine, and nothing in the facts shows an immediate operational or safety risk that can't wait for normal approval. The emergency waiver of advance finance approval therefore doesn't apply (DEF-1, EMG-2, EMG-3). Even if it did, it would only waive finance approval. Manager approval would still be needed (EXP-3, EMG-1).

**Missing facts**

- **Vendor status:** You didn't say whether the vendor is approved or prohibited. Vendor rules apply regardless of anything else (EXP-3). If the vendor is prohibited, the purchase can't go ahead without a specific written authorization from the compliance officer. Manager or finance approval doesn't replace that authorization (VEN-1, VEN-2). If the vendor isn't prohibited, no extra vendor step applies.
- **Total amount:** I've assumed $2,600 is the total including taxes and fees. If the total is higher, the result is the same, since it's still over $2,500.

**Notifications:** None are required. The 24-hour finance notification only applies to qualifying emergency purchases (EMG-1, DEF-2).

## R15 — answers Q4

I can't answer this reliably yet, because I don't have the Meridian Works policy or the Q3 facts.

- **The working directory is empty.** There's no policy document, prior question, or fact pattern in it.
- **I couldn't look anywhere else.** My attempts to read the parent `repro-sessions` folder and the wider `ICM-COP-14-Astra` folder were blocked because those locations haven't been granted read permission.
- **This session has no record of Q3.** I can't see what the original facts were (the amount, the approval thresholds, who signed off, and so on).

I could guess how a typical procurement policy treats a prohibited vendor, but that would be making up Meridian Works' rules. That's not a sound basis for a policy answer.

To answer it, I need one of these:
1. **The text**: paste the relevant Meridian Works policy sections, especially any on prohibited or restricted vendors, compliance-officer authorization and exceptions, plus the Q3 fact pattern.
2. **Access**: grant read access to the folder that holds them, or tell me the path, and I'll find and cite the provisions myself.

Once I have them, I'll say whether the purchase may proceed and point to the exact provisions. In particular, I'll check whether the policy has any exception route for prohibited vendors and whether that route requires the written compliance-officer authorization that's missing here.

## R16 — answers Q7

**No, the emergency exception does not apply.** On these facts the $4,000 purchase needs both manager approval and finance approval, and both must be obtained before the purchase.

**1. Date and threshold.** The purchase is on October 12, 2026, which is after July 1, 2025. So the current $2,500 routine threshold applies, not the old $2,000 limit (AMD-1, AMD-2, DEF-3). The amendment changes only that threshold (AMD-3).

**2. Approval tier.** The threshold is measured on the total amount, including taxes and fees (EXP-4). $4,000 is above $2,500, so it falls under EXP-2: **manager approval and finance approval, both before purchase**.

**3. Emergency claim: not established.**
- A qualifying emergency means an immediate operational or safety risk that cannot reasonably wait for normal approval. Calling a request "urgent" is not enough (DEF-1, EMG-3).
- Without evidence meeting DEF-1, emergency status is not established and the ordinary approvals still apply (EMG-2).
- So the EMG-1 waiver of advance finance approval doesn't apply. That's true even though $4,000 is under the $5,000 emergency cap.
- The only thing EMG-1 would replace is advance finance approval, which would become a finance notification within 24 hours after purchase. That route isn't available here (EMG-1, DEF-2).
- Even a valid emergency would never waive manager approval (EXP-3, EMG-1, EMG-3).

**4. Travel.** This is not a travel or airfare purchase, so no travel-office approval is needed (TRV-1 doesn't apply).

**5. Vendor status: not given.** Vendor restrictions apply separately from every other rule (EXP-3, VEN-1):
- **Approved or non-prohibited vendor:** the result above stands.
- **Prohibited vendor:** the purchase must not go ahead without a specific written authorization from the compliance officer, on top of the manager and finance approvals. Manager or finance approval can't stand in for that authorization (VEN-1, VEN-2).

**What would change the answer:** facts showing an immediate operational or safety risk that can't wait for normal approval, plus an approved vendor. Then advance finance approval would be waived, but manager approval before purchase would still be needed and finance would have to be notified within 24 hours (EMG-1, DEF-1).

**On the facts supplied:** get manager approval and finance approval before purchase (EXP-2, AMD-2, EXP-4, EMG-2, EMG-3, DEF-1). If the vendor is prohibited, also get written compliance-officer authorization (VEN-1, VEN-2).
