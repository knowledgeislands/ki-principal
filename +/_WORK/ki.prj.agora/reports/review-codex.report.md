# KI > [Techne](</Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/techne.md>) > [Agora](</Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md>) › review-codex

**🤖 → 👤 Handoff to supervisor · Run report at 20:41 GMT · last mark 00:04 GMT**

---

## Done

Independently reviewed committed local `main` at `4adbf3846560f26631498224ffa2aaf4b306adf8`: the Portal, app, Accounts, Roadmap, Jobs, Guilds, compatibility paths, tests, tooling and current documentation. No other reviewer's report was read.

`bun run self:check` passes on that baseline.

`bun run test` passes: 49 suites, 461 tests, including the boundary checker's deliberate violations.

Isolated probes confirm the initial sync bypass, successful-looking broadcast despite failed persistence, native-tab race, misleading job wording and omitted folded-title roadmap record. They used stubs and temporary files, without starting Electron or contacting a service.

Optional local Knip analysis reports two unused exports; this cleanup failure is separate from the passing required checks.

No repository files changed, no commits, no installations, packaging, app operations or remote calls. The task's instruction to pull was superseded by its explicit no-network rule. A temporary snapshot excluded the checkout's concurrent uncommitted work and was used for review and checks; its temporary files have been removed.

Read the existing shared run inbox. Its historical instructions address earlier app, design, documentation and integration runs; they provide background only and do not change this review's read-only scope.

## In Progress

Nothing running.

Outstanding — no action requested now: the supervisor owns merging the independent reviews and choosing the later refactor's scope. This report neither implements nor approves delivery.

Verification limits: local committed baseline only; remote freshness was not checked. Installed applications, live account/job data and interactive Electron behaviour were not exercised. Source locations below refer to the frozen baseline; concurrent work may move their lines.

## Findings

The foundations are sound: presence, protocol and state remain free of I/O; Electron is confined to its three declared entry points; Accounts and Jobs separate tool access from sanitising pure models; Guilds separates catalogue, reading and presentation decisions. The boundary tests check that their checker can actually fail. The weak point is orchestration: independently sensible pieces meet in a few large, stateful owners whose ordering is less well tested than their individual rules.

**Must-fix — correctness and lifecycle defects to resolve before the next delivery.**

### STARTUP-GUARD - Initial sync can move a checkout held by a running agent

**Goal:** Check factoring and running-agent protection, requested by Kris on 6 November 2026.

**Scope:** [src/agora.ts:277](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:277), [src/review.ts:77](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/review.ts:77), [src/review.ts:97](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/review.ts:97), [src/agora.test.ts:364](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.test.ts:364).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

`start()` performs its first sync before `reviewNow()` reads agent ownership. `Review.runs` starts empty, and `sync()` interprets no matching run as permission to fast-forward. The probe records one merge and zero ownership reads; refreshing ownership first prevents the merge. Later syncs rely on ownership from the last review, normally five minutes old, and an initial failed read leaves the permissive empty list. The existing protection test explicitly reviews first, hiding the startup defect.

**Proposed refactor:** Put a successful, sufficiently current ownership reading inside sync's preconditions; unknown ownership must withhold fast-forwarding. Test startup, an agent starting between reviews, and failed ownership reads. **Size M; risk medium**, because Git scheduling changes must preserve fetch-only operation while movement is withheld.

Queries raised: none.

### OUTBOX-DURABILITY - Failed persistence still returns a successful broadcast result

**Goal:** Check reliable delivery and ownership of broadcast state.

**Scope:** [src/agora.ts:570](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:570), [src/agora.ts:772](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:772), [src/main.ts:293](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/main.ts:293).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

`saveOutbox()` changes memory before writing, catches a write failure and returns normally. `broadcast()` then returns a sent record and the Portal reports delivery or queuing. With a deliberately unwritable state location, the probe returns a peer marked queued while logging that the outbox could not be written. Restarting loses that queued delivery: the outbox is the retry record for an absent peer.

**Proposed refactor:** Give an outbox owner an explicit persistence result. Persist pending delivery before claiming durable queuing, retain idempotent delivery, and surface failed saves instead of success notifications. Test both initial enqueue and delivery-state persistence failures. **Size M; risk medium**, especially around restart and retry behaviour.

Queries raised: none.

### TAB-RACE - An abandoned Observatory load can cover the newly selected page

**Goal:** Check Agora's separation from embedded Observatory pages.

**Scope:** [src/app/main.ts:412](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/main.ts:412), [src/app/renderer/index.ts:1911](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/renderer/index.ts:1911).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

