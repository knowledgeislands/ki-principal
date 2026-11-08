# KI > Techne > Agora › refactor

**🤖 → 👤 Handoff to supervisor · Run report at 21:36 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- Eleven small commits on `main`, each gated by `bun run self:check` and `bun run test`, all pushed fast-forward; `main` is level with `origin/main`.
- Seven real bugs the reviews found are fixed and named below; everything else keeps its behaviour.
- `Agora` has lost its ahead and settle calls and its sampled readings to their own modules; every tool runs through one process runner; front matter is read in one place; the estate's paths are named once.
- knip now gates `self:check`, so a dead export fails the check rather than waiting for the next review.
- The `doorbell/` write stays, as asked; Ping stays as code, and the docs now say nothing sends one yet.
- Nothing was installed, packaged or relaunched; no other repository was touched; no roadmap record was created. The installer fix is therefore proven by its suite, not by an install.

## Done

**The merged list.** The two reviews agree on seven things: `Agora` does too much in one class (AGORA-CLASS, AGORA-COHESION); the two shells carry work that is not shell work (SHELL-LEAK, APP-COMPOSITION); one renderer holds every page (RENDERER, WINDOW-COHESION); front matter and the roadmap are read three ways (PARSERS and HELPERS, ROADMAP-READING); dead code lingers and nothing gates it (DEAD-PING and KNIP-GATE, LEGACY-SURFACE); the docs have drifted (DOCS, DOC-DRIFT); and the suites leave the composition thin (TESTS-GAPS, TEST-SEAMS). Only Claude saw ESTATE-PATHS, RUNNERS, TRAY-DUP, ISLANDS-IO, APP-COMPAT and the CSS warnings. Only Codex saw STARTUP-GUARD, OUTBOX-DURABILITY, TAB-RACE, JOBS-TRUTH, INSTALL-GATE, READ-BOUNDS, BOUNDARY-COVERAGE and the jobs placed through the lands. They differ in three places. On Ping, Claude would remove it or give it a sender and Codex keeps it live: I keep it, since the brief and the specification's goal 4 name it, and the docs now say so plainly. On the sync guard, Codex asks for a fresh successful `ki agent status` before any fast-forward and one queue per checkout: I read the runs before the first sync and hold that sync to the rule, which closes the real bug, but a later failed read keeps the last reading and logs rather than halting every fast-forward, because one `ki` failure would otherwise stop the keeping-level the rig exists for; whether a stale reading should hold is a policy call, listed below. On the shape of the split, Claude names three coordinators and Codex extracts the sync workflow: I took the two seams that were clean tonight, the calls and the sampled readings, and the exchange (broadcasts, outbox, acknowledgements) is the next seam.

**The real bugs, each named in its commit.** The start-up sync could fast-forward a checkout a running agent was working in, because the runs were read after it (STARTUP-GUARD). A tab load abandoned mid-way could cover the page chosen after it (TAB-RACE). Rig's jobs could not be placed until the lands had been read, and the rig source was read once from them (Codex's jobs hazard, ESTATE-PATHS). A broadcast whose outbox could not be saved was reported queued (OUTBOX-DURABILITY). The Jobs page said every last run ended well when no run was recorded, and worded a calendar it could not say (JOBS-TRUTH). The installer went on when the app had not quit and removed the old bundle before the new one was in place (INSTALL-GATE). A work record whose title is a folded or literal block vanished from the Roadmap page, and a skill's list field showed nothing (ROADMAP-READING, PARSERS).

**The commits**, oldest first, each gated green:

- `ca8238d` fix(sync): read the runs before the first sync, so start never moves a checkout an agent works in; adds `review.test.ts`.
- `9d2c9d9` refactor(agora): lift the ahead and settle calls and the sampled readings out of the class, into `calls.ts` and `sampled.ts` with its suite.
- `79cf6bf` refactor(tools): run every tool through one process runner (`run.ts`) and find each by one locator in `tool-env.ts`.
- `9a17c2c` fix(app): show the tab last asked for, place Rig's jobs without the lands, and name the estate once (`estate.ts`); the rehearsal leaves the app's main process for an Electron-free `rehearsal.ts`.
- `bf6cc1f` fix(broadcast): say when the outbox could not be saved, rather than reporting a durable queue.
- `46a7f99` fix(jobs): say no run is recorded, and show a calendar the words cannot say as declared.
- `1c67904` fix(install): stop when the Agora app does not quit, and copy each bundle in before removing the old; the bundle id comes from one place.
- `5ed8ff3` refactor(tray): name the symbol's images in one place, shared with the icon tooling.
- `07d0575` chore: remove the dead exports (`describeBroadcast`, `groupCount`, `summarise`) and gate `self:check` with knip.
- `f76ecb8` refactor(frontmatter): read front matter in one place (`frontmatter.ts`, `json.ts`), and scan an island's roadmap once with bounded reads.
- `63a2d70` docs: the how-it-works page, the app design note's sidebar, door and module table, and the README's test and check lines now match the code.

**Checks.** Before each commit `bun run self:check` and `bun run test` passed; after the last, both pass again with 54 suite files and 492 tests, and the boundary suite holds with the new modules named in `.dependency-cruiser.ts`. Every push was a fast-forward.

## In Progress

Nothing is unpushed or half-done. These were left on purpose, as candidates, no record created:

- **The exchange out of `Agora`**: broadcasts, the outbox and acknowledgements are the next clean seam; `Agora` is 1130 lines from 1288 and still the composition root. Left because it touches delivery and retry together and wanted a night of its own.
- **The renderer split by page**: 2405 lines with shared globals (RENDERER, WINDOW-COHESION). Left because it changes nothing the person sees and is too large for small gated commits tonight.
- **The app's controller out of its main process** (APP-COMPOSITION): the rehearsal is out; the data coordination is still in the shell.
- **Ping's sender**: either a `ping` verb at the Portal's door and a button in the app, or reword the specification's goal 4. Kept as code per the brief.
- **The sync policy on a failed `ki agent status` read**: today the last reading stands and the failure is logged; Codex would hold every fast-forward until a fresh read succeeds. A policy choice for Kris when convenient.
- **The rigs' colours and an `[app]` section rendered by Rig** (ESTATE-PATHS): the paths are now in `estate.ts`; moving them into configuration changes Rig's rendering in another repository.
- **APP-COMPAT**: the app still carries compatibility for an older Portal; removing it changes behaviour on a mismatched install, so it waits with the `doorbell/` tail.
- **The `doorbell/` write**: kept until Kris says it can go; the README names its end.
- **BOUNDARY-COVERAGE**: the cruiser's pure lists name modules by file, so a new module is unguarded until named; a rule by folder would mean moving files.
- **Suites for `server.ts` and the lands reader's runners** (TESTS-GAPS, ISLANDS-IO): the reader's roadmap scan is now shared and bounded; its process runners still sit beside its parsing.
- **19 `noDescendingSpecificity` warnings in `app.css`**: reordering rules can change the cascade, so it is a styling pass with a look at the window, not a blind refactor.
- **The installer's fix proven by an install**: the next install, by the household, is the test the brief did not allow tonight.
- **A shared `plural` in `words.ts`**: the last small helper copied across modules (HELPERS).

## Queries

None. Nothing tonight needed a decision only Kris can make; the policy choices above wait as candidates.

🧵 ki.prj.agora
