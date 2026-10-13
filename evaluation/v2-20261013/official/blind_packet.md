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

# QUESTIONS (corrected v2; Q4 is self-contained)

**Q1.** Under Meridian Works policy, an employee requests a routine, non-travel equipment purchase of $2,400 on October 12, 2026. What approvals are required before proceeding?

**Q2.** Under Meridian Works policy, an employee requests a routine, non-travel equipment purchase of $2,600 on October 12, 2026. What approvals are required before proceeding?

**Q3.** Under Meridian Works policy, an immediate operational risk that cannot reasonably await normal approval requires a $4,000 non-travel purchase on October 12, 2026, from an approved vendor. What approvals and notifications are required?

**Q4.** Under Meridian Works policy, an immediate operational risk that cannot reasonably await normal approval requires a $4,000 non-travel purchase on October 12, 2026, from a prohibited vendor, and there is no written compliance-officer authorization. May the purchase proceed? Explain.

**Q5.** An employee plans a routine $900 airfare purchase on October 12, 2026, under Meridian Works policy. What approvals are required before the purchase?

**Q6.** Under Meridian Works policy, what approvals were required for a routine, non-travel $2,300 purchase on June 15, 2025?

**Q7.** An employee requests a $4,000 non-travel purchase on October 12, 2026, calling it 'urgent' but providing no evidence of immediate operational or safety risk. Can the employee use Meridian Works' emergency exception, and what approval requirements apply on the supplied facts?

**Q8.** Under Meridian Works policy, a $4,000 non-travel purchase on October 12, 2026, qualifies as an emergency and uses an approved vendor, but the employee cannot obtain manager approval. May the employee proceed solely under the emergency exception? Explain.

# RESPONSES TO SCORE (shuffled; arm identity withheld; directory paths stripped)

## R01 — answers Q8

**No.** The employee may not go ahead under the emergency exception alone. The exception removes only the need for advance finance approval. Manager approval is still required before the purchase.

**How the rules apply**

1. **Which threshold applies.** The purchase is dated October 12, 2026, which is after the July 1, 2025 amendment, so the $2,500 threshold applies (AMD-2, DEF-3). At $4,000, a routine purchase would need both manager and finance approval in advance (EXP-2).

2. **The emergency exception applies.** EMG-1 covers a qualifying emergency of $5,000 or less from an approved vendor. This purchase meets all three conditions: it is a qualifying emergency (as given), it is $4,000, and the vendor is approved. Advance finance approval is therefore waived.

3. **Manager approval is not waived.** Three provisions say so:
   - **EMG-1:** "Manager approval remains required before proceeding."
   - **EMG-3:** "An emergency does not waive manager approval."
   - **EXP-3:** The Emergency Policy "may waive advance finance approval, but not manager approval."

   "Advance" means before the transaction proceeds (DEF-2). The manager must therefore approve before the purchase, not afterward. No provision lets someone else approve in the manager's place or lets approval be given later.

4. **Finance notification is a separate step.** If the purchase does go ahead with manager approval, finance must be notified within 24 hours afterward (EMG-1). That notice is not the same as finance approval (DEF-2), and it does not replace the missing manager approval.

5. **Rules that don't come into play.** Travel-office approval isn't relevant because this is not a travel purchase. Vendor restrictions aren't a barrier because the vendor is approved.

**Conclusion:** The employee does not need advance finance approval but must get manager approval before buying. Without it, the purchase cannot proceed under the emergency exception or any other provision in these documents.

## R02 — answers Q2

**You need two approvals before buying: manager approval and finance approval.** Both must be in place before the purchase goes ahead.

**How I got there**

1. **The date sets the threshold.** October 12, 2026 is after July 1, 2025, so the current $2,500 routine threshold applies, not the older $2,000 one. The new limit doesn't apply to purchases before that date (AMD-2, AMD-1, DEF-3).
2. **The amount is over the threshold.** $2,600 is above $2,500, so the higher-value tier applies. That tier needs both manager and finance approval before purchase (EXP-2). The lower tier, which needs only manager approval, covers $2,500 or less (EXP-1).
3. **What the amount includes.** Thresholds are measured on the full transaction amount in US dollars, including taxes and fees (EXP-4). I've assumed $2,600 is that full amount. If $2,600 is before tax or fees, the total is higher, and you still land in the same tier.

**Exceptions that don't apply**