`showTab()` hides existing pages, awaits reachability, then creates and shows a native view without rechecking which tab is wanted. Selecting Repositories, switching Home while that check waits, then completing it shows Repositories over Home. A stubbed execution of the actual function confirms this. Repeated bounds requests while the first check waits can also create competing views for the same tab.

**Proposed refactor:** Extract a tab owner with the current requested tab, one pending creation per tab, and a generation check after each await. Release failed or superseded views explicitly. Test leaving during load, rapid switching and repeated resize requests. **Size M; risk medium**, confined to embedded-page lifecycle.

Queries raised: none.

### JOBS-TRUTH - Schedule and outcome summaries overstate the readings

**Goal:** Check the Scheduled jobs view's fidelity to Rig and recorded runs.

**Scope:** [src/app/jobs.ts:65](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/jobs.ts:65), [src/app/jobs.ts:102](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/jobs.ts:102), [src/app/jobs.ts:205](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/jobs.ts:205).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

`scheduleWords()` keeps weekday, hour and minute, silently dropping other calendar constraints and replacing absent time fields with zero. The probe turns `day=1,hour=8,minute=0` into a daily schedule and `minute=30` into a fixed midnight time. A separate probe with one job and no recorded run produces a headline claiming every last run ended well. These are misleading operational statements.

**Proposed refactor:** Use a typed schedule representation preserving declared constraints; show the original schedule when translation is unsupported. Treat no recorded run and unknown selection as explicit states in the headline. Cover unsupported constraints, omitted fields, short intervals, no runs and empty readings. **Size M; risk low to medium**, within pure presentation rules.

Queries raised: none.

### ROADMAP-READING - Valid records disappear and the two readers disagree

**Goal:** Check Roadmap completeness, duplication and metadata parsing.

**Scope:** [src/app/roadmap.ts:76](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/roadmap.ts:76), [src/app/roadmap.ts:130](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/roadmap.ts:130), [src/app/islands.ts:179](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/islands.ts:179), [src/app/islands.ts:225](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/islands.ts:225).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The handwritten parser skips folded scalar markers; a valid record with a folded `title` returns null and silently vanishes in the probe. `roadmapCounts()` separately reads front matter and counts Markdown notes lacking a record id/title, so map counts need not match the table. `readRecords()` stops after any Markdown filename in the first folder, even if none parsed as a record, contradicting its stated first-folder-with-records rule.

**Proposed refactor:** Use one bounded front-matter reader with typed adapters and explicit parse notices. Derive table rows and map counts from the same parsed records, and base folder precedence on valid records. Share parsing primitives with [src/app/guilds.ts:85](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/guilds.ts:85) and [src/roster.ts:159](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/roster.ts:159), whose quoting and block support differ. Test folded titles, escaped quotes and a notes-only first folder. **Size M; risk medium**, because existing metadata interpretations must be preserved deliberately.

Queries raised: none.

### INSTALL-GATE - Installation continues even when the viewer has not stopped

**Goal:** Check tooling orchestration without executing an installation.

**Scope:** [tooling/install/install.ts:122](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/tooling/install/install.ts:122), [tooling/install/install.ts:129](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/tooling/install/install.ts:129), [tooling/install/install.ts:135](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/tooling/install/install.ts:135).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The Portal shutdown wait is checked and aborts on timeout; the viewer's equivalent wait is ignored. Installation can therefore remove the viewer bundle while its process still runs. Both live bundles are also removed before replacement copies have succeeded, so a failed copy leaves the previous app gone. Pure installer decision tests do not exercise this command ordering.

**Proposed refactor:** Check both shutdown gates. Prepare and verify replacement copies before removing live paths, and extract the executing sequence behind a runner so timeout and copy failures can be tested without touching applications. **Size M; risk medium to high** for implementation, which needs a separately authorised Mac installation check. This review performed none.

Queries raised: none.

**Nice-to-have — structural improvements after correctness fixes, in priority order.**

### AGORA-COHESION - Independent workflows share too much central mutable state

**Goal:** Assess module cohesion and tangled orchestration.

**Scope:** [src/agora.ts:172](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:172), [src/agora.ts:816](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:816), [src/agora.ts:855](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:855), [src/review.ts:35](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/review.ts:35).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The 1,252-line Agora object owns presence, transport, discovery, sync, watch history, push attribution, settle timers, calls, roster, local serving, accounts/jobs sampling, broadcasts, acknowledgements and wakes. Its sync/watch/event locks do not form one repository lock: peer rings, pushed signals and settle timers call `fetchAndCheck()` directly, while event rounds use another path. The fetching counter suppresses some watch reactions; it does not serialize Git operations or message-history updates.

