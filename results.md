> **Current headline (2026-10-13).** Three separate evidence sets. They are not pooled.
>
> | Evidence set | A — no folder | B — specialist folder | C — sources only | B vs A | B vs C |
> |---|---|---|---|---|---|
> | Corrected official v2, Q1–Q8 (A/B/C_V2_01) | 14/80 | 80/80 | 80/80 | 8 W / 0 T / 0 L | 0 W / 8 T / 0 L |
> | Separate-session U1–U8 (A/B/C_U_01) | 8/80 | 77/80 | 80/80 | 8 / 0 / 0 | **0 / 7 / 1** |
> | Original v1, Q1–Q8 (A2/B1/C1; reruns below) | 11 | 80 | 78 | 8 / 0 / 0 | 2 / 6 / 0 |
>
> The folder beats no folder on every question, but A has no policy text, so A/B mostly measures source availability. Against the six sources alone (C), the folder tied on all corrected v2 questions and on 7 of 8 questions it did not write. It **lost U8** by 3 points: it treated a genuinely ambiguous vendor branch as settled, where the frozen criterion required both readings. Nothing in the folder was changed because of this; the folder is frozen for these tests (see the end of this report). Sections below are chronological. Everything before "Corrected official v2" scores the original **v1** questions (archived in `history/questions-v1.md`). Root `questions.md` is now v2: Q4 was made self-contained after the folder already existed, so v2 is a correction, not original pre-registration.

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
- Stage 2 alone did not measure run-to-run consistency; the imported A/B rerun below and Stage 4 repeats provide limited repeat evidence.

## Limitations and disclosures
1. **Folder author bias.** The specialist folder was written by Claude (Opus 5.5) in the same session that had already read the questions and answer key. The examples deliberately use different amounts and scenarios, but the folder cannot be called blind to the test.
2. **Assessor.** Scoring was done by an independent subagent (same model family) that received only the rubric, key, questions and 24 shuffled responses with directory paths removed (`evaluation/scoring-run-1/`). A responses are recognisable by content (refusals), so blinding was effective only between B and C. No second assessor was used, so no disagreements were adjudicated.
3. **Interface.** Claude Code print mode adds Claude Code's default system prompt (not exportable). Read/Glob/Grep were enabled in all arms for parity, and temperature was not controllable. The first control attempt (A1) failed authentication before reaching the model. Its records are retained.
4. **Ceiling effect.** B and C are both at or near ceiling, so this 8-question set cannot separate structure from sources. Harder holdout questions, D/E ablations and repeated runs are needed.

## Stage 3 — Pre-registered supplemental work (executed in Stage 4, below)

The aggressive-summary (D) and index-first (E) variants, together with eight supplemental post-analysis challenge questions (H1–H8), have been committed as experimental materials. At Stage 3 no D/E/H scores existed; completed Stage 4 results follow below. The H questions were designed after the Stage 2 results were known and are not truly blind unseen questions. All Stage 2 scores above remain unchanged. See `diagnostics/README-stage3.md` and `evaluation/holdout/`.

## Stage 4 — H-series supplemental runs (executed 2026-10-12)

**Runs DH1, EH1, CH1 · one run per arm · `claude-opus-5-5` via Claude Code CLI 2.1.288 (same build as Stage 2) · unmodified `scripts/run_holdout_cli.sh` at commit 206da8e · raw captures committed at 9855e10 before scoring.** All preflight gates and all three `verify_stage4_capture.py` checks passed; 24/24 sessions exit 0, no permission denials, no retries. Manifests: `diagnostics/{aggressive-summary,index-first}/raw/run-manifest-?H1.md`, `diagnostics/source-only/run-manifest-CH1.md`.

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
6. Arms ran sequentially (D, E, C) rather than interleaved. No statistical significance claimed. Run-to-run consistency: see the repeat below.

## Stage 4 — repeat run (run 2) and run-to-run consistency

