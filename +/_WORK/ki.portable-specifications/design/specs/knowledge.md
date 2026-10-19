# Knowledge specification

> The format for a knowledge package: an Agent Skills extension, a skill into which the knowledge of one area is condensed and factored, described so that a reader can tell whether it is the package that tells them what they want to know, and read progressively.

**Status:** draft 0.4, 20 October 2026. Name `knowledge`. To be held in a new skill, `ki-knowledge-package`, as `references/standards-knowledge-spec.md`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe knowledge packages.

## What a knowledge package is

A knowledge package is, first and foremost, an extension of Agent Skills: a skill into which the knowledge of one area is condensed and factored. Its focus is the knowledge itself, what is known about the area, rather than doing, learning or performing an action, which is what an ordinary skill's instructions are for. It keeps a skill's shape, a directory, an entry file with front matter and progressive disclosure, and changes what the body holds: knowledge condensed to what holds and factored into an overview and focused files, kept current by an owner who stands behind it.

A person or an agent who wants to learn about the area, or has a question about it, reads its description to decide whether this is the package for them, then its overview, then only the files they need. It is not raw evidence (an acquisition's output is a source the package may cite, not part of it), not the method for acquiring knowledge from a source (that is an [acquire package](acquire.md)) and not the record of a piece of work (that is a [work package](work.md)).

### What condensing and factoring leave

Making a knowledge package is condensing and factoring: drawing the knowledge of one area out of wherever it lies, condensing it to what holds, and factoring it into an overview and focused files. This specification sets no workflow for doing so, and there is no separate curation stage. However a package is made, it must leave a reader with three things:

- **The scope of the area:** what the package covers and where it stops. The `description` names the area and its boundaries, and the body says what lies outside it, in the recommended Limits section.
- **What was drawn out:** what the package holds and where. The overview's Contents names every file and what it covers; a package with no other files holds what was drawn out in its overview.
- **Provenance:** where each part came from, in the required [Sources](#body-content) section.

These belong to the package's own contract: [Validation](#validation) checks them where they can be checked, and a reviewer judges them where they cannot.

## Directory structure

A knowledge package is a directory containing, at minimum, a `KNOWLEDGE.md` file:

```text
area-name/
|-- KNOWLEDGE.md     # Required: metadata + overview and contents
|-- references/      # Optional: the body of knowledge, one focused file per subtopic
|-- assets/          # Optional: diagrams, images, data, schemas
`-- ...              # Any additional files or directories
```

## `KNOWLEDGE.md` format

The `KNOWLEDGE.md` file must contain YAML front matter followed by Markdown content.

### Front matter

| Field | Required | Constraints |
| - | - | - |
| `name` | Yes | Max 64 characters. Lowercase letters, numbers and hyphens only. Must not start or end with a hyphen. Must match the directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Says what the knowledge covers, who it is for and at what depth, and what it answers. |
| `license` | No | Licence name or reference to a bundled licence file. |
| `metadata` | No | A map from string keys to string values. Holds `updated`, `owner` and `spec`, and any property this specification does not define. |

No other top-level key is allowed.

**Minimal example:**

```markdown
---
name: uk-vat-for-freelancers
description: Explains UK VAT for sole-trader freelancers, from first principles to working a quarterly return - registration thresholds, flat rate and standard schemes, digital record-keeping and returns. Use to learn how VAT applies to you, decide whether and how to register, or check how a return is worked out. Not for limited companies or import duties.
---
```

**Example with optional fields:**

```markdown
---
name: uk-vat-for-freelancers
description: Explains UK VAT for sole-trader freelancers, from first principles to working a quarterly return - registration thresholds, flat rate and standard schemes, digital record-keeping and returns. Use to learn how VAT applies to you, decide whether and how to register, or check how a return is worked out. Not for limited companies or import duties.
license: CC-BY-4.0
metadata:
  updated: "2026-10-19"
  owner: accounts-team
  spec: "knowledge/1"
  version: "2.1"
---
```

Both examples show the front matter only; the body of a conforming package also needs its `## Sources` section.

#### `name` field

As Agent Skills: 1-64 characters; lowercase `a-z`, `0-9` and `-` only; no leading, trailing or consecutive hyphens; matches the parent directory. Name the area, not the format: `uk-vat-for-freelancers`, not `vat-notes` or `knowledge-1`.

#### `description` field

The required `description` field is the one thing a reader sees before choosing, so it decides whether the package is found and whether the right reader opens it.

- Must be 1-1024 characters
- Must name the area it covers, and should say where it stops
- Should say who it is for and at what depth: an introduction for a newcomer, a working guide for a practitioner, or a reference for someone who knows the field
- Should say what a reader can learn or answer with it ("Use to ..." or "Answers ..."), then any close neighbours it does not cover ("Not for ...")
- Should use the words a person asking about the area would use

**Good:** `Explains UK VAT for sole-trader freelancers, from first principles to working a quarterly return - registration thresholds, flat rate and standard schemes, digital record-keeping and returns. Use to learn how VAT applies to you, decide whether and how to register, or check how a return is worked out. Not for limited companies or import duties.`

**Poor:** `Tax information.`

#### `license` field

As Agent Skills.

#### `metadata` field

A map from string keys to string values, as Agent Skills. This specification defines three keys, each a string:

- `updated` (recommended) - the date someone last checked that the content is still true, `YYYY-MM-DD`, not the date of the last edit. A reader weighs a package by its currency, so `updated` is read with `name` and `description`: an old date says to check before relying on it. A package whose subject changes fast should state its review cadence in the overview.
- `owner` (recommended) - who stands behind the package and keeps it current: a person, team or organisation, in words.
- `spec` - the specification and major version the package follows, `knowledge/1`. Absent means `knowledge/1`, now and in every later version. A reader that does not support the major version named rejects the package rather than reading it as an earlier one.

Any other property goes here as a string, with a key name unlikely to clash with another reader's, such as a prefix of the profile that defines it. A reader ignores `metadata` keys it does not know. A package's own version, where it has one, goes in `metadata.version`, as Agent Skills' examples do.

### Body content

The Markdown body is the overview: enough to answer the commonest questions directly, to orient a newcomer, and to route every other question to the right file. It has one required section:

- **`## Sources`** (required) - where the knowledge comes from, with links or citations, so every claim can be traced. Knowledge drawn from an acquisition's output cites it as any other source, by [external reference](#references-outside-the-package): the output it was taken from and when the acquisition read the source, and, where it helps a reader, the [acquire package](acquire.md) that made it. Knowledge written from the owner's own experience says so. The section is never empty.

Recommended sections:

- **Overview** - the area in a few paragraphs, with the key terms defined once, and what a reader is assumed to know already
- **Contents** - one line per file in the package: what it covers and when to read it, in the order a newcomer would read them where there is one
- **Limits** - what the package does not cover, and known gaps or open questions

Keep `KNOWLEDGE.md` under 500 lines and about 5,000 tokens; move detail into `references/`.

## Optional directories

### `references/`

The body of knowledge itself, where it is factored: Markdown files, each focused on one subtopic, named for its content (`flat-rate-scheme.md`, not `part-2.md`). Split mutually exclusive subtopics so a question loads only what it needs. A file longer than about 100 lines opens with its own contents list, so a partial read still shows its scope. Every file is listed in the overview's Contents.

### `assets/`

Diagrams, images, tables of data and schemas the knowledge refers to.

A knowledge package has no `scripts/`: its focus is knowledge, not action. Executable steps belong in an ordinary skill, or, for acquiring knowledge from a source, in an [acquire package](acquire.md).

## Progressive disclosure

1. **Metadata** (about 100 tokens): `name`, `description` and `metadata.updated`, read for every candidate package to decide which suits the reader and how far to trust its currency
2. **Overview** (under 5,000 tokens recommended): the `KNOWLEDGE.md` body, read once the package is chosen
3. **Body** (as needed): files in `references/` and `assets/`, read only when the Contents line says the reader needs them

## File references

Use relative paths from the package root, one level deep from `KNOWLEDGE.md`: every file is linked from the Contents, and files in `references/` do not depend on chains of further links to be understood. A file may link a sibling for related detail. Such an internal link stays inside the package and must resolve.

### References outside the package

Anything outside the package, such as a document, another package or an acquisition's output cited in Sources, is an external reference, written in one of three forms:

- **A package name**, such as `hmrc-guidance`: it resolves to the package of that name the reader can see, first a sibling directory of this package, then any collection of packages the reader is given
- **A URL**: it resolves as the URL does
- **A relative path that leaves the package**, beginning `../`: it resolves from the directory of the file that holds it, as any relative link does

An external reference must have one of these forms, but validation does not require it to resolve, because what it names lives, moves and ends on its own. A reader that cannot resolve one reports it as unresolved and goes on reading the package.

## Validation

A package is valid when:

- `KNOWLEDGE.md` exists and begins with a YAML front matter mapping
- the front matter has only the fields listed above, `name` and `description` meet their constraints, and `name` matches the directory
- `metadata` maps strings to strings; `metadata.updated`, where present, is a valid `YYYY-MM-DD` date no later than today; `metadata.spec`, where present, is `knowledge/` followed by a major version the reader supports
- the body has a `## Sources` section that is not empty
- every file under `references/` is linked from `KNOWLEDGE.md`, every internal link resolves inside the package, and every external reference has one of the three forms above

There is one level of validity. Size limits are recommendations, warned and never failed. Whether the description routes well and names its audience, the sources support the claims and the content is current are judgements a reviewer makes. No reference validator exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `name`, `description`, `license` and `metadata` with their constraints, and Agent Skills' advice that `metadata` keys be reasonably unique; `references/` and `assets/`; three disclosure tiers with the same budgets; relative file references one level deep.
- **Different, and why:** the entry file is `KNOWLEDGE.md`, in upper case as `SKILL.md` is, which is this specification's rule, not Agent Skills'; the body is condensed knowledge, not instructions, so the package must leave a reader with the scope of its area, what was drawn out and its provenance, its body requires a Sources section and recommends Overview, Contents and Limits, and `references/` is the body proper rather than supporting detail; `metadata.updated` is defined and read in the first tier, because knowledge goes stale and a reader must judge its currency before choosing; `metadata.owner` is defined, so a reader knows who stands behind it; `metadata.spec` is defined, so a reader can tell the version; external references to other packages and evidence are defined, because a package cites the sources it was condensed from, an acquisition's output among them; the description names its audience and depth, because a learner must tell whether a package suits them; `compatibility`, `allowed-tools` and `scripts/` are dropped, because a skill whose focus is knowledge, not action, needs no environment and runs nothing.
- **Skill validity:** every added field sits in `metadata`, so the front matter uses only fields Agent Skills defines; renamed to `SKILL.md`, a conforming package passed the checks `skills-ref validate` made when its source was read on 19 October 2026. It is a skill whose focus is knowledge rather than action.

## Relation to the other specifications

A knowledge package and an [acquire package](acquire.md) are separate extensions of Agent Skills, and neither is a stage of the other: acquire is a skill whose task is acquisition, knowledge one whose focus is what is known. Neither names the other in its `metadata`. A knowledge package may cite an acquisition's output, or the acquire package that made it, in its Sources, as it cites any other source. A [work package](work.md) may cite a knowledge package as the background its worker reads, and the durable findings of a piece of work may be condensed into one.
