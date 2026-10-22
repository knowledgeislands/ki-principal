# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev2-vis030-a

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 03:08 BST · last mark 02:12 BST**

---

## Done

VERDICT: REFUSE · confidence high · An unreadable first territory leaves the rendered chart with no keyboard tab stop, violating the narrowed acceptance criteria.

- **Acceptance blocker - initial keyboard focus.** In [the overlay fallback](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/known-lands.ts:303), initial focus falls back to `home(0)`; [home](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/known-lands.ts:192) returns no node when the first archipelago has no islands. An unreadable territory is deliberately retained as an empty archipelago, so later readable territories can render while every island remains `tabindex="-1"`. Keyboard users cannot enter the chart to select an island or use its arrow, Home and Page navigation. This contradicts the record’s [Boundary and completed interaction step](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md:31) and the [operator guide’s one-tab-stop promise](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/guides/operator/read-the-instruments.md:296).
- **Independent reproduction - FAIL.** Reordered the existing fixture so its unreadable territory comes first, rebuilt placements with the production `withChart`, validated the result with `parseKnownLandsReport`, and mounted the production instrument against the repository’s DOM fixture entirely in memory: four rendered islands, zero tab stops, one required. This is a valid backend-generated layout, not malformed input; the existing keyboard test starts with a readable territory and misses it.
- **Reviewed scope and commits.** Reviewed [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) at `8f090308`, its predecessor `67cebf93`, and the idea-home change `c88355d0` in ki-principal; all named commits are ancestors of their local HEADs, and both reviewed files match the specified revisions. No literal Done-when section exists at the immutable baseline or either named Observatory commit; the Goal, Boundary acceptance paragraph, six checked Steps, Verify and Review supply the operative completion criteria.
- **Repository checks - PASS.** The seven chart, contract, evidence, overlay, vendoring, layout and degraded-state test files pass 83 tests; token and glyph digest tests pass 19 more, for 102 passing tests across nine files. Direct local TypeScript no-emit checks pass all eight applicable root/workspace/source configurations. Passing tests do not cover the reproduced unreadable-first-territory failure.
- **Other narrowed behaviour - supported.** Shared backend placement/image geometry, declared Capitals, explicit unknown condition, Beacon severity marks and off-chart accounting, repository filtering without another observation, accessible island lists, mechanical vendoring and degraded reads have implementation and passing targeted evidence. The retained tabs and routes are not removed by the narrowed delivery.
- **Durable follow-ups - PASS.** [Observatory Project Notes](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md:59), committed in `c88355d0`, retain trade routes, the Activity split, stored positions and Kris’s attended visual check. They preserve the convergence and separate-approval gates, old-route redirects, every exchange/change/window/reader, the Workers shared-reader sequencing constraint, and backend-only XDG preference handling. The restructure and Workers records now point to that home rather than removed phases. No unhomed later-scope idea was found.
- **Durable knowledge - supported.** [The repository standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-repo/references/standards-repository.md:244) owns declared maturity and audit-derived decline; the [design-language decision](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-002-observatory-design-language.md:53) owns density, width and scrolling navigation; the [glyph decision](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-008-line-glyphs-beside-tabs-and-subjects.md) and pinned source/digests own vendoring; [the Ancient-set decision](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-038-ancient-is-the-isometric-set.md) preserves the separate tile-set choice. The shipped chart’s contracts and operating behaviour also live in the specification and operator guide.
- **Pruning readiness - not ready.** The record remains awaiting review, and the keyboard blocker prevents acceptance. Independently, deleting it unchanged would break 43 local Markdown-link occurrences in 20 files, plus literal-path references below. Before any later prune, repair references to the accepted record’s immutable Git revision, preserve line citations as anchors where appropriate, commit the accepted terminal record, and keep deletion in a subsequent prune-only commit. No trade-linked retention reference was found in the estate-wide scan.
- **Review boundary.** No repository files, services, schedules, credentials or remotes were changed. No network calls were made. Full build, browser smoke and the full hosted audit were not rerun because they can emit files or perform network/process work outside this read-only authority; the report distinguishes its direct targeted verification from the prior full-gate claims. Other reviewers’ conclusions were not consulted: report files were scanned mechanically for identifiers and link targets only, and only their locations appear below.

### References a later prune must repair

Local Markdown links, including report links inventoried without consulting their prose (43 occurrences):