**Proposed refactor:** Extract a repository coordinator with one queue per checkout, then a broadcast/outbox owner and a read-model sampler. Leave Agora as composition and lifecycle owner; keep the small pure modules. Test overlapping event, fallback and peer rounds plus shutdown with work pending. **Size L; risk medium to high**: extract one workflow per reviewed change, rather than replacing this with another universal manager.

Queries raised: none.

### WINDOW-COHESION - Every page shares one large renderer state space

**Goal:** Assess cohesion of the new views and maintainability.

**Scope:** [src/app/renderer/index.ts:84](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/renderer/index.ts:84), [src/app/renderer/index.ts:1019](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/renderer/index.ts:1019), [src/app/renderer/index.ts:1426](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/renderer/index.ts:1426), [src/app/renderer/index.ts:2327](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/renderer/index.ts:2327).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The 2,380-line renderer combines SVG drawing, gestures, animation, search, navigation, information pages, settings/updates and detail panes. Each feature adds globals and cases to common navigation/feed callbacks. Pure page models already exist, but rendering ownership has not followed that split. The 1,953-line stylesheet has accumulated similarly.

**Proposed refactor:** Give Home/map and each information page their own renderer module and state, with small mount/update/dispose contracts and the typed bridge passed in. Keep shell/navigation and shared DOM/detail helpers small; split CSS along page ownership. No framework migration is needed. **Size L; risk medium**; establish checks for selection, filtering, scroll/focus and stale async results before moving code.

Queries raised: none.

### APP-COMPOSITION - The Electron edge also coordinates data and rehearsal

**Goal:** Check the Portal/app split and thin-shell intent.

**Scope:** [src/app/main.ts:141](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/main.ts:141), [src/app/main.ts:311](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/main.ts:311), [src/app/main.ts:342](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/main.ts:342), [src/app/main.ts:467](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/main.ts:467), [src/app/renderer/index.ts:2356](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/renderer/index.ts:2356).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The two-app split is sensible and the Unix speaking door is narrow. App `main.ts`, however, owns feed merging, three refresh loops, feature caches, filesystem discovery, settings/update policy and about a hundred lines of screenshot rehearsal. A concrete ordering hazard is `jobPlaces()`: its Rig source depends on lands, but the renderer requests it only once; an early response fixes that fallback root at null even after lands arrive.

**Proposed refactor:** Move refresh, caching and message merging into a Node-testable app controller emitting coherent snapshots, including job placement metadata. Keep windows, IPC registration and native views at the Electron edge. Move rehearsal planning into development tooling with an injected window adapter. **Size M; risk medium**. Fix the one-shot placement dependency with the Jobs repair.

Queries raised: none.

### READ-BOUNDS - File limits apply after entire files have already been read

**Goal:** Check robustness and responsiveness of estate-wide reads.

**Scope:** [src/app/islands.ts:196](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/islands.ts:196), [src/app/islands.ts:237](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/islands.ts:237), [src/app/islands.ts:272](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/islands.ts:272), [src/app/skills.ts:126](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/skills.ts:126).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

Roadmap and message readers call synchronous `readFileSync()` before checking text length; roadmap counts have no size check. Large files still allocate and block the app main process. Counts and record lists also reread the same files through separate loops. The skill reader already offers a better local pattern: size check first, then a binary probe.

**Proposed refactor:** Reuse a bounded text-reading adapter enforcing byte limits before full allocation, and build one metadata snapshot per refresh. Use bounded asynchronous reads where estate size makes pauses material. Report skipped inputs explicitly. **Size M; risk low to medium**, mainly around filesystem races and consistent notices.

Queries raised: none.

### TEST-SEAMS - Strong rule tests leave async composition insufficiently covered

**Goal:** Assess test quality beyond the passing suite count.

**Scope:** [src/boundaries.test.ts:1](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/boundaries.test.ts:1), [src/agora.test.ts:364](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.test.ts:364), [src/app/jobs.test.ts:49](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/app/jobs.test.ts:49), [src/install.test.ts:1](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/install.test.ts:1).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

Temporary Git repositories, real loopback transport tests, privacy-field exclusion checks and deliberate boundary crossings are substantial strengths. But ownership tests arrange the safe order, schedule tests cover the supported subset, and installer tests cover decisions rather than execution. Native-tab ownership and renderer page lifecycle lack direct behavioural suites. Passing the individual rules cannot establish correct ordering in their shells.

**Proposed refactor:** Use extracted controller/runner seams for deferred-promise and failure-injection tests covering the defects above, including restart after failed writes. Add a small page/bridge smoke suite for selection and stale results. Assert observable outcomes rather than copied implementation details; keep Git fixtures temporary. **Size M; risk low**; installed apps are unnecessary for these checks.

Queries raised: none.

