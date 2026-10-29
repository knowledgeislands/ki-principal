# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-sm-polish

**🤖 → 👤 Handoff to supervisor · Run report at 22:28 GMT · last mark 16:18 GMT**

---

## Done

- I redrew the [work state machine](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md) in Archify to the Mermaid sketch's shape. The four-state cycle is a square loop inside Working: With worker at top left, Handoff to supervisor at top right, With supervisor at bottom right and Handoff to worker at bottom left. Start (work) is on the left, and the new End (work) final state is on the right. `conclude` reaches End (work) from With worker (over the top of the loop) and from With supervisor. `stop · drain, portable` now leaves only from End (work) to At rest. No arcs cross and every arc has a label. Everything that was already there is kept.
- The two handoff states are muted grey and labelled "transitional"; the stable states are labelled "stable". The legend has a "Handoff: transitional" entry and a new "Stable and transitional" card. Archify's showcase gates all pass (validate, deliver, check and the browser check). I exported the SVG with the ki-diagrams exporter in its default dual form and checked a screenshot by eye.
- I updated the note's tables:
  - States has a new End (work) row, and each Meaning cell now says stable or transitional.
  - Transitions has a new `conclude` row with preconditions, work and postconditions. It takes Kris's stop words, so the supervisor concludes.
  - `stop` now runs from End (work), and the orchestrator does the drain.
  - Wording elsewhere follows (the Roles and Reading the machine text, the old-to-new map and the status line naming WORKING-EXIT).
- Committed as c304e203 (`docs(work): ki.prj.ways-of-working polish work state machine`), with the repository audit hook passing.

## In Progress

Nothing is running.

Outstanding - no action requested now: none. Archify cannot draw a node with a dashed border, so "lighter" is done with the muted grey type. Finished took the orange type that the handoffs used before.

## Queries

### END-RECORD - What `state.md` records while the work is at End (work)

**Context:** End (work) now sits between `conclude` and `stop`. I wrote it as transient, like Bootstrap: it has no `state` value of its own, `state.md` keeps the inner state the work concluded from until `stop` completes, and a failed `stop` leaves the work at End (work) marked blocked, `NOT DRAINED`, with `blocking` set. That fills in a detail WORKING-EXIT did not state.

**Query:** Should End (work) stay transient with no `state` value, or get its own value, such as `concluded`?

**Options:**

a) (recommended, confidence medium - matches how Bootstrap is treated, and `conclude` and `stop` usually run in one turn) Keep it transient: no value of its own, and the concluded-from state is kept with `blocking` while a drain fails.

b) Give it its own `state` value, such as `concluded`, so that a blocked drain shows as End (work) in `state.md` and in the banner.

### 🤖 → 👤 Handoff to supervisor · since 22:28 GMT

👤 1 with you

- [with you] END-RECORD · owner · since 22:28
- [committed] work state machine polish

🧵 ki.prj.ways-of-working
