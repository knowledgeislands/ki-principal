# chezmoi › tower-remove

**🤖 → 👤 Handoff to supervisor · Run report at 01:37 BST**

---

## Done

- Before: `~/Applications/Tower Assistant.app` version 2.0 (build 3), bundle id `uk.me.kris.tower-assistant`, running as pid 1200 under launchd's ordinary app label; no login item, no LaunchAgent plist, no embedded login helper; one Dock tile pointed at it.
- Quit the app: done, no process left · undo: relaunch after putting it back.
- Moved the bundle to the Trash through Finder: `~/Applications` copy gone, now `~/.Trash/Tower Assistant.app` · undo: Finder › Trash › Put Back, or `mv ~/.Trash/"Tower Assistant.app" ~/Applications/`.
- No login item or LaunchAgent to remove, so nothing was booted out or backed up.
- `/Applications/Tower Assistant.app` (2.1) still absent; not installed. Held Rig files `10-applications.toml` and `40-macos.toml` left unapplied (`chezmoi status` shows only those two); Dock untouched.
- Source search: no live `~/Applications/Tower Assistant` reference; `docs/guides/tools/tower-assistant.md` only mentions it historically ("earlier `~/Applications`").
- No commits; no source changes.
- `rig doctor`: before 1 finding, after 2, exits non-zero both times.
  - `firewall.screen-sharing-tailnet` drifted (anchor changed, exposed beyond the tailnet): there before this run; connection-critical, so not touched.
  - `dock.workstation` drifted (`dock-item-path-missing:tower-assistant`): new. The Dock tile still points at the removed copy and is now broken, as expected. Reported, not fixed.

Kept, because Tower Assistant 2.1 will reuse them: `~/Library/Preferences/uk.me.kris.tower-assistant.plist`. The app has no Application Support, cache, container, HTTP storage or saved-state folder. Also left in Preferences, not keyed by the bundle id and not in scope: eleven `tower-assistant-{identity,permissions,shell}-test-*.plist` files that look like leftovers from tests. The signing identity in the login keychain was not touched.

## In Progress

Nothing. Remaining drift: the broken Dock tile and `dock.workstation` finding clear once 2.1 is installed at `/Applications` and the held `10-applications.toml` and `40-macos.toml` are reviewed and applied. The firewall finding needs its own approved fix.

## Queries

None.
