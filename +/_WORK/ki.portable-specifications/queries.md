# ki.portable-specifications queries

## Open

### WORK-PROFILE - Must the house work package conform to the portable `work` spec?

since 2026-10-19 · from plan · reviewed by query-review-2

**Context:** The `work` draft requires `name`, `updated`, four states and the entry file. The house work package uses `id`, `since`, seven states and `work.md`, and `ki work status`, the Observatory, `ki agent close` and the rubrics read it across 33 live packages. The draft also builds in house rules, the message-queue order, the query form, decision pointers, `state.md` caps and a routing tier, which Kris said the spec should not infer. The draft's profile table wrongly claims the house already conforms; a mapped profile needs an explicit field and state mapping. ENTRY-NAMES settled only the spec's file name.

**Query:** Should the house package stay a mapped profile of `work`, or change to conform to it?

**Options:**

a) (recommended, confidence high - reviewed; it separates the portable contract from house practice and needs no estate-wide migration) Keep the house as a mapped profile with an explicit mapping, and move the house rules out of the spec into the profile.

b) Make the house conform, with an estate-wide rename and reader changes in ki.tools-burndown and ki.observatory.

c) Bend the spec to the house's `id`, `since`, seven states and `work.md`.

### KNOWLEDGE-SKILL - Which skill owns the `knowledge` spec

since 2026-10-19 · from plan · reviewed by query-review-2

**Context:** Under SPEC-HOME, each spec lives in its owning skill for now; `ki-work-package` owns `work` and `ki-acquire` owns `acquire`. No harness skill covers curated knowledge packages: `ki-repo-kb` governs an island's zones, `ki-authoring` writing conventions and `ki-skills` Agent Skills quality. The new Project note already names a new skill, but its name and remit are unsettled.

**Query:** Where should the `knowledge` spec be homed?

**Options:**

a) (recommended, confidence high - reviewed; it gives the package contract and its later validation a clear owner without widening neighbouring skills) A new governance skill, such as `ki-knowledge-package`, owning the spec and later its rubric.

b) `ki-repo-kb`, as a reference beside the island method.

c) `ki-skills`, beside the Agent Skills reference.

### MOVE-GATE - Where the Project finishes

since 2026-10-19 · from plan · reviewed by query-review-2

**Context:** The last step moves the specs into the KI Specifications repository, which is on hold until Kris restarts it at its v1 boundary, a date outside this Project's control. The paused Specifications Project owns that repository's readiness, and the move needs an explicit v1-boundary review there.

**Query:** Should the Project close once the specs are published and the move is handed off, or stay open until KI Specifications accepts them?

**Options:**

a) (recommended, confidence high - reviewed; publication is a deliverable this Project controls, while the undated restart belongs to another owner) Finish at publication, with a handoff record in KI Specifications' roadmap that its restart unblocks.

b) Stay open, on hold after publication, until KI Specifications restarts and accepts them.

### SPEC-LOCATION - Whether the optional `spec` field sits in `metadata`

since 2026-10-19 · from plan · reviewed by query-review-2

**Context:** Kris chose an optional `spec` version field under SPEC-VERSION. The drafts put it, and other added fields (`updated`, `acquired-with`, `source`, `mutation`, `omissions`, `produces`), at the top level. Agent Skills' `metadata` is a string-to-string map; if its validator rejects unknown top-level keys, top-level fields break the "also a valid skill" claim, while `metadata.spec` would not. The list field `omissions` cannot go in `metadata`. Whether the validator does reject them is what SPEC-LIVE-READ would settle.

**Query:** Should `spec` and the other single-value added fields sit in `metadata`, deciding list fields after the live check?

**Options:**

a) (recommended, confidence high - reviewed; the documented extension map takes single values, and the live check settles the rest) Put `spec` and the other single-value fields in `metadata` as strings, and decide list fields after SPEC-LIVE-READ.

b) Keep them at the top level, as drafted, and drop the "valid skill" claim.

## Parked

None
