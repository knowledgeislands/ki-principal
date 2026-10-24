VERDICT: Q1 watcher-first medium · Q2 thread-line-last high

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-blind-coord-queries

**🤖 → 👤 Handoff to supervisor · Run report at 02:36 BST · last mark 02:10 BST**

---

## Done

- Completed the independent review of both method questions; recommendations and reasoning follow under Queries.
- Grounding check: reviewed the coordination standard, coordinator output style and background-run standard; verified the report's identity and mark from permitted metadata.
- Blindness check: did not open this work's queries, decisions, run reports or coordination-lessons design note.
- Scope check: no repository edits, commits, remote calls, scheduler changes or subagents; only the requested runtime report and status were written.

## In Progress

Nothing running.

**Outstanding - no action requested now:** None.

## Queries

### WAKE-SCOPE - watcher first, with an explicit limit

**Context:** The existing method provides a completion watcher within an owner-agreed autonomy window. It also acknowledges that queued messages do not create a wake when none is armed ([coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:191), [inbox check](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:772)). A watcher therefore improves completion pickup without providing idle-message or overnight guarantees. A durable service adds a separate operational commitment; the brief establishes the gap, but no required unattended response time.

**Query:** Should the next step remain the completion watcher, with session wakes labelled best effort and durable message pickup deferred?

**Options:**

a) (recommended, confidence medium - this advances the agreed direction with the least additional machinery; the need for an overnight guarantee remains an owner choice) Pursue the watcher first. State the best-effort limit plainly, including idle messages and overnight processing. Revisit durable pickup when the owner requires unattended service within a defined window; that requirement would justify the bounded tools-ki and Rig design before implementation.

b) Route the bounded tools-ki and Rig design now, agreeing pre-check, cancellation, authority and failure reporting before implementation. Choose this if unattended message and completion pickup is required now, accepting the service's operational obligations.

### DRAIN-RESULT - keep the thread line last

**Context:** The final DRAINED / NOT DRAINED prompt worked, so the result should remain unmistakable. That does not establish that its final position caused the success. The existing banner and hold-report rules consistently reserve the final line for work identity ([coordinator style](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md:79), [hold report](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:891)); Done already provides a clear place for the outcome.

**Query:** Should an explicit drain check keep the thread line last and put the drain result in Done?

**Options:**

a) (recommended, confidence high - the outcome can stay explicit within the existing report shape, avoiding a new exception) Keep the thread line last. Put DRAINED or NOT DRAINED prominently in Done, with any blocker beside it; preserve the appropriate work state and banner.

b) Allow a narrow exception only for an explicitly requested drain check, placing the result after the thread line and updating the method and generated surfaces consistently.

### 🤖 → 👤 Handoff to supervisor · since 02:36 BST

👤 2 with you

- [with you] WAKE-SCOPE recommendation · ways-of-working coordinator · since 02:36 BST
- [with you] DRAIN-RESULT recommendation · ways-of-working coordinator · since 02:36 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
