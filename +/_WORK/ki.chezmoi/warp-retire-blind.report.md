# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › warp-retire-blind

**🤖 → 👤 Handoff to supervisor · Run report at 08:35 BST · last mark not supplied in blind brief**

---

## Done

Independent recommendation: add a staged, attended terra retirement; confidence **medium** — prove the replacement and preserve recoverable data before destructive cleanup, while account-wide effects and Warp’s current deletion/export semantics remain unverified.

Source review: inspected commits `6e6fef8`, `1649d10`, `9e3879d` and `385a024`; no commits or repository changes made.

Pending-state check: `chezmoi status` confirms the Ghostty additions, eleven Warp removals and overlapping Rig changes; no diff or apply run.

Rig overlap check: source and live TOML parse successfully; the shared files also carry GitUp, Orca, Tower Assistant, Starship and a Nerd Font declaration.

Shell check: `zsh -n dot_zsh/60_territory` passed; no interactive tab, permission or session-migration test performed.

Feature check: installed Ghostty is **1.3.1**; its bundled official documentation describes horizontal tabs, shell titles and prompt navigation, with no native vertical sidebar or persistent per-tab last-command list documented.

Report lint: passed with the repository configuration and the required bold handoff line exempted; default lint settings had flagged the mandated line and single-line paragraphs. Checker cache files created by this review were removed.

Isolation check: forbidden work-package files and other agents’ reports were not read; no network calls, application actions, secrets inspection or machine configuration changes made. Only the requested report and status files remain from this review.

Retirement sequence reviewed:

1. Inventory terra’s live Warp tabs, foreground jobs and background processes; save required scrollback, commands and unsaved work. A terminal process cannot generally be moved into Ghostty: finish it, deliberately restart it, or reattach an already persistent session. Keep a working Terminal.app window available.

2. Apply only the reviewed Ghostty config and territory fragment first, leaving Warp’s eleven files intact. The eventual operator must obtain the required targeted diff review and approval; this review deliberately did not run that diff. Reload Ghostty, open a fresh Zsh and try `territory ki` **before** deleting or uninstalling anything. Check the directory, title and Automation permission; manual new-tab plus `cd` remains the fallback. The shell-loader change in `385a024` is separate and shares `~/.zshrc` with the pending Starship work.

3. Export required Warp Drive material and separately preserve required conversations, local state and live settings/keybindings/tab configs. Verify the exports are readable outside Warp; do not assume a Drive export includes conversations or session scrollback. Use private storage outside Git for potentially sensitive material.

4. Establish whether sol uses the same account, shared Drive material or conversations before account-wide deletion. This inspection need not happen in the same sitting. Delete only the explicitly approved cloud material while access still works, verify the result, then disable sync and sign out. Confirm what sync actually covers; turning it off or uninstalling is not evidence of cloud erasure. Do not treat service retention or backups as verified deleted.

5. Drain sessions, quit Warp fully and remove its login item before removing its files. Reopening Warp can recreate settings or resume cloud activity. Scope the later chezmoi apply to the exact terminal targets and all eleven removed **target paths**, rather than a broad home, configuration or Warp-directory apply.

6. Review the shared Rig files once as a combined pending change. Applying a filename writes its current complete source; it cannot select just the Warp commit. `10-applications.toml` also changes GitUp, Orca and font intent; `16-homebrew.toml` combines GitUp and Starship; `40-macos.toml` combines terminal handlers/Dock and Tower Assistant; `60-skills.toml` removes Warp’s runtime selection. If those combined contents are not approved, defer the affected Rig files rather than overwrite them with an older commit or hand-edit live targets. A later “Starship apply” must use the same current source, so it does not undo the terminal change.

7. Before `brew uninstall --cask --zap warp`, inspect the actual installed cask’s removal/zap scope and confirm preserved data covers it. Zap can remove more than the eleven managed files; neither zap nor deleting those files proves cloud cleanup. Check for remaining app data, credentials and runtime skill links without deleting unrelated material. Keeping the app temporarily is reasonable until these checks pass, rather than for an arbitrary week.

8. Read every `rig doctor` finding before and after the combined configuration/removal work; explain remaining findings rather than calling an unchanged count healthy. Keep the both-Mac `rig apply` hold intact. Once explicitly released, reconcile approved handlers and Dock, then verify `.toml`, `.sh` and `.zsh` open in Zed and Warp is absent from the Dock/login items. Uninstalling Warp may release its handler registration; it does **not** prove Zed becomes the selected handler. While reconciliation is held, report handler/Dock drift as pending.

**Sidebar and last-command gap:** Ghostty’s [bundled configuration reference](/Applications/Ghostty.app/Contents/Resources/ghostty/doc/ghostty.5.md:3520) describes titlebar tabs; [prompt navigation](/Applications/Ghostty.app/Contents/Resources/ghostty/doc/ghostty.5.md:4421) can revisit commands in scrollback. Its Zsh integration shows a running command in the title and returns to the directory at the prompt. The managed territory function sets a fixed tab-title override, so those tab labels do not become a last-command history. This replaces territory launch locations, not Warp’s sidebar workflow. No alternative product was verified under the network restriction; if that view is essential, settle the gap before destructive cleanup.

## In Progress

Nothing is running. Retirement, exports, account cleanup, applies and uninstall remain unperformed.

Outstanding — no action requested now: Warp’s public documentation could not be fetched under the no-network rule. Cloud deletion coverage, export completeness and retention guarantees therefore remain unverified. Sol’s state and live terra sessions were not inspected. The parent work’s mark was not supplied and was not read across the blind boundary.

## Queries

### WARP-RETIRE — Retire Warp on terra in stages

**Context:** Ghostty is the chosen terminal, but deleting settings, cloud history and the application before testing the replacement would remove useful recovery routes. Keeping only Warp’s binary for a week after that deletion offers a limited fallback. A both-Mac `rig apply` hold remains in force.

**Query:** Adopt the staged terra sequence below, with irreversible cleanup dependent on verified preservation and account scope?

**Options:**

a) (recommended, confidence medium - proves Ghostty first and preserves recovery while cloud semantics and sol’s account state remain unverified) Begin terra’s attended transition now; complete retirement when the following prerequisites are satisfied, without requiring both Macs in the same sitting.

b) Complete the attended retirement immediately, only if every prerequisite below can be verified now; otherwise pause at the unmet prerequisite.

c) Keep Warp installed for a week after applying, with an explicit retained-data and restoration plan; the week alone does not preserve settings, sessions or deleted cloud conversations.

d) Hold every apply until sol is available in the same sitting; use this if account scope cannot be established separately, although the evidence does not show a technical requirement for simultaneous local applies.

### 🤖 → 👤 Handoff to supervisor · since 08:35 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Choose the retirement sequence; irreversible cleanup awaits preservation and account-scope checks · supervisor · since 08:35 BST
