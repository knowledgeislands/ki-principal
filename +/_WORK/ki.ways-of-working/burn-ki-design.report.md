# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › burn-ki-design

**🤖 → 👤 Handoff to supervisor · Run report at 07:31 BST**

---

## Done

- Inventoried the [ki-design roadmap](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/). Five records are open before the run and five after. None was Ready, and none could be planned and delivered without Kris, another repository, a network install or an attended check, so nothing was delivered. There are no commits and nothing was pushed. No worktree was needed, and the tree is untouched.
- Read-only `ki repo audit --skill ki-work-roadmap`: FAIL=0, WARN=10. Each of the five records gets two migration-window warnings: no `size:`, and project `ki-design` missing from the project registry.

| Record | Before | After | Why skipped | Commits | Pushed |
| --- | --- | --- | --- | --- | --- |
| [KI-DESIGN-ICO-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md) Icon seed set | awaiting-review, now | unchanged | Kris needs to look at the drawings on the contact sheet | none | no |
| [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md) Art licensing | draft, now | unchanged | Kris has to decide ownership, and the generator terms have to be read, which is a network call | none | no |
| [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) Lit SSR spike | draft, now | unchanged | The spike runs in the site repository (`apps-knowledgeislands.info`), needs `@lit-labs/ssr` installed from the network, and hydration has to be checked in a browser | none | no |
| [KI-DESIGN-MAP-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-MAP-002-isometric-renderer.md) Isometric renderer | draft, next | unchanged | Design calls are open (see Queries), and the 60 fps check needs a laptop browser | none | no |
| [KI-DESIGN-TIL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-TIL-002-ancient-tile-set.md) Ancient tile set | draft, next | unchanged | Blocked by ART-002, and batch 1b needs the image generator and Kris's judgement | none | no |

- Stale records, with a recommended disposition for each. Nothing was cancelled or edited.
  - KI-DESIGN-MAP-002 is stale against [GDR-KI-DESIGN-038](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-038-ancient-is-the-isometric-set.md). Its Verify still says "Arcadia renders from the Modern set", but Modern is now a frozen fixture and the isometric view is Ancient only. It also predates the open hex-terrain composition question in [OPEN.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/OPEN.md), which recommends keeping the renderer unchanged until Pilot 0 passes. Recommended: put it on hold behind that pilot, then replan it with Modern as the test fixture and Ancient as the target.
  - KI-DESIGN-TIL-002 still names KI-DESIGN-ART-001 as a blocker in its Boundary and Dependencies, but ART-001 was closed in `be8b802`. Its frontmatter `blocked_by: []` also leaves out ART-002. Recommended: replan the record so that only ART-002 remains, in `blocked_by`, and move it to on hold until that lands.
  - There are no duplicates and nothing has been superseded.

## In Progress

- Nothing. Local `main` is six commits ahead of `origin/main`, all made before this run: `9bc7dbd`, `e1d20b6` and `bbf4eb2` (the 05:24 to 05:28 accept and prune), and `ba2991c`, `e7b4c9a` and `6c6926f` (GPT-6, 06:12 to 06:18). They are not mine, so under PUSH-NOT-WITH-YOU they stay unpushed. Pending handoff: ki-design, this Mac, `main`, six unpushed commits.

## Queries

**Context:** KI-DESIGN-MAP-002 asks for a Canvas 2D renderer drawing "from a tile set's atlas". No atlas format exists: the sets are loose SVGs plus `render-iso.ts`. The open hex-terrain composition question may replace the fixed-plinth model that the renderer would be built on.
**Query:** Should MAP-002 wait for composition Pilot 0, or be built now on the current plinth model?
**Options:** a) (recommended, confidence medium - building now would probably be rebuilt after the pilot) Put MAP-002 on hold behind Pilot 0, then replan it with an atlas format, Modern as the fixture and Ancient as the target. b) Plan it now on the plinth model, with a recording-context test and no frame-rate claim. c) Cancel it until the Ancient set exists.

**Context:** The five ITEM-2 warnings are for a missing `size:` on each record.
**Query:** May a later run add sizes as a tidy: ART-002 s, ELE-001 m, ICO-001 s, MAP-002 l, TIL-002 xl?
**Options:** a) (recommended, confidence high - estimates only, and it clears five warnings) Yes, as one `docs(roadmap)` commit, leaving the awaiting-review ICO-001 alone until it is accepted. b) Leave sizing to whoever next plans each record.
