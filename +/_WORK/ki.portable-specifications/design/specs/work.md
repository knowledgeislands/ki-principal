# Work specification

> The format for a work package: one piece of work, its definition and its current state, packaged so that any person or agent can pick it up.

**Status:** draft 0.1, 19 October 2026. Name `work`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

## What a work package is

A work package holds one piece of work that outlasts a single session: what the work is for, where it stands, what it is waiting to decide, what has been asked of it and what has been decided. It carries current state, not history, so that a reader who has never seen the work can continue it. It is not a transcript, a task list for a whole organisation or a knowledge base; durable knowledge the work produces belongs in a [knowledge package](knowledge.md) or another owning home.

## Directory structure

A work package is a directory containing, at minimum, five files:

```text
work-name/
|-- WORK.md          # Required: metadata + definition
|-- state.md         # Required: where the work stands now
|-- queries.md       # Required: open and parked questions
|-- messages.md      # Required: incoming queue, in priority order
|-- decisions.md     # Required: decisions log
|-- references/      # Optional: design notes, reports, briefs
|-- assets/          # Optional: diagrams, templates, data
`-- ...              # Any additional files or directories
```

All five files exist from the moment the package is created, each saying `None` until it has content, so that a reader never meets a missing file and a sender never has to create one.

## `WORK.md` format

`WORK.md` is the definition: what the work is, its goals and what it takes. It must contain YAML front matter followed by Markdown content. It is read first and changes rarely; it holds no state.

### Front matter

| Field | Required | Constraints |
| - | - | - |
| `name` | Yes | Max 64 characters. Lowercase letters, numbers and hyphens, with `.` allowed between segments. Must match the directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Says what the work does, what it takes and what it is not for. |
| `spec` | No | The specification and major version the package follows, `work/1`. Absent means `work/1`. |
| `license` | No | Licence name or reference to a bundled licence file. |
| `compatibility` | No | Max 500 characters. Environment requirements, such as tools or access the work needs. |
| `metadata` | No | A map from string keys to string values, for properties this specification does not define. |

**Minimal example:**

```markdown
---
name: payroll-migration
description: Moves payroll from the legacy system to the new provider by the April run. Takes data mapping, parallel runs and cut-over tasks. Not for pension scheme changes (pensions-review).
---
```

**Example with optional fields:**

```markdown
---
name: finance.payroll-migration
description: Moves payroll from the legacy system to the new provider by the April run. Takes data mapping, parallel runs and cut-over tasks. Not for pension scheme changes (finance.pensions-review).
spec: work/1
metadata:
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

The required `description` field is the routing signal: someone with a new unit of work reads the descriptions of the packages they could send it to and picks one.

- Must be 1-1024 characters
- Should say what the work does, then the kinds of unit it takes, then what it is not for, naming the neighbouring work by name
- Should be tested against a handful of units that could plausibly go to more than one package

**Good:** `Moves payroll from the legacy system to the new provider by the April run. Takes data mapping, parallel runs and cut-over tasks. Not for pension scheme changes (pensions-review).`

**Poor:** `Payroll stuff.`

A package that is winding down says so in its description ("Not taking new units") rather than through a separate flag.

#### `spec`, `license`, `compatibility` and `metadata` fields

`license`, `compatibility` and `metadata` keep the Agent Skills meaning. `spec` names the specification version so that a reader can tell a package written to a later major version. A reader ignores top-level keys it does not know, so a local profile may add its own fields; a profile should prefix them, or put them in `metadata`, to avoid clashing with a later version of this specification.

### Body content

The Markdown body after the front matter is the definition. Recommended sections:

- `## Goals` - the standing goals, stable across the work's phases, as few as it needs
- `## Scope` - `In:` and `Out:` lines naming what the work takes and which other work takes the rest

Keep the body under about 300 words. State, next steps, evidence and history do not belong in `WORK.md`.

## Pick-up files

### `state.md`

Where the work stands now. It is rewritten in place at every change of state, never appended to.

| Field | Required | Constraints |
| - | - | - |
| `state` | Yes | `active`, `waiting`, `on-hold` or `done`. |
| `updated` | Yes | When the state last changed, as UTC RFC 3339. |
| `waiting-on` | When `waiting` | Who or what the work waits on, in words. |
| `release` | When `on-hold` | The condition that ends the hold, in words. |

`active` means someone is working it; `waiting` that it waits on a named person, decision or event; `on-hold` that nobody is working it until the release; `done` that it is finished and its package may be removed. A profile may record a finer state in a field of its own, provided `state` still holds the one of the four it maps to, so that any reader can tell where every package stands.

