# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › drain

**🤖 → 👤 Handoff to supervisor · Run report at 07:53 BST · last mark 00:20 BST**

---

## Done

Where each residual now lives:

| Residual | Lives in |
| --- | --- |
| 1 Handler read-back timing | New [KI-TOOL-RIG-CORE-070](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) (triage) |
| 1 23 October `.toml` evidence | Added to [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) |
| 2 terra's firewall state and corrected re-apply procedure | Added to [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md); FIREWALL-REAPPLY stays in queries.md |
| 3 `exposed-beyond-tailnet` wording | New [KI-TOOL-RIG-CORE-071](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-071-firewall-exposure-wording.md) (triage) |
| 4 Tower apply, Dock and the eleven test plists | New [KB-DOTFILES-UE-106](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-106-apply-tower-assistant-at-applications.md) (triage); TOWER-INSTALL stays in queries.md |
| 4 Tower 2.1 build and install | Already held by apps-tower KB-MIDNIGHT-TOWER-APP-006 and KB-MIDNIGHT-TOWER-APP-005 |
| 4 Tests leaving the plists | TOWER-TEST-PLISTS line in [kb.regular.site-tower messages.md](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.regular.site-tower/messages.md) |
| 5 sol level with terra, then its drift | New [KB-DOTFILES-UE-105](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-105-bring-sol-level-with-terra.md) (triage) |
| 6 VS Code territory layout | Already held: VSCODE-LAYOUT in [ki.tools-burndown messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md); its chezmoi sync step is in state.md; nothing captured |
| 7 TERRA-REMOVALS | Already held by [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md) |
| 7 ORCA-ADOPT, ORCA-PER-PANE | New [KB-DOTFILES-UE-107](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-107-decide-orca-adoption.md) (triage), with the draft upstream issue |
| 7 RADAR-DESIGN, RADAR-PUBLIC | New [KB-DOTFILES-UE-108](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-108-decide-tool-radar.md) (triage) |
| 8 Rig removal, app footprint, machine management | Already held in ki.mac-studio-setup messages.md |
| 8 Tower Save Nudge privacy grant | Already held by KB-DOTFILES-UE-071 |
| 8 MGIT-EXTERNAL-MEMBER, ki-engineering DESIGN-2 audit failure | Already with ki.tools-burndown; nothing captured |
| 8 Claude Desktop relaunch, TRUST-COMPLETE, UE-090 and UE-100 attended steps, `/tmp/apply-plan-backup`, `stage3-dock-before.plist` | Already in ki.chezmoi state.md or their existing records |
| 8 Warp leftovers, report copies | Already resolved; nothing captured |

Commits. All three repositories are now level with origin, but this run did not push them (see Queries).

- chezmoi: `04043ae` reserves UE-105 to UE-108. `f3f17fa chore: baseline` was made by someone else at 07:46. `943aff9` is mine and carries the gate fixes. Gate: audit pass, node pass, rumdl pass.
- tools-rig: `980f88b` reserves CORE-070 and CORE-071; it was committed before the gate ran. `6ecdd04 chore: baseline` (not mine) carries the four record changes. Gate: audit, shellcheck, `bash -n`, assemble check, benchmark, provider smoke, Bats 645/645, mandoc and diff check all pass. After the rebase, no ID collides.
- personal-principal: `b84cd1ff chore: baseline` (not mine) carries the TOWER-TEST-PLISTS line. Its gate was not run separately.
- No lock files and no uncommitted files in any of the three. The temp directory is empty.

## In Progress

Nothing.

## Queries

**BASELINE-SWEEP** (Needs: decision)

**Context:** At 07:46:54 BST, something other than this run committed every uncommitted file in chezmoi, tools-rig and personal-principal as `chore: baseline`, with no co-author trailer. Between 07:47 and 07:50 it pulled and pushed all three. That included this run's captures, and in chezmoi it included the records before two titles were shortened to pass audit ITEM-1 (fixed in `943aff9`). The message is in neither tools-mgit nor tools-ki. The hnr hold-drain run launched at 07:45, but its scope is hnr-principal. The contents match what I wrote, so I left the history alone.

**Query:** Was this sweep yours, and should its non-conventional commits stay?

**Options:**

a) (recommended, confidence medium) Leave them. They are pushed, the content is right, and rewriting pushed history would mean a force-push. Trace the sweep separately if it was not yours. b) Have the sweep's owner name it, so that future runs expect it. c) Treat it as a defect and capture a record in the owning repository once it is identified.

**CAPTURE-GATE** (Needs: acknowledgement)

**Context:** `ki-next`'s CAPTURE-GATE says a background run never creates records. This run created six triage records on your explicit drain authority from 01:48 BST. It also changed adopted records CORE-047 and CORE-069, as the brief authorised.

**Query:** Do you accept these captures as within the drain authority?

**Options:**

a) (recommended, confidence high) Accept them. They are triage only and unadopted, and the coordinator adopts or cancels them under `ki-next`. b) Have the coordinator review each one before adoption.

🧵 Coordination thread · KI > Rig > chezmoi (ki.chezmoi)
