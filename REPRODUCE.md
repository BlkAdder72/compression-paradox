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
