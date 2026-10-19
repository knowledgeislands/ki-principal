# Work specification

> The format for a work package: one piece of work, its definition and its current state, packaged so that any person or agent can pick it up.

**Status:** draft 0.2, 19 October 2026. Name `work`. To be held in `ki-work-package` as `references/standards-work-spec.md`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe work packages.

## What a work package is

A work package holds one piece of work that outlasts a single session: what the work is for, where it stands, what it is waiting to have decided, what has been sent to it and what has been decided. It carries current state, not history, so that a reader who has never seen the work can continue it. It is not a transcript, a task list for a whole organisation or a knowledge base; durable knowledge the work produces belongs in a [knowledge package](knowledge.md) or another owning home.

This specification sets the files and what each entry in them carries. It says nothing about how a team works them: who may write, in what order messages are taken, how a question is put or when a decision is pruned are for a team's own profile.

## Directory structure

A work package is a directory containing, at minimum, five files:

```text
work-name/
|-- WORK.md          # Required: metadata + definition
|-- state.md         # Required: where the work stands now
|-- queries.md       # Required: questions waiting to be decided
|-- messages.md      # Required: messages sent to the work, not yet acted on
|-- decisions.md     # Required: decisions the work runs on
|-- references/      # Optional: design notes, reports, briefs
|-- assets/          # Optional: diagrams, templates, data
`-- ...              # Any additional files or directories
```

All five files exist from the moment the package is created, empty or saying `None` until they have content, so that a reader never meets a missing file.

## `WORK.md` format

`WORK.md` is the definition: what the work is and what it is for. It must contain YAML front matter followed by Markdown content. It is read first and changes rarely; it holds no state.

### Front matter

| Field | Required | Constraints |
| - | - | - |
| `name` | Yes | Max 64 characters. Lowercase letters, numbers and hyphens, with `.` allowed between segments. Must match the directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Says what the work does and what it covers. |
| `license` | No | Licence name or reference to a bundled licence file. |
| `compatibility` | No | Max 500 characters. Environment requirements, such as tools or access the work needs. |
| `metadata` | No | A map from string keys to string values. Holds `spec` and any property this specification does not define. |

No other top-level key is allowed.

**Minimal example:**

```markdown
---
name: payroll-migration
description: Moves payroll from the legacy system to the new provider by the April run, covering data mapping, parallel runs and cut-over.
---
```

**Example with optional fields:**

```markdown
---
name: finance.payroll-migration
description: Moves payroll from the legacy system to the new provider by the April run, covering data mapping, parallel runs and cut-over.
compatibility: Needs read access to both payroll systems
metadata:
  spec: "work/1"
  owner: finance-team
  created: "2026-10-19"
---
```

#### `name` field

The required `name` field:

- Must be 1-64 characters
- May only contain lowercase alphanumeric characters (`a-z`, `0-9`), hyphens (`-`) and full stops (`.`)
- Must not start or end with a hyphen or a full stop, and must not contain `--`, `..`, `-.` or `.-`
- Must match the parent directory name

A full stop separates segments when the work sits within larger work, such as `finance.payroll-migration`, so a flat directory of packages can show nesting without nested directories.

**Valid:** `payroll-migration`, `finance.payroll-migration`. **Invalid:** `Payroll-Migration` (uppercase), `.payroll` (leading full stop), `finance..payroll` (empty segment).

#### `description` field

The required `description` field tells a reader what the work is without opening the package.

- Must be 1-1024 characters
- Should say what the work does and what it covers, in words that tell it apart from similar work

**Good:** `Moves payroll from the legacy system to the new provider by the April run, covering data mapping, parallel runs and cut-over.`

**Poor:** `Payroll stuff.`

#### `license` and `compatibility` fields

As Agent Skills.

#### `metadata` field

A map from string keys to string values, as Agent Skills. This specification defines one key:

- `spec` - the specification and major version the package follows, `work/1`. Absent means `work/1`, now and in every later version. A reader that does not support the major version named rejects the package rather than reading it as an earlier one.

Any other property goes here as a string, with a key name unlikely to clash with another reader's, such as a prefix of the profile that defines it. A reader ignores `metadata` keys it does not know. A package's own version, where it has one, goes in `metadata.version`, as Agent Skills' examples do.

### Body content

The Markdown body after the front matter is the definition. Recommended sections:

- `## Goals` - what the work is for, as few goals as it needs
- `## Scope` - what the work covers, and what it leaves to other work

State, next steps and history do not belong in `WORK.md`.

## The other required files

### `state.md`

Where the work stands now. It is rewritten in place at every change of state, never appended to. It must contain YAML front matter followed by Markdown content.