**Scored runs: CH2, DH3, EH3 · same CLI build, model, runner and prompts as run 1 · raw captures committed (e4d5bd2, fcecdea) before scoring · fresh blind assessor, new shuffle (`evaluation/scoring-run-3/`).** All gates and capture checks passed; 24/24 sessions exit 0, no permission denials.

**Excluded runs DH2 and EH2 (operator error, disclosed).** The run-1 manifests had been saved inside `diagnostics/aggressive-summary/` and `diagnostics/index-first/`, which the runner copies into every session. Several DH2/EH2 sessions opened them. They held run settings only (no answers, key or scores), but exposure differed from run 1, so those runs are kept unedited and not scored (`raw/run-manifest-?H2.md`). Fix (b3d2417): manifests moved into `raw/` (the runner strips it), and `preflight_stage4.py` now fails if an arm folder holds anything beyond its frozen files. D and E were then rerun cleanly as DH3/EH3. CH2 was unaffected (arm C copies `fixture/`). `verify_stage4_capture.py` was also fixed to read UTF-8: it had rejected the valid CH2-H6 capture on Windows (cp1252 default).

| Arm | Run 1 | Run 2 | Correct conclusions (run 1 / run 2) | False authorizations | Critical omissions |
|---|---|---|---|---|---|
| C — source-only | 80 | **80** | 8/8 · 8/8 | 0 | 0 |
| D — aggressive summary | 80 | **77** | 8/8 · 8/8 | 0 | 0 |
| E — index-first | 80 | **80** | 8/8 · 8/8 | 0 | 0 |

Run 2, per question: C and E scored 10 everywhere. D scored 9 on H2, H3 and H7, and 10 elsewhere.
- **D H2, D H3 (evidence 0):** cited only `file:line`, no section identifier. This is the same formatting failure seen in Stage 2's C1 and in the borderline DH1 H8 item.
- **D H7 (exceptions 1):** correct conclusion, but it hedged that a "strict reading" of EMG-1 ("approved vendor") might deny the exception that EMG-2 extends to authorised prohibited vendors. That ambiguity comes from the primary text, not the summary, which says nothing about vendors in emergencies.
- **Pairwise, run 2:** E vs D 3 wins / 5 ties / 0 losses. C vs D 3 / 5 / 0. E vs C 0 / 8 / 0.

**Consistency.** Across two runs, all 32 C/E responses and all 16 D responses (48 total) reached the correct operational conclusion, with no false authorizations or critical omissions. C and E were perfectly stable (80/80 twice). D was the only arm to drop points (80 → 77), all on secondary rubric items.

**Hypothesis, updated.** The pre-registered claim concerned *condition coverage*: that E would preserve conditions more consistently than D. It remains **not supported**, because neither arm omitted a condition in either run. There is a weak directional signal that D is less stable on citation form and hedging (3 points in one of two runs). It is too small to distinguish from run-to-run noise with n = 2. Mean wall time, run 2: C ≈ 21.0 s, D ≈ 23.9 s, E ≈ 22.5 s.

**Assessor notes (run 2).** The assessor could not confirm DEF-3 and VEN-3 from the packet and treated them as real. They are real: both exist in the fixture, so no change. It judged C's H7 answer (R02) as covering "authorization does not replace manager approval" (lenient reading) and noted a minor date-scope inconsistency in C's H5 (R09) without deduction. A stricter assessor might have docked those items. Same-family single assessor, no adjudication.


## Finalization audit note (2026-10-12)

This lowercase `results.md` is the exact competition-required report path. The legacy uppercase report is preserved byte-for-byte at `history/RESULTS-original.md` and in full Git history; there is only one root results report. The first-stage and supplemental figures above are recorded outcomes, **not independently rerun in this finalization pass**. No independently authored third-party challenge has yet been captured. For exact fresh-clone procedures and limitations see `REPRODUCE.md`.

## Repair audit and imported A/B reproduction (2026-10-13)

