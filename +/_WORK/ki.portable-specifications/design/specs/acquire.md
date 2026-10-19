# Acquire specification

> The format for an acquire package: how to acquire knowledge from one source or with one tool, faithfully and repeatably, so that what it yields can be curated into a knowledge package.

**Status:** draft 0.2, 19 October 2026. Name `acquire`. To be held in `ki-acquire` as `references/standards-acquire-spec.md`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe acquire packages.

## What an acquire package is

An acquire package is knowledge acquisition itself, not knowledge at rest: the method for getting what a source holds, such as a command-line tool's own help, a documentation site, a meeting-notes service, an issue tracker or a mailbox export. It says what the source is, what may be read and what must never be changed, how to read it, what the output looks like and carries, how to verify it, and what the source cannot give. Running it yields output that someone curates into a [knowledge package](knowledge.md). It holds no captured content and no credentials.

The method's rigour follows its source. Learning a tool from its help needs a short procedure and a light check; capturing a meeting archive or a tracker's history, where every item matters and the source changes, needs complete enumeration, counts and checksums. The required sections are the same for both; what goes in them is proportionate.

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
| `metadata` | Yes | A map from string keys to string values. Must hold `source` and `mutation`; may hold `omissions`, `produces` and `spec`, and any property this specification does not define. |
| `compatibility` | No | Max 500 characters. Tools, accounts and network access the method needs. |
| `license` | No | Licence name or reference to a bundled licence file. |
| `allowed-tools` | No | Space-separated pre-approved tools, as Agent Skills. Experimental. |

No other top-level key is allowed.

**Minimal example**, learning a tool from its own help:

```markdown
---
name: git-help
description: Acquires how to use git from its own command-line help and manual pages, one command at a time, for the version installed. Use to learn or refresh how git commands behave. Not for a repository's history or contents.
metadata:
  source: "git command-line help and man pages, local install"
  mutation: "none"
---
```

**Example with optional fields**, capturing a collection:

```markdown
---
name: tracker-issues
description: Acquires issues, comments and their history from an issue tracker through its read-only API, one project and date window at a time. Use to capture a project's issue history for curation. Not for creating or editing issues.
compatibility: Requires network access to the tracker and a read-only API token in the user's credential store
allowed-tools: Bash(curl:*) Bash(jq:*) Read
metadata:
  source: "Issue tracker REST API, read-only token"
  mutation: "none"
  omissions: "attachments, private-comments, deleted-issues"
  produces: project-history
  spec: "acquire/1"
  version: "1.0"
---
```

#### `name` and `description` fields

As Agent Skills. Name the source and what is taken from it (`tracker-issues`, `git-help`), not the action alone (`importer`). The description should say which source, what knowledge, when to use it and what it does not do, so that a reader choosing between methods for the same source can tell them apart.

#### `compatibility`, `license` and `allowed-tools` fields

As Agent Skills, with `compatibility` usually needed here because acquisition depends on accounts, tools and network access.

#### `metadata` field

A map from string keys to string values, as Agent Skills. This specification defines five keys, each a string:

- `source` (required) - max 200 characters. The source or tool read, and the interface used to read it, such as `Meeting-notes service, official MCP server` or `git command-line help and man pages, local install`. Two packages reading the same source through different interfaces are different methods and say so here.
- `mutation` (required) - `none` or `declared`: what the method may change at the source. `none` means it only reads. `declared` means it makes changes the body's Mutation section lists one by one, each with its confirmation step, such as marking an item as acquired in a private folder. Anything not listed is forbidden; an advertised write operation the source offers grants no permission. Most acquire packages should be `none`.
- `omissions` (recommended) - what the source holds that this method does not capture, such as audio, edit history or deleted items, as one comma-separated list in a single string. Declaring omissions lets the curator and every later reader tell "not captured" from "not there". An omission not declared is a defect in the package.
- `produces` - the name or relative path of the [knowledge package](knowledge.md) this method feeds. The knowledge package names this acquire package back in its `metadata.acquired-with`.
- `spec` - the specification and major version the package follows, `acquire/1`. Absent means `acquire/1`, now and in every later version. A reader that does not support the major version named rejects the package rather than reading it as an earlier one.

Any other property goes here as a string, with a key name unlikely to clash with another reader's, such as a prefix of the profile that defines it. A reader ignores `metadata` keys it does not know. A package's own version, where it has one, goes in `metadata.version`, as Agent Skills' examples do.

### Body content

Unlike a skill's body, an acquire package's body has required sections, because a reader must know the method's guarantees before running it:

