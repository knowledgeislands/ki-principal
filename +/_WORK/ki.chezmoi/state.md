---
id: ki.chezmoi
state: on-hold
hold:
  reason: paused
  release: Kris resumes the sol pass from a session on sol
since: 2026-10-24T14:55:02Z
received: 2026-10-20T01:30:00Z
beat: null
mark: 2026-10-24T15:06:58Z
method_read: beb56729
---

# ki.chezmoi state

## Now

- ON HOLD at Kris's 24 October, 15:55 BST instruction. No implementation is running; the remaining baseline pass waits for a session on sol.
- terra: firewall v5 rehearsal and apply are complete; the last recorded Rig doctor has zero findings. Drift remains: [sync-close](/Users/krisbrown/.local/state/ki/agents/chezmoi/sync-close.report.md) retains eleven pending targets, including connection-sensitive and app-owned settings, for their owners.
- Every machine-specific instruction starts with terra: or sol:.

## Next steps

1. sol: resume the [sol-pass checklist](messages.md), checking the active Rig build and its hold before reviewed scoped applies under [KB-DOTFILES-UE-105](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-105-bring-sol-level-with-terra.md); complete the independent app/removal and health checks in [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md). The firewall is a separate connection-critical pass under [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md), with an adapted v5 wrapper and an exact sol restore rehearsal before any policy write.
2. sol: complete local unmanaged-file and software reviews under [KB-DOTFILES-UE-111](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-111-review-unmanaged-files.md) and [KB-DOTFILES-UE-112](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-112-review-workstation-software.md). Trial host selection is settled; Orca's remaining safety/comparison and per-pane questions stay in [KB-DOTFILES-UE-107](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-107-decide-orca-adoption.md), while radar implementation proposals stay in [KB-DOTFILES-UE-108](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-108-decide-tool-radar.md).
3. terra: and sol: DEFUDDLE-INSTALL is received, deferred until work resumes. Declare the Homebrew formula (minimum 0.19.5), then prove install, version observation, repeat apply, drift detection and removal; check both Macs. Owner direction and source: [KB-PRINCIPAL-007](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Roadmap/KB-PRINCIPAL-007-software-discovery-and-evaluation.md). No install is authorised during this hold.
4. terra: finish the health/drift reconciliation and establish a supported receipt-only UTM cleanup that preserves the MAS app and all VMs under [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md). The broken Claude Code URL-handler executable remains a recorded software-review finding under [KB-DOTFILES-UE-112](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-112-review-workstation-software.md), not a completed repair.
5. homeless: TRUST-COMPLETE still needs its chezmoi Decision Record; keep the owner's complete-trust/no-folder-prompts direction in [decisions](decisions.md). Other retained authority: survey outcome unconfirmed, vega render held, Paperclip disabled, sol NordVPN undecided.
6. Sync VS Code source after ki.tools-burndown delivers the [receiving layout message](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md). Retain the [Tower visual prompt](design/tower-assistant-claude-design-prompt.md) for its live apps-tower reference and the [take-stock retro](design/retro-2026-10-20.md) for ki.ways-of-working's live synthesis.
7. Reconcile source/target drift and cross-host history through their owners before calling the baseline settled; [sync-close](/Users/krisbrown/.local/state/ki/agents/chezmoi/sync-close.report.md) holds the latest evidence and its unresolved SYNC-RECONCILE query.

## Held

- sol: Rig apply remains held until its checkout is checked against the reviewed build in [KB-DOTFILES-UE-105](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-105-bring-sol-level-with-terra.md); the sol .toml handler waits on [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md). Every apply still requires the scoped diff/review gate; this tidy lifts no hold.
