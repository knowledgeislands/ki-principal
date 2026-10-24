# [Tower](/Users/krisbrown/workspaces/personal/personal-principal/Streams/Initiatives/tower.md) › apps-tower.midnight.ninja › tower-path

**🤖 → 👤 Handoff to supervisor · Run report at 23:54 BST**

---

## Done

- Terra check (nothing moved): `/Applications/Tower Assistant.app` does **not exist** on terra. The only copy is `~/Applications/Tower Assistant.app`, version 2.0, and `codesign --verify --deep --strict` passes on it. Release 2.1, the one that installs to `/Applications`, is not installed on terra, so KB-MIDNIGHT-TOWER-APP-006's delivery has not reached this Mac.
- `rig doctor` before (live config, profile `laptop`): 6 findings, and I read each one:
  - `default-application.sh` and `default-application.zsh` are drifted (Ghostty instead of Zed).
  - `default-application.toml` is drifted (VS Code instead of Zed), and it is also the 1 historical apply failure, from 19 October.
  - `dock.workstation` is drifted (order).
  - `firewall.screen-sharing-tailnet` is drifted (anchor-changed, exposed-beyond-tailnet).
  - None of them is Tower-related, and none can be fixed without an apply, which the hold forbids. The firewall one is connection-critical and has no restore path in this brief, so I left all six alone.
- Commit `d47acf8` `fix(rig): declare Tower Assistant at /Applications`:
  - `tool.tower-assistant` artefact and `dock-item.tower-assistant` path now say `/Applications/Tower Assistant.app`, and the stale "pinned until the move" comment is gone.
  - The catalogue test assertion and the "Move to /Applications" section of `docs/guides/tools/tower-assistant.md` are updated to match.
  - `rig-tower-save-nudge` is unchanged: it already prefers `/Applications`, keeps its `~/Applications` fallback, and its test already covers both.
- Gate: `ki repo audit` passed (0 FAIL, 4 legacy WARN, all pre-existing). `node --test` gave 355 tests, 353 pass, 0 fail. `rumdl check .` is clean.
- `rig doctor` after, run against a temporary copy of the live config with only the two changed files re-rendered through `chezmoi cat` (`RIG_CONFIG_HOME`, nothing applied): still 6 findings. The one change is that `dock.workstation` now reports `dock-item-path-missing:tower-assistant` instead of `order`, because the declared path does not exist on terra. The tool artefact gives no finding, since the tool is catalogue-only. The temporary copy has been deleted.
- Scoped `chezmoi diff`, for Kris's review:
  - `~/.config/rig/conf.d/10-applications.toml`: `artifacts = ["~/Applications/Tower Assistant.app"]` becomes `["/Applications/Tower Assistant.app"]`.
  - `~/.config/rig/conf.d/40-macos.toml`: the "Pinned from the current install…" comment is removed, and `dock-item.tower-assistant` `path` changes from `~/Applications/…` to `/Applications/Tower Assistant.app`.
- Apply commands, for when Kris approves, the hold lifts and that Mac's copy is in `/Applications`: `chezmoi apply ~/.config/rig/conf.d/10-applications.toml ~/.config/rig/conf.d/40-macos.toml`, then `rig apply --target dock.workstation --dry-run`, then that apply after review, then `rig doctor`.
- Nothing applied, nothing moved, no push. The other session's `dot_mgit.toml` was not touched. chezmoi shows unrelated drift on `.codex/hooks.json`, which I left alone.

## In Progress

Nothing.

## Queries

**Context:** Source now declares `/Applications`, but terra still has only 2.0 in `~/Applications`. Applying before the attended 2.1 install and move would make `dock.workstation` report `dock-item-path-missing` and drop the Dock tile. **Query:** Should the attended 2.1 install into `/Applications` happen on terra (and on the other Mac, if it is also still on `~/Applications`) before this commit is applied? **Options:** a) (recommended, confidence high - the guide and Rig have no path fallback) Install 2.1 to `/Applications` on each Mac and retire the `~/Applications` copy, then apply this commit there when the hold lifts. b) Apply now and accept the Dock finding until the move. c) Revert `d47acf8` until the move is done.
