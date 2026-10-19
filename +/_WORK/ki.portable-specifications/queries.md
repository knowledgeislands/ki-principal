# ki.portable-specifications queries

## Open

### CURATION-OWNER - Who owns what curation must do and record

since 2026-10-20 · from revise · reviewed by draft-review, views differ

**Context:** Curation is the step between `acquire`, acquiring knowledge, and `knowledge`, which Kris defined as "a package of knowledge that is well curated". Draft 0.2 asks only that a knowledge package's Sources name what it was taken from, including an acquire run's output, and nothing says what curation must do or record. The new `ki-knowledge-package` skill will own the `knowledge` spec and its rubric, `ki-acquire` owns `acquire`, and this Project leaves knowledge-acquisition practice to ki.knowledge-acquisition. The revise run recommended leaving curation to ki.knowledge-acquisition, at medium confidence, as practice rather than format. The blind review recommended the knowledge owner, at high confidence: a faithful capture and a curated package promise different things, so the curated package's own contract should state the minimum evidence of curation (selection and scope, material transformations or synthesis, unresolved uncertainty and provenance) without prescribing a workflow, while acquisition practice stays with ki.knowledge-acquisition.

**Query:** Who should own what curation must do and record?

**Options:**

a) (recommended, confidence medium - review agrees, but the run that raised it preferred b); the curated result and its rubric already belong to the knowledge owner) `ki-knowledge-package` owns curation guidance, and `knowledge` gains a short Curation section on what a curated package must record; acquisition practice stays with ki.knowledge-acquisition.

b) The specs keep only the Sources requirement, and curation practice goes to ki.knowledge-acquisition by a line in its `messages.md`.

c) `ki-acquire` owns it as the last stage of an acquisition, and `acquire`'s Output section names what curation receives.

## Parked

None
