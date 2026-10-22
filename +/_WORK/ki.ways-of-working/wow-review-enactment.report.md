# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-enactment

**🤖 → 👤 Handoff to supervisor · Run report at 23:20 BST · last mark 23:05 BST**

---

## Done

- Blind review of ENACTMENT-ADMIN finished. I changed no files and made no commits. Verdict: the proposal is unsound as framed. Its premise contradicts the record that actually establishes the gate.
- **The premise is wrong, and the proposal supersedes the wrong record.** The gate is set by [SDR-KI-PRINCIPAL-004](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-004-the-enactment-process.md), not by SDR-KI-PRINCIPAL-002. The Decision section of SDR-KI-PRINCIPAL-004 reads "Nothing reaches Pillars or Resources as settled knowledge except through council ratification". Admin was added later, under Consequences. So the gate was built to protect Pillars and Resources, and Admin is the add-on. [SDR-KI-PRINCIPAL-002](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-002-the-home-of-knowledge.md) only restates the gate in one sentence.
- **Records that depend on the current gate.** [GDR-KI-PRINCIPAL-012](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-012-official-not-canon.md) defines "canonical knowledge" as knowledge that has passed the Enactment Process into Pillars or Resources; under an Admin-only gate that definition would describe nothing. [SDR-KI-PRINCIPAL-007](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/SDR-KI-PRINCIPAL-007-the-great-library-of-arcadia.md) and the Great Library note say the Library grows "only through governance".
- **What Pillars and Resources would lose:**
  - approval before a change is made, at the `ready` step;
  - a recorded starting point to compare the change against;
  - a separate review before the change is accepted;
  - kept `done` records as evidence of each change;
  - the internal half of the Contribution Process, which protects the portable model in `Pillars/Philosophy` that every island adopts;
  - a gate on Techné's canonical [Engineering Practice](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Engineering Practice/Engineering Practice.md>).
- **What would still cover them, only partly:**
  - Git keeps a history of changes but records no approval.
  - The pre-commit and CI audit checks mechanical conformance only. [Conformance](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Conformance.md) itself says judgement changes still need the Enactment Process.
  - Decision records cover the reasons for decisions, not note prose.
  - The rule in AGENTS.md, "Confirm with the user before writing changes", holds in an interactive session. It gives little protection against a background agent acting on the authority in its brief.
  - Nothing reviews the content of a change.
- **Assumptions in ki-principal:**
  - AGENTS.md, "Changing canonical content".
  - The island's [Enactment Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Processes/Enactment Process.md>): Stores, "When a record is needed", and the governance footer (used in 2 of the 6 roadmap records).
  - `Admin/Operations/Processes/Processes.md`, the Glossary entries for Enactment and Contribution, and Conformance.
  - About 14 notes in the portable model: the model Enactment Process note, Governance, Jurisdiction, Processes, How Change Happens, Model, Knowledge Islands, Structure, Great Library, Arcadia, Council, Charter (realisation), Configuration, Contribution Process and Acquisition Process.
- **Assumptions in ki-agentic-harness:**
  - The `ki-repo-kb-streams` skill and its `standards-enactment-process.md`.
  - The `ki-repo-kb-principal` skill and its `standards-principal.md`.
  - The `ki-repo-kb` skill's line on the canonical-zone gate, and its save, update and improve modes. These would keep sending Pillars changes to a proposal, so the island and the shared skills would disagree.
  - The eval in `evals/scenarios/ki-repo-kb-streams.ts`, which requires the answer to name Admin, Pillars and Resources and to send a Pillars change through a proposal.
  - The streams-curator and KB-curator subagents.
  - These skills are shared by every Knowledge Base in the territory: 7 other principal islands' AGENTS.md files mention the gate.
- **Mechanical checks:** no hook in either repository enforces the gate. The principal anchor audit (PRINCIPAL-2) and the streams gate audit (GATE-1) would still pass with an Admin-only anchor, because they check only that the anchor exists.
- **A replacement decision record is needed.** Narrowing the gate reverses the Decision of SDR-KI-PRINCIPAL-004. That needs a new SDR superseding it, plus amendments to SDR-KI-PRINCIPAL-002 and GDR-KI-PRINCIPAL-012. Superseding SDR-KI-PRINCIPAL-002 alone would leave SDR-KI-PRINCIPAL-004 standing and contradicting the new gate.
- **Smallest safe change set if adopted, in this order:**
  1. Write the new SDR and its amendments under one record.
  2. Edit AGENTS.md and the island's Enactment Process.
  3. Edit the portable-model notes. These are in Pillars, so under today's gate they need that same record or an owner instruction.
  4. Send the harness changes as a line in the harness's `messages.md`, not as a record. They are best made as a per-base setting for which zones are gated, with the portable default unchanged, so other islands are unaffected.
  5. Leave existing roadmap footers as historical wording.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Not checked: what friction prompted the proposal. My brief did not state it, and the masking rule kept me from reading the work package's queries, decisions and reports.

## Queries

### ENACTMENT-ADMIN - Narrow the Enactment gate to Admin only

**Context:** The gate on Admin, Pillars and Resources is set by SDR-KI-PRINCIPAL-004. Its Decision text gates Pillars and Resources; Admin appears only in its Consequences. GDR-KI-PRINCIPAL-012 defines "canonical knowledge" as what passed that gate into Pillars or Resources. An explicit owner instruction for a bounded change already stands in for a record. Ungating Pillars removes approval-before-change, review and retained evidence for the portable model and Engineering Practice. Only Git history, the mechanical audits and the interactive "confirm with the user" rule would remain. The change touches about 20 notes in ki-principal and 6 harness skills, an eval and 2 subagents, all shared by every Knowledge Base. It needs a new SDR superseding SDR-KI-PRINCIPAL-004, not SDR-KI-PRINCIPAL-002.

**Query:** Should the Enactment gate be narrowed to Admin only?

**Options:**

a) (recommended, confidence medium - the premise conflicts with SDR-KI-PRINCIPAL-004 and GDR-KI-PRINCIPAL-012, verified directly, but the friction it targets was outside this review) Keep the gate on all three zones. Relieve any friction by widening the owner-instruction stand-in in the island's Enactment Process local specifics, for example letting one approved scope cover a batch of related Pillars and Resources edits. This needs no SDR and no harness change.

b) Use a tiered gate. Admin, the portable model in `Pillars/Philosophy` and Engineering Practice stay gated. Other Pillars and Resources notes need only the owner's confirmation, without a record. This needs a new SDR superseding SDR-KI-PRINCIPAL-004 and a per-base gated-zones setting in the harness, sent as a line in the harness's `messages.md`.

c) Adopt the proposal with its record corrected. Write a new SDR superseding SDR-KI-PRINCIPAL-004 and amending SDR-KI-PRINCIPAL-002 and GDR-KI-PRINCIPAL-012. Rewrite AGENTS.md, the island's Enactment Process and the portable-model notes under one record. Send the change to the shared skills, eval and subagents as a line in the harness's `messages.md`.

### 🤖 → 👤 Handoff to supervisor · since 23:20 BST

👤 1 with you

- [with you] ENACTMENT-ADMIN · owner · since 23:20
