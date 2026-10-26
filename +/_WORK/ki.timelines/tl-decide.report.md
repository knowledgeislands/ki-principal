# [Foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/timelines.md) › tl-decide

**🤖 → 👤 Handoff to supervisor · Run report at 00:38 BST · last mark 19:03 BST**

---

## Done

- Wrote the decided design, [timelines-skill-design.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/design/timelines-skill-design.md). Every settled point is cited by its decision tag, or marked "merge" where the merged report settled it on evidence. It covers the scope, the dated-item model, sources, sets and feeds, the view data format (`<skill>-view/1`, a superset of 5G's `ViewData`), checks, the code home and privacy rules. The name appears as `<skill>` throughout.
- Settled two points myself and flagged both for harness planning to confirm. UIDs take the form `<logical id>@<uid domain>`, which combines the merge's base namespace with 5G's existing host suffix, so 5G's UIDs stay exactly as they are. And an invalid timed busy item shows in views with its diagnostic but is left out of feeds until fixed (my reading of TIMED-BUSY).
- Wrote the rollout plan in the ADOPTION-ORDER sequence as seven steps. Each step names its owning repository, its entry check and its proof. The plan also says that records outside the Knowledge Islands territory use `project: ki-principal/timelines`.
- Drafted the handoff for [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) in the note's last section, ready to route. It proposes a project change, plus Context, Boundary, Shaping, Dependencies and Verify text. It quotes the decisions in words and links only durable documentation. It is marked as not blocking any ki-principal record.
- Committed the note by explicit path as `46d2b5e4`; the commit hook's repository audit passed with no failures. Not pushed.
- Changed nothing in the harness record, 5G Emerge, legal-principal or personal-principal. Ran no `ki repo conform`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- SKILL-NAME is still with Kris in `queries.md`, and the design leaves it as `<skill>`. Step 1's entry check needs the answer before the harness creates the skill.
- Three points are left for the harness to settle when it plans [KI-HARNESS-GOV-222 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md): where a base's manifest lives (`.ki.toml` or a declared file), how a cancelled item is projected, and the two readings above. They are listed in the handoff, not put to Kris.
- The coordinator still has to route the handoff through State of play.

## Queries

### PROVIDER-FIRST - Which calendar provider the first sync adapter targets

**Context:** Under FEED-HOME, account sync comes after connector work and is proved on a test calendar before any real dates. That makes rollout step 4 belong to `mcp-gsuite`, `mcp-m365` or both. Both reviews checked the connector code. Google can already pick a calendar and update an event by its id, but it lacks all-day writes, transparency and a created-by marker. Microsoft has no update tool, no calendar picker and no busy-status field, so it needs more work. One review also notes, from prior knowledge and not verified, that a dedicated Google calendar has its own secret address, which would give subscriptions on Kris's other devices. Which calendar Kris actually schedules from is not known. Nothing needs this answer until steps 2 and 3 are done.

**Query:** Should the first calendar-writing connector work and the adapter proof target Google, Microsoft or both?

**Options:**

a) (recommended, confidence medium - Google has fewer gaps in code both reviews checked, but which calendar Kris schedules from is unknown and the secret-address benefit is unverified) Google first, through `mcp-gsuite`, with Microsoft only if the acceptance matrix or Kris's scheduling tool calls for it.

b) Microsoft first, through `mcp-m365`, if Kris's real scheduling happens in Outlook.

c) Both together, so the acceptance matrix covers both from the start, at roughly twice the connector work.

d) Leave it open until step 4 is due.

### 🤖 → 👤 Handoff to supervisor · since 00:38 BST

👤 2 with you

- [with you] PROVIDER-FIRST · owner · since 00:38
- [with you] SKILL-NAME · owner · since 2026-10-20
- [committed] design note
- [unpushed] design note commit
