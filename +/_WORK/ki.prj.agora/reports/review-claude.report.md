# KI > Techne > Agora › review-claude

**🤖 → 👤 Handoff to supervisor · Run report at 20:46 GMT · last mark 00:04 GMT**

---

## Done

- Review only: no commit, no file changed, nothing pushed. Reviewed `main` at `4adbf38` from a clean `git archive` export, because the working tree holds another session's uncommitted phone and KIV work (`src/phone.ts`, `src/app/kiv.ts`, edits to `agora.ts`, `config.ts`, README) that is not on `main` and not reviewed here.
- No pull was made: the brief's body says "pull first", its Rules forbid every remote call, and the Rules win.
- `bun run self:check` on clean `main`: pass, with 22 Biome warnings (20 are `noDescendingSpecificity` in `src/app/renderer/app.css`). On the working tree it fails with one error from the other session's uncommitted work, not from `main`.
- `bun run test` on clean `main`: pass, 49 files, 461 tests. On the working tree: 50 files, 467 tests, pass.
- `knip` on clean `main`: two unused exports (`describeBroadcast`, `PRESENCE_WORD`); it under-reports because `src/**/*.test.ts` are entries (KNIP-GATE below).
- The other reviewer's report was neither looked for nor read.

## In Progress

Nothing. The review is complete.

## Findings

Findings are ordered most important first. Each carries a **Class** line: must-fix or nice-to-have. Sizes are S (an hour), M (a half day), L (a day or more). Line numbers are `main` at `4adbf38`.

### AGORA-CLASS - `Agora` is a composition root, a scheduler and six coordinators in one class

**Goal:** Make `src/agora.ts` a thin composition of parts that are each testable alone.
**Scope:** `src/agora.ts` (1252 lines), `src/agora.test.ts` (1091 lines), `src/review.ts`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix.

**Where.** `src/agora.ts:228-276` (constructor builds `LocalServer`, `MessagesWatch`, `Review`, `GitEvents` and `Waker` itself and re-wraps `deps.changed` and `deps.news`), `:277-290` (five `setInterval` timers plus a sixth for waking), `:312` `snapshot()` and `:380` `view()` (two parallel pictures of the same state, `view()` mapping `config.peers` and `config.watch` separately at `:389`, `:403`, `:422`), `:986-1005` (`readAccounts` and `readJobs` are the same ten lines twice, with `ACCOUNTS_MS` and `JOBS_MS` at `:120-122` both `60_000`), `:1132` `callAhead` and `:1200` `callSettle` (the same owners-then-log-then-`callPackage` loop). About 35 private fields.

**What is wrong.** The class owns peer exchange, the outbox, watching, syncing and settling, readings, the local view, waking and the timers. Its collaborators are constructed inside it, so `Review` has no suite of its own and cannot be replaced in a test; every Agora test builds the whole machine. The public surface used by production is only `start`, `stop`, `snapshot`, `view`, `broadcast` and `mark`, so the rest is internal reach.

