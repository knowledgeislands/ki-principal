# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › spec-areas-design

**🤖 → 👤 Handoff to supervisor · Run report at 14:27 BST · last mark 13:37 BST**

---

## Done

- Design note written: [design/spec-areas.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/spec-areas.md). It covers each area's description, owner, spec file, outline (purpose, layout, required files and front matter, conformance, versioning) and later KIS path, gives a one-or-two verdict with evidence, sets out the relations to agentskills.io and the work package, and proposes a run sequence. It is uncommitted, as the brief required.
- **Knowledge package (acquire output):** the description is current but scattered across tools-ki's acquisition spec, the ChatGPT and Granola code, `ki-acquire`'s standards and the Acquisition Process note. The two built sources disagree on shape: ChatGPT emits a KEP and Granola a `meeting.md` package. Proposed owner `ki-acquire`, spec at `references/standards-knowledge-package.md`, with the retired KIS-0002 layout as the base. Later it becomes a KIS that supersedes KIS-0002.
- **Work package:** already specified in `ki-work-package` `references/standards-work-package.md`. That file is being rewritten now, and I did not touch it. The spec run adds only a conformance statement and a format version, chained after work-package-standard and no-alias-sweep.
- **Agent context package:** nowhere specified today. The pieces are acquire's `context/<territory>/README.md` exports, the KB-ACQUIRE-005 seeds, the 15 October Agent Knowledge Model capture and its Knowledge Manifest, and the retired KIS-0001. Google's Open Knowledge Format is an external reference. Proposed: a new skill with the agentskills.io shape applied to knowledge.
- **Verdict: two areas.** The knowledge package is sealed, hash-identified evidence going into an island. The context package is regenerated, progressively read knowledge going out to agents. They share a provenance vocabulary, which the context spec should cite from the knowledge spec.
- Limitation: one naming clash found. The retired KIS-0001 used "Knowledge Package" for what is here the context package, and tools-ki's ACQUIRE-001 calls the KEP a "Knowledge Exchange Package" and cites the deleted KIS-0002.
- Checks: read-only throughout apart from the one note; no commits, pushes or network calls. The note uses ASCII hyphens only. The other uncommitted changes in ki-principal (`decisions.md`, `.ki.toml`) were left untouched.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- After the knowledge-package spec lands, tools-ki needs a handoff to fix ACQUIRE-001's wording and its citation of KIS-0002.
- When KI Specifications opens v1, a handoff for the three KIPs is needed; KI-SPECS-PLAN holds this until then.
- The blind review of the medium and low queries below is already authorised and should run before the knowledge and context spec runs launch.

## Queries

### SPEC-AREAS-SPLIT - Treat acquire's package and the agent context package as two areas

**Context:** Acquire's package is sealed, identified by its content hash and read whole, carrying a source into an island. The context package is regenerated, identified by name and date and read progressively by agents, carrying island knowledge out. They were already two separate specs in July (KIS-0002 and KIS-0001). **Query:** Should these be specified as two areas with a shared provenance vocabulary, or as one? **Options:** a) (recommended, confidence high - direction, mutability, reader and lineage all differ) Two areas, with the context spec citing the knowledge spec's provenance fields. b) One package spec with two profiles, evidence and context.

### CONTEXT-OWNER - Which skill owns the agent context package spec

**Context:** No skill owns it today. `ki-repo-kb` owns the island's internal method and is already large. `ki-acquire` owns evidence coming in, which is the opposite direction. Acquire only hosts the exports because external agents read them there. **Query:** Which skill should own the agent context package spec? **Options:** a) (recommended, confidence medium - one unit of comprehension per skill, but adds a skill) A new harness skill, `ki-context-package`, beside `ki-repo-kb`. b) A new standards file inside `ki-repo-kb`. c) A new standards file inside `ki-acquire`.

### PACKAGE-NAMES - Names for the two knowledge-bearing packages

**Context:** Your request calls acquire's output the "knowledge package". The retired KIS-0001 used "Knowledge Package" for something closer to the context package. The code says KEP, "Knowledge Export Package", and tools-ki's spec says "Knowledge Exchange Package". **Query:** What should the acquire output and the agent context package be called? **Options:** a) (recommended, confidence medium - keeps your wording and drops the Export/Exchange drift) "Knowledge package" for acquire's output, keeping `kep` only as the manifest's file name for compatibility, and "context package" for the agent one. b) "Acquisition package" for acquire's output, leaving "knowledge package" unused to avoid the KIS-0001 clash. c) Keep "Knowledge Export Package (KEP)" for acquire's output and "knowledge package" for the agent one, as in July.

### OLD-SPEC - Which older agent knowledge spec you meant

**Context:** The oldest agent-knowledge spec found is the retired KIS-0001 Knowledge Package (July 2026), with its informative schema and examples still in KI Specifications. Other candidates are Google's Open Knowledge Format (June 2026, external) and acquire's `context/` exports with the 15 October Agent Knowledge Model capture. The note assumes KIS-0001 is prior art, not the base. **Query:** Is KIS-0001 the older spec you meant, and should it be prior art or the base for the context package spec? **Options:** a) (recommended, confidence low - inferred, not stated) KIS-0001 is the one; use it as prior art, keeping its digest and terminology fields and leaving its task and handover fields to the work package. b) KIS-0001 is the one; use it as the base and trim it. c) You meant something else; name it and the spec run reads it first.

### SPEC-SEQUENCE - Order of the three spec runs

**Context:** The knowledge-package spec writes only `ki-acquire` files and can start once the names are settled. The context-package spec needs the owner, name and old-spec answers. The work-package spec writes the skill that work-package-standard and no-alias-sweep are changing now. **Query:** Should the spec runs go in this order: knowledge package, then context package, with the work package chained after work-package-standard and no-alias-sweep? **Options:** a) (recommended, confidence medium - avoids file overlap and lets the context spec cite shared fields) Blind review first; then spec-knowledge-package in parallel with the work-package chain; then spec-context-package after it. b) Run the knowledge and context specs in parallel after the blind review, with the work-package spec still chained.
