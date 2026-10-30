# Brief: receive-landscape

Work: ki.prj.ways-of-working (KI > Model > Ways of working), package `+/_WORK/ki.prj.ways-of-working/` in ki-principal.

1. Read the landscape run report at `/Users/krisbrown/.local/state/ki/agents/ki-prj-ways-of-working/landscape.report.md`. Copy its five queries (ORCH-NAME, ORCA-REACH, AGENT-HOME, WAKE, WORKTREE-OPTOUT) in full, Context, Query and Options with the recommended option first and its confidence, into `queries.md` under `## Open`, each with a `since 2026-10-30 · from run/landscape` line. Change no existing query.
2. The report says its research notes `vendor-landscape.md` and `skills-inventory.md` are in the run's temporary folder. Find them (look under `/Users/krisbrown/.local/state/ki/agents/ki-prj-ways-of-working/`, the run's launch and log files, and `/tmp` or `$TMPDIR` paths the run used); if found, copy them into `design/landscape-vendors.md` and `design/landscape-skills-inventory.md` and link both from `design/landscape.md`'s sources. If not found, say so.
3. Write a short run report.

Writes: `queries.md`, the two new design files and the link line in `design/landscape.md` only. Commit by explicit path, subject `docs(work): ki.prj.ways-of-working receive landscape`, push fast-forward only; stop on divergence. British English, ASCII hyphens only.
