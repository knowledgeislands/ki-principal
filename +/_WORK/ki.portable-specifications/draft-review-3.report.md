# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › draft-review-3

**🤖 → 👤 Handoff to supervisor · Run report at 00:40 BST · last mark 23:45 BST**

---

## Done

Earlier findings from [draft-review-2](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/draft-review-2.report.md>):

1. Fixed - all three specifications use the containing file's directory as the relative-path base, classify by normalised location, and show nested internal and external examples.
2. Not fully fixed - scope boundaries, exclusions, provenance and the supporting-file map are required, but the universal map rule still disagrees with its exceptions; see N3.
3. Fixed - package references have a distinct notation, sibling-first resolution, an explicit fallback ambiguity rule and an unresolved-but-valid example.
4. Fixed - present fields must meet their constraints, optional compatibility is included, acquire states the complete local name grammar, and knowledge validation prohibits its scripts directory.
5. Fixed - the relationship wording defines and requires no linking metadata field while allowing profile extensions.
6. Fixed - work distinguishes the specification's upper-case entry name from the reference parser's lower-case fallback.
7. Fixed - the profile no longer implies a required state-file name, maps its identifier into metadata and points to draft 0.5.

### N1 - [must-fix] The blanket reference-validator claim exceeds the saved parser's capabilities

Files and sections: [specs.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:23>), Shared conventions; [work.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:228>), [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:193>) and [acquire.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:190>), Relation to Agent Skills / Skill validity.

The drafts assert that renaming a conforming entry to the skill entry name passes the reference validator, subject only to the dotted work name. A permitted quoted metadata value containing three consecutive hyphens breaks the saved parser: its delimiter split truncates the front matter inside that value, leaving an unterminated quoted scalar. This occurs with an otherwise conforming acquire source value and equally applies to optional metadata in the other formats. The relevant source is [parser.py](</var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/specifications/live-read/src/parser.py:45>), whose hash matches the supplied live check. The full YAML parses; the fragment produced by the saved parser does not.

Proposed fix: retain the owner's Agent Skills validity claim as a claim about the portable format, and distinguish it from compatibility with this demonstration validator. Limit the validator statement to the illustrated serialisations and the field checks actually verified, documenting this parser limitation. Replace wording implying an executed successful validation with wording supported by the source inspection. Do not silently narrow the portable metadata contract to accommodate a parser bug.

### N2 - [should-fix] Audience and depth are both constraints and recommendations

File and sections: [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:46>), Front matter / description; [description field](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:88>); [Validation](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:187>); Relation to Agent Skills.

The field table and validity review require the description to identify audience and depth, while the detailed field rule recommends them. A description identifying its area and exclusions but omitting audience or depth can therefore pass one reading and fail another. What the description answers has a similar table-versus-recommendation mismatch.

Proposed fix: keep area and boundaries required, and make audience, depth and answer examples recommendations consistently in the table, detailed rule, validation commentary and relation summary. Alternatively make all of them explicitly required throughout; either result must yield one conformance judgement.

### N3 - [should-fix] The universal map rule does not carry its later exemptions

File and sections: [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:20>), What condensing and factoring leave; [Body content](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:116>); File references; [Validation](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:183>).

The introductory contract requires every file other than the entry to be mapped with what each covers. Body content and validation exempt the named licence file and allow directory links to cover groups. The File references paragraph again says every file is linked from the map, while the reviewer is told to assess coverage for each file. A package containing only its entry and a named licence, or a map covering a group of diagrams by one directory link, has no single unqualified reading across those rules. This is the residual part of earlier finding 2.

Proposed fix: define the map's coverage set once, excluding the entry and named licence file, and make the map conditional on that set being non-empty. State consistently that a directory entry covers its contained files and describes their collective coverage and reading use; require individual descriptions only where collective coverage is insufficient.

### N4 - [should-fix] The profile identifies an absolute-link failure without mapping it

File and sections: [work-house-profile.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:26>), Conformance today; [Conversion rules](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:40>).

The profile promises a portable reader can obtain the same result through its mapping, but absolute Markdown targets are expressly identified as non-conforming and receive no conversion or failure rule. The field and state mappings are explicit; a reader still cannot determine how those links become portable references or what happens when a target is unavailable on the reading machine.

Proposed fix: add a deterministic reference mapping. Rewrite an identifiable internal target relative to its containing file, accounting for the entry rename; preserve a known external canonical URL or explicitly supplied package reference; otherwise report an unmapped external dependency. State that unresolved machine paths prevent a fully conforming portable rendering rather than claiming the mapping handles them.

### N5 - [should-fix] ASCII-only names are attributed to Agent Skills unchanged

Files and sections: [knowledge.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:80>) and [acquire.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:76>), name field and Relation to Agent Skills; [work.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:77>), name field; [specs.md](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:17>), Shared conventions.

The drafts limit letters and digits to ASCII and describe the knowledge/acquire name constraints as unchanged Agent Skills rules. The saved specification expressly permits Unicode lowercase alphanumeric characters, and the saved validator normalises with NFKC and accepts non-ASCII lowercase names. Its name function accepted an accented lowercase test name in this review. The supplied live check already records this distinction as drift D6.

Proposed fix: keep the drafts' explicitly stated ASCII grammar, but identify that restriction as their own portability choice and add it to the differences from Agent Skills. Correct the shared-conventions summary; keep the package-reference grammar aligned with the chosen package-name grammar.

Checks and authority:

- Owner-decision review: read the work definition, all decisions, the state and the supplied Agent Skills check; the metadata placement, version default, upper-case entries, one validity level, mapped house profile, owning skills and independent knowledge-as-skill framing are represented, subject to the findings above; no new owner choice is required.
- Fresh review: all five draft 0.5 files read; the principal earlier reference-resolution defects are repaired, with the remaining consistency and implementability issues listed above.
- Agent Skills evidence: the saved specification, parser and validator hashes exactly match the supplied live check; reviewed those local sources without a network call.
- Front-matter examples: all six examples parse as YAML and use string metadata; the saved validator's field functions accept the five undotted examples and reject the dotted work example as expected.
- Parser edge case: reproduced the saved delimiter operation and independently confirmed that its truncated front matter is invalid YAML; full parser and CLI execution remain unperformed because their dependencies are unavailable locally.
- Repository outcome: this run wrote no repository file, ran no conform command and made no Git, remote, publication or environment change; commit identifiers: none.

Not ready for the owner's read: correct the validator guarantee and reconcile the remaining conformance rules before presenting the final text.

## In Progress

Nothing is running.

Outstanding - no action requested now: the supervising worker owns the corrections and any follow-up review; full reference-validator execution remains a verification limitation.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 00:40 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Draft 0.5 review corrections · supervisor · since 00:40 BST
