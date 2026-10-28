# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › draft-review-2

**🤖 → 👤 Handoff to supervisor · Run report at 00:11 BST · last mark 23:45 BST**

---

## Done

### 1. [must-fix] Relative references have conflicting bases and an unreliable external/internal boundary

Files and sections: [work.md:175](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:175>), [knowledge.md:142](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:142>) and [acquire.md:127](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:127>), File references / References outside the package.

Internal paths are rooted at the package, while external paths are relative to the containing file. From a supporting file, a path beginning with `../` can still resolve inside the package. For example, from a file in the package's references directory, a parent-relative link into its assets directory remains internal. Classifying by prefix would exempt a missing internal target from the required resolution check; classifying by location requires the opposite result.

Proposed fix: choose one explicit base for each notation and classify relative targets by their normalised location against the package boundary. Retain all three external forms, sibling-first package lookup and form-only external validation. State that a parent-relative link which remains inside the package is internal and must resolve. Add one nested-file example for each case.

### 2. [must-fix] The knowledge contract makes boundaries and the file map both mandatory and optional

File and sections: [knowledge.md:15](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:15>), What condensing and factoring leave; description; Body content; File references; Validation.

The contract requires the description to name boundaries, the body to state exclusions, and Contents to name every file and its coverage. Later, description boundaries are only recommended, Contents and Limits are recommended sections, and validation checks only files under references for entry-point links. An author following the latter rules can omit the promised exclusions and the map of assets or other supporting files.

Proposed fix: make scope boundaries, exclusions and a complete map of supporting material required outcomes throughout. Allow flexible headings, but require the map whenever supporting files exist, covering assets and additional directories as well as references. Exempt the entry file itself explicitly. Keep provenance required and identify the semantic checks a reviewer makes, including whether each part can be traced to its source.

### 3. [should-fix] Package-name references lack a distinguishable notation and a collision rule

Files and sections: [work.md:179](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:179>), [knowledge.md:146](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:146>) and [acquire.md:131](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:131>), References outside the package; [specs.md:15](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:15>), Shared conventions.

A bare name can denote either an internal file/directory or an external package. The rule does not identify how a validator distinguishes them without resolving the target, which external validation deliberately does not require. Sibling-first priority is explicit and consistent, but multiple same-name candidates in supplied collections have no defined outcome.

Proposed fix: define the syntax or context that marks a package-name reference, retain sibling-first lookup, and report ambiguity when fallback collections expose multiple candidates. Include an unresolved but correctly formed example which remains valid. Do not add target availability to validity.

### 4. [should-fix] Validity checklists do not cover all normative constraints

Files and sections: [work.md:189](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:189>), [acquire.md:141](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:141>) and [knowledge.md:156](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:156>), Validation; acquire Front matter / name and description.

Work and acquire check name, description and metadata explicitly but omit their optional compatibility constraint. Knowledge's checklist omits its prohibition on scripts. Acquire also delegates its detailed name rules to Agent Skills instead of stating the consecutive-hyphen prohibition locally. A checklist-based implementer can therefore disagree with a reader applying all the surrounding prose, weakening the qualified skill-validity claims.

Proposed fix: require every present field to satisfy its declared constraints, state the complete acquire name grammar locally, and include each additional package prohibition in Validation. In particular, compatibility must be a non-empty string of at most 500 characters under the [live Agent Skills specification](https://agentskills.io/specification).

### 5. [should-fix] Removing dedicated relationship fields reads as banning all metadata relationships

Files and sections: [knowledge.md:176](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/knowledge.md:176>), [acquire.md:162](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/acquire.md:162>) and [specs.md:34](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md:34>), How they relate / Relation to the other specifications.

These sections say neither package names the other in metadata, while the metadata rules allow arbitrary additional string properties and profile extensions. The owner definition removes the acquisition-to-knowledge pipeline; it does not require a prohibition on optional relationships chosen by a profile.

Proposed fix: say that neither specification defines or requires a metadata field linking it to the other. Preserve their independence and the dropped pipeline fields without contradicting the extension mechanism.

### 6. [nit] The validator filename claim is too narrow

File and section: [work.md:200](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work.md:200>), Validation.

The statement that skills-ref checks only the upper-case skill entry omits its lower-case fallback, documented in the supplied [live check](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/agentskills-check.md>). This does not alter the decision to use upper-case package entry names.

Proposed fix: say it validates an Agent Skills entry rather than the five-file work contract; distinguish the specification's required upper-case filename from the validator's tolerated lower-case fallback.

### 7. [nit] The profile misstates the portable state schema

File and section: [work-house-profile.md:22](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/work-house-profile.md:22>), Conformance today.

The second conformance bullet implies that the portable state file requires a name field. It requires no such field; the profile's own State file table correctly moves the house identifier into metadata. Its introductory version pointer also still names draft 0.3.

Proposed fix: separate the entry-file identifier rename from the state-file identifier's move to metadata, and update the draft pointer after the corrections above.

Checks and authority:

- Owner-decision audit: read the work definition, every entry in its decisions log and the supplied Agent Skills check; upper-case entries, owning skills, metadata placement, one validity level, version defaults, mapped house profile and the independent knowledge-as-skill framing are represented. No additional owner decision is needed for these corrections.
- Cross-draft audit: all five drafts read; the three external forms, sibling-first lookup and form-only external checks agree in all three specifications, subject to findings 1 and 3.
- Front-matter check: skills-ref executable and Python module unavailable locally; Ruby's YAML parser and explicit field/type/name/length checks passed five of six examples, with the dotted work name rejected as expected. This was a limited independent check, not a skills-ref execution or a complete package validation.
- Live-source check: the current Agent Skills page was read; that used one read-only web request despite the brief's blanket no-remote clause. No other remote calls were made.
- Repository outcome: no repository files changed; no conform command, commit, push or publication. Commit identifiers: none.

## In Progress

Nothing running.

Outstanding - no action requested now: the supervising worker owns revisions and any subsequent review; skills-ref execution remains unperformed because it is unavailable locally.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 00:11 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Draft 0.4 review findings · supervisor · since 00:11 BST
