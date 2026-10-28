# Agent Skills live check

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.portable-specifications` · **Date:** 2026-10-19

Written by run live-read under SPEC-LIVE-READ (Kris, 19 October): one read-only check of the live Agent Skills specification for the drafts in [specs/](specs/specs.md), step 1 of [the plan](plan.md#steps). Read at about 23:45 BST on 19 October 2026. Nothing outside this note was edited, and nothing was published.

## Contents

- [Sources read](#sources-read)
- [Findings](#findings)
- [Drift from the harness reference](#drift-from-the-harness-reference)
- [What it means for the drafts](#what-it-means-for-the-drafts)

## Sources read

The `main` branch was read without the GitHub API, so no commit is pinned; each source file is identified by its SHA-256 at reading.

| Source | URL | SHA-256 at reading |
| --- | --- | --- |
| Specification page | <https://agentskills.io/specification> | - |
| Its source, `docs/specification.mdx` | <https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx> | `b9079c0c10b7930e8c6a20ff2bc10cda2a3343c55185120e3f1116a1a529b220` |
| Repository README | <https://github.com/agentskills/agentskills/blob/main/README.md> | - |
| Documentation licence, `docs/LICENSE` | <https://github.com/agentskills/agentskills/blob/main/docs/LICENSE> | - |
| `skills-ref` README | <https://github.com/agentskills/agentskills/tree/main/skills-ref> | - |
| Validator, `skills_ref/validator.py` | <https://github.com/agentskills/agentskills/blob/main/skills-ref/src/skills_ref/validator.py> | `b5ee3d8537c83c959c31c2cb080a5227646ede5aea545f1ac835ed3c4645f6c5` |
| Parser, `skills_ref/parser.py` | <https://github.com/agentskills/agentskills/blob/main/skills-ref/src/skills_ref/parser.py> | `9a74c9a90eb217b82bec27570332eab74547acfbee2973c0a8bcd23f6c7bc211` |
| Harness reference | `ki-agentic-harness` at `2ec94edc`, [`standards-agent-skills.md`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-skills/references/standards-agent-skills.md), last changed `3c48876f` (15 September); its source list marks SPEC and `skills-ref` last reviewed 2026-09-26 | - |

The specification page links one repository, `agentskills/agentskills`, from its Validation section: "Use the [skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) reference library to validate your skills". The `skills-ref` README says: "This library is intended for demonstration purposes only. It is not meant to be used in production."

## Findings

### 1. Case of files other than `SKILL.md`

**Answer:** Agent Skills sets no rule on the case of any file but `SKILL.md`, and its own examples mix upper-case and lower-case names.

- No case rule: "A skill directory may contain any files and directories beyond the required `SKILL.md`. The conventions below are recommendations for organizing common types of content." ([specification, Optional directories](https://agentskills.io/specification); `docs/specification.mdx` line 189)
- Upper-case examples in `references/`: "`REFERENCE.md` - Detailed technical reference", "`FORMS.md` - Form templates or structured data formats", beside "Domain-specific files (`finance.md`, `legal.md`, etc.)" (`docs/specification.mdx` lines 203-205)
- File-reference example: "See [the reference guide](references/REFERENCE.md) for details." (`docs/specification.mdx` line 231)
- The reference validator tolerates a lower-case entry file: `parser.py` line 15, "Prefers SKILL.md (uppercase) but accepts skill.md (lowercase).", and line 23, `for name in ("SKILL.md", "skill.md"):`

### 2. Where a skill's own version lives

**Answer:** in `metadata.version`, by example only. Agent Skills has no top-level version field and no rule naming the key; `version` appears in both `metadata` examples.

- "Example with optional fields" and the `metadata` field example both read:

  ```yaml
  metadata:
    author: example-org
    version: "1.0"
  ```

  (`docs/specification.mdx` lines 51-53 and 157-159; [specification, `metadata` field](https://agentskills.io/specification))
- The field's purpose: "Clients can use this to store additional properties not defined by the Agent Skills spec" (line 151).
- Agent Skills has no field for the specification's own version.

### 3. Closed fields and `metadata` values

**Answer:** the specification lists six fields without saying in words that no others are allowed, but `skills-ref` treats the list as closed and rejects any other top-level key. `metadata` is string-to-string by the specification's words; `skills-ref` coerces rather than rejects.

- The specification's field table: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` ([specification, Frontmatter](https://agentskills.io/specification)). No sentence on the page forbids or permits other top-level keys.
- `validator.py` lines 14-22:

  ```python
  # Allowed frontmatter fields per Agent Skills Spec
  ALLOWED_FIELDS = {
      "name",
      "description",
      "license",
      "allowed-tools",
      "metadata",
      "compatibility",
  }
  ```

- `validator.py` lines 108-112, run first in `validate_metadata` (line 132):

  ```python
  extra_fields = set(metadata.keys()) - ALLOWED_FIELDS
  if extra_fields:
      errors.append(
          f"Unexpected fields in frontmatter: {', '.join(sorted(extra_fields))}. "
          f"Only {sorted(ALLOWED_FIELDS)} are allowed."
  ```

- `metadata` in the specification: "A map from string keys to string values" and "We recommend making your key names reasonably unique to avoid accidental conflicts" (`docs/specification.mdx` lines 150-152).
- `metadata` in `skills-ref`: `parser.py` lines 61-62 coerce a mapping's keys and values with `str()`, `metadata["metadata"] = {str(k): str(v) for k, v in metadata["metadata"].items()}`; a non-mapping passes through unchanged, and `validator.py` has no `metadata` check. So `metadata.version: 1.0` unquoted is accepted and read as the string `"1.0"`, and a list value becomes its Python string form.
- `name` in `skills-ref`: `validator.py` admits only `c.isalnum() or c == "-"` after NFKC normalisation, so `.` fails.

### 4. Licence of the specification text

**Answer:** Creative Commons Attribution 4.0 International (CC BY 4.0). The drafts may follow its wording closely, provided they carry the attribution CC BY 4.0 requires and mark that they are modified.

- Repository README, License: "Code in this repository is licensed under Apache 2.0. Documentation is licensed under CC-BY-4.0. See individual directories for details." ([README](https://github.com/agentskills/agentskills/blob/main/README.md))
- `docs/LICENSE` opens "Attribution 4.0 International" ([docs/LICENSE](https://github.com/agentskills/agentskills/blob/main/docs/LICENSE)); the specification page is built from `docs/specification.mdx` in that directory. The live page carries no licence footer of its own.
- `skills-ref` code is Apache 2.0 (its README: "Apache 2.0").
- Origin: "The Agent Skills format was originally developed by Anthropic, released as an open standard" (README). `docs/LICENSE` names no copyright holder.
- CC BY 4.0 Section 3(a): "If You Share the Licensed Material (including in modified form), You must:" keep the identification of the creator and any copyright notice supplied, a notice referring to the licence, a notice referring to the disclaimer, and a link to the material where reasonably practicable; "indicate if You modified the Licensed Material and retain an indication of any previous modifications"; and "indicate the Licensed Material is licensed under this Public License". These "may be satisfied in any reasonable manner based on the medium, means, and context". An adapter's own licence "must not prevent recipients of the Adapted Material from complying with this Public License". Section 2(a)(6) also bars implying endorsement.

A sufficient attribution line for each draft and each published page: "Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe <work|knowledge|acquire> packages." This is a reading of the licence, not legal advice.

## Drift from the harness reference

Compared with [`standards-agent-skills.md`](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/keystone/ki-skills/references/standards-agent-skills.md). The exact numbers in its §14 (64, 1,024, 1-500, under 500 lines, under 5,000 tokens, about 100 tokens) and its layout, `name`, `description`, disclosure and file-reference rules all match the live page. The drift:

| # | Local reference | Live | Weight |
| --- | --- | --- | --- |
| D1 | ※5: "The reference validator (`skills-ref validate`) checks frontmatter/naming only"; §6 calls Claude Code-only fields "valid in CC, may not port" | `skills-ref` rejects every top-level key outside its six with "Unexpected fields in frontmatter"; a skill using Claude Code fields fails `skills-ref validate` | Material: the reference understates the closed set, and the drafts' "also a valid skill" claim rested on the gap |
| D2 | Records neither the specification text's licence nor `skills-ref`'s | Documentation CC BY 4.0; code Apache 2.0 | Gap; matters wherever the harness quotes the specification |
| D3 | §6: `metadata` "string→string map", listed as "validated when present" | Specification: string to string, and key names "reasonably unique"; `skills-ref` coerces values with `str()` and never rejects | Minor: the uniqueness advice is missing, and the reference validator does not validate `metadata` |
| D4 | §2: `SKILL.md` is the required entry point | `skills-ref` also accepts `skill.md` when `SKILL.md` is absent | Minor; the specification names only `SKILL.md` |
| D5 | §2: supporting files "named by content (`form-validation-rules.md`, not `doc2.md`)" | Specification examples use generic upper-case `REFERENCE.md` and `FORMS.md` | Minor; the local rule is best practice, not the specification, and is silent on case |
| D6 | §4: "lowercase letters, digits, and hyphens only" | Specification: "unicode lowercase alphanumeric characters (`a-z`, `0-9`)"; `skills-ref` normalises with NFKC and admits any `isalnum()` lower-case character | Minor; the specification is itself ambiguous |

D1 and D2 are for the harness's next `ki-skills` REFRESH; this run edits nothing there.

## What it means for the drafts

| Draft claim | Where | Finding | Consequence |
| --- | --- | --- | --- |
| "Renamed `KNOWLEDGE.md` to `SKILL.md`, a conforming package is also a valid skill" | `knowledge.md` line 138 | 3: `updated`, `acquired-with` and `spec` are top-level keys outside the six | False as written: `skills-ref validate` fails any package using them. Either move them into `metadata` as quoted strings (`metadata.spec: "knowledge/1"`, `metadata.updated: "2026-10-19"`), after which the claim holds, or drop the sentence |
| "An acquire package is a skill whose task is acquisition" | `acquire.md` line 148 | 3: required `source` and `mutation`, and optional `omissions`, `produces` and `spec`, are top-level | False as written for every conforming package, since `source` and `mutation` are required. Same choice: move them into `metadata` (`omissions` becomes one comma-separated string), or say an acquire package shares Agent Skills' layout without being a valid skill |
| "A reader ignores top-level keys it does not know" | `work.md` line 95, `knowledge.md` line 89, `acquire.md` line 94, `specs.md` line 17 | 3 | The drafts' own rule, and the opposite of `skills-ref`'s. Keep it if wanted, but list it under "Different, and why", not imply Agent Skills does the same |
| "an upper-case entry file", listed as reused unchanged | `work.md` line 180, `knowledge.md` line 137, `acquire.md` line 148, `specs.md` line 17 | 1 | Agent Skills fixes one name, `SKILL.md`; the general rule is the drafts'. Reword to "one entry file in upper case, as `SKILL.md` is", under "Different" |
| ENTRY-NAMES: Agent Skills "keeps every other file lower-case" | [plan](plan.md#entry-names) | 1 | Wrong: no rule, and its own examples use `REFERENCE.md` and `FORMS.md`. Drop it. Case gives no reason against `WORK.md` beside lower-case `state.md`, and `skills-ref`'s acceptance of `skill.md` shows Agent Skills' own tooling tolerates a lower-case entry file |
| "a package's own version, where it has one, goes in `metadata.version`" | `knowledge.md` line 89; examples at `knowledge.md` line 59, `acquire.md` line 68 | 2 | Consistent with Agent Skills' examples, which are an example, not a rule; say "as Agent Skills' examples do". The examples' quoted values are right |
| `spec` field | All three | 2, 3 | Agent Skills has no counterpart, so `spec` is genuinely new; at top level it breaks skill validity, in `metadata` it does not |
| `name` with `.` between segments | `work.md` line 37 | 3 | Rightly listed under "Different": a dotted name fails `skills-ref`. `work` makes no valid-skill claim, so no change |
| "`license` and `metadata` with their constraints", reused unchanged | All three | 3 | Holds; add Agent Skills' advice that `metadata` key names be "reasonably unique", which the drafts' prefixing advice already matches |
| Text follows the agentskills.io page closely | All three, and any publication | 4 | Allowed under CC BY 4.0 with attribution and a statement of change. Add the attribution line above to each draft before SPEC-TEXT, and require it on each page at SPEC-PUBLISH; the site's own page licence must not stop readers complying with CC BY 4.0 |
