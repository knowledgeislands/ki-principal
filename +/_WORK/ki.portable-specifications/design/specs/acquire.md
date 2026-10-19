# Acquire specification

> The format for an acquire package: how to acquire knowledge from one source or with one tool, faithfully and repeatably, so that what it yields can be traced and relied on.

**Status:** draft 0.5, 20 October 2026. Name `acquire`. To be held in `ki-acquire` as `references/standards-acquire-spec.md`. Follows the [Agent Skills specification](https://agentskills.io/specification); see [Relation to Agent Skills](#relation-to-agent-skills).

Structure and some wording adapted from the [Agent Skills specification](https://agentskills.io/specification), originally developed by Anthropic and published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); changed to describe acquire packages.

## What an acquire package is

An acquire package is knowledge acquisition itself, not knowledge at rest: the method for getting what a source holds, such as a command-line tool's own help, a documentation site, a meeting-notes service, an issue tracker or a mailbox export. It says what the source is, what may be read and what must never be changed, how to read it, what the output looks like and carries, how to verify it, and what the source cannot give. Running it yields output whose provenance is kept, so that whatever relies on it can trace it; a [knowledge package](knowledge.md) may cite it among its Sources, as it cites any other source. It holds no captured content and no credentials.

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
| `name` | Yes | Max 64 characters. Lowercase letters, numbers and hyphens only. Must not start or end with a hyphen or contain `--`. Must match the directory name. |
| `description` | Yes | Max 1024 characters. Non-empty. Says which source it reads, what knowledge it yields and when to use it. |
| `metadata` | Yes | A map from string keys to string values. Must hold `source` and `mutation`; may hold `omissions` and `spec`, and any property this specification does not define. |
| `compatibility` | No | Max 500 characters. Non-empty if present. Tools, accounts and network access the method needs. |
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
description: Acquires issues, comments and their history from an issue tracker through its read-only API, one project and date window at a time. Use to capture a project's issue history. Not for creating or editing issues.
compatibility: Requires network access to the tracker and a read-only API token in the user's credential store
allowed-tools: Bash(curl:*) Bash(jq:*) Read
metadata:
  source: "Issue tracker REST API, read-only token"
  mutation: "none"
  omissions: "attachments, private-comments, deleted-issues"
  spec: "acquire/1"
  version: "1.0"
---
```

#### `name` field

The required `name` field, as Agent Skills:

- Must be 1-64 characters
- May only contain lowercase alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`)
- Must not start or end with a hyphen, and must not contain `--`
- Must match the parent directory name

Name the source and what is taken from it (`tracker-issues`, `git-help`), not the action alone (`importer`). **Invalid:** `Git-Help` (uppercase), `-git-help` (leading hyphen), `git--help` (consecutive hyphens).

#### `description` field

The required `description` field must be 1-1024 characters. It should say which source, what knowledge, when to use it and what it does not do, so that a reader choosing between methods for the same source can tell them apart.

#### `compatibility`, `license` and `allowed-tools` fields

As Agent Skills: `compatibility`, where present, is 1-500 characters, and `allowed-tools` is one string of space-separated tool names. `compatibility` is usually needed here because acquisition depends on accounts, tools and network access.

#### `metadata` field

A map from string keys to string values, as Agent Skills. This specification defines four keys, each a string:

- `source` (required) - max 200 characters. The source or tool read, and the interface used to read it, such as `Meeting-notes service, official MCP server` or `git command-line help and man pages, local install`. Two packages reading the same source through different interfaces are different methods and say so here.
- `mutation` (required) - `none` or `declared`: what the method may change at the source. `none` means it only reads. `declared` means it makes changes the body's Mutation section lists one by one, each with its confirmation step, such as marking an item as acquired in a private folder. Anything not listed is forbidden; an advertised write operation the source offers grants no permission. Most acquire packages should be `none`.
- `omissions` (recommended) - what the source holds that this method does not capture, such as audio, edit history or deleted items, as one comma-separated list in a single string. Declaring omissions lets every later reader tell "not captured" from "not there". An omission not declared is a defect in the package.
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

Executable steps. As Agent Skills recommends, a script is self-contained or documents its dependencies, gives helpful error messages and handles edge cases gracefully. This specification adds two requirements of its own: a script offers a dry run for any step that writes, and stops rather than continues when the source's responses change shape.

### `references/`

The source's surface in detail: the operations, commands or endpoints used, their limits and paging, field mappings into the output, and known edge cases. One file per concern, loaded when the procedure needs it.

### `assets/`

Templates for output items, schemas, and small fixtures for testing the scripts. Never real captured content.

## Progressive disclosure

1. **Metadata** (about 150 tokens): `name`, `description`, `metadata.source` and `metadata.mutation`, read to choose a method and to see at once whether it can change the source
2. **Method** (under 5,000 tokens recommended): the `ACQUIRE.md` body, read before a run
3. **Resources** (as needed): `references/`, `scripts/` and `assets/`, loaded or run when a procedure step names them

## File references

A file reference is the target of a Markdown link in any file of the package. It is written in one of three notations, told apart by their form alone, without resolving them:

- **A package name**, `package:` followed by the package's `name`, such as `package:git-help`
- **A URL**, beginning with a scheme other than `package:`, such as `https:`
- **A relative path**, anything else, such as `references/endpoints.md`; it must not begin with `/`

A fragment, `#` and what follows it, is not part of the reference. Make execution intent explicit: "Run `scripts/list.py`" executes it, "See `scripts/list.py` for the paging rules" reads it; a path named so follows the same rules as a link's.

### Relative paths

A relative path resolves from the directory of the file that holds it, as any Markdown link does. In `ACQUIRE.md` that directory is the package root, so `See [the endpoints](references/endpoints.md).` reads as it would in a skill. The resolved path, with its `.` and `..` segments removed, is then classified by where it lands:

- **Internal:** it lands inside the package directory. It must resolve to a file or directory there, whether or not it begins `../`.
- **External:** it lands outside the package directory. It is an external reference.

From `references/endpoints.md`, a file one level down:

- `paging.md` lands at `references/paging.md`: internal, and must resolve
- `../assets/issue-schema.json` lands at `assets/issue-schema.json`: internal, and must resolve, though it begins `../`
- `../../tracker-attachments/ACQUIRE.md` lands outside the package: external

Keep file references one level deep from `ACQUIRE.md`, as Agent Skills does: name what a procedure step needs from `ACQUIRE.md` directly, not through chains of further links.

### References outside the package

Anything outside the package, such as the place a run's output is kept, the source's own documentation or another acquire package, is an external reference: a package name, a URL, or a relative path that lands outside the package.

- **A package name** resolves first to its sibling, the package of that name in the directory that holds this package. Only when there is no sibling does it resolve to the package of that name in any collection of packages the reader is given; if those collections hold more than one, the reader reports the reference as ambiguous, naming the candidates, and resolves it to none of them. `<name>` is 1-64 lowercase letters, numbers, hyphens and full stops, starting and ending with a letter or number, with no two of `-` and `.` together, which admits the name of every work, knowledge and acquire package.
- **A URL** resolves as the URL does.
- **A relative path** resolves from the directory of the file that holds it, as above.

An external reference must have one of these forms, but validation does not require it to resolve, because what it names lives, moves and ends on its own. A reader that cannot resolve one, or finds it ambiguous, reports it and goes on reading the package. An `ACQUIRE.md` that cites `package:git-help` when no package of that name is in sight is well formed, and the package is valid.

## Validation

A package is valid when:

- `ACQUIRE.md` exists and begins with a YAML front matter mapping
- the front matter has only the fields listed above, every field present meets its constraints, `compatibility` and `allowed-tools` included, and `name` matches the directory
- `metadata` maps strings to strings; it holds `source`, non-empty and at most 200 characters, and `mutation`, `none` or `declared`; `metadata.omissions`, where present, is a comma-separated list with no empty item; `metadata.spec`, where present, is `acquire/` followed by a major version the reader supports
- the body has the Scope, Procedure, Output and Verification sections, and a Mutation section when `metadata.mutation` is `declared`
- no file in the package holds a credential, token or captured source content
- every file reference is a package name, a URL or a relative path in the forms above; every relative path that lands inside the package resolves there

There is one level of validity. Size limits are recommendations, warned and never failed. A reviewer judges what cannot be checked by machine, against a trial run: whether the procedure really finds everything in scope, whether its rigour suits the source, and whether the declared omissions are the whole list; whether the Mutation section lists each permitted write with its confirmation; whether each script offers a dry run for any step that writes and stops when the source's responses change shape; and whether `assets/` holds no real captured content. No reference validator exists yet.

## Relation to Agent Skills

- **Reused unchanged:** a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `name`, `description`, `license`, `compatibility`, `metadata` and `allowed-tools` with their constraints, and Agent Skills' advice that `metadata` keys be reasonably unique; `scripts/`, with Agent Skills' recommendations for scripts, `references/` and `assets/`; three disclosure tiers; file references one level deep.
- **Different, and why:** the entry file is `ACQUIRE.md`, in upper case as `SKILL.md` is, which is this specification's rule, not Agent Skills'; `metadata` is required and must hold `source` and `mutation`, because a reader must see what is read and whether the source can be changed before trusting a run, and both are read in the first tier, which is therefore about 150 tokens rather than 100; `metadata.omissions` is defined, so the gaps are machine-readable; `metadata.spec` is defined so a reader can tell the version; the body has required sections, because completeness, provenance and verification are the guarantees acquisition exists to give; scripts must offer a dry run for any step that writes and must stop when the source's responses change shape, because a write made unseen or a response misread breaks those guarantees; a relative path resolves from the directory of the file that holds it rather than from the package root, which gives the same target in `ACQUIRE.md` and lets a link in a nested file work in any Markdown viewer; external references to other packages and to kept output are defined, in three notations a validator tells apart by form, because a run's output is kept outside the method; no captured content or credentials may sit in the package.
- **Skill validity:** every added field sits in `metadata`, so the front matter uses only fields Agent Skills defines; renamed to `SKILL.md`, a conforming package passed the checks `skills-ref validate` made when its source was read on 19 October 2026, and is a skill whose task is acquisition.

## Relation to the other specifications

An acquire package and a [knowledge package](knowledge.md) are separate extensions of Agent Skills, and neither is a stage of the other: acquire is a skill whose task is acquisition, knowledge one whose focus is what is known. Neither specification defines or requires a `metadata` field linking a package to the other kind, and a profile's own `metadata` keys are not restricted by this; a knowledge package may cite a run's output, or this acquire package, in its Sources, as it cites any other source. A [work package](work.md) may cite an acquire package as the method a piece of its work follows; the method itself outlasts the work.
