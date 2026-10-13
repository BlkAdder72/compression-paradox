> **Status 2026-10-13:** corrected official v2 and separate-session U1–U8 were run with A/B/C and scored. See the headline at the top of `results.md`: v2 A 14 / B 80 / C 80; U A 8 / B 77 / C 80, where the folder lost U8 to sources-only. Raw evidence pointers are in `control/README.md` and `treatment/README.md`. Older sections below describe the v1 history.

# THE COMPRESSION PARADOX — Competition #14

**Current status (2026-10-12):** Official A/B completed; supplementary C and D/E experiments completed. Actual records, caveats and failures appear in [`results.md`](results.md). The original uppercase report is retained at `history/RESULTS-original.md`; `results.md` is the specification-required root report.

## What the folder does

The specialist interprets the six-document **fictional Meridian Works policy** by using compressed navigation as a pointer to primary rules, not a substitute for them. The required ICM files are in [`specialist/`](specialist/): `identity.md`, `rules.md`, `examples.md`, `reference/`, and `README.md`.

## What the experiment actually found

- Official no-folder A2: **11/80**; treatment B1: **80/80**. All 8 official questions improved, but this comparison is confounded: A lacked the policy source while B had it.
- Full-sources-only C1: **78/80**, also **8/8 correct operational conclusions**. The two treatment points above C were citation-format differences, not decision quality.
- Supplemental H-series, two runs each: **C 80/80 twice; D 80/80 then 77/80; E 80/80 twice**. All three variants made 8/8 correct decisions in both runs. The proposed condition-coverage advantage of index-first navigation was **not observed**.
- Excluded contaminated attempts DH2/EH2 remain preserved and documented. The H-series questions were not independently authored blind questions.

## Judge quick start

1. Confirm chronology with `git log --oneline --reverse`: benchmark frozen at `df36e7d`, control before specialist, treatment after.
2. Read [`questions.md`](questions.md), [`protocol.md`](protocol.md), [`evaluation/scoring-rubric.md`](evaluation/scoring-rubric.md), [`evaluation/expected-answers.md`](evaluation/expected-answers.md).
3. Read [`results.md`](results.md) for question-level wins, ties, losses, original and supplemental findings and exclusions.
4. Run `python scripts/verify_submission.py` and `python scripts/verify_stage3.py` to inspect static integrity. These are **not** model performance tests.
5. Follow [`REPRODUCE.md`](REPRODUCE.md) for a fresh, real Claude rerun, with a different run ID. Exact results are nondeterministic and not yet independently verified.

## Scientific limitations

A/B improvement cannot isolate context architecture; source-only provides the meaningful comparator. Limited A/B repetitions, same-family assessor, eight-question ceiling effects, different levels of source exposure, and model aliases limit inference. We report those limitations rather than claim that compression architecture independently improved accuracy.

## Release repair status (2026-10-13)

Offline repair and verification are separate from model execution. See [readiness and blockers](RELEASE-READINESS.md), [changelog](CHANGELOG.md), and the [generated challenge / external-author protocol](evaluation/challenge/PROTOCOL.md). Imported A/B rerun records score 11/80 and 80/80; no new Claude run occurred during this repair.
