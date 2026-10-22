# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › field-survey

**🤖 → 👤 Handoff to supervisor · Run report at 08:24 BST**

---

## Done

This was a read-only survey: no edits, commits or pushes anywhere, and the net record count is zero in every repository. Usage counts come from a frontmatter and heading scan of all 316 records in the 31 registered repositories that hold `docs/roadmap/` or `Streams/Roadmap/` (210 roadmap, 106 KB Streams). `ki-design`, which is outside the registry and outside this run's scope, holds 10 more. The SIZE-PRIORITY entry quoted 367 records. That count was taken differently, and I have not reconciled the two.

Sources:

- Standards: [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md), [repository-roadmap standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-repository-roadmaps.md), [Streams structure](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb-streams/references/standards-streams-structure.md), [ki-work adapter crosswalk](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-change-management-adapters.md), [Project registry "Attributes by level"](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-project-registry.md) and [ki-repo-kb universal fields](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-kb/references/standards-frontmatter.md).
- Validators: harness audit checker [roadmap-evidence.ts](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/scripts/rubric/contexts/roadmap-evidence.ts) (A), and tools-ki reader [items.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/work/items.ts) behind `ki work` (W).
- ki-specifications has no work-item schema: its only schema is `knowledge-package.schema.json`.

### Table 1 - Current fields

In the Validator column, A is the harness audit (`ki repo audit`) and W is tools-ki `ki work`. "fail" means the record is rejected or the audit fails, "warn" means a warning only, and "-" means the field is not checked. Use is the number of records carrying the field, out of 316, and the number of repositories, out of 31.

