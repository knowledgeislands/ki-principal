# Knowledge specification

> The format for a knowledge package: a curated body of knowledge on one topic, described so that a reader can tell whether it is the package that tells them what they want to know, and read progressively.

**Status:** draft 0.3, 20 October 2026. Name `knowledge`. To be held in a new skill, `ki-knowledge-package`, as `references/standards-knowledge-spec.md`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe knowledge packages.

## What a knowledge package is

A knowledge package is knowledge at rest: what is known about a topic, selected, organised and kept current by a named owner who stands behind it. A person or an agent who wants to learn about the topic, or has a question about it, reads its description to decide whether this is the package for them, then its overview, then only the files they need. It is not raw evidence (an acquisition's capture belongs with the [acquire package](acquire.md) that made it), not instructions for performing a task (that is a skill) and not the record of a piece of work (that is a [work package](work.md)).

## Directory structure

A knowledge package is a directory containing, at minimum, a `KNOWLEDGE.md` file:

```text
topic-name/
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
| `metadata` | No | A map from string keys to string values. Holds `updated`, `owner`, `acquired-with` and `spec`, and any property this specification does not define. |

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
  acquired-with: hmrc-guidance
  spec: "knowledge/1"
  version: "2.1"
---
```

Both examples show the front matter only; the body of a conforming package also needs its `## Sources` section.

#### `name` field

As Agent Skills: 1-64 characters; lowercase `a-z`, `0-9` and `-` only; no leading, trailing or consecutive hyphens; matches the parent directory. Name the topic, not the format: `uk-vat-for-freelancers`, not `vat-notes` or `knowledge-1`.

#### `description` field

The required `description` field is the one thing a reader sees before choosing, so it decides whether the package is found and whether the right reader opens it.

- Must be 1-1024 characters
- Should name the topic and its boundaries
- Should say who it is for and at what depth: an introduction for a newcomer, a working guide for a practitioner, or a reference for someone who knows the field
- Should say what a reader can learn or answer with it ("Use to ..." or "Answers ..."), then any close neighbours it does not cover ("Not for ...")
- Should use the words a person asking about the topic would use

**Good:** `Explains UK VAT for sole-trader freelancers, from first principles to working a quarterly return - registration thresholds, flat rate and standard schemes, digital record-keeping and returns. Use to learn how VAT applies to you, decide whether and how to register, or check how a return is worked out. Not for limited companies or import duties.`

**Poor:** `Tax information.`

#### `license` field

As Agent Skills.

#### `metadata` field

A map from string keys to string values, as Agent Skills. This specification defines four keys, each a string:

- `updated` (recommended) - the date someone last checked that the content is still true, `YYYY-MM-DD`, not the date of the last edit. A reader weighs a package by its currency, so `updated` is read with `name` and `description`: an old date says to check before relying on it. A package whose subject changes fast should state its review cadence in the overview.
- `owner` (recommended) - who stands behind the package and keeps it current: a person, team or organisation, in words.
- `acquired-with` - an [external reference](#references-outside-the-package) to the [acquire package](acquire.md) that produces or refreshes this package: its name, a URL or a relative path. A package curated by hand omits it. When present, refreshing the package means running that acquire package again and curating the result.
- `spec` - the specification and major version the package follows, `knowledge/1`. Absent means `knowledge/1`, now and in every later version. A reader that does not support the major version named rejects the package rather than reading it as an earlier one.

Any other property goes here as a string, with a key name unlikely to clash with another reader's, such as a prefix of the profile that defines it. A reader ignores `metadata` keys it does not know. A package's own version, where it has one, goes in `metadata.version`, as Agent Skills' examples do.

### Body content

The Markdown body is the overview: enough to answer the commonest questions directly, to orient a newcomer, and to route every other question to the right file. It has one required section:

- **`## Sources`** (required) - where the knowledge comes from, with links or citations, so every claim can be traced. Content curated from an acquire run names its provenance: the [acquire package](acquire.md) that was run, the run's output it was taken from, and when that run read the source. Knowledge written from the owner's own experience says so. The section is never empty.

Recommended sections:

- **Overview** - the topic in a few paragraphs, with the key terms defined once, and what a reader is assumed to know already
- **Contents** - one line per file in the package: what it covers and when to read it, in the order a newcomer would read them where there is one
- **Limits** - what the package does not cover, and known gaps or open questions

Keep `KNOWLEDGE.md` under 500 lines and about 5,000 tokens; move detail into `references/`.

## Optional directories

### `references/`

The body of knowledge itself: Markdown files, each focused on one subtopic, named for its content (`flat-rate-scheme.md`, not `part-2.md`). Split mutually exclusive subtopics so a question loads only what it needs. A file longer than about 100 lines opens with its own contents list, so a partial read still shows its scope. Every file is listed in the overview's Contents.

### `assets/`

Diagrams, images, tables of data and schemas the knowledge refers to.

A knowledge package has no `scripts/`: it holds knowledge, not procedure. Executable steps for gathering or refreshing it belong in an [acquire package](acquire.md).

## Progressive disclosure

1. **Metadata** (about 100 tokens): `name`, `description` and `metadata.updated`, read for every candidate package to decide which suits the reader and how far to trust its currency
2. **Overview** (under 5,000 tokens recommended): the `KNOWLEDGE.md` body, read once the package is chosen
3. **Body** (as needed): files in `references/` and `assets/`, read only when the Contents line says the reader needs them

## File references

Use relative paths from the package root, one level deep from `KNOWLEDGE.md`: every file is linked from the Contents, and files in `references/` do not depend on chains of further links to be understood. A file may link a sibling for related detail. Such an internal link stays inside the package and must resolve.

### References outside the package

Anything outside the package, such as the [acquire package](acquire.md) that refreshes it, a run's output, or a document cited in Sources, is an external reference, written in one of three forms:

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
- every file under `references/` is linked from `KNOWLEDGE.md`, every internal link resolves inside the package, and every external reference, including `metadata.acquired-with`, has one of the three forms above

There is one level of validity. Size limits are recommendations, warned and never failed. Whether the description routes well and names its audience, the sources support the claims and the content is current are judgements a reviewer makes. No reference validator exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `name`, `description`, `license` and `metadata` with their constraints, and Agent Skills' advice that `metadata` keys be reasonably unique; `references/` and `assets/`; three disclosure tiers with the same budgets; relative file references one level deep.
- **Different, and why:** the entry file is `KNOWLEDGE.md`, in upper case as `SKILL.md` is, which is this specification's rule, not Agent Skills'; the body is knowledge, not instructions, so it requires a Sources section, carrying the provenance of anything curated from an acquire run, and recommends Overview, Contents and Limits, and `references/` is the body proper rather than supporting detail; `metadata.updated` is defined and read in the first tier, because knowledge goes stale and a reader must judge its currency before choosing; `metadata.owner` is defined, so a reader knows who stands behind it; `metadata.acquired-with` is defined, so the method that refreshes the package is discoverable; `metadata.spec` is defined, so a reader can tell the version; external references to other packages and evidence are defined, because a package cites the method and output it was curated from; the description names its audience and depth, because a learner must tell whether a package suits them; `compatibility`, `allowed-tools` and `scripts/` are dropped, because knowledge at rest needs no environment and runs nothing.
- **Skill validity:** every added field sits in `metadata`, so the front matter uses only fields Agent Skills defines; renamed to `SKILL.md`, a conforming package passed the checks `skills-ref validate` made when its source was read on 19 October 2026. It is still not a skill in substance, since its body is knowledge, not instructions.

## Relation to the other specifications

An [acquire package](acquire.md) may produce or refresh a knowledge package. Where that persistent relationship is declared, the knowledge package names the acquire package in `metadata.acquired-with` and the acquire package names it back in `metadata.produces`. A [work package](work.md) may cite a knowledge package as the background its worker reads, and the durable findings of a piece of work may be curated into one.
