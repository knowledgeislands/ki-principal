# terra-actions

**🤖 → 👤 Handoff to supervisor · Run report at 18:48 BST**

---

## Done

- **Spark daemon:** nothing to stop. No `Spark Daemon` or `com.xenonium` process, launchd job or login item is left. `/Applications/Spark.app` and the `spark-app` cask are both gone, so your uninstall worked. Spark Desktop (`readdle-spark`) was not touched. Undo: none needed.
- **TRUST-APPLY:** applied the six named targets cleanly, and `chezmoi status` shows all six clean. Claude Desktop is running and reads `claude_desktop_config.json` only at launch, so quit and reopen it to see the new folders. Claude Code picks up `settings.json` in new sessions. Undo: revert the source commit `25c0bde` and re-apply the same six targets.
- **TOWER-PATH:** added one TOWER-PATH message to the [kb.regular.site-tower queue](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.regular.site-tower/messages.md). It records that the move to `/Applications` is cancelled, that `~/Applications/Tower Assistant.app` is the permanent home and that TOWER-PATH-WAIT is withdrawn. Committed in personal-principal as `a544630` (local, not pushed); rumdl passes.
- **Nudge script, explained:** [`rig-tower-save-nudge`](/Users/krisbrown/.local/share/chezmoi/bin/scheduled/executable_rig-tower-save-nudge) starts a fresh copy of Tower Assistant in the background with a 30-second limit. The app then tries to nudge The Tower into saving and writes back a result. The script turns that result into one line in the shared scheduled-job report: nudged, skipped (the game isn't running, there's no window, the window is already minimised, or a nudge is already running), or a failure such as missing Accessibility permission.
  - **When it runs:** never on its own. Its Rig scheduled job has been retired, and the tests confirm there is no `scheduled-job.tower-save-nudge` declaration. Nothing for it is in launchd or `~/Library/LaunchAgents`. Tower Assistant now runs its own five-minute timer from the menu bar. The script is only an optional, manual diagnostic.
  - **Simplify it?** Yes. It looks in `/Applications` first and falls back to `~/Applications` only until the move. With the move cancelled, it should point straight at `~/Applications/Tower Assistant.app`, keeping the `TOWER_NUDGE_APP` override. The comment and the "Move to Applications" section of [the guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/tools/tower-assistant.md) should be updated with it. I haven't changed anything.

## In Progress

None.

## Queries

**Context:** The nudge wrapper and its guide still assume Tower Assistant will move to `/Applications`, which you have now cancelled. **Query:** Shall ki.chezmoi simplify the wrapper's app lookup to `~/Applications` only, and remove the move section from the guide? **Options:** a) (recommended, confidence high - a single permanent path removes dead fallback logic and stale guidance) Yes, as a small separate change with its test updated; b) Leave it as it is, since the fallback does no harm.
