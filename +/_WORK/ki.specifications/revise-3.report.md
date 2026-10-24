# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › revise-3

**🤖 → 👤 Handoff to supervisor · Run report at 00:06 BST · last mark 23:45 BST**

---

## Done

Draft 0.4 is in [design/specs/](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md). It follows KNOWLEDGE-AS-SKILL. Nothing outside `design/specs/` changed, and nothing was committed, pushed or published.

- [knowledge.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md):
  - **New opening.** A knowledge package is first and foremost an Agent Skills extension: a skill into which the knowledge of one area is condensed and factored. Its focus is the knowledge rather than doing, learning or performing an action.
  - **Its own contract.** A new subsection, "What condensing and factoring leave", says every package must leave a reader with three things: the scope of the area (in `description` and Limits), what was drawn out (in Contents, or in the overview alone for a single-file package) and provenance (in Sources). It prescribes no workflow and says there is no separate curation stage.
  - **Fields removed.** `metadata.acquired-with` is gone. Sources now cites an acquisition's output like any other source, naming the output and its read time, and the acquire package where it helps a reader.
  - **Description rule.** It is now "must name the area it covers" (it was "should").
  - **Wording.** "Topic" is now "area" where it means the package's scope.
  - **Skill validity.** The `scripts/` note, "Different, and why" and the Relation sections are reframed. The claim now ends "a skill whose focus is knowledge rather than action", replacing "not a skill in substance". The validator wording that VALID-SKILL set is unchanged.
- [acquire.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md):
  - `metadata.produces` is removed, along with the "curated into a knowledge package" framing.
  - The tracker example no longer has `produces` and no longer says "for curation".
  - The Relation section now says acquire and knowledge are separate extensions and neither is a stage of the other. Neither names the other in `metadata`, and a knowledge package may cite a run's output in its Sources.
- [specs.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md):
  - "Curation is open" is removed. In its place, one paragraph says making a knowledge package is condensing and factoring, under `knowledge`'s own contract.
  - The relation diagram no longer has the acquire-to-knowledge arrow.
  - The draft 0.4 history line, the knowledge row, the metadata field list, and the earlier-material rows for capture and `ki-pulse` are updated to match.
- [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md): only the status line changed, to draft 0.4, so the set carries one version. `work-house-profile.md` is untouched.
- **Checks:**
  - No em or en dashes.
  - No pipeline wording is left (`acquired-with`, `produces`, "feeds", "curated into"). The remaining "curated" is spec-areas.md's own wording, quoted in the earlier-material table.
  - Every revise-2 fix and every other owner decision still reads as before, including Overview, Contents and Limits staying recommended.
  - The changes to the example front matter only remove `metadata` string keys, so the skills-ref results still hold. I did not re-run the validator.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The four revised drafts are uncommitted in `design/specs/`, waiting for the supervisor to receive them.

## Queries

### LINK-FIELDS - drop the acquire and knowledge link fields entirely

**Context:** The brief said to remove any reciprocal acquire-to-knowledge relationship framed as a pipeline, while still letting a package cite its sources. The pipeline was carried by two metadata fields:

- `acquired-with` on knowledge meant "refresh by re-running this acquire package and curating the result".
- `produces` on acquire meant "the knowledge package this method feeds".

I removed both. Provenance now lives only in the knowledge package's Sources section, which may cite an acquire package or its output by external reference. This also removes a field that SPEC-LOCATION had listed, though SPEC-LOCATION itself, that added fields go in `metadata` as strings, is unchanged.

**Query:** Should the drafts keep both link fields removed, rather than keep a one-way citation field?

**Options:**
a) (recommended, confidence medium - this follows KNOWLEDGE-AS-SKILL's "drop the transition" most closely, but it removes fields the owner had seen in drafts 0.2 and 0.3) Keep both removed, with provenance carried only by Sources.
b) Restore a one-way, non-reciprocal `metadata.sources`-style key on knowledge, an optional machine-readable list of the external references cited, with no field on acquire.