- **Travel:** This is a non-travel purchase, so travel-office approval isn't needed (TRV-1).
- **Emergency:** Nothing in the facts shows an immediate operational or safety risk that can't wait for normal approval, so the emergency exception isn't established. Even if it applied, it would only remove the need for *advance* finance approval. Manager approval would still be needed, and finance would have to be told within 24 hours after the purchase (DEF-1, EMG-1, EMG-2, EXP-3).

**One fact is missing: the vendor**

The facts don't say whether the vendor is approved or prohibited. If it's prohibited, the purchase can't go ahead without a specific written authorization from the compliance officer. That authorization is needed on top of the manager and finance approvals. Those approvals can't stand in for it, and it can't stand in for them (VEN-1, VEN-2, EXP-3).

No other approvals or notifications are needed.

## R03 — answers Q1

**Only manager approval is needed, and it must be given before the purchase.**

Why:

1. **The current threshold applies.** The purchase date, October 12, 2026, is after July 1, 2025, so the $2,500 limit applies (AMD-2, DEF-3). The older $2,000 limit in AMD-1 covered only purchases before that date. Under it, this purchase would also have needed finance approval.
2. **The amount is under the limit.** $2,400 is at or below $2,500, so EXP-1 applies: manager approval before purchase. EXP-2, which adds finance approval above $2,500, does not apply. Note that the limit counts the total including taxes and fees (EXP-4). If those push the total above $2,500, finance approval is also required.
3. **No other policies are triggered:**
   - **Travel:** this isn't a travel purchase, so travel-office approval (TRV-1) doesn't apply.
   - **Emergency:** it's described as routine, so the Emergency Policy isn't relevant. It couldn't waive manager approval anyway (EMG-1, EMG-3).
4. **One caveat on the vendor:** the request doesn't say who the vendor is. Vendor restrictions always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without a specific written authorization from the compliance officer (VEN-1, VEN-2). Manager approval doesn't count as that authorization.

## R04 — answers Q1

I couldn't find the Meridian Works policy, so I can't tell you which approvals this purchase needs.

The working directory (`Q1`) is empty, and I have no saved notes about Meridian Works. I also don't have any outside knowledge of the company's procurement or approval rules. Any approval chain I gave you would be a guess, and for a compliance question a wrong answer could do more harm than none.

To answer it, I'd need the policy itself. You could:
- put the policy file (PDF, DOCX, MD, etc.) in this directory or give me its path, or
- paste the relevant sections, such as approval thresholds, purchase categories and any rules that take effect on a certain date.

Once I have it, I'll check the purchase details against the policy: the $2,400 amount, that it's routine and not travel, and the October 12, 2026 request date. I'll also check whether any thresholds or rules changed around that date.

## R05 — answers Q2

**Answer: The employee needs both manager approval and finance approval before making the purchase.**

**Why:**

- **Threshold (EXP-2, AMD-2):** The purchase date is October 12, 2026. That is after July 1, 2025, so the current $2,500 routine threshold applies. $2,600 is above $2,500, so EXP-2 requires both manager and finance approval before purchase. The amount counts the full total, including taxes and fees (EXP-4).
- **Timing (DEF-2):** Both approvals have to come before the purchase happens.
- **Travel approval (TRV-1):** Not needed. This isn't airfare.
- **Emergency waiver (EMG-1, EMG-2, DEF-1):** Doesn't apply. The purchase is described as routine, and nothing points to an immediate operational or safety risk. So finance approval is not waived. Even if it were an emergency, manager approval would still be required.
- **Vendor (VEN-1, VEN-3):** The vendor isn't named. If it turns out to be a prohibited vendor, the purchase also needs written authorization from the compliance officer, and manager and finance approval can't stand in for that (VEN-2).

## R06 — answers Q4

**No, the purchase may not proceed.** It is from a prohibited vendor and there is no written compliance-officer authorization. Nothing in the policy overrides that, including the emergency.

**Why**

1. **The vendor rule decides it.** A purchase from a prohibited vendor "must not proceed" without written compliance-officer authorization, and "Emergency status alone does not change this prohibition" (VEN-1). Vendor restrictions are checked separately from every other exception: "Vendor restrictions always apply" (EXP-3), and an emergency "does not waive... vendor restrictions" (EMG-3).

2. **The emergency is real but doesn't help here.** The facts meet the definition of a qualifying emergency: an immediate operational risk that cannot reasonably await normal approval (DEF-1). The $4,000 amount is also within the $5,000 emergency cap (EMG-1, EXP-4). But the emergency exception only covers purchases from an **approved vendor** (EMG-1). It "does not apply to a prohibited vendor unless the vendor has received written compliance-officer authorization under VEN-2" (EMG-2). That authorization is missing, so the exception is unavailable.

