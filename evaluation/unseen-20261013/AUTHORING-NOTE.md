# Authoring Note — Meridian Works Policy Evaluation Set (U1–U8)

Generated in a separate Claude session using only the supplied primary documents. The session's configured model identifier was `claude-opus-5-5`. The serving model cannot be independently verified from inside the session. The questions were not written by a human, were not reviewed by anyone outside this session, and were not reviewed by a model from a different family. No model comparison was run and no responses were graded.

## Source files

All six files arrived in one ZIP archive. Each was confirmed present and readable as UTF-8 Markdown before authoring began.

1. `01-expense-policy.md` (EXP-1 – EXP-4)
2. `02-travel-policy.md` (TRV-1 – TRV-2)
3. `03-emergency-policy.md` (EMG-1 – EMG-3)
4. `04-vendor-policy.md` (VEN-1 – VEN-3)
5. `05-policy-amendments.md` (AMD-1 – AMD-3)
6. `06-definitions.md` (DEF-1 – DEF-3)

No other material was consulted: no web pages, other conversations, project files, existing questions, model outputs, specialist instructions or results. The session environment automatically included a short account-profile note about the requesting user. It has nothing to do with Meridian Works and was not used.

## Coverage

| ID | Primary focus | Secondary elements |
|----|---------------|--------------------|
| U1 | Threshold boundary including tax and fees ($2,554.50, then exactly $2,500.00) | Inclusive "or less"; current threshold |
| U2 | Historical vs. current effective date ($2,300 on June 20, 2025 vs. July 1, 2025) | No retroactivity; audit date doesn't matter |
| U3 | Emergency qualification that holds, plus the $5,000 cap ($4,800 vs. $5,150) | Manager approval still required; 24-hour notice is not an approval |
| U4 | "Urgent" label without qualifying facts | Conditional outcome if DEF-1 facts are added |
| U5 | Prohibited vendor; manager/finance approval can't substitute for compliance authorization | Finance approval not needed at $1,200 |
| U6 | Emergency + authorized prohibited vendor | **Explicit ambiguity** (see A1) |
| U7 | Airfare dependencies: travel office + expense threshold; $800.00 boundary | Base fare under threshold but total over; travel office does not replace finance |
| U8 | Missing fact (vendor status) requiring a conditional answer | Emergency airfare; travel office not waived; prohibited-vendor branch |

Every category is covered at least twice. Taxes and fees: U1, U7. Effective dates: U2, plus the date-dependent threshold in U1, U5 and U7. Emergency: U3, U4, U6, U8. Vendor: U5, U6, U8. Travel: U7, U8. Conditional answers: U4, U6, U8.

## Ambiguities and limitations

- **A1 – Authorized prohibited vendor under the emergency exception (U6, U8 branch 3).** EMG-1 waives finance approval only for purchases "from an approved vendor." Under VEN-3, a vendor is approved only if the facts designate it approved. EMG-2, however, says the exception does not apply to a prohibited vendor "unless the vendor has received written compliance-officer authorization under VEN-2," which implies an authorized prohibited vendor *can* use the exception. The text does not resolve this. The gold answers lay out both readings and their consequences, and do not invent a rule.
- **A2 – "Non-travel" wording vs. airfare.** EXP-1 and EXP-2 describe "routine non-travel" purchases. EXP-3 and TRV-2 nonetheless apply "the relevant/applicable purchase threshold" to airfare and all travel expenses. U7 and U8 apply the $2,500 manager/finance threshold to airfare based on EXP-3 and TRV-2. That is the reading the text points to, but it is an inference across sections.
- **A3 – Scope of EXP-4 (tax-inclusive totals).** EXP-4 sits in the Expense Policy but says "All thresholds." The set assumes it also governs the $800 travel threshold and the $5,000 emergency cap. EMG-1's word "totaling" supports this for the emergency cap. To limit exposure, the U7(b) boundary case reaches exactly $800.00 only after adding taxes and fees, and TRV-1 states expressly that $800 or less needs no travel-office approval.
- **A4 – Finance notice when no finance approval would be needed anyway.** EMG-1 does not say whether the 24-hour notice applies to emergency purchases already below the routine threshold. No question depends on this.
- **A5 – "Incurred" vs. transaction date.** EXP-1/EXP-2 use "incurred" and DEF-3 uses "transaction date." Every dated scenario uses a single unambiguous date, so no question depends on the difference.
- **A6 – Travel threshold before July 1, 2025.** The Travel Policy has no effective date. AMD-3 says the amendment didn't change it. No question tests pre-July-2025 airfare.
- **Limitations.** The set has only eight questions, from six short source documents. Gold answers were written and checked by the same model that wrote the questions. DEF-1 qualification is stated in the facts (U3, U6, U8) or left out entirely (U4) to avoid judgment calls, so the set doesn't test whether borderline facts amount to an emergency.

## Self-check against the source text

- **Readability:** all six files were extracted and printed in full; all six section-heading sets were parsed.
- **JSON:** parsed with Python `json`, decoded as UTF-8. Top-level keys are exactly `provenance` and `questions`. There are 8 questions, each with exactly `id`, `prompt`, `gold` and `critical_requirements` (a non-empty array).
- **IDs:** U1–U8, unique and in order.
- **Citations:** every section identifier in each `gold` and `critical_requirements` field was extracted by regex and matched against the 18 `##` headings in the sources (AMD-1–3, DEF-1–3, EMG-1–3, EXP-1–4, TRV-1–2, VEN-1–3). Every cited section exists, and every question cites at least one.
- **Answer leakage / self-containment:** each prompt was checked automatically for section identifiers and for references to other questions ("U#", "previous/earlier question"). None were found. Each prompt names the policy set and supplies every fact it needs: date, amount breakdown, vendor status (or explicitly says it is unknown) and approvals obtained.
- **Arithmetic:** checked in code: 2,350 + 164.50 + 40 = 2,554.50; minus 54.50 = 2,500.00; 2,430 + 270 = 2,700; 742.50 + 57.50 = 800.00.
- **Rule-by-rule re-read:** each gold conclusion was re-checked against its cited provisions. Examples: no retroactivity (AMD-2), emergency doesn't waive manager approval or travel office (EMG-1, EMG-3, EXP-3), notice is not approval (DEF-2), approvals can't imply compliance authorization (VEN-2), and travel office doesn't replace other approvals (TRV-2).