| Field | Meaning | Values | Required | Validator | Use |
| --- | --- | --- | --- | --- | --- |
| `id` | Record identifier matching the filename | `<REPO>[-<AREA>]-<NNN>` | always | A fail · W fail | 316 / 31 |
| `area` | Immutable issuing code inside the identifier | `.ki.toml` area map | when the repository declares areas, otherwise forbidden | A fail · W - | 236 / 25 |
| `title` | Compact label | at most four words | always | A fail (ITEM-1) · W fail if empty, length not checked | 316 / 31, 25 over four words in 6 repos |
| `status` | How far the work has got | `triage` `draft` `ready` `in-progress` `awaiting-review` `done` `cancelled` | always | A fail · W fail | draft 168, triage 71, awaiting-review 41, in-progress 16, done 16, ready 3, cancelled 1 |
| `horizon` | When the work is intended (the only priority signal today) | `now` `next` `soon` `future` `hold` | exactly when adopted and open | A fail on missing, retired or disallowed values · W fail on missing, legacy values tolerated and reported | 228 / 30: now 61, future 42, next 35, soon 19, hold 16; retired `triage` 45, `waiting-for` 8, `parked` 2 |
| `hold` | Why held and the release condition | `reason` (`waiting-for`, `parked`), `condition`, optional `review` date, optional `trades` | exactly when `horizon: hold` | A fail · W fail | 16 / 10, `review` on 11 |
| `blocks` / `blocked_by` | Local build-order dependencies | arrays of same-repository identifiers, `[]` when empty | always | A fail (ITEM-5: reciprocal, acyclic) · W fail on shape only | 316 / 31 |
| `baseline_ref` | Commit where execution began | `null` or a full commit ID | always | A fail, including null or set by status · W fail on shape | 316 / 31 |
| `created_at` / `updated_at` | Creation and last semantic change | RFC 3339 UTC at second precision, created no later than updated | always | A fail · W fail | 316 / 31 |
| `kind` | Controlling outcome | `deliver` `decide` `investigate` `audit` | once adopted | A fail on bad value, warn when missing · W fail on bad value, legacy when missing | 140 / 24 (deliver 128, audit 6, investigate 4, decide 2); 106 adopted open records lack it |
| `purpose` | Why the work exists | `capability` `corrective` `debt` `governance` `learning` `adoption` `upkeep` | optional | A fail on bad value · W fail on bad value | 97 / 17 (capability 48, corrective 27, governance 10, debt 8, upkeep 3, learning 1, adoption 0) |
| `project` | Territory Project served | registry slug, optionally `<territory>/<slug>` | optional | A warn if unknown · W fail on shape | 65 / 12 |
| `theme` | Territory theme for projectless work | registry slug | projectless records only | A warn if unknown or redundant beside a Project · W fail on shape | 121 / 13; 12 records in personal-principal also name a Project |
| `initiative` | Thread-model name for theme | slug | legacy | A warn, fail if beside `theme` · W legacy | 13 / 3 |
| `component` | Repository part touched | `.ki.toml` `components` | optional | A fail if undeclared · W fail if undeclared | 49 / 7 |
| `resolution` | Why cancelled work ended | `obsolete` `rejected` `duplicate` `merged` `superseded` | exactly when cancelled | A fail · W fail | 1 / 1 |
| `resolution_target` | Record that replaced it | canonical identifier | for duplicate, merged and superseded only | A fail · W fail | 0 |
| `transferred_from` | Handoff origin | non-empty text | optional | A - · W - | 7 / 3 |
| `task_links` | Links to external tasks, such as Paperclip | provider map of six-field references; relation from a fixed list | optional | A fail on shape, plus ITEM-6 judgement · W fail on shape | 2 / 2 |
| `housekeeping_template` / `scheduled_for` | Recurring-run link and due date | template id and ISO date | recurring runs only | A fail on linkage (ki-work-recurring) · W allowed | 1 / 1 |
| `note_type`, `tags`, `created`, `updated`, `reviewed`, `author` | KB universal note fields | per ki-repo-kb | KB Streams only, optional | A (Streams) allowed · W allowed in KB, fail in roadmap | note_type 38 / 6, tags 8 / 2 |
| `priority` (not in the standard) | - | - | none | A (Streams) warn as unknown · W warn ("horizon is the only priority signal"), fail in roadmap repositories | 5 / 1 (legal-principal: medium 3, high 1, low 1) |
| `waiting_on_trades`, `intake_disposition(_target)`, `candidate` | Retired | - | must be absent | A fail · W tolerated as legacy (`candidate` would fail as unknown) | 0 |
| Body: `Goal`, `Context`, `Boundary` ... `Discussion` last | Outcome, evidence, exclusions, reasoning | Goal non-empty | always | A fail (ITEM-3), with Goal quality judged under ITEM-4 · W - | Goal 316, Boundary 316, Context 312, Discussion 299 |
| Body: `Shaping` | Approach, dependencies, open decisions, promotion conditions | - | at Soon | A - (not deterministic) · W - | 26 |
| Body: `Current state`, `Steps`, `Files touched`, `Verify`, `Dependencies / blocks`, `Documentation impact` (Decision Records, Specifications, Guides, Roadmap) | Plan | Steps as `- [ ]` / `- [x]` | Now and Next | A fail · W - | 100 to 132 each, plus 15 with variant casing or names such as `Dependencies and Blocks` |
| Body: `Delegation` | Worker deliverables and gates | - | when delegated | A - · W - | 20 |
| Body: `Review` (Delivered, Change Summary, Verification, Outstanding concerns, Post-change review, Mini recap) | Acceptance packet | - | at awaiting-review and after | A fail on shape · W - | 58 |
| Body: `Done` / `Cancelled` | Who accepted or cancelled, and when | one line | at done or cancelled | A fail · W - | 16 / 0 |

### Table 2 - History

Commits are in ki-agentic-harness unless another repository is named. The work-item format's history is in `git log` of [standards-work-item-format.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md).

