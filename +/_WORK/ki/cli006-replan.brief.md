# cli006-replan

For ki.agent-host, as CLI006-PLAN a), high, taken under Kris's OVERNIGHT authority of 20 October. Under `ki-plan`, re-check the 12 October plan of `tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md` against the current tools-techne and ki-techne-harness sources, including the host-patching work accepted since then, as the plan itself asks. Bring the plan up to date in the record, and leave it ready for Kris's review. Do not set it to Ready, and implement nothing. Record the outcome in `ki-principal/+/_WORK/ki.agent-host/decisions.md` in one line.

## Rules

- Do not push, and make no remote, GitHub-settings or host changes.
- CAPTURE-GATE (Kris, 19 October): create no roadmap record. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Other sessions are active. Leave alone any file another session has uncommitted changes in, and name it. Put explicit paths on the commit command itself.
- Commit only your own changes, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>".
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query gives Context, Query and Options, with a) recommended and its confidence.