This repair performed offline integrity and arithmetic checks, not fresh Claude calls or independent grading. The uploaded archive already contained A_REPRO_1/B_REPRO_1. Their raw captures, manifests and scorer files support the recorded totals below; provider authenticity and assessor independence have not been externally verified. `history/REPRODUCTION-RESULTS-repair-annotated.md` contains the imported report with repair clarifications.

| Evidence | A total /80 | B total /80 | B wins / ties / losses |
|---|---:|---:|---|
| Original A2/B1 | 11 | 80 | 8 / 0 / 0 |
| Imported A_REPRO_1/B_REPRO_1 | 11 | 80 | 8 / 0 / 0 |
| New execution during this repair | PENDING | PENDING | Not measured (superseded: see "Fresh verification runs" below) |

The imported rerun matches all original per-question scores. Recomputed mean duration: A 12.919625 seconds; B 26.106875 seconds. This is evidence from the supplied archive, not an independent clean-machine reproduction. Source availability still confounds A/B; B/C operational correctness remains tied in the original comparison.

`python scripts/audit_evidence.py` verifies stored score arithmetic, eight completed result records per scored arm/run, and 238 existing checksum entries. It does not regrade answers or prove that the provider generated them. All original raw files, including failed and excluded attempts, remain unchanged. Historical assessor descriptions are reported claims, not independently established external review.

At the time of that repair, fresh A/B and H-series tests were PENDING because no accessible Claude CLI was found in that environment; they were executed later the same day (next section). External unseen author: NOT AVAILABLE. The G-series kit in `evaluation/challenge/` is generated, unexecuted, and explicitly NOT independent. No Git remote or actual public repository URL was present, so public GitHub access and publication are UNVERIFIED. Competition rule source and exact deadline/timezone were not supplied; full external rule compliance cannot be certified from package structure alone. See `RELEASE-READINESS.md`.

## Fresh verification runs (executed 2026-10-13)

**New runs, distinct from the imported A_REPRO_1/B_REPRO_1 records. Six runs at revision `9e79e0e` · Claude Code CLI 2.1.288 · actual model `claude-opus-5-5` in all 48 sessions · `scripts/run_trials.py` from a fresh clone · pre-registered in `evaluation/fresh-20261013/PLAN.md` before any call · raw evidence committed (`64b3ca9`) before scoring.** Run record: `evidence/fresh-20261013/RUN-RECORD.md`. Scoring: `evaluation/fresh-20261013/` (two blinded assessors per set, adjudication, `summary.json`).

### Official Q1–Q8 (A/B/C)
| Arm | Run | Score /80 | Strict-evidence /80 | Correct conclusions | False authorizations | Mean wall time |
|---|---|---|---|---|---|---|
| A — no folder | A_FRESH_20261013_01 | **16** | 16 | 0 fully correct (Q4 partial, 2/4 conclusion) | 0 | 14.2 s |
| B — specialist folder | B_FRESH_20261013_01 | **80** | 80 | 8 / 8 | 0 | 19.5 s |
| C — source only | C_FRESH_20261013_01 | **80** | 80 | 8 / 8 | 0 | 15.9 s |

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|---|---|---|---|---|---|---|---|---|
| A | 1 | 1 | 1 | 4 | 1 | 1 | 4 | 3 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| C | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |

- **B vs A: 8 wins, 0 ties, 0 losses. C vs A: 8 / 0 / 0. B vs C: 0 / 8 / 0.**
- The official A/B comparison is **confounded**: B has the policy text and A does not, so it does not isolate the folder's architecture. The architecture test is B vs C. In this fresh run B and C tie on every question, and the original run's +2 B advantage did not recur, because C now cited section IDs. This run therefore shows **no measurable benefit from the specialist structure beyond supplying the sources**.
- **A behaviour:** all 8 responses said the policy was unavailable and invented no thresholds (transparent uncertainty 8/8).
  - On Q4, Q7 and Q8, A reasoned conditionally and earned partial credit.
  - Q8 lost the unsupported-claims point: it floated a backup approver or after-the-fact approval as "most likely", which contradicts the policy's pre-purchase manager approval.
  - A scored 16 here versus 11 in A2 and A_REPRO_1, a run-to-run difference in how far the model reasons without sources.
