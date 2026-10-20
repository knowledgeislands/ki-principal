# review027 brief

Work: ki.mac-studio-setup, [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Supervisor: the coordinator of ki.mac-studio-setup. Last mark 23:36 BST on 19 October.

## Task

Give one independent, read-only review. [KI-TOOL-RIG-CLI-027](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.md) is at Awaiting review (commit `66c9c57`). Its Outstanding concerns name three small gaps: `rig status` accepts a repeated `--profile`, `--problems`, `--unmanaged` or `--retired` (last wins) although RIG-PORT-014 says a repeated option exits 2; `remove`'s `--format` pre-scan; and `--sudo` missing from the guide and manual `apply` synopses. Verify each from the code, spec and docs.

Decide how they should be handled: capture a new Triage record (note the CAPTURE-GATE rule: runs create no records, and the coordinator creates one only for a blocker, a defect seen failing or Kris's request); fix them as a follow-up commit within KI-TOOL-RIG-CLI-027 before acceptance; or leave them as recorded concerns. Weigh whether each gap is a defect against the record's own acceptance criteria. Give one recommendation with confidence high, medium or low and a one-line reason.

## Limits

Read only. No edits, commits, remote calls, tests that write, sudo, `launchctl`, `pfctl`, `rig apply` or `chezmoi apply`.

## Report

Write status lines, each `HH:MM BST - <step>`, to `~/.local/state/ki/agents/mac-studio-setup/review027.status`, ending with `DONE`, `FAILED` or `BLOCKED`. Write the report to `~/.local/state/ki/agents/mac-studio-setup/review027.report.md` as a run report: heading `# [Rig](...) › [Mac Studio setup](...) › review027`, form line, Done, In Progress, Queries (one Q-027-REPEATS query in Context, Query and Options form, a recommended a) first), banner.
