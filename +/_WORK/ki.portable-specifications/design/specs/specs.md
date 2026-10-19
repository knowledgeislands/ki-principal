# Specification drafts: work, knowledge and acquire

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working`, handing over to `ki.portable-specifications` · **Date:** 2026-10-19

Drafts written by the run spec-drafts under Kris's definition of the three areas at 14:27 BST on 19 October (decisions log entry "owner definition, SPEC-AREAS"). Each is a portable, tool-neutral specification in the [Agent Skills specification](https://agentskills.io/specification)'s page format, ready either to sit in an owning skill or to be published at `knowledgeislands.info/specs/{work,knowledge,acquire}`; that choice, SPEC-HOME, passes to `ki.portable-specifications` with these drafts. Nothing here is published. The open choices are in the spec-drafts run report, not here.

## The three specifications

| Spec | Entry file | What the package holds | Read by |
| --- | --- | --- | --- |
| [work](work.md) | `WORK.md` + four pick-up files | One piece of work: its definition and its current state, questions, incoming queue and decisions | Whoever routes work to it, and whoever picks it up |
| [knowledge](knowledge.md) | `KNOWLEDGE.md` | A curated body of knowledge on one topic, as a collection of Markdown files | A person or agent with a question about the topic |
| [acquire](acquire.md) | `ACQUIRE.md` | The method for acquiring knowledge from one source or with one tool | Whoever captures or refreshes knowledge from that source |

## Shared conventions

All three take from Agent Skills, unchanged: a package is a directory named for it; an upper-case entry file with YAML front matter and a Markdown body; `name` (Agent Skills rules, with `.` also allowed between segments of a work name), `description` (at most 1,024 characters, the routing signal), `license` and `metadata`; the optional `references/` and `assets/` directories; progressive disclosure from metadata to entry body to resources; relative file references one level deep; soft size limits. All three add an optional `spec` field (`work/1`, `knowledge/1`, `acquire/1`) and let a reader ignore top-level keys it does not know, so a local profile can extend a package without breaking a portable reader.

## How they relate

```text
          produces / refreshes                 cited as background
 acquire ----------------------> knowledge <-------------------------+
    ^      (produces <-> acquired-with)                               |
    |                                                                 |
    +---------------------------- work -------------------------------+
           cited as the method a unit follows
```

An acquire package produces or refreshes a knowledge package, and each names the other. A work package may cite either, but contains neither: it is removed when the work is done, while knowledge and methods outlast it, and its durable findings are curated into a knowledge package first.

## Where earlier material maps

Kris's definitions of 14:27 BST supersede the framing in [spec-areas.md](../spec-areas.md), written just before them.

| Earlier material | Maps to |
| --- | --- |
| spec-areas.md's "agent context package": curated, progressively read knowledge going out to agents | `knowledge`. Its Knowledge Manifest fields map as: scope and relevance to `description`, currency to `updated`, provenance to the Sources section, discovery routes to the Contents section; authority is left to a profile's `metadata`. |
| spec-areas.md's "knowledge package": acquire's sealed, hash-identified capture (the KEP, `kep.toml`, and Granola's `meeting.md` packages) | Not one of the three. It is the capture an acquire package's `## Output` describes, kept as an implementation format by `ki-acquire` and tools-ki; the resulting knowledge package cites it in its Sources. The name "knowledge package" now means the curated package. |
| The work package of the `ki-work-package` skill | `work`, as its Knowledge Islands profile; see below. |
| The `ki-acquire-granola` and `ki-acquire-chatgpt` skills, with `ki-acquire`'s common standard | `acquire` in substance: their `ki-acquire-*` front matter maps onto `source`, `mutation` (`read-only` to `none`, `explicit-marker` to `declared`), `omissions` and `compatibility`, and the common standard's scope, coverage, identity, preservation and verification rules became the required body sections. tools-ki's actions, properties, checkpoint and reset scopes stay profile fields. |
| `ki-pulse` | An acquisition method whose output is transient; it could become an acquire package without `produces`. |
| acquire's `context/<territory>/README.md` exports and seeds | Candidate knowledge packages, one per territory. |
| The retired KIS-0001 Knowledge Package (July 2026) | Prior art: its digests, terminology and open questions inform `knowledge`; its tasks, deliverables and handover inform `work`. Its Minimal, Standard and Extended conformance levels are not carried over. |
| Google's Open Knowledge Format (OKF v0.1) | An aligned external reference for `knowledge`, not read in full for these drafts. |

## The Knowledge Islands work-package profile

The `work` spec holds nothing of the Knowledge Islands ways of working. The house work package conforms to it as a profile:

| Knowledge Islands | `work` |
| --- | --- |
| `+/_WORK/<id>/`, dotted id such as `ki.observatory` | Package directory; dotted names conform |
| `work.md` | `WORK.md`, subject to ENTRY-NAMES |
| `id` | `name` |
| `level`, `title`, `label`, `project`, `theme`, `worker`, `supervisor`, `created_at` | Profile fields, ignored by a portable reader |
| `state.md` `state`: `with-worker` | `active` |
| `handoff-to-supervisor`, `with-supervisor`, `handoff-to-worker`, `handoff` | `waiting`, `target` mapping to `waiting-on` |
| `on-hold`, `hold.release` | `on-hold`, `release` |
| `finished` | `done` |
| `since` | `updated` |
| `blocking`, `received`, `beat`, `mark`, `method_read` | Profile fields |
| Run reports, `briefs/`, `design/` | Additional files, or `references/` and `assets/` |
| `messages.md` lines with a required tag and sender title | Messages lines, tag optional |

To conform, the profile keeps the four-value `state` and moves its seven states into a profile field (for example `ki-state`), or a reader maps them; that choice comes with the profile, not these drafts.
