# Handoff to Codex — Competition #14 "Compression Paradox" verification (2026-10-13)

## Exact revisions
- **Received:** `c12af4a4843ed14e152ec183dd1b1daf444740bc`, from `compression-paradox-release-2026-10-13.zip` (SHA-256 `02d126059be7b9e7df05f8215bf898254d41996117f0dcc9da9cda8e2c5f8b58`).
- **Model runs executed at:** `9e79e0e981bb739c53b44c996cd0eca61782b1db`, the pre-registration commit, from a fresh `git clone --no-local` with a clean tree.
- **Final offline verification at:** `eee0f20caf4ae0cdceb761a3931ad3a018131b71`, checked in three fresh clones.
- **Returned HEAD:** the commit that adds this file and `verification/2026-10-13/`. It only adds logs and this handoff on top of `eee0f20`, and was re-checked in place. Run `git log -1` in the returned repository to see it.
- History was not rewritten. No existing run, transcript, failed attempt or historical report was modified or removed.

## Commits added (in order)
| Commit | Change |
|---|---|
| `02bb445` | fix: `results.md` is the only root results report. The annotated A_REPRO_1/B_REPRO_1 report moved to `history/REPRODUCTION-RESULTS-repair-annotated.md` (fixes a garbled sentence), and `verify_submission.py` guard added and tested against a planted file. |
| `7122334` | docs: Stage 3 README points to `results.md` (it referenced the removed `RESULTS.md`). |
| `9e79e0e` | prereg: `evaluation/fresh-20261013/PLAN.md` freezes run IDs and order, contamination rules, rubric/key hashes and the evidence-item interpretation. Also adds `evidence/** -text`. |
| `c810226` | `scripts/review_fresh_captures.py`: read-only tool-access and provenance review. |
| `64b3ca9` | Raw evidence of six fresh runs, tool-access review, session listing, run record and retained failed attempt. Committed **before scoring**. |
| `a941589` | `scripts/prepare_fresh_packets.py` and the two blinded packets with keys. |
| `07e2cbe` | Two assessors per set, disagreements, adjudication, and `scripts/score_fresh.py` summary. |
| `eee0f20` | `results.md` fresh section, `RELEASE-READINESS.md`, `CHANGELOG.md`, and the MSIX CLI path in `REPRODUCE.md`. |
| (HEAD) | `verification/2026-10-13/` logs and this handoff. |

## Fresh Claude tests — DONE
- **Runs:** A_FRESH_20261013_01, B_FRESH_20261013_01, C_FRESH_20261013_01 (official Q1–Q8), and CH_FRESH_01, DH_FRESH_01, EH_FRESH_01 (H1–H8). These are new runs, distinct from the imported A_REPRO_1/B_REPRO_1.
- **Execution:** CLI `2.1.288 (Claude Code)`, binary SHA-256 `84304f7d…0ab91`. Actual model `claude-opus-5-5` in all 48 init events and every assistant message. All exits 0, 48/48 success events, stderr empty.
- **Timing:** 19:13:18–19:29:42Z.
- **Records:** prompt and source hashes, revision, commands and timestamps are in each `evidence/fresh-20261013/<RUN>/manifest.json`.
- **Contamination:** all six runs CLEAN (`tool-access-review.txt`). Only allowlisted files were present and read. Outside attempts were denied (A: 7, B: 1, C: 1). Five A Globs of Claude Code's own empty auto-memory folders were permitted and returned nothing.
- **Failed attempt retained:** the first launch was rejected before execution, because the MSIX-virtualized CLI path is invisible to native Python (`logs/attempt0-cli-path-rejected.log`).

## Scores (frozen rubric; 2 blinded assessors per set; 47/48 items agreed; 1 adjudicated)
| Set | Arm | Total /80 | Strict evidence | False auth. | Critical omissions |
|---|---|---|---|---|---|
| Official | A | 16 | 16 | 0 | 8 (no policy) |
| Official | B | 80 | 80 | 0 | 0 |
| Official | C | 80 | 80 | 0 | 0 |
| H-series | C | 80 | 80 | 0 | 0 |
| H-series | D | 80 | 79 | 0 | 0 |
| H-series | E | 80 | 80 | 0 | 0 |

- **Pairwise:** B vs A 8/0/0; C vs A 8/0/0; **B vs C 0/8/0** (no architecture advantage beyond sources); H-series all 0/8/0.
- **Assessor conflicts and limits:** the assessors are the same model family as the tested model and the orchestrator. Arms are recognisable (A by content and folder name, D via `SUMMARY.md`, one B via `examples.md`).
- **Benchmark quirk:** Q4 refers to "the same facts as Q3" across independent sessions.
- Full details are in `results.md`, under "Fresh verification runs".

## Commands run and results (logs in `verification/2026-10-13/`)
- **Commands:** `python scripts/verify_submission.py`, `verify_stage3.py`, `preflight_stage4.py`, `verify_control_capture.py`, `audit_evidence.py` (238 → 340 hash entries), `test_runner.py` (5 tests), `test_blind_packet.py` (1 test), `score_fresh.py summary`, and `git fsck --full`.
- **Results:** all rc=0 on the received `c12af4a`, on fresh clones of `c12af4a` and `eee0f20` (default `autocrlf=true` and documented `autocrlf=false`), and in a case-sensitive directory.
- **Case-sensitive test:** Windows NTFS per-directory case sensitivity (`fsutil file setCaseSensitiveInfo`), not Linux. WSL had only the stopped `docker-desktop` distribution. The probe confirmed distinct `x.probe` and `X.PROBE` files, and historical `4392931` checked out both `RESULTS.md` and `results.md`.
- **Environment:** Windows 11 Pro 10.0.26300, Python 3.13.14, Git 2.55.0.windows.1, Git Bash.

## Rules, deadline and public repository
- **Official rules and deadline: PENDING.** Not identifiable from the repository, local files or web search (`verification/2026-10-13/external-checks.md`). **Need the authoritative URL from the user.** No requirement or deadline is assumed.
- **Public GitHub: UNVERIFIED / not published.** No remote, no `gh`, no authentication. Public commit search for `df36e7d`, `4392931` and `c12af4a` returned 0, and the three name matches are unrelated. Nothing was pushed. Comparing a published commit with the tested release requires the real URL and publication authorization from the user.

## Unresolved blockers
1. Rules URL, requirements and deadline with timezone: user input needed.
2. Public repository URL, publication authorization, and a signed-out accessibility check comparing the published commit with `eee0f20` or HEAD.
3. Independent unseen questions: no external author available. G1–G4 stay generated, non-independent and unexecuted.
4. Scientific limits:
   - Each set was run once in a fixed order, not counterbalanced.
   - The assessors are the same model family as the tested model.
   - Inherited user-level Claude Code configuration.
   - The provider's server revision is unobservable.
   - Small, near-ceiling benchmark.