3. **Manager or finance approval can't stand in for it.** The compliance officer's authorization cannot be inferred from manager or finance approval (VEN-2).

**What would let it proceed**

- **Step 1: compliance-officer authorization.** Get a specific written authorization from the compliance officer for this transaction (VEN-2).
- **Step 2: the approvals that would then apply.** On October 12, 2026, the routine threshold is $2,500 (AMD-2; DEF-3), so $4,000 is a higher-value purchase:
  - **If the emergency exception applies** (it is no longer blocked once the vendor is authorized, per EMG-2): manager approval is needed before purchase. Advance finance approval is waived, but finance must be notified within 24 hours after the purchase (EMG-1, EXP-3, DEF-2). Notifying finance is not the same as finance approving it.
  - **Otherwise:** both manager and finance approval are needed before purchase (EXP-2).

Even in an emergency, manager approval is never waived (EXP-3, EMG-3).

## R07 — answers Q8

**No.** The employee may not proceed. The emergency exception only waives advance finance approval. Manager approval before purchase is still required, and without it the purchase cannot go ahead.

**How the rules apply**

1. **Date and threshold:** The purchase is dated October 12, 2026, which is after July 1, 2025, so the current $2,500 routine threshold applies (AMD-2, DEF-3). Under that threshold, a $4,000 purchase would normally need both manager and finance approval before purchase (EXP-2, EXP-4).
2. **Emergency exception:** The facts say it is a qualifying emergency (DEF-1). The $4,000 total is under the $5,000 emergency cap, and the vendor is approved (VEN-3). So the exception applies, and advance finance approval is waived (EMG-1).
3. **What the exception doesn't waive:** Under EMG-1, "Manager approval remains required before proceeding." EXP-3 says the Emergency Policy "may waive advance finance approval, but not manager approval." EMG-3 adds that "an emergency does not waive manager approval." No provision removes the manager when they can't be reached, and no provision names a substitute approver.
4. **Notifying finance isn't approval:** Finance must be told within 24 hours after the purchase. That is a step after the purchase, not an approval, and it can't stand in for manager approval (EMG-1, DEF-2).

**What's required for this purchase to proceed**

| Requirement | Status | Timing |
|---|---|---|
| Manager approval | Required, not waived | Before purchase |
| Finance approval | Waived by the emergency exception | — |
| Finance notification | Required | Within 24 hours after purchase |
| Travel-office approval | Doesn't apply (not airfare) | — |
| Vendor authorization | Not needed (approved vendor) | — |

**Conclusion:** The emergency exception removes the need for finance approval, but the manager's approval before purchase still applies. If the employee can't get it, they may not make the purchase under the emergency exception or any other provision.

Sources: AMD-2, DEF-3, EXP-2, EXP-3, EXP-4, EMG-1, EMG-3, DEF-1, DEF-2, VEN-3.

## R08 — answers Q5

I can't answer this from the documents I can see. Your working directory (`Q5`) is empty, and when I tried to search the parent folder for "Meridian," the permission request was declined.

Approval rules like this depend on the specific policy: dollar thresholds, which travel categories count, who has to sign off, and when a version took effect. Since your date is October 12, 2026, which policy version was in force on that date matters too. I'd rather not guess at any of that.

To get an answer, either:
- put the Meridian Works expense/travel policy (and any amendments or memos) in the Q5 folder, or paste the relevant sections here, or
- grant read access to `A_V2_01` if the policy is stored there.

Once I can read it, I'll list the approvals required for a routine $900 airfare purchase on October 12, 2026, and cite the specific sections.

## R09 — answers Q6

**Answer: both manager approval and finance approval were required.**

**Why:**
1. **The date decides which threshold applies.** June 15, 2025 is before the July 1, 2025 effective date of the current $2,500 threshold. That threshold "does not apply retroactively" (AMD-2), and the Amendments Policy decides which threshold governs a given date (DEF-3). So the historic rule in AMD-1 applies, not EXP-1 or EXP-2, which only cover purchases on or after July 1, 2025.
2. **Under AMD-1, routine purchases above $2,000 need both manager and finance approval.** $2,300 is above $2,000. Thresholds are measured on the total amount including taxes and fees (EXP-4). If $2,300 is that total, it falls in the higher tier.
3. **The current rule would give a different answer.** Under EXP-1, the same purchase made on or after July 1, 2025 would need only manager approval, because it is $2,500 or less. That rule did not apply on June 15, 2025.

**Timing:** EXP-1 and EXP-2 say approval must come before purchase. AMD-1's own wording just says the approvals were "required" and doesn't state when they had to happen.

