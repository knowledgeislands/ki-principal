# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › ideas-board

**🤖 → 👤 Handoff to supervisor · Run report at 02:02 GMT · last mark 01:31 GMT**

---

## Done

- Drafted the empty-board design note, [design](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/design.md), for your morning review. It covers where work and ideas live today, with counts; gates and work-in-progress limits; what does not fit today; and twelve places where the structure contradicts itself. It ends with nine queries.
- Wrote the consolidated ideas list, [ideas](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/ideas.md): 244 entries, each linked to its source. Nothing was changed or deleted at any source.
- Committed both files as `0526cffd` and pushed. The scoped repository audit passed for both paths, and all 198 links resolve.

In short, the board is far from empty:

- 16 work packages: 1 active, 5 waiting on you, 9 on hold and 1 finished but never removed.
- 45 open queries, 120 parked queries and about 140 queued messages.
- Only 3 of 22 roadmap records are genuinely next in line or in review.
- The sharpest contradiction: the standards' "keep about three agents running" and "three or four" active-package cap are looser than your WIP-LIMIT answer.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- None of the queries has had a blind review. The design note says so, and each one should go through the masked review before it is taken.

## Queries

### IDEAS-HOME - Where should ideas live?

**Context:** Ideas live today in four sanctioned places (Project pages, theme pages, idea-stage Projects and repository `_IDEAS.md` ledgers) plus Emerging Concepts, parked queries and held packages. You asked for them to be consolidated in a single place. One territory list is easiest to review and to keep empty, but it moves ideas away from the Project pages that give them context, and it needs the roadmap standard changing.

**Query:** Where should every idea in the Knowledge Islands territory live?

**Options:**

a) (recommended, confidence medium - it gives you one place to review and age ideas, but it reverses the 17 October rule that ideas start on their Project page) One territory ideas list in Knowledge Islands Principal, each idea one line naming its Project or theme and linking to fuller text where it exists; Project and theme pages keep their context but no longer hold ideas.

b) Leave ideas where they are and generate the consolidated list from them on demand, like [ideas](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/empty-board/ideas.md), so there is one place to look but several places to write.

c) One ideas list per repository, with Project pages pointing to them.

### WIP-PACKAGE - How many units may a package have in flight?

**Context:** Overnight this package ran up to three units at once, as the current "keep about three agents running" rule allows. You asked for one at a time where possible, finished quickly. A unit's independent review is a separate run, but it works on the same change.

**Query:** How many units may one work package have in flight at a time?

**Options:**

a) (recommended, confidence high - it is your WIP-LIMIT answer written down, and allowing the review keeps reviews independent without a second piece of work) One unit at a time, plus at most one independent review of that same unit.

b) One unit at a time with nothing alongside it, reviews included.

c) Up to two units at a time where they touch different repositories.

### WIP-TERRITORY - How many packages may be active across the territory?

**Context:** The current cap is "three or four" Project packages, not counting State of play; today five packages are neither on hold nor finished, one being worked and four waiting on you. A package waiting on you would count as active under this proposal, so that answering frees a slot.

**Query:** How many work packages may be active at once across the Knowledge Islands territory?

**Options:**

a) (recommended, confidence medium - it tightens the existing cap to its lower bound without stopping you working on more than one thing a day, though "minimal parallelisation" could mean one) At most three Project or regular packages, plus State of play, with packages waiting on you counting as active.

b) One package at a time, plus State of play: strictly serial.

c) Keep "three or four", with packages waiting on you not counted.

### ROADMAP-UPCOMING - Should the roadmap hold only upcoming work?

**Context:** Records can sit on the roadmap with horizon `soon`, `future` or `hold`, and done records stay until pruned. Today 19 of 22 records are finished, held, in triage or tied to work that is not moving. Making the roadmap hold only `now` and `next` would turn the other horizons into ideas, which needs the roadmap standard and its checker changing in the harness and tools-ki.

**Query:** Should a roadmap hold only records that are coming up next, with everything else moved back to ideas?

**Options:**

a) (recommended, confidence medium - it is what EMPTY-BOARD asks for, but it changes a standard and a checker that other territories also use) Yes: only `now` and `next` stay, capped at three per repository and ten across the territory; `soon` and `future` records go back to ideas, and held records go back to ideas unless their release is in sight within a fortnight.