- **Critical omissions:** A, on every question. B and C: none.
- **Benchmark design note (disclosed, unchanged):** Q4 says "The same facts as Q3 apply", but each question runs in an independent session. In this run one B and one C answer remarked that they could not see Q3's facts, yet both answered correctly. Q4 depends on context the session does not supply.

### H-series H1–H8 (C/D/E; post-analysis questions, not independent holdouts)
| Arm | Run | Score /80 | Strict-evidence /80 | Correct conclusions | False authorizations | Critical omissions | Mean wall time |
|---|---|---|---|---|---|---|---|
| C — source only | CH_FRESH_01 | **80** | 80 | 8 / 8 | 0 | 0 | 16.2 s |
| D — aggressive summary | DH_FRESH_01 | **80** | 79 | 8 / 8 | 0 | 0 | 18.2 s |
| E — index first | EH_FRESH_01 | **80** | 80 | 8 / 8 | 0 | 0 | 18.0 s |

Every question scored 10 in every arm. **C vs D, C vs E, D vs E: 0 / 8 / 0.** Under the strict evidence reading, D H1 drops to 9: it cited mostly `file:line`, and its only section ID was DEF-1, which is real but not a controlling section for H1. Every D session again read the full sources as well as SUMMARY.md, and five D answers explicitly flagged the summary's omissions. The aggressive summary therefore again did not cause a missed condition. Combined with the three Stage 4 runs, the pre-registered E-over-D hypothesis remains **not supported** on condition coverage.

### Contamination review, provenance and disclosures
1. **Tool access:** all six runs were CLEAN under the pre-registered review (`evidence/fresh-20261013/tool-access-review.txt`). No read outside the session or off the arm allowlist occurred, and no outside search returned content. Session folders held exactly the allowlisted files (`session-workspace-listing.txt`).
   - A had 7 denied attempts to search its parent folders; B and C had 1 each. All were blocked.
   - Five A sessions globbed Claude Code's own per-session auto-memory folder. It was permitted, every one returned "No files found", and no content was obtained.
2. **Unsuccessful attempt:** the first launch was rejected by the runner before any session started, because native Python cannot see the MSIX-virtualized CLI path. No call was made and the log is retained. The runs used the identical binary (same SHA-256) at its real path.
3. **Assessors:** four assessor subagents, two per packet, each reading only its blinded packet.
   - **Conflict:** they are the same model family as the tested model and as the orchestrating agent. They are not independent humans.
   - **Agreement:** the assessors agreed on 47 of 48 items. The one disagreement (A Q8, unsupported point) was adjudicated with a written reason. Assessor totals were official 177/176 and H 240/240.
   - **Evidence item:** the ambiguous evidence item was resolved in the plan before scoring. Primary means any real section ID used correctly; strict means a key-listed ID only. Both totals are reported.
4. **Recognisable arms:** A responses are recognisable by content, and several name their `A_FRESH…` folder. Five D responses name `SUMMARY.md`, and one B response cites `examples.md`. Responses were not edited.
5. **Limits:**
   - One round per arm in a fixed order (A, B, C, then C, D, E), so not counterbalanced.
   - Same machine and account, and user-level Claude Code configuration was inherited.
   - The server-side model revision is not observable, and temperature is not controllable.
   - These are same-day results on a small, near-ceiling benchmark, with no significance claimed.
6. **Not run:** G1–G4 (`evaluation/challenge/`) remain generated, non-independent and unexecuted. No external author was available, so no independent unseen questions exist.

## Corrected official v2 (executed 2026-10-13)