**Exceptions:** None apply on the facts given.
- **Travel:** This isn't a travel purchase, so TRV-1 and TRV-2 aren't triggered.
- **Emergency:** No emergency is described, so the emergency waiver of advance finance approval (EXP-3) isn't available.
- **Vendor:** The vendor's status isn't stated. Vendor restrictions apply separately from everything else (EXP-3). If the vendor were prohibited, the Vendor Policy would add its own requirement on top of these approvals.

**Sources:** AMD-1, AMD-2, DEF-3, EXP-1, EXP-2, EXP-3, EXP-4.

## R10 — answers Q3

I can't answer this from the Meridian Works policy, because I couldn't find a copy of it:

- The working directory (`Q3`) is empty.
- My request to read the parent folder (`A_V2_01`) was denied.
- There's nothing saved in memory about Meridian Works.

I don't want to guess. Procurement policies differ a lot in their dollar thresholds, who can approve emergencies, and notification deadlines. A made-up answer could look right and still be wrong.

To get an accurate answer, you can do one of these:
1. **Paste the relevant policy text** into the chat. That means the purchasing or approval thresholds, the emergency or urgent purchase provisions, the approved vendor rules, and any effective dates or amendments.
2. **Put the policy files in the Q3 folder**, or let me read the parent folder if that's where they are.

Once I have the policy, I'll check these points for your facts:
- Which approval tier a $4,000 non-travel purchase falls into.
- Whether "immediate operational risk that cannot reasonably await normal approval" meets the emergency exception, and who can approve under it.
- Whether buying from an approved vendor changes any requirement.
- Whether any version of the policy, amendment or effective date applies to October 12, 2026.
- What notifications are due after the fact, to whom, and by when.

## R11 — answers Q4

I can't give you a definitive answer yet because I don't have the Meridian Works policy text. Your working directory (`Q4`) is empty, my request to read the parent folder was denied, and I have no saved notes about this policy. I won't make up what the policy says.

