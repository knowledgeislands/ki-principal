# Acquire specification

> The format for an acquire package: how to acquire knowledge from one source or with one tool, faithfully and repeatably, so that what it yields can be curated into a knowledge package.

**Status:** draft 0.1, 19 October 2026. Name `acquire`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

## What an acquire package is

An acquire package is knowledge acquisition itself, not knowledge at rest: the method for getting what a source holds, such as a meeting-notes service, an issue tracker, a documentation site, a mailbox export or a command-line tool's own help. It says what the source is, what may be read and what must never be changed, how to enumerate and read it completely, what the output looks like and carries, how to verify it, and what the source cannot give. Running it yields a capture that someone curates into a [knowledge package](knowledge.md). It holds no captured content and no credentials.

## Directory structure

An acquire package is a directory containing, at minimum, an `ACQUIRE.md` file:

```text
source-name/
|-- ACQUIRE.md       # Required: metadata + the acquisition method
|-- scripts/         # Optional: executable steps (list, read, verify)
|-- references/      # Optional: the source's surface, field mappings, edge cases
|-- assets/          # Optional: output templates, schemas, sample fixtures
`-- ...              # Any additional files or directories
```

## `ACQUIRE.md` format

The `ACQUIRE.md` file must contain YAML front matter followed by Markdown content.

### Front matter

| Field | Required | Constraints |
| - | - | - |
| `name` | Yes | Max 64 characters. Lowercase letters, numbers and hyphens only. Must not start or end with a hyphen. Must match the directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Says which source it reads, what knowledge it yields and when to use it. |
| `source` | Yes | Max 200 characters. The source or tool read, and the interface used to read it. |
| `mutation` | Yes | `none` or `declared`. |
| `omissions` | No | A list of what the source holds but this method does not capture. Recommended. |
| `produces` | No | Name or relative path of the [knowledge package](knowledge.md) this method produces or refreshes. |
| `spec` | No | The specification and major version the package follows, `acquire/1`. Absent means `acquire/1`. |
| `compatibility` | No | Max 500 characters. Tools, accounts and network access the method needs. |
| `license` | No | Licence name or reference to a bundled licence file. |
| `metadata` | No | A map from string keys to string values, for properties this specification does not define. |
| `allowed-tools` | No | Space-separated pre-approved tools, as Agent Skills. Experimental. |

**Minimal example:**

```markdown
---
name: tracker-issues
description: Acquires issues, comments and their history from an issue tracker through its read-only API, one project and date window at a time. Use to capture a project's issue history for curation. Not for creating or editing issues.
source: Issue tracker REST API, read-only token
mutation: none
---
```

**Example with optional fields:**

```markdown
---
name: tracker-issues
description: Acquires issues, comments and their history from an issue tracker through its read-only API, one project and date window at a time. Use to capture a project's issue history for curation. Not for creating or editing issues.
source: Issue tracker REST API, read-only token
mutation: none
omissions: [attachments, private-comments, deleted-issues]
produces: project-history
compatibility: Requires network access to the tracker and a read-only API token in the user's credential store
allowed-tools: Bash(curl:*) Bash(jq:*) Read
metadata:
  version: "1.0"
