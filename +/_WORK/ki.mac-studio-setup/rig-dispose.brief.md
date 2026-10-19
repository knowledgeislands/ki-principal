# rig-dispose brief

Work: ki.mac-studio-setup, [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Supervisor: the coordinator of ki.mac-studio-setup. Last mark 23:36 BST on 19 October. Authority: OVERNIGHT (Kris, 20 October 00:28 BST, act on high-confidence recommendations) and GOOD-STATE (local changes in tools-rig). Read `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/triage-review.report.md` for the reviewed dispositions.

## Task

Apply these roadmap dispositions in tools-rig under `ki-work-roadmap`, editing records only:

1. RIG-MANAGERS a): fold G2 of KI-TOOL-RIG-CORE-066 into KI-TOOL-RIG-CORE-067, keeping built-in and custom-provider availability and one actionable manager-level finding; narrow KI-TOOL-RIG-CORE-066's goal and boundary to the delivered G3 (uv from mise), leaving it at Awaiting review.
2. KI-TOOL-RIG-CORE-053 and KI-TOOL-RIG-CORE-067 adopted into Next.
3. KI-TOOL-RIG-CORE-068 adopted into Now for planning and evidence preparation only; implementation waits for Kris's attended NordVPN check and a tested restore path.
4. KI-TOOL-RIG-CORE-069 adopted into Now for diagnosis and planning, with no live handler change.
5. KI-TOOL-RIG-CORE-056 stays in Future, separate from 053. Do not touch KI-TOOL-RIG-CORE-057, KI-TOOL-RIG-CORE-064 or KI-TOOL-RIG-DIST-011.

Cite Kris's OVERNIGHT decision and the triage review in each record's log.

## Limits

- No sudo, `launchctl`, `pfctl`, `rig apply`, `chezmoi apply`, `duti` or other live machine or handler change. No push, no remote calls, no `--no-verify`, no force-push. `ki repo conform` only with `--dry-run`.
- Create no new roadmap records (CAPTURE-GATE); put anything new under Queries. Never self-accept.
- Leave `package.json`, `bun.lock`, `.husky/` and `.githooks/` unchanged. Leave any other session's changes alone and name them.
- Run the gates the change needs (`git diff --check`, `ki repo audit --repo .`, and for code the full Bats suite and shell gate); commit by explicit path, local only on `main`.
- Any query: Context, Query, Options, a recommended a) with confidence high, medium or low and a one-line reason.

## Report

Write status lines, each `HH:MM BST - <step>`, to `~/.local/state/ki/agents/mac-studio-setup/rig-dispose.status`, ending with `DONE`, `FAILED` or `BLOCKED`. Write the report to `~/.local/state/ki/agents/mac-studio-setup/rig-dispose.report.md` as a run report: heading `# [Rig](...) › [Mac Studio setup](...) › rig-dispose`, form line, Done, In Progress, Queries, banner.
