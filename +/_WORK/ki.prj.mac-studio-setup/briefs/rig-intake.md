# rig-intake - shape RIG-INTAKE for the retained Rig capability lines

Work: ki.prj.mac-studio-setup (KI > Rig > Mac Studio setup), package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/`.

## Task

`messages.md` in the package holds nine retained Rig capability lines routed here: RIG-APP-FOOTPRINT (IMPORTANT), RIG-COMMENT-KIND, RIG-NOTIFICATIONS (two lines), RIG-MACHINE-MANAGEMENT, RIG-CLI-CONSISTENCY, WAKE-SUBSTRATE, RIG-TUI, RIG-SSH-CHECK and RIG-REMINDER-DOCTOR. Read each line and anything it links to, then read the tools-rig roadmap (`/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/`) to find existing records that already cover each need (for example shipped `rig remove`, KI-TOOL-RIG-CORE-053, KI-TOOL-RIG-CORE-067).

For each line propose one disposition, grouping lines that are the same capability:

- fold into an existing tools-rig record (name it);
- capture as an unadopted tools-rig triage record under `ki-next` (Kris has asked for RIG-TUI and RIG-SSH-CHECK as idea records explicitly);
- hold under BURN-DOWN (Kris, 14 October: "burn the roadmap down; no new feature records"), stating the release;
- return to its sender, with the reason.

Weigh BURN-DOWN against Kris's explicit requests in the lines themselves. Write the result as one owner query, RIG-INTAKE, in the `ki-coordination` owner-report query shape (Context, Query, lettered Options, recommended first with confidence and reason), plus a per-line disposition table.

## Bounds

Read-only everywhere. Do not create, edit or commit any tools-rig record, and do not edit `messages.md`, `queries.md`, `decisions.md` or `state.md`. Your only write is the report below. No sudo, no `rig apply`, no system change. Never stash, rebase, reset, force-push or use `--no-verify`.

## Report

Write your run report (Done, In Progress, Queries) to `/Users/krisbrown/.local/state/ki/agents/ki-prj-mac-studio-setup/rig-intake.report.md`; the launcher homes it in the work package. Commit nothing.
