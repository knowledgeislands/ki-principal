---
id: ki.chezmoi
state: with-worker
hold:
  reason: paused
  release: kb receives RIG-PER-MACHINE (sol pass handed to kb.regular.rig-sol); then rewrite the remit to the chezmoi approach
since: 2026-10-24T01:50:00Z
received: 2026-10-20T01:30:00Z
beat: null
mark: 2026-10-24T18:54:18Z
method_read: beb56729
---

# ki.chezmoi state

## Now

- Running on sol: sol-drift reconciles the remaining chezmoi and Rig drift (Kris 02:50).
- terra: level with source at 18:07 BST (`chezmoi status` empty, Rig doctor 0 findings). drift-low applied the 7 low-risk targets; codexbar-fix (038d999) fixed the JSON helper and applied the CodexBar patch; Claude Code repaired its URL helper after Kris's Terminal session (afe3256); Defuddle 0.19.5, installed by Kris, is declared and adopted in Rig for both Macs (5723c99). UTM's stale Homebrew record was cleared with the App Store app and VMs verified unchanged (500d2d5, KB-DOTFILES-UE-086 B8a); Rig shows zero unmanaged items. terra is finished.
- sol (from the sol session of 23-24 October, merged 24 October 20:50 BST): mcporter restarted on sol and verified (02:25); WhatsApp MCP fails discovery, pre-existing. Tower Assistant 2.1 installed on sol with its own signing identity, Accessibility and Dock done, doctor 4 (02:46); KB-DOTFILES-UE-106 updated and ready for acceptance. With Kris: firewall re-apply at terra.
- sol: Warp retired on sol; chezmoi and harness pushed and the Warp cleanup applied (02:26). With Kris: WARP-CONTAINER and WARP-HANDLER (Finder steps on sol); Warp backups deleted after.
- ON HOLD at Kris's 24 October, 15:55 BST instruction. No implementation is running; the remaining baseline pass waits for a session on sol.
- terra: firewall v5 rehearsal and apply are complete; the last recorded Rig doctor has zero findings. Drift: four app-owned targets remain (see above).
- Every machine-specific instruction starts with terra: or sol:.

## Next steps

1. sol: resume the [sol-pass checklist](messages.md), checking the active Rig build and its hold before reviewed scoped applies under [KB-DOTFILES-UE-105](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-105-bring-sol-level-with-terra.md); complete the independent app/removal and health checks in [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md). The firewall is a separate connection-critical pass under [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), with an adapted v5 wrapper and an exact sol restore rehearsal before any policy write.
2. sol: complete local unmanaged-file and software reviews under [KB-DOTFILES-UE-111](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-111-review-unmanaged-files.md) and [KB-DOTFILES-UE-112](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-112-review-workstation-software.md). Trial host selection is settled; Orca's remaining safety/comparison and per-pane questions stay in [KB-DOTFILES-UE-107](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-107-decide-orca-adoption.md), while radar implementation proposals stay in [KB-DOTFILES-UE-108](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-108-decide-tool-radar.md).
3. sol: install Defuddle through Rig in the sol pass (declared for both Macs in 5723c99; terra done).
4. sol: complete the remaining KB-DOTFILES-UE-086 checks (terra's B8a is done) under [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md).
5. homeless: TRUST-COMPLETE still needs its chezmoi Decision Record; keep the owner's complete-trust/no-folder-prompts direction in [decisions](decisions.md). Other retained authority: survey outcome unconfirmed, vega render held, Paperclip disabled, sol NordVPN undecided.
6. Sync VS Code source after ki.tools-burndown delivers the [receiving layout message](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md). Retain the [Tower visual prompt](design/tower-assistant-claude-design-prompt.md) for its live apps-tower reference and the [take-stock retro](design/retro-2026-10-20.md) for ki.ways-of-working's live synthesis.
7. Reconcile source/target drift and cross-host history through their owners before calling the baseline settled; [sync-close](/Users/krisbrown/.local/state/ki/agents/chezmoi/sync-close.report.md) holds the latest evidence and its unresolved SYNC-RECONCILE query.

## Held

- sol: Rig apply remains held until its checkout is checked against the reviewed build in [KB-DOTFILES-UE-105](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-105-bring-sol-level-with-terra.md); the sol .toml handler waits on [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md). Every apply still requires the scoped diff/review gate; this tidy lifts no hold.