**Runs A_V2_01, B_V2_01, C_V2_01 · revision `ef44500` (pre-registered in `evaluation/v2-20261013/PLAN.md`) · Claude Code CLI 2.1.288 · observed model `claude-opus-5-5` in all 24 sessions · fresh sessions, identical flags, fixed order A→B→C · raw evidence committed (`c7afda4`) before scoring.**
- Questions are root `questions.md` v2, prompts in `control/prompts-v2/`. Q4 now states its own facts; the other seven prompts are byte-identical to v1.
- v2 is a separate evidence set. v1 Q4 scores are not reused.
- Evidence and run records: `evidence/v2-20261013/` (`RUN-RECORD.md`, `tool-access-review.txt`). Scoring files: `evaluation/v2-20261013/official/`.

| Arm | Score /80 | Strict evidence | Correct conclusions | False auth. | Critical omissions | Mean wall time |
|---|---|---|---|---|---|---|
| A — no folder | **14** | 14 | 0 / 8 | 0 | 8 (no policy access) | 13.1 s |
| B — specialist folder | **80** | 80 | 8 / 8 | 0 | 0 | 18.9 s |
| C — sources only | **80** | 80 | 8 / 8 | 0 | 0 | 15.3 s |

| | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 | Q7 | Q8 |
|---|---|---|---|---|---|---|---|---|
| A | 1 | 1 | 1 | 4 | 1 | 1 | 4 | 1 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |
| C | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |

- **Category scores** (conclusion/rules/exceptions/evidence/unsupported): every B and C answer scored 4/2/2/1/1.
  - A Q1, Q2, Q3, Q5, Q6 and Q8 scored 0/0/0/0/1. Each said the policy was unavailable, with no checkable answer.
  - A Q4 scored 2/1/1/0/1, capped at 4.
  - A Q7 scored 2/0/1/0/1, capped at 4.
- **Pairwise:** B vs A 8/0/0; C vs A 8/0/0; **B vs C 0/8/0**.
- With the self-contained Q4, B and C both answered Q4 fully. The v1 remark "could not see Q3's facts" no longer occurs.
- **Interpretation:** A/B shows the folder beats no folder, but A lacked the policy. B/C shows **no measurable benefit from the folder's structure beyond supplying the sources** on this question set, which is at ceiling.

## U1–U8: questions generated in a separate Claude session (executed 2026-10-13)

**Runs A_U_01, B_U_01, C_U_01 · same revision, CLI, model, flags and order as v2 · only each `prompt` field was sent · raw evidence committed (`c7afda4`) before scoring.**
- **Provenance:** per the supplied `AUTHORING-NOTE.md`, U1–U8 were generated in a separate Claude session (configured `claude-opus-5-5`) using only the six primary documents. They were not written by the folder's author session.
  - Independent human authorship, cross-model-family independence and moderator acceptance are **not** claimed.
  - The operator had seen the questions before running them, and the specialist was not changed.
- **Scoring** used the frozen rules in `evaluation/unseen-20261013/REVIEW-AND-RUN-PLAN.md`, committed before any run. These include the prospective U6/U8 "acknowledge both readings" criterion and the U8 24-hour-notice clarification.
- Evidence and run records: `evidence/unseen-20261013/`. Scoring files: `evaluation/unseen-20261013/scoring-U_01/`.

| Arm | Score /80 | Strict evidence | Correct conclusions | False auth. | Critical omissions | Ambiguity deductions | Mean wall time |
|---|---|---|---|---|---|---|---|
| A — no folder | **8** | 8 | 0 / 8 | 0 | 8 (no policy access) | 0 | 13.6 s |
| B — specialist folder | **77** | 77 | 8 / 8 | 0 | 1 (U8 branch) | **3 (U8)** | 21.7 s |
| C — sources only | **80** | 80 | 8 / 8 | 0 | 0 | 0 | 22.6 s |

