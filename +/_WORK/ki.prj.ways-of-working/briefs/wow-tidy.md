# Brief: wow-tidy

Work: ki.prj.ways-of-working, package `+/_WORK/ki.prj.ways-of-working/` in ki-principal. Tidy under the `ki-work-package` "Tidying the work folder" rules and `ki-coordination` pruning at a mark. Delete by explicit path, with `git rm` for tracked files and `rm` with literal paths for untracked ones:

- every report at the package root and under `reports/` whose outcome has a durable home (a record, `decisions.md`, a design note or a commit) and whose queries are in `queries.md`;
- every brief under `briefs/` whose run has finished and been received. Keep `briefs/*.packet.md` only if a review is still pending, and keep the briefs of runs still running or queued (`ki agent status ki-prj-ways-of-working`).

Never touch these three files: `public-report-review.report.md`, `sol-private-report-assessment.report.md` and `reports/z-session-retirement-20261030.md`. Keep design notes. Do not move anything into a new layout, because LAYOUT-SHAPE is undecided. List each deletion and its home in your report.

Then close the stale runs `ways-of-working-reg` and `ways-sol-resume-20261029` with `ki agent close <run>`. If a blocker remains, report it. Commit by explicit path, subject `docs(work): ki.prj.ways-of-working tidy at window start`, and push fast-forward only.
