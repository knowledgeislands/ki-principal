# Knowledge graph folder: design note

Design note for [ki.sop.main](../work.md), focus `_emerging`, under the `ki-work-design` method. It answers KNOWLEDGE-FOLDER, Kris's ask relayed by `personal.reg.assistant-terra` (ATER-005 IMPORTANT 22:47 GMT, ATER-007 22:49 and ATER-008 23:22, 4 November 2026): "take this on for Knowledge Islands Principal, quickly", and say how State of play would plan it. The source is the [knowledge folder proposal](https://github.com/krisb/inbox/blob/792fb629c0df9b9e904eb08d99dc2663f8d509fe/+/_WORK/personal.reg.inbox-terra/capture/knowledge-folder.proposal.md), with its "Pulling from the assistant's graph" and "Layered graphs" sections.

Status: draft, brief and proposed-plan stage, 4 November 2026. No independent review has run and nothing in the island has changed. The method's next step is two blind reviews of this plan before the merged report; the queries at the end go to Kris with it.

## Summary

Knowledge Islands Principal gains a top-level `knowledge/` graph beside `Pillars/`, and `Pillars/` empties into it over time. The plan runs in four phases: adopt the standard and open the folder with its home page; pull the assistant's staged Knowledge Islands cards across as the first nodes; upgrade Pillars subtree by subtree, leaving a pointer behind each page; and retire `Pillars/` when it is empty. Everything is one Enactment record plus one governance decision for the first two phases, then one record per Pillars subtree. Five of the proposal's seven questions need Kris; the evidence settles two, and narrows the rest to a recommendation each.

## Evidence read

- **The island's rules.** Root `AGENTS.md` names five zones and strictly enforces the Pillars/Resources boundary, the Enactment gate on `Admin`, `Pillars` and `Resources`, and a same-name index note in every folder. [Structure](../../../../Pillars/Philosophy/Model/Conventions/Structure/Structure.md) defines the Library as Pillars and Resources, Streams as status trackers that link into Pillars, and folder notes named after their folder. The [Enactment Process](<../../../../Admin/Operations/Processes/Enactment Process.md>) requires a record for new or reworked canonical content and "any batch rename or structural reorganisation", and lets one bounded owner approval stand in for a record over a batch of related edits.
- **The assistant's graph.** `curated/knowledge-islands/ki-principal/Pillars/` in the assistant repository already holds 41 kebab-case cards staged for this island: 19 under `knowledge-graph/`, 15 under `knowledge-tending/`, 2 under `iconography/`, 1 under `ethical-knowledge/`, and the `ki-principal.md` and Knowledge Islands roots. Each carries front matter `id`, `title`, `type`, `status`, `territory`, `island`, and a `links` map from a local alias to a `predicate`. Predicates in use are `ki:part-of`, `ki:has-member`, `ki:concerns`, `ki:uses-principle`, `ki:supports` and `skos:related`. Most cards are `status: proposal`.
- **The island today.** `Pillars/` holds 129 Markdown files in 65 folders across Philosophy, Aesthetics, Engineering Practice and Technē. 29 files in the agentic harness cite `Pillars/` paths, most of them under `Pillars/Philosophy/Model`, so a moved page must leave a pointer or the harness breaks.
- **The folder-note clash.** The coordination baseline already starts work-package focus folders with `index.md` (this folder has one), while the island's rule is a same-name note and the proposal asks for `_index.md`.

## Units of comprehension

| Unit | Boundary | Hand-offs |
| --- | --- | --- |
| Graph standard | What makes a `knowledge/` folder: naming, node minimum, folder note, link rules | Written into `ki-repo-kb` by the harness; this island adopts it by decision |
| Island adoption | This island's governance: Structure, Enactment Process, Routing Rules, `AGENTS.md` and one governance decision | Reads the standard; gates every pull |
| Home page | `knowledge/_index.md`, the graph's entry point and map of content | Points into Pillars until a node replaces each page |
| Pull | Moving one card or Pillars page into `knowledge/` as one or more nodes | Leaves a pointer at the old place; updates the home page |
| Attachment point | A node this graph promises not to move, which other graphs may pin | Declared here; read by the assistant's shadows |
| Shadow node | A read-only pointer in another repository's graph to an attachment point | Owned by that repository, never by this island |
| Checks | KIG and rubric checks that nodes, links and pointers hold | Harness and `tools-kig`, by message |

## The plan

### Phase 0 - adopt (one sitting, Kris's go)

1. Kris answers the queries below; State of play records each in the `ki.sop.main` decisions log.
2. One governance decision record, `GDR-KI-PRINCIPAL-<next>`, in the shape of [GDR-KI-PRINCIPAL-002](../../../../Admin/Governance/Decisions/GDR-KI-PRINCIPAL-002-admin-zone-governance-and-operations.md): `knowledge/` becomes the island's internal-knowledge zone, replacing `Pillars/` over time; the node minimum, folder note and link rules below; Resources stays outside.
3. One Enactment record in `Streams/Roadmap/`, captured through `ki-next`, covering phases 0 and 1 as related changes: the decision, Structure (top-level table, routing rule 3, the boundary and folder-note sections), the Enactment Process's Stores bullet, Routing Rules, and root `AGENTS.md` (exempt from Enactment, but changed in the same commit so the rules agree).
4. A line to the agentic harness's `messages.md` asking it to carry the graph standard in `ki-repo-kb` and its rubric, so the island's index-note audit accepts `knowledge/_index.md`. It is not blocking: the island can run ahead of the audit for one cycle, its findings noted as expected.

