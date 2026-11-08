# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › kiv-embed

**🤖 → 👤 Handoff to supervisor · Run report at 20:36 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- The Agora app now has the KIV in its sidebar. The "Inbox… comes later" placeholder has gone, and in its place are two groups. **KIV · Knowledge** holds Captured, Context, Curated and Actions. **KIV · Tools** holds Graph atlas, Tending and Key. Each is a tab that opens the KIV's own page (`/view/captured`, `/view/context`, `/view/curated`, `/actions`, `/graph`, `/tending`, `/key`) on 127.0.0.1, the same way the Observatory's Repositories and Activity tabs work.
- If the KIV is not running, the tab offers a **Start the KIV** button, with the command beside it.
  - Pressing it starts the KIV's server from the Inbox as Agora's own child process, on this Mac and on loopback only, and points it at this Mac's Agora view.
  - The tab says "Starting the KIV…" while it waits, then opens the page.
  - If the KIV can't start, the tab gives the reason and the command to run by hand.
  - Agora stops a KIV it started when the app quits. A KIV that was already running is used as it is and never stopped.
- Agora's configuration has a new `[kiv]` section: `port` (default 4747) and `inbox` (default `~/kis/personal/inbox`).
- The specification, `AGENTS.md` and the app's design note now say the KIV belongs to ki.prj.agora (KIV-TO-AGORA), embedded for now with its code still in the Inbox. The old conflict note, C19, is marked settled for the KIV.
- The KIV notes the brief pointed to (`personal.reg.inbox-sol/kiv/` with `kiv.md`, `designer-queue.md` and the 1 November handoff) are not in the Inbox checkout. I worked from the KIV's README and its code instead.

## Done

- e352778 `feat(app): embed the KIV as tabs in the Agora app, starting it on request`, pushed to `origin/main`.
  - `bun run self:check` passed on a clean worktree of `origin/main` with this change. The only new item is one more CSS-ordering warning of a kind the file already has many of; there are no errors.
  - `bun run test` passed: 474 tests in 51 files, including new ones for the KIV tabs, the start/stop logic and the `[kiv]` setting.
- I have not seen the KIV tabs in a running window, because the brief rules out launching any app. The first time it opens, check that the Start button brings a tab up.

## In Progress

Nothing is in progress. These are candidates for the later slice that moves the KIV's code into apps-agora. I have created no roadmap records:

- **Code:** `packages/kiv/` in the Inbox: `serve.ts`, 17 modules under `lib/`, `assets/`, `board/`, `no-registry.ts`, plus `kiv.test.ts`, `matrix.test.ts` and the browser tests (`e2e/`, `e2e.config.ts`, including the screenshot references in `e2e/look.e2e.ts-snapshots/`).
- **Dependencies:** the pinned `d3` 7.9.0, which it serves from `node_modules/`, and `e2e` 0.22.0 with its Chromium install. These Inbox scripts would need equivalents in apps-agora: `self:kiv:start`, `self:kiv:dev`, `self:kiv:e2e*` and the `bun test packages/kiv` part of the Inbox's `test` script.
- **Data paths into the Inbox:**
  - It reads the Inbox's `knowledge/` areas (`captured`, `context`, `curated`, `actions`).
  - Its default `--root` is the Inbox repository two folders above the package. Once the code moves, that default must become a configured Inbox path.
  - It reads `packages/kig/considered.md` and the KIG checks for Tending.
  - It reads the dotfiles checkout and the work roots for Focus, Workers and Packages.
- **Its one write:** deferring an action card through `POST /defer`. That raises the boundary question below.
- **Tests and boundaries:** its Bun tests would need to run under Agora's Vitest, or alongside it. It would also need a place in `.dependency-cruiser.ts`. Its HTML pages are a different style from the app's own pages, so whether they become native views is its own decision.

## Queries

### KIV-WRITE - the KIV's one write against "Agora never edits knowledge"

**Context:** Agora's specification and `AGENTS.md` say Agora never edits knowledge. The KIV, which Agora now owns, has one write: on its Actions page, a person can defer an action card. That changes the card's due date and urgency and adds one line to it, without committing. The embedded Actions tab still allows this. I recorded it in the specification as open for you, without settling it.

**Query:** Should the KIV keep its defer action now that it is Agora's?

**Options:**

a) (recommended, confidence medium - it is a deliberate edit you make with a click, it commits nothing, and taking it away would lose a working feature) Keep it as the one named exception, and say so in the boundary.

b) Turn deferring off in the app's KIV tabs, so the embedded KIV only reads.

c) Leave the change to an Inbox-owned tool and drop it from the KIV when its code moves to Agora.

🧵 ki.prj.agora
