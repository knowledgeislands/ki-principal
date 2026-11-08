# [KI > Techne > Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › fold-in

**🤖 → 👤 Handoff to supervisor · Run report at 05:44 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Agora map opens on **Focused**: only the islands taking part right now, each with its island portal lit and a small count of queued work and waiting messages under its name. Switch to **Everything** in the toolbar, or press `e` (and `f` to go back). Click an island to see why it is taking part and what is waiting there.
- You can keep the Agora window on top, or snap it to a half, a corner or the full height of the screen. Use the pin in the toolbar or the Window menu: Control-Option-P keeps it on top, and Control-Option with an arrow or U, I, J or K snaps it.
- Once the households install, Agora is two apps. **Agora Portal** sits in the menu bar: a click opens Agora, and a right-click shows its short menu. **Agora** is in Applications with the illustrator's island as its icon.
- The interaction spec now names the five ways agents talk, which each tool uses and which it should use. It also sets the word-chain test every new link must pass, with tonight's two games as its first results, says how a talking agent stays available by delegating, and names the three portals.

## Done

Every ask in the inbox since 04:40 GMT has been checked against `main`. Four were partly or wholly missing and are now done. The other three were already in place from agora-app and app-polish: the app shell with toolbar, left sidebar and right tray; zoom and pan with fit-to-view; and island detail on click.

- **The interaction specification** (`6830fbd`), in [docs/spec/agent-interaction.md](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/spec/agent-interaction.md). It gains four sections, and later sections are renumbered:
  - **Section 7, communication strategies.** The five named strategies are direct API, through the Agora Portal, shared mailbox, scheduled check and listening loop. A table gives what each of the seven harness profiles uses today and should use.
  - **Section 8, staying available by delegating.** An agent that communicates SHOULD delegate its work, choosing the model for each piece. Delegation is distinct from coordination. Each harness profile is marked as a one-man band or a business with a team.
  - **Section 9, the interaction test.** This is the themed word chain: last letter to first letter, Shiritori, and Geography or Atlas when on places. It runs 10 rounds, records latency and rule-keeping for each, and ends with the improvement question. Tonight's two games are its first results: both links pass, every word was valid, and no word repeated.
  - **Section 10, the three portals.** These are the island portal, the principal portal, and the planar portal on `krisb/ki-portal`, kept by the watchman, with how a message hops between them.
  - **The information architect's improvement** is adopted as the burst rule in Section 6.2: hold the turn open on the mailbox while talking, open a burst with one line, and close it with `QUIET`. Its measured wake-up lateness was added to its profile, and its game row in Appendix A was corrected from 4 rounds to 10.
- **The map and window** (`7f99d60`):
  - Focused (the default, remembered) and Everything, from the toolbar or the `f` and `e` keys.
  - Active islands are drawn with a lit beacon and a glowing edge; idle islands are faded.
  - A pill on each island shows its queued work (`▤`), messages in and not yet ACKed (`↓`), and messages out awaiting an ACK (`↑`). The island's tray adds "Taking part", "Queued work" and "Messages waiting".
  - Keep on Top and seven snap areas are available from the toolbar pin and the Window menu.
  - Opening the app again (a click on the Portal, or Open Agora) brings its window forward.
  - The new logic sits in pure, tested modules: `src/app/activity.ts` and `src/app/placement.ts`. Two screenshots from live data are in the design note.
- **Two installable apps** (`e605213`):
  - `bun run self:package` builds `Agora Portal.app`, with the meeting ring icon, and `dist/app-package/…/Agora.app`, with the illustrator's island icon from `identity/chatgpt/agora-app-icon.svg`. `self:package:portal` and `self:package:app` build one each.
  - `self:install` now installs both. It quits and replaces the old Portal at `~/Applications/Agora.app` with the viewer of that name.
  - A click on the Portal opens or brings forward Agora, and a right-click shows the menu.
  - Open Agora looks for `Agora.app` and passes over one that is still the old Portal.
  - README, CHANGELOG, identity and app design notes are updated.
