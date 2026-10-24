# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) › drift-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 19:09 BST · last mark 08:51 BST**

---

## Done

The chezmoi drift on terra is resolved apart from the two held Codex files. I ran no bare `chezmoi apply` or `chezmoi diff`, and changed no source, so there is nothing to commit.

- **Classified `chezmoi status`.** After apply-stages, three entries were left:
  - `~/.codex/config.toml`: held (CODEX-CONFIG). Not touched.
  - `~/.codex/hooks.json`: held (ORCA-HOOKS). Not touched.
  - `~/workspaces/claude-desktop/Projects/HNR`: due for removal.
- **Removed `~/workspaces/claude-desktop/Projects/HNR`.** `.chezmoiremove` retires it (`HNR` was renamed to `Humans Not Robots`), but something recreated it as an empty folder at 15:17 today. I checked it held no entries, then ran a scoped `chezmoi apply --force` of that one target. `--force` was needed only because chezmoi asks for confirmation and there is no terminal to answer it. Outcome: the folder is gone and `chezmoi status` now lists only the two held files. Undo: `mkdir ~/workspaces/claude-desktop/Projects/HNR`.
- **Moved Warp's leftovers to the Trash** through Finder, so they can be put back: the `2BBY89MBSN.dev.warp` Group Container, the `dev.warp.Warp-Stable` and `dev.warp.Warp-Preview` caches, and `warp_preview.log.old.0` and `.1`. Warp was not running. Outcome: none of the five paths exists any more and all five are in `~/.Trash`. Finder named the Stable cache `dev.warp.Warp-Stable 19.09.24` because a folder of that name was already there from the zap. Undo: Put Back in Finder.
- **Broken Warp Dock tile:** left for stage 3, as the brief says.
- **`rig doctor`:** not run, because no Rig file changed. apply-stages left 6 findings, all explained in its report.

## In Progress

Nothing.

**Source side:**

- `workspaces/humans-not-robots/dot_mgit.toml` has uncommitted changes. They add `apps-sky.humansnotrobots.be` and `apps-snowflake.humansnotrobots.be` as members, and the file was modified at 17:04. They look like they belong to the session that committed `08505ae` (the move of the humansnotrobots.be sites) and set up the new repositories. I left them alone.
- One commit on `main` is not pushed: `25c0bde` ("chore(trust): regenerate trusted folders for new repositories", 18:26). This is compared with `origin/main` as of the last fetch, since I ran none. Not pushed.

## Queries

None.

**Drift remaining:**

- `~/.codex/config.toml`: held under CODEX-CONFIG. Its render reads 1Password, so Kris diffs it at the screen.
- `~/.codex/hooks.json`: held under ORCA-HOOKS while orca-hooks-research runs.
- `workspaces/humans-not-robots/dot_mgit.toml` (source): another session's uncommitted edit. Its owner commits it.
- `25c0bde` on `main`: not pushed, because no push was authorised.
- Warp Dock tile: waits for the stage 3 Dock apply.