### LEGACY-SURFACE - Remove proved leftovers while retaining live compatibility

**Goal:** Distinguish dead code from required transition behaviour.

**Scope:** [src/broadcast.ts:363](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/broadcast.ts:363), [src/wording.ts:164](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/wording.ts:164), [src/agora.ts:606](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/agora.ts:606), [src/files.ts:44](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/files.ts:44), [src/menu.ts:40](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/menu.ts:40).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

Knip identifies unused `describeBroadcast` and `PRESENCE_WORD`, remnants of previous presentation. Standalone `Agora.ping()` is called only by tests; no current menu exposes Ping. Presence `pingAll()`, fallback sync and sync helpers remain production paths. The small current tray menu has already replaced the old detailed tree. The `call`/`doorbell` double write and `doorbellAt` alias are required compatibility during the documented transition; `door.ts` is the distinct app-to-Portal socket.

**Proposed refactor:** Delete the two proved unused exports; narrow test-only conveniences as their services emerge. Retain ping/ack protocol compatibility, live sync and the call transition. Give the first build after 20 November 2026 an explicit compatibility-removal follow-up and contract check. **Size S; risk low** for dead exports, medium if protocol/view compatibility is included.

Queries raised: none.

### BOUNDARY-COVERAGE - Purity protection depends on enumerated filenames

**Goal:** Check whether architecture guards protect future extractions.

**Scope:** [.dependency-cruiser.ts:19](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/.dependency-cruiser.ts:19), [.dependency-cruiser.ts:23](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/.dependency-cruiser.ts:23), [src/boundaries.test.ts:30](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/src/boundaries.test.ts:30).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The current graph is clean, but pure modules receive their extra protections only when their exact filename appears in a regular expression. A newly extracted domain module can import runtime facilities without being classified as core. A twenty-module graph floor also protects weakly against partial graph loss now that the tree is much larger, although explicit entry-point and deliberate-crossing checks help.

**Proposed refactor:** Make module classification exhaustive through owned directories or an asserted inventory, and compare graph source coverage with files it should read. Retain deliberate-crossing probes and the isolated TypeScript-compatible checker installation. **Size S/M; risk low**, with care for browser and Node type-only dependencies.

Queries raised: none.

### DOC-DRIFT - Current help points to removed tray features

**Goal:** Check documentation against the delivered Portal and app.

**Scope:** [docs/how-agora-works.md:22](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/how-agora-works.md:22), [docs/how-agora-works.md:26](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/how-agora-works.md:26), [docs/how-agora-works.md:28](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/how-agora-works.md:28), [docs/design/agora-app.md:28](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/design/agora-app.md:28), [docs/design/agora-app.md:95](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/design/agora-app.md:95).

**As of:** 20:40 GMT, 6 November 2026, baseline above.

The current two-minute guide says checkouts appear in the tray, broadcasts/pings are sent there, and the tray shows ping replies. That no longer describes the slim Portal. The app design lists Settings as still to come although implemented, and its door table omits the implemented away action. These are present-tense help errors, distinct from specifications explicitly describing future work.

**Proposed refactor:** Update current-behaviour help from the actual menu, sidebar and speaking-door contract; mark unavailable ping controls honestly. Keep one authoritative description of each interface and link to it from other documents and implementation comments. **Size S; risk low**.

Queries raised: none.

## Top five

1. **Own and guard repository sync**: fresh successful agent ownership before movement, one queue per checkout, then extract this workflow from Agora. Addresses STARTUP-GUARD and AGORA-COHESION. Size M followed by staged L; medium risk.

2. **Make broadcast queuing durably accountable**: an outbox service with explicit persistence failures and restart/retry tests. Addresses OUTBOX-DURABILITY. Size M; medium risk.

3. **Separate app coordination and page rendering from Electron setup**: fix native-tab ordering first, then extract the controller and page-owned renderer modules. Addresses TAB-RACE, APP-COMPOSITION and WINDOW-COHESION. Size M followed by staged L; medium risk.

4. **Build trustworthy feature metadata once per refresh**: unified roadmap parsing/counts, preserved schedule constraints, truthful no-run states, dynamic job placement and bounded reads. Addresses ROADMAP-READING, JOBS-TRUTH and READ-BOUNDS. Size M in separate feature changes; medium risk.

5. **Make installation a checked, testable sequence**: gate both shutdowns, verify replacement copies before live-path removal, and exercise timeout/copy failures through a runner. Addresses INSTALL-GATE. Size M; medium to high risk for the later authorised installation check.

## Queries

No outstanding queries for Kris. The baseline and verification limits are stated above; these findings inform the supervisor's later merged plan and request no authority to change the checkout.

🧵 ki.prj.agora