**How the answer will likely turn out.** Your facts set up a conflict between two rules: an emergency exception (an immediate operational risk that can't wait for normal approval) and a prohibited-vendor restriction (where written compliance-officer authorization seems to be the way around it). Which one wins depends on the policy's wording:

1. **If the prohibited-vendor rule has its own exception that requires written compliance-officer authorization**, the answer is almost certainly **no**. A specific rule about prohibited vendors usually controls over a general emergency exception. An emergency normally speeds up or changes the *ordinary approval* process. It doesn't usually waive a separate compliance requirement, especially one that has to be in writing. Without that written authorization, the purchase shouldn't proceed.
2. **If the emergency exception expressly overrides all procurement restrictions, including vendor prohibitions** (for example, "notwithstanding any other provision"), the purchase might proceed. Even then, the policy probably requires documentation, notice, or ratification after the fact.
3. **Other facts that could matter:**
   - **The $4,000 amount:** whether it falls under a dollar threshold that triggers different approval tiers.
   - **"Non-travel":** whether travel and non-travel purchases are treated differently.
   - **The October 12, 2026 date:** whether a policy version or amendment took effect around then.
   - **Who can authorize:** whether someone other than the compliance officer, such as a delegate, can sign off in an emergency.

**What I need:** Please paste the relevant sections, or grant read access to the folder where the policy is stored. I'm looking for the emergency or exigent-purchase provision, the prohibited-vendor provision, the approval thresholds, and any effective-date or amendment language. With those, I can give you a firm answer that cites the specific provisions.

## R12 — answers Q8

I can't answer that from the policy, because I don't have the policy text. The working directory (`Q8`) is empty. I tried to look in the parent folder, but the permission request wasn't granted, so I haven't read any Meridian Works documents.

The answer depends on how the policy's wording sets up the emergency exception:

- **The exception replaces manager approval.** If the policy says something like "in an emergency, an employee may buy without prior approval," then the employee may go ahead. They would likely still have to document the purchase or get approval afterward.
- **The exception relaxes something else.** If it only waives other requirements, such as competitive bids or the approved-vendor rule, then manager approval is still required and the employee can't rely on the exception alone.
- **There's a dollar cap or a substitute approver.** Many policies limit emergency purchases to an amount, say $2,500, or require approval from someone else, like a department head or Finance, when the manager isn't available. If so, the $4,000 amount or the missing substitute approval could rule the purchase out.
- **The rules are date-specific.** You mention October 12, 2026, so there may be a policy revision or effective date that changes which rules apply.

If you paste the policy text here or let me read the parent folder, I'll check the actual wording and give you a definite answer with citations.

## R13 — answers Q7

**No. The employee can't use the emergency exception on these facts.** The ordinary rules apply: the $4,000 purchase needs **both manager approval and finance approval before it is made**.

**1. Which threshold applies (date first)**
- The transaction date is October 12, 2026. That is after the July 1, 2025 change, so the current routine threshold of $2,500 applies (AMD-2, DEF-3). The older $2,000 threshold in AMD-1 does not.

**2. Why the emergency exception doesn't apply**
- A qualifying emergency needs "an immediate operational or safety risk that cannot reasonably await normal approval." Calling a request "urgent" is not enough (DEF-1).
- "The label 'urgent' alone is not sufficient to establish a qualifying emergency" (EMG-3).
- Without evidence that DEF-1 is met, "emergency qualification is not established and ordinary purchase approvals continue to apply" (EMG-2).
- Because the request doesn't qualify, EMG-1 never applies. That means advance finance approval is not waived. The 24-hour after-purchase notice to finance in EMG-1 also doesn't come into play, and it is a notice, not an approval (DEF-2).
- Even if the employee later showed a real emergency, the $4,000 amount is under EMG-1's $5,000 cap. In that case only advance finance approval would be waived. Manager approval before the purchase would still be required, finance would need to be told within 24 hours after the purchase, and the vendor would have to be approved (EMG-1, EXP-3, EMG-3). Those facts haven't been supplied, so this doesn't apply now.

**3. Ordinary approvals**
- $4,000 is above the $2,500 threshold, measured on the total amount including taxes and fees (EXP-4).
- So **manager approval and finance approval are both required before the purchase** (EXP-2). "Before" means before the transaction goes ahead (DEF-2).

**4. Other things checked**
- **Travel:** This is not a travel purchase, so travel-office approval isn't triggered (TRV-1).
- **Vendor status:** The facts don't say whether the vendor is approved. That doesn't change the answer above. However, vendor rules apply separately: if the vendor is prohibited, the purchase can't go ahead without a specific written authorization from the compliance officer. Manager or finance approval doesn't count as that authorization (VEN-1, VEN-2, EXP-3).

**Bottom line:** Get manager approval and finance approval before buying (EXP-2, AMD-2). Also confirm the vendor's status and, if the vendor is prohibited, get written compliance-officer authorization.

## R14 — answers Q3

**You need manager approval before buying, and you must notify finance within 24 hours after buying.** Advance finance approval is waived.

**Why the emergency exception applies (EMG-1):**
- **Qualifying emergency:** An immediate operational risk that can't reasonably wait for normal approval fits the definition in DEF-1. It's more than just calling the request "urgent," which EMG-3 says isn't enough.
- **Amount:** $4,000 is within the $5,000-or-less emergency limit.
- **Vendor:** The vendor is approved (VEN-3), so the vendor restrictions don't block the exception.

**What's required:**
1. **Manager approval before the purchase.** The emergency exception never waives this (EXP-3, EMG-1, EMG-3).
2. **Finance notification within 24 hours after the purchase** (EMG-1). This is a notice after the fact, not an approval (DEF-2).

**What's not required:**
- **Advance finance approval.** Normally it would be needed, because a routine purchase over the $2,500 threshold in effect since July 1, 2025 requires it (EXP-2, AMD-2). The emergency exception waives it.
- **Travel-office approval.** The purchase isn't airfare (TRV-1).
- **Compliance-officer authorization.** The vendor isn't prohibited (VEN-1/VEN-2).

**Timing:** The purchase date was October 12, 2026, and today is October 13, 2026. The 24-hour window to notify finance therefore closes today, at the same time of day the purchase was made. If finance hasn't been notified yet, do it now.

## R15 — answers Q6

I can't answer this from anything I have access to. I don't have Meridian Works' policy documents, and I don't know the company's approval rules from general knowledge.

Here's where I looked:
- **The working directory (`Q6`)** is empty.
- **The parent folder (`A_V2_01`)**: my request to read it was denied, so I didn't look inside.
- **My memory from earlier sessions** has nothing saved for this project.

I'd rather not guess at the approval levels. Purchasing policies differ a lot between companies, and the answer may depend on which version of the policy was in effect on June 15, 2025.

To get an answer, you can:
1. Paste the relevant policy text here (approval thresholds, the effective dates of any revisions, and any amendments).
2. Put the policy files in the Q6 folder, or tell me their path.
3. Let me read the parent folder `A_V2_01`, if the policy is stored there.

Once I have the documents, I'll find which version applied on June 15, 2025, and tell you which approvals a routine, non-travel $2,300 purchase needed, citing the sections.

## R16 — answers Q2

I can't answer this yet because I don't have the Meridian Works policy. I couldn't find it anywhere I can reach:

- The working directory (`Q2`) is empty.
- I asked to read the parent folder (`A_V2_01`), but that permission was declined.
- There's nothing saved in memory about Meridian Works.

I don't want to guess at approval thresholds, since every company sets its own, and a made-up answer could send the request down the wrong path.

You can get me the policy in any of these ways:
1. Paste the policy text, or at least the purchasing/approval section, into the chat.
2. Put the policy file in the `Q2` folder.
3. Give me read access to the parent folder if the policy is there.

Once I have it, I'll check the $2,600 amount against the approval tiers. I'll also look for anything tied to the October 12, 2026 date, such as a policy version that took effect around then, a fiscal-quarter or year-end rule, or a temporary freeze. Then I'll check whether "routine, non-travel equipment" falls under any category-specific rules.

## R17 — answers Q3

You need **manager approval before the purchase**, and you must **notify finance within 24 hours after the purchase**. You don't need advance finance approval, because the emergency exception waives it.

**Approvals and notifications**

| Requirement | Timing | Source |
|---|---|---|
| Manager approval | Before the purchase | EMG-1, EXP-3, EMG-3 |
| Finance approval | **Waived** (normally required in advance) | EMG-1, EXP-3 |
| Finance notification | Within 24 hours after the purchase. This is a notice, not an approval. | EMG-1, DEF-2 |
| Travel-office approval | Not needed (not a travel purchase) | TRV-1 |
| Compliance-officer authorization | Not needed (approved vendor) | VEN-1, VEN-3, EMG-2 |

**How I got there**

1. **Date and threshold:** October 12, 2026 is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3). Without the exception, $4,000 is over $2,500, so you'd normally need both manager and finance approval before buying (EXP-2, EXP-4).
2. **Does it count as an emergency?** Yes. You described an immediate operational risk that can't reasonably wait for normal approval, which matches the definition in DEF-1. It's more than just calling the request "urgent" (EMG-2, EMG-3).
3. **Emergency exception (EMG-1):** All three conditions are met:
   - it's a qualifying emergency;
   - $4,000 is within the $5,000 limit;
   - the vendor is approved.

   So the advance finance approval is waived.
