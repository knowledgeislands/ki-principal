# triage-review brief

Work: ki.mac-studio-setup, [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Supervisor: the coordinator of ki.mac-studio-setup. Last mark 23:36 BST on 19 October.

## Task

Give one independent, read-only review of the disposition of these tools-rig roadmap records: KI-TOOL-RIG-CORE-053, KI-TOOL-RIG-CORE-056, KI-TOOL-RIG-CORE-057, KI-TOOL-RIG-CORE-064, KI-TOOL-RIG-CORE-067, KI-TOOL-RIG-CORE-068, KI-TOOL-RIG-CORE-069 and KI-TOOL-RIG-DIST-011, all under `/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/`. For each, decide: adopt into Now, Next or Future; cancel; merge into another record; or move it out of Rig to a named owner. Give a confidence and a one-line reason.

Form your own view from the records, the specifications, the code and the ki-work-roadmap rules first. Only then read the two proposals, which disagree in places, and say for each record whether you agree with either:

- `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/rig-triage.report.md` (its Queries, including any query on KI-TOOL-RIG-CORE-066).
- `/Users/krisbrown/.local/state/ki/agents/tools-burndown/acceptrig.report.md` (cancel DIST-011, merge 056 into 053, reject 057 and 064 from Rig). One finding to test: roadmap-census-2 says DIST-011's hold is about to be met by KI-PRINCIPAL-GOV-035, the Techne focus that brings vega back into scope, so it may not be obsolete.

Standing context: Kris wants triage burned down, tools burn-down first, no roadmap cap and no new records (CAPTURE-GATE, BURN-WAVE-1, TRIAGE-ALL, 19 October).

## Limits

Read only. No edits, commits, remote calls, tests that write, sudo, `launchctl`, `pfctl`, `rig apply` or `chezmoi apply`.

## Report

Write status lines, each `HH:MM BST - <step>`, to `~/.local/state/ki/agents/mac-studio-setup/triage-review.status`, ending with `DONE`, `FAILED` or `BLOCKED`. Write the report to `~/.local/state/ki/agents/mac-studio-setup/triage-review.report.md` as a run report: the heading `# [Rig](...) › [Mac Studio setup](...) › triage-review`, the form line, then Done (one line per record: your disposition, confidence, reason, and agree or disagree with each proposal), In Progress and Queries (one RIG-TRIAGE query in Context, Query and Options form, with a recommended a) and its confidence, plus one for any query on KI-TOOL-RIG-CORE-066), then the banner.
