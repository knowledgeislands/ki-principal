# wow-harness-coord - write tonight's coordination and delegation decisions into the harness

Work in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness. Read /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md entries dated 2026-10-24 and 2026-10-25 for Kris's exact answers; each is read back as taken and that read-back is your specification. Read /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unattended-work.md and /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/method-lines.md for the design behind them.

Carry these into the ki-coordination standard (skills/change-management/ki-coordination/references/standards-coordination.md), its output-style source, hooks/coordinator-reminder.sh, the rubric and ki-delegation, wherever each belongs:

- COMMIT-CADENCE and PACKAGE-PUSH: the standing push rule (push everything stacked on main, other sessions' commits included, fast-forward only, never forced, never --no-verify, stop on divergence), replacing the own-commits-only rule; commit the work package after every finished change and sync at least every 15 minutes while work runs; Kris's words that uncommitted package changes block pulls and pushes.
- SUMMARY-WINDOW, THREAD-RENAME (harness half), FINDINGS-SECTION, QUERY-RULES, DRAIN-END, COORD-COMMANDS, METHOD-NUDGE (the stale-method warning in the hook), REVIEW-CHECK (extend COORD-11), THEME-CLOSE (checker failure date 7 November 2026).
- RUN-SECRETS, Cloudflare half only: ki-delegation and ki-repo-website-cloudflare.
- The unattended-window decisions: WINDOW-CLOCK (end recorded as local time with zone and UTC), DENY-LIST, WINDOW-PLAN, CONFLICT-RUN, PROGRESS-SCOPE, RETURN-FORM.
- DECISION-HOMES: home PRFLOW in the harness AGENTS.md.
- COORD2-RUBRIC: the remaining label check near coordination.ts:372, if that file is in this repository; if it is in tools-ki, do not touch tools-ki and say so in the report.

Then run `ki dev skill generate ki-coordination --write`, and any other generator the changed skills need, and run the repository's tests and checks until they pass. Commit in coherent units. Do not touch ki-work-package or ki-work-roadmap: wow-harness-model follows you and owns those.

## Authority and rules

Kris granted an unattended window tonight, recorded in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md (the 25 October entries from 01:07 GMT on), ending 09:00 GMT. Within it you may edit, commit and push fast-forward only. Never force-push, never use `--no-verify`, no release, no DNS, Cloudflare or GitHub settings change, and no standard or configuration change beyond what Kris's logged answers decide. Stage by explicit path only; never commit, revert or stash another session's files. After every commit: `git pull --ff-only` then push. If the pull cannot fast-forward, follow CONFLICT-RUN as decided: in your own worktree, rebase only this run's unpublished commits, verify, and stop on another session's content, uncertain ownership or a judgement call. Anything needing Kris becomes a query in your report (tag, Context, Query, Options with a) recommended carrying its confidence and reason), not a guess. Stop starting new steps at 08:45 GMT. Write the report in the ki-coordination owner-report shape, closing with the banner and the line `🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)`. British English, ASCII hyphens only.