4. **What the exception doesn't change:** The emergency never removes the need for manager approval (EXP-3, EMG-3). The finance notice comes after the purchase and is not the same as finance approval (DEF-2).
5. **Vendor:** The vendor is approved, so no vendor restriction applies (VEN-3).

One thing to check: the $4,000 must be the full amount, including taxes and fees (EXP-4). If the total goes over $5,000, the exception no longer applies. You'd then need both manager and finance approval before buying (EXP-2).

## R18 — answers Q7

I can't answer this from Meridian Works' actual policy, because I couldn't find it.

- **What I checked:** The working folder (`Q7`) is empty.
- **What I couldn't check:** I asked to read the parent folder (`A_V2_01`), but that permission wasn't granted.

I'd be guessing if I gave you Meridian Works' approval thresholds, approvers, or emergency-exception rules, so I haven't.

**What I can say generally:** Most purchasing policies only allow an emergency exception when there is real evidence of urgent need, such as an immediate operational, safety or legal risk. Calling a request "urgent" usually isn't enough. On your facts, the employee has given no evidence of immediate operational or safety risk. So the likely answer is that the exception doesn't apply, and the $4,000 purchase goes through the normal approval process for its dollar amount. Whether that holds for Meridian Works depends on how its policy defines "emergency," what documentation it requires, and its approval tiers. Some policies also set different rules for different dates, which might matter for October 12, 2026.

**To get a definite answer, you can either:**
1. Paste the relevant policy text (the purchasing or approval policy and the emergency-exception section) here, or
2. Give me read access to `A_V2_01` or wherever the policy is stored.

Then I can tell you whether the exception applies and exactly which approvals are needed, with citations to the policy.

## R19 — answers Q6

The purchase needed **both manager approval and finance approval** before it was made.

1. **The old threshold applies.** EXP-1 and EXP-2 set the current $2,500 threshold, but only for purchases on or after July 1, 2025. AMD-2 says that $2,500 limit "does not apply retroactively." DEF-3 says the Amendments Policy decides which threshold applies based on the transaction date.
2. **Under the old rule, $2,300 is over the limit.** AMD-1 says that before July 1, 2025, routine purchases above $2,000 needed both manager and finance approval. $2,300 is above $2,000.
3. **The amount includes everything.** Under EXP-4, the threshold is measured against the total in US dollars, including taxes and fees.