### Phase 1 - first slice (the record above, delivered in one run)

1. Create `knowledge/_index.md`: what the graph is, its attachment points, and a map of content whose entries point into Pillars where nothing newer exists yet.
2. Pull the assistant's 41 staged cards into `knowledge/knowledge-graph/`, `knowledge/knowledge-tending/`, `knowledge/iconography/` and `knowledge/ethical-knowledge/`, each folder with its `_index.md`. Each card keeps its `id` and links; `island` and `territory` stay; `status` stays as the card had it, so a `proposal` card arrives as a proposal, not as settled practice.
3. Where a pulled card overlaps a Pillars page (the capture funnel against the Work Process and Acquisition material is the clearest case), the node links to the page as a legacy note; nothing in Pillars changes in this phase.
4. Declare the first attachment points: only the cards Kris names (query ATTACH-SET), recommended to be the three the proposal's picture shows, the capture funnel, the knowledge graph and the work process once it is pulled.
5. Send `personal.reg.inbox-terra` one line naming the canonical paths, so the assistant replaces its copies with shadow nodes under its own `context/`. The assistant owns that change.

### Phase 2 - progressive (one record per Pillars subtree)

1. Order: Philosophy/Model first, because the harness cites it most and the work, capture and coordination cards already in the graph attach there; then Philosophy's other subtrees, Aesthetics, Engineering Practice, and Technē last, under the [Techne Programme Focus](<../../../../Admin/Governance/Policies/Techne Programme Focus.md>).
2. Each record upgrades its subtree's pages: front matter, a kebab-case name, and a split wherever a page holds more than one idea. Each old page becomes a pointer stub (front matter `replaced_by`, one line naming the node), so the 29 harness citations and every inbound link still resolve.
3. The same record repoints the home page entry, and sends a line to the harness's `messages.md` listing the changed paths so the harness repoints its own citations.

### Phase 3 - complete (one record)

When every Pillars page is a stub and no harness file cites one, a final record deletes `Pillars/` and its stubs, and Structure drops the Pillars rows. The later lower-case rename of `Admin`, `Calendar`, `Streams` and `Resources` is separate work (query RENAME-WHEN).

## Rules the evidence settles

- **Resources stays outside `knowledge/` here.** `AGENTS.md` strictly enforces the internal-versus-reference boundary, and the proposal leaves Resources unchanged. So `knowledge/` replaces Pillars alone, the primary home path is enough inside it, and no internal/reference split is needed within the graph: everything in it is internal. This answers the proposal's question 2 and the Knowledge Islands Principal half of question 1. Whether another territory may bring its Resources in is query RESOURCES-IN.
- **Admin and Streams link into `knowledge/` with plain relative links.** Structure already says Streams notes are status trackers that link to knowledge rather than hold it, and Admin is governance, not knowledge. Neither needs nodes of its own; a node may link back to an Admin or Streams note as a legacy link. This answers question 4.
- **Links from the graph into Pillars and Resources are legacy links; nothing old must link back.** As the proposal sets out. A link from a pulled node into a Resources note uses the predicate the card already chose, typically `skos:related`.
- **A pull leaves a pointer.** The harness's citations make a bare move unsafe; the pointer stub is required, not optional.
- **The node minimum follows the cards already written.** Front matter `id` (kebab-case, unique within the island and equal to the file stem), `title`, `type`, `status`, and `links` as a map of local alias to `predicate`; one idea per node, judged by the [contextual atomicity](</Users/krisbrown/kis/personal/assistant/curated/knowledge-islands/ki-principal/Pillars/knowledge-graph/contextual-atomicity.md>) card rather than a word count. The primary home is the path, so the `pillar` field the cards carry is dropped. The predicate set is the six in use, with any new predicate added by the standard, not by a card. This answers question 3 for a first version; the review stage may challenge it.

## Queries for Kris

Each is in Context/Query/Options form in the run report and in `discussions.md` once State of play receives it.

- **INDEX-NAME** - `_index.md` or `index.md` for every folder note, in `knowledge/` and in work-package focus folders alike. Recommended: `_index.md` for both, with the coordination baseline updated to match (medium confidence; the work-package change is a small rollout, but `_emerging/index.md` and its peers must be renamed).
- **ATTACH-HOW** - how a node is declared an attachment point and what it promises. Recommended: front matter `attachment: true` on the node, listed under "Attachment points" in `knowledge/_index.md` and checked by KIG to agree; the promise is a stable `id` and path, with deprecation by pointer rather than removal (medium confidence). A shadow node carries `shadows:` with the canonical path and the revision it was read at, and `checked:` with a date.
- **ATTACH-SET** - which nodes are the first attachment points. Recommended: the capture funnel, the knowledge graph, and the work process once pulled (medium confidence).
- **RESOURCES-IN** - whether another territory may bring Resources into its graph. Recommended: no for now; every territory keeps Resources outside until one shows a need (medium confidence).
- **RENAME-WHEN** - when the older areas move to lower case. Recommended: after phase 3, as one separate record per repository, because the harness and every link would move twice otherwise (high confidence).
- **PACE** - first milestone. Recommended: phases 0 and 1 in one approval this week, the graph standard in the harness in parallel, with phase 2 records taken one subtree at a time from then on (high confidence; this is what "quickly" asks for with the gate intact).

## Next steps

1. Two blind reviews of this plan, under the `ki-work-design` method.
2. Merged report with the queries above to Kris.
3. On Kris's answers: the decision, the Enactment record and the first slice, as one run.
