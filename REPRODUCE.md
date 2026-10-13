# Reproduce the Projects UI comparison

The current UI evidence is A_UI_01/B_UI_01/C_UI_01; the CLI commands below reproduce a separate interface and evidence set. Hosted UI/model behavior can change. The committed inputs are the reproducible artifact; exact future wording is not guaranteed.

1. Clone the public repository with full history. Read the frozen UI plan, input-manifest.json and KNOWLEDGE-IMPORT.md under evaluation/projects-20261013. Run the offline checks below.
2. Create three new private Claude Projects in A/B/C order. No project descriptions or extra instructions. Turn account-memory sharing off; confirm empty project memory. A receives no files, B the ten unchanged specialist files, C the six fixture sources only. Never import questions, golds, assessments or the whole repo.
3. Match the observed import method: Add text content for each UTF-8 file, original contents unchanged (CRLF may normalize to LF). B titles are specialist-relative paths; C titles are fixture-relative filenames. Verify each form value against its source and save title/content hashes. Verify B has ten and C six files.
4. For each arm, start a new chat for each Q1,Q2,Q3,Q5,Q6,Q7,Q8. Set displayed Opus 5.5 Medium / Manual, turn Memory off every time (it resets), leave Research and external connectors off. Save settings and disclose residual tool availability. Send only the exact `prompt` string from evaluation/seven-20261013/questions.json.
5. After each response finishes, expand visible tool disclosures and save the complete response article and main DOM, exact prompt, chat URL, displayed model and timestamps. If interrupted, retain the attempt and recover the same chat; never silently regenerate. UI timestamps include observation delay and do not measure inference speed.
6. Check empty project memory afterward. Commit raw captures before grading. Apply the unchanged scoring rubric and golds, record assessor exposure and item rationales; disclose the Q6 timing issue in results.md. Independent blinded review is preferable; this submission used one unblinded Codex assessor.

The submitted UI run used separate clean projects to avoid contamination, not add/remove in one previously used project. B/C used text import, not a binary folder upload. Browser switching, A Q1 recovery, and visible-access limits are in evidence/projects-20261013/COMPLETION.md. Do not present this adaptation as exact literal walkthrough compliance.

UI verification:
```text
python scripts/verify_projects.py
python scripts/score_projects.py --check
```
The first validates all 21 captures and frozen/imported inputs. The second binds score arithmetic to pre-assessment commit 5f52b52. Neither certifies provider internals or semantic grading. CLI/session durations below must not be attributed to the UI runs.

---

# Reproduce the separate CLI seven-question benchmark

The default official suite is now exactly Q1,Q2,Q3,Q5,Q6,Q7,Q8 from root questions.md. It sends prompt text only. Expected answers and the JSON gold fields never enter model sessions. The existing seven-run scores come from new A/B/C_SEVEN_01 captures, not recalculated earlier results.

## Actual prerequisites

- Git with full history and Python **3.10+**, standard library only, on PATH as `python`. No pip packages, jq, Node or SDK required. Bash is optional for the `.sh` wrappers.
- For real calls: installed authenticated Claude Code CLI, model entitlement, network access and quota. Imported records identify CLI 2.1.288 and `claude-opus-5-5`; current availability is not guaranteed. Check `claude --version` and authenticate with the installed CLI's documented login flow. Override with `--claude /absolute/path/to/claude` and `--model IDENTIFIER`; disclose any change. Use a native executable on Windows. **Windows desktop-app CLI (MSIX):** the Claude desktop app is a Store package, so `%APPDATA%\Claude\claude-code\<ver>\<id>\claude.exe` is visible to Git Bash through package virtualization, but not to native Python. `run_trials.py` then stops with "Claude CLI unavailable". Pass the real path instead: `--claude C:/Users/<you>/AppData/Local/Packages/Claude_<publisher-id>/LocalCache/Roaming/Claude/claude-code/<ver>/<id>/claude.exe` (verify with `--version` and SHA-256).
- Clean committed checkout; never-used run IDs; separate writable absolute output and session directories outside the repository. Replace the example C:/paradox-* locations with user-owned paths as necessary. On Linux/macOS use appropriate absolute paths.
- Controlled CLI account/user configuration. Fresh directories are NOT OS isolation: parent instructions, inherited settings and permitted external reads can contaminate sessions. Keep identical configuration/permissions and inspect every tool trace. Hidden prompts, temperature and server model revisions may not be controllable.
- Evaluation using the frozen rubric and key, with assessor identity and conflicts disclosed. Capture success does not establish a score, external authorship or provider authenticity.

## Public clone and line endings

```text
git clone -c core.autocrlf=false https://github.com/BlkAdder72/compression-paradox.git
cd compression-paradox
git status --porcelain
git fsck --full
python --version
```

Start from a clean committed checkout. .gitattributes enforces LF for editable text even with core.autocrlf=true; raw evidence and historical files retain their bytes. Never normalize captures. Old commits retain the historical RESULTS.md/results.md case collision; inspect their blobs with git show instead of checking out those conflicting trees on case-insensitive Windows. Current HEAD has only root results.md.

