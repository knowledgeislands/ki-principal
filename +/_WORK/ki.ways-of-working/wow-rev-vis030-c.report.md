# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-vis030-c

**🤖 → 👤 Handoff to supervisor · Run report at 02:49 BST · last mark 02:45 BST**

---

## Done

- Blind acceptance review of [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) at `67cebf93` on `main`, read only; no commit, no file changed, no remote call.
- Checks run on the primary checkout at `67cebf93`: `bun run test --force` pass; `bun run self:typecheck --force` pass; `ki repo audit --repo .` FAIL=0 with 8 warnings, none on this record; `rumdl check` on the record pass.

### Verdict

**ACCEPT**, confidence **high**: the narrowed scope is authorised and transparent, every claimed commit and test exists on `main`, and the governing audits pass; the three conditions below bind the prune, not the acceptance.

### Scope legitimacy

- The narrowing was ordered by the coordinator's brief to `wow-burn-accept-apps` ("narrow it to the delivered stage, homing the two later phases as ideas in the observatory package (no new record), and take it to awaiting-review") under OVERNIGHT-BURNDOWN ("Follow-ups go as `messages.md` lines or Idea lines, never new records") and the 02:28 BST burn-down grant in the ki.ways-of-working decisions log. It is not a silent drop: Context names the instruction, Boundary moves the two phases to Out of scope, and Discussion, "Later ideas retained for the observatory package", keeps both ideas with their gates (KI-OBSERVA-APP-044 convergence, Kris's separate approval, the `?view=` redirects, the preserved readers and the shared Activity reader).
- The former merged records VIS-035 and VIS-036 (merged into this record on 19 October, `f0251b6`, pruned in `4da194b`) therefore survive as ideas, which matches the roadmap standard's ideas rule: an idea has no identifier and waits on the Project note or theme page.
- The unchecked step "Positions as a host preference" was removed rather than kept, which the format standard permits only for completed steps by implication; the narrowing covers it, and the decision survives as DESIGN-POSITIONS a) in the ki.observatory decisions log and in the record's Discussion. See condition 2.

### Delivered work is real

- The six delivery commits named in Change Summary (`21be3a6`, `6b2096c`, `3427c48`, `c3cfb36`, `7819e7b`, `74f155b`) and baseline `9f56976c` are all ancestors of `main`.
- Code exists where the record says: `packages/evidence/src/known-lands.ts`, `packages/contracts/src/known-lands.ts`, `packages/instruments/src/known-lands.ts`, `apps/site/src/known-lands-chart.ts`, `apps/site/src/hexmap-upstream.ts`, `scripts/design/vendor-ki-design.ts`, with the vendored tree under `apps/site/src/vendor/ki-design/`.
- Tests cover each acceptance criterion: same backend layout for image and overlay (`apps/site/src/known-lands-chart.test.ts:39-92`); every drawn signal lands on a rendered island, selection without re-observation, keyboard movement, unavailable Beacon and read-only behaviour (`packages/instruments/src/known-lands.test.ts:123-241`); degraded states (`apps/site/src/degraded.test.ts:459-470` and the selectable-chart case near line 822); vendoring digests (`apps/site/src/hexmap-upstream.test.ts`); contract shapes (`packages/contracts/src/contract-shapes.test.ts`).
- Documentation impact is met: `docs/specs/contracts.md:34` names `observatory/known-lands/v1` with `chart` and the SVG route; `docs/guides/operator/read-the-instruments.md:290` has the Known Lands section; `CHANGELOG.md:13-16` carries the three entries.
- Frontmatter is valid for acceptance: `size: m`, `kind: deliver`, `horizon: now`, `status: awaiting-review`, every Step `- [x]`, the six Review headings in order and immediately before Discussion.

### Findings

None blocks acceptance. Each is a condition on the later prune or a repair for the acceptance commit.

1. **Ideas not yet homed (prune condition).** The two ideas and the stored-positions note exist only in the record's Discussion. Nothing in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/` (work.md, messages.md, decisions.md, state.md) or `Streams/` yet carries "trade-routes layer" or "Activity split". The standard says anything held only in a record being pruned is held nowhere, and the record itself (`docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md:120`, Outstanding concerns) names this as a precondition. Home them as `Idea:` bullets on the owning Project note's `## Notes` (the ideas rule names the Project note or theme page, not the work package folder) before the prune commit.
2. **Stored positions missing from the homing list.** The "Later ideas retained" section (`...VIS-030-known-lands-chart.md:159-164`) lists two ideas; stored positions appear only as a closing paragraph. The `wow-burn-accept-apps` query recommended homing "the stored-position note" too. Include it with the two ideas.
3. **Verification text is stale (repair in the acceptance commit).** `...VIS-030-known-lands-chart.md:110` records `ki repo audit` failing DESIGN-2 and "this packet remains uncommitted", but `5ef758e6` migrated `tooling/boundaries` to `tooling/depcruise` and the packet was committed in `67cebf93`. On the committed tree the audit now passes (FAIL=0). The acceptor should record that outcome in Verification when recording the review outcome, so the retained record does not carry a failing gate as its last word.
4. **Kris's visual check must survive the prune.** Outstanding concerns (`...VIS-030-known-lands-chart.md:120`) names Kris's visual check of marks, rings, detail placement and Page Up / Page Down. Under the 20 October approval the look is provisional until his designs, so it is not an acceptance gate for the delivered stage, but it is an attended item for the morning list; carry it as a `messages.md` line in ki.observatory before the prune, or it is lost.
5. **Inbound links to repair before the prune.** `docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md:59` and `:98`, and `docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md:62`, link the record by relative path; ki-principal's `+/_WORK/ki.observatory/messages.md:14` (VIS-SIZES) and `decisions.md` link it by absolute path. Repair to commit-pinned links in a separate commit ahead of the prune, per the cross-repository reference preflight; the ki-principal links are outside this repository's authority and need the coordinator.
6. **Minor packet shape.** Change Summary names commits rather than files (Files touched covers them), and Mini recap proposes no learning routes. Neither affects the acceptance decision.

### Repository audit warnings seen

Eight warnings, none on VIS-030: HOLD-1 on the trades hold past its 2026-10-21 review date, ITEM-2 size missing on KI-OBSERVA-VIS-028, and six others unrelated to this record.

## In Progress

None.

## Queries

None. The verdict is ACCEPT; pruning waits on findings 1, 2, 4 and 5.
