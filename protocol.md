# Frozen experimental protocol v1.0

## Registered question and source design
The question set, source fixture, expected answers, rubric, and protocol must be committed before control or treatment execution. Check the git log. This initial commit does **not** include a specialist folder. The six fixture files are benchmark artifacts, not files loaded into the no-folder control.

## Official arms
- **A, no-folder control:** a fresh model session without specialist folder, reference files, answer key, and without access to the repository. Submit Q1–Q8 **exactly** as written, in the listed order, using separate fresh sessions per question. Save complete unedited raw records including exact prompts and any system/developer messages exportable through the interface, tool calls, timestamps, refusals, errors, and retries. Do not silently restart failures.
- **B, treatment:** same model identifier, settings, tool availability and session isolation; only difference is the specialist's files (identity.md, rules.md, examples.md, README.md, reference/). Submit precisely the same Q1–Q8 with no extra hints. Preserve raw records as above.

**Model pin caveat:** Model names/aliases may not fix server weights. Record provider, named model, revision/version if available, interface, sampling parameters if adjustable, date/time, and all observable tool permissions. If any are unavailable, state 'unavailable', not guessed. Repeat runs if feasible; substantial model drift weakens reproducibility claims.

## Why two kinds of controls matter
Official A/B tests whether the *whole folder, including its sources*, helps compared with no folder. It does NOT isolate compression architecture, because the treatment has facts absent from A. Label this confound prominently in results.

## Supplementary arms, not replacements
**C, source-only:** give the same six full fixture documents with no specialist identity/rules/examples/navigation. This isolates the incremental benefit of specialist structure, subject to differing delivery mechanics.
**D, aggressive summary:** specialist with short rule summaries and all original primary sources still accessible.
**E, index-first:** specialist navigational index pointing to primary sections and dependencies, plus all original primary sources.
Predefine the exact variants and commit them before running comparative diagnostics; do not tune against the scored questions. Publish raw transcripts of every variant and the modifications introduced. Optional holdout questions should be independently authored, committed before run, and identified as later tests.

## Outcomes
Primary metric: 0–80 rubric score, plus question-by-question wins, ties, losses. Secondary metrics: omission count, false permission, unsupported claims, latency (measured only), and actual source file access (only if logs available). Also disclose cases where A correctly expresses uncertainty because it lacked policy access. Avoid claiming the model internally attended to a provision. Individual trials are not statistically independent if shared context is used; use independent sessions.

## Integrity and storage
Never replace or clean raw outputs. Append reruns with their own IDs. Preserve the exact model output and tool traces. Each run manifest must specify git SHA, source exposure, test question SHA256, model/settings, date, and raw transcript filenames. If access to genuine model runs is unavailable, leave transcript directories empty and report **not run** rather than generating imitations. Results must label every unexecuted arm **pending**.
