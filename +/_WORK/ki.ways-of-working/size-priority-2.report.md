# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › size-priority-2

**🤖 → 👤 Handoff to supervisor · Run report at 08:46 BST · last mark 08:07 BST**

---

## Done

- **ki-agentic-harness, `d9cd8718` and `7b8c4fb1`, pushed fast-forward with only my commits on top.** I took over the stopped run's 5-line edit and finished it.
  - Priority and size: the [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md#priority-and-size) gains a Priority and size section. `priority` is high, medium or low, beside horizon, and an absent one reads as `medium`. `size` is s, m, l or xl, required from capture. I wrote the one-line meanings myself: an hour or two; about a day; several days; split before Ready.
  - Migration window: the [repository-roadmap standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md#migration-tolerance) defines it. Until it closes, a missing size, a missing `kind` on an adopted open record, `initiative` and `purpose: adoption` warn. They fail from the first ki release after `ki work` shows no gaps across the estate.
  - Other standards updated: the Streams structure, the `ki-work` crosswalk, the Project registry's "Attributes by level" (the "only priority signal" wording is gone), and `ki-next` capture and selection.
  - Checkers: the roadmap and Streams checkers apply the new rules, with tests for them, and the Streams rubric was regenerated.
  - `initiative` and `purpose: adoption` are retired, with a tolerance note.
  - Checks: `bun run test` passes 1262 of 1262 and `bunx tsc --noEmit` is clean. The focused audits for `ki-skills`, `ki-work-roadmap` and `ki-work` pass. The `ki-work-roadmap` audit now warns 18 times, once for each harness record without a size; that is fleet backfill, not a failure.
- **ki-principal, `35d7947`, pushed fast-forward with only my commit.** It adds [GDR-KI-PRINCIPAL-016](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-016-priority-and-size-on-work-records.md), "Priority and size on work records", and indexes it under Work decisions in [Decisions.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/Decisions.md).
  - It reverses the 15 October PRIORITY-FIELD answer and records the retirements and the three fields kept. Your explicit instruction stands in for an Enactment record.
  - The pre-commit audit passed.
  - I left another session's dirty file alone: `+/_WORK/ki.chezmoi/decisions.md`, plus its untracked report and brief.
- **tools-ki, `c0ae063b` (ledger reservation) and `cc930b04`, pushed.** They capture [KI-TOOL-KI-CLI-155](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-155-priority-and-size-fields.md), "Priority and size fields", at triage. It is the handoff for the validator and `ki work`. I did not change the validator.
- **Net records:** 0 in ki-agentic-harness, 0 in ki-principal (the GDR is not a work record), and 1 in tools-ki.
- **Found while doing this, and handled:** today's `ki` rejects a roadmap record that carries any unknown field. In roadmap repositories, records cannot carry `priority` or `size` until a ki release accepts them.
  - `7b8c4fb1` makes writers adopt the fields with that release.
  - KI-TOOL-KI-CLI-155 puts accepting the fields first.
  - Until then, the harness checker's size warnings stand.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [GDR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-005-the-roadmap-model.md) still lists `adoption` among the purposes. GDR-KI-PRINCIPAL-016 records that it amends this, but I did not edit GDR-005 because the brief asked for one GDR. A one-line in-place update would align it.
- Owners backfill sizes by judgement, once a ki release accepts the field. No other repository's records were touched.
- When the window closes, the harness checker's warnings must change to failures, in step with that ki release. GDR-KI-PRINCIPAL-016 records this; there is no separate record.

## Queries

### DECIDE-KIND - `kind: decide` kept, not retired

**Context:** `decide` is on two live records: the website's home-page layout choice and the Tower data model. The roadmap standard's graduation test also names it. An idea becomes a record when "it is a decision with an owner and a needed-by date, adopted as `kind: decide`". Retiring it would mean rewriting that test, and those decisions would be filed as `investigate`, which closes on a finding rather than a decision.

**Query:** Should `kind: decide` stay?

**Options:**

a) (recommended, confidence high - another rule depends on it, it is in live use, and no tolerance cost) Keep it, as committed.

b) Retire it: fold decisions into `investigate`, rewrite the graduation test, and tolerate it during the window.

### RESOLUTION-TARGET - `resolution_target` kept, not retired

**Context:** No record carries it today, because only one record has ever been cancelled. It is the structured pointer that a duplicate, merged or superseded cancellation must give, and `ki-accept` requires it. The open harness record [KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md) plans to narrow it to same-repository targets rather than remove it.

**Query:** Should `resolution_target` stay?

**Options:**

a) (recommended, confidence high - it is required by the cancellation rules and by `ki-accept`, and already has a narrowing record) Keep it, and let KI-HARNESS-GOV-170 narrow it.

b) Retire it, and name the replacement only in prose in `## Cancelled`, which means changing `ki-accept` and the checker.

### TASK-LINKS - `task_links` kept, not retired

**Context:** Two records carry it. The Paperclip coordination standard names it as "the durable structured association" between a KI record and its Paperclip tasks. Paperclip is held under PAPERCLIP-REQ until Wave F, and this repository's AGENTS.md still grants Paperclip local delivery. Retiring it now would remove the link Paperclip depends on when it returns.

**Query:** Should `task_links` stay while Paperclip is parked?

**Options:**

a) (recommended, confidence medium - it is load-bearing for parked work, and if Wave F changes the Paperclip design this could be revisited) Keep it until PAPERCLIP-REQ is decided at Wave F.

b) Retire it now with a tolerance warning, and redesign the Paperclip link when Wave F returns.
