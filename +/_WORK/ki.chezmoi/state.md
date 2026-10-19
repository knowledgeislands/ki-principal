---
id: ki.chezmoi
state: with-worker
since: 2026-10-19T18:06:00Z
received: null
beat: null
mark: 2026-10-19T18:02:56Z
method_read: eff6163b
---

# ki.chezmoi state

## Now

- With worker since 19:06 BST on 19 October; marked at 19:02 BST.
- Running: mark-tidy-1019 (report sweep, link pinning, decisions life cycle) and mgit-completion (regenerate `_mgit`, source only); queued: burndown-push, after mgit-completion.
- With Kris: SOURCE-LOCALS-LIVE and RIG-LIVE-DELIVER in `queries.md`; every live apply waits for Kris's explicit approval.
- Four commits of other works sit unpushed in ki-principal above origin; this work's commits stack on them and stay unpushed until Kris pushes.

## Next steps

1. Once mark-tidy-1019 has finished, log BURNDOWN-PUSH (Kris's agreement, routed 19:25 BST from Ways of working) in `decisions.md`.
2. Receive mark-tidy-1019, mgit-completion and burndown-push: copy their queries into `queries.md`, home outcomes, then show Kris the one-target `_mgit` diff and wait for apply approval.
3. On Kris's SOURCE-LOCALS-LIVE answer, close SOURCE-LOCALS-GATE and SOURCE-LOCALS-APPLY and record whether any `[locals]` apply remains. Keep the [historical Sol evidence](host-locals-sol.report.md).
4. Apply nothing without Kris's next explicit approval, scripts excluded and one reviewed target at a time. The LOCALS-DIFF warning stands: a full `chezmoi diff` may drop dev-linked harness `[locals]` entries and change the Codex config ([reinstall-check report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/reinstall-check.report.md)).
5. On RIG-LIVE-DELIVER a), plan and deliver [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) source-side with the firewall declaration, `rig doctor` before and after.
6. Carry Kris's authorised, undelivered source directions, dropped from the work file on 19 October; their words are in the [work file at 541a5d91](https://github.com/knowledgeislands/ki-principal/blob/541a5d9149af8a8d9a4b10201a21e34cafcab3a7/%2B/_WORK/ki.chezmoi/work.md) and the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md): SEAT-BIND and SEAT-HOSTS as SEAT-CHANGE amends them, PAPERCLIP-OFF, TOML-OPENER and SSH-CONSOLE (the physical-console fallback in the macOS workstation guide); FW-DECLARE and FW-DECLARE-NOW ride RIG-LIVE-DELIVER. Each is source-only, with its `chezmoi diff` reviewed before any apply.
7. Then put the parked queries in `queries.md` back one at a time, each with a recommendation and its reason.

## Held

- Both-Mac Rig apply - until Kris lifts it.
- Privacy and rationale audits - until the owner resumes them.
- WhatsApp refresh and vega rendering - parked until Kris takes them up.
- Non-blocking Rig-vault and macOS-settings proposals - with their receiving works, until they act.
