# Stage 2 — Authentic no-folder control

**Status: PENDING actual Claude sessions.** This package contains no purported model output.

1. Use **the same Claude model and mode** planned for treatment. Record model display label, API model ID/revision if available, interface version, time zone, dates, temperature or unavailable, tools, and any other visible settings in `control/run-manifest.md`. Do not infer unavailable settings.
2. Start **eight fresh independent chats**, each without project knowledge or uploaded files, memory/custom context (to the degree controllable), or access to this repository. Do not add instruction text or hints. No external research tools should be enabled in either arm.
3. For each chat, paste the **exact contents** of `control/prompts/Q1.txt` through `Q8.txt` as the sole user prompt, in order. Do not paste the Q labels, answer key, or metadata.
4. Export/save the **complete, unedited** transcript for each chat to `control/raw/Q1.*` through `Q8.*`. If full exports are unavailable, preserve verbatim prompt/response together with the honest limitation in the manifest; never reconstruct omitted tool traces as though they were raw.
5. Record all failed calls, retries, refusals, and interruptions. Never select a 'best' run. Record capture filenames, SHA256 hashes, provider/interface, and model details.
6. Run `python scripts/verify_control_capture.py`, manually verify that each capture contains the exact question and real provider answer, then commit raw control evidence **before creating specialist/**.

**Integrity reminder:** the no-folder model has no access to the fictional Meridian Works policy. This measures folder-plus-source availability, not the incremental benefit of ICM structure. The supplemental source-only comparison is required for architectural interpretation.
