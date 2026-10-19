# skill-reviews-delete

Kris approved deleting `ki-agentic-harness/+/_WORK_REVIEW/ki.regular.skill-reviews/` on 19 October (REVIEW-HOLD a)). `review-hold-apply` found that the local `origin/main` ref, last fetched at 23:22 BST that day, already contains the GOV-193 acceptance `c0924316`, the prune `b7f35cdf`, and the pushed commits `a830b6ed` and `58d41ccc`. No GOV-193 file remains on that ref. State of play accepts this local ref as the confirmation, so do not fetch.

1. Check those four commits are on the local `origin/main`. If any of them is missing, stop and raise a query.
2. Repoint line 22 of `docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md` to a GitHub link pinned to the last commit where the folder's `decisions.md` existed.
3. Delete the folder, and remove its line from the `+/_WORK_REVIEW/` README index.
4. Make one commit in ki-agentic-harness. Do not push.

## Rules

- CAPTURE-GATE (Kris, 19 October): create no roadmap record. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Commit only your own changes, by explicit path on the commit command, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". Do not push.
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries.
