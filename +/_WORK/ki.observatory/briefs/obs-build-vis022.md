# obs-build-vis022: build overdue-against-schedule

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Record: [KI-OBSERVA-VIS-022](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md>), Ready (3b3c785). Acted on overnight under OVERNIGHT: RIG-SCHEDULE a), reviewed high (obs-review-7 agreed).

1. Build the record as planned: schedules from `rig show --format json`, strict parsing of the `calendar:` and `interval:` encoding, 2-hour grace after the most recent scheduled run, the 26-hour fallback with its reason shown for anything unparseable, disabled jobs not judged overdue.
2. Correct the record where it calls the whole source a specified stable contract: the declaration values are specified (RIG-STATE-033, RIG-CONF-016), but the schedule string's encoding is implementation evidence only, which the strict parser and the visible fallback bound. Note that a specification handoff to tools-rig has been requested.
3. Fix the stale `RIG_UNAVAILABLE` text in packages/evidence/src/machine.ts, which still says Rig has no JSON output.
4. Run tests, typecheck, lint, contract checks, the browser smoke check and the roadmap audit. Do not restart or stop the live service (AGENTS.md); say in the report that a restart is due for Kris.
5. Move the record to Awaiting review with its Review section. Commit by explicit path, conventional subjects, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Do not push.

Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-build-vis022`, the bold form line, `---`, Done, In Progress, Queries. British English, ASCII hyphens only.
