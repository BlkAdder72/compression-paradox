# Fresh run record — 2026-10-13 (new runs, not imported records)

These six runs were executed in this verification pass. They are distinct from the imported `A_REPRO_1`/`B_REPRO_1` records and from every earlier run. Pre-registration: `evaluation/fresh-20261013/PLAN.md` (commit 9e79e0e, made before any model call).

## Revision, tooling, environment
- Tested revision: **9e79e0e981bb739c53b44c996cd0eca61782b1db**. The runs used a fresh `git clone --no-local` of that commit with a clean working tree (the runner enforces this), recorded in every `manifest.json`.
- Runner: `scripts/run_trials.py`, unmodified. Command per session (from the manifests): `claude -p --model claude-opus-5-5 --output-format stream-json --verbose --tools Read,Glob,Grep --strict-mcp-config --no-session-persistence --permission-mode default`, with the exact prompt bytes on stdin. Prompt and source SHA-256 values are in each manifest.
- CLI: **Claude Code 2.1.288**, native Windows `claude.exe` bundled with the Claude desktop app (SHA-256 `84304f7d4b0cd0ebcbe8318695a260151b48991a6659c3366fdd5da290c0ab91`). Executable path: `C:/Users/mmazu/AppData/Local/Packages/Claude_pzs8sxrjxfjjc/LocalCache/Roaming/Claude/claude-code/2.1.288/36aa8c97bf86/claude.exe`. Authenticated with the user's claude.ai login.
- Model: requested `claude-opus-5-5`. **Actual model ID was `claude-opus-5-5` in every init event and every assistant message of all 48 sessions** (`tool-access-review.txt`). The server-side revision is not observable.
- Environment: Microsoft Windows 11 Pro 10.0.26300, NTFS. Python 3.13.14, Git 2.55.0.windows.1, run from Git Bash. Session workspace `C:/paradox-sessions-20261013`; raw output `C:/paradox-captures-20261013`. Both are separate roots outside the repository.

## Runs (planned order; one attempt each; all complete)
| Order | Run ID | Suite | Arm | Files per session | UTC start–end | Exits | Success events |
|---|---|---|---|---|---|---|---|
| 1 | A_FRESH_20261013_01 | official Q1–Q8 | A | 0 | 19:13:18–19:15:40 | all 0 | 8/8 |
| 2 | B_FRESH_20261013_01 | official Q1–Q8 | B | 10 | 19:15:41–19:18:45 | all 0 | 8/8 |
| 3 | C_FRESH_20261013_01 | official Q1–Q8 | C | 6 | 19:18:46–19:21:20 | all 0 | 8/8 |
| 4 | CH_FRESH_01 | holdout H1–H8 | C | 6 | 19:21:21–19:23:57 | all 0 | 8/8 |
| 5 | DH_FRESH_01 | holdout H1–H8 | D | 8 | 19:23:58–19:26:51 | all 0 | 8/8 |
| 6 | EH_FRESH_01 | holdout H1–H8 | E | 7 | 19:26:52–19:29:42 | all 0 | 8/8 |

Each run folder holds the unedited `Qn`/`Hn.stream.jsonl` (full tool traces), `.stderr.txt` (all empty), `manifest.json` and `SHA256SUMS.txt`. The copies here were checksum-verified against the originals and are byte-identical.

## Unsuccessful attempt (retained)
- **Attempt 0, 19:12:33–19:12:36Z.** All six invocations were rejected by the runner before any session started: "Claude CLI unavailable; no model execution performed". No directory, capture or model call was created (`logs/attempt0-cli-path-rejected.log`).
- **Cause:** the desktop app is an MSIX package. The path `%APPDATA%\Claude\claude-code\...\claude.exe` is visible to Git Bash through package file-system virtualization, but native Python cannot see it. The identical binary (same SHA-256) lives at the real path given above.
- Because nothing was created, the run IDs were still unused and were reused for attempt 1 (`logs/attempt1-runs.log`). This is a deviation from the plan's `_02` retry naming, which was written for runs that had started.

## Contamination review (before scoring)
`scripts/review_fresh_captures.py` → `tool-access-review.txt`. **All six runs: CLEAN.** No session read any file outside its own folder or off its arm's allowlist, and no outside search returned content. `session-workspace-listing.txt` hashes every file present in every session folder: A 0, B 80, C 48, CH 48, D 64, E 56, exactly the allowlisted copies.
- **Permission denials:**
  - A: 7 in 6 sessions. These were Glob of the run folder `C:/paradox-sessions-20261013/A_FRESH_20261013_01` and one Grep of `C:/paradox-sessions-20261013`, searching for the policy.
  - B Q4 and C Q4: 1 each, a Glob of their run folder.
  - H-series: none.
  - All attempts were blocked.
- **Notes (not violations):** in A Q1, Q2, Q3, Q5 and Q6 the model ran a Glob on Claude Code's per-session auto-memory folder `C:\Users\mmazu\.claude\projects\C--paradox-sessions-20261013-A-FRESH-20261013-01-Qn\memory`. Claude Code permits this by default, and every one returned "No files found" (new, empty folders). No information was obtained.
- **Inherited configuration (disclosed, not isolated):** user-level Claude Code settings, plugins and skills were present, as listed in each init event, as in all earlier runs. Directory separation is not OS isolation.

## Status
Raw evidence was committed before any assessor packet was built. Scoring is recorded separately in `evaluation/fresh-20261013/`.
