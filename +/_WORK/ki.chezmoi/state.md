---
id: ki.chezmoi
state: handoff-to-supervisor
since: 2026-10-19T18:45:12Z
received: null
beat: null
mark: 2026-10-19T18:02:56Z
method_read: 979e075a
---

# ki.chezmoi state

## Now

- Handoff to supervisor since 19:46 BST on 19 October; marked at 19:02 BST.
- Nothing running. Run reports sit in `~/.local/state/ki/agents/chezmoi/`.
- With Kris: SOURCE-LOCALS-LIVE, MGIT-APPLY, and the reviewed RIG-LIVE-DELIVER, TRIAGE-CUT and CARRY-DIRECTIONS in `queries.md`; every live apply waits for Kris's explicit approval.

## Next steps

1. Take Kris's answers to the open queries: MGIT-APPLY a) applies `~/.zsh/completions/_mgit` alone and verifies; TRIAGE-CUT a) merges UE-095 and holds UE-096 through `ki-next`.
2. On Kris's SOURCE-LOCALS-LIVE answer, close SOURCE-LOCALS-GATE and SOURCE-LOCALS-APPLY and record whether any `[locals]` apply remains. Keep the [historical Sol evidence](host-locals-sol.report.md).
3. Apply nothing without Kris's next explicit approval, scripts excluded and one reviewed target at a time. The LOCALS-DIFF warning stands: a full `chezmoi diff` may drop dev-linked harness `[locals]` entries and change the Codex config ([reinstall-check report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/reinstall-check.report.md)).
4. On RIG-LIVE-DELIVER a), plan and deliver [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) source-side with the firewall declaration, `rig doctor` before and after.
5. Carry Kris's authorised, undelivered source directions, dropped from the work file on 19 October; their words are in the [work file at 541a5d91](https://github.com/knowledgeislands/ki-principal/blob/541a5d9149af8a8d9a4b10201a21e34cafcab3a7/%2B/_WORK/ki.chezmoi/work.md) and the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md): SEAT-BIND and SEAT-HOSTS as SEAT-CHANGE amends them, PAPERCLIP-OFF, TOML-OPENER and SSH-CONSOLE (the physical-console fallback in the macOS workstation guide); FW-DECLARE and FW-DECLARE-NOW ride RIG-LIVE-DELIVER. Each is source-only, with its `chezmoi diff` reviewed before any apply.
6. Then put the parked queries in `queries.md` back one at a time, each with a recommendation and its reason.

## Held

- Both-Mac Rig apply - until Kris lifts it.
- Privacy and rationale audits - until the owner resumes them.
- WhatsApp refresh and vega rendering - parked until Kris takes them up.
- Non-blocking Rig-vault and macOS-settings proposals - with their receiving works, until they act.
