# obs-build-app046: make the browser smoke check green

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Record: [KI-OBSERVA-APP-046](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-046-browser-smoke-check-red.md>), at triage. Acted on overnight under OVERNIGHT: the causes are diagnosed, the change is to the check and its fixture only, and it unblocks KI-OBSERVA-VIS-041's Verify (high confidence, non-destructive).

1. Plan the record to Ready under the repository's ki-work-roadmap rules (priority now), using its proposed fix: reading time relative to the run's clock plus a deliberate stale check; the four missing reads for sessions, work, review and known-lands; the feedback read and the inline-handler wording allowed in the Mermaid step, keeping every containment check.
2. Build it. Change the smoke check and its fixture only; if a product change looks needed, stop and report it as a query instead.
3. Run `bun run self:test:browser` (full Chromium is installed) until it passes, plus tests, typecheck and lint. The smoke check uses its own loopback port: do not restart or stop the live service (repository AGENTS.md).
4. Move the record to Awaiting review with its Review section, and update KI-OBSERVA-VIS-041's Review line that cites it. Commit by explicit path, conventional subjects, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Do not push.

Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-build-app046`, the bold form line, `---`, Done, In Progress, Queries. British English, ASCII hyphens only.
