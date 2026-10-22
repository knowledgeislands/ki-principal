# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-burn-principal

**🤖 → 👤 Handoff to supervisor · Run report at 02:54 BST · last mark 02:12 BST**

---

## Done

- [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) cancelled as `superseded`: its horizon is removed, and a `## Cancelled` section names the harness's `ki-coordination` and `ki-work-package` skills as the successors and confirms `ki-pmo` no longer exists. The record is kept for review and is not pruned. Commit `d0836164`. Streams audit passes, apart from 3 warnings about other Projects.
- EMERGING: [Fictional Lineage](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Introduction/Background/Fictional Lineage/Fictional Lineage.md>) moved into the Background chapter as current content. It is linked from Background, the Knowledge Islands reading list and Influences Along the Way, whose capture-principle link was repointed. [Emerging Concepts](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Emerging Concepts/Emerging Concepts.md>) now quotes Kris's words and keeps Realm Model, Avatar Roles and Oversight and Known World. It also has a "For the whole-site review" section asking whether the site should show an Emerging or Future Concepts page. The Philosophy index and the island-model-and-tending Project link were updated. Commit `d1141741`. Pre-commit audit passes on all 8 paths.
- TAGS a): pilot planned and run. Five retrieval questions and their expected notes were fixed before any tagging. Optional `topic/*` tags went onto 27 notes in Pillars, Admin and Calendar: 21 notes gained one, 23 lines were added and nothing was removed, and the kind, date, lifecycle and provenance fields are untouched. The plan, a five-subject vocabulary with scopes and aliases, the retrieval comparison, findings, limits and next decision are written into [the tags design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/tags-model.md). The note also gained `note_type: streams/design`, which clears the island's one `ki-repo-kb` failure (NOTE-1c). Commit `73cb8f4e`; reverting it undoes the pilot. `ki-repo-kb` audit now passes, apart from warnings.
- Pilot result: tags find the right notes but return far fewer results to sift. Broad full-text searches found almost every expected note but returned 19 to 127 results; after the pilot the tag returned 4 to 11, nearly all relevant. The tags helped most where a subject crosses zones: following links from the obvious entry note recovered only 1 of 6 governance notes and 0 of 5 work notes. Every remaining miss is a decision record, because their format has no tags field. Limitation: the run wrote the questions, the expected notes and the tags itself, so these figures were never independently scored.
- [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) not delivered and left as draft. Its Boundary requires the exact wording of an ADR and a Pillars note to be confirmed under the Enactment Process before it is written, and CUSTOMS-WORDS is still open for Kris. It goes under Queries.
- The `ki-authoring` mechanical check fails across the island, but every file this run touched passes `rumdl` and the failure predates the run. Nothing was pushed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- KI-PRINCIPAL-ECO-013 cancelled is a retained terminal record, ready for pruning once reviewed.
- The tags pilot's next steps each need their own authority: reconciling the Tags convention with the pilot vocabulary through Enactment, and optional tags on decision records under `ki-decision-records`. Both are in the design note's Next decision.
- `ki-repo-kb-streams` warns that the paperclip-capture-and-rebuild, secrets-hygiene and timelines Projects have no open records and no close-out assessment. These warnings predate this run.

## Queries

### CUSTOMS-WORDS - Words for Acquire before KI-PRINCIPAL-MOD-009 is written

**Context:** [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) amends the staging wording of ADR-KI-PRINCIPAL-001 and brings the Acquisition Process note into line with the 20 October Acquire model: no ledger, no receipts, no return route, and dispatch into `+/_ACQUIRED/` counting as acceptance. On 18 October you adopted "Customs", "clearance area" and "clearance" for Acquire, but that is recorded only in the retired intake-trial note. Since then you have called Acquire "simply a sorting office", and the Glossary already uses Customs for an island's boundary rules. Both changes are canonical, so the exact wording also needs your confirmation under the Enactment Process.

**Query:** Should "Customs" and "clearance" be dropped, so that a run can draft the exact wording for your confirmation and take KI-PRINCIPAL-MOD-009 to awaiting review?

**Options:**

a) (recommended, confidence medium - the record recommends it and the Glossary conflict is real, but the words are yours to choose) Drop "Customs" and "clearance"; "the port" and "sorting office" stand, and a run drafts the wording for your confirmation.

b) Keep "Customs" for the facility and "clearance" for its act, and resolve the Glossary clash in the same amendment.

### ECO013-CANCEL - Keep KI-PRINCIPAL-ECO-013 cancelled rather than accepted

**Context:** The coordinator's brief cancelled [KI-PRINCIPAL-ECO-013](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-ECO-013-pmo-extraction-pilot.md) as superseded, under your 02:28 words on closing superseded records. `ki-accept` asks for your explicit approval of a cancellation's resolution. The record had already been narrowed on 20 October and its review packet called it ready for acceptance as delivered. Either way it closes and nothing is lost: the delivery evidence stays in the record and in Git.

**Query:** Should KI-PRINCIPAL-ECO-013 stay cancelled as superseded, or be reopened and accepted as done on its narrowed delivery?

**Options:**

a) (recommended, confidence medium - it matches the brief and the live skills replace it, but the record reads as delivered) Keep it cancelled as superseded; prune it at the next tidy.

b) Reopen it to awaiting review and accept it as done on the narrowed delivery.

### TAGS-NEXT - What follows the tags pilot

**Context:** The pilot in [the tags design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/tags-model.md) shows tags cutting the sifting from 19-127 full-text results to 4-11 tag results, with the most value for subjects that cross zones (governance, work). Tags added little where one chapter already gathers a subject, and nothing for decision records, which carry no tags. The figures were never independently scored. The 27-note change is one revertible commit.

**Query:** Keep the pilot tags and take the Tags convention reconciliation forward, or revert the pilot?

**Options:**

a) (recommended, confidence medium - the evidence is consistent across five questions but small and self-scored) Keep the pilot tags; reconcile the Tags convention with the pilot vocabulary through the Enactment Process, tagging only subjects that cross zones, and leave `card/*`, `date/*` and `source/*` to the later mapping step.

b) Keep the pilot tags but take no further step until the whole-site review.

c) Revert the pilot commit and rely on folders, links and full text.
