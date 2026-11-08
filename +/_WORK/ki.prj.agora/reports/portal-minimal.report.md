# KI > Techne > Agora › portal-minimal

**🤖 → 👤 Handoff to supervisor · Run report at 05:50 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- Right-clicking the Agora Portal in the menu bar now shows only who is in the Agora (or the one thing needing a look), **Open Agora** and **Quit Agora Portal**. A left-click still opens Agora or brings it forward.
- **Away…** is now a button in the Agora app's toolbar, beside Mark all and Broadcast…. It opens a small Away window with 2, 4 or 8 hours, a time of day, and I'm back while an away is running.
- You'll see this once the households reinstall the Portal and the app. Nothing was installed this run.

## Done

- **The tray menu is down to four lines.** These are the status line, Open Agora, a separator and Quit Agora Portal. Broadcast…, Away / I'm back, Ping, Mark all, Sync now and About are gone from it. When Agora isn't configured, the menu shows what's wrong, where Agora reads its settings, Open log and Quit (About is gone from there too).
- **Speaking now lives in the Agora app.** Broadcast… and Mark all were already reachable through the Portal's door. Away wasn't, so I added it: the app's new Away… button asks the Portal to open its own Away window, and the Portal sends the away or back broadcast itself, as it did from the menu. The app's error message no longer says "use its menu in the menu bar".
- **Docs updated:** `docs/design/identity.md` (menu section, its choices and the menu mocks, including the not-configured one), the README's text mock and its Broadcast, Ping and Mark sections, and `docs/design/agora-app.md` (toolbar). `docs/walkthrough/` was not touched.
- **Commit** 98c367a `feat(portal): cut the Portal's menu to status, Open Agora and Quit; Away moves to the app`, pushed to main.
- **Checks:** `bun run self:check` passes (11 biome warnings, all of them already there before this run). `bun run test` passes 373 of 373, including new tests for the menu, the door accepting `away`, and reading the Away window's answer.
- **Choices I made:**
  - Ping, Sync now, Mark only and the No art tick now have no button anywhere, since your list of what to keep named only Broadcast, Away and Mark all. Mark all in the app marks with a Summary and with the art.
  - Agora still fetches on every event and on its 15-minute fallback, so nothing depends on Sync now.
  - The code behind ping and sync stays in Agora, unused by the interface, so it's easy to bring back.
  - The About panel was removed along with its menu item.

## In Progress

Nothing.

## Queries

### Q1 - The specification still says you speak to everyone from the tray

**Context:** Goal 4 in `docs/spec/agora.md` reads "You can speak to everyone from the tray", and counts it done when Broadcast, Away, I'm back, Ping and Mark all each reach every agent "from one tray action". After this change you speak from the Agora app instead, and Ping has no button. The specification governs the repository, and changing a goal is your call, so I left it as it was.

**Query:** Should goal 4 now say you speak to everyone from the Agora app, and should Ping stay in it?

**Options:**

a) (recommended, confidence medium - this matches what you asked for at 05:40 and keeps the goal testable) Reword goal 4 to "You can speak to everyone from the Agora app", done when Broadcast, Away, I'm back and Mark all each reach every agent from one button in the app, and drop Ping from the goal.

b) Reword it the same way, but keep Ping by adding a Ping button to the app's toolbar.

c) Leave the specification as it is for now.

Candidate roadmap record (not created): the specification change in Q1, if you choose a) or b).

🧵 ki.prj.agora