| Field | Status | Date | Deciding source | Reason |
| --- | --- | --- | --- | --- |
| `phase` | rejected | 2026-07-02 | `6b47cfc8` ki-plans plan format | Phasing lived in `ROADMAP.md`, and a plan existed only for Next work. |
| `roadmap` (plan to item link) | reversed | 2026-07-29 | `99a6a464`, the cutover to flat work items | The plan and the item merged into one file. |
| `horizon` | adopted, then changed | 2026-07-29; 2026-10-07 | `99a6a464`; [GDR-KI-PRINCIPAL-005](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-005-the-roadmap-model.md) with `1780ff75` and `067dc0ff` | It began as six horizons, Blocking, Next, Soon, Waiting for, Parked and Future, and became now, next, soon, future and hold. Waiting-for and parked moved into the `hold` mapping, and triage moved to `status`. |
| `status` | adopted, changed three times | 2026-07-02; 2026-08-05; 2026-09-14; 2026-10-07 | `6b47cfc8`; `f0ad297e`; `9be803f6`; GDR-KI-PRINCIPAL-005 | It went from open, in-progress and done to draft to done, then gained triage intake, then cancelled with a resolution. |
| `theme` (free-text grouping, and the code in the identifier) | adopted, changed, retired, readopted | 2026-07-29; 2026-08-09; 2026-10-07; 2026-10-18 | `99a6a464`; `2de4c1a6` and `6f4fe7e8`; `1780ff75`; [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md) with `c0759d85` | The identifier code became `area`, and the grouping gave way to `initiative` and `project`. It came back as a territory theme label under the work model. |
| `initiative` | adopted, then reversed | 2026-10-07; 2026-10-18 | GDR-KI-PRINCIPAL-005 (`1780ff75`); GDR-KI-PRINCIPAL-009 | "Initiatives become themes". It now warns during the tolerance window of [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/08468196/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md). |
| `candidate: true` | adopted, then reversed | 2026-07-29; 2026-09-14 | `99a6a464`; `9be803f6` | It marked speculative Future work, and the `triage` status replaced it. |
| `priority` and `dependencies` (old Streams proposals: urgent, high, medium, low) | reversed | 2026-08-05 | `f0ad297e`, which unified the roadmap and Streams lifecycle | Streams adopted roadmap records, with `horizon` for queue position and `blocks` / `blocked_by` for order. |
| `blocks` / `blocked-by` | adopted, then changed | 2026-07-02; 2026-08-10; 2026-09-08; 2026-10-09 | `6b47cfc8`; `584bcebf`; `5580cd47`; `4de7f5a2` | The fields became snake_case, then were defined as build order rather than lifecycle waits, then restricted to same-repository identifiers. |
| `baseline_ref`, `transferred_from` | adopted, then renamed | 2026-07-29; 2026-08-10 | `99a6a464`; `584bcebf` | The kebab-case names became snake_case. |
| `housekeeping_template`, `scheduled_for` | adopted | 2026-08-10 | `584bcebf` with ki-work-recurring | They link recurring runs. |
| `waiting_on_trades` | adopted, then reversed | 2026-08-10; 2026-10-07 | `584bcebf` (trades `bb69054c`); `067dc0ff` | `hold.trades` replaced it. |
| `title` of at most four words | adopted | 2026-08-05 | `f51e2bf3` | A compact list label; the detail goes in the Goal. |
| `area` | adopted, then changed | 2026-08-09; 2026-10-07; 2026-10-15 | `2de4c1a6`; `067dc0ff`; AREA-WORD, in ki-principal `b4a2306` | It became a fixed issuing code, declared as a code-to-title map, and "area" was reserved for namespaces. |
| `created_at` / `updated_at` | adopted | 2026-09-13; required 2026-09-14 | [GDR-KI-HARNESS-008](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/decisions/GDR-KI-HARNESS-008-portable-work-item-timestamps.md); `50af8c2e`; `b2d7c3cd` | Portable age and staleness, without event history. |
| `intake_disposition(_target)` | adopted, then reversed | 2026-09-14; 2026-10-07 | `9be803f6`; `067dc0ff` | The cancelled status with `resolution` replaced it. |
| `task_links` | adopted | 2026-09-27 | `0a89f7af` | A per-item map to external tasks that does not claim ownership. |
| `kind`, `purpose`, `project`, `component`, `hold`, `resolution`, `resolution_target` | adopted | 2026-10-07 | GDR-KI-PRINCIPAL-005 (`1780ff75`, `31dea9bb`) | Roadmap model v1: one territory classification vocabulary. |
| Type field on Projects and themes (TYPE-FIELD) | rejected | 2026-10-15 | ki-principal `ef5deac` types-review report; crosswalk `45bbaea6` | `kind` and `purpose` stay on records only. The crosswalk shows Type "None" for Projects and themes. I took the answer from the crosswalk and did not find Kris's literal answer. |
| Pause condition as front matter (PAUSE-CONDITION) | rejected | 2026-10-15 | ki-principal `b4a2306` | "No new front matter": the release condition goes in a line in the Project's Notes. This is a Project-level decision. |
| `priority` (PRIORITY-FIELD) | rejected | 2026-10-15 | ki-principal `b4a2306`, from query `ef5deac`; tools-ki `6aa676a0` (2026-10-16) | The field was removed from [KI-PRINCIPAL-MOD-006 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/b4e46eda/Streams/Roadmap/KI-PRINCIPAL-MOD-006-knowledge-acquisition-lifecycle.md) and [KI-PRINCIPAL-MOD-008](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-008-whole-philosophy-coherence-review.md). Unknown fields now warn, and "horizon stays the only priority signal". |
| `priority` and `size` (SIZE-PRIORITY) | proposed, vocabulary decided, delivery stopped | 2026-10-19 08:06 to 08:17 BST | [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), "owner request, SIZE-PRIORITY" and "owner answers, mark recap" | Both required from capture: priority high, medium or low; size s, m, l or xl, with xl meaning split before Ready; warn first, then fail. The size-priority run's status reads "STOPPED by owner" at 08:17 BST. It left an uncommitted 5-line edit in the harness work-item format. No GDR or tools-ki follow-up exists yet. |
| `groups` (topical metadata) | parked | 2026-08-09 | `a7af666a` | Identities were separated from groups. A base may choose a vocabulary, but no standard defines one. |
| Owner or assignee, due or target date, effort or estimate | never proposed for records | - | none found | A record's owner is its repository. Projects carry `lead` and a target. Dates on records are only `hold.review` and `scheduled_for`. "Effort" appears only as agent effort. |
| Body sections | adopted over time | 2026-08-02 to 2026-10-16 | `831e1aa4` (Goal), `0a8da798` (task-list Steps), `3e283758` (Review shape), `4677aa94` (Documentation impact), `5f8dff6b` (Outstanding concerns need identifiers), `05ee5b1f` (pull-request link in the body, not a field) | Each change hardened what the checker can test. |

