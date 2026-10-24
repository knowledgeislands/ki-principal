# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-deliver-rig-056

**🤖 → 👤 Handoff to supervisor · Run report at 22:33 BST · last mark 09:27 BST**

---

## Done

- Classification confirmed: [KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) is a read-only investigation. It does not wait on KI-TOOL-RIG-CORE-053's observe-only shape question; its finding feeds into that question instead. It needs no live apply.
- Planned to Ready (tools-rig `ee0bfa3`). The record moved from Future to Now under the 22:03 BST self-serve burndown, and its method was narrowed to read-only evidence. A throwaway app or a scratch account would change the workstation, which this run may not do, so each unknown is written up as an evidence gap instead.
- Delivered to awaiting review (tools-rig `45aa494`). Finding: on macOS 27 a system agent, MenuBarAgent, keeps menu-bar order and the "Allow in the Menu Bar" list in its own restricted container, which other processes cannot open. It reads the `NSStatusItem Preferred Position` keys only as a legacy fallback, and seven of those keys on sol are stale (wider than either display). There is no public interface for setting order. Recommendation: stay report-only and open no declaration record (confidence high).
- Verify evidence: every claim is marked observed, inferred or gap, and each observed claim names the read-only command behind it. Nothing was written, restarted or launched. The roadmap audit shows no finding on this record. `git diff --check` passes.
- Pre-commit hook (RIG-PRECOMMIT-BATS): passed on both commits, 611 of 611 Bats tests, staged audit PASS. It did not fail this time.
- Follow-up routed as RIG-053-LEGACY-ORDER in the [ki.tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md) (ki-principal `ab08272f`, commit gate passed). KI-TOOL-RIG-CORE-053's order-drift check ranks icons by the legacy keys. Its review and post-release owner check should therefore read one key, Command-drag that icon, and read the key again before relying on the check.
- Local tools-rig `main` fast-forwarded to `45aa494`; the worktree and its branch are removed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- KI-TOOL-RIG-CORE-056 is awaiting an independent review. I did not accept it.
- Two attempts to list the protected containers were refused by the system. No consent was granted, but macOS's privacy controls may have logged the attempts.
- Pending handoff: on sol, tools-rig `main` is 2 ahead of `origin/main` (this run's `ee0bfa3` and `45aa494`). ki-principal `main` is 17 ahead (this run's `ab08272f` plus other sessions' commits). Nothing was pushed. ki-principal's `+/_WORK/ki.ways-of-working/messages.md` has another session's uncommitted change, which I left untouched.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 22:33 BST

🤖 0 running

- [awaiting review] KI-TOOL-RIG-CORE-056 · independent reviewer · 22:33 BST
- [committed] tools-rig `ee0bfa3`, `45aa494`; ki-principal `ab08272f`
- [unpushed] tools-rig main, 2 ahead
- [unpushed] ki-principal main, 17 ahead
