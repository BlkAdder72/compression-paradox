# Results — Compression Paradox benchmark, Stage 2 (single run per arm)

**Scored 2026-10-12 · model `claude-opus-5-5` via Claude Code CLI 2.1.288 · n = 8 questions · one run per arm · no statistical significance claimed.**

| Arm | Exposure | Score /80 | Correct operational conclusions | False authorizations |
|---|---|---|---|---|
| A — no-folder control (run A2) | nothing | **11** | 0 / 8 | 0 |
| B — treatment, specialist folder (B1) | identity + rules + examples + index + 6 sources | **80** | 8 / 8 | 0 |
| C — source-only diagnostic (C1) | 6 sources only | **78** | 8 / 8 | 0 |
| D — aggressive summary | — | not run on Q1–Q8 (see Stage 4, H-series) | | |
| E — index-first | — | not run on Q1–Q8 (see Stage 4, H-series) | | |

Per question (capped totals):

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|---|---|---|---|---|---|---|---|---|
| A | 1 | 1 | 1 | 1 | 1 | 1 | 4 | 1 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| C | 9 | 10 | 10 | 10 | 10 | 9 | 10 | 10 |

- **B vs A (official A/B):** 8 wins, 0 ties, 0 losses. **Confounded:** B had the policy text and A did not. This does not show the folder's structure adds value.
- **B vs C (architecture diagnostic):** 2 wins, 6 ties, 0 losses (+2 points). Both B wins (Q1, Q6) come only from the 1-point *evidence* item: C gave correct answers but cited `file:line` instead of section identifiers. On operational correctness B and C tie 8/8. The likely cause is B's rule 9 ("cite section identifiers"), which is a formatting instruction, not better navigation.
- **C vs A:** 8 wins, 0 losses. Supplying the sources accounts for almost all of the gain.
- **Compression Paradox check:** the specialist folder did **not** hide any essential condition in this run. B made no omissions, regressions or false authorizations. With full sources available to both B and C, this benchmark shows no measurable navigation advantage from the structure beyond citation format.

