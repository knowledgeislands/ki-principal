# mgit-accept - accept and prune in tools-mgit and tools-git-almanac

## Goal

In /Users/krisbrown/workspaces/knowledge-islands/tools-mgit and /Users/krisbrown/workspaces/knowledge-islands/tools-git-almanac:

- list every roadmap record that is Awaiting review or Done;
- ki-accept each Awaiting review record whose verification evidence is recorded;
- prune the Done records;
- push each repository.

Leave KI-TOOL-MGIT-CLI-017, KI-TOOL-MGIT-CLI-024 and KI-TOOL-MGIT-CLI-025 alone, because Ways of working accepts them. Change nothing about KI-TOOL-MGIT-CLI-018 or -019, which wait on Kris's MGIT-PLAN answer.

## Boundaries

- Kris's approval, 18 October, relayed by Ways of working (ACCEPT-PRUNE): "anything which is awaiting acceptance can be accepted, and then we can prune anything which is in a state of done". Accept under `ki-accept` only a record whose verification evidence is recorded in the record; list any without evidence and leave it alone. Prune Done records under `ki-work-roadmap`, in a prune-only commit.
- Before starting, check for another session working in the repository: an uncommitted tree, a rebase or merge in progress, or commits newer than 30 minutes. If you find one, stop and report it.
- Ways of working is moving every repository to the latest dependencies and rumdl 0.3.0 (run estate-deps), so expect `package.json` commits. Fetch, then pull with rebase before each push. Push fast-forward only; never force-push, use `--no-verify` or rewrite history. Stage by explicit path. Commits use Conventional Commits and end with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- No code changes, no release, tag or version bump, and no remote branch delete. Do not touch tools-ki.

## Report

Write the run report to /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/mgit-accept.report.md under the current ki-coordination and ki-delegation run-report form: the heading with the run name, a glyph-state form line, Done, In Progress and Queries, Needs tags for queries, and no reply block. List each record accepted, pruned or skipped, with its full identifier and a link. Do not commit the report; the coordinator commits it.
