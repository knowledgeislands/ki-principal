# Brief: receive-sol

Work: ki.prj.ways-of-working (KI > Model > Ways of working), package `+/_WORK/ki.prj.ways-of-working/` in ki-principal.

Goal: receive four unreceived run reports at the package root into the package, so the coordinator can put their queries to Kris.

1. Read `sol-finish-line-plan.report.md`, `sol-host-sync-design.report.md`, `sol-private-report-assessment.report.md` and `sol-state-machine-readiness.report.md`.
2. Copy every query each report raises, in full (Context, Query, Options with the recommended option first and its confidence), into `queries.md` under `## Open`, keeping the tags; where a tag already exists under Parked (for example HOST-SYNC), place the new query beside it and say in its Context which parked query it refines. Do not change or remove existing queries.
3. The report `sol-private-report-assessment.report.md` concerns private material: copy only what the report itself states; do not open, quote or expose any protected payload.
4. Add one query AMEND-RACE under `## Open` from this message line, with Context, Query and Options (recommended first, with confidence): "in the shared hnr-principal checkout a run amended `HEAD` after another package's explicit-path commit had landed, so `a1d61be4` became `21f4f02b` under the amending run's subject and trailer (tree identical, nothing lost). Proposed rule for ki-git: in a shared checkout, amend only after confirming `HEAD` is your own commit, or never amend." Read `ki-git` in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/` to ground the options; change no skill.
5. Write a short report `reports/receive-sol.report.md`: one line per received report giving its outcome and whether its outcome has a durable home elsewhere, and the list of tags added.

Writes: `queries.md` and your report only. Do not edit `state.md`, `decisions.md`, `messages.md` or the four source reports, and do not delete anything. Commit `queries.md` and your report by explicit path, subject `docs(work): ki.prj.ways-of-working receive sol reports`, and push fast-forward only; stop on divergence. British English, ASCII hyphens only.