| Field | Required | Constraints |
| - | - | - |
| `state` | Yes | `active`, `waiting`, `on-hold` or `done`. |
| `updated` | Yes | When the state last changed, as UTC RFC 3339. |
| `waiting-on` | When `waiting` | Who or what the work waits on, in words. |
| `release` | When `on-hold` | The condition that ends the hold, in words. |
| `metadata` | No | A map from string keys to string values, for properties this specification does not define. |

No other top-level key is allowed.

- `active` - someone holds the work and the next move is theirs.
- `waiting` - the work has been handed to a named person, piece of work or event, and waits for it.
- `on-hold` - nobody is working it until the release.
- `done` - the work is finished.

A profile may keep a finer state of its own in `metadata`, provided `state` still holds the one of the four it maps to, so that any reader can tell where every package stands.

The body says where the work stands and what whoever picks it up does first. It holds the present only. When the package is under version control, the history of `state.md` is the history of the work; otherwise there is none, by design.

### `queries.md`

Every question the work is waiting to have decided. Each query is a level-three heading, `### <ID> - <title>`, the identifier short and unique within the package, followed by enough context to decide it and the question itself. A query leaves this file when it is decided, and the decision is recorded in `decisions.md`. Other headings, such as sections grouping queries, may appear; a reader treats only level-three headings as queries.

### `messages.md`

Messages sent to the work and not yet acted on: one list item per message, each carrying the date it was sent, who sent it and the message, with any detail linked rather than copied.

```markdown
- 2026-10-19 · finance-lead: Hold the cut-over until the audit closes.
- 2026-10-18 · payroll-team: The February extract is in references/feb-extract.md.
```

A message leaves the file once the work has acted on it. This specification sets no order in which messages are taken; a profile may.

### `decisions.md`

The decisions the work runs on, one entry per decision: a heading with the date and a short title, who decided, and the decision. An entry may be removed once its substance lives in a durable home elsewhere.

## Optional directories

The Agent Skills conventions apply. `references/` holds documents read when another file names them: design notes, reports, briefs to others. `assets/` holds diagrams, templates and data files.

## Progressive disclosure

A work package is read in three tiers, as a skill is:

1. **Metadata** (about 100 tokens): `name` and `description` from `WORK.md` and the `state.md` front matter, read to tell what each package is and where it stands without opening it
2. **Package** (bounded by the size limits below): the `WORK.md` body, then `state.md`, `queries.md`, `messages.md` and `decisions.md`, read in full by whoever takes the work on
3. **Resources** (as needed): `references/` and `assets/`, read only when another file names them

Keep `WORK.md` and each of the other required files under 500 lines and about 5,000 tokens; move detail into `references/`.

## File references

Use relative paths from the package root, one level deep, as Agent Skills does: `See [the cut-over plan](references/cut-over-plan.md).`

## Validation

A package is valid when:

- the directory holds all five required files, and `WORK.md` and `state.md` each begin with a YAML front matter mapping
- `WORK.md` front matter has only the fields listed above, `name` and `description` meet their constraints, and `name` matches the directory
- `metadata`, in either file, maps strings to strings, and `metadata.spec`, where present, is `work/` followed by a major version the reader supports
- `state.md` front matter has only the fields listed above, with a valid `state` and `updated` and with `waiting-on` or `release` where its state requires one
- `WORK.md` carries no state
- every relative link resolves inside the package

There is one level of validity. Size limits are recommendations, warned and never failed. No reference validator exists yet; `skills-ref validate` checks only a `SKILL.md`, and would reject a dotted `name`.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `description`, `license`, `compatibility` and `metadata` with their constraints, and Agent Skills' advice that `metadata` keys be reasonably unique; `references/` and `assets/`; three disclosure tiers; relative file references one level deep; soft size limits.
- **Different, and why:** the entry file is `WORK.md`, in upper case as `SKILL.md` is, which is this specification's rule, not Agent Skills'; five required files rather than one, because a work package carries changing state beside a stable definition and keeping them apart lets the definition stay small and rarely edited; `name` admits `.` between segments, because work nests within larger work, so a work package is never a valid skill; `metadata.spec` is defined, because work packages are long-lived and a reader must tell which version wrote one; the closed list of top-level keys is stated in words, where Agent Skills states it only through its validator; the metadata tier also reads the `state.md` front matter, because where work stands is part of what it is; no `scripts/` or `allowed-tools`, because a work package directs work rather than performing it.

## Relation to the other specifications

A work package may cite a [knowledge package](knowledge.md) as the background its worker reads, or an [acquire package](acquire.md) as the method a piece of its work follows, by relative path or name in any of its files. Neither belongs inside a work package: the work ends, while knowledge and acquisition methods outlast it.