- [apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md:54) - lines 54, 61, 69, 100; 4 link occurrences.
- [ki-principal/+/_WORK/ki.observatory/messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/messages.md:14) - lines 14; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md:120) - lines 120, 139; 2 link occurrences.
- [ki-principal/+/_WORK/ki.ways-of-working/sweep-queries.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/sweep-queries.report.md:132) - lines 132; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/sweep-review-2.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/sweep-review-2.report.md:99) - lines 99; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-apps-depcruise.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-apps-depcruise.report.md:11) - lines 11; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-burn-accept-apps.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-burn-accept-apps.report.md:10) - lines 10, 18, 36; 3 link occurrences.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-burn-plan.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-burn-plan.report.md:38) - lines 38; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-fix-vis030.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-fix-vis030.report.md:11) - lines 11; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-night-observatory-queue-b.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-night-observatory-queue-b.report.md:17) - lines 17, 53, 77; 3 link occurrences.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-night-observatory-queue.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-night-observatory-queue.report.md:43) - lines 43; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-night2-obs-vis-042-accept-g.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-night2-obs-vis-042-accept-g.report.md:35) - lines 35; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-night2-obs-vis-042-e.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-night2-obs-vis-042-e.report.md:43) - lines 43; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-night2-obs-vis-042-g.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-night2-obs-vis-042-g.report.md:47) - lines 47; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-overnight-sweep.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-overnight-sweep.report.md:41) - lines 41, 57, 149, 229; 4 link occurrences.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-a.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-a.report.md:17) - lines 17, 19, 25, 45; 5 link occurrences.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-b.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-b.report.md:9) - lines 9, 30, 31, 32, 36, 37; 8 link occurrences.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-c.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-c.report.md:9) - lines 9; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-roadmap-sweep.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-roadmap-sweep.report.md:271) - lines 271; 1 link occurrence.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-vis030-home.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-vis030-home.report.md:11) - lines 11, 39; 2 link occurrences.

Literal pathname references (7 lines in 6 files); briefs and historical reports can retain their wording while the source location is archived or annotated:

- [apps-observatory.local/-/design-handoff/REPORT-2026-10-19.md](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/-/design-handoff/REPORT-2026-10-19.md:16) - lines 16, 17.
- [ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev2-vis030-a.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev2-vis030-a.md:7) - lines 7.
- [ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev2-vis030-b.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev2-vis030-b.md:7) - lines 7.
- [ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev2-vis030-c.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/wow-rev2-vis030-c.md:7) - lines 7.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-c.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-rev-vis030-c.report.md:34) - lines 34.
- [ki-principal/+/_WORK/ki.ways-of-working/wow-roadmap-sweep.report.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/wow-roadmap-sweep.report.md:370) - lines 370.

Identifier-only references do not become dangling file links: the Observatory changelog, instrument metadata/comments, contract comments, vendoring provenance/script, both coordination decisions logs, and the historical burn-observatory report. The separate ki-design handoff’s similarly named file is its own existing design document, not an inbound link to the roadmap record. Generated caches, dependencies, build output and Git object storage are not live reference sources.

## In Progress

Nothing running.

**Outstanding - no action requested now:** The next authorised implementer owns the keyboard repair and regression test; the later closure worker owns the reference repairs and terminal-before-prune commit boundary. Kris’s visual follow-up and the three gated ideas remain with the Observatory Project and are not reopened as obligations of this narrowed record.

## Queries

### VIS030-KEYBOARD - Return [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) for its missing initial tab stop

**Context:** The delivered chart renders four usable islands but exposes none to Tab when an unreadable territory is first. The minimal chart’s agreed keyboard and degraded-state requirements still apply; narrowing later ideas does not waive them. Acceptance and pruning therefore cannot proceed on the reviewed revision.

**Query:** Should the delivery return for a bounded initial-focus repair and a regression test before another blind acceptance review?

**Options:**

a) (recommended, confidence high - reproduced with valid production layout and the actual instrument) Keep the record awaiting review, choose the first rendered island when the first archipelago has none, add an unreadable-first-territory keyboard regression, verify it, and rerun the blind acceptance review before any acceptance or prune.

b) Keep the record awaiting review and defer the repair; do not accept or prune this revision.

### 🤖 → 👤 Handoff to supervisor · since 03:08 BST

👤 1 with you · ⛔ 1 blocked

- [with you] VIS030-KEYBOARD · work/ki.ways-of-working · since 03:08 BST
- [blocked] chart acceptance and pruning · work/ki.ways-of-working · since 03:08 BST