---
```

#### `name` and `description` fields

As Agent Skills. Name the source and what is taken from it (`tracker-issues`, `meeting-notes`), not the action alone (`importer`). The description should say which source, what knowledge, when to use it and what it does not do, so that a reader choosing between methods for the same source can tell them apart.

#### `source` field

The source and the interface through which it is read, such as `Meeting-notes service, official MCP server` or `git command-line help and man pages`. Two packages reading the same source through different interfaces are different methods and say so here.

#### `mutation` field

What the method may change at the source. `none` means it only reads. `declared` means it makes changes the body's Mutation section lists one by one, each with its confirmation step, such as marking an item as acquired in a private folder. Anything not listed is forbidden; an advertised write operation the source offers grants no permission. Most acquire packages should be `none`.

#### `omissions` field

What the source holds that this method does not capture, such as audio, edit history or deleted items. Declaring omissions lets the curator and every later reader tell "not captured" from "not there". An omission not declared is a defect in the package.

#### `produces` field

The knowledge package this method feeds. The knowledge package names this acquire package back in its `acquired-with` field.

#### `spec`, `compatibility`, `license`, `metadata` and `allowed-tools` fields

As Agent Skills, with `compatibility` usually needed here because acquisition depends on accounts, tools and network access. `spec` names the specification version. A reader ignores top-level keys it does not know; a local profile should prefix its own or put them in `metadata`.

### Body content

Unlike a skill's body, an acquire package's body has required sections, because a reader must know the method's guarantees before running it:

- **`## Scope`** (required) - what an authorised run may cover (accounts, projects, date windows, ownership) and what is always out of scope
- **`## Procedure`** (required) - the steps: connect, enumerate every identity in scope, read each, preserve, then verify. An empty listing is not proof the source is empty unless the source says so explicitly
- **`## Output`** (required) - the shape of what a run yields and what each item carries: the source identity, the source's own dates kept apart from the capture time, the coverage reached (reference, digest, partial or complete) and checksums for exact bytes kept
- **`## Verification`** (required) - how a run proves it is complete: reading back what was written, reconciling counts against the source, and naming what was missing or failed rather than claiming success
- **`## Mutation`** (required when `mutation` is `declared`) - each permitted write and its confirmation
- **`## Repeat runs`** (recommended) - how a later run recognises what it already holds, reuses identities, captures amendments as new versions rather than overwriting, and resumes after interruption
- **`## Access`** (recommended) - how to connect, with credentials kept in the user's own credential store and never written into the package, its output or its logs

Keep `ACQUIRE.md` under 500 lines and about 5,000 tokens; move the source's detailed surface into `references/`.

## Optional directories

### `scripts/`

Executable steps, as Agent Skills: self-contained or with stated dependencies, clear errors, and a dry run for any step that writes. A script must stop rather than continue when the source's responses change shape.

### `references/`

The source's surface in detail: the operations or endpoints used, their limits and paging, field mappings into the output, and known edge cases. One file per concern, loaded when the procedure needs it.

### `assets/`

Templates for output items, schemas, and small fixtures for testing the scripts. Never real captured content.

## Progressive disclosure

1. **Metadata** (about 150 tokens): `name`, `description`, `source` and `mutation`, read to choose a method and to see at once whether it can change the source
2. **Method** (under 5,000 tokens recommended): the `ACQUIRE.md` body, read before a run
3. **Resources** (as needed): `references/`, `scripts/` and `assets/`, loaded or run when a procedure step names them

## File references

Use relative paths from the package root, one level deep, as Agent Skills does. Make execution intent explicit: "Run `scripts/list.py`" executes it, "See `scripts/list.py` for the paging rules" reads it.

## Validation

A package is valid when:

- `ACQUIRE.md` exists and begins with a YAML front matter mapping
- `name`, `description`, `source` and `mutation` meet their constraints, and `name` matches the directory
- the body has the Scope, Procedure, Output and Verification sections, and a Mutation section when `mutation` is `declared`
- no file in the package holds a credential, token or captured source content
- every relative link resolves inside the package

Whether the procedure really enumerates the source completely, and whether the declared omissions are the whole list, are judgements a reviewer makes against a trial run. No reference validator exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an upper-case entry file with YAML front matter and a Markdown body; `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools` with their constraints; `scripts/`, `references/` and `assets/`; three disclosure tiers; relative file references one level deep. An acquire package is a skill whose task is acquisition.
- **Different, and why:** `source` and `mutation` are required, because a reader must see what is read and whether the source can be changed before trusting a run; `omissions` and `produces` are added, so the gaps and the destination are machine-readable; the body has required sections, because completeness, provenance and verification are the guarantees acquisition exists to give; `spec` is added so a reader can tell the version; no captured content or credentials may sit in the package.

## Relation to the other specifications

An acquire package produces or refreshes a [knowledge package](knowledge.md): a run's output is curated into it, and the two name each other through `produces` and `acquired-with`. A [work package](work.md) may cite an acquire package as the method one of its units follows, and records each run's outcome in its own state; the method itself outlasts the work.
