# ki.chezmoi queries

## Open

### TERRA-ADOBE-LEFTOVERS: clear the remaining Adobe and BlueStacks leftovers on terra

- terra: Context: both apps are uninstalled; a blind review (adobe-left-review, Codex high) found no remaining app that uses the shared Adobe data, the root-owned `/Library` leftovers or the stale `com.adobe.ccxprocess` registration.
- Query: how far to clear them?
- Options: a) (recommended, confidence medium - no consumer found, every move reversible) full cleanup: a run moves the user data to `~/.Trash/adobe-leftovers-2026-10-24/` and boots out the stale registration; Kris runs one sudo paste block moving the `/Library` items to a dated backup in `/Users/Shared`. b) user data and registration only; leave the root-owned items. c) leave everything.
- FIREWALL-REAPPLY: Kris chose a) (00:47 BST); run firewall-apply.
- Not raised: CORE-SET-COMMENTS (stays in the worksheet).
- ORCA-ADOPT, ORCA-PER-PANE → KB-DOTFILES-UE-107 (sol); RADAR-DESIGN, RADAR-PUBLIC → KB-DOTFILES-UE-108; run records-update (Kris, 00:49 BST).

## Parked

None (Kris unparked everything, 24 October).
