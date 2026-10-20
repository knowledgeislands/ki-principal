# obs-smoke-record: capture the red browser smoke check

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Acted on overnight under OVERNIGHT: SMOKE-RED a), high confidence, non-destructive.

obs-smoke-baseline (~/.local/state/ki/agents/observatory/obs-smoke-baseline.report.md) found that `bun run self:test:browser` fails on main and at 04a2ebb alike, with the full Chromium build too, in two places: dimming (every view still dimmed "once read" and "after refresh", the Beacon also on opening and after the scope change; sessions, work, review and known-lands report "the smoke check names no read for this view") and Mermaid (refused requests to `/api/feedback/draft` and `/api/knowledge-bases/asset`, a console 403, a content-policy refusal of an inline handler).

1. Read-only diagnosis: find the likely cause of each failure from the code and the smoke script, and, if cheap, when each started (`git log` of the smoke script and the code it exercises; no bisect that rewrites the tree).
2. Capture one triage record under the repository's ki-work-roadmap rules (reserve the ID as the repository requires), naming both failures, the evidence, the likely causes and a proposed fix, and noting that KI-OBSERVA-VIS-041's "browser smoke check passes" cannot be met until it lands. Link it from VIS-041's Review section in one line; do not change VIS-041's status.
3. Fix nothing in the code. Run the roadmap audit and Markdown lint; commit by explicit path with a `docs(roadmap):` subject and the trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Do not push.

Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-smoke-record`, the bold form line, `---`, Done, In Progress, Queries. British English, ASCII hyphens only.
