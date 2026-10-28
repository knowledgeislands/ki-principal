# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-shape-blind

**🤖 → 👤 Handoff to supervisor · Run report at 01:57 BST · last mark unavailable within permitted reads**

---

## Done

Completed both recommendations independently against the permitted work-package and coordination sections.

Blind-scope check: no package queries, decisions, reports or design files read; no repository writes, network calls or agents launched.

Report-link check: both local heading targets exist; heading labels and work id verified against the coordination standard.

Commits: none; this review is read-only.

Limitation: the supervisor's last-mark time and wider work state were not supplied and were not read; the banner covers these two review questions only.

## In Progress

Nothing running. Both recommendations await the supervisor's decision.

## Queries

### STEWARD-FIELD - Where the stewardship assignment belongs

**Context:** The assignment names the work responsible for looking after a Project package and changes through an acknowledged handover. The existing worker and supervisor fields describe holders, from which pick-up derives where the work currently lies. Combining stewardship with worker would make one field carry both responsibility and holder semantics.

**Query:** Should the committed stewardship assignment use a dedicated work-valued field or the existing worker field?

**Options:**

a) (recommended, confidence high - Persistent responsibility deserves a distinct meaning from the holder used to interpret current state.) Add a dedicated field accepting only work/<id> values, naming the responsible State of play while it stewards the Project; make its change or removal part of the acknowledged handover when the Project gains or loses its own coordination thread.

b) Reuse worker: work/<sop id> during State of play stewardship and agent while the Project has its own thread, defining that change as the committed handover.

### HOST-TARGET - What a host requirement restricts

**Context:** The coordination standard takes IMPORTANT lines first, preserves queue order and requires a receiver to do what its authority permits. It explicitly distinguishes receipt and disposition from completing the requested work. A machine requirement can therefore constrain execution without preventing responsible handling of the line.

**Query:** Should an optional host or category tag restrict only device-dependent execution or all handling by an ineligible coordinator?

**Options:**

a) (recommended, confidence high - Execution-only targeting preserves priority and accountable receipt while keeping machine-dependent actions on an eligible host.) Let any coordinator acknowledge, plan, raise a query or arrange an authorised dispatch in queue order; enforce the tag before device-dependent execution. Record the pending execution or handover durably, and never treat acknowledgement as completion or dispatch as new authority.

b) Let a thread act only on untagged lines or lines matching its own host or category, retaining all others in the queue and showing their count and age in its banner.

### 🤖 → 👤 Handoff to supervisor · since 01:57 BST

🤖 0 running · 👤 2 with you · ⛔ 0 blocked

- [with you] STEWARD-FIELD: dedicated stewardship field · supervisor · since 01:57 BST
- [with you] HOST-TARGET: restrict device-dependent execution · supervisor · since 01:57 BST

🧵 Coordination thread · Ways of working (ki.ways-of-working)
