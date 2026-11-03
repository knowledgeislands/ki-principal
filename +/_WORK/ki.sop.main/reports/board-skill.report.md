# [Knowledge Islands](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › State of play › board-skill

**🤖 → 👤 Handoff to supervisor · Run report at 03:34 GMT · last mark 16:17 GMT**

---

## Done

- ANNOTATED-BOARD-SKILL and its addendum landed in ki-agentic-harness `main` at `4721d886`, `feat(ki-design-system): annotated board as a standing projection`, published.
- What it adds to the [ki-design-system skill](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/design/ki-design-system/SKILL.md):
  - **Review stage.** Review is now stage 0 of design work: the owner quotes region codes on the board, and those findings become the brief. Options go on the board beside the screenshot they answer.
  - **Projections.** The [standard](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/design/ki-design-system/references/standards-design-system.md) now has two kinds of projection. The board is the second kind: it is refreshed from the running interface and is kept after design work is retired.
  - **New reference.** [standards-annotated-board.md](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/design/ki-design-system/references/standards-annotated-board.md) covers numbered pages, shells with `N0`/`T0`, `0.x.y` component artboards in every state, region codes, measuring, refresh and feedback. It is named to fit the house filename rule, not `annotated-board.md` as proposed.
  - **Rubric.** DSYS-8 now asks whether the board is current, and the rubric was regenerated.
  - **Provenance.** Provenance is recorded without naming any other territory.
- **Board tooling.** [`scripts/annotate-board.ts`](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/design/ki-design-system/scripts/annotate-board.ts) carries the parts of the board scripts that work for any site, rewritten as TypeScript with 12 new tests:
  - a plan-driven in-page region collector;
  - region coding;
  - overlays;
  - a `board.json` with each artboard's legend;
  - local previews.
- **Left with each site.** These parts stay with the site: browser capture, switching components between states, and writing the Claude Design canvas files.
- **Generated surfaces.** The design skill-area diagram was regenerated because its file count changed.
- **Checks:**
  - `bun run test`: passed, 1541 tests.
  - `bunx tsc --noEmit`: passed.
  - Focused `ki repo audit` for ki-skills, ki-repo-harness, ki-diagrams, ki-authoring and ki-git, in an isolated home: all passed. The warnings are elsewhere in the harness and not from this change: stale review dates on other skills, and diagram freshness warnings.
  - The pre-commit hook: passed.
- **Housekeeping.** The worktree and its branch were removed after the fast-forward.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The reply line to personal.reg.assistant-terra was appended to its `messages.md` in the assistant repository and left uncommitted. The file had no uncommitted change before, and this brief authorised only the append. The keyholder of that package commits it.
- `ki repo audit --skill ki-design-system` cannot run in the harness itself, because the harness does not declare the skill. Its rubric publication was checked through the ki-skills audit instead.

## Queries

### BOARD-CAPTURE - whether the harness should also drive the browser for boards

**Context:** The harness now gives any site the collector, the region codes and the overlays. Each site still writes its own browser steps: taking screenshots, switching components between states, and publishing to its canvas. The harness already drives a system Chrome without Playwright for `ki-diagrams`, but that code is private to that skill. Sharing it would mean publishing it as a shared module, which touches a second skill. Only one site, the KIV, has a board so far.

**Query:** Should `ki-design-system` get its own capture step, which takes screenshots of each page and component state from a plan, now or only once a second site adopts the board?

**Options:**

a) (recommended, confidence medium - one site's needs may not generalise; a second board would show which capture steps are common) Wait for a second site, then add capture by sharing `ki-diagrams`' Chrome driver.

b) Add a capture step now, driven by the board plan, sharing the Chrome driver from `ki-diagrams`.

### 🤖 → 👤 Handoff to supervisor · since 03:34 GMT

👤 1 with you

- [with you] BOARD-CAPTURE · owner · since 03:34

🧵 ki.sop.main
