---
id: ki.chezmoi
state: with-worker
since: 2026-10-19T22:28:00Z
received: null
beat: null
mark: 2026-10-19T22:30:05Z
method_read: 979e075a
---

# ki.chezmoi state

## Now

- With worker; marked at 23:30 BST on 19 October.
- Sol's SSH key delivery and firewall are applied and verified; the evidence is in KI-TOOL-RIG-CORE-047 (tools-rig `2ab9354`, unpushed).
- The NordVPN bypass follow-up is captured as KI-TOOL-RIG-CORE-068 (tools-rig `6c06d8c`, `abb734b`, unpushed); detection only, no attended trial approved.
- KI-TOOL-RIG-CORE-047 stays awaiting-review: the NordVPN on/off checks and Terra's `rig apply --sudo` are outstanding (Decision 131). State of play is told.
- parked-three is received: IWORK, STYLE-LINK and DIR-PRUNE are committed in chezmoi (`2470321`, `7ac9047`, `d5ac9c9`, unpushed); STYLE-WHEN a) taken (Decision 133).
- Running: ue090-plan (plans the open UE-090 gaps), mcporter-restart (Decision 132).
- With Kris: CLAUDE-APPLY.

## Next steps

1. Receive ue090-plan and mcporter-restart; blind-review any medium, low or destructive query.
2. On Kris's CLAUDE-APPLY answer, launch the targeted diff, apply and verification of `~/.claude/settings.json` and `~/.claude/output-styles/ki-coordinator.md`.
3. CONSUMER-MIGRATE: mgit v0.18.0 is released; check what migration this work owes.
4. Pushing tools-rig, chezmoi and the ki-principal work folder is Kris's call.

## Held

- Both-Mac Rig apply - until Kris lifts it.
- REST-HOLD, narrowed to UE-090 gap 1 together with UE-087.
- The attended NordVPN trial - until a tested restore path exists (KI-TOOL-RIG-CORE-068).
- Privacy and rationale audits - until the owner resumes them.
- WhatsApp refresh and vega rendering - parked until Kris takes them up.
