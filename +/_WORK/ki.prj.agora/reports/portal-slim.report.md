# KI > Techne > Agora › portal-slim

**🤖 → 👤 Handoff to supervisor · Run report at 05:03 GMT · last mark 00:04 GMT**

---

## Done

- **The tray is now the Agora Portal.** About, tooltip, menu, notifications and README call it the Agora Portal. Its menu is one status line (who is in the Agora, or what needs a look when anything does), **Open Agora**, Broadcast…, Away / I'm back, Ping, Mark all, Sync now, About Agora Portal and Quit Agora Portal.
- **The reporting submenus are gone:** Agents, Macs and checkouts, Runs, Broadcasts and News, and the items inside them (Review now, Ask after the others now, Check for news now, Mark news as read). What they showed is still in the read endpoint and `state.json` for the Agora app. I removed the wording that only those submenus used, along with its tests. The "several things need a look" notice now says "Open Agora to see them."
- **Open Agora** opens a packaged `Agora App.app` from `~/Applications` or `/Applications` if one is installed. Otherwise it runs `bun run app:start` in a source checkout: the Portal's own in development, else `~/kis/knowledge-islands/apps-agora.local`. The app's output goes to `~/.local/state/ki/agora/agora-app.log`. If neither exists, a notification says so. Opening the app clears the news dot. The decision logic is in `src/open.ts`, with tests in `src/open.test.ts`.
- Updated `docs/design/identity.md` (the Portal's menu, the status line, and the choices below), the README and the "what comes next" list in `docs/design/agora-app.md`.
- Commit `082daa6` feat(portal): slim the tray to the Agora Portal with Open Agora. `self:check` passed; `bun run test` passed (336 tests); `bun run build` passed. Nothing was installed or relaunched, so the installed `~/Applications/Agora.app` still shows the old menu until the households install.
- Choices I made:
  1. I kept **About Agora Portal** in the menu, because the rename is visible there.
  2. **Open log** now appears only in the menu shown when Agora is not configured. The log stays at `~/.local/state/ki/agora/agora.log`.
  3. I named the future packaged app `Agora App.app` (see Queries).
  4. When the Portal runs packaged, it falls back to the estate's standard checkout path.
  5. Sync now still reviews after it fetches.

## New and noteworthy

- Click **Open Agora** in the menu bar to open the Agora app. In development there is no `bun run app:start` to type.
- The menu bar is quiet: one line tells you who is here, or what needs a look, and the rest is for speaking to your agents.

## In Progress

Nothing. Not checked by hand: Open Agora was not clicked in a running Portal, because this run may not relaunch the Portal. The tests cover the choice of how to open the app, but not the actual launch.

## Queries

### Q1 - Name of the packaged Agora app

**Context:** The Portal's packaged bundle is already called `Agora.app`. Open Agora looks first for a packaged Agora app, which nobody has packaged yet. I had it look for `Agora App.app`.

**Query:** Is `Agora App.app` the right name for the packaged app, alongside the Portal's `Agora.app`?

**Options:**

a) (recommended, confidence medium - it avoids renaming what the households already install) Keep `Agora App.app` for the app and `Agora.app` for the Portal for now.

b) Rename at packaging time: the Portal becomes `Agora Portal.app` and the app takes `Agora.app`. This means updating the Portal's packaging, launch agent and installer.

### Q2 - Broadcast answers have no screen until the app shows them

**Context:** The tray's Broadcasts submenu was the only screen showing who has a broadcast and who answered a ping or a mark. The data is still in `outbox.json` and the read endpoint, but the Agora app doesn't show it yet. Candidate roadmap record: "Agora app: Broadcasts page (delivery and who answered)", which matches the app's planned Broadcasts page.

**Query:** Should the app's Broadcasts page come next, so ping and mark answers can be seen again?

**Options:**

a) (recommended, confidence high - Ping and Mark all now have no visible answers) Yes, make it the next app slice.

b) Leave it in the app's existing backlog order.

🧵 ki.prj.agora
