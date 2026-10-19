# Brief - ki-brew

Bring Homebrew's `ki` up to date on this machine for KI > Foundations > Baseline rollout (`ki.baseline-rollout`).

## Task

KI-BREW: run `brew update` and check the `ki` formula's version against the latest tools-ki release tag (`/Users/krisbrown/workspaces/knowledge-islands/tools-ki`). If the formula offers a newer `ki` than the installed one, run `brew upgrade ki` and confirm `/opt/homebrew/bin/ki --version`. Report whether tonight's hooks-migration release is already in the formula; if it is not, say so, and the worker will rerun this later. Upgrade nothing else.

## Authority

Kris, 2026-10-19 23:59 BST: "Anything high confidence can be done." It covers exactly the task above. Each territory's Capital keeps ownership: capture records as unadopted triage records under `ki-next` (and `ki-repo-kb-streams` where the repository keeps `Streams/Roadmap/`), following each repository's own AGENTS.md; adoption, priority and delivery stay with the receiving repository. No repository writes or commits; the only change is the Homebrew upgrade. The estate's Husky-to-`.githooks` migration runs tonight: never touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`, never run `ki repo conform` without `--dry-run`, and if a Git lock is held, wait and retry; name any other session's uncommitted files without touching them. Evidence for this wave: `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/report-wave1-sweep.md` and `report-wave1-audit.md` beside it, and the queries in `queries.md` there.

## Report

Return a run report in the `ki-coordination` run-report form: under Done one line per repository with each record or change, linked by absolute path, and its commit; any decision Kris must make as a query with a recommended option and confidence.