### Observations

- **Priority overlap.** Horizon, `blocked_by` and the proposed `priority` all say "what first". The [crosswalk](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work/references/standards-project-registry.md) still says "`horizon` only", and both validators still warn on `priority`, while this morning's answers point the other way.
- **Classification overlap.** `theme` and `project` overlap, and naming both is redundant: 12 records in personal-principal do it. `initiative` is still on 13 records.
- **Retired shapes still in use.** The standard says the checker fails retired horizons, but 55 records in 11 repositories still carry `horizon: triage`, `waiting-for` or `parked`. tools-ki tolerates them, so `ki work` and `ki repo audit` disagree. Those repositories evidently do not run the roadmap audit to green.
- **Unchecked or warn-only fields.** `kind` is required once a record is adopted, but a missing one only warns, and 106 adopted open records in 12 repositories lack it. 25 titles exceed four words. 17 records lack `## Discussion`, and 15 use variant section names.
- **Fields and vocabulary values that are hardly used.** `decide` appears twice, `adoption` never, `resolution_target` never, and `task_links` twice.
- **In use but outside the standard.** `priority` appears on 5 records in legal-principal. The repeated `## Machine responsibilities` section is on 16 records, and dated "follow-up - 16 October" sections are on several. There are no unknown fields beyond these.
- **Points to discuss:**
  - Does `priority` replace or sit beside horizon's selection role?
  - Is `size` enough on its own, without effort, owner or due date?
  - Should missing `kind` stop warning and fail, now that 106 records lack it?
  - Who migrates the 55 retired horizons?
  - Should tools-ki fail what the harness fails?

## In Progress

Nothing is running.

Outstanding - no action requested now: the uncommitted SIZE-PRIORITY edit in [standards-work-item-format.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md) belongs to the stopped size-priority run. I left it untouched.

## Queries

### SIZE-PRIORITY-EDIT - The stopped run's uncommitted edit

**Context:** The size-priority run stopped at 08:17 BST in the middle of an edit. It left `priority` and `size` in the work-item format's required list and examples, uncommitted in ki-agentic-harness's primary checkout. The format links to a "Priority and size" section that does not exist yet. Any other session committing in that checkout must work around the dirty file.

**Query:** Should the half-made edit wait for the outcome of this field discussion, or be removed now?

**Options:**

a) (recommended, confidence medium - the discussion may change the shape of the edit) Leave it in place until the discussion settles, then let one run either finish it under a GDR or revert it.

b) Have a run restore the file now and restart SIZE-PRIORITY from clean once the discussion has settled.
