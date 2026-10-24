# chezmoi › json-apply

**🤖 → 👤 Handoff to supervisor · Run report at 00:49 BST**

---

## Done

- Applied `~/bin/chezmoi/json` alone, bringing it up to the source from orca-coexist's `5bfaa32`. Before applying, the live file matched the previous source byte for byte, so it had no edits of its own.
- The pending change, as `chezmoi diff ~/bin/chezmoi/json` showed it (contains no secrets): `mergeOwnedHooks` gains a `first` option that puts owned hook groups first rather than last. A new exported `transformCodexHooksFragments` and a CLI subcommand `transform-codex-hooks-fragments <hooks.json>` merge only the declared hook groups into the shared `~/.codex/hooks.json`, leaving Orca's registrations in place. The usage string lists the new subcommand.
- Checks: `chezmoi status` now lists only `.config/rig/conf.d/10-applications.toml` and `40-macos.toml`, the two files held under TOWER-APPLY. Neither was applied. The Git tree is clean, there are no lock files, and nothing was committed or pushed.

## In Progress

Nothing.

## Queries

None.
