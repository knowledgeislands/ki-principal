# Knowledge specification

> The format for a knowledge package: a curated body of knowledge on one topic, described so that a reader can tell whether it answers their question, and read progressively.

**Status:** draft 0.1, 19 October 2026. Name `knowledge`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

## What a knowledge package is

A knowledge package is knowledge at rest: what is known about a topic, selected, organised and kept current by someone who stands behind it. A person or an agent with a question reads its description to decide whether this is the package that answers it, then its overview, then only the files the question needs. It is not raw evidence (an acquisition's capture belongs with the [acquire package](acquire.md) that made it), not instructions for performing a task (that is a skill) and not the record of a piece of work (that is a [work package](work.md)).

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
| `description` | Yes | Max 1024 characters. Non-empty. Says what the knowledge covers and which questions it answers. |
| `updated` | No | The date the content was last checked as current, `YYYY-MM-DD`. Recommended. |
| `acquired-with` | No | Name or relative path of the [acquire package](acquire.md) that produces or refreshes this package. |
| `spec` | No | The specification and major version the package follows, `knowledge/1`. Absent means `knowledge/1`. |
| `license` | No | Licence name or reference to a bundled licence file. |
| `metadata` | No | A map from string keys to string values, for properties this specification does not define. |

**Minimal example:**

```markdown
---
name: uk-vat-for-freelancers
description: Explains UK VAT for sole-trader freelancers - registration thresholds, flat rate and standard schemes, digital record-keeping and quarterly returns. Use to decide whether and how to register, or how a return is worked out. Not for limited companies or import duties.
---
```

**Example with optional fields:**

```markdown
---
name: uk-vat-for-freelancers
description: Explains UK VAT for sole-trader freelancers - registration thresholds, flat rate and standard schemes, digital record-keeping and quarterly returns. Use to decide whether and how to register, or how a return is worked out. Not for limited companies or import duties.
updated: 2026-10-19
acquired-with: hmrc-guidance
license: CC-BY-4.0
metadata:
  owner: accounts-team
  version: "2.1"
---
```

#### `name` field

As Agent Skills: 1-64 characters; lowercase `a-z`, `0-9` and `-` only; no leading, trailing or consecutive hyphens; matches the parent directory. Name the topic, not the format: `uk-vat-for-freelancers`, not `vat-notes` or `knowledge-1`.

#### `description` field

The required `description` field is the one thing a reader sees before choosing, so it decides whether the package is found.

- Must be 1-1024 characters
- Should name the topic and its boundaries, then the questions it answers ("Use to ..." or "Answers ..."), then any close neighbours it does not cover ("Not for ...")
- Should use the words a person asking the question would use

**Good:** `Explains UK VAT for sole-trader freelancers - registration thresholds, flat rate and standard schemes, digital record-keeping and quarterly returns. Use to decide whether and how to register, or how a return is worked out. Not for limited companies or import duties.`

**Poor:** `Tax information.`

#### `updated` field

The date someone last checked that the content is still true, not the date of the last edit. A reader weighs a package by its currency: an old date says to check before relying on it. A package whose subject changes fast should state its review cadence in the body.

#### `acquired-with` field

Links the package to the method that keeps it current. A package curated by hand omits it. When present, refreshing the package means running that acquire package again and curating the result.

#### `spec`, `license` and `metadata` fields

`license` and `metadata` keep the Agent Skills meaning; a package's own version, where it has one, goes in `metadata.version`. `spec` names the specification version. A reader ignores top-level keys it does not know; a local profile should prefix its own or put them in `metadata`.

### Body content

The Markdown body is the overview: enough to answer the commonest questions directly and to route every other question to the right file. Recommended sections:

- **Overview** - the topic in a few paragraphs, with the key terms defined once
- **Contents** - one line per file in the package: what it covers and when to read it
- **Sources** - where the knowledge comes from, with links or citations, so every claim can be traced
- **Limits** - what the package does not cover, and known gaps or open questions

Keep `KNOWLEDGE.md` under 500 lines and about 5,000 tokens; move detail into `references/`.

## Optional directories

### `references/`

The body of knowledge itself: Markdown files, each focused on one subtopic, named for its content (`flat-rate-scheme.md`, not `part-2.md`). Split mutually exclusive subtopics so a question loads only what it needs. A file longer than about 100 lines opens with its own contents list, so a partial read still shows its scope. Every file is listed in the overview's Contents.

### `assets/`

Diagrams, images, tables of data and schemas the knowledge refers to.

A knowledge package has no `scripts/`: it holds knowledge, not procedure. Executable steps for gathering or refreshing it belong in an [acquire package](acquire.md).

## Progressive disclosure

1. **Metadata** (about 100 tokens): `name` and `description`, read for every candidate package to decide which answers the question
2. **Overview** (under 5,000 tokens recommended): the `KNOWLEDGE.md` body, read once the package is chosen
3. **Body** (as needed): files in `references/` and `assets/`, read only when the Contents line says the question needs them

## File references

Use relative paths from the package root, one level deep from `KNOWLEDGE.md`: every file is linked from the Contents, and files in `references/` do not depend on chains of further links to be understood. A file may link a sibling for related detail.

## Validation

A package is valid when:

- `KNOWLEDGE.md` exists and begins with a YAML front matter mapping
- `name` and `description` meet their constraints, and `name` matches the directory
- `updated`, where present, is a valid date no later than today
- every file under `references/` is linked from `KNOWLEDGE.md`, and every relative link resolves inside the package

Size limits are recommendations, warned and never failed. Whether the description routes well, the sources support the claims and the content is current are judgements a reviewer makes. No reference validator exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an upper-case entry file with YAML front matter and a Markdown body; `name`, `description`, `license` and `metadata` with their constraints; `references/` and `assets/`; three disclosure tiers with the same budgets; relative file references one level deep.
- **Different, and why:** the body is knowledge, not instructions, so its recommended sections are Overview, Contents, Sources and Limits, and `references/` is the body proper rather than supporting detail; `updated` is added because knowledge goes stale and a reader must judge its currency; `acquired-with` is added so the method that refreshes the package is discoverable; `spec` is added so a reader can tell the version; `compatibility`, `allowed-tools` and `scripts/` are dropped, because knowledge at rest needs no environment and runs nothing. Renamed `KNOWLEDGE.md` to `SKILL.md`, a conforming package is also a valid skill.

## Relation to the other specifications

An [acquire package](acquire.md) produces or refreshes a knowledge package, and the knowledge package names it in `acquired-with`. A [work package](work.md) may cite a knowledge package as the background its worker reads; the work's durable findings are curated into a knowledge package before the work package is removed.
