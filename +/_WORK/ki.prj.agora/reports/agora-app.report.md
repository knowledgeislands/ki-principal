# KI > Techne > Agora › agora-app

**🤖 → 👤 Handoff to supervisor · Run report at 04:57 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- You can now open **the Agora**, a window showing all eight territories as island groups. Each island shows what it built this week, who is working there (councils, work packages and doers, coloured sol orange or terra teal), what waits on you and what needs a look. In apps-agora.local run `bun run app:start`.
- When one package sends a message to another, **golden light runs between their islands** and the line appears under "What is being said".
- **Click any island** to see who works there, the packages resting on it, its last ten commits and its roadmap counts. The **Repositories** and **Activity** tabs open the Observatory's own pages inside the window.

## Done

- **The Portal's feed now reports messages** (`5c1ad3c`). When a watched package's `messages.md` gains a line, its live stream sends a `message` event saying who sent it, to whom, its kind (message or ACK) and its id, never the words. The view also keeps the last 50 as a new `messages` field. Adding a field doesn't change the version, so it stays `view/v1`, and `docs/api/view-v1.md` documents it. The tray itself is unchanged.
- **The Agora app, first version** (`2bf4751`, `234cf98`). It is a second Electron entry, built and started with `bun run app:start`, and has one window with night and day themes in the Knowledge Islands look:
  - **Home is the civilisation map** and fits the window without scrolling:
    - Territories are dashed frames, islands are hex tiles, and the principal island has the larger tile.
    - Small blocks on a tile count its commits this week; today's are lit.
    - Faint dots show packages resting on an island; six stones show its meeting point.
    - Councils (State of play mains) have ringed marks, work packages round marks and doers (runs) square marks. Listening shows as solid, unknown as hollow, silent as struck through in red.
    - Each worker shows its ★ primary focus and how many messages wait for it.
    - A gold diamond marks a package handed to you. An amber or red `!` marks an island that needs a look.
    - Faint gold threads run up to each council, a short arc marks the great portal to terra, and golden light marks each message as it passes.
    - The sol, terra and Both planes buttons dim the other rig.
  - **The side panel** shows at a glance the work packages by rig, what waits on you and what needs a look (each click opens its island), when each rig was last heard, the latest messages, and a key.
  - **The island panel** shows its territory, checkout, health, workers with their state, listening and focus, resting packages, recent commits and roadmap counts.
  - **The tabs** show the Observatory's Repositories and Activity instruments from its local service on port 1675. If the Observatory is not running, the tab shows how to start it.
  - **Fallbacks:** without the Portal, the map still draws every island and shows a banner. If the Portal predates message events, the app reads the message files itself.
  - **The design note** is `docs/design/agora-app.md`, with screenshots of night, day and an island, what it shows, how it is built and what comes next. The README and CHANGELOG are updated.
- **How it is built:** Electron is only in `src/app/main.ts` and `src/app/preload.ts`. The model, layout, words and event reader are pure modules with tests. The window runs sandboxed and can reach only those pure modules. Four new boundary rules each have a deliberate crossing that proves they can fail.
- **Check run:** I started the app in development against the live Portal on sol several times, including through `bun run app:start`, and closed it each time; none is left running.
  - The map drew 8 territories and 63 islands, with 10 work packages on sol and terra and 8 doers.
  - It showed 1 package waiting on you and 5 notices.
  - Light ran between real islands (replayed from recent message lines).
  - The ki-principal panel loaded its commits, and the Repositories tab loaded the Observatory.
- **Checks:** `bun run self:check` passes. `bun run test` passes, 340 tests (up from 296). knip is clean. All three commits are pushed to `main`.

**Choices I made**

- **Data:** the app's main process follows the Portal's stream. The window can't do it directly, because the Portal refuses pages loaded from a file. Islands come from `ki territory list` and `ki territory show --format json`, which mark the principal island (`kind: owner`) and health. `ki` exits with an error when a territory has members not registered on this Mac, but its JSON is still whole, so the app uses it.
- **Who works where:** a package sits on the island that holds its `+/_WORK/<id>/` folder, which puts project packages on the principal island, as AGORA-APP-NOW says.
- **Roles:** a `*.sop.main` package is a council's leader. Every other watched package is an enabler. Each `ki agent` run is a doer, placed on the island it works in, or else on its package's island.
- **"Waits on you"** means a package whose state is `handoff-to-supervisor` or `with-supervisor`. It counts packages, not queries.
- **Needs a look:** a checkout that is behind, ahead, diverged, detached or broken; a settle; a blocked or stranded run; a silent package. A checkout that is only dirty counts as work in progress, not a notice.
- **Message events:** they are named `message` on the stream. After a restart the Portal first notes the lines already there, so nothing old replays. It reads only the packages this Mac watches.
- **The app hears messages itself** from every package folder on the islands: the ones the Portal doesn't watch, or all of them when the Portal running predates message events. That was the case on sol tonight, and I may not install a new Portal.
- **Senders with no island:** a sender with no island of its own (an old id, or a design session) sends from its territory's council, found from the id's first part (`ki`, `hnr`), or else from the recipient's council.
- **Tabs:** they use embedded Electron views rather than frames, because the Observatory forbids being framed. Each tab can only show pages from its own local address.
- **Layout:** there is no left rail yet; the tabs sit in the title bar. The design pack's other pages are listed in the design note as next steps.
- **Screenshots:** I committed only the map and the ki-principal panel. I checked the Observatory tab but didn't commit a picture of it, because it shows another app's data.
- **Separate app profile:** the app keeps its own Electron profile, so it never competes with the Portal for a single-instance lock.
- **Development-only settings:** a few environment variables (`AGORA_APP_CAPTURE`, `_ISLAND`, `_TAB`, `_REPLAY_TALK`, `_THEME`) let the check take its screenshots. They are documented in the design note.

**Possible roadmap records (none created):**

- Package the Agora app beside the Portal, plus the Portal's Open Agora item (`portal-slim`).
- Count open queries for "waits on you", not only packages.
- Fold the KIV's views in as tabs.
- Build the design pack's remaining pages: Who's doing what, What's being said, Broadcasts, Waits on you, Macs and the portal, Checkouts.
- Use the illustrator's art as the map's ground.

## In Progress

- Message events come from the Portal itself only once the households install this Portal build on each Mac. Until then the app hears messages on its own, so the lights still work.
- terra's work packages show "listening not known" for the same reason: terra's Portal isn't sending its roster yet.

## Queries

None.

🧵 ki.prj.agora
