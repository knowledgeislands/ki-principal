# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › accept-prep

**🤖 → 👤 Handoff to supervisor · Run report at 05:06 BST · last mark 04:40 BST**

---

## Done

Read-only preparation on sol at HEAD `577bdb0`, clean tree. I made no commits and changed no records or live state. Gate: `ki repo audit` passes with 0 failures and 11 warnings (five of them are the missing sizes below), `node --test` passes 290 of 292 with 2 skipped and 0 failed, and `rumdl check .` is clean.

Awaiting review, one line each:

- [KB-DOTFILES-UE-077](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md): **can be accepted now.** Both Verify searches give the expected result, and the op-cache tests pass. On sol the old Keychain entry is gone and the cache has refetched since the expiry. Terra relies on your Keychain report (Decision 176).
- [KB-DOTFILES-UE-093](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-093-restore-emerge-test-prerequisites.md): **can be accepted now.** `json5` resolves in sol's Emerge checkout, which is clean with its dependencies present, and the Emerge suite passes.
- [KB-DOTFILES-UE-098](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-098-workspaces-git-audit-roots.md): **not yet.** The source change is right, but both live client configs on sol still hold the old 10-root list, and the audit flags that mismatch. You need to do the record's attended steps 1–4 (diff, apply the two targets, restart mcporter and relaunch Claude Desktop, containment check) on sol and then on terra. One note: `~/workspaces/_external` no longer exists, so the new root covers the 8 territories plus `chatgpt-codex`, `claude-desktop` and `vscode`.
- [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md): **not yet.** `~/bin/rig-bringup-check` has not been applied on sol. On terra and then sol, you need to review `chezmoi diff ~/bin/rig-bringup-check`, apply it, run it with `--attended-1password` at the screen, then do the guide's screen checks and the end-to-end trial. Suggest doing this in the same sitting as the KB-DOTFILES-UE-098 apply on each Mac.
- [KB-DOTFILES-UE-100](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md): **not yet.** Sol's 30-minute collection is complete, but terra's is not. You need to run the attended collection on terra (Outstanding concerns steps 1–4). The record's goal, a bounded number of child processes, is still not met, so even after terra it needs a mitigation decision inside this record. For context, sol's daemon restarted at 04:41 and has 8 children (about 0.3 GiB). Claude sessions hosted in Zed run the Homebrew mcporter directly, which supports the theory that Zed is the cause.

## In Progress

Nothing is running.

Outstanding - no action requested now. Other open records:

- [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md): **finish next** (confidence medium). The remaining work is attended clean-up you do at each machine.
  - On sol, C1 and C7i are effectively done. Still to do: C4 (remove the Homebrew `uv` and `python@3.10`, `@3.13` and `@3.14`), C7a–h (Dropbox, iTerm, Synology Drive and `hermes-agent` are still installed), then C8–C9.
  - On terra: B1–B8a and C7i.
  - The mas uninstalls need sudo.
- [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md): **finish next** (high). It is Ready and nothing blocks it; it is source-only work that can be delegated to `ki-implement`.
- [KB-DOTFILES-UE-097](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-097-configure-gmail-routing-paths.md): **move to Hold** (high). It is blocked by [KI-MCP-GSUITE-TOOL-009](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/KI-MCP-GSUITE-TOOL-009-add-gmail-routing-report-mode.md), which is itself on Hold.
- [KB-DOTFILES-UE-087](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-087-manage-headroom-profile-arguments.md): **merge into** [KB-DOTFILES-UE-101](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-101-declare-headroom-user-deployment.md) (high).
  - Both records say to plan the argument source and the deployment together, and 101 is held only on 087.
  - After the merge, 101 becomes a Next draft that keeps its connection/restore boundary.