b) Keep the horizons as they are, but count only `now` and `next` as upcoming, and cap those.

### GATES - Are the two gates right?

**Context:** Section 3 proposes Gate 1 (idea to upcoming: you say yes, it has a home, the next step is known, it is small, and there is room) and Gate 2 (upcoming to active: it is Ready, nothing it needs is missing, and the package and the territory have a free slot). Most of these already exist in `ki-next` and `ki-plan`; the new parts are the size rule and the room checks.

**Query:** Should the two gates in section 3 be adopted as written?

**Options:**

a) (recommended, confidence medium - most of each gate restates existing rules, and the new size and room checks are easily relaxed later) Adopt both gates as written.

b) Adopt them without the size rule, so larger work can be adopted and split later.

### PARKED-TO-IDEAS - What happens to parked queries?

**Context:** 120 parked queries sit in nine packages with no age limit; several point at records that no longer exist, and eight here are duplicated. A parked query is a decision nobody is currently making, which is what an idea is. Moving one keeps its recommendation, so nothing is lost.

**Query:** Should parked queries move to the ideas list?

**Options:**

a) (recommended, confidence medium - it empties the Parked sections and stops stale decisions piling up, but some parked queries are close to answerable and might be better brought back) Yes: at each package's next mark, each parked query moves to the ideas list with its recommendation, and the Parked section goes.

b) Keep Parked sections, but offer any parked query older than 30 days for dropping at your next review.

### HOLD-CLOSE - What happens to packages on hold?

**Context:** Nine packages are on hold, six of them since 18 to 20 October. While held they still receive messages they cannot act on, such as the ORCA-ENV-LEAK security fix waiting in tools-burndown. Closing a held package would home its decisions, move its messages and parked queries to the ideas list and remove its folder, leaving the Project `paused`; reopening means creating a fresh package.

**Query:** Should a package on hold for more than 14 days be closed out?

**Options:**

a) (recommended, confidence low - it clears the board fastest, but closing a package is hard to undo cleanly and several held packages, such as tools-burndown, hold live handoffs) Yes, after you have seen what each would close, one package at a time.

b) No: keep held packages, but route new messages for a held package to State of play instead, so nothing waits behind a hold.

c) Keep held packages as they are.

### QUICK-FIXES - Fix the easily undone contradictions now?

**Context:** Three contradictions can be fixed in Knowledge Islands Principal alone, each easily undone: nine Project pages whose `lifecycle` disagrees with their package (seven `active` but on hold, two `active` with no package); the finished Knowledge acquisition folder, which the standard says should already be gone and whose history Git keeps; and the eight duplicated parked entries in this package.

**Query:** Should one small run make these three fixes now, as a bounded change you approve?

**Options:**

a) (recommended, confidence medium - each fix is small, within this island and recoverable from Git, though the lifecycle wording for held Projects needs a choice between `paused` and keeping `active`) Yes: set the seven held Projects to `paused` and the two packageless ones to `planned`, remove the Knowledge acquisition folder, and remove the duplicate entries.

b) Fold them into the wider rollout instead, after the standards change.

### DONE-PRUNE - Prune the seven finished records?

**Context:** Seven records are done and accepted but still on their roadmaps: [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md), [KI-HARNESS-GOV-232](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-232-any-package-coordination.md), [KI-HARNESS-GOV-233](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-233-typed-work-naming-readers.md), [KI-HARNESS-GOV-234](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-234-footer-markdown-writers.md), [KI-TOOL-KI-CLI-173](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-173-regular-coordination-readers.md), [KI-TOOL-KI-CLI-174](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-174-typed-work-naming-readers.md) and [KI-TOOL-KI-CLI-175](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-175-footer-markdown-writers.md). Pruning is yours to approve; it removes the file from the roadmap and Git keeps it.

**Query:** Should the seven done records be pruned now?

**Options:**

a) (recommended, confidence medium - they are closed and pruning is recoverable from Git, but this run has not rechecked each one's closure evidence) Yes, through `ki-accept`'s prune, each repository in turn, after a check that each closure is complete.

b) Leave them until each owning work's next mark.

### 🤖 → 👤 Handoff to supervisor · since 02:02 GMT

👤 9 with you

- [with you] empty-board draft and its nine queries · owner · since 02:02 GMT
- [committed] design/empty-board

🧵 ki.prj.ways-of-working
