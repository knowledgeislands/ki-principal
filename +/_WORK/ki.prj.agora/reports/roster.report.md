# [KI > Techne](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/techne.md) › [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md) › roster

**🤖 → 👤 Handoff to supervisor · Run report at 04:04 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- Each Mac's Agora now knows who is doing what on both Macs: every live agent, its territory, its focus areas with ⭐ ⏰ ⏸, whether it is listening, and how many messages wait for it.
- The tray has an **Agents** submenu listing each live agent and its focus areas. An agent that is not listening is marked ⚠︎.
- `curl -s http://127.0.0.1:1677/v1/roster.txt` prints your table (Mac, Territory, Work package, Focus areas, Listening), ready for the KIV, the Observatory or a summary footer.
- You can ask the address book who covers something: `curl -s 'http://127.0.0.1:1677/v1/lookup?q=kiv'` lists the live agents whose focus id matches first, then those whose focus line mentions the word. It only suggests; nothing is sent.

## Done

- **Roster built** in apps-agora.local, commit `d4a6878` (`feat: show who is doing what, with the focus address book`), pushed to `main`.
  - A new pure module, `src/roster.ts`, reads each watched package's `work.md` (title, territory, the `## Focus` list with ids, ⭐ ⏰ ⏸ marks and each line's words), `state.md` front matter (state, since, listening_enabled, listening_status) and `messages.md` (Inbound lines waiting, ACK lines aside; Outbound lines awaiting ACK). It also builds the plain table and the `lookup` address book. Its new I/O edge, `src/packages.ts`, reads these files from the checkout on disk and does no extra fetch. `.dependency-cruiser.ts` now lists `roster` in the pure core.
  - The roster is read at each review and after each messages check. It travels in the state picture the Macs exchange, so each Mac holds both Macs' rosters, and it is written to `state.json`. A picture from an older Agora without a roster is still accepted.
  - The read-only local endpoint adds a `roster` field to `/v1/state`, plus `/v1/roster` (JSON), `/v1/roster.txt` (plain table) and `/v1/lookup?q=<word>`. `docs/api/view-v1.md`, the README (new "Who is doing what" section) and the CHANGELOG describe them.
  - The tray adds an **Agents** line, such as `Agents: 10, ⚠︎ 2 not listening`. Its submenu has one line per live agent, such as `⚠︎ terra · personal.reg.inbox-terra: capture ⭐; not listening; 2 waiting`.
- **Rebased onto the settle slice:** another `ki.prj.agora` run pushed `c6ba5e1` (settle) while this run worked. The conflicts were all additions in the same places (`settles` beside `roster`), so I kept both sides unchanged and regenerated the example payload. All checks were re-run on the combined code before pushing.
- **Checks:** `bun run self:check` passes. `bun run test` passes, 267 tests in 22 files. rumdl passes on README, CHANGELOG and the API page. A read-only run against this Mac's four real packages parsed every title, focus line and listening field correctly.
- **Choices made:**
  - Territory is the first part of the `work.md` title (`KI`, `Personal`, `HNR`), or the first part of the work id when there is no title.
  - Listening means `listening_enabled: true` and `listening_status: on`. It is `unknown` when `state.md` has neither field, and `not listening` otherwise.
  - "Live" means every watched package except one whose state is `finished`. On-hold packages still show.
  - Address-book order: exact focus id before a match in the line's words (whole words, any case). Within each, listening agents come first and paused (⏸) focus areas come last.
  - Holding areas (`_emerging`, `aside`) stay in the table and the tray as written in `work.md`.
  - The view now carries the focus lines' words and titles, which is wider than its earlier "no file contents" promise. It still carries no message lines, only their counts. The API page states this.
  - The tray's Agents submenu lists up to 12 agents and counts the rest, like the other submenus.

## In Progress

- Nothing from this run. The new build reaches Kris only once the households install it on sol and terra (AGORA-INSTALL-GRANT). Each Mac shows the other Mac's roster only once both run the new build.
- Roadmap record candidates, not created: `KI-AGORA-NET-002` "Who is doing what: roster and focus address book" (this slice, to record as built), and a follow-up "Route from the tray: ask the address book who covers a word". HEALTH-TIERS could later use the roster's listening field and the ⚠︎ mark when it moves into Agora.
- The tray-tidy run (TRAY-CALM) should decide where the Agents line sits among the two summary lines and the submenus.

## Queries

None.

🧵 ki.prj.agora
