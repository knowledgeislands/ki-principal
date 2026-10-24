# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › revise-5

**🤖 → 👤 Handoff to supervisor · Run report at 00:45 BST · last mark 23:45 BST**

---

## Done

The five drafts in [design/specs/](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md>) are now at draft 0.6, fixing the findings of [draft-review-3](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/draft-review-3.report.md>). Every owner decision still holds.

- **N1 (validator claim):**
  - **Format claim kept:** VALID-SKILL's claim stays. In `knowledge` and `acquire`, a conforming package renamed to `SKILL.md` is a valid skill under the Agent Skills specification. The drafts now say plainly that this is a claim about the format.
  - **`skills-ref` claim narrowed:** each Skill validity section, and a new Shared conventions line in `specs.md`, now claims only what reading the validator's source supports, without running it. Its field checks accept the examples as written.
  - **Parser limit stated:** the parser reads front matter with `strictyaml`, and the front matter ends at the first `---` wherever it falls. So a value with three hyphens in a row fails to parse.
  - The `metadata` contract is not narrowed to work around this.
- **N2 (description rules):** I took the first option. A description must give its area and where it stops. Audience, depth and what it answers are recommendations, and a description without them is still valid. This now reads the same in the field table, the field rule, Validation (the reviewer's checklist and a closing sentence) and Relation to Agent Skills.
- **N3 (the map):**
  - **One definition:** "mapped files" is defined once, under What condensing and factoring leave. It means every file except `KNOWLEDGE.md` and a licence file the `license` field names. A map is needed only when there are any.
  - **Directory links:** a link to a directory covers all the files in it, and its line describes them together. A file needs its own entry only where that line does not cover it.
  - **Used everywhere:** the Body content, `references/`, `assets/`, File references, Validation, reviewer and Relation wording all use the term.
- **N4 (house profile links):** `work-house-profile.md` gets a new Links conversion rule, with three cases in order:
  1. A path inside this package's own `/+/_WORK/<id>/` is rewritten relative to the file that holds the link, reading `work.md` as `WORK.md`.
  2. A path the reader has been given a URL or package name for becomes that URL or package name.
  3. Anything else is reported as an unmapped external dependency.

  A package with any unmapped link has no fully conforming portable reading, and Conformance today now says so.
- **N5 (ASCII names):** the name rules in all three specs now say ASCII `a-z` and `0-9`. The drafts state this as their own portability choice, listed under Different, because Agent Skills itself allows Unicode lowercase letters. `specs.md` has a new ASCII names convention, and the `package:` reference grammar now allows the same characters.
- **Status and history:** the three spec status lines read draft 0.6, the profile points to draft 0.6, and the overview history in `specs.md` has a draft 0.6 entry.
- **Checks:**
  - No em or en dashes in any of the five files.
  - One conformance reading for each rule: I searched for leftover "passed `skills-ref`" claims, "every file" map wording, required audience wording and non-ASCII name wording, and found none.
  - All six example front matters pass the field, type, name and length checks. The saved `skills-ref` field functions accept the five undotted examples and reject the dotted work example, as the drafts say.
- **Not committed:** nothing is committed, as the brief directs (commit identifiers: none). I wrote only in `design/specs/` and made no remote, publication or conform call.

## In Progress

Nothing is running.

Outstanding - no action requested now: `skills-ref` has still not been run in full, because its dependencies are not installed locally. The drafts now claim only what reading its source supports. The five changed drafts are uncommitted in `design/specs/`, for the supervising worker to commit.

## Queries

No outstanding queries.
