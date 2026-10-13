> Current state (2026-10-13): root `questions.md` is v2 (self-contained Q4). Corrected v2 and U1–U8 have been run (A/B/C_V2_01, A/B/C_U_01) and scored; see `results.md`. All older Q-series captures and scores are v1 (`history/questions-v1.md`); reproduce them with `--suite legacy`. v2 is a post-results correction, not original pre-registration.

# Reproduce and audit Competition #14

## Actual prerequisites

- Git with full history and Python **3.10+**, standard library only, on PATH as `python`. No pip packages, jq, Node or SDK required. Bash is optional for the `.sh` wrappers.
- For real calls: installed authenticated Claude Code CLI, model entitlement, network access and quota. Imported records identify CLI 2.1.288 and `claude-opus-5-5`; current availability is not guaranteed. Check `claude --version` and authenticate with the installed CLI's documented login flow. Override with `--claude /absolute/path/to/claude` and `--model IDENTIFIER`; disclose any change. Use a native executable on Windows. **Windows desktop-app CLI (MSIX):** the Claude desktop app is a Store package, so `%APPDATA%\Claude\claude-code\<ver>\<id>\claude.exe` is visible to Git Bash through package virtualization, but not to native Python. `run_trials.py` then stops with "Claude CLI unavailable". Pass the real path instead: `--claude C:/Users/<you>/AppData/Local/Packages/Claude_<publisher-id>/LocalCache/Roaming/Claude/claude-code/<ver>/<id>/claude.exe` (verify with `--version` and SHA-256).
- Clean committed checkout; never-used run IDs; separate writable absolute output and session directories outside the repository. Replace the example C:/paradox-* locations with user-owned paths as necessary. On Linux/macOS use appropriate absolute paths.
- Controlled CLI account/user configuration. Fresh directories are NOT OS isolation: parent instructions, inherited settings and permitted external reads can contaminate sessions. Keep identical configuration/permissions and inspect every tool trace. Hidden prompts, temperature and server model revisions may not be controllable.
- Human evaluation using the frozen rubric and key. Capture success does not establish a score, external authorship or provider authenticity.

## Fresh clone and line endings

The release ZIP includes `.git`, retaining the full supplied history. Clone from its extracted repository:

```text
git clone --no-local -c core.autocrlf=false /absolute/path/to/extracted/compression-paradox /absolute/path/to/fresh-checkout
```

For an actual public repository, substitute its verified URL; none is known here. From the fresh checkout:

```text
git config core.autocrlf false
git status --porcelain
git fsck --full
python --version
```

Status must be empty. `.gitattributes` forces LF for ordinary text even with `core.autocrlf=true`; raw evidence and historical reports are `-text`. Never normalize transcripts or regenerate frozen prompts. Historical commits retain the old case collision; on Windows inspect their blobs with `git show COMMIT:PATH` rather than checking out conflicting trees. HEAD has exactly one root `results.md`.

## Offline checks (no model calls)

```text
python scripts/verify_submission.py
python scripts/verify_stage3.py
python scripts/preflight_stage4.py
python scripts/verify_control_capture.py
python scripts/audit_evidence.py
python scripts/test_runner.py
```

The audit checks stored checksums, scored capture result records and arithmetic, not independent grading or authenticity. `verify_fixture.py` and `prepare_control.py` are historical Stage 1 tools that intentionally reject completed specialist folders at HEAD. `prepare_holdout.py` writes materials and is not a read-only gate.

## Fresh A/B/C

Dry-run validates inputs without invoking Claude or creating captures:

```text
python scripts/run_trials.py --arm A --run-id A_FRESH_20261013_01 --workspace C:/paradox-sessions --output C:/paradox-captures --dry-run
```

With real authenticated access, run:

```text
python scripts/run_trials.py --arm A --run-id A_FRESH_20261013_01 --workspace C:/paradox-sessions --output C:/paradox-captures
python scripts/run_trials.py --arm B --run-id B_FRESH_20261013_01 --workspace C:/paradox-sessions --output C:/paradox-captures
python scripts/run_trials.py --arm C --run-id C_FRESH_20261013_01 --workspace C:/paradox-sessions --output C:/paradox-captures
```

A receives no files; B gets ten specialist files; C gets six primary sources. All receive unchanged Q1-Q8 bytes, identical CLI flags and fresh sessions. C is necessary to separate architecture from source availability. Predeclare repetitions/order and counterbalance subsequent rounds (e.g. C/B/A). Never reuse historical IDs, especially A_REPRO_1/B_REPRO_1.

The runner refuses existing run directories, stops on failed exits/timeouts/incomplete result events, and retains raw stdout/stderr. Each output run folder contains manifests with prompt/source hashes, revision, CLI version, requested model, commands, timestamps/exits and checksums. COMPLETE_UNGRADED only means structurally completed captures. Review actual model IDs, outside reads and denials; disclose/exclude contamination. Commit raw evidence before grading. Retain every failed attempt.

Grade using `evaluation/scoring-rubric.md` and `evaluation/expected-answers.md`, preferably with blinded independent assessors; preserve category/per-question scores, disagreements, wins/ties/losses and provenance. Do not change scoring criteria after viewing results.

