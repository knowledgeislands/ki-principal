# KI > Techne > Agora › tray-tidy

**🤖 → 👤 Handoff to supervisor · Run report at 04:10 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The tray's top level is now short and calm: "10 agents on 2 Macs", then "All well", your actions, and five submenus (Agents, Macs and checkouts, Runs, Broadcasts, News) holding the detail.
- When something is wrong, line 2 says what ("2 need a look: 1 checkout, 1 agent not listening") and the submenu holding it says so in its label, so one click takes you there; when nothing is wrong, nothing extra shows.
- An agent whose thread is not listening, or a stranded run, now counts as needing a look and lights the diamond on the symbol.
- I'm back appears only while you are away, and the Away item then reads "Away until 08:00".

## Done

- Rebuilt the tray menu to Kris's TRAY-CALM order: two summary lines; Broadcast…, Away (I'm back only while away), Ping, Mark all; the Agents, Macs and checkouts, Runs, Broadcasts and News submenus; then Sync now, Open log, About and Quit. Commit `02a0291` (`feat: calm the tray: …`).
- The menu's shape now lives in a new pure module, `src/menu.ts`, with `src/menu.test.ts` checking the calm top level, the exceptions surfacing and the detail one level down; every computed line stays in `src/wording.ts` with tests. `src/main.ts` only turns the items into Electron's and carries out each action.
- Updated `docs/design/identity.md` (the menu section rewritten, with two text mocks, the line 1 and line 2 tables, the submenu labels and the choices made), the README (a text mock of the menu and the renamed items), and one line of `docs/spec/agora-protocol.md`.
- Checks: `bun run self:check` passed; `bun run test` passed (23 files, 280 tests); `bun run build` passed.
- Choices made, each recorded in `identity.md`:
  - "Mac" replaces "computer" on screen (menu, tooltip, notifications, About), following Kris's own words; "rig" stays in code.
  - Line 1 counts live agents (a finished package aside) on the Macs still in the group.
  - `All well` only when reviewed, listening, every Mac heard from and nothing to look at; with a Mac not heard from, line 2 reads `Nothing needs a look` and line 1 names the Mac.
  - What needs a look grows to agents definitely not listening and stranded runs; an agent whose listening is only unknown, and a territory member not kept, show inside their submenus and are not counted, so a missing field does not light the diamond.
  - Review now, Ask after the others now and the listening address moved into Macs and checkouts; Territories became a submenu there; Check for news now and Mark news as read moved into News; the Orca thread lines moved to the foot of Agents. "Ping threads" is now "Ping".
  - Times in the Broadcasts submenu now read `HH:MM`, as the voice guide sets, and "1 needs a look" is now grammatical.

## In Progress

- The installed `~/Applications/Agora.app` still shows the old menu until the households rebuild and install it on each Mac; this run installed nothing. The calm tray belongs with [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md)'s review and acceptance rather than a new record; no record was created.
- Not seen on screen: the menu is tested as a tree, but this run did not start Electron (a second copy would clash with the installed one's port).

## Queries

None.

🧵 ki.prj.agora
