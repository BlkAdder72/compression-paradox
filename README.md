# THE COMPRESSION PARADOX — Competition #14

**Status: Stage 2 executed 2026-10-12 (arms A, B, C on Q1–Q8); Stage 4 executed 2026-10-12 (arms C, D, E on supplemental H1–H8, all 80/80). Each arm run once with `claude-opus-5-5`. See `RESULTS.md`.** (Stage 1 text below is unchanged.)

Research question: Can evidence-preserving context compression improve specialist navigation without hiding essential conditions? The official no-folder versus folder test measures the *combined* effect of supplying references and structure; a source-only supplementary arm is required to isolate architectural value.

The six `fixture/` documents define a self-contained **fictional** policy. Eight frozen questions are in `questions.md`; independent answers and scoring appear in `evaluation/`. The specialist folder is intentionally **not** created in Stage 1, because precommitting questions before building the folder is part of the competition.

## Ordered procedure
1. Inspect `questions.md`, policy fixture, gold answers, rubric and protocol. Run `python scripts/verify_fixture.py`. Commit the baseline BEFORE creating a specialist folder.
2. Run no-folder control in real model sessions and save **unedited** raw transcripts under `control/raw/` with a run manifest; commit.
3. Create `specialist/{identity.md,rules.md,examples.md,README.md,reference/}`. Copy fixture sources into `specialist/reference/`; design an index that points to evidence instead of substituting summaries. Commit before testing.
4. Run treatment under matching conditions and save unedited records to `treatment/raw/`; commit.
5. Score with original answer key, report ties, regressions and wins, then run source-only and optional ablations as **separate** diagnostics. No model runs or measured wins are claimed by this Stage 1 package.

## Avoid deceptive interpretation
The no-folder control lacks the private fictional policy, so an A/B improvement alone does **not** prove architectural superiority. A source-only diagnostic is central to testing the Compression Paradox hypothesis. This benchmark is small and makes no claim of statistical significance.

## Stage 3 diagnostic preparation

Aggressive-summary and index-first ablation variants and eight supplemental post-analysis challenge questions have been frozen, with offline verification in `scripts/verify_stage3.py`. They were **run in Stage 4** (see `RESULTS.md`). Do not interpret these as reproduction or performance evidence. See `diagnostics/README-stage3.md`.
