# Brief - va-plan

Close the apps-vallearmonia.com planning gaps for KI > Foundations > Baseline rollout (`ki.baseline-rollout`).

## Task

In `/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com`:

1. Run `ki-plan` on the four drafts VA-WEBSITE-CONT-005, VA-WEBSITE-SANC-009, VA-WEBSITE-SANC-008 and VA-WEBSITE-SITE-004 in `docs/roadmap/`, adding their missing sections (Current state, Files touched, Dependencies / blocks, Documentation impact, and for SITE-004 Steps and Verify). Keep every record a draft: approval to Ready is Kris's.
2. Separately, repair VA-WEBSITE-SITE-003, keeping it awaiting review: complete its missing execution sections, review fields and final Discussion only from evidence you can find in Git history and the repository; never invent completion, and report any evidence you cannot recover.

## Authority

Kris, 2026-10-19 23:59 BST: "Anything high confidence can be done." It covers exactly the task above. Each territory's Capital keeps ownership: capture records as unadopted triage records under `ki-next` (and `ki-repo-kb-streams` where the repository keeps `Streams/Roadmap/`), following each repository's own AGENTS.md; adoption, priority and delivery stay with the receiving repository. Commit your own work in each repository by explicit path under `ki-git`, one Conventional Commit per repository, ending with the trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; never push. The estate's Husky-to-`.githooks` migration runs tonight: never touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`, never run `ki repo conform` without `--dry-run`, and if a Git lock is held, wait and retry; name any other session's uncommitted files without touching them. Evidence for this wave: `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.baseline-rollout/report-wave1-sweep.md` and `report-wave1-audit.md` beside it, and the queries in `queries.md` there.

## Report

Return a run report in the `ki-coordination` run-report form: under Done one line per repository with each record or change, linked by absolute path, and its commit; any decision Kris must make as a query with a recommended option and confidence.
