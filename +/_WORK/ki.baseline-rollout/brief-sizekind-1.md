# Brief - sizekind-1

Propose size and kind backfill for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), territories humans-not-robots, legal and personal.

## Task

SIZE-KIND, read-only: for every repository with a `.ki.toml` under `/Users/krisbrown/workspaces/humans-not-robots/`, `/Users/krisbrown/workspaces/legal/` and `/Users/krisbrown/workspaces/personal/` (`dotfiles` is the chezmoi source at `/Users/krisbrown/.local/share/chezmoi`), list every open record missing `size` and every adopted open record missing `kind`, and propose each value under `ki-work-roadmap`'s rules with a short reason or an open uncertainty. One table per repository. Note dotfiles' records still naming `initiative`. Write nothing in any repository: this run only proposes; Kris confirms per repository before any write pass.

## Authority

Kris, 2026-10-19 23:59 BST: "Anything high confidence can be done." It covers exactly the task above. Each territory's Capital keeps ownership: capture records as unadopted triage records under `ki-next` (and `ki-repo-kb-streams` where the repository keeps `Streams/Roadmap/`), following each repository's own AGENTS.md; adoption, priority and delivery stay with the receiving repository. This run is read-only: no commits, no writes outside the run state folder. The estate's Husky-to-`.githooks` migration runs tonight: never touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`, never run `ki repo conform` without `--dry-run`, and if a Git lock is held, wait and retry; name any other session's uncommitted files without touching them. Evidence for this wave: `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/report-wave1-sweep.md` and `report-wave1-audit.md` beside it, and the queries in `queries.md` there.

## Report

Return a run report in the `ki-coordination` run-report form: under Done one line per repository with each record or change, linked by absolute path, and its commit; any decision Kris must make as a query with a recommended option and confidence.
