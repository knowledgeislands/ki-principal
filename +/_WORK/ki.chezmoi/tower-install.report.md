# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › tower-install

**🤖 → 👤 Handoff to supervisor · Run report at 01:02 BST · last mark 23:45 BST**

---

## Done

- terra: Tower Assistant 2.1 (build 4) installed at `/Applications/Tower Assistant.app` via `build.sh install` from apps-tower, signature verified; no `~/Applications` copy; preferences plist kept (paused, 300 s). Undo: remove the bundle.
- terra: `10-applications.toml` was already level with source when this run reached it (live file rewritten at 00:52 by another route); `chezmoi apply` of `40-macos.toml` took effect (Dock item now `/Applications`). Undo: restore the pre-apply copy.
- terra: `rig apply --target dock:workstation` completed; Dock holds Tower Assistant from `/Applications`. Undo: re-import the pre-apply Dock plist and restart the Dock. The app is catalogue-only and the wrapper was retired on 23 October, so neither had a Rig target.
- terra: Accessibility carried over the move: the permission check returned `permissionGranted`, so no grant was needed from Kris; the app runs from `/Applications` as a regular Dock app.
- terra: `rig doctor` 2 → 1 findings: `dock.workstation` cleared; `firewall.screen-sharing-tailnet` remains, left to the running firewall-apply. `chezmoi status` no longer lists either Rig file (only Claude Desktop's config, not this run's).
- [KB-DOTFILES-UE-106](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-106-apply-tower-assistant-at-applications.md) gained `terra:` evidence, with sol still to do: chezmoi `63f3ad2`. Gate: audit pass (0 fail), tests pass, rumdl clean.
- Not pushed: another session's `d3ddab1` (Prime Video declaration) is also ahead of origin, so the push condition "only your commits ahead" failed.

## In Progress

- Attended, under KB-MIDNIGHT-TOWER-APP-005 and KB-MIDNIGHT-TOWER-APP-006: a live **Nudge Now** with The Tower running (it was not running), the **Show in Dock** toggle across a relaunch, the Permissions panel, and re-enabling Start at Login if wanted.
- sol: KB-DOTFILES-UE-106 not started there; waits on KB-DOTFILES-UE-105 and a 2.1 install on sol.
- terra: the eleven `tower-assistant-*-test-*.plist` files remain, waiting on apps-tower's confirmation.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 01:02 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Tower Assistant 2.1 on terra, attended checks and push · chezmoi supervisor · since 01:02 BST

🧵 Coordination thread · KI > Rig > chezmoi (ki.chezmoi)