## Offline checks — no provider calls

```text
python scripts/verify_submission.py
python scripts/verify_stage3.py
python scripts/preflight_stage4.py
python scripts/verify_control_capture.py
python scripts/verify_unseen.py
python scripts/verify_seven.py
python scripts/audit_evidence.py
python scripts/test_runner.py
python scripts/test_blind_packet.py
python scripts/score_seven.py --check
```

These validate structure, chronology, exact prompt/gold identity, frozen inputs, checksums, arithmetic and runner behavior. They do not independently grade answers or authenticate a provider. The current seven-prompt/gold check compares directly against df36e7d, before original control and specialist. Historical verify_fixture.py and prepare_control.py intentionally reject completed specialist folders at HEAD; they are not current release gates.

## Fresh official A/B/C calls

The paths below are examples; choose separate writable absolute session/output locations outside the repository. Use NEVER-USED run IDs; the runner refuses an existing capture/session directory. On Windows, provide --claude with the native executable path if claude is not on PATH. Confirm the model and disclose any substitution.

```text
python scripts/run_trials.py --suite official --arm A --run-id A_SEVEN_RECHECK_01 --workspace C:/paradox7-sessions --output C:/paradox7-captures --dry-run
python scripts/run_trials.py --suite official --arm A --run-id A_SEVEN_RECHECK_01 --workspace C:/paradox7-sessions --output C:/paradox7-captures
python scripts/run_trials.py --suite official --arm B --run-id B_SEVEN_RECHECK_01 --workspace C:/paradox7-sessions --output C:/paradox7-captures
python scripts/run_trials.py --suite official --arm C --run-id C_SEVEN_RECHECK_01 --workspace C:/paradox7-sessions --output C:/paradox7-captures
python scripts/review_fresh_captures.py --sessions-root C:/paradox7-sessions C:/paradox7-captures/A_SEVEN_RECHECK_01 C:/paradox7-captures/B_SEVEN_RECHECK_01 C:/paradox7-captures/C_SEVEN_RECHECK_01
```

A receives zero files, B the ten frozen specialist files, C the six primary sources. Each question starts a fresh session; same prompt bytes and listed order in every arm. Review all access traces and actual model IDs. An automated REVIEW flag requires a documented disposition before grading; do not silently relabel or discard it. Retain failures and excluded attempts; retry only under a new ID with the reason recorded. Predeclare order/repetitions and account configuration. Raw completion is not a score. Commit new captures before evaluation.

## Evaluate new responses

Use the unchanged per-question rubric with the seven gold rows in questions.md: 10 points each, maximum 70. The old frozen rubric's 80-point total describes its original eight questions. Never infer a score from capture success. Record categories, rationale, critical omissions, false authorizations, timing and question-level comparisons. Prefer blinded independent review when available and disclose what actually occurred; this submitted seven-run round used one unblinded Codex assessor as frozen in its plan.

A shuffled packet can be built from completed current runs using:

```text
python scripts/prepare_blind.py --questions evaluation/seven-20261013/questions.json --run A=C:/paradox7-captures/A_SEVEN_RECHECK_01 --run B=C:/paradox7-captures/B_SEVEN_RECHECK_01 --run C=C:/paradox7-captures/C_SEVEN_RECHECK_01 --output C:/paradox7-grading/RECHECK_01
```

Give graders packet.md and the rubric, withhold mapping.json, and disclose recognizable answers. Do not overwrite existing assessment files. score_seven.py validates the committed seven-run scores only; it does not grade new captures. Model output, hypothetical-date comments and exact totals may vary.

## Historical and supplementary suites
| Suite | Questions | Status |
|---|---|---|
| official (default) | Seven original IDs, excluding Q4 | Current submitted benchmark |
| official-v2 | Eight corrected Q prompts, including self-contained Q4 | Historical; originally called official before this revision |
| legacy | Eight original v1 prompts, including dependent Q4 | Historical |
| holdout | H1–H8 | Post-analysis, not independently authored |
| challenge --questions evaluation/unseen-20261013/external-questions.json | U1–U8 | Separate-session Claude authorship; earlier completed runs |

Use new IDs for every rerun. The G-series challenge remains generated, unexecuted and non-independent. Historical exact commands are archived in history/REPRODUCE-before-seven.md; their old --suite official selected eight questions then. Today use --suite official-v2 to reproduce that selection. Frozen v2 and U manifests' UNEXECUTED labels describe their freeze-time state, not current progress. The seven input manifest likewise records the pre-call freeze and must not be edited after execution.

See evidence/seven-20261013/RUN-RECORD.md for actual new commands, revision, source exposure and access disposition. All earlier raw material and full Git history are preserved. Original separate-key placement, post-results seven-item selection and CLI interface remain disclosed; no command can retroactively change chronology or promise moderator acceptance.
