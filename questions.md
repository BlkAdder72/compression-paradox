# Official seven-question benchmark — Q1–Q3, Q5–Q8

These seven prompts and their expected answers are unchanged from commit `df36e7d`, before the first control run and creation of the specialist. Original IDs are retained for traceability. Q4 is excluded because its original cross-question dependency required a later amendment; all versions, scores and raw Q4 captures remain in history and the historical evidence directories.

This seven-question selection and consolidated question-and-answer file were made after the earlier results were known. This is a disclosed subset, not a claim that this exact seven-item selection was originally preregistered. Original expected answers were committed in `evaluation/expected-answers.md` at the same initial commit; they were not originally in questions.md. Full chronology is in `evaluation/seven-20261013/PLAN.md`.

Send only each prompt below, in this order, to separate fresh sessions. Never send the expected answers to a tested model. The current `--suite official` runs exactly these seven; `--suite official-v2` preserves the historical eight-question corrected benchmark. Maximum score: 70 under the unchanged per-question rubric.

**Q1.** Under Meridian Works policy, an employee requests a routine, non-travel equipment purchase of $2,400 on October 12, 2026. What approvals are required before proceeding?

**Q2.** Under Meridian Works policy, an employee requests a routine, non-travel equipment purchase of $2,600 on October 12, 2026. What approvals are required before proceeding?

**Q3.** Under Meridian Works policy, an immediate operational risk that cannot reasonably await normal approval requires a $4,000 non-travel purchase on October 12, 2026, from an approved vendor. What approvals and notifications are required?

**Q5.** An employee plans a routine $900 airfare purchase on October 12, 2026, under Meridian Works policy. What approvals are required before the purchase?

**Q6.** Under Meridian Works policy, what approvals were required for a routine, non-travel $2,300 purchase on June 15, 2025?

**Q7.** An employee requests a $4,000 non-travel purchase on October 12, 2026, calling it 'urgent' but providing no evidence of immediate operational or safety risk. Can the employee use Meridian Works' emergency exception, and what approval requirements apply on the supplied facts?

**Q8.** Under Meridian Works policy, a $4,000 non-travel purchase on October 12, 2026, qualifies as an emergency and uses an approved vendor, but the employee cannot obtain manager approval. May the employee proceed solely under the emergency exception? Explain.

## Expected answers — evaluator only

| ID | Gold conclusion | Required components | Evidence | Disqualifying mistake |
|---|---|---|---|---|
| Q1 | Manager approval before purchase | No finance approval required for routine $2,400; threshold $2,500 inclusive | EXP-1, AMD-2 | Finance approval required |
| Q2 | Manager AND finance before purchase | $2,600 is above current $2,500 threshold | EXP-2, AMD-2 | Manager alone sufficient |
| Q3 | Manager before purchase; finance notified within 24 hours after purchase; no advance finance approval | Qualified immediate risk, approved vendor, $4,000 <= $5,000, non-travel | EMG-1, DEF-1, DEF-2, EXP-3 | No manager approval; finance approval confused with notification |
| Q5 | Advance travel-office AND manager before purchase | Airfare $900 > $800; $900 <= $2,500; approvals independent | TRV-1, TRV-2, EXP-1, EXP-3 | Travel approval replaces manager approval |
| Q6 | Manager AND finance before purchase | Historic pre-July-2025 threshold $2,000; $2,300 > $2,000 | AMD-1, AMD-2 | Applies $2,500 threshold retroactively |
| Q7 | Emergency qualification not established; ordinary manager AND finance approval required on supplied facts | 'Urgent' does not prove immediate risk; $4,000 > $2,500 | EMG-2, EMG-3, DEF-1, EXP-2 | Definitively authorizes emergency waiver |
| Q8 | No, cannot proceed | Emergency waives only advance finance; manager approval remains required | EMG-1, EMG-3, EXP-3 | Assumes manager can be bypassed |
