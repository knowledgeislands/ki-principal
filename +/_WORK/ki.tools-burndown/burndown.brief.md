# burndown - roadmap burndown push

Repositories: /Users/krisbrown/workspaces/knowledge-islands/tools-ki, /Users/krisbrown/workspaces/knowledge-islands/tools-mgit and every MCP server repository: mcp-acquire-whatsapp, mcp-git-audit, mcp-gsuite, mcp-housekeeping-claude, mcp-ki-kb-fs, mcp-ki-kb-notion-mirror, mcp-m365 under /Users/krisbrown/workspaces/knowledge-islands. Work package: /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown.

Kris agreed (19 October, via ki.ways-of-working, BURNDOWN-PUSH): prune every record that is done under `ki-work-roadmap`; bring every record awaiting review to Kris as one acceptance batch; and cancel or merge triage records, aiming for at least half, each with a one-line reason, for Kris to confirm before anything is cancelled. Report the net count before and after.

1. Count each repository's records by status first (`ki work`).
2. Prune every done record under `ki-accept`'s prune rules and `ki-work-roadmap`'s done-before-prune commit boundary, one commit per repository by explicit path. In tools-ki the cli155 and wpreader runs are writing now: never touch KI-TOOL-KI-CLI-155, -149, -150, -152 or any record created today, stage only your own paths, and retry on an index lock.
3. Acceptance batch: for every Awaiting review record, one line each with what was delivered, its verification and any known limit, so Kris can accept them together. Change nothing.
4. Triage proposal: for every triage record, cancel, merge into <id>, or keep, with a one-line reason; aim for at least half cancelled or merged. Change nothing; each proposal becomes a query.
5. Report the before and after counts per repository and in total, after the prunes and as they would stand once the proposal is confirmed.

Work under ki-delegation and ki-git: commit your own changes by explicit path, never push, tag, publish or delete a remote branch, never use --no-verify. Write your report to /Users/krisbrown/.local/state/ki/agents/tools-burndown/burndown.report.md in the ki-coordination owner-report shape (Done, In Progress, Queries with Context, Query and lettered Options, a) recommended with confidence); put the acceptance batch and the triage proposal each in one query whose options let Kris accept all, accept with named exceptions, or decline. Raise a blocking query in the report and stop rather than guess.
