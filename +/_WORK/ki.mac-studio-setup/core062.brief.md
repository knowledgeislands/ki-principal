# core062 brief

Work: ki.mac-studio-setup, [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md). Supervisor: the coordinator of ki.mac-studio-setup. Last mark 23:36 BST on 19 October.

## Task

Deliver [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) in tools-rig to Awaiting review under `ki-work-roadmap`, taking it from draft through Ready. Kris decided on 2026-10-20 at 00:16 BST: "Q-062-SCOPE/ABSENT proceed with recommendation", which means:

- Q-062-SCOPE a): the own-address destination with no interface match. State the remaining targeted case, which includes TCP as well as UDP, in the specification, ADR-KI-TOOL-RIG-009 and the firewall guide. Word "tailnet-only" so it does not promise authenticated Tailscale ingress. Keep the advice to turn Screen Sharing off on untrusted shared networks.
- Q-062-ABSENT a): when apply cannot find the Mac's own tailnet address, report `unknown` with `tailnet-address-undiscoverable` and install or rewrite nothing.

Record both answers in the record's queries, then deliver the plan as written: paired IPv4 and IPv6 discovery, refusal on ambiguous discovery, stale-address reporting, isolated fixture tests, and the specification, ADR, guide, help and changelog updates the plan names. Write in the record that any live rollout is attended at the screen and carries the tested SSH rollback and restore path from KI-TOOL-RIG-CORE-047.

Run the full test gate, the shell gate, `git diff --check` and `ki repo audit --repo .`. Commit by explicit path, local only on `main`. Do not self-accept.

## Limits

- No sudo, `launchctl`, `pfctl`, `rig apply` or `chezmoi apply`; no live machine changes. No push, no remote calls, no `--no-verify`, no force-push. `ki repo conform` only with `--dry-run`.
- Create no new roadmap records (CAPTURE-GATE); put anything new under Queries instead.
- Leave `package.json`, `bun.lock`, `.husky/` and `.githooks/` unchanged. Leave any other session's changes alone and name them in the report.

## Report

Write status lines, each `HH:MM BST - <step>`, to `~/.local/state/ki/agents/mac-studio-setup/core062.status`, ending with `DONE`, `FAILED` or `BLOCKED`. Write the report to `~/.local/state/ki/agents/mac-studio-setup/core062.report.md` as a run report: the heading `# [Rig](...) › [Mac Studio setup](...) › core062`, the form line, then Done, In Progress and Queries (Context, Query, Options with a recommended a) and its confidence), then the banner.

Authority: local edits and commits in tools-rig only, under GOOD-STATE (Kris, 15 October) and the decision above.
