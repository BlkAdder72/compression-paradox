# External checks — 2026-10-13

## Competition #14 rules and deadline — PENDING (not identified)
- The repository, its history and every local copy (`compression-paradox-*`, `Astra Review`) contain no URL and no rules or deadline text: a grep for `http(s)://` and for deadline/rules terms found nothing.
- Web searches run (US web search, 2026-10-13):
  - `"Compression Paradox" competition #14 Claude specialist folder`
  - `ICM "Interpretable Context Methodology" competition 14 rules deadline`
- Neither search returned a page identifying this competition. Results concerned unrelated compression research, compression benchmarks and the COMAP MCM/ICM modeling contest, none of which matches.
- No URL, requirement or deadline is asserted. **The user must supply the authoritative rules link.**

## Public GitHub repository — UNVERIFIED / not published
- `git remote -v` is empty in this repository and in every local copy. The `gh` CLI is not installed, and no GitHub authentication is available.
- Unauthenticated GitHub REST commit search (`https://api.github.com/search/commits?q=hash:<sha>`) returned:
  - `df36e7d29dcfc73b4a2cc25aa25434c62bcba2d8` (pre-registration): total_count 0
  - `4392931a5893848a5ed22b55ab3a1886b7d3de73`: total_count 0
  - `c12af4a4843ed14e152ec183dd1b1daf444740bc` (received release): total_count 0
- Commit search covers only indexed public default branches, so 0 results is not proof of absence.
- Repository-name search `compression-paradox in:name` returned three unrelated repositories: `MagnetonIO/time-compression-paradox`, `Hybos/compression-energy-paradox` and `Princelab-paradox/AI_compression`. None contains this history.
- Nothing was pushed or published. Publication needs the user's explicit authorization and target URL.

## External unseen-question author — PENDING (not available)
No genuinely external person was accessible in this session. A subagent does not qualify, so none was used as an author. G1–G4 remain generated, non-independent and unexecuted.

## Case-sensitive filesystem
- Linux was not available: the only WSL distribution is Docker Desktop's internal `docker-desktop`, which is stopped.
- Used instead: a genuinely case-sensitive NTFS directory (`fsutil file setCaseSensitiveInfo <dir> enable`; the attribute was confirmed on the directory and inherited by clone subdirectories).
- Probe: `x.probe` and `X.PROBE` coexisted as two distinct files.
- Fresh clones of `c12af4a` and `eee0f20` passed every check there. Historical commit `4392931` checked out with both `RESULTS.md` and `results.md` present.
- This is Windows NTFS per-directory case sensitivity, not a Linux filesystem, and not a change to `core.ignorecase`.
