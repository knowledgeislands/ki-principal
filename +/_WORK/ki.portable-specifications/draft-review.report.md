# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › draft-review

**🤖 → 👤 Handoff to supervisor · Run report at 23:59 BST · last mark 23:45 BST**

---

## Done

- Read-only review completed for all five draft 0.2 files; no repository changes, commits or remote calls.
- Owner definitions checked: knowledge's description routes by topic, audience, depth and questions; acquire addresses acquisition itself and explicitly scales down for learning a tool; work separates the main house roles, ordering and reporting rules into the profile, subject to the findings below.
- Recorded decisions checked: owning skills, upper-case entry names, permanent version-1 default, unsupported-major rejection, metadata strings, one validity level, soft limits, mapped house profile and later publication/handoff are represented; no publication or move was attempted.
- Agent Skills evidence checked against the live-check note and its locally retained specification, parser and validator; all three source SHA-256 values match the note.
- Compatibility checked directly with the cached validator's metadata-validation function: both knowledge examples and both acquire examples pass; undotted work passes after entry renaming, while dotted work fails; extra companion files are not rejected.
- House profile checked against the current work-package standard and Work Process note: all seven state mappings are correct, including supervisor-held work mapping to active; all current house field names appear, with conversion precision needing improvement below.
- Progressive disclosure and attribution checked: the three tiers and attribution lines are present; the work tier's aggregate budget and several consistency points need clarification below.

### Part 1 - must fix

1. **New packages are simultaneously permitted and forbidden to have empty entry/state files.** [work.md:31](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:31) permits all five files to start empty or with a placeholder, but [work.md:183](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:183) requires definition and state front matter, including a valid initial state. Limit the empty-file allowance to the query, message and decision files, and require a valid definition and state at creation.

2. **Cross-package relative references conflict with package-contained validation.** [work.md:199](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:199) permits relative citations of knowledge/acquire packages while expressly keeping them outside the work package; [work.md:188](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:188) rejects relative links that leave it. The same distinction is unresolved for acquisition relationships and evidence provenance in [knowledge.md:93](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:93), [knowledge.md:104](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:104), [knowledge.md:138](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:138), [acquire.md:90](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:90) and [acquire.md:142](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:142). Distinguish internal resource links from external package/evidence references, and define how each resolves and validates; otherwise the advertised cross-package citation cannot conform.

3. **The blanket claim that work cannot be a valid skill is false.** [specs.md:23](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:23) treats dotted names and extra required files as universal barriers, and [work.md:195](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:195) generalises the dotted-name case to every work package. The work grammar also permits undotted names: its minimal example passes the cached validator's metadata checks, and Agent Skills permits additional files. State that the original entry filename is different and dotted names fail after renaming, while an undotted package can pass after renaming. Do not describe extra companion files as a validator failure.

### Part 1 - should fix

4. **The stated Sources minimum is only a recommendation in the normative draft.** [specs.md:43](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:43) presents source naming as what knowledge requires, but [knowledge.md:100](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:100) makes Sources one of the recommended sections and [knowledge.md:135](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:135) does not require it. Make that existing minimum explicit, including provenance for curated run output, or soften the overview's claim. Broader curation obligations remain the separate CURATION-OWNER decision.

5. **The house mapping is not yet a deterministic conversion.** [work-house-profile.md:43](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:43) and [work-house-profile.md:58](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:58) group fields under illustrative prefixed names without specifying every destination key; nullable timestamps/revisions also lack an omission-versus-string rule, although one nullable theme case is covered. Spell out destination names and conversions for booleans, nulls and timestamps so two portable readers preserve the same meaning. The seven-state mapping itself needs no correction.

6. **Work changes the progressive-disclosure budget without identifying the aggregate difference.** [work.md:170](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:170) loads all five files in full and [work.md:173](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:173) gives each roughly 5,000 tokens, allowing a roughly 25,000-token second tier; [work.md:194](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:194) describes the size conventions as unchanged from Agent Skills' roughly 5,000-token entry body. Specify a combined recommendation or expressly describe the larger aggregate budget as a difference. The limits should remain advisory under CONFORMANCE-LEVELS.

7. **Acquire's script guarantees are partly its own additions.** [acquire.md:113](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:113) introduces dry-run and source-shape stopping requirements under an Agent Skills attribution. The cached Agent Skills script section recommends self-contained dependencies, helpful errors and graceful edge cases; it does not impose those two requirements. Separate the inherited recommendations from acquire's added guarantees and identify the latter under its differences.

### Part 1 - nit

8. **Relationship prose overstates optional reciprocal fields.** [specs.md:41](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:41) and [acquire.md:154](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:154) describe every acquisition method and knowledge package as naming each other, but their relationship fields are optional and [specs.md:55](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:55) explicitly allows transient output without a destination package. Qualify reciprocity as applying when that persistent relationship is declared.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Supervisor-owned follow-up: reconcile the findings before approving the next draft; this run made no corrections.
- Verification limitation: the full skills-ref CLI was not executed because the retained source subset lacks its parser dependency; the original validator's metadata checks were executed, and parser/validation behaviour was inspected directly. No dependency was installed.
- Retained material: this report is the sole report artefact; this run left no temporary files in its temporary directory.

## Queries

### CURATION-OWNER - Who owns what curation must do and record?

**Context:** This blind recommendation follows the owner's definitions, the recorded ownership of knowledge in ki-knowledge-package and acquire in ki-acquire, the acquisition-practice boundary, and the drafts' Sources, Output, Limits and refresh provisions. A source-faithful capture and a selected, organised knowledge package make different promises. The destination's quality contract should state the minimum evidence of curation; detailed capture and acquisition practice can remain with ki.knowledge-acquisition. A short section can record selection/scope, material transformations or synthesis, unresolved uncertainty and provenance without prescribing a house workflow.

**Query:** Who should own what curation must do and record?

**Options:**

a) (recommended, confidence high - the knowledge owner already owns the curated result and its rubric, independently of how material was acquired) "`ki-knowledge-package` owns curation guidance, and `knowledge` gains a short Curation section on what a curated package must record."

b) "The specs keep only the Sources requirement; curation practice goes to ki.knowledge-acquisition."

c) "`ki-acquire` owns it as the last stage of acquisition, and `acquire`'s Output section names what curation receives."

### 🤖 → 👤 Handoff to supervisor · since 23:59 BST

👤 1 with you

- [with you] CURATION-OWNER recommendation · owner · since 23:59 BST