## Transparent uncertainty in A
Every A response said it lacked the Meridian Works policy and invented no thresholds, so A made 0 unsupported claims and 0 false authorizations. On Q7, A reasoned conditionally that "urgent" without evidence of risk would likely not qualify, which earned partial credit (assessor's judgement call: conclusion 2 vs 0, capped total 4 either way). Under the rubric, refusals earn no conclusion points because the answers were checkable.

## Secondary metrics (measured from captures)
- Wall time per session (`duration_ms`): A mean ≈ 13.8 s, B ≈ 26.0 s, C ≈ 19.6 s.
- Visible source reads: A 0 files. B read all 10 folder files in 7 of 8 sessions (8 in Q6). C read all 6 sources in every session.
- Permission denials (attempted reads outside the session directory, all blocked): A 7 of 8 sessions, B 1 of 8, C 1 of 8.
- Run-to-run consistency: **not measured** (single run per arm).

## Limitations and disclosures
1. **Folder author bias.** The specialist folder was written by Claude (Opus 5.5) in the same session that had already read the questions and answer key. The examples deliberately use different amounts and scenarios, but the folder cannot be called blind to the test.
2. **Assessor.** Scoring was done by an independent subagent (same model family) that received only the rubric, key, questions and 24 shuffled responses with directory paths removed (`evaluation/scoring-run-1/`). A responses are recognisable by content (refusals), so blinding was effective only between B and C. No second assessor was used, so no disagreements were adjudicated.
3. **Interface.** Claude Code print mode adds Claude Code's default system prompt (not exportable). Read/Glob/Grep were enabled in all arms for parity, and temperature was not controllable. The first control attempt (A1) failed authentication before reaching the model. Its records are retained.
4. **Ceiling effect.** B and C are both at or near ceiling, so this 8-question set cannot separate structure from sources. Harder holdout questions, D/E ablations and repeated runs are needed.

## Stage 3 — Pre-registered supplemental work (executed in Stage 4, below)

The aggressive-summary (D) and index-first (E) variants, together with eight supplemental post-analysis challenge questions (H1–H8), have been committed as experimental materials. **No D/E/H scores exist yet.** The H questions were designed after the Stage 2 results were known and are not truly blind unseen questions. All Stage 2 scores above remain unchanged. See `diagnostics/README-stage3.md` and `evaluation/holdout/`.

## Stage 4 — H-series supplemental runs (executed 2026-10-12)

**Runs DH1, EH1, CH1 · one run per arm · `claude-opus-5-5` via Claude Code CLI 2.1.288 (same build as Stage 2) · unmodified `scripts/run_holdout_cli.sh` at commit 206da8e · raw captures committed at 9855e10 before scoring.** All preflight gates and all three `verify_stage4_capture.py` checks passed; 24/24 sessions exit 0, no permission denials, no retries. Manifests: `diagnostics/*/run-manifest-?H1.md`.

| Arm | Exposure | Score /80 | Correct operational conclusions | False authorizations | Critical omissions |
|---|---|---|---|---|---|
| C — source-only (CH1) | 6 sources | **80** | 8 / 8 | 0 | 0 |
| D — aggressive summary (DH1) | README + SUMMARY + 6 sources | **80** (79 under strict evidence reading, see below) | 8 / 8 | 0 | 0 |
| E — index-first (EH1) | index README + 6 sources | **80** | 8 / 8 | 0 | 0 |

Per question: every response scored 10 on H1–H8 in every arm. **D vs C, E vs C, E vs D: 0 wins, 8 ties, 0 losses.**

- **Pre-registered hypothesis** ("E will preserve condition coverage more consistently than D on boundary and cross-policy cases"): **not supported**. D and E tied at ceiling; neither omitted a condition. The secondary clause (E may take longer or open more files) was not borne out: D opened the most files (6–8 per session, mean wall time ≈ 23.7 s), E opened 7 (≈ 24.1 s), C opened 6 (≈ 20.0 s).
- **Compression Paradox check:** the aggressive summary did **not** hide essential conditions in this run, but the reason matters. Every D session also read the full primary sources, often *before* SUMMARY.md. In 4 of 8 (H3, H5, H6, H8) the answer explicitly flagged the summary as incomplete and relied on the primary text (citing DEF-3). So this run tests "summary plus full sources" against a careful reader, not "summary alone". A harder test would remove or demote the sources, or penalise the extra reads.
- **Ceiling effect persists.** All three arms are at 80/80 on questions designed to stress boundaries. This set cannot separate the arms either.

### Scoring and disclosures
1. **Assessor.** One independent subagent (same model family) scored 24 shuffled responses using only `evaluation/scoring-run-2/blind_packet.md` (rubric + H questions + holdout key + responses, directory paths stripped). Unblinding key: `blind_key.json` (seeded shuffle). Scores: `assessor-scores.json`. No second assessor, so no adjudication.
2. **Blinding leak.** Four D responses name `SUMMARY.md`, so those are identifiable as D. They were not edited.
3. **Assessor uncertainty.** R16 (D, H8) cites mostly `file:line` plus DEF-3, a real section not in H8's controlling list. The assessor awarded the evidence point. Under a stricter reading (controlling-list IDs only), D scores 79/80. Operational conclusion unaffected either way.
4. **Rubric adaptation.** The rubric names false-authorization questions only for the Q-series. For H, the assessor was told to flag any omitted pre-purchase approval or any wrongly asserted waiver or compliance. This mapping was set before scoring.
5. **Not blind questions.** H1–H8 were written after the Stage 2 results were known, so they are supplemental post-analysis challenge questions, not independent holdouts. D/E were not run on Q1–Q8.
6. Single run per arm; run-to-run consistency not measured; no statistical significance claimed. Arms ran sequentially (D, E, C) rather than interleaved.
