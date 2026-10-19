# plan069 brief

Work: ki.mac-studio-setup, [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Supervisor: the coordinator of ki.mac-studio-setup. Last mark 23:36 BST on 19 October. Authority: OVERNIGHT (Kris, 20 October 00:28 BST, act on high-confidence recommendations) and GOOD-STATE (local changes in tools-rig). Read `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/triage-review.report.md` for the reviewed dispositions.

## Task

Plan [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) to Ready under `ki-work-roadmap`. Diagnose from code, the cited reports and read-only observation only (for example reading Launch Services state; never writing a handler). Where the native interface cannot be verified without a live change, plan an attended step for Kris with its restore path and say so; if Ready cannot honestly be reached, leave it at draft and raise one query.

## Limits

- No sudo, `launchctl`, `pfctl`, `rig apply`, `chezmoi apply`, `duti` or other live machine or handler change. No push, no remote calls, no `--no-verify`, no force-push. `ki repo conform` only with `--dry-run`.
- Create no new roadmap records (CAPTURE-GATE); put anything new under Queries. Never self-accept.
- Leave `package.json`, `bun.lock`, `.husky/` and `.githooks/` unchanged. Leave any other session's changes alone and name them.
- Run the gates the change needs (`git diff --check`, `ki repo audit --repo .`, and for code the full Bats suite and shell gate); commit by explicit path, local only on `main`.
- Any query: Context, Query, Options, a recommended a) with confidence high, medium or low and a one-line reason.

## Report

Write status lines, each `HH:MM BST - <step>`, to `~/.local/state/ki/agents/mac-studio-setup/plan069.status`, ending with `DONE`, `FAILED` or `BLOCKED`. Write the report to `~/.local/state/ki/agents/mac-studio-setup/plan069.report.md` as a run report: heading `# [Rig](...) › [Mac Studio setup](...) › plan069`, form line, Done, In Progress, Queries, banner.
