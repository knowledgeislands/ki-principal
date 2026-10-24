# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › draft-review-4

**🤖 → 👤 Handoff to supervisor · Run report at 00:49 BST · last mark 23:45 BST**

---

## Done

1. Fixed - earlier N1: all four validity summaries distinguish Agent Skills format validity from the demonstration validator, limit the source-inspection claim to the examples' field checks and document its YAML/delimiter limitations.
2. Fixed - earlier N2: [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:46>), Front matter, description, Validation and Relation to Agent Skills consistently require area and boundaries while recommending audience, depth and answer examples.
3. Fixed - earlier N3: [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:20>) defines the mapped-file set once, excludes the entry and named licence file, makes the map conditional and consistently permits collective directory coverage.
4. Not fully fixed - earlier N4: [work-house-profile.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:50>), Conversion rules, now maps absolute targets and reports unmapped dependencies, but preserves relative targets through the entry rename; residual finding R1 below.
5. Fixed - earlier N5: all three name rules and relation summaries, and [specs.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:17>), identify ASCII-only names as the drafts' restriction, distinguish Agent Skills' Unicode rule and align the package-reference grammar.

### R1 - [should-fix] Relative links to the house entry break during conversion

File and section: [work-house-profile.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:50>), Conversion rules / Links; residual earlier N4.

The mapping preserves relative targets unchanged while renaming the entry to its upper-case portable name. A permitted house report in `design/` can link to the definition through a relative target using its current lower-case name. After conversion that target no longer identifies the entry on a case-sensitive filesystem, so a valid house package can produce a broken internal reference and fail the portable contract. The rename handling in the absolute-path branch does not cover this case.

Proposed fix: resolve each relative target against its containing house file, apply the entry rename when it identifies that entry, then express the result relative to the converted containing file. Preserve its fragment. Extend this rule to references from sibling packages when their supplied conversion mapping identifies a renamed entry, or report that dependency as requiring conversion. Do not preserve a known renamed target unchanged.

### N1 - [should-fix] Optional omissions metadata has an unconditional completeness obligation

File and sections: [acquire.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:101>), metadata / omissions, and [Validation](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:186>).

The omissions field is recommended, but the same rule makes any undeclared omission a package defect, and the reviewer must assess whether the declared omissions are complete. The required body sections do not specify an alternative omissions declaration. Nor does the spec distinguish an omission within the promised acquisition from material deliberately excluded by Scope. A method that correctly captures its chosen scope but omits other material the source holds therefore has no single clear conformance judgement when that metadata field is absent.

Proposed fix: define omissions against the acquisition's declared scope and coverage promise. Require disclosure when gaps exist, and say whether it must use the metadata field or may use an identified body section; permit absence when there are no such gaps. Align the field rule and validation. This clarifies the existing guarantees without requiring a new owner decision.

Checks and authority:

- Review coverage: read [work.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/work.md>), every entry in [decisions.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/decisions.md>), [agentskills-check.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/agentskills-check.md>), all five draft 0.6 files and the full [draft-review-3 report](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/draft-review-3.report.md>); checked the house mapping against its referenced standard.
- Owner decisions: the required entry names, metadata placement, permanent version-1 default, unsupported-major rejection, single validity level, mapped house profile, owning skills, independent knowledge-as-skill framing and open profile keys are represented; no new owner choice is needed.
- Agent Skills claims: the saved specification, parser and validator hashes match the supplied live check; source review found no further inaccurate Agent Skills claim after the five corrections.
- Examples: all six front-matter examples parse with Ruby's YAML parser and use string metadata; the saved validator's source-extracted field functions accept the five undotted examples and reject the dotted work example as expected.
- Portability check: confirmed the profile explicitly preserves relative paths; an exact-case target check reproduces the entry-rename failure without creating any package files.
- Verification limitation: full reference-parser and CLI execution was not performed; the executed checks cover YAML parsing and source-extracted field functions, not the complete validator.
- Repository outcome: no repository file changed; no conform, Git, remote, publication or persistent environment operation; commit identifiers: none. Only this report and the required status file were written.

Not ready for the owner's read: finish the entry-reference mapping and make omissions disclosure yield one clear conformance judgement.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervising worker owns the two corrections and any follow-up review; complete reference-validator execution remains outside this run's verification.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 00:49 BST

🤖 0 running · 🤝 1 handoff · ⛔ 0 blocked

- [handoff] Draft 0.6 review and two corrections · supervisor · since 00:49 BST