- [KB-DOTFILES-UE-096](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md): **keep parked at Soon.** It waits on [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md).
- [KB-DOTFILES-UE-071](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-071-audit-macos-privacy-permissions.md) (terra) and [KB-DOTFILES-UE-094](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-094-audit-sol-privacy-permissions.md) (sol): **keep parked at Future.** Each needs you at that machine.
- [KB-DOTFILES-UE-089](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-089-ki-tool-release-channels.md): **keep parked at Future** (low). Its scheduled fast-forward of tool checkouts conflicts with your SOURCE-REFRESH b) answer (Decision 157, no unattended pull); settle that when it is planned.
- [KB-DOTFILES-UE-035](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-035-install-whatsapp-spool-refresh.md): **keep at Hold** until terra shows one successful unattended 10:15 run with a log review. The job is not installed on sol, so only terra can supply the evidence.
- [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md): **keep parked** (medium). 111 entries still need your rationale: 76 tools and 35 macOS settings. Cancelling it would leave those "Review needed" placeholders in place.
- [KB-DOTFILES-UE-099](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-099-resource-subject-links-and-service-paths.md): **keep at triage.**
  - It needs a released Rig that supports subject links.
  - [KI-TOOL-RIG-CORE-065](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-065-resource-subject-links.md) is awaiting review, the latest release is v0.7.0, and the installed build is `0.7.0+dev`.
- [KB-DOTFILES-UE-102](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-102-prompt-notice-for-unapplied-pulls.md) and [KB-DOTFILES-UE-103](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-103-report-absent-mcp-commands.md): **keep at triage** (low). Both were captured tonight.

Five records have no size. My suggested sizes, which would also clear the audit warnings: KB-DOTFILES-UE-027 m, KB-DOTFILES-UE-071 m, KB-DOTFILES-UE-087 s (no longer needed if merged), KB-DOTFILES-UE-089 l and KB-DOTFILES-UE-094 s.

Inbound links to the four done records queued for prune:

- [KB-DOTFILES-UE-082](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-082-tolerate-missing-template-tools.md): linked from KB-DOTFILES-UE-103, so the prune must rewrite that link to the pinned "(pruned)" form. The setup guide and KB-DOTFILES-UE-090 only mention it, without a link.
- [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md): mentioned in KB-DOTFILES-UE-086 only, with no link.
- [KB-DOTFILES-UE-092](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-092-restore-local-skill-projection.md): linked from KB-DOTFILES-UE-088 (pruned alongside it), KB-DOTFILES-UE-090 and KB-DOTFILES-UE-093. Those last links must be rewritten unless KB-DOTFILES-UE-093 is accepted and pruned in the same pass.
- [KB-DOTFILES-UE-088](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-088-ssh-alias-for-sol.md): mentioned in KB-DOTFILES-UE-090 only, with no link.
- Outside the repository, only historical ki-principal files link to them: `+/_WORK/ki.chezmoi/decisions.md`, `+/_WORK/ki.mac-studio-setup/hostkey-check.report.md` and 10 `+/_WORK/ki.baseline-rollout/` review reports. Nothing in personal-principal, ki-agentic-harness or tools-rig links to them.

## Queries

**ACCEPT-BATCH**

**Context:** Of the five records awaiting review, only KB-DOTFILES-UE-077 and KB-DOTFILES-UE-093 have every step done and every check passing. KB-DOTFILES-UE-098, KB-DOTFILES-UE-090 and KB-DOTFILES-UE-100 each need you at terra and/or sol first, as listed under Done.

**Query:** Accept [KB-DOTFILES-UE-077](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md) and [KB-DOTFILES-UE-093](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-093-restore-emerge-test-prerequisites.md) now?

**Options:** a) (recommended, confidence high - every step is done and both Verify sections pass) accept both. b) accept only one; name which. c) not yet.

**CLEAR-BATCH**

**Context:** These are the cancel/merge and tidy recommendations above. None of them cancels a record.

**Query:** Apply these roadmap tidy-ups?

1. Merge [KB-DOTFILES-UE-087](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-087-manage-headroom-profile-arguments.md) into [KB-DOTFILES-UE-101](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-101-declare-headroom-user-deployment.md) and move 101 to a Next draft.
2. Move [KB-DOTFILES-UE-097](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-097-configure-gmail-routing-paths.md) to Hold behind KI-MCP-GSUITE-TOOL-009.
3. Record the suggested sizes.

**Options:** a) (recommended, confidence high - the two Headroom records already say to plan together, 097's blocker is itself held, and the sizes clear five audit warnings) apply all three. b) apply a subset; name which. c) none.

### 🤖 → 👤 Handoff to supervisor · since 05:06 BST

👤 2 with you

- [with you] ACCEPT-BATCH · Kris · since 05:06
- [with you] CLEAR-BATCH · Kris · since 05:06
