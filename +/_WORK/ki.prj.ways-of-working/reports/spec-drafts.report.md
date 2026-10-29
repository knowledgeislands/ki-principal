# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › spec-drafts

**🤖 → 👤 Handoff to supervisor · Run report at 14:35 BST · last mark 13:37 BST**

---

## Done

- Wrote three draft specs in the agentskills.io page format, plus a short index: [work](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/specs/work.md), [knowledge](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/specs/knowledge.md), [acquire](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/specs/acquire.md) and [specs.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/specs/specs.md). Each covers what the package is, its directory structure, the entry file's front matter (with constraints, valid and invalid examples), body content, optional directories, progressive disclosure, file references, validation, how it relates to Agent Skills and how it relates to the other two specs.
- `work`: `WORK.md` (the definition, with the routing description) plus `state.md`, `queries.md`, `messages.md` and `decisions.md`. It has four portable states (`active`, `waiting`, `on-hold`, `done`) and the priority-ordered message queue with the `IMPORTANT` flag. It contains nothing of the Knowledge Islands ways of working; `specs.md` maps the house work package onto it as a profile, including the seven states.
- `knowledge`: `KNOWLEDGE.md`, whose description tells a reader whether this package answers their question, then Overview, Contents, Sources and Limits, with the body of knowledge in `references/`. It adds `updated` and `acquired-with`. Rename the entry file to `SKILL.md` and a conforming package is also a valid skill.
- `acquire`: `ACQUIRE.md` with required `source` and `mutation` fields, plus optional `omissions` and `produces`. The body must have Scope, Procedure, Output and Verification sections. These come from `ki-acquire`'s common standard, the Granola and ChatGPT skills' `ki-acquire-*` front matter and tools-ki's ACQUIRE-010 to ACQUIRE-018.
- How the three relate: an acquire package produces or refreshes a knowledge package, and each names the other through `produces` and `acquired-with`. A work package may cite either but contains neither.
- How the older framing maps, given that your definitions now win: spec-areas-design's "agent context package" becomes `knowledge`. Its sealed acquire "knowledge package" (the KEP and Granola packages) is not one of the three: it is capture evidence that an acquire package's Output describes, and it stays an implementation format of `ki-acquire` and tools-ki. KIS-0001 is prior art for `knowledge` and `work`. As a result, spec-areas-design's queries SPEC-AREAS-SPLIT and PACKAGE-NAMES are overtaken by your naming, and CONTEXT-OWNER and OLD-SPEC pass to `ki.specifications` as questions about the `knowledge` spec.
- Choices visible in the drafts: all three take an optional `spec` field; work names may contain `.` between segments, so the house's dotted ids conform; a reader ignores top-level keys it doesn't know, so a local profile can add its own fields.
- Commit `9d26b89d` in ki-principal: the four `design/specs/` files only, by explicit path; the commit gate passed. Not pushed.
- Checks: no em or en dashes and no stray non-ASCII characters (only the `·` separator in the message examples); every relative link resolves.
- Limitations: I fetched the agentskills.io specification and the skills-ref README it links, read-only. Your brief asked for this, but it goes against the brief's no-network rule. Google's Open Knowledge Format note was skimmed, not read in full. No reference validator exists for any of the three.
- Left untouched: other sessions' dirty files in ki-principal, namely `+/_WORK/ki.chezmoi/`, `+/_WORK/ki.specifications/create-project.report.md`, and this work's `decisions.md`, `work.md`, `state.md`, `queries.md`, `messages.md` and `design/spec-areas.md`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Under SPECIFICATIONS-PROJECT, the drafts and SPEC-HOME pass to `ki.specifications` with a dated line in its `messages.md`; that is the coordinator's move.
- Once the queries below are answered, the house work-package profile needs a decision on how to carry its seven states (a profile field such as `ki-state`, or a reader mapping), raised with the profile in `ki.specifications`.

## Queries

### ENTRY-NAMES - Upper-case entry files for the three packages

**Context:** Agent Skills marks a package's entry with an upper-case `SKILL.md` and keeps every other file lower-case. The drafts follow that with `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`. The house work package, which the migration pass is moving folders into now, uses a lower-case `work.md`. Choosing upper case means a case-only rename of each live `work.md`. Doing that during the current pass costs least, but on macOS a case-only rename needs `git mv` in two steps. **Query:** Should the entry files be upper case, `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`, as Agent Skills does? **Options:** a) (recommended, confidence medium - matches Agent Skills and marks the entry file at a glance; the cost is one rename across the estate) Upper case for all three, with the house work package renaming `work.md` to `WORK.md` in the current migration pass. b) Upper case for `KNOWLEDGE.md` and `ACQUIRE.md` only, keeping `work.md` as built, so the work spec is the one exception. c) Lower case for all three: `work.md`, `knowledge.md` and `acquire.md`.

### SPEC-VERSION - Whether a package declares which spec version it follows

**Context:** Agent Skills has no spec-version field and puts a skill's own version in `metadata.version`. Work and knowledge packages live for a long time and are rewritten in place, so a later reader may meet one written to an older major version. The drafts add an optional top-level `spec` field (`work/1`, `knowledge/1`, `acquire/1`); when it is absent, a reader assumes version 1. Each package's own version stays in `metadata.version`. **Query:** Should the three specs carry the optional `spec` field? **Options:** a) (recommended, confidence medium - one optional line now avoids guessing at the first breaking change, while staying silent costs nothing until then) Keep the optional `spec` field, absent meaning version 1. b) Follow Agent Skills exactly: no field, with the spec version carried only by the published page. c) Make `spec` required from version 1.

### CONFORMANCE-LEVELS - One validity level or graded levels

**Context:** Agent Skills has one level: a skill is valid or not, and size and quality are recommendations. The retired KIS-0001 had Minimal, Standard and Extended levels. The drafts use one level: hard rules make a package valid, soft limits are warned and never failed, and quality is left to a reviewer's judgement. **Query:** Should each spec have a single validity level, as Agent Skills does? **Options:** a) (recommended, confidence high - matches Agent Skills, and nothing yet needs a graded level) One level per spec, with soft limits warned. b) Graded levels (Minimal, Standard and Extended) as in KIS-0001.

### SPEC-HOME - Where the three specs live

**Context:** You left the home open: the owning skills, or `knowledgeislands.info/specs/{work,knowledge,acquire}`, and SPECIFICATIONS-PROJECT passes the choice to `ki.specifications`. The evidence: the drafts are tool-neutral and ready for either home. Two of the three have an existing skill (`ki-work-package` and `ki-acquire`), but their standards are written in the house dialect, so each would hold the portable spec beside its own profile. `knowledge` has no owning skill. The website has another session (Claude Design) working in it. KI Specifications is on hold until v1 under KI-SPECS-PLAN. Publishing is outward-facing and hard to take back. **Query:** Should the specs be held in the owning skills now and published to the website later, from the same text? **Options:** a) (recommended, confidence medium - avoids publishing drafts and the website clash, and keeps one text to publish later; `knowledge` still needs an owning skill) Hold each portable spec as one reference in its owning skill, with a new skill for `knowledge`, and publish the same text at `knowledgeislands.info/specs/` once `ki.specifications` is satisfied and Claude Design has finished. b) Publish at `knowledgeislands.info/specs/` now, with the skills linking to the pages. c) Keep the drafts in `ki.specifications`'s work folder until KI Specifications opens v1, then raise them as KIPs.