| | U1 | U2 | U3 | U4 | U5 | U6 | U7 | U8 |
|---|---|---|---|---|---|---|---|---|
| A | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| B | 10 | 10 | 10 | 10 | 10 | 10 | 10 | **7** |
| C | 10 | 10 | 10 | 10 | 10 | 10 | 10 | 10 |

- **Category scores:**
  - Every A answer scored 0/0/0/0/1: the policy was unavailable and no answer was given.
  - B U8 scored 2/2/1/1/1.
  - Every other B and C answer scored 4/2/2/1/1, with every subpart correct.
- **Pairwise:** B vs A 8/0/0; C vs A 8/0/0; **B vs C 0/7/1 (the folder lost U8)**.
- **The loss (B U8, 7/10):**
  - **What B got right:** travel-office approval is required, manager approval was obtained, the approved-vendor branch is correct, the neither-approved-nor-prohibited branch is correct, and a prohibited vendor with no authorization must not proceed.
  - **What it missed:** for an airline that is prohibited but holds written compliance-officer authorization, it stated the restrictive reading (EMG-1 plus VEN-3: no waiver, so advance finance approval is needed) as settled. It never gave the textually supported permissive reading (EMG-2: waiver applies, plus a 24-hour finance notice).
  - **Scoring:** the frozen criterion required both readings, so this is an **ambiguity-related deduction of 3**. It is not a false authorization, because the advice is more cautious than either reading requires.
  - **C U8:** stated the permissive reading in its table and the restrictive reading in a note, and scored 10. On U6, which tests the same tension, B and C both gave both readings and scored 10. A had no policy text.
- **Possible cause (not established):** the folder's rule 8 ("Vendor restrictions are checked independently of every other exception") and its README index line ("Vendor restrictions survive other exceptions") may push toward the restrictive reading. One run cannot separate this from run-to-run variation.
- **What changed in the folder because of it: nothing.** The specialist is frozen for these unseen tests. Tuning it after seeing U1–U8 would invalidate them. A candidate change for a future, separately tested revision is a rule that, when provisions conflict, both readings must be stated with their consequences. That revision would need new unseen questions.
- **Interpretation:** on questions the folder's author did not write, the folder again beats no folder (source availability). Against sources alone it tied 7 and lost 1. There is **no evidence of an advantage from the folder's structure**.

## Disclosures for v2 and U1–U8
1. **Contamination review** (`scripts/review_fresh_captures.py`): all six runs CLEAN.
   - Session folders contained exactly the allowlisted copies (A 0, B 80, C 48 per set), and nothing outside them was read.
   - A: 7 (v2) and 8 (U) denied searches of its parent run folder, all blocked. It also made 5 (v2) and 1 (U) permitted searches of Claude Code's own per-session auto-memory folder, all of which returned "No files found".
   - B and C: no denials.
2. **Failures and retries:** none. All 48 sessions completed on the first attempt with exit code 0 and empty stderr.
3. **Assessors:**
   - Two blinded assessor subagents per set, each given only its packet; the U-series assessors also received the verbatim frozen rules.
   - **Conflict:** the assessors are the same model family as the tested model, the U-question author and the orchestrator.
   - **Agreement:** 23 of 24 items in each set. Assessor totals: v2 A 15 vs 14, B and C 80/80; U B 77 vs 79, A and C identical.
   - **Adjudication** (in writing, in the adjudicated files):
     - v2 A Q4 was capped at 4, because it left open an emergency override of the vendor ban (the key's disqualifying mistake).
     - U8 B was scored 7, because the rubric awards conclusion 4 only to fully correct answers.
4. **Recognisable arms:** A answers are recognisable by content, and several name their `A_V2_01` or `A_U_01` working folder. B and C answers carried no identifying paths in either packet.
5. **Limits:**
   - One round per arm in a fixed order (not counterbalanced), on the same machine and account, with inherited user-level Claude Code configuration.
   - The server-side model revision is not observable, and temperature is not controllable.
   - Small question sets near ceiling; no statistical significance is claimed.
   - G1–G4 remain generated and unexecuted.