The current $2,500 rule would only require manager approval, but it doesn't apply to a June 15, 2025 purchase.

Some caveats:
- **Travel Policy:** It doesn't apply because the purchase isn't travel.
- **Emergency waiver:** EMG-1 can waive advance finance approval, but you described the purchase as routine, so it doesn't qualify (DEF-1, EMG-2).
- **Vendor:** No vendor was named. If it was a prohibited vendor, the purchase also needed written authorization from the compliance officer (VEN-1). Manager or finance approval can't replace that (VEN-2).

## R20 — answers Q5

Two approvals are needed before the purchase: **manager approval** and **travel-office approval**. Finance approval isn't needed.

1. **Travel-office approval.** Under TRV-1 in `02-travel-policy.md:4`, any airfare above $800 needs advance travel-office approval, and $900 is over that line. "Advance" means before the transaction goes ahead (DEF-2).

2. **Manager approval.** The purchase is dated October 12, 2026, which is after July 1, 2025, so the current $2,500 threshold applies (AMD-2, DEF-3). A routine purchase of $2,500 or less needs manager approval only. $900 is under that, so finance approval isn't triggered.
   - EXP-1 (`01-expense-policy.md:5`) is worded for "non-travel" purchases. However, EXP-3 (`01-expense-policy.md:11`) and TRV-2 (`02-travel-policy.md:7`) say airfare is also subject to the Expense Policy purchase threshold. TRV-2 adds that travel-office approval never replaces manager approval.

**What doesn't apply:**
- **Finance approval:** not required, because $900 is below $2,500.
- **Emergency rules:** the purchase is routine, so the Emergency Policy doesn't apply. That means there's no 24-hour finance notification requirement.
- **Vendor rules:** the facts don't say whether the airline is a prohibited vendor. If it were, the purchase would also need written authorization from the compliance officer (VEN-1).

## R21 — answers Q5

**Two approvals are needed before the purchase: travel-office approval and manager approval.** Finance approval is not required.

**Required approvals (both before purchase)**
1. **Travel-office approval, in advance.** Airfare above $800 needs it, and $900 is above $800 (TRV-1). "Advance" means before the transaction proceeds (DEF-2).
2. **Manager approval.** The purchase is on October 12, 2026, which is after July 1, 2025, so the current $2,500 limit applies (AMD-2, DEF-3). The pre-July 2025 $2,000 limit (AMD-1) does not apply, and it would give the same result anyway. $900 is under $2,500, so manager approval is required before purchase (EXP-1, EXP-4). Airfare is subject to the travel rules and the purchase rules together (EXP-3, TRV-2).

**Not required**
- **Finance approval.** It only applies to purchases above $2,500 (EXP-2).
- **Notifications.** None apply. The 24-hour notice to finance only comes into play under the emergency exception (EMG-1).

**Exceptions**
- **Emergency (EMG-1 to EMG-3, DEF-1):** Doesn't apply because the purchase is routine. Even a qualifying emergency would only waive advance finance approval. It never waives manager approval or travel-office approval.
- **One approval replacing another:** Not allowed. Travel-office approval doesn't replace manager approval (TRV-2), and each approval is a separate requirement.

**Missing fact: vendor status.** The facts don't say whether the airline or booking vendor is approved or prohibited. Vendor rules always apply (EXP-3). If the vendor is prohibited, the purchase can't go ahead without a specific written authorization from the compliance officer. That would be in addition to the two approvals above, and manager or travel-office approval can't stand in for it (VEN-1, VEN-2).

**Timing note:** Today is October 13, 2026, so October 12 has already passed. If the purchase was made without both approvals in place, it didn't follow policy. The policy doesn't allow approval after the purchase.

## R22 — answers Q4

**No, the purchase may not proceed.** Meridian Works has prohibited this vendor and there is no written compliance-officer authorization, so the purchase is blocked. The emergency doesn't change that.

**Why**

1. **The vendor ban is absolute without written authorization.** VEN-1 says a purchase from a prohibited vendor "must not proceed" without written compliance-officer authorization, and that "emergency status alone does not change this prohibition." EXP-3 says "vendor restrictions always apply," and EMG-3 says an emergency "does not waive... vendor restrictions."