**Why it matters.** Every fast change tonight landed here (accounts, jobs, settle calls, pushed signals), and the file grows again in the working tree (36 more lines in the other session's phone work). Each addition widens the blast radius and the suite that must be read to understand it.

**Refactor.** Keep `Agora` as the composition root and scheduler only. Lift three coordinators out, each with its own deps and suite: an `Exchange` (hello, ping, state, outbox flush, acks, `receive`), a `Calls` coordinator (`checkAhead`, `settle*`, `callAhead`, `callSettle`, `callPackage`, sharing one `callOwners(checkout, line)` helper), and a `Readings` coordinator (`readAccounts`, `readJobs` as one `readSource(kind)` with a map of readers and one `READINGS_MS`). Pass constructed collaborators in through `AgoraDeps` with the current constructor defaults, so a test can hand in a stub `Review`. Build `view()` from `snapshot()` rather than beside it. Size M to L. Risk medium: `agora.test.ts` is a wide safety net and should be split along the same seams (TESTS-GAPS).

### SHELL-LEAK - The two shells carry work that is not shell work

**Goal:** Keep `src/main.ts` and `src/app/main.ts` to Electron lifecycle and wiring, as `AGENTS.md` and `.dependency-cruiser.ts` intend.
**Scope:** `src/main.ts:311-348`, `src/app/main.ts:174-231`, `:467-566`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix.

**Where.** `src/main.ts:311` `ask()` builds about thirty lines of HTML and script as a string and loads them by a `data:` URL at `:348`; `:361` adds `Command+Q` to one menu item by matching the action id. `src/app/main.ts:467` `rehearse()` (about 85 lines of environment-driven `executeJavaScript` for screenshot checks) and `:552` `screenshot()` ship in the production main process. `:174-231` registers about twenty `ipcMain` handlers inline in `start()`, each repeating the `unknown`-to-typed check.

**What is wrong.** The ask page is a second renderer hidden in a string, with no file the renderer type-check (`tsc -p src/app/renderer`) sees. The rehearsal is a test harness living in the product. The IPC table is the app's API surface but is not visible as one.

**Why it matters.** The boundary rules are only as good as what the shells hold; the shells are exempt from the "pure" rules, so anything placed there escapes them. The ask page cannot be tested and is the Portal's only remaining UI.

**Refactor.** The ask page is live: the app's Broadcast and Away actions knock on the door (`POST /v1/do`), `speak()` at `src/main.ts:213` answers, and the Portal opens its own window to collect the words. The clean move is to let the app, which already has a window, collect the text and the Away choice and send them through the door as the finished action, so `ask()` and `awayWindow()` leave the Portal and the Portal keeps no page at all. Failing that, move the page to `src/app/renderer/ask.html` built by `tooling/app/build.ts` so the renderer type-check sees it. Move `rehearse()` and `screenshot()` to `src/app/rehearsal.ts`, loaded only when `AGORA_REHEARSE` is set, or to `tooling/`. Replace the inline handlers with one `bridge.ts` table `{ [channel]: handler }` typed by `CHANNELS`, with a `handle(bridge)` loop in `start()`. Size S to M. Risk low.

### ESTATE-PATHS - The estate's paths, URLs and rig names are hardcoded in six places

**Goal:** One source for where the checkout, the Observatory, Rig's source and the rigs' colours come from.
**Scope:** `src/open.ts:18`, `src/app/main.ts:51-52`, `:66`, `:312`, `src/app/updates.ts:15`, `src/app/renderer/index.ts:127`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix.

**Where.** The checkout path `~/kis/knowledge-islands/apps-agora.local` is written three times (`src/open.ts:18`, `src/app/main.ts:66`, `src/app/updates.ts:15`, the last inside a shell command string). The Observatory address and its start command are constants at `src/app/main.ts:51-52`. The chezmoi source path is at `:312`. The renderer colours rigs by name, `terra` and `sol`, at `src/app/renderer/index.ts:127`.

**What is wrong.** Configuration already owns the rig name, peers and the local port (`src/config.ts`), yet the app learns the rest from literals. A second household, a moved checkout or a third rig gets a wrong path or the fallback colour silently.

**Why it matters.** The README says Rig renders Agora's configuration from the rig list; these literals are the part Rig cannot render.

**Refactor.** Add an `[app]` table to the configuration (`checkout`, `observatory`, `observatory_start`, `rig_source`) with today's values as defaults in `DEFAULTS`, exposed through `readSettings()` so the renderer and `updates.ts` take them from the bridge. Colour rigs by their index in `config.peers` with this rig first, mapping to `--rig-0`, `--rig-1` variables. Size S to M. Risk low.

### DEAD-PING - Ping is kept as code with no sender, and five more exports are test-only

**Goal:** Nothing in `src/` that production cannot reach.
**Scope:** `src/agora.ts:606`, `src/broadcast.ts:124`, `:363`, `src/wording.ts:164`, `src/presence.ts:65`, `src/state.ts:175`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix (a decision; the edit is small).

**Where.** `Agora.ping()` at `src/agora.ts:606` has no caller outside tests since the Portal's menu went; `pingText` at `src/broadcast.ts:124` is reached only through it. `describeBroadcast` (`src/broadcast.ts:363`) and `PRESENCE_WORD` (`src/wording.ts:164`) are unused; `groupCount` (`src/presence.ts:65`) and `summarise` (`src/state.ts:175`, "the tray's one-line count") are used only by their suites.

**What is wrong.** The README's Ping section (`README.md:148-162`) already says nothing on screen sends a ping; the specification's goal 4 (`docs/spec/agora.md:23`) says Ping reaches every agent from the Agora app. The code sits between the two.

**Why it matters.** Dead sending code keeps a message kind, an outbox branch and a README section alive, and the next reader cannot tell whether it is a feature on its way or a leftover.

**Refactor.** Decide (Query Q1). If Ping goes: remove `ping()`, `pingText` and the `ping` describe block in `agora.test.ts:866`, keep answering and acknowledging (`answerable`, `ack` message) because a mark takes the ping's path, and reword the README. If Ping stays: add it to the app's actions through the door (`DoorAction`), which closes the spec goal. Either way remove the four test-only exports or move them to the suites. Size S. Risk low.

### RUNNERS - Seven process runners and six tool locators, each slightly different

**Goal:** One way to run a tool and one way to find it.
**Scope:** `src/git.ts`, `src/account-tools.ts`, `src/job-tools.ts`, `src/ki.ts`, `src/orca.ts`, `src/tailscale.ts`, `src/app/islands.ts`, `src/tool-env.ts`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix.

**Where.** `execFile` is wrapped at `src/git.ts:9`, `src/account-tools.ts:58`, `src/job-tools.ts:23`, `src/ki.ts:26`, `src/orca.ts:24`, `src/tailscale.ts:38`, `src/app/islands.ts:23` and `:40`, with timeouts from 10 to 60 seconds, `maxBuffer` from the default to 16 MiB, and three ways of shaping the error. `gitText()` at `src/app/islands.ts:20` re-implements `git` from `src/git.ts:7` without `GIT_TERMINAL_PROMPT=0` and without trimming. `kiText()` at `:36` re-implements `kiRunner` from `src/ki.ts`. Locators: `findKi` (`src/ki.ts:16`), `findTailscale` (`src/tailscale.ts:28`), `findOrca` (`src/orca.ts:8`), `findBun` (`src/tool-env.ts:98`), `findRig` (`src/job-tools.ts:32`) and the `places` lists in `src/account-tools.ts:30` and `:38`, each with its own candidate list and its own signature.

**What is wrong.** The same concern, "run this tool with Agora's PATH and say which command failed" (the subject of commit `9587ac2`), is solved seven times. A fix to one, such as the full-PATH fix, must be repeated.

**Why it matters.** Tonight's PATH bug was exactly this class of drift.

**Refactor.** `src/run.ts` with `runTool(command, args, { timeout, maxBuffer, env, keepOutputOnError })` returning stdout and used by every runner, so `git`, `kiRunner`, `commandRunner`, `toolRunner`, `cliRunner`, `orcaRunner`, `gitText` and `kiText` become one-line specialisations or disappear. `findTool(name, { explicit, places, home, exists })` in `src/tool-env.ts` replacing the six locators, each keeping its candidate list as data. Size M. Risk low to medium: keep each caller's timeout and buffer deliberately, and keep `kiText`'s "stdout even on non-zero exit" as an option.

### PARSERS - Three front-matter parsers and two roadmap scans

**Goal:** One front-matter reader in the core, used by the roster, the Roadmap page and the Guilds page.
**Scope:** `src/roster.ts:160`, `src/app/roadmap.ts:77`, `:112`, `src/app/guilds.ts:85`, `:122`, `src/app/islands.ts:174-248`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix.

**Where.** `frontMatter` (`src/roster.ts:160`, strings and booleans), `recordFields` (`src/app/roadmap.ts:77`, strings and lists) and `skillFields` (`src/app/guilds.ts:85`, ordered pairs) parse the same YAML-ish block three ways; `unquote` is written twice (`src/app/roadmap.ts:112`, `src/app/guilds.ts:122`). `roadmapCounts` (`src/app/islands.ts:226`) walks the same folders as `readRecords` (`:179`) a second time with `frontMatter` instead of `parseRecord`, and repeats the folder list inline at `:227` though `ROADMAP_FOLDERS` is declared at `:174`.

**What is wrong.** Three parsers mean three answers to a quoted value, a list or a stray colon; a record the Roadmap page shows may count differently in the island panel.

**Why it matters.** The Roadmap and Guilds pages are tonight's additions; this is the moment to settle the parser before a fourth page (Activities, Live Artifacts) adds a fourth.

**Refactor.** `src/frontmatter.ts` in the core: `frontMatter(text): { fields: Map<string, string | string[] | boolean | null>, body: string }` with one `unquote`; `roster.frontMatter`, `recordFields` and `skillFields` become thin adapters or go. Derive the island panel's counts from `readRecords` (or a shared `scanRecords(root)`), and use `ROADMAP_FOLDERS` in both. Add the new module to the `core` list in `.dependency-cruiser.ts`. Size M. Risk medium: the three suites (`roster.test.ts`, `roadmap.test.ts`, `guilds.test.ts`) pin the current behaviours and must all stay green.

### HELPERS - Small helpers copied across modules

**Goal:** Each small helper written once, in a core module both the Portal and the app may import.
**Scope:** `src/state.ts`, `src/roster.ts`, `src/jobs.ts`, `src/accounts.ts`, `src/wording.ts`, `src/app/words.ts`, `src/app/guilds.ts`, `src/app/activity.ts`, `src/talk.ts`, `src/app/islands.ts`, `src/packages.ts`, `src/review.ts`.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (S, do it with PARSERS).

**Where.** `isRecord` four times (`src/state.ts:375`, `src/roster.ts:300`, `src/jobs.ts:67`, `src/accounts.ts:271`); `isoTime` and `shown` twice each (`src/jobs.ts:71`, `:81`, `src/accounts.ts:81`, `:286`); `plural` four times (`src/wording.ts:61`, `src/app/words.ts:108`, `src/app/guilds.ts:228`, `src/app/activity.ts:53`); `clock` three times with two meanings (`src/wording.ts:267`, `src/app/words.ts:89`, `src/app/jobs.ts:51`); the work-id pattern three times (`src/talk.ts:36`, `src/app/islands.ts:47`, and a looser one at `src/files.ts:22`); the one-mebibyte ceiling at `src/packages.ts:8` and inline at `src/app/islands.ts:273`; a bounded worker pool at `src/app/islands.ts:113` and again as `Review.each` at `src/review.ts:181`.

**Refactor.** `src/json.ts` (`isRecord`, `isoTime`, `shown`), `src/ids.ts` (`WORK_ID`, `MAX_FILE_BYTES`), `src/pool.ts`, and a core `src/words.ts` (`plural`, `clock`, `ago`) that `wording.ts` and `app/words.ts` import. Each goes into the `core` list in `.dependency-cruiser.ts`. Size S. Risk low.

### TRAY-DUP - The tray icon's states are declared twice and the bundle id three times

**Goal:** One declaration of the tray's looks and one of the app id.
**Scope:** `tooling/icons/tray.ts:17-19`, `:94`, `src/wording.ts:21-24`, `:52`, `tooling/install/install.ts:34`, `src/bundle.ts:2`.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have.

**Where.** `tooling/icons/tray.ts` declares `Presence` and `TrayState` and names icons in `trayName()`; `src/wording.ts` declares `TrayPresence` and `TrayLook` and names them in `trayIconName()`. `tooling/install/install.ts:34` redefines `APP_ID` rather than importing it from `src/bundle.ts:2`.

**Why it matters.** A renamed icon state drifts between what is drawn and what is looked up, and nothing fails until the tray shows the wrong image.

**Refactor.** Move `TrayPresence`, `TrayLook` and `trayIconName` to a small `src/tray-look.ts` in the core (`wording.ts` cannot join the core because it imports `Snapshot` from `agora.ts`); have `tooling/icons/tray.ts` import it and derive `allTrayStates()` from the type. Import `APP_ID` in the installer. Size S. Risk low.

### RENDERER - One 2380-line renderer with 33 globals holds every page

**Goal:** A page per file with its own state, the router thin.
**Scope:** `src/app/renderer/index.ts`, `src/app/renderer/app.css` (1953 lines).
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (L), but the CSS warnings are must-fix (S).

**Where.** `src/app/renderer/index.ts` has 33 top-level `let` variables and 79 functions: the map (`:183-636`), the tray panels (`:636-1018`), Accounts (`:1070`), Roadmap (`:1141-1413`), Guilds and the skill pane (`:1425-1695`), Jobs (`:1695`), Settings (`:1855`), Updates (`:1885`), search, keyboard, theme. `app.css` carries 20 `noDescendingSpecificity` warnings, the whole of tonight's warning count.

**What is wrong.** Page state is shared mutable module state; a Roadmap filter and a Guilds selection sit beside the map's zoom in one scope. The renderer has no tests by design, so size is its only guard. No `innerHTML` is used anywhere, which is right.

**Refactor.** `renderer/pages/{accounts,roadmap,guilds,jobs,settings,updates}.ts`, each exporting `show(root, bridge, state)` with its own module state; `renderer/dom.ts` for the `html()` helper and `renderer/state.ts` for what pages share (model, selection, theme). Split `app.css` by page and reorder the twenty rules Biome names. Size L for the split, S for the CSS. Risk medium: the rehearsal screenshots (`rehearse()`) are the only check, so do it page by page.

### KNIP-GATE - Dead code is not found because tests count as entry points, and knip is not a gate

**Goal:** `self:check` catches an export only a test uses.
**Scope:** `knip.json`, `package.json` scripts.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (S).

**Where.** `knip.json` lists `src/**/*.test.ts` as `entry`, so `groupCount`, `summarise` and `ping()` count as used; knip reported only two exports. `self:check` runs `tsc`, `tsc -p src/app/renderer` and `biome check`, not knip; the pre-commit hook runs lint-staged and syncpack only.

**Refactor.** Let knip's Vitest plugin own the suites (drop the test entry), keep `*.test-support.ts` as project files, and add `knip` to `self:check` (or a `self:deps` script the hook runs). Size S. Risk low.

### TESTS-GAPS - Six modules have no suite, and the Agora suite is the only cover for Review

**Goal:** Each I/O module with a suite that drives it through a stub, and `Review` tested alone.
**Scope:** `src/review.ts`, `src/server.ts`, `src/git.ts`, `src/account-tools.ts`, `src/job-tools.ts`, `src/app/update-tools.ts`, `src/protocol.ts`, `src/agora.test.ts`.
**As of:** `main` at `4adbf38`.
**Class:** must-fix for `review.ts` and `server.ts`; nice-to-have for the rest.

**Where.** No sibling suite for `review.ts` (keeping level, the disabled fast-forward while a run works, `PARALLEL`, `describeUnresolved`), `server.ts` (trust by Tailscale identity, the 512 KiB body limit at `src/server.ts:5`, the refusal reply; `Refused` is exercised only through `agora.test.ts` and `broadcast.test.ts`), `git.ts`, `account-tools.ts`, `job-tools.ts`, `app/update-tools.ts`; `protocol.ts`'s `parseMessage` is exercised only through `state.test.ts`. `agora.test.ts` (1091 lines, six describes at `:124`, `:230`, `:584`, `:723`, `:866`, `:982`) is the only cover for `Review`, which `Agora` constructs itself (`src/agora.ts:251`).

**Why it matters.** `review.ts` and `server.ts` carry the two rules `AGENTS.md` cares most about: never more than a fast-forward of a clean checkout, and never a request from anyone but a configured peer of the same user.

**Refactor.** `review.test.ts` on temporary repositories from `git.test-support.ts` (clean-behind fast-forwards; dirty, ahead, diverged and a run's checkout do not); `server.test.ts` with a stub `whois` for trust, the body limit and the refusal reply; `protocol.test.ts` for each message type's rejection cases. Split `agora.test.ts` along AGORA-CLASS's coordinators. Size M. Risk low.

### ISLANDS-IO - The lands reader mixes pure parsing with its runners

**Goal:** The parsers of `ki territory` output and Git logs cruised as pure.
**Scope:** `src/app/islands.ts`.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (S).

**Where.** `territoryHandles` (`:53`), `parseTerritory` (`:58`) and `parseCommits` (`:161`) are pure but sit with `gitText`, `kiText`, `readdirSync` and `readFileSync`, outside `appCore`, so the pure rule does not check them; `.dependency-cruiser.ts:22` describes `appCore` as including "which islands take part" though `islands.ts` is not in the list.

**Refactor.** Move the three parsers to `src/app/lands.ts` in `appCore`; keep `islands.ts` as the reader; make the comment match the list. Size S. Risk low.

### DOORBELL-TAIL - The doorbell's old path has no recorded end

**Goal:** The transition from `doorbell/` to `call/` has a stop condition in one place.
**Scope:** `src/files.ts:26-41`, `src/view.ts:110-111`, `:300`, `docs/api/view-v1.md:47`, `README.md`, `CHANGELOG.md`.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (a decision; Query Q2).

**Where.** `oldCallPath` (`src/files.ts:36`) and the double write in `callPackage`; `doorbellAt` beside `calledAt` in the view (`src/view.ts:110-111`, `:300`); the view contract (`docs/api/view-v1.md:47`). The docs are consistent with the code: the README, the protocol spec, the view contract and six CHANGELOG lines all describe the transition. What is missing is when it ends.

**Refactor.** One `OLD_CALL_PATH` constant with its removal note naming the condition ("when every watched package's thread waits on `call/`"), and a roadmap record for the removal, so the leftover is a planned step rather than a tail. Size S. Risk low.

### APP-COMPAT - The app carries compatibility for a Portal it is always installed with

**Goal:** No compatibility code for a pairing that cannot happen after `self:install`.
**Scope:** `src/app/main.ts:96`, `:359`.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (S).

**Where.** `refreshJobs` (`:96`, "for a Portal that predates carrying them") and `listen` (`:359`, "the Portal running predates message events") each keep a second path. Both apps build and install together from one checkout (`self:install` packages both), so the pairing exists only in development between a `self:start` Portal and an `app:start` app of different ages.

**Refactor.** Drop both paths, or keep them under one `olderPortal` flag with a removal note. Size S. Risk low.

### DOCS - What no longer matches

**Goal:** Documents say what the code does.
**Scope:** `docs/spec/agora.md:23`, `README.md:150`, `.dependency-cruiser.ts:22`.
**As of:** `main` at `4adbf38`.
**Class:** nice-to-have (S).

The README, `AGENTS.md`, the protocol spec and the view contract match the code closely, including the PORTAL-MINIMAL menu, the doorbell transition and the read-only Accounts and Jobs boundaries. The mismatches found: the specification's goal 4 says Ping is sent from the Agora app while the README says nothing on screen sends one (DEAD-PING); the `appCore` comment in `.dependency-cruiser.ts` names islands as pure (ISLANDS-IO). `MenuAction` still carries `'open log'`, reachable only from the not-configured menu, which is right but worth a comment.

## Top five

1. **Split `Agora`** into a composition root plus Exchange, Calls and Readings coordinators, with collaborators injected and `review.test.ts` added (AGORA-CLASS, TESTS-GAPS).
2. **One tool runner and one tool locator** replacing seven `execFile` wrappers and six finders, so the next PATH or timeout fix is made once (RUNNERS).
3. **One configuration source** for the checkout, the Observatory, Rig's source and the rigs' colours, rendered by Rig like the rest (ESTATE-PATHS).
4. **One front-matter parser** in the core for the roster, Roadmap and Guilds pages, and one roadmap scan (PARSERS, HELPERS).
5. **A dead-code pass that sticks**: decide Ping, remove the test-only exports, drop the rehearsal and ask page from the shells, and make knip part of `self:check` (DEAD-PING, SHELL-LEAK, KNIP-GATE).

## Queries

### Q1 - Does Ping stay?

**Context**

`Agora.ping()` and `pingText` have no production caller since the Portal's menu went (PORTAL-MINIMAL). The README says nothing on screen sends a ping; the specification's goal 4 says Ping reaches every agent from the Agora app. Answers and acknowledgements must stay either way, because a mark takes the ping's path.

**Query**

Should the sending side of Ping be removed, or added to the Agora app's actions?

**Options**

a) (recommended, confidence medium - the README already says nothing sends one, marks cover the "are you listening" need, and removing it closes a dead branch; the spec goal would then be reworded to Broadcast, Away, I'm back and Mark) Remove `ping()`, `pingText` and the ping suite; keep answering and acknowledging; reword README and the spec's goal 4.

b) Add Ping to the Agora app through the door, meeting the spec's goal 4 as written.

c) Leave it as it is and note it as a planned app action in the roadmap.

### Q2 - When does the old `doorbell/` path stop?

**Context**

Every call is written to both `call/<work-id>` and `doorbell/<work-id>`, and the view carries `doorbellAt` beside `calledAt`, until the old path stops. The code and the docs describe the transition but nothing names its end, which depends on threads outside this repository.

**Query**

What condition ends the double write, and where is it recorded?

**Options**

a) (recommended, confidence high - the condition is observable from Agora's own watched packages, and a roadmap record makes the removal a planned step) End it once every watched package's thread waits on `call/`, recorded as a roadmap record with the removal of `oldCallPath` and `doorbellAt`.

b) End it now, in the next release, and tell each thread by broadcast.

c) Keep both paths indefinitely.

🧵 ki.prj.agora
