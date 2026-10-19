# email-routing-hold

Kris answered LANE-OWNERS a) on 19 October: the 12 email-routing draft records in mcp-m365 and mcp-gsuite move to one hold until a Project opens to own them.

1. Find the email-routing records in each repository's `docs/roadmap/`.
2. Hold each one under `ki-next` and `ki-work-roadmap`, with the same hold condition on all of them: "until a Project opens to own email routing (LANE-OWNERS, Kris, 19 October)".
3. In your report, note that the work `/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/hnr.email-routing/work.md` exists. Do not write to it.
4. Commit once per repository.
5. If the count is not 12, or a record is already active with another session, leave that record alone and say so.

## Rules

- CAPTURE-GATE (Kris, 19 October): create no roadmap record except one this brief names. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Commit only your own changes, staged by explicit path under `ki-git`, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". Do not push. If another session has uncommitted changes in a file you need, leave that file alone and name it in your report.
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query needs Context, Query and Options, with a) recommended and its confidence.
