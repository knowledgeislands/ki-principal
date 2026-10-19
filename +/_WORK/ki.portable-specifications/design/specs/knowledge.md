# Knowledge specification

> The format for a knowledge package: an Agent Skills extension, a skill into which the knowledge of one area is condensed and factored, described so that a reader can tell whether it is the package that tells them what they want to know, and read progressively.

**Status:** draft 0.6, 20 October 2026. Name `knowledge`. To be held in a new skill, `ki-knowledge-package`, as `references/standards-knowledge-spec.md`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe knowledge packages.

## What a knowledge package is

A knowledge package is, first and foremost, an extension of Agent Skills: a skill into which the knowledge of one area is condensed and factored. Its focus is the knowledge itself, what is known about the area, rather than doing, learning or performing an action, which is what an ordinary skill's instructions are for. It keeps a skill's shape, a directory, an entry file with front matter and progressive disclosure, and changes what the body holds: knowledge condensed to what holds and factored into an overview and focused files, kept current by an owner who stands behind it.

A person or an agent who wants to learn about the area, or has a question about it, reads its description to decide whether this is the package for them, then its overview, then only the files they need. It is not raw evidence (an acquisition's output is a source the package may cite, not part of it), not the method for acquiring knowledge from a source (that is an [acquire package](acquire.md)) and not the record of a piece of work (that is a [work package](work.md)).

### What condensing and factoring leave

Making a knowledge package is condensing and factoring: drawing the knowledge of one area out of wherever it lies, condensing it to what holds, and factoring it into an overview and focused files. This specification sets no workflow for doing so, and there is no separate curation stage. However a package is made, it must leave a reader with three things:

- **The scope of the area:** what the package covers and where it stops. The `description` must name the area and where it stops, and the body must say what lies outside it.
- **What was drawn out:** what the package holds and where. The package's **mapped files** are every file in it, in `references/`, `assets/` or any other directory, except `KNOWLEDGE.md` and a licence file the `license` field names. When there are any, the body must map them, with what they cover; when there are none, what was drawn out is in the body, and no map is needed.
- **Provenance:** where each part came from, in the required [Sources](#body-content) section.

All three are required. The headings under which the body gives its limits and its map are the author's to choose; [Body content](#body-content) recommends them. [Validation](#validation) checks these outcomes where they can be checked, and a reviewer judges them where they cannot.

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
| `name` | Yes | Max 64 characters. Lowercase ASCII letters `a-z`, digits `0-9` and hyphens only. Must not start or end with a hyphen or contain `--`. Must match the directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Names the area and where it stops. Recommended: who it is for, at what depth, and what it answers. |
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

Both examples show the front matter only; the body of a conforming package also needs its `## Sources` section and its limits, and a map when it has mapped files.

#### `name` field

As Agent Skills, except that letters and digits are ASCII only: 1-64 characters; lowercase `a-z`, `0-9` and `-` only; no leading, trailing or consecutive hyphens; matches the parent directory. Agent Skills' text admits Unicode lowercase alphanumeric characters; this specification keeps to `a-z` and `0-9`, its own portability choice, so that a name reads the same on every file system and in every `package:` reference. Name the area, not the format: `uk-vat-for-freelancers`, not `vat-notes` or `knowledge-1`.

#### `description` field

The required `description` field is the one thing a reader sees before choosing, so it decides whether the package is found and whether the right reader opens it.

- Must be 1-1024 characters
- Must name the area it covers and say where it stops, such as by naming close neighbours it does not cover ("Not for ...")
- Should say who it is for and at what depth: an introduction for a newcomer, a working guide for a practitioner, or a reference for someone who knows the field
- Should say what a reader can learn or answer with it ("Use to ..." or "Answers ...")
- Should use the words a person asking about the area would use

The area and where it stops are required; audience, depth, what it answers and wording are recommendations, and a description without them is still valid.

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

The Markdown body is the overview: enough to answer the commonest questions directly, to orient a newcomer, and to route every other question to the right file. It must give its sources and its limits, and a map whenever the package has [mapped files](#what-condensing-and-factoring-leave); the sources go under a fixed heading, the limits and the map under headings of the author's choice:

- **`## Sources`** (required) - where the knowledge comes from, with links or citations, so every claim can be traced. Knowledge drawn from an acquisition's output cites it as any other source, by [external reference](#references-outside-the-package): the output it was taken from and when the acquisition read the source, and, where it helps a reader, the [acquire package](acquire.md) that made it. Knowledge written from the owner's own experience says so. The section is never empty.
- **The limits** (required) - what the package does not cover, with known gaps or open questions. Recommended heading `## Limits`.
- **The map** (required whenever the package has mapped files) - a link to each mapped file, or to a directory that holds it, with a line on what it covers and when to read it, in the order a newcomer would read them where there is one. A link to a directory covers every mapped file in it, and its line says what those files cover together and when to read them; a file in it needs an entry of its own only where that line does not say what the file covers. Recommended heading `## Contents`.

Recommended besides: **`## Overview`** - the area in a few paragraphs, with the key terms defined once, and what a reader is assumed to know already.

Keep `KNOWLEDGE.md` under 500 lines and about 5,000 tokens; move detail into `references/`.

## Optional directories

### `references/`

The body of knowledge itself, where it is factored: Markdown files, each focused on one subtopic, named for its content (`flat-rate-scheme.md`, not `part-2.md`). Split mutually exclusive subtopics so a question loads only what it needs. A file longer than about 100 lines opens with its own contents list, so a partial read still shows its scope. Each mapped file here is covered by the body's map, alone or by its directory.

### `assets/`

Diagrams, images, tables of data and schemas the knowledge refers to. Each mapped file here is covered by the body's map, alone or by its directory.

A knowledge package has no `scripts/`: its focus is knowledge, not action. Executable steps belong in an ordinary skill, or, for acquiring knowledge from a source, in an [acquire package](acquire.md).

## Progressive disclosure

1. **Metadata** (about 100 tokens): `name`, `description` and `metadata.updated`, read for every candidate package to decide which suits the reader and how far to trust its currency
2. **Overview** (under 5,000 tokens recommended): the `KNOWLEDGE.md` body, read once the package is chosen
3. **Body** (as needed): files in `references/`, `assets/` and any other directory, read only when the map says the reader needs them

## File references

A file reference is the target of a Markdown link in any file of the package. It is written in one of three notations, told apart by their form alone, without resolving them:

- **A package name**, `package:` followed by the package's `name`, such as `package:hmrc-guidance`
- **A URL**, beginning with a scheme other than `package:`, such as `https:`
- **A relative path**, anything else, such as `references/flat-rate-scheme.md`; it must not begin with `/`

A fragment, `#` and what follows it, is not part of the reference.

### Relative paths

A relative path resolves from the directory of the file that holds it, as any Markdown link does. In `KNOWLEDGE.md` that directory is the package root, so its map's `[Flat rate scheme](references/flat-rate-scheme.md)` reads as it would in a skill. The resolved path, with its `.` and `..` segments removed, is then classified by where it lands:

- **Internal:** it lands inside the package directory. It must resolve to a file or directory there, whether or not it begins `../`.
- **External:** it lands outside the package directory. It is an external reference.

From `references/flat-rate-scheme.md`, a file one level down:

- `registration.md` lands at `references/registration.md`: internal, and must resolve
- `../assets/flat-rate-percentages.csv` lands at `assets/flat-rate-percentages.csv`: internal, and must resolve, though it begins `../`
- `../../uk-income-tax-for-freelancers/KNOWLEDGE.md` lands outside the package: external

Keep file references one level deep from `KNOWLEDGE.md`: every mapped file is covered by its map, alone or by its directory, and files in `references/` do not depend on chains of further links to be understood. A file may link a sibling for related detail.

### References outside the package

Anything outside the package, such as a document, another package or an acquisition's output cited in Sources, is an external reference: a package name, a URL, or a relative path that lands outside the package.

- **A package name** resolves first to its sibling, the package of that name in the directory that holds this package. Only when there is no sibling does it resolve to the package of that name in any collection of packages the reader is given; if those collections hold more than one, the reader reports the reference as ambiguous, naming the candidates, and resolves it to none of them. `<name>` is 1-64 characters of lowercase ASCII letters `a-z`, digits `0-9`, hyphens and full stops, starting and ending with a letter or digit, with no two of `-` and `.` together, which admits the name of every work, knowledge and acquire package.
- **A URL** resolves as the URL does.
- **A relative path** resolves from the directory of the file that holds it, as above.

An external reference must have one of these forms, but validation does not require it to resolve, because what it names lives, moves and ends on its own. A reader that cannot resolve one, or finds it ambiguous, reports it and goes on reading the package. A Sources entry citing `package:hmrc-guidance` when no package of that name is in sight is well formed, and the package is valid.

## Validation

A package is valid when:

- `KNOWLEDGE.md` exists and begins with a YAML front matter mapping
- the front matter has only the fields listed above, every field present meets its constraints, and `name` matches the directory
- `metadata` maps strings to strings; `metadata.updated`, where present, is a valid `YYYY-MM-DD` date no later than today; `metadata.spec`, where present, is `knowledge/` followed by a major version the reader supports
- the body has a `## Sources` section that is not empty
- every [mapped file](#what-condensing-and-factoring-leave) is linked from the `KNOWLEDGE.md` body, itself or through a link to a directory that holds it
- the package has no `scripts/` directory
- every file reference is a package name, a URL or a relative path in the forms above; every relative path that lands inside the package resolves there

There is one level of validity. Size limits are recommendations, warned and never failed. A reviewer judges what cannot be checked by machine: that the description names the area and where it stops; that the body states what lies outside the area; that the map says what each mapped file covers, alone or in its directory's line; that each part of the knowledge can be traced through Sources to where it came from, and the sources support the claims; and that the content is current. Whether the description says its audience, depth and what it answers is a recommendation a reviewer may advise on, never a ground for invalidity. No reference validator for this specification exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `description`, `license` and `metadata` with their constraints, `name`'s length, hyphen and directory rules, and Agent Skills' advice that `metadata` keys be reasonably unique; `references/` and `assets/`; three disclosure tiers with the same budgets; file references one level deep.
- **Different, and why:** the entry file is `KNOWLEDGE.md`, in upper case as `SKILL.md` is, which is this specification's rule, not Agent Skills'; the body is condensed knowledge, not instructions, so the package must leave a reader with the scope of its area, what was drawn out and its provenance: its description must say where the area stops, its body requires a Sources section, a statement of its limits and a map of its mapped files, under recommended headings, and `references/` is the body proper rather than supporting detail; `metadata.updated` is defined and read in the first tier, because knowledge goes stale and a reader must judge its currency before choosing; `metadata.owner` is defined, so a reader knows who stands behind it; `metadata.spec` is defined, so a reader can tell the version; a relative path resolves from the directory of the file that holds it rather than from the package root, which gives the same target in `KNOWLEDGE.md` and lets a link in a nested file work in any Markdown viewer; external references to other packages and evidence are defined, in three notations a validator tells apart by form, because a package cites the sources it was condensed from, an acquisition's output among them; the description is recommended to name its audience, depth and what it answers, because a learner must tell whether a package suits them; `name`'s letters and digits are ASCII `a-z` and `0-9` only, where Agent Skills' text admits Unicode lowercase alphanumeric characters, so that a name reads the same on every file system and in every `package:` reference; `compatibility`, `allowed-tools` and `scripts/` are dropped, because a skill whose focus is knowledge, not action, needs no environment and runs nothing.
- **Skill validity:** every added field sits in `metadata`, so the front matter uses only fields Agent Skills defines, and a conforming name is a valid skill name; renamed to `SKILL.md`, a conforming package is a valid skill under the Agent Skills specification, one whose focus is knowledge rather than action. That is a claim about the format. Of `skills-ref`, the reference validator Agent Skills links, which its README calls a demonstration not meant for production, this specification claims only what inspecting its source as read on 19 October 2026 supports, without running it: its field checks accept the front matter of the examples above, written as shown. Its parser is narrower than the format: it reads the front matter with `strictyaml`, a subset of YAML, and ends it at the first `---` after the opening one wherever that falls, so a value holding three hyphens in a row, which this specification allows, cuts the front matter short and the package fails to parse there. That is a limit of the validator; this specification does not narrow its values to suit it.

## Relation to the other specifications

A knowledge package and an [acquire package](acquire.md) are separate extensions of Agent Skills, and neither is a stage of the other: acquire is a skill whose task is acquisition, knowledge one whose focus is what is known. Neither specification defines or requires a `metadata` field linking a package to the other kind; a profile's own `metadata` keys are not restricted by this. A knowledge package may cite an acquisition's output, or the acquire package that made it, in its Sources, as it cites any other source. A [work package](work.md) may cite a knowledge package as the background its worker reads, and the durable findings of a piece of work may be condensed into one.
