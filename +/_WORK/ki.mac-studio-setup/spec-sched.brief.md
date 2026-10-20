# spec-sched brief

Work: ki.mac-studio-setup, [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Supervisor: the coordinator of ki.mac-studio-setup. Last mark 23:36 BST on 19 October. Authority: OVERNIGHT (Kris, 20 October 00:28 BST, act on high-confidence recommendations) and GOOD-STATE (local changes in tools-rig).

## Task

ki.observatory asks tools-rig to specify how `rig show --format json` encodes a resource's `schedule` string: `calendar:` and `interval:` prefixes, with several records joined by `;`. RIG-STATE-033 and RIG-CONF-016 cover the values and grammar but not this encoding. The Observatory record KI-OBSERVA-VIS-022 now parses it strictly, with a 26-hour fallback.

Read the code that produces `schedule`, then specify the encoding exactly as it is today, beside RIG-STATE-033 (or where the specs place JSON output), cross-referencing RIG-CONF-016. Add a fixture test that pins the encoding if none exists. Change no behaviour and add no structured field. Follow the repository's rules for spec changes; if they need a roadmap record, stop and raise one query instead of creating a record.

## Limits

- No sudo, `launchctl`, `pfctl`, `rig apply`, `chezmoi apply` or other live machine change. No push, no remote calls, no `--no-verify`, no force-push. `ki repo conform` only with `--dry-run`.
- Create no new roadmap records (CAPTURE-GATE). Leave `package.json`, `bun.lock`, `.husky/` and `.githooks/` unchanged. Leave any other session's changes alone and name them.
- Run `git diff --check`, `ki repo audit --repo .` and, if a test changes, the full Bats suite; commit by explicit path, local only on `main`.

## Report

Write status lines, each `HH:MM BST - <step>`, to `~/.local/state/ki/agents/mac-studio-setup/spec-sched.status`, ending with `DONE`, `FAILED` or `BLOCKED`. Write the report to `~/.local/state/ki/agents/mac-studio-setup/spec-sched.report.md` as a run report: heading `# [Rig](...) › [Mac Studio setup](...) › spec-sched`, form line, Done (naming the requirement identifier and commit so ki.observatory can cite them), In Progress, Queries, banner.
