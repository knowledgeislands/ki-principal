# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-deliver-mod-008

**🤖 → 👤 Handoff to supervisor · Run report at 22:28 BST · last mark 09:27 BST**

---

## Done

- [KI-PRINCIPAL-MOD-008](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-008-whole-philosophy-coherence-review.md) is at awaiting review. The record confirms the WORKABLE classification. Kris's 22:03 BST burndown authority stood in for the ready approval, and the record says so. It now holds a referenced Findings table, the plan sections, Documentation impact, the Review packet, `size: l` and the Governance footer.
- Ten consistency findings are fixed across 15 Philosophy notes, with each change traced to its finding:
  - F1: the "teritories" typo.
  - F2: the retired "Knowledge Capitals" name for Realisation.
  - F3: "satellite" islands, against SDR-KI-PRINCIPAL-005.
  - F4: the reading-order index now includes the Acquisition and Work Processes, four Tools, and Tending as adoptable.
  - F5: "chapters" now reads "acts".
  - F6: the notes now speak of four processes, not two, and the Citizen link points to Jurisdiction.
  - F7: the archipelago used as a governance unit now reads territory.
  - F8: "Knowledge Capital" as a folder now reads the `Admin/` zone.
  - F9: "judgment" now reads "judgement".
  - F10: the note-type list was missing activity notes.
- No change alters meaning; every contradiction of laid-down philosophy is raised as a query below, under the 2026-10-11 guard.
- The website drift is routed as one non-blocking line, WEBSITE-PHILOSOPHY-DRIFT, in [State of play messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md). It covers four points: the archipelago drawn as a separate grouping with "Satellites", the zone count, the harbour and lighthouse icons, and two of four processes shown.
- Commits on local main, not pushed: `001544e9` `docs(pillars): align the Philosophy for KI-PRINCIPAL-MOD-008` and `21901509` `docs(roadmap): move KI-PRINCIPAL-MOD-008 to awaiting review`. Main is fast-forwarded after rebasing over two commits from other sessions. The worktree and branch have been removed.
- Check results:
  - Links: no broken internal link in `Pillars/Philosophy` apart from the unchanged template placeholders and the Format examples.
  - Retired vocabulary: none left outside image alt text and the query lines.
  - Dashes: no em or en dash in the 17 touched files.
  - Audits: `ki repo audit --skill` for `ki-work`, `ki-repo-kb-streams`, `ki-work-roadmap` and `ki-repo-kb` exit 0 with no new finding, and STREAM-12 on this record has cleared.
  - Commit gate: passed. The worktree had no `node_modules`, so I linked the primary checkout's identical install for the commit, without a network install. The link has been removed.
- Limitation: these queries have not been blind-reviewed, because this run may not launch agents. Each confidence below is the run's own.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Eighteen Philosophy notes still carry `status: draft - April 2026`. This is left for the Status Review activity or for acceptance.
- The portable Model Enactment Process note repeats island-local specifics that the `Admin/` note already holds.
- The Governance concept's examples ("Linear sync") are dated.
- SDR-KI-PRINCIPAL-002 still says "Harbour". It is historical under GDR-KI-PRINCIPAL-010.
- The two commits are unpushed on local main, stacked with other sessions' commits.

## Queries

### ACCEPT - accept KI-PRINCIPAL-MOD-008

**Context:** The review is delivered with ten fixes, eight open queries and a website handoff. The record's Verify evidence is complete. Accepting closes the review. The queries below can be decided before or after acceptance, and their follow-up belongs to the owning work.

**Query:** Accept [KI-PRINCIPAL-MOD-008](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-008-whole-philosophy-coherence-review.md) as done?

**Options:**
a) (recommended, confidence medium - the review is complete and the queries are separable decisions) Accept now, and carry the queries as decisions for the owning work.
b) Hold acceptance until the queries are answered and any follow-up wording is made under this record.

### CALENDAR-LIBRARY - is Calendar part of the Library?

**Context:** Structure, The Home of Knowledge and the website put Calendar inside the Library. SDR-KI-PRINCIPAL-002 defines the Library as Pillars plus Resources, with Calendar beside it. Calendar entries are exempt from the Enactment record, but Structure says "Nothing enters the Library except through the governance process".

**Query:** Should Calendar sit inside the Library?

**Options:**
a) (recommended, confidence low - two notes and the website agree, but SDR-002 is the decision of record) Keep Calendar in the Library, state that it is appended by note-type convention rather than by proposal, and amend SDR-KI-PRINCIPAL-002's wording.
b) Follow SDR-KI-PRINCIPAL-002, and move Calendar out of the Library in Structure, The Home of Knowledge and the website.

### ENACTMENT-ADMIN - does the portable gate cover Admin?