- **"island portal", not "summit portal".** No "summit portal" was left in this repository. The map's "great portal" label is now the "planar portal", drawn from the `ki-portal` island. The only mention of "great portal" left is the spec's note that earlier drafts used that name.
- **Checks:** `bun run self:check` passes; `bun run test` passes (372 tests, up from 358). I packaged both apps locally into `dist/` only, with network calls blocked by a dead proxy, and checked the bundle names, executables, launch agent placement, the viewer's entry point and its icon. I did not open, install or launch the packaged apps.
- **The running Agora app (pid 44810) was left running and not restarted.** My builds rewrote `dist/app/` under it. It keeps running its loaded code, but if its window is reloaded (⌘R) it would pick up the new page with the old main process, and only the pin would do nothing until it restarts.

Choices I made:

1. **App names follow your 05:20 words, "Agora Portal" and "Agora".** This takes option b) of portal-slim's Q1, so that query is settled by your later message. To keep the households' install safe, the Portal keeps its bundle identifier and launch agent label, and only its name and executable change.
2. **Icons.** The Portal keeps the meeting ring. The viewer takes the illustrator's island icon, which was drawn as the "agora app icon".
3. **"Taking part"** means a non-finished worker on the island, a run in state `running`, a message line to or from it in the last 2 hours, or commits today. Focused also keeps each territory's principal island, so the route up to the principal portal still shows, and hides territories with nothing taking part.
4. **"Queued work"** is roadmap records whose status is `triage`, `draft`, `ready`, `now` or `next`, plus runs in state `queued`. The roadmap counts are now read with the lands, every 3 minutes.
5. **Snap areas** are left half, right half, the four corners, and full height (which keeps the window's width). The keys are Control-Option, the same on every Mac. Pin and snap are not remembered across launches; that is listed as a next step.
6. **Portal click.** When Agora is configured, a left click opens the app. When it is not configured, a click shows the menu so setup stays reachable. The tooltip says "Click to open Agora, right-click for the menu".
7. **The word-chain test's pass rule is my proposal.** A link passes when all 10 rounds are played, each round after the first comes back within the receiver's stated conversation interval (30 seconds at most), the first round comes back within its idle interval plus a minute, breaches are named, and the improvement answer is recorded.
8. **Delegation profiles.** Claude Code is "a business with a team". Codex, Claude Desktop and Claude Design are "one-man bands", and for Codex this is marked as not yet verified. For runs it is set by the brief.
9. **Capture profile.** A screenshot check now uses its own profile, so it runs beside an open Agora app without touching it.

## In Progress

- **Not checked by hand:**
  - the Portal click and right-click, because I may not relaunch the Portal;
  - the packaged viewer starting, because it shares its single-instance lock with the running development app, and I may not install;
  - pin and snap in a live window: the menu and bounds are unit-tested, but the window itself was only screenshotted.
- **Roadmap candidates (none created):**
  - Remember pin and snap across launches.
  - Let the Focused window (2 hours) and the queued statuses be set in configuration.
  - Run the interaction test through the Portal once its entrance exists, recording each link's result.
  - Verify whether Codex can run helpers while it answers, as one-man band or team.
  - Draw the planar portal's own island once `ki-portal` carries traffic between planes.

## Queries

### Q1 - Install both apps on sol, then terra

**Context**

The households' `bun run self:install` now installs two apps. Agora Portal moves to `~/Applications/Agora Portal.app`, and the Agora app takes `~/Applications/Agora.app`, replacing the old Portal there. The Portal keeps its bundle identifier and launch agent, but macOS may ask once more to allow it in the background, because the app's path and ad-hoc signature change. This also covers app-polish's Q1: the reinstall that makes the app's Mark all and Broadcast work.

**Query**

Should the households install both apps from `main` now?

**Options**

a) (recommended, confidence high - everything it installs is tested and the old Portal is quit and replaced cleanly) Ask personal.reg.household-sol to run `bun run self:install` from `main`, approve the background item if macOS asks, and have terra's household follow.

b) Wait for the next planned reinstall, and keep opening the app with `bun run app:start` until then.

🧵 ki.prj.agora
