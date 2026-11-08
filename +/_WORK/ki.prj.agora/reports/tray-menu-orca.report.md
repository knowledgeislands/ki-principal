# KI > Techne > Agora › tray-menu-orca

**🤖 → 👤 Handoff to supervisor · Run report at 20:28 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Portal's tray now works like Orca's. A click or a right-click shows one menu: Open Agora, then Settings… and Check for Updates…, then Quit Agora and Quit Agora Completely.
- Orca's meanings match the brief. Orca's plain Quit leaves its sessions running, and its Quit Completely stops them too. So Quit Agora closes only the app and the Portal stays in the group, while Quit Agora Completely closes both and this Mac leaves the Agora.
- Orca lists Quit Completely above Quit. I kept the order Kris gave, with plain Quit first (query Q1).
- Settings and Updates are now real pages in the Agora app's sidebar. Settings has replaced the greyed "Settings, coming later" entry. Screenshots of both pages from a throwaway capture run looked right.
- None of this shows on Kris's Mac until the households run the install. The installed app predates the build-commit record, so Check for Updates only works from the next install on.

## Done

- **Commit 9b5d615** `feat(portal): give the tray Orca's menu, with Settings and Check for Updates in the app`, pushed to `origin/main`. Checks: `bun run self:check` passed and `bun run test` passed (46 files, 445 tests). Both ran on a clean worktree of `origin/main` plus this change, because another run has unfinished Guilds work in the main checkout. Both typechecks also passed on the main checkout with that work in place.
- **Tray** (`src/menu.ts`, `src/main.ts`): the menu is set as the symbol's own menu, so both clicks open it. The status line has moved out of the menu and now leads the tooltip, for example `Agora Portal. 3 need a look: … . 10 agents on 2 Macs`. The icon keeps its diamond and count. ⌘Q sits on Quit Agora, as Orca puts it on its plain Quit.
- **Opening the app on a page, or closing it:** the Portal starts the app with `--agora-place=settings`, `--agora-place=updates` or `--agora-quit` (`src/app/request.ts`). If the app is already open, it gets the flag through its single-instance lock and turns to the page or closes. If it is closed, it opens on the page, or does nothing for a quit.
- **Settings page** (read only): shows the configuration file path, this Mac's name, its peers, the watched packages and the local view's port, with an Open in Editor button. Changing settings stays open under CONFIG-OWNER.
- **Updates page:** fetches apps-agora.local and counts how many commits `origin/main` has beyond the commit the app was built from. It then says either `Agora is up to date (<commit>)` or `A newer Agora is available: <n> commits ahead`, followed by the install command and a Copy button. If the fetch fails, it says so. Agora installs nothing itself.
- **Build commit:** every app build, and so every packaging, now writes `dist/app/build.json` with the commit it was built from. The packaged app includes it.
- **Docs:** updated the specification's goal 4 (speaking happens in the Agora app, which the tray's Open Agora opens), the menu section of `docs/design/identity.md`, and the README's menu text.
- No install, packaging, app relaunch, roadmap record or other repository was touched.

## In Progress

- Nothing in progress.
- The other run's uncommitted Guilds work in `src/app/` is still dirty in the main checkout. My change sits under it, and the two were joined without conflict markers.

## Queries

### Q1 - Which Quit comes first in the menu

**Context**

Orca's tray lists Quit Completely above Quit. Kris's request listed "quit completely and quit" in that order, but the brief set plain Quit Agora first. I followed the brief.

**Query**

Should Agora keep plain Quit first, or copy Orca and put Quit Agora Completely first?

**Options**

a) (recommended, confidence medium - the brief set this order, and the safe choice, which keeps this Mac in the group, sits next to ⌘Q) Keep Quit Agora first.

b) Copy Orca exactly and put Quit Agora Completely first.

### Q2 - Two passages outside this run's docs are now out of date

**Context**

The brief allowed only spec goal 4, the identity menu section and the README. Two other passages now describe the old tray. Spec goal 5 says the tray shows what needs a look "at its top", which is now the tooltip and the symbol. `docs/design/agora-app.md` still lists Settings under Coming.

**Query**

May a small follow-up correct those two passages?

**Options**

a) (recommended, confidence high - each is a one-line wording fix that only follows what has shipped) Yes, in a short follow-up run.

b) Leave them as they are for now.

### Q3 - Should Quit Agora Completely ask first

**Context**

Orca asks for confirmation before Quit Completely, because it stops running agents. Agora's Quit Agora Completely takes this Mac out of the group straight away, as the old Quit Agora Portal did, and nothing is lost since Git stays the record.

**Query**

Should Quit Agora Completely show a confirmation first?

**Options**

a) (recommended, confidence medium - leaving loses nothing and restarting the Portal brings the Mac back, so a prompt would only slow Kris down) No confirmation, as now.

b) Add an Orca-style confirmation that says this Mac leaves the Agora.

🧵 ki.prj.agora
