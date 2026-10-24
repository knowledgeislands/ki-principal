# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › revise

**🤖 → 👤 Handoff to supervisor · Run report at 23:56 BST · last mark 23:45 BST**

---

## Done

- [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md), draft 0.2: house ways of working removed (message order and `IMPORTANT` lines, the query form, the decisions life cycle, `state.md` sections and caps, the Register tier and the "Takes ... Not for ..." description voice); each file now states only what an entry carries; three disclosure tiers; `spec` moved to `metadata.spec`; `state.md` gains `metadata`; validation checks `spec` and drops the message-order check; CC BY 4.0 attribution added.
- [knowledge.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md), draft 0.2: the description now says who the package is for and at what depth; `metadata.updated` is read in the first tier; `metadata.owner` added for the named owner; `updated`, `acquired-with` and `spec` moved into `metadata` as strings; Sources names the run output it was taken from; "also a valid skill" now holds and is reworded to what `skills-ref` checked on 19 October; owned by `ki-knowledge-package`; attribution added.
- [acquire.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md), draft 0.2: the depth of each method now depends on its source (a new `git-help` minimal example for learning a tool); coverage levels and checksums are recommended, not required; Procedure and Verification scale from a tool's help to a whole collection; `source`, `mutation`, `produces`, `spec` and `omissions` (as one comma-separated string) moved into `metadata`; "is a skill whose task is acquisition" now holds; attribution added.
- [specs.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md): rewritten to the decisions. Upper-case entry files and a closed list of top-level keys are now listed as the drafts' own rules, not as things taken from Agent Skills; there is an owning-skill column; the false claim that the house package conforms is removed; curation is named as open.
- [work-house-profile.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md), new: says where the house package fails the spec today, maps its fields and its seven states onto the spec's four (using Kris's four kinds, so `with-supervisor` is now `active` rather than draft 0.1's `waiting`), and lists the house rules left to the profile.
- Every draft now closes the list of top-level keys, as `skills-ref` does, so a reader ignores only unknown `metadata` keys. This replaces draft 0.1's "a reader ignores top-level keys it does not know". Checks: no en or em dashes; every relative link resolves, apart from one example path in a code span. Nothing committed, as the brief directs; only `design/specs/` was written.

## In Progress

Nothing is running. Next under the plan: one blind review of draft 0.2 (step 4), then SPEC-TEXT to Kris.

Outstanding - no action requested now: the `work.md` to `WORK.md` rename under ENTRY-NAMES still needs its line in ki.ways-of-working's `messages.md`, which is the coordinator's to send; the drift-check rubric criteria come when the specs are homed (step 6).

## Queries

### CURATION-OWNER - Who owns curation, turning captured material into a knowledge package

**Context:** Curation sits between `acquire` and `knowledge`. Draft 0.2 asks only that a knowledge package's Sources name what it was taken from, including an acquire run's output. Nothing says what curation must do or record, or who owns that. This Project's scope leaves knowledge-acquisition practice to ki.knowledge-acquisition, and `ki-knowledge-package` will own the `knowledge` spec and its rubric.

**Query:** Who should own what curation must do and record?

**Options:**

a) (recommended, confidence medium - curation is a practice rather than a format, and practice is out of this Project's scope; but it could equally be read as part of keeping knowledge "well curated") The specs keep only the Sources requirement, and curation practice goes to ki.knowledge-acquisition by a line in its `messages.md`.

b) `ki-knowledge-package` owns curation guidance beside the `knowledge` spec, and `knowledge` gains a short Curation section saying what a curated package must record.

c) `ki-acquire` owns it as the last stage of an acquisition, and `acquire`'s Output section names what curation receives.

### 🤖 → 👤 Handoff to supervisor · since 23:56 BST

👤 1 with you

- [with you] CURATION-OWNER · owner · since 23:56
- [uncommitted] design/specs drafts 0.2 and work-house-profile.md
