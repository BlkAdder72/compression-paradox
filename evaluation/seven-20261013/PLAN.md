# Seven-question fresh execution plan — frozen before calls

## Chronology and selection
Original commit df36e7d contains all seven prompts and their original answer rows, before control da56555 and specialist 3d9be31. Original answers lived in evaluation/expected-answers.md. This new root questions.md consolidates them before the fresh runs. Seven-item selection occurred after prior results. Only Q4 is excluded, for its context dependency and subsequent post-folder amendment; no answer was removed based on performance. The original eight-question runs, including Q4, remain available. This cannot retrospectively change original file placement or guarantee moderator acceptance.

## Execution
Use unchanged specialist and fixture. Runs A_SEVEN_01, B_SEVEN_01, C_SEVEN_01: seven independent fresh sessions each in original retained ID order Q1,Q2,Q3,Q5,Q6,Q7,Q8. Fixed arm order A,B,C. Same native Claude Code 2.1.288 binary, requested model claude-opus-5-5, identical runner flags and account configuration. A has no files, B ten specialist files, C six primary documents. Default --suite official selects the seven-question JSON, and sends only prompt fields. --suite official-v2 remains the eight-question historical suite. CLI is not the Projects UI. Account configuration and provider model revision limitations persist.

Stop on failure; retain every byte and attempt. Do not retry an existing ID. If execution fails, record the cause and use a new numbered ID for any replacement; no silent cherry-picking. Review model IDs, session contents, permissions and all tool traces before grading. Exclude contamination prospectively and disclose it. Preserve raw captures under evidence/seven-20261013 and commit them before grading. No seven-question scores are claimed until execution succeeds.

## Evaluation
Use unchanged evaluation/scoring-rubric.md and original gold answers, restricted to retained IDs. Maximum 70; conclusion 0/2/4, rules 0–2, exceptions 0–2, evidence 0–1, unsupported 0–1. Wrong operational conclusion capped at 4. Evidence requires correctly used real section ID and no false ID. Report each category and rationale, false authorizations, full conclusions, per-question W/T/L, measured mean wall times and source reads. No pooled totals with U or old Q sets.

The Codex assistant will assess the complete recorded responses against the frozen keys and source corpus. This is one model assessor with prior knowledge of the experiment; do not claim independent human review, effective blinding or two-assessor agreement for these new runs. Raw responses, scoring rationale and arithmetic remain reviewable. Earlier two-assessor results are historical/supplementary. Any additional review must be separately identified, never invented.

Do not tune specialist or questions after seeing these outputs. Report any loss or tie. U1–U8 remain the separately authored supplementary evidence; they are not replaced or represented as newly run here. This round tests the exact seven-item submitted benchmark. Freeze input hashes and commit this plan before model calls.