Recommended body sections: `## Now` (at most five lines, the present only), `## Next steps` (numbered, what the next person to pick it up does first) and `## Held` (items waiting on a named condition). Keep the body under about 400 words. When the package is under version control, the history of `state.md` is the history of the work; otherwise there is none, by design.

### `queries.md`

Every question the work is waiting to have decided, in full, under `## Open` and `## Parked`. Each query is a level-three heading `### <TAG> - <title>`, the tag a short, stable, upper-case mnemonic, followed by its context, the question in one sentence and its options, the recommended option first with its reason. Parking moves a query under `## Parked` with the condition for bringing it back. An answered query leaves this file in the same change that records the answer in `decisions.md`.

### `messages.md`

The work's incoming queue: one list item per message sent to the work.

```markdown
- IMPORTANT · 2026-10-19 · SCOPE-CHANGE · finance-lead: Hold the cut-over until the audit closes.
- 2026-10-18 · TEST-DATA · payroll-team: The February extract is in references/feb-extract.md.
```

- **Order:** lines stand in priority order, top first. A sender appends an ordinary line at the end, unless it is the one who sets priority, which may place a line where its priority warrants.
- **Important lines:** a line beginning `IMPORTANT` goes at the top, below any important lines already there. The worker takes important lines first, in their order, one at a time, never grouping or reordering them. This is how whoever directs the work changes how it is done.
- **Grouping:** below the important lines, the worker takes the queue from the top and may group similar lines into one unit, naming each line it groups.
- **Writers:** a sender adds or replaces only its own line and edits nothing else in the package. Only the work removes a line, once it has acted on it and recorded the outcome where it lands.
- A line stays short, about 60 words, with detail linked rather than copied. The tag is optional.

### `decisions.md`

The decisions the work runs on, one entry per decision: a heading with the date, time and a short title; who decided; the decision in their own words where they gave them; and how it was taken and what it authorises. An entry whose substance now lives in a durable home elsewhere may be reduced to a one-line pointer to that home, or removed. Keep the file under about 400 lines.

## Optional directories

The Agent Skills conventions apply. `references/` holds documents read when the pick-up files name them: design notes, run or progress reports, briefs to others. Remove each once its outcome has a home. `assets/` holds diagrams, templates and data files. Scripts and tool output do not belong in a work package; they belong with the work's product.

## Progressive disclosure

A work package is read in four tiers rather than three, because routing and picking up are different readers:

1. **Register** (about 100 tokens): `name`, `description` and the `state.md` front matter, read by whoever routes new work or lists all work
2. **Definition** (under 300 words): the `WORK.md` body, read when two descriptions both match, or before picking the work up
3. **Pick-up** (bounded by the size limits above): `state.md`, `messages.md`, `queries.md` and `decisions.md`, read in full by whoever takes the work on, messages first
4. **Resources** (as needed): `references/` and `assets/`, read only when a pick-up file names them

A sender reads nothing in the receiving package: it adds a line to `messages.md`.

## File references

Use relative paths from the package root, one level deep, as Agent Skills does: `See [the cut-over plan](references/cut-over-plan.md).` A pick-up file links a report rather than copying its evidence.

## Validation

A package is valid when:

- the directory holds all five required files, and `WORK.md` begins with a YAML front matter mapping
- `name` and `description` meet their constraints, and `name` matches the directory
- `state.md` front matter has a valid `state` and `updated`, with `waiting-on` or `release` where its state requires one
- `WORK.md` carries no state field and no `Next steps` section
- every important line in `messages.md` stands above every ordinary line
- every relative link resolves inside the package

Size limits are recommendations, warned and never failed. No reference validator exists yet; `skills-ref validate` checks only a `SKILL.md`.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an upper-case entry file with YAML front matter and a Markdown body; `description`, `license`, `compatibility` and `metadata` with their constraints; `references/` and `assets/`; relative file references one level deep; soft size limits.
- **Different, and why:** five required files rather than one, because a work package carries changing state beside a stable definition and keeping them apart lets the definition stay small and rarely edited; `name` admits `.` between segments, because work nests within larger work; an optional `spec` field, because work packages are long-lived and a reader must tell which version wrote one; four disclosure tiers, because routing reads only the register; no `scripts/` or `allowed-tools`, because a work package directs work rather than performing it.

## Relation to the other specifications

A work package may cite a [knowledge package](knowledge.md) as the background its worker reads, or an [acquire package](acquire.md) as the method a unit of work follows, by relative path or name in `WORK.md`, `state.md` or a message. Neither belongs inside a work package: a work package is removed when the work is done, while knowledge and acquisition methods outlast it.
