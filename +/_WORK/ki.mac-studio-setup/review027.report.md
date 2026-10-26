# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › review027

**🤖 → 👤 Handoff to supervisor · Run report at 01:36 BST · last mark 23:36 BST**

---

## Done

- Independently reviewed [KI-TOOL-RIG-CLI-027](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.mdCLI-027) at `66c9c57`; the primary checkout was clean at the start, and all reviewed runtime functions exactly match their assembled executable copies.
- Repeated status options: confirmed a contract defect; all four named options pass parsing, with the last profile retained, while repeated format is rejected; see [status parser](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/22-observation.bash:1044) and [RIG-PORT-014](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/portability.md).
- Removal pre-scan: confirmed a literal-value defect in [report buffering](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/30-commands.bash:1293); it treats a profile value resembling the format option as an option itself, despite the [normaliser](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/00-runtime.bash:193) preserving it correctly.
- Apply synopsis: confirmed a documentation alignment defect; the [authored inventory](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/00-runtime.bash:178) and parser accept sudo, but the [consumer synopsis](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/user/commands.md:13) and [manual synopsis](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/man/rig.1:41) omit it, contrary to [RIG-PORT-007](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/specs/portability.md); both documents explain it elsewhere.
- Read-only checks: isolated in-memory Bash probes confirmed duplicate acceptance and removal argument corruption, with operational resolution replaced by a stopping stub; exact predicates verified the specification clauses and synopsis omissions.
- Provenance: the removal pre-scan is byte-identical to the immutable baseline, and both synopsis omissions predate delivery; no repository edits, commits, records, remote calls or machine operations were made.
- Concurrent work: an unrelated [roadmap record](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) changed during review and was left untouched; the reviewed delivery paths and HEAD remain unchanged.

## In Progress

Nothing is running. The supervisor owns the disposition decision below; implementation and acceptance remain outside this review.

Outstanding - no action requested now: the full repository gate was not rerun because this brief forbids tests that write; the delivery record's prior gate results were not independently revalidated.

## Queries

### [Q-027-REPEATS - Resolve the three concerns before acceptance](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.mdCLI-027)

**Context:** The record has no separate Acceptance heading; its Goal, Boundary, Design, checked Steps and Verify section define the acceptance boundary. Repeats contradict the newly added grammar's rejection rule and its conforming claim. The removal concern also contradicts the Design's verbatim-value promise: the originally recorded example still ends in usage error, but a profile value resembling the format option is stolen even when the remaining arguments are well formed; a comparable option-like value reaches profile resolution. The sudo omission is lower severity and pre-existing, but these synopses were changed by this delivery, whose Steps explicitly invoke public-interface alignment. It needs only a documentation correction, not new privilege behaviour. All three therefore have an existing owner in this record; their age does not make the present acceptance claims true.

**Query:** Should all three be corrected within the existing record before acceptance?

**Options:**

a) (recommended, confidence high - direct source checks and isolated probes establish small defects against this record's grammar and alignment promises) Make one follow-up commit within [KI-TOOL-RIG-CLI-027](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.mdCLI-027) before acceptance: reject the four duplicate status options, make the removal format scan respect value boundaries, and add sudo to both apply synopses; add focused regression coverage, regenerate the executable and run the required gate. Create no Triage record.

b) Fix only the duplicate status options and retain the other two as recorded concerns, explicitly acknowledging that the verbatim-value and synopsis-alignment claims remain incomplete.

c) Defer a demonstrated parser defect to coordinator-created Triage under CAPTURE-GATE, and retain the synopsis omission as a concern; runs create no records, and speculative capture remains excluded. This fragments work already owned here and does not resolve the current acceptance mismatch.

### 🤖 → 👤 Handoff to supervisor · since 01:36 BST

👤 1 with you · 🅿️ 0 parked

- [with you] Q-027-REPEATS · supervisor · since 01:36 BST
