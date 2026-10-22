# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-rev2-vis030-b

**🤖 → 👤 Handoff to supervisor · Run report at 03:07 BST · last mark 03:04 BST**

---

## Done

VERDICT: REFUSE · confidence high · the delivered chart meets its narrowed Done-when, but pruning now would orphan the island-condition follow-up, which was routed to this record and has no other durable home.

Blind review of [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) at apps-observatory.local `8f090308`, with `67cebf93` and ki-principal `c88355d0`. Read-only: no commit and no edit outside this report and the status file.

1. **The delivery meets the narrowed record.** All six Steps are ticked. The baseline and the six delivery commits named in the Change Summary are ancestors of `HEAD`. `67cebf93` and `8f090308` touch only roadmap records. The Review packet has its six headings in order, ahead of Discussion. The narrowing decision (ki.ways-of-working 02:49 BST) is committed in ki-principal. The operator guide and `docs/specs/contracts.md` document the instrument and the additive `chart` field.
2. **Checks pass.** `bun run test`, `self:typecheck`, `build`, `knip` and `rumdl check .` all pass, though Turbo served the first three from cache. Forced focused runs pass: chart, digest, degraded and layout gave 61 passes; the instrument test gave 11. `ki repo audit --repo .` has FAIL=0 and 8 warnings, none on this record. I did not rerun the browser smoke.
3. **Refusal ground: an idea with no durable home.** The island-condition projection is not homed anywhere else. It means the chart drawing each island's declared maturity and its audit-health decline or ruin, in place of `unknown`. The ki.observatory [messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/messages.md) line ISLAND-CONDITION (2026-10-21) routes it here: "Settle the projection in the existing Known Lands work, then rerun only that mapping." The `c88355d0` follow-up section in the [Observatory Project Notes](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md#known-lands-follow-up-2026-10-22) homes trade routes, the Activity split, stored positions and the visual check, but not this. The Observatory side survives elsewhere only as a pointer line in the decisions log and a comment in `beacon.ts`. The upstream model itself is durable: the harness `ki-repo` Island maturity standard and tools-ki TERRITORY-008, which conforms.
4. **The record contradicts current evidence.** Its Goal, Boundary and Dependencies / blocks say maturity and decline evidence is "not yet supplied upstream". They also say the harness and tools-ki "must" deliver it first. Both have: harness MATURITY-1 is live, and tools-ki `5aebeb9d` (20 October) publishes `ki/territory/v1` with `maturity` and `health`. The narrowing should exclude the consumer mapping explicitly rather than rest on an absent dependency.
5. **Pruning would break these inbound links. Repair them in a commit before the prune.**
   - [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) is a live draft with four relative links to the record (lines 54, 61, 69 and 100). Line 69 still says the record "is in progress". Line 100 makes APP-044 wait on it as part of step 3, so that statement needs restating as shipped.
   - [ki.observatory messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/messages.md) has three entries that depend on the record. The VIS-SIZES line 14 links to it and is already met, since the record has `size: m`. ISLAND-CONDITION (line 13) and OBS-LANDED-VIS030 (line 2) both depend on it. These are peer edits in ki-principal.
   - About fifteen ki.ways-of-working run reports carry absolute local links to the record. These are historical and do not block.
   - Bare identifiers do not block either: `roadmap: 'KI-OBSERVA-VIS-030'` in `known-lands.ts`, code comments, the CHANGELOG and the 19 October design-handoff report. Other instruments already cite pruned records the same way.
6. **Other knowledge is homed.**
   - The CONDITION-TOML decision and the maturity scale are in the harness standard.
   - DESIGN-POSITIONS and the three ideas are in the Project Notes.
   - Instrument behaviour and keyboard model are in the operator guide.
   - Large screens and TAB-SCROLL are in PDR-KI-OBSERVA-002 and `layout.test.ts`.
   - One gap is minor: the overlay-versus-browser-renderer rationale and the "board and app differ" list live only in Discussion. They are design input for Kris's redesign. Homing them is optional but advisable, for example as a line in the Project Notes visual follow-up.

## In Progress

Nothing running.

## Queries

**ISLAND-CONDITION-HOME**

**Context:** The record's narrowing homed three ideas but not the island-condition projection, which the 21 October ISLAND-CONDITION message routed to "the existing Known Lands work". Its upstream contract, `ki/territory/v1`, now exists. Pruning would leave that message with no target and the idea with no durable home.

**Query:** Where should the island-condition projection live so that KI-OBSERVA-VIS-030 can be accepted and pruned?

**Options:** a) (recommended, confidence high - this matches the existing narrowing and creates no record) add a fourth idea, "island condition", to the Known Lands follow-up section of the Observatory Project Notes. It would read `ki/territory/v1` maturity and health, with the open projection question. Correct the record's stale "not yet supplied upstream" wording, repair the APP-044 and messages references in a commit before the prune, then run fresh reviews. b) Reopen KI-OBSERVA-VIS-030 to deliver the condition mapping before acceptance. c) Capture a separate triage record through `ki-next` and link it from APP-044 and the message.
