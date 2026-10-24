# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Portable specifications](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md>) › revise-4

**🤖 → 👤 Handoff to supervisor · Run report at 00:37 BST · last mark 23:45 BST**

---

## Done

The five drafts in [design/specs/](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/specs/specs.md>) are now at draft 0.5. Every owner decision is unchanged, LINK-FIELDS included.

- **Finding 1, relative references (must-fix):** each of the three specs now uses a single base. A relative path resolves from the directory of the file that holds it, which is the package root in the entry file. After `.` and `..` are normalised, the path is classed by where it lands: inside the package it is internal and must resolve, even when it begins `../`; outside the package it is external. Each spec gives a nested-file example of each case, from a file in `references/`. The difference from Agent Skills' root-relative rule is listed under "Different, and why".
- **Finding 2, the knowledge contract (must-fix):** the description must name the area and say where it stops. The body must state its limits. Whenever the package has other files, the body must also map every one of them (references, assets and any other directory). `KNOWLEDGE.md` and a named licence file are exempt, and a directory of similar files can be mapped with one link. Headings are flexible: Limits and Contents are recommended, and `## Sources` stays required. Validation now checks the map mechanically and lists what a reviewer judges, including whether each part can be traced to its source.
- **Finding 3, package names (should-fix):** a package-name reference is now written `package:<name>`, so a validator can tell it apart from a URL (any other scheme) or a relative path (anything else) without resolving it. The name grammar covers work, knowledge and acquire names. Lookup still tries the sibling package first. If there is no sibling and the given collections hold more than one match, the reader reports the reference as ambiguous, names the candidates and resolves to none of them. Each spec has an example of an unresolved but well-formed reference that is still valid.
- **Finding 4, Validation coverage (should-fix):** every field that is present must meet its constraints, and `compatibility` is now 1-500 characters and non-empty in work and acquire. Acquire states its full name grammar locally, including the ban on `--`, and both tables now carry that ban. Validation now also checks:
  - knowledge: the ban on `scripts/`
  - work: query headings and their unique IDs
  - acquire: the `source` length, the `mutation` values and the `omissions` list form
  - Where something cannot be checked mechanically (message and decision contents, script dry runs, the Mutation list, no captured content in assets), the Validation section names it as a reviewer's judgement.
- **Finding 5, link fields (should-fix, and LINK-FIELDS):** `specs.md`, `knowledge.md` and `acquire.md` now say that neither spec defines or requires a `metadata` field linking a package to the other kind, and that profile keys are not restricted.
- **Finding 6, validator filename (nit):** `work.md` now says that `skills-ref validate` checks an Agent Skills entry, not the five-file contract. It also separates the `SKILL.md` name the specification requires from the lower-case `skill.md` the validator tolerates.
- **Finding 7, profile (nit):** the house profile now treats the entry file's `id`-to-`name` rename separately from the state file's `id` moving to `metadata.ki-id`, and its pointer now names draft 0.5. I also added one conformance gap that the new notation rule makes explicit: run reports and briefs use absolute-path links, which the spec does not allow.
- **Status and history:** the three status lines read draft 0.5, 20 October 2026, and the overview's history has a draft 0.5 entry.
- **Checks:**
  - No em or en dashes in any of the five files.
  - A Ruby YAML check of the six example front-matter blocks for fields, types, name grammar and lengths passed all six. This was not a run of `skills-ref`.
  - I matched each Validation list against its spec's normative statements by hand.
  - No commit, no `ki repo conform`, no remote call, and nothing written outside `design/specs/`. Commit identifiers: none, because the brief bars committing.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The five drafts are uncommitted in `design/specs/` for the coordinator to receive and commit.
- `package:` was my choice of token under the brief. Kris can weigh it at SPEC-TEXT if he wants another.
- The new nested-path rule should go through the next blind review, before SPEC-TEXT.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 00:37 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] Draft 0.5, five revised drafts · supervisor · since 00:37 BST
- [uncommitted] design/specs/ five drafts
