# Supplementary diagnostic arms — predefined before execution

| Arm | Definition | Status |
|---|---|---|
| C, source-only | Working directory contains exactly the six `fixture/` files (byte-identical, same filenames), nothing else. No identity, rules, examples or index. Same runner flags, model, CLI version and session strategy as A and B (`scripts/run_arm_cli.sh`, `SRC_DIR=fixture`, run ID `C1`). Raw output: `diagnostics/source-only/raw/`. | defined; to be run |
| D, aggressive summary | defined in Stage 3 (`diagnostics/README-stage3.md`) | H-series run DH1 executed (Stage 4) |
| E, index-first | defined in Stage 3 (`diagnostics/README-stage3.md`) | H-series run EH1 executed (Stage 4) |

C is not tuned against the scored questions: it uses the frozen fixture unchanged.
