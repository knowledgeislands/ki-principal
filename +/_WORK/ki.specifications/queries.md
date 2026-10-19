# ki.specifications queries

## Open

### PROJECT-NAME - Which note this Project takes, since `specifications` is already a different Project

since 2026-10-19 · from create-project

**Context:** `Streams/Projects/specifications.md` already exists and describes a different Project: its outcome is "KI Specifications presents one consistent account of its authority and retained process, and the transferred KBEP and KBIP protocols each have a recorded disposition", it sits under Model, is `lifecycle: paused` since Kris paused it with the website on 2026-10-07, has no open records, and is registered in `Streams/Projects/Projects.md`. This Project, opened under SPECIFICATIONS-PROJECT on 19 October, owns the three portable specs (`work`, `knowledge`, `acquire`), SPEC-HOME, publication and "the later move into KI Specifications", so the two meet at KI Specifications but differ in outcome. The create-project run changed nothing in that note or the registry. The work id `ki.specifications` requires the Project slug `specifications`, so options b) and c) also rename one side.

**Query:** Should this Project take over the existing `specifications` note, or should one of the two Projects take a new name?

**Options:**

a) (recommended, confidence medium - both end in KI Specifications and the paused one has nothing in flight, but this widens the scope of a Project Kris paused) Fold the paused Project into this one: conform `specifications.md` to a new outcome covering the three specs, their home, publication and the move into KI Specifications, carrying the repository review and the KBEP and KBIP dispositions as a later step in its Notes, and rewrite its entries in `Projects.md` and on the Model theme page; the work id stays `ki.specifications`.

b) Keep the paused Project as it is and give this one a new slug, such as `portable-specifications`, renaming this work folder and its id to match.

c) Rename the paused Project, such as to `ki-specifications-review`, with its registry entries and links, and give this Project the `specifications` slug.

### SPEC-HOME - Where the three specifications live

since 2026-10-19 · from create-project and spec-drafts

**Context:** Kris defined three portable specs on 19 October, `work`, `knowledge` and `acquire`, all using progressive disclosure "in line with agentskills.io spec standards", and gave two homes: the owning skills, or `knowledgeislands.info/specs/{work,knowledge,acquire}` (the opener wrote `knowledgeislands.info/specifications/{name}`; the path is part of the answer). Earlier the same day Kris said "I want to get those spec'd within a skill that owns them for now, then we formalise out of them later". The drafts, now in this work's `design/specs/`, are tool-neutral and ready for either home. Two specs have an owning skill, `ki-work-package` and `ki-acquire`, whose standards are in the house dialect, so each would hold the portable spec beside its own profile; `knowledge` has no owning skill. Another session (Claude Design) is working in the website, the website Project is paused, KI Specifications is on hold until its v1, and publishing is outward-facing and hard to take back.

**Query:** Should the three specs be held in their owning skills now and published to the website later from the same text?

**Options:**

a) (recommended, confidence medium - it follows "within a skill that owns them for now", avoids publishing drafts and the website clash, and keeps one text to publish; `knowledge` still needs a new owning skill) Hold each spec as one reference in its owning skill, with a new skill for `knowledge`, written in the agentskills.io page format, and publish the same text on the website as a later step of this Project, with the path chosen then.

b) Publish all three on the website now, at `knowledgeislands.info/specs/` or `knowledgeislands.info/specifications/` as Kris chooses, with the owning skills linking to the pages as the canonical text.

c) Keep the drafts in this work folder until KI Specifications opens v1, then raise them there as proposals.

### ENTRY-NAMES - Upper-case entry files for the three packages

since 2026-10-19 · from spec-drafts

**Context:** Agent Skills marks a package's entry with an upper-case `SKILL.md` and keeps every other file lower-case. The drafts follow that with `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`. The house work package, which ki.ways-of-working's migration pass is moving folders into now, uses a lower-case `work.md`, so upper case means a case-only rename of each live `work.md`, which ki.ways-of-working would carry. Doing that during the current pass costs least, but on macOS a case-only rename needs `git mv` in two steps.

**Query:** Should the entry files be upper case, `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`, as Agent Skills does?

**Options:**

a) (recommended, confidence medium - matches Agent Skills and marks the entry file at a glance; the cost is one rename across the estate) Upper case for all three, with the house work package renaming `work.md` to `WORK.md` in the current migration pass.

b) Upper case for `KNOWLEDGE.md` and `ACQUIRE.md` only, keeping `work.md` as built, so the work spec is the one exception.

c) Lower case for all three: `work.md`, `knowledge.md` and `acquire.md`.

### SPEC-VERSION - Whether a package declares which spec version it follows

since 2026-10-19 · from spec-drafts

**Context:** Agent Skills has no spec-version field and puts a skill's own version in `metadata.version`. Work and knowledge packages live for a long time and are rewritten in place, so a later reader may meet one written to an older major version. The drafts add an optional top-level `spec` field (`work/1`, `knowledge/1`, `acquire/1`); when it is absent, a reader assumes version 1. Each package's own version stays in `metadata.version`.

**Query:** Should the three specs carry the optional `spec` field?

**Options:**

a) (recommended, confidence medium - one optional line now avoids guessing at the first breaking change, while staying silent costs nothing until then) Keep the optional `spec` field, absent meaning version 1.

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