**Context:** Five places in the portable model say nothing enters Pillars or Resources without enactment, and none of them names Admin: Governance, Jurisdiction, the Model Enactment Process, Processes and the Great Library. SDR-KI-PRINCIPAL-002 and the island's own Enactment Process include `Admin/`.

**Query:** Should the portable gate statements name `Admin/` as well?

**Options:**
a) (recommended, confidence medium - this matches the island's practice and SDR-002) Add `Admin/` to the portable gate statements.
b) Keep the portable model to Pillars and Resources and treat Admin gating as an island choice.

### CAPITAL-OF-CAPITALS - KIP as "Knowledge Capital of Knowledge Capitals"

**Context:** Knowledge Islands.md lines 20 and 135 call Knowledge Islands Principal "the Knowledge Capital of Knowledge Capitals". Territories and Archipelagos says its authorship gives it "no jurisdiction over another territory", and the Great Library is "reference, not jurisdiction".

**Query:** Should the phrase be reworded so that it does not imply a role over other territories' Capitals?

**Options:**
a) (recommended, confidence medium - it removes a contradiction with SDR-KI-PRINCIPAL-005) Reword it as "the canonical home of the model, without jurisdiction over other territories", and keep the "legendary utopia" image.
b) Keep the phrase as rhetoric and add a qualifying sentence.

### TAGS - keep subject tags beside note_type?

**Context:** Kris asked on 2026-10-12 whether subject tags are still needed. The `card/*` and `calendar/*` tags repeat what `note_type` already says, while the `topic/*` tags still help search across folders.

**Query:** Which tag families should the model keep?

**Options:**
a) (recommended, confidence low - retiring tags touches many notes and tools) Keep `topic/*`, `date/*` and `source/*`, and retire the `card/*` and `calendar/*` type tags in favour of `note_type`.
b) Keep the full taxonomy unchanged.
c) Retire all tags in favour of `note_type`, folders and links.

### EMERGING - what to do with the Emerging Concepts

**Context:** Four notes sit in Emerging Concepts: Realm Model, Avatar Roles and Oversight, Known World and Fictional Lineage. ADR-KI-PRINCIPAL-005 settles one persona with one name across working contexts. The Techne Programme Focus says that knowledge consolidation alone does not accept candidates.

**Query:** Which Emerging Concepts should move to the settled Philosophy?

**Options:**
a) (recommended, confidence medium - this respects the Focus and ADR-005) Leave Realm Model, Avatar Roles and Oversight and Known World open, and keep one Avatar name under ADR-KI-PRINCIPAL-005. Adopt Fictional Lineage into Background beside Influences Along the Way.
b) Leave all four open.

### CANDIDATE-PRINCIPLES - adopt the two candidate engineering principles?

**Context:** Engineering Practice Principles holds two candidates: a neutrality extension to Provider-Neutral Execution, and FOSS-First and Inspectable. Both are consistent with the existing principles. The Techne Programme Focus says that consolidation alone does not accept candidates.

**Query:** Should the two candidate principles be adopted?

**Options:**
a) (recommended, confidence medium - this follows the Focus as written) Leave both as candidates until the owner takes them up.
b) Adopt both now.

### STRUCTURE-TODOS - settle the Port and Routes and Customs to-dos

**Context:** Structure's Port to-do is now largely settled by GDR-KI-PRINCIPAL-010 and the `+`/`-` rules. Routes and Customs is still open, though Territories and Archipelagos has a route paragraph and `ki-trades` governs exchange.

**Query:** Should the Port to-do become a settled section?

**Options:**
a) (recommended, confidence medium - the decision already exists) Make Port a settled section that cites GDR-KI-PRINCIPAL-010. Keep the Routes and Customs to-do, with pointers to the route paragraph and to `ki-trades`.
b) Leave both to-dos as they are.

### LAYER-PATHS - content-layer paths that do not exist

**Context:** Authoring Guidelines lines 31, 32 and 84 give content-layer paths under `/Pillars/Knowledge Capital/Model/...` that do not exist. Configuration names the Charter and `Admin/Operations/Activities/` as the homes.

**Query:** Should the paths be rewritten to the declared homes?

**Options:**
a) (recommended, confidence medium - the current paths are unreachable) Rewrite them to the Charter and `Admin/Operations/Activities/`.
b) Remove the layered-path scheme and describe the layers in words.

### 🤖 → 👤 Handoff to supervisor · since 22:28 BST

👤 9 with you · 📥 1 to accept

- [with you] ACCEPT KI-PRINCIPAL-MOD-008 · owner · since 22:28
- [with you] 8 coherence queries · owner · since 22:28
- [committed] ki-principal main 001544e9, 21901509
- [unpushed] ki-principal main
