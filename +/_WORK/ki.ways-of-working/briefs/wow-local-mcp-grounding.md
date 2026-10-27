---
work: ki.ways-of-working
run: ways-of-working
agent: wow-local-mcp-grounding
written_at: 2026-10-27T03:23:41.123633+00:00
---

# Task: ground current MCP/tool delivery against existing local symlinks, without a release cycle

Kris explicitly says on 27 October 2026: "you don't need to release any of the tools because you've got access to them all locally because they're all simlinked ... You should be able to get all of the tool changes bedded down, you should be able to get all the MCP changes bedded down." The read-back is LOCAL-SYMLINKS and OBSERVATORY-HOME in ki-principal/+/_WORK/ki.ways-of-working/decisions.md. Current autonomy permits confident parts; no release, tag or publication cycle is needed. This run is a SMALL READ-ONLY grounding unit and must not become another estate audit.

Exact primary checkouts under /Users/krisbrown/workspaces/knowledge-islands:

- mcp-acquire-whatsapp
- mcp-git-audit
- mcp-gsuite
- mcp-housekeeping-chatgpt
- mcp-housekeeping-claude
- mcp-ki-kb-fs
- mcp-m365

Only inspect these seven repositories and their already-declared local execution bindings; relevant binding skills may explain how to read non-secret command/path fields. Do not dump configs, environment, credentials or token values. Do not invoke provider tools, list external data, mutate bindings, restart servers/daemons, install/upgrade, run MCP auth flows, fetch/push or publish. Current tools-ki/rig work is reserved by quick-wins, tap-log and opener-reboot; do not duplicate their work or tests.

Read only concise current status/roadmap/work state as needed. Identify current committed or dirty implementation changes and unresolved local branches, resolve the existing symlink/declared local command path, and distinguish direct source execution from generated dist that actually needs rebuilding. Do not run builds, test suites, app audits or broad history scans. Inspect only meaningful currently-unintegrated commit ranges if necessary, not every old branch. A local symlink observation is not evidence a provider operation succeeded; state this accurately without making remote calls.

Return a short per-repository observation: local source is already the executable path, a precise remaining local delivery requirement, or cannot determine from available safe evidence. If any already-authorised current change still needs work, give an exact bounded next unit with allowed paths, original authority, true prerequisites and one sufficient targeted verification. Remove release-cycle assumptions from the analysis, not from arbitrary records. Do not revive ideas/held/future records, accept work, invent policy, author new work records or change repository content. If no additional implementation is warranted, say so without commissioning another check. Report blockers and useful confident partials only; no new owner choices unless essential.

Do not use background subagents. Never end session while waiting.

**Report** to `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-local-mcp-grounding.report.md`, in the run's state folder and nowhere else, as an owner report: the ki-coordination report heading of the work you report to with `› <run name>` added, `# [<Theme>](<local theme page>) › [<Project>](<local Project note>) › <run name>`, the bold `**🤖 → 👤 Handoff to supervisor · Run report at <local time> · last mark <local time>**` line, adding `· blocked` after the state where you send back with a blocking query, and one `---`, then `## Done`, `## In Progress` and `## Queries`, each query carrying **Context**, **Query** and lettered **Options** as separate paragraphs with a blank line between them, each option its own paragraph, `a) (recommended, confidence <level> - <reason>)` first, no bullets and no reply block; where the brief asks for findings, add `## Findings` between `## In Progress` and `## Queries`, each finding a `### <TAG> - <title>` heading opening with its **Goal**, **Scope** and **As of** lines before any table, and write it also to the finding file the brief names; then, for coordinating work, the glyph banner the ki-coordination [Banner](../../../change-management/ki-coordination/references/standards-coordination.md#banner) section prints, its `###` state heading, counts line and `- [state] what · holder · since` list, closing with one thread line, `🧵 Coordination thread · <label> (<id>)` for Project work or `🧵 State of play thread · <label> (<id>)` for territory work, using the work you report to, and no send or resume line; a run report to a conversational session or ad hoc work has no mark in its form line and no banner. The report's first non-blank line is its `#` heading, after front matter if the report has any. Run tools quietly under the ki-coordination [quiet-tools rule](../../../change-management/ki-coordination/references/standards-coordination.md#quiet-tools): run Git with `-q`, never paste gate, audit or Git output, and report each outcome in one line. Owner reports, run reports and banners omit routine push state and other sessions' stacked commits; if your own unit could not be published because its push failed, Done names the affected unit and reason. A hold report keeps nothing about pushes beyond a failure.

Temporary output goes in <temporary>/, outside every repository; never remove it yourself, ki agent close empties and removes it, so home what must survive first. Write nothing into `+/_WORK/ki.ways-of-working/` beyond your report.

Do not use background subagents. Never end your session while waiting.
