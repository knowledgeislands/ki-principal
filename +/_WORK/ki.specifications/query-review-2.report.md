# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › query-review-2

**🤖 → 👤 Handoff to supervisor · Run report at 23:41 BST · last mark 19:00 BST**

---

## Done

Four queries reviewed against the local drafts, plan, house contracts and Agent Skills reference; no repository changes or commits.

## In Progress

Nothing is running. Live specification and validator behaviour remain unverified: the run forbids network calls, and no local `skills-ref` executable or validator source was found in the searched locations.

## Queries

### WORK-PROFILE - House package conformance

**Context:** Checked the [work draft](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md), its profile table and the harness work-package standard; the documented readers and tools-ki source depend on `work.md`. The house rules are present in the portable draft, but the profile table's claim that the house already conforms is false: field and state mappings need an explicit adapter or exported conforming view; the 33-package count was not independently recounted.

**Query:** Should the house package stay a mapped profile of `work`, or change to conform to it?

**Options:**

a) (recommended, confidence high - separates a portable contract from house practice without requiring an unrelated estate migration) "Keep the house as a mapped profile; move house rules out of the spec into the profile."

b) Make the house conform, with an estate-wide rename and reader changes.

c) Bend the spec to the house's `id`, `since`, seven states and `work.md`.

### KNOWLEDGE-SKILL - Owning skill

**Context:** Checked the [knowledge draft](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md) and the skill boundaries: `ki-repo-kb` governs an island's zones, `ki-authoring` writing conventions, and `ki-skills` Agent Skills quality. None owns this standalone curated-package contract; the new Project note already names a new skill, although its name and bounded remit still need settling.

**Query:** Where should the `knowledge` spec be homed?

**Options:**

a) (recommended, confidence high - gives the distinct package contract and its future validation a clear owner without broadening neighbouring skills) "A new governance skill, such as `ki-knowledge-package`, owning the spec and later its rubric."

b) `ki-repo-kb`, as a reference beside the island method.

c) `ki-skills`, beside the Agent Skills reference.

### MOVE-GATE - Project finish

**Context:** Checked the [plan](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/plan.md), Project outcome and KI Specifications' README: restart and normative adoption are explicitly outside this Project's control. The handoff should be blocked by the receiver's restart, rather than block publication or this Project's owner-approved closure; the outcome must make that boundary explicit.

**Query:** Should the Project close at publication with the move handed off, or stay open until KI Specifications accepts the specs?

**Options:**

a) (recommended, confidence high - publication is a verifiable deliverable while an undated receiver restart has separate ownership) "Finish at publication, with a blocking handoff record in KI Specifications' roadmap."

b) Stay open, on hold after publication, until KI Specifications restarts and accepts them.

### SPEC-LOCATION - Optional specification version

**Context:** Checked all three front-matter tables and the [local Agent Skills reference](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-skills/references/standards-agent-skills.md), whose source review is dated 26 September: it specifies string-to-string `metadata`, but does not establish rejection of unknown top-level keys. Moving `spec` alone cannot repair compatibility: all added scalar fields need the same treatment with string values, `omissions` is the draft's list (`produces` is scalar), and actual skill validation still needs `SKILL.md`.

**Query:** Should the optional `spec` field sit at the top level or in `metadata.spec`?

**Options:**

a) (recommended, confidence medium - the documented extension map supports scalar metadata, but current upstream validator behaviour was not directly checked) "`metadata.spec`, with the other single-value fields, deciding list fields after a live check."

b) Top level, dropping the "valid skill" claim.

### 🤖 → 👤 Handoff to supervisor · since 23:41 BST

👤 4 with you

- [with you] WORK-PROFILE · supervisor · since 23:41 BST
- [with you] KNOWLEDGE-SKILL · supervisor · since 23:41 BST
- [with you] MOVE-GATE · supervisor · since 23:41 BST
- [with you] SPEC-LOCATION · supervisor · since 23:41 BST
