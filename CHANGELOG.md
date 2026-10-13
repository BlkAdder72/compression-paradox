# Release repair changelog — 2026-10-13

Input: latest `compression-paradox.zip` attachment exposed by the referenced chat. SHA-256: `0622f1ba2ad322f218ac32117fb6ca0cc6c1a4f24f817ea3cdf238d84f16855d`. Original HEAD: `4392931`. Original archive and synced project sources were not modified.

1. Restored lowercase `results.md` from Git and moved uppercase report unchanged to `history/RESULTS-original.md`. Retained history without rewriting. Checked unique case-folded paths and clean tree.
2. Enforced LF for ordinary text; preserved raw/historical bytes. Added explicit UTF-8 reads and ran offline guards.
3. Replaced unsafe runners with portable Python capture and Bash wrappers: no overwrite, source allowlists, timeout/failure preservation, result validation and metadata/checksums. Dry-preflighted all arms, checked shell syntax and added regression tests. Test stubs are not model evidence.
4. Audited stored checksums, scored result records and arithmetic. Reconciled root results with imported A/B rerun; corrected 48-versus-32 C/E response count and stale Stage 3 status. Original score files and historical reports retained.
5. Added four generated, explicitly non-independent, unexecuted questions; external-author protocol; capture and blinded-packet kit. No new model results or external authorship claimed.
6. Rewrote prerequisites, core.autocrlf guidance, fresh-run commands and limits.

See the accompanying verification report for executed checkout, history, script, evidence and ZIP checks. See `RELEASE-READINESS.md` for unresolved external gates.