2. **The emergency exception doesn't cover this vendor.** The facts do describe a qualifying emergency under DEF-1: an immediate operational risk that can't reasonably wait for normal approval. The $4,000 amount is also within EMG-1's $5,000 cap. But EMG-1 only applies to purchases from an **approved vendor**. EMG-2 says the exception "does not apply to a prohibited vendor unless the vendor has received written compliance-officer authorization under VEN-2." No such authorization exists.

3. **Other approvals can't fill the gap.** Under VEN-2, compliance-officer authorization "may not be inferred from manager or finance approval." Getting manager and finance sign-off, which would normally be needed for a purchase over $2,500 dated after July 1, 2025 (EXP-2, AMD-2), still would not allow this purchase.

**What would allow it to proceed**

The compliance officer would need to give specific written authorization for this transaction under VEN-2. With that in place, the emergency exception could apply:
- Advance finance approval would be waived.
- **Manager approval would still be required before the purchase** (EMG-1, EXP-3).
- Finance must be **notified within 24 hours after the purchase** (EMG-1, DEF-2).

Without that authorization, the only compliant choice is to use an approved vendor or not make the purchase.

## R23 — answers Q1

**You only need manager approval, and it must be obtained before the purchase.** Finance approval isn't required, and no other approval applies on the facts given.

**How I got there**

1. **Date (AMD-1, AMD-2, DEF-3):** October 12, 2026 is after July 1, 2025, so the current $2,500 routine threshold applies. The older $2,000 limit in AMD-1 does not apply. Under that older limit, $2,400 would also have needed finance approval.
2. **Amount (EXP-1, EXP-4):** $2,400 is "$2,500 or less," which puts it in the EXP-1 tier: manager approval before purchase. The EXP-2 tier (manager and finance) starts only above $2,500. EXP-4 says the threshold is measured on the total transaction amount, including taxes and fees. That means $2,400 must be the all-in total. If taxes or fees push the total above $2,500, EXP-2 applies and finance approval is also required before purchase.
3. **Travel (TRV-1, TRV-2):** This is not a travel or airfare purchase, so travel-office approval doesn't apply.
4. **Emergency (EMG-1, EMG-2, DEF-1):** The purchase is routine and no emergency is claimed, so the emergency exception doesn't apply. It wouldn't matter here anyway: the exception only waives advance finance approval, which this purchase doesn't need, and never waives manager approval (EXP-3, EMG-3).
5. **Vendor (VEN-1, VEN-2, VEN-3, EXP-3):** You didn't say whether the vendor is approved or prohibited. On the facts given, no vendor restriction applies. If the vendor is prohibited, the purchase cannot go ahead without a specific written authorization from the compliance officer. Manager approval does not count as that authorization, and it is needed in addition to manager approval.

**Notifications:** None. The 24-hour finance notice in EMG-1 applies only to qualifying emergency purchases.

## R24 — answers Q7

**No, the employee can't use the emergency exception.** On these facts, the purchase needs **both manager approval and finance approval before it is made.**

**1. The emergency exception doesn't apply**
- Calling a request "urgent" isn't enough. A qualifying emergency means a purchase needed to address an *immediate operational or safety risk that cannot reasonably await normal approval* (DEF-1). The policy says plainly that "the label 'urgent' alone is not sufficient" (EMG-3).
- Without evidence that the DEF-1 test is met, "emergency qualification is **not established** and ordinary purchase approvals continue to apply" (EMG-2).
- The $4,000 amount is under the exception's $5,000 cap (EMG-1). But that only matters once a qualifying emergency is shown, and none is here.

**2. Which threshold applies**
- The purchase date is October 12, 2026, which is after July 1, 2025. So the current $2,500 routine threshold applies, not the older $2,000 one (AMD-1, AMD-2, DEF-3).
- $4,000 is above $2,500, so EXP-2 applies: **manager and finance approval, both before purchase**. The amount is measured as the full total, including taxes and fees (EXP-4).

**3. Other rules**
- **Vendor:** The facts don't say whether the vendor is approved or prohibited. Vendor restrictions apply either way (EXP-3, VEN-1). If the vendor is prohibited, the purchase can't go ahead without specific written authorization from the compliance officer. Manager or finance approval doesn't count as that authorization (VEN-2).
- **Travel:** This isn't a travel purchase, so travel-office approval under TRV-1 doesn't apply.

**4. If a real emergency were shown later**
Suppose new facts showed an immediate operational or safety risk and the vendor were approved. Then advance finance approval would be waived, but two things would still be required:
- manager approval before the purchase
- notice to finance within 24 hours after the purchase (EMG-1, DEF-2)

**Bottom line:** As things stand, the employee needs to get manager approval and finance approval before buying. They also need to meet any vendor restrictions that apply.