- **`## Scope`** (required) - what a run may cover (accounts, projects, commands, date windows, ownership) and what is always out of scope
- **`## Procedure`** (required) - the steps: connect or open the source, find what is in scope, read each part, keep what was read, then verify. Say how the method knows it has found everything in scope; for a collection, enumerate every identity, since an empty listing is not proof the source is empty unless the source says so explicitly
- **`## Output`** (required) - the shape of what a run yields and what each item carries: what it was taken from and when it was read, with the source's own dates, where it has them, kept apart from the reading time. Recommended where the output is kept as evidence or the source changes: the coverage reached for each item (reference, digest, partial or complete) and checksums for exact bytes kept
- **`## Verification`** (required) - how a run shows it is complete and faithful, in proportion to the source: for a tool's help, that the version read is recorded and each command in scope was read; for a collection, reading back what was written and reconciling counts against the source. A run names what was missing or failed rather than claiming success
- **`## Mutation`** (required when `metadata.mutation` is `declared`) - each permitted write and its confirmation
- **`## Repeat runs`** (recommended) - how a later run recognises what it already holds, reuses identities, captures amendments as new versions rather than overwriting, and resumes after interruption
- **`## Access`** (recommended) - how to connect, with credentials kept in the user's own credential store and never written into the package, its output or its logs

Keep `ACQUIRE.md` under 500 lines and about 5,000 tokens; move the source's detailed surface into `references/`.

## Optional directories

### `scripts/`

Executable steps, as Agent Skills: self-contained or with stated dependencies, clear errors, and a dry run for any step that writes. A script must stop rather than continue when the source's responses change shape.

### `references/`

The source's surface in detail: the operations, commands or endpoints used, their limits and paging, field mappings into the output, and known edge cases. One file per concern, loaded when the procedure needs it.

### `assets/`

Templates for output items, schemas, and small fixtures for testing the scripts. Never real captured content.

## Progressive disclosure

1. **Metadata** (about 150 tokens): `name`, `description`, `metadata.source` and `metadata.mutation`, read to choose a method and to see at once whether it can change the source
2. **Method** (under 5,000 tokens recommended): the `ACQUIRE.md` body, read before a run
3. **Resources** (as needed): `references/`, `scripts/` and `assets/`, loaded or run when a procedure step names them

## File references

Use relative paths from the package root, one level deep, as Agent Skills does. Make execution intent explicit: "Run `scripts/list.py`" executes it, "See `scripts/list.py` for the paging rules" reads it.

## Validation

A package is valid when:

- `ACQUIRE.md` exists and begins with a YAML front matter mapping
- the front matter has only the fields listed above, `name` and `description` meet their constraints, and `name` matches the directory
- `metadata` maps strings to strings and holds `source` and `mutation` meeting their constraints; `metadata.spec`, where present, is `acquire/` followed by a major version the reader supports
- the body has the Scope, Procedure, Output and Verification sections, and a Mutation section when `metadata.mutation` is `declared`
- no file in the package holds a credential, token or captured source content
- every relative link resolves inside the package

There is one level of validity. Size limits are recommendations, warned and never failed. Whether the procedure really finds everything in scope, whether its rigour suits the source, and whether the declared omissions are the whole list are judgements a reviewer makes against a trial run. No reference validator exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools` with their constraints, and Agent Skills' advice that `metadata` keys be reasonably unique; `scripts/`, `references/` and `assets/`; three disclosure tiers; relative file references one level deep.
- **Different, and why:** the entry file is `ACQUIRE.md`, in upper case as `SKILL.md` is, which is this specification's rule, not Agent Skills'; `metadata` is required and must hold `source` and `mutation`, because a reader must see what is read and whether the source can be changed before trusting a run, and both are read in the first tier; `metadata.omissions` and `metadata.produces` are defined, so the gaps and the destination are machine-readable; `metadata.spec` is defined so a reader can tell the version; the body has required sections, because completeness, provenance and verification are the guarantees acquisition exists to give; no captured content or credentials may sit in the package.
- **Skill validity:** every added field sits in `metadata`, so the front matter uses only fields Agent Skills defines; renamed to `SKILL.md`, a conforming package passed the checks `skills-ref validate` made when its source was read on 19 October 2026, and is a skill whose task is acquisition.

## Relation to the other specifications

An acquire package produces or refreshes a [knowledge package](knowledge.md): a run's output is curated into it, and the two name each other through `metadata.produces` and `metadata.acquired-with`. A [work package](work.md) may cite an acquire package as the method a piece of its work follows; the method itself outlasts the work.
