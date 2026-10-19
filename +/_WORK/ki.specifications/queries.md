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

### ENTRY-NAMES - Upper-case entry files for the three packages

since 2026-10-19 · from spec-drafts · reviewed by query-review, 19:43 BST

**Context:** Agent Skills names a package's entry file `SKILL.md` and keeps every other file lower-case. The drafts follow that with `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`. The live work-package contract requires a lower-case `work.md`, and names tools that depend on it, so upper case means a case-only rename of each live `work.md`, which ki.ways-of-working would carry during its current migration pass, needing a two-step `git mv` on macOS. The blind review recommends c) instead, at medium confidence: Agent Skills fixes one filename, `SKILL.md`, rather than a general rule that entry files are upper case, so the analogy brings no shown interoperability gain for the cost of changing the live contract.

**Query:** Should the entry files be upper case, `WORK.md`, `KNOWLEDGE.md` and `ACQUIRE.md`, as Agent Skills does?

**Options:**

a) (recommended, confidence medium - review disagrees; it matches Agent Skills and marks the entry file at a glance, at the cost of one rename across the estate) Upper case for all three, with the house work package renaming `work.md` to `WORK.md` in the current migration pass.

b) Upper case for `KNOWLEDGE.md` and `ACQUIRE.md` only, keeping `work.md` as built, so the work spec is the one exception.

c) Lower case for all three: `work.md`, `knowledge.md` and `acquire.md`.

## Parked

None
