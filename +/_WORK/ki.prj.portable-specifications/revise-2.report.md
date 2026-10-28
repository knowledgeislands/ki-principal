# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › revise-2

**🤖 → 👤 Handoff to supervisor · Run report at 00:03 BST · last mark 23:45 BST**

---

## Done

Draft 0.3 is written in the five files under [design/specs/](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md). Status lines read 0.3, 20 October, and the overview records the revision. All eight findings were fixed, and none was rejected. Nothing outside `design/specs/` changed. Nothing was committed, pushed or published, and the brief asked for none of that.

- **1, empty files:** [work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md) now requires `WORK.md` and `state.md` to be valid from creation, with the initial state. Only `queries.md`, `messages.md` and `decisions.md` may start empty or `None`. The house profile's folder row says the same.
- **2, cross-package references:** each spec has a new subsection, "References outside the package", that separates two kinds of link:
  - Internal links must resolve inside the package.
  - External references are given by package name (looked up first among sibling directories, then in any collection the reader has), by URL, or by a relative path starting `../`. Validation checks only their form, not whether they resolve, and a reader reports one it cannot resolve.
  - `acquired-with`, `produces`, the Sources provenance and the work-to-package citations all use these external references. Each Validation list and the overview's shared conventions are updated to match.
- **3, work and skill validity:** I removed "never a valid skill" and the overview's claim of a universal barrier. Both now say:
  - a work package makes no claim to be a skill, and its entry file is `WORK.md`;
  - once renamed to `SKILL.md`, an undotted name passes and a dotted name fails;
  - the four other required files count as additional files, which Agent Skills allows.
- **4, Sources:** [knowledge.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md) now requires a non-empty `## Sources` section, and Validation checks for it.
  - For content curated from an acquire run, the section names the acquire package, the run output used and when the run read the source.
  - Overview, Contents and Limits stay recommended.
  - A note under the examples says a conforming body still needs Sources.
  - The overview's curation paragraph is updated to match. There is no Curation section and no broader curation duty.
- **5, house mapping:** [work-house-profile.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md) has a new "Conversion rules" section:
  - house fields map to `metadata` keys as `ki-` plus the field name, with `_` written as `-`;
  - strings and timestamps are copied unchanged;
  - booleans become `"true"` or `"false"`;
  - a `null` or absent field is omitted, never written as `"null"`.
  - Each house field now has its own row naming its exact destination key, and the state table says where each `waiting-on` and `release` value is copied from. The seven-state mapping is unchanged.
- **6, disclosure budget:** the work spec now states that the package tier can reach about 25,000 tokens at the per-file limits. That figure is listed under "Different, and why" with its reason, and the limits stay advisory under CONFORMANCE-LEVELS. I made the same kind of fix in acquire, whose 150-token first tier is now stated as a difference from Agent Skills' 100.
- **7, acquire scripts:** [acquire.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md) `scripts/` now separates Agent Skills' recommendations (self-contained, helpful errors, edge cases handled gracefully) from acquire's own two requirements (a dry run for any step that writes, and stopping when a response changes shape). The two requirements are listed as differences.
- **8, reciprocity:** the overview, acquire and knowledge now say the two packages name each other only "where that persistent relationship is declared". A method with transient output names no knowledge package.
- **Checks:**
  - No em or en dashes and no stale "every relative link" or "never a valid skill" wording remain.
  - The remaining mentions of draft 0.2 are historical.
  - No example front matter changed, so the review's validator results still apply. I did not re-run the validator.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The external-reference rule (three forms, name lookup starting with siblings, checked for form only) is this run's design to settle finding 2. The next review may want to look at it.
- The five revised drafts are uncommitted in `design/specs/`, waiting for the supervisor to receive them.

## Queries

No outstanding queries
