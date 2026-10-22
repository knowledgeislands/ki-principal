# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev-vis030-b

**🤖 → 👤 Handoff to supervisor · Run report at 02:48 BST · last mark 02:12 BST**

---

## Done

Blind acceptance review of [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md), read only, nothing committed.

**Verdict: REFUSE.** Confidence high: the code is real and the gates pass, but the narrowing has left two surviving records pointing at phases VIS-030 no longer carries, and the ideas the record itself says must be homed before pruning have no home yet.

Checks:

- `bun run test --force`: pass, 8 of 8 tasks.
- `bun run self:typecheck`: pass.
- `bunx rumdl check docs/roadmap`: pass.
- `ki repo audit --repo .`: FAIL=0, WARN=8. None of the warnings are about VIS-030.
- Change Summary commits `21be3a6`, `6b2096c`, `3427c48`, `c3cfb36`, `7819e7b` and `74f155b`: all on `main`, and their subjects match the record.
- Delivered evidence is present for every claim I checked: `apps/site/src/known-lands-chart.ts` with its test, `packages/instruments/src/known-lands.ts` with its test, and the hexmap digest test. The tests cover marks, signal accounting, selecting an island without a fresh read (it reads only `/api/beacon` and `/api/known-lands`), keyboard movement and an unreadable Beacon. `degraded.test.ts` covers `known-lands`, and the contract spec, operator guide and CHANGELOG are updated.
- The Review packet has all six sections in the right order, immediately before Discussion.

Blockers:

1. **The narrowing is silent in the surviving records.** The two phases were moved out of VIS-030, but the records that rely on VIS-030 to hold them were not updated:
   - [KI-OBSERVA-APP-044:42](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) still says "Trade routes layer and Activity split in KI-OBSERVA-VIS-030" are carried by a record.
   - [KI-OBSERVA-VIS-045:62](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) still names "KI-OBSERVA-VIS-030's Activity phase".

   Pruning VIS-030 would leave both depending on a record that no longer exists. The ki-accept reference preflight requires these to be repaired before the prune.
2. **The ideas are not homed, though the record says they must be first.** [VIS-030:116](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) and [VIS-030:159](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) require the trade-routes and Activity ideas to go into `+/_WORK/ki.observatory/` before any prune. Neither appears as an `Idea:` line anywhere in that package; I searched `work.md`, `messages.md`, `state.md`, `decisions.md` and `queries.md` in ki-principal. Under ki-work-roadmap, ideas belong as `Idea:` bullets in the owning Project note or theme page; a record's Discussion is not a home that survives pruning.
3. **Stored positions would disappear when the record is pruned.** [VIS-030:164](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) and the removed open Step "Positions as a host preference under XDG state, behind the backend" carried Kris's DESIGN-POSITIONS a) decision, an approved planned step. The package line VIS-030-MINIMAL and the message OBS-LANDED-VIS030 both reserve positions for Kris. The narrowing keeps positions only in this record's Discussion and leaves them off the list of ideas to home.
4. **The narrowing's approval cannot be traced.** [VIS-030:29](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) and [VIS-030:99](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) cite "the approved 22 October narrowing". The 02:28 BST burn-down entry in the [ways-of-working decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) allows delivering, accepting, and closing superseded or done records. It names no narrowing of VIS-030, and no decision line in either package does. Narrowings of other records do have their own lines (GOV189-SCOPE a), for example). The record should quote its exact source.

Non-blocking:

- [VIS-030:110](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md): the Verification section is out of date. It says the audit failed DESIGN-2 and that "this packet remains uncommitted". Commit `5ef758e6` has since moved the root to `tooling/depcruise`, the packet is committed, and the audit now passes, so refresh this section at acceptance.
- [VIS-030:178](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) still says "the Positions as a host preference step stays open", but that step has been removed.
- Kris's visual check is open, and the record's own acceptance allows that. It should appear as a concern in the ACCEPT bundle.

## In Progress

Nothing.

## Queries

**Context:** The delivered chart and interaction are real and every gate passes. Blockers 1 to 4 are all bookkeeping, and none of them involves code.

**Query:** How should KI-OBSERVA-VIS-030 reach acceptance and pruning?

**Options:** a) (recommended, confidence high - each fix is small and local, and only then does the narrowing stop being silent) do it in order. First, the coordinator records the narrowing as its own decision line, or asks Kris for it, since positions were reserved for him. Next, homing all three ideas (trade-routes layer, Activity split and stored positions) as `Idea:` lines in the ki.observatory Project note or package. Then one apps-observatory run repoints KI-OBSERVA-APP-044:42 and KI-OBSERVA-VIS-045:62 to those homes and refreshes VIS-030's Verification and its line 178. Finally the record is re-reviewed and accepted, and the prune comes in its own later commit. b) Accept VIS-030 as done now and hold the prune until the ideas are homed and the references repaired; this leaves the authority gap in blocker 4 open. c) Return VIS-030 to in-progress and restore the positions Step.