## Fresh H-series (not independent holdout)

```text
python scripts/run_trials.py --arm C --suite holdout --run-id CH_FRESH_01 --workspace C:/paradox-sessions --output C:/paradox-captures
python scripts/run_trials.py --arm D --suite holdout --run-id DH_FRESH_01 --workspace C:/paradox-sessions --output C:/paradox-captures
python scripts/run_trials.py --arm E --suite holdout --run-id EH_FRESH_01 --workspace C:/paradox-sessions --output C:/paradox-captures
```

Use `evaluation/holdout/expected-answers.md`, the original rubric and disclosed H-series false-authorization mapping. H1-H8 are post-analysis questions. The new runner excludes all historical raw/manifest files from sessions. Its output layout differs from legacy runners; do not pass new captures to the old `verify_stage4_capture.py`.

## Generated challenge and external unseen author

See `evaluation/challenge/PROTOCOL.md` for exact G-series run and blinded-packet commands and the external-author procedure. G1-G4 are generated, unexecuted and NOT independent. No external authorship or new Claude scores are claimed.

## Optional Bash wrappers

Set PYTHON_BIN, CLAUDE_BIN, MODEL, RUN_ID, SANDBOX_BASE and OUTPUT_BASE. `run_control_cli.sh` fixes A; `run_arm_cli.sh` uses ARM=B or C; `run_holdout_cli.sh` uses ARM=C, D or E. Old SRC_DIR/OUT_DIR examples are obsolete; direct Python commands are preferred on Windows.

## Corrected v2 execution and legacy reproduction

The default `--suite official` now selects `control/prompts-v2/`, including self-contained Q4. Original `control/prompts/` and its manifest are unchanged; their `question_source` describes the historical root location, now archived as `history/questions-v1.md`. Use `--suite legacy` to reproduce every existing Q-series score. Answer keys embedded in root questions.md are never sent to model sessions.

After committing v2 and starting from a clean checkout, use distinct run IDs:

```text
python scripts/run_trials.py --suite official --arm A --run-id A_V2_01 --workspace C:/paradox-v2-sessions --output C:/paradox-v2-captures
python scripts/run_trials.py --suite official --arm B --run-id B_V2_01 --workspace C:/paradox-v2-sessions --output C:/paradox-v2-captures
python scripts/run_trials.py --suite official --arm C --run-id C_V2_01 --workspace C:/paradox-v2-sessions --output C:/paradox-v2-captures
```

Use the frozen rubric and unchanged gold conclusions; grade new responses separately. Do not substitute old Q4 scores. All eight questions must be sent in the same order in each arm. Record that v2 was corrected after the folder existed. The historical v1 chronology is retained; do not claim v2 preceded original folder creation.

## Commands actually executed for v2 and U1–U8 (2026-10-13)

These were run from a fresh `git clone --no-local` of `ef44500`, a clean tree, on Windows 11 with Git Bash. `CL` is the native `claude.exe` at its real MSIX path (see "Actual prerequisites"); it is version 2.1.288.

```text
python scripts/verify_unseen.py
python scripts/run_trials.py --suite official --arm A --run-id A_V2_01 --workspace C:/paradox-v2-sessions --output C:/paradox-v2-captures --claude CL
python scripts/run_trials.py --suite official --arm B --run-id B_V2_01 --workspace C:/paradox-v2-sessions --output C:/paradox-v2-captures --claude CL
python scripts/run_trials.py --suite official --arm C --run-id C_V2_01 --workspace C:/paradox-v2-sessions --output C:/paradox-v2-captures --claude CL
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm A --run-id A_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures --claude CL
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm B --run-id B_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures --claude CL
python scripts/run_trials.py --suite challenge --questions evaluation/unseen-20261013/external-questions.json --arm C --run-id C_U_01 --workspace C:/paradox-u-sessions --output C:/paradox-u-captures --claude CL
python scripts/review_fresh_captures.py --sessions-root C:/paradox-v2-sessions evidence/v2-20261013/A_V2_01 evidence/v2-20261013/B_V2_01 evidence/v2-20261013/C_V2_01
python scripts/review_fresh_captures.py --sessions-root C:/paradox-u-sessions evidence/unseen-20261013/A_U_01 evidence/unseen-20261013/B_U_01 evidence/unseen-20261013/C_U_01
python scripts/prepare_v2_packet.py
python scripts/prepare_blind.py --questions evaluation/unseen-20261013/external-questions.json --run A=<abs>/evidence/unseen-20261013/A_U_01 --run B=<abs>/evidence/unseen-20261013/B_U_01 --run C=<abs>/evidence/unseen-20261013/C_U_01 --output <abs>/evaluation/unseen-20261013/scoring-U_01/packet
python scripts/score_v2_u.py disagreements
python scripts/score_v2_u.py summary
```

- Captures were copied byte-for-byte into `evidence/` and committed before the packets were built.
- To re-run, use new run IDs and empty workspace and output folders. The runner refuses existing IDs.
- A mod's re-run should match the pattern rather than exact text: A has no policy access, and B and C reach the key conclusions with section citations.
- Model output varies run to run, so exact wording and the U8 ambiguity handling may differ.
