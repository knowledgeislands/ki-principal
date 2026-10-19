# Specification drafts: work, knowledge and acquire

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.portable-specifications` · **Date:** 2026-10-19

Draft 0.1 was written by the run spec-drafts under Kris's definition of the three areas at 14:27 BST on 19 October, in ki.ways-of-working. Draft 0.2 was written by the run revise, step 3 of [the plan](../plan.md#steps), to every owner decision in [decisions.md](../../decisions.md) and the findings of the [live Agent Skills check](../agentskills-check.md). Draft 0.3 was written by the run revise-2 on 20 October to the findings of the blind review of draft 0.2, [draft-review](../../draft-review.report.md). Draft 0.4 was written by the run revise-3 on 20 October to Kris's definition KNOWLEDGE-AS-SKILL, which makes `knowledge` an Agent Skills extension first and foremost and drops the acquire-to-knowledge transition. Each is a portable, tool-neutral specification in the [Agent Skills specification](https://agentskills.io/specification)'s page format. Under SPEC-HOME and KNOWLEDGE-SKILL each will be held as one reference in its owning skill, `ki-work-package`, a new `ki-knowledge-package` and `ki-acquire`, and published from the same text later in this Project. Nothing here is published.

## The three specifications

| Spec | Entry file | What the package holds | Read by | Owning skill |
| --- | --- | --- | --- | --- |
| [work](work.md) | `WORK.md` + four other required files | One piece of work: its definition and its current state, questions, incoming messages and decisions | Whoever looks for work or picks it up | `ki-work-package` |
| [knowledge](knowledge.md) | `KNOWLEDGE.md` | The knowledge of one area, condensed and factored into a skill whose focus is the knowledge rather than an action | A person or agent who wants to learn about the topic or has a question about it | `ki-knowledge-package` |
| [acquire](acquire.md) | `ACQUIRE.md` | The method for acquiring knowledge from one source or with one tool | Whoever captures or refreshes knowledge from that source | `ki-acquire` |

## Shared conventions

All three take from Agent Skills: a package is a directory named for it; an entry file with YAML front matter and a Markdown body; `name` (Agent Skills rules, with `.` also allowed between segments of a work name), `description` (at most 1,024 characters), `license` and `metadata`; the optional `references/` and `assets/` directories; progressive disclosure in three tiers, from metadata to entry body to resources; relative file references one level deep; soft size limits.

All three add, as their own rules rather than Agent Skills':

- **One entry file in upper case,** named for the spec, as `SKILL.md` is (ENTRY-NAMES). Agent Skills fixes only the name `SKILL.md` and sets no rule on the case of other files.
- **A closed list of top-level keys,** stated in words. Agent Skills' page lists six fields without saying no others are allowed; its validator, `skills-ref`, rejects any other.
- **Every added field in `metadata`, as a string** (SPEC-LOCATION): `spec`, `knowledge`'s `updated` and `owner`, and `acquire`'s `source`, `mutation` and `omissions`, the last one comma-separated string. A reader ignores `metadata` keys it does not know, and a profile adds its own there with a prefix, following Agent Skills' advice that keys be reasonably unique. So `knowledge` and `acquire` packages, renamed to `SKILL.md`, pass `skills-ref validate` as read on 19 October. A `work` package makes no such claim: its entry file is `WORK.md`, and renamed to `SKILL.md` its front matter passes only when its `name` has no `.`; its four other required files are additional files, which Agent Skills allows.
- **`metadata.spec`** (SPEC-VERSION): `work/1`, `knowledge/1` or `acquire/1`; absent means version 1 for good; a reader rejects a major version it does not support, and validation checks the field.
- **Internal links and external references:** a relative link inside the package must resolve; anything outside it, another package or evidence kept elsewhere, is an external reference by package name, URL or a relative path beginning `../`, checked for its form but not required to resolve.
- **One level of validity** (CONFORMANCE-LEVELS), with size limits warned and never failed.
- **Attribution:** each draft carries the CC BY 4.0 attribution line the [live check](../agentskills-check.md#4-licence-of-the-specification-text) sets, and each published page must carry it too.

Each spec stays self-contained, as Agent Skills is. A drift check, one rubric criterion in each owning skill naming these shared rules, keeps them in step.

## How they relate

```text
 acquire                                knowledge
    ^                                       ^
    |  cited as the method                  |  cited as background
    +---------------- work -----------------+
```

Each is its own extension of Agent Skills, and none is a stage of another. `knowledge` and `acquire` are both skills: one whose focus is the knowledge of an area, one whose task is acquiring from a source. Neither names the other in its `metadata`; a knowledge package may cite an acquisition's output among its Sources, as it cites any other source. A work package may cite either, but contains neither: the work ends, while knowledge and methods outlast it.

Making a knowledge package is condensing and factoring the knowledge of one area into it (KNOWLEDGE-AS-SKILL). `knowledge` sets what that must leave a reader with, the scope of the area, what was drawn out and its provenance, as the package's own contract, and prescribes no workflow; there is no separate curation stage.

## Where earlier material maps

Kris's definitions of 14:27 BST supersede the framing in [spec-areas.md](../spec-areas.md), written just before them.

| Earlier material | Maps to |
| --- | --- |
| spec-areas.md's "agent context package": curated, progressively read knowledge going out to agents | `knowledge`. Its Knowledge Manifest fields map as: scope and relevance to `description`, currency to `metadata.updated`, provenance to the Sources section, discovery routes to the Contents section, ownership to `metadata.owner`; authority is left to a profile's `metadata`. |
| spec-areas.md's "knowledge package": acquire's sealed, hash-identified capture (the KEP, `kep.toml`, and Granola's `meeting.md` packages) | Not one of the three. It is the output an acquire package's `## Output` describes, kept as an implementation format by `ki-acquire` and tools-ki; a knowledge package may cite it in its Sources. The name "knowledge package" now means the condensed skill `knowledge` defines. |
| The work package of the `ki-work-package` skill | A mapped profile of `work`, not a conforming package; see [work-house-profile.md](work-house-profile.md). |
| The `ki-acquire-granola` and `ki-acquire-chatgpt` skills, with `ki-acquire`'s common standard | `acquire` in substance: their `ki-acquire-*` front matter maps onto `metadata.source`, `metadata.mutation` (`read-only` to `none`, `explicit-marker` to `declared`), `metadata.omissions` and `compatibility`, and the common standard's scope, coverage, identity, preservation and verification rules became the required body sections, with coverage levels and checksums recommended rather than required. tools-ki's actions, properties, checkpoint and reset scopes stay profile fields. |
| `ki-pulse` | An acquisition method whose output is transient; it could become an acquire package. |
| acquire's `context/<territory>/README.md` exports and seeds | Candidate knowledge packages, one per territory. |
| The retired KIS-0001 Knowledge Package (July 2026) | Prior art: its digests, terminology and open questions inform `knowledge`; its tasks, deliverables and handover inform `work`. Its Minimal, Standard and Extended conformance levels are not carried over. |
| Google's Open Knowledge Format (OKF v0.1) | An aligned external reference for `knowledge`, not read in full for these drafts. |

## The Knowledge Islands work-package profile

The house work package, as built, does not conform to `work`; draft 0.1's claim that it did was wrong. Under WORK-PROFILE it stays a mapped profile, and [work-house-profile.md](work-house-profile.md) gives the field and state mapping and lists the house rules draft 0.2 moved out of the spec.
