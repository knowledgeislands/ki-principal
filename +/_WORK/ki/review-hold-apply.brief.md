# review-hold-apply

Apply Kris's REVIEW-HOLD answer of 19 October, option a), to the six work folders in `+/_WORK_REVIEW/`. The live-or-dead assessment is in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/review-hold.report.md`.

1. Move ki.agent-host, ki.estate-factorisation and ki.paperclip-capture-and-rebuild from `+/_WORK_REVIEW/` back to `+/_WORK/` as on-hold packages under `ki-work-package`. Each `state.md` must say `state: on-hold`, with the reason, the release and the since time. Fix any links the move breaks.
2. Copy the two items that exist only in the old ki.baseline-rollout (CHECKLIST, and the `update-ki-pin.yml` payload-field mismatch) into `## Parked` in the live `+/_WORK/ki.baseline-rollout/queries.md`. Each gets its tag, one line of context and its recommended option.
3. Delete the old ki.baseline-rollout and ki.regular.command-centre from ki-principal's `+/_WORK_REVIEW/`.
4. Delete ki.regular.skill-reviews from ki-agentic-harness's `+/_WORK_REVIEW/`, but first fetch and confirm on the remote that its record was accepted and pruned. If you can't confirm it, leave that folder in place and raise a query.

Commit separately in each repository.

## Rules

- CAPTURE-GATE (Kris, 19 October): create no roadmap record except one this brief names. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Commit only your own changes, staged by explicit path under `ki-git`, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". Do not push. If another session has uncommitted changes in a file you need, leave that file alone and name it in your report.
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query needs Context, Query and Options, with a) recommended and its confidence.
