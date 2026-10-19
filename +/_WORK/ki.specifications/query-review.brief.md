# Brief - specifications/query-review

You are a blind reviewer for four open owner queries in the Knowledge Islands work `ki.specifications` (KI > Model > Specifications). For each query below you get its Context, Query and options with no recommendation; option order means nothing. Check what you can directly, read only and change nothing:

- `Streams/Projects/specifications.md`, `Streams/Projects/Projects.md` and `Streams/Themes/model.md` in this checkout.
- The drafts in `+/_WORK/ki.specifications/design/specs/` (`specs.md`, `work.md`, `knowledge.md`, `acquire.md`) and the stocktake `+/_WORK/ki.specifications/design/spec-areas.md`.
- The owner's words in `+/_WORK/ki.specifications/work.md` and the SPEC-AREAS and SPECIFICATIONS-PROJECT entries of `+/_WORK/ki.ways-of-working/decisions.md`.
- The skills `ki-work-package` and `ki-acquire` under `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/`, and <https://agentskills.io/specification>.

Do not edit, commit, push or publish anything.

## Queries

### PROJECT-NAME - Which note this Project takes

**Context:** `Streams/Projects/specifications.md` already describes a different Project, outcome "KI Specifications presents one consistent account of its authority and retained process, and the transferred KBEP and KBIP protocols each have a recorded disposition", under Model, `lifecycle: paused` since 2026-10-07 with the website, no open records, registered in `Projects.md`. This Project owns three portable specs (`work`, `knowledge`, `acquire`), their home, publication and their later move into KI Specifications. The work id `ki.specifications` requires the Project slug `specifications`. **Query:** Should this Project take over the existing `specifications` note, or should one of the two Projects take a new name? **Options:**

- Fold the paused Project into this one: new outcome covering the three specs, home, publication and the move into KI Specifications, carrying the repository review and KBEP/KBIP dispositions as a later step; rewrite the registry and theme entries; work id unchanged.
- Keep the paused Project; give this one a new slug such as `portable-specifications`, renaming the work folder and id.
- Rename the paused Project, such as `ki-specifications-review`, with its registry entries and links; this Project takes `specifications`.

### SPEC-HOME - Where the three specifications live

**Context:** The owner gave two homes: the owning skills, or `knowledgeislands.info/specs/{work,knowledge,acquire}` (an opener wrote `/specifications/{name}`). Earlier that day the owner said "I want to get those spec'd within a skill that owns them for now, then we formalise out of them later". The drafts are tool-neutral. `ki-work-package` and `ki-acquire` exist with house-dialect standards; `knowledge` has no owning skill. Another session works in the website; the website Project is paused; KI Specifications is on hold until its v1; publishing is outward-facing and hard to take back. **Query:** Where should the three specs be held now, and when and where published? **Options:**

- Hold each spec as one reference in its owning skill (a new skill for `knowledge`), in agentskills.io page format, and publish the same text on the website later in this Project, choosing the path then.
- Publish all three on the website now, the skills linking to the pages as canonical.
- Keep the drafts in the work folder until KI Specifications opens v1, then raise them there as proposals.

### ENTRY-NAMES - Entry-file case

**Context:** Agent Skills uses upper-case `SKILL.md` and lower-case other files. The drafts use `WORK.md`, `KNOWLEDGE.md`, `ACQUIRE.md`. The live house work package uses lower-case `work.md`, currently being rolled out across the estate; upper case means a case-only rename of every live `work.md` (two-step `git mv` on macOS), cheapest during the current migration pass. **Query:** Should the entry files be upper case as Agent Skills does? **Options:**

- Upper case for all three, renaming `work.md` to `WORK.md` in the current migration pass.
- Upper case for `KNOWLEDGE.md` and `ACQUIRE.md` only, keeping `work.md`.
- Lower case for all three.

### SPEC-VERSION - Declaring the spec version

**Context:** Agent Skills has no spec-version field; a skill's own version is `metadata.version`. Work and knowledge packages live long and are rewritten in place. The drafts add an optional top-level `spec` field (`work/1` and so on), absent meaning version 1. **Query:** Should the three specs carry the optional `spec` field? **Options:**

- Keep the optional `spec` field, absent meaning version 1.
- No field, the version carried only by the published page.
- Make `spec` required from version 1.

## Report

Write your report as the run packet directs. For each query give, under its tag: your recommended option quoted, your confidence (`high`, `medium` or `low`) with a one-line reason, and one or two lines of what you checked directly and anything in the Context you found wrong or missing. Nothing else.
