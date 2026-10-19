# ki.specifications queries

## Open

### PROJECT-NAME - Which note this Project takes, since `specifications` is already a different Project

since 2026-10-19 · from create-project · reviewed by query-review, 19:43 BST

**Context:** `Streams/Projects/specifications.md` already exists and describes a different Project: its outcome is "KI Specifications presents one consistent account of its authority and retained process, and the transferred KBEP and KBIP protocols each have a recorded disposition", it sits under Model, is `lifecycle: paused` since Kris paused it with the website on 2026-10-07, says it has no open records, and is registered in `Streams/Projects/Projects.md`; the Model theme page has no entry for it. This Project owns the three portable specs (`work`, `knowledge`, `acquire`), their home, publication and the later move into KI Specifications, so the two meet at KI Specifications but differ in outcome. The work id `ki.specifications` requires the slug `specifications`, so options b) and c) also rename one side. The blind review recommends b) instead, at medium confidence: the two outcomes are distinct, the old one is explicitly waiting on release from its pause, and Kris asked for a new Project.

**Query:** Should this Project take over the existing `specifications` note, or should one of the two Projects take a new name?

**Options:**

a) (recommended, confidence medium - review disagrees; both end in KI Specifications and the paused one has nothing in flight, but this widens a Project Kris paused) Fold the paused Project into this one: conform `specifications.md` to a new outcome covering the three specs, their home, publication and the move into KI Specifications, carrying the repository review and the KBEP and KBIP dispositions as a later step, and rewrite its `Projects.md` entry; the work id stays `ki.specifications`.

b) Keep the paused Project as it is and give this one a new slug, such as `portable-specifications`, renaming this work folder and its id to match.

c) Rename the paused Project, such as to `ki-specifications-review`, with its registry entry and links, and give this Project the `specifications` slug.

### SPEC-HOME - Where the three specifications live

since 2026-10-19 · from create-project and spec-drafts · reviewed by query-review, 19:43 BST

**Context:** Kris defined three portable specs on 19 October, `work`, `knowledge` and `acquire`, all using progressive disclosure "in line with agentskills.io spec standards", and gave two homes: the owning skills, or `knowledgeislands.info/specs/{work,knowledge,acquire}` (the opener wrote `knowledgeislands.info/specifications/{name}`; the path is part of the answer). Earlier the same day Kris said "I want to get those spec'd within a skill that owns them for now, then we formalise out of them later". The drafts in this work's `design/specs/` are tool-neutral and ready for either home. `ki-work-package` and `ki-acquire` own two of them and would each hold the portable spec as a reference distinct from their house-dialect standard; `knowledge` has no owning skill, and the stocktake predates Kris's refined definition of it. Another session (Claude Design) is working in the website, the website Project is paused, KI Specifications is on hold until its v1, and publishing is outward-facing and hard to take back.

**Query:** Should the three specs be held in their owning skills now and published to the website later from the same text?

**Options:**

a) (recommended, confidence high - reviewed; it follows "within a skill that owns them for now" and publishes nothing yet, and `knowledge` still needs a new skill) Hold each spec as one reference in its owning skill, with a new skill for `knowledge`, written in the agentskills.io page format, and publish the same text on the website as a later step of this Project, with the path chosen then.

b) Publish all three on the website now, at `knowledgeislands.info/specs/` or `knowledgeislands.info/specifications/` as Kris chooses, with the owning skills linking to the pages as the canonical text.

c) Keep the drafts in this work folder until KI Specifications opens v1, then raise them there as proposals.

### ENTRY-NAMES - Upper-case entry files for the three packages

since 2026-10-19 · from spec-drafts · reviewed by query-review, 19:43 BST

**Context:** Agent Skills names a package's entry file `SKILL.md` and keeps every other file lower-case. The drafts follow that with `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`. The live work-package contract requires a lower-case `work.md`, and names tools that depend on it, so upper case means a case-only rename of each live `work.md`, which ki.ways-of-working would carry during its current migration pass, needing a two-step `git mv` on macOS. The blind review recommends c) instead, at medium confidence: Agent Skills fixes one filename, `SKILL.md`, rather than a general rule that entry files are upper case, so the analogy brings no shown interoperability gain for the cost of changing the live contract.

**Query:** Should the entry files be upper case, `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`, as Agent Skills does?

**Options:**

a) (recommended, confidence medium - review disagrees; it matches Agent Skills and marks the entry file at a glance, at the cost of one rename across the estate) Upper case for all three, with the house work package renaming `work.md` to `WORK.md` in the current migration pass.

b) Upper case for `KNOWLEDGE.md` and `ACQUIRE.md` only, keeping `work.md` as built, so the work spec is the one exception.

c) Lower case for all three: `work.md`, `knowledge.md` and `acquire.md`.

### SPEC-VERSION - Whether a package declares which spec version it follows

since 2026-10-19 · from spec-drafts · reviewed by query-review, 19:43 BST

**Context:** Agent Skills has no spec-version field and puts a skill's own version in `metadata.version`. Work and knowledge packages live for a long time and are rewritten in place, so a later reader may meet one written to an older major version. The drafts add an optional top-level `spec` field (`work/1`, `knowledge/1`, `acquire/1`); when it is absent, a reader assumes version 1, and each package's own version stays in `metadata.version`. The review adds that absence must mean version 1 permanently, that readers must reject a declared major version they do not support, and that the drafts' validation lists do not yet check `spec`.

**Query:** Should the three specs carry the optional `spec` field?

**Options:**

a) (recommended, confidence high - reviewed; one optional line names the format apart from content versions and changing web pages, and version-1 packages need no migration) Keep the optional `spec` field, absence meaning version 1 for good, with readers rejecting an unsupported major and validation checking the field.

b) Follow Agent Skills exactly: no field, with the spec version carried only by the published page.

c) Make `spec` required from version 1.

### CONFORMANCE-LEVELS - One validity level or graded levels

since 2026-10-19 · from spec-drafts

**Context:** Agent Skills has one level: a skill is valid or not, and size and quality are recommendations. A retired earlier KI specification had Minimal, Standard and Extended levels. The drafts use one level: hard rules make a package valid, soft limits are warned and never failed, and quality is left to a reviewer's judgement.

**Query:** Should each spec have a single validity level, as Agent Skills does?

**Options:**

a) (recommended, confidence high - matches Agent Skills, and nothing yet needs a graded level) One level per spec, with soft limits warned.

b) Graded levels (Minimal, Standard and Extended), as the retired specification had.

## Parked

None
