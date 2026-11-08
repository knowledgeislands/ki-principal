# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › app-polish

**🤖 → 👤 Handoff to supervisor · Run report at 05:22 GMT · last mark 00:04 GMT**

---

## Done

- **The shell Kris asked for.** A toolbar runs across the top. It shows each rig's presence (this Mac first, a peer not heard from lately drawn hollow), one word on the whole (`All well`, `9 need a look`, `Portal not answering`; click it for the glance), the search, **Mark all**, **Broadcast…**, the time and the theme button. A sidebar runs down the left with Home, the Observatory's Repositories and Activity, and greyed places still to come: Inbox (for the KIV's views), Art gallery and Settings. It folds to icons with its button or ⌘\ and remembers its state, and its foot says whether the Portal is open. The map now fills the window.
- **The tray.** It slides out over the map's right edge for an island, a work package or doer, a message line, or the glance, and Escape or × closes it. A worker's tray is new: role, rig, state and since when, listening, messages waiting and awaiting an ACK, its island, the package that brought a doer in, its focus areas with their words, and what it lately said. A message line's tray shows who said it to whom, on which islands, and offers **Light it again**.
- **Zoom and pan.** Pinch or ⌘-scroll zooms about the pointer, a scroll or a drag moves the map, a double-click zooms in, and buttons at the lower left zoom and fit. The keys are `+` `−` `0` and the arrows. Movement glides, and the map cannot drift off into empty sea. Words grow more slowly than the land, so close in every island names itself and labels stay apart. Island names now draw above every tile, so a neighbouring island no longer hides one.
- **Search.** The toolbar search finds islands, packages and doers by name, territory, rig or focus area, best match first. Arrow keys choose, and Enter opens the result in the tray and glides the map to it.
- **Speaking through the Portal.** **Broadcast…** asks the Portal to open its own Broadcast window, where Kris writes the words. **Mark all** asks for one more click in place, then asks every listening thread to strike its mark with a Summary. Both go through a new door on the Portal: a private socket only Kris's user can open, taking only those two requests. The read endpoint stays read-only.
- **The look.** Land and sea use the illustrator's palette (sea-glass, moss, sandstone and cream) on the `ki-design` Instrument tokens, night and day. Tiles are drawn as low hexagonal islands, as in the app icon.
- **Pure tested modules** hold the logic: search (`src/app/search.ts`), the sidebar and toolbar words (`src/app/shell.ts`), zoom and pan (`src/app/viewport.ts`), and the door (`src/door.ts`, tested on its own temporary sockets). The boundary rules cover the new modules.
- **Docs.** `docs/design/agora-app.md` is rewritten around the new window, with five fresh screenshots from live data: home by night and by day, the glance, an island's tray by day, and a zoomed view. The README is updated.
- **Checked on live data** in development: all 8 territories and 64 islands drew, along with 10 work packages on 2 rigs, the doers, light passing, the tray, search, the folded sidebar, an Observatory page (it is running) and the placeholder pages, by night and by day.
- **Left running for Kris.** The development app is open on its own, detached from this run, with its output in `~/.local/state/ki/agora/agora-app.log`. **Open Agora** in the Portal brings its window forward.
- Commits `2d9c1af` (the Portal's door), `a8d723d` (the app's shell, tray, zoom and search) and `e17a2a0` (outline icons, gold count, picture rehearsals) are pushed. `bun run self:check` passes. `bun run test` passes all 36 files (358 tests).

Choices I made:

- **The door is a Unix socket.** It sits in an owner-only folder, `~/.local/state/ki/agora/door/portal.sock`, rather than being a write route on the read endpoint. The endpoint keeps its read-only promise, and the door follows the specification's entrance (a socket, never a network address).
- **Broadcast opens the Portal's own window.** The app does not take the words itself, so the Portal remains the only speaker.
- **Mark all means "Mark and summarise"**, the menu's first choice, with a confirm step because it reaches every thread on every Mac.
- **A plain scroll moves the map and a pinch zooms**, as in Maps on a Mac. ⌘ with the scroll wheel also zooms, for a mouse.
- **Some parts moved.** The old tab strip became sidebar places, the side panel's glance moved into the tray, and the key moved behind a **Key** button on the map. The map gets the whole width.
- **Settings is a placeholder**, because host settings are captured for later and out of scope tonight.

## In Progress

- **The installed Portal predates the door.** Until it is reinstalled from `main`, **Mark all** and **Broadcast…** in the app say the Portal is not running or predates its door, and point Kris to the Portal's menu. Everything else works against it. See the query below.
- **Roadmap candidates (not created):**
  - Reinstall the Portal with its door.
  - The remaining pack pages as sidebar places: Who's doing what, What's being said, Broadcasts, Waits on you, Macs and the portal, Checkouts.
  - The KIV's views under Inbox.
  - The illustrator's art as the map's ground (Art gallery).
  - Island feedback through the Portal's `say` once the entrance is built.

## New and noteworthy

- Find any island, package or doer from the toolbar: press `/`, type a name or focus area, then press Enter, and the map glides to it.
- Zoom into any territory with a pinch, `+` or a double-click, and press `0` to fit it back.
- Click anything on the map and its story slides out on the right; Escape puts it away. A worker's tray shows its focus areas and what it lately said.
- Mark all and Broadcast are one click from the app's toolbar once the Portal is reinstalled.

## Queries

### Q1 - Reinstall the Portal so the app's Mark all and Broadcast work

**Context:** The app's two speaking buttons reach the Portal through a new door that only the Portal on `main` has. The Portal installed in `~/Applications/Agora.app` was built before it. I was not allowed to install, and installing belongs to the households.

**Query:** Should the household on sol reinstall the Portal from `main` now, with terra's household following, so the buttons work?

**Options:**

a) (recommended, confidence high - the change is small and tested, and both buttons only ask the Portal to do what its own menu already does) Ask personal.reg.household-sol to run `bun run self:install` from `main`, and terra's household to follow.

b) Wait until the next planned reinstall, and use the Portal's menu for Mark all and Broadcast until then.

🧵 ki.prj.agora
