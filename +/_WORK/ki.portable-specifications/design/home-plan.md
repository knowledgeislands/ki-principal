# Home plan: the three specifications into ki-agentic-harness

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.portable-specifications` · **Date:** 2026-10-20

Written by the read-only run home-plan to prepare [plan](plan.md#steps) step 6 (6a home-work, 6b home-acquire, 6c home-knowledge), so the three runs can start when Kris accepts the texts under SPEC-TEXT. It applies SPEC-HOME, ENTRY-NAMES, KNOWLEDGE-SKILL and WORK-PROFILE in [decisions](../decisions.md). Every fact was checked locally on 20 October against ki-agentic-harness at `5daad99e`, whose working tree was clean; the installed harness `knowledgeislands/ki-agentic-harness` is a link to that checkout, so a new skill resolves without an install step. Nothing was changed outside this file.

## Contents

- [Gate and order](#gate-and-order)
- [The homing transform](#the-homing-transform)
- [6a home-work: ki-work-package](#6a-home-work-ki-work-package)
- [6b home-acquire: ki-acquire](#6b-home-acquire-ki-acquire)
- [6c home-knowledge: the new ki-knowledge-package](#6c-home-knowledge-the-new-ki-knowledge-package)
- [The drift criterion](#the-drift-criterion)
- [Verification](#verification)
- [Running the three in parallel](#running-the-three-in-parallel)
- [What graduates](#what-graduates)
- [What needs Kris](#what-needs-kris)

## Gate and order

- **Gate:** SPEC-TEXT accepted; the approved text is the drafts in `design/specs/` at the commit Kris approves, which each run names in its brief and its skill's `sources.md`.
- **6b and 6c** start together the moment SPEC-TEXT is accepted.
- **6a** waits for ki.ways-of-working's queued harness chain, ENTRY-NAMES (`work.md` to `WORK.md`, across the `ki-work-package` contract and its readers), which rewrites the same `SKILL.md`, standard, rubric context and `sources.md`. If that rename has landed when 6a runs, the profile's entry-file lines change with it (see [6a](#6a-home-work-ki-work-package)).
- **Records and review:** see HOMING-REVIEW under [What needs Kris](#what-needs-kris).

## The homing transform

Each homed reference is its approved draft with these edits and no others; any other wording change goes back to Kris under SPEC-TEXT.

1. **Status line:** `**Status:** draft 0.8, 20 October 2026. Name <name>. To be held in ...` becomes `**Status:** version 1, accepted <date of SPEC-TEXT>. Name <name>. Held here until it is published and moved to KI Specifications.` The draft history stays in Git and in this work folder.
2. **Attribution line:** kept word for word, as the [live check](agentskills-check.md#4-licence-of-the-specification-text) sets. The harness is MIT; the file carries its own CC BY 4.0 notice, which is what the licence asks.
3. **Links between the specifications** (`[knowledge package](knowledge.md)`, `[acquire package](acquire.md)`, `[work package](work.md)`, nine links across the three) become unlinked words naming the specification, such as "a knowledge package, as the `knowledge` specification defines it". A relative link across skills breaks the harness rule that another skill is named, never reached by path (KI-LINK-3), and naming `ki-*` skills inside the text would make a portable spec house-specific. Publication (plan step 8) turns the names back into links to the published pages.
4. **A `## Contents` list** after the attribution line, from the file's own `##` headings. Each reference runs to about 200 lines, and REF-3 warns on a reference over 100 lines without one.

The example links inside inline code, such as `` `See [the cut-over plan](references/cut-over-plan.md).` ``, stay as they are; they are code, not links.

## 6a home-work: ki-work-package

Root: `skills/governance/ki-work-package/`.

| File | Change |
| --- | --- |
| `references/standards-work-spec.md` | Add: `design/specs/work.md` through the homing transform |
| `references/standards-work-spec-profile.md` | Add: `design/specs/work-house-profile.md`, edited as below |
| `SKILL.md` | Change: one paragraph, below |
| `references/sources.md` | Change: two rows and a Last review entry, below |
| `scripts/rubric/items/spec.ts` | Add: the `SPEC` family with SPEC-1, [below](#the-drift-criterion) |
| `scripts/rubric/items/index.ts` | Change: import `SPEC`, append it to `families` |
| `scripts/rubric/contexts/work-package.ts` | Change: add `'SPEC'` to the subject's `families` list (line 1001) |
| `references/rubric.md` | Regenerate: `ki dev skill rubric ki-work-package --write` |

**The profile's edits.** Title `# Knowledge Islands work-package profile`. The provenance paragraph shrinks to one sentence: "This profile maps the house work package, as [the work-package standard](standards-work-package.md) defines it, onto [the portable work specification](standards-work-spec.md); it changes neither." Its run history moves to `sources.md`. The absolute-path link to the standard and the link to `work.md` become those two relative links; the "earlier claim in `specs.md`" sentence goes, keeping the list of where the house package fails. If ENTRY-NAMES has landed, the `work.md`-to-`WORK.md` lines (the entry-file failure, "Until it lands, the mapping reads `work.md` as `WORK.md`", the Folder and files row and the link rule's entry rename) are rewritten to say the house entry is already `WORK.md` and the rename rule applies only to packages not yet migrated; this is the one change beyond the transform, and the run reports it.

**SKILL.md wording**, a new bullet at the end of `## Shared model`:

> - **Portable specification** - [the work specification](references/standards-work-spec.md) is `work`, the portable, tool-neutral format of a work package, an extension of the Agent Skills format: it sets the files and what each entry carries, and nothing of how a team works them. The house package is a mapped profile of it, not a conforming package; [the profile](references/standards-work-spec-profile.md) maps each house field and state onto it and names the house rules the specification leaves to this standard. Read the specification to write or read a package for use outside Knowledge Islands, and the profile to convert between the two; neither changes this standard.

The `description` does not change, so 6a leaves the generated catalogue alone.

**sources.md** (table form, as the file uses):

| Source | Last reviewed | Governs |
| --- | --- | --- |
| The portable `work` specification drafts 0.1 to 0.8, their blind reviews and Kris's SPEC-TEXT approval, in Knowledge Islands Principal's `ki.portable-specifications` work at `<commit>` | `<date>` | `standards-work-spec.md` and `standards-work-spec-profile.md` |
| The [Agent Skills specification](https://agentskills.io/specification), documentation under CC BY 4.0, read live with the `skills-ref` source on 2026-10-19 | 2026-10-19 | The format `work` extends, its attribution and what is claimed of `skills-ref` |

The Last review entry names SPEC-HOME and WORK-PROFILE in Kris's words and says the house standard did not change. The refresh class stays `canonical · on-change`; Agent Skills drift is caught by `ki-skills` REFRESH, and the D1 and D2 drift the live check found are that REFRESH's.

## 6b home-acquire: ki-acquire

Root: `skills/acquire/ki-acquire/`.

| File | Change |
| --- | --- |
| `references/standards-acquire-spec.md` | Add: `design/specs/acquire.md` through the homing transform |
| `SKILL.md` | Change: one paragraph, below |
| `references/sources.md` | Change: two bullets and a Last review paragraph |
| `scripts/rubric/items/spec.ts` | Add: the `SPEC` family with SPEC-1 |
| `scripts/rubric/items/index.ts` | Change: import `SPEC`, add it to `families` before `RUBRIC` |
| `scripts/rubric/contexts/acquisition.ts` | Change: add the subject `{ families: ['SPEC'], context: () => context }` |
| `references/rubric.md` | Regenerate: `ki dev skill rubric ki-acquire --write` |

No profile file: WORK-PROFILE asked for one only for `work`. The provider front matter mapping in [specs.md](specs/specs.md#where-earlier-material-maps) (`ki-acquire-*` keys to `metadata.source`, `metadata.mutation` and `metadata.omissions`) goes into the Last review paragraph as provenance, not into the standard.

**SKILL.md wording**, a new paragraph after the second paragraph (the one that begins "This skill owns the common capture contract"):

> [The acquire specification](references/standards-acquire-spec.md) is `acquire`, the portable, tool-neutral format of an acquire package: the method for acquiring knowledge from one source or with one tool, as an extension of the Agent Skills format. Read it to write or review a method meant for use outside Knowledge Islands, or to read a provider skill's contract as a portable package; [the common acquisition standard](references/standards-acquisition.md) and the provider skills stay the house contract.

The `description` does not change.

**sources.md** gains a bullet for the `acquire` drafts, reviews and SPEC-TEXT approval at `<commit>`, and one for the Agent Skills specification under CC BY 4.0, read live on 2026-10-19. The refresh class stays `canonical · on-change`.

## 6c home-knowledge: the new ki-knowledge-package

Root: `skills/governance/ki-knowledge-package/`, in the governance concern beside `ki-work-package`, as KNOWLEDGE-SKILL ("a new governance skill") says.

### Files

| File | Content |
| --- | --- |
| `SKILL.md` | New, below |
| `references/standards-knowledge-spec.md` | `design/specs/knowledge.md` through the homing transform |
| `references/sources.md` | New, below |
| `references/rubric.md` | Generated: `ki dev skill rubric ki-knowledge-package --write` |
| `scripts/shared/rubric.ts` | A byte copy of `skills/keystone/ki-skills/scripts/shared/rubric.ts`, the materialised `ki-skills:rubric` module |
| `scripts/rubric/contexts/knowledge.ts` | The session, on the pattern of `ki-acquire`'s `contexts/acquisition.ts`: configuration keys and rubric publication, subjects `CONFIG`, `SPEC`, `RUBRIC`, no proposal writes |
| `scripts/rubric/items/configuration.ts` | `CONFIG-1 [M]`, no configuration properties, on `ki-acquire`'s pattern |
| `scripts/rubric/items/publication.ts` | `RUBRIC`, `createRubricPublicationFamily` as in the other two |
| `scripts/rubric/items/spec.ts` | `SPEC` with SPEC-1, [below](#the-drift-criterion) |
| `scripts/rubric/items/index.ts` | `contract: 1`, `name: 'ki-knowledge-package'`, `concern: 'portable knowledge packages'`, families `[CONFIG, SPEC, RUBRIC]` |
| `scripts/rubric/items/configuration.test.ts` | On `ki-acquire`'s test: an unknown key is a violation, and the RUBRIC subject exists |

No `assets/`, no evals: neither `ki-work-package` nor `ki-acquire` has an eval scenario, and a scenario needs a house-specific fact to test, which can follow once packages exist. The criteria that check a knowledge package itself (its description's area and boundaries, its map, its Sources) are not in this step: KNOWLEDGE-SKILL gives the skill "the `knowledge` spec and later its rubric", and the plan's "No validator" risk stands until then.

### SKILL.md

```markdown
---
name: ki-knowledge-package
ki-kind: governance
ki-applicability: declaration-only
ki-depends-on: []
ki-shared-dependencies: [ki-skills:rubric]
description: >
  Own `knowledge`, the portable specification of a knowledge package: an Agent Skills extension into which the
  knowledge of one area is condensed and factored, with its `KNOWLEDGE.md` entry, description, limits, map and
  Sources. Use to write, review or explain a knowledge package or the specification; `ki-skills` owns skills that
  perform actions, `ki-repo-kb` owns knowledge bases and `ki-acquire` owns acquisition methods.
argument-hint: 'audit <repo> | conform <repo> | educate <repo> | help | refresh'
---

# Knowledge package

Read [the knowledge specification](references/standards-knowledge-spec.md) before writing, reviewing or explaining a knowledge package. It is `knowledge`, a portable, tool-neutral format: a skill whose focus is the knowledge of one area rather than an action, read progressively from its description to its overview to the files a reader needs. [The generated rubric](references/rubric.md) publishes this skill's criteria, and [the sources](references/sources.md) record the specification's provenance and its Agent Skills basis.

This skill owns the specification only. It accepts no repository configuration properties and does not yet check packages mechanically; a package is reviewed against the specification by reading it.

## Operating modes

For `help`, `-h`, `?` or no recognised mode, explain the specification, the modes and the off-ramps without reading or changing anything; offer a mode choice only in an interactive session.

### Mode AUDIT

Run `ki repo audit --skill ki-knowledge-package --repo <repo>`. Review a supplied package against the specification's Validation section; the mechanical audit covers only configuration and rubric publication, so a passing audit does not establish that a package conforms.

### Mode CONFORM

Run AUDIT, then `ki repo conform --skill ki-knowledge-package --repo <repo> --dry-run`. The host may regenerate rubric publication. This mode never writes or rewrites a package.

### Mode EDUCATE

Explain the specification from its reference: what condensing and factoring must leave a reader with, the entry file and its fields, progressive disclosure and file references. Do not create a package merely to demonstrate it.

### Mode REFRESH

REFRESH writes only in `ki-agentic-harness`; from an installed copy, stop and name the harness. Read [the sources](references/sources.md), re-check the Agent Skills specification the format extends, propose the smallest change, and record the review after it occurs.
```

The description runs to about 420 characters. `declaration-only` because `ki-repo` has no repository evidence for knowledge packages (`detected` would need a `ki-repo` change); `ki-depends-on: []` because nothing is composed.

### sources.md

`**Refresh:** external-spec · quarterly`, because the format extends Agent Skills, an external specification, and LONG-4b requires a clock cadence for that class. Rows: Kris's definition of `knowledge` (19 October, 14:27 BST) and KNOWLEDGE-AS-SKILL (20 October); the drafts, their reviews and SPEC-TEXT at `<commit>`; the Agent Skills specification under CC BY 4.0, read live on 2026-10-19; the retired KIS-0001 Knowledge Package as prior art; Google's Open Knowledge Format v0.1 as an aligned reference not read in full. A Last review block states what was confirmed.

### Registration

| File | Change | Check |
| --- | --- | --- |
| `.ki.toml` | Add an empty `[skills.ki-knowledge-package]` beside `[skills.ki-acquire]`, so its own audit runs here, as `ki-acquire`'s does | `ki repo audit --skill ki-knowledge-package` resolves |
| `skills/repo-structure/ki-repo-harness/scripts/rubric/contexts/skill-functions.ts` | Add `'ki-knowledge-package'` to the Records group of `records-and-code` (`ki-decision-records`, `ki-specs`, `ki-guides`), whose purpose is "govern what a repository records, explains and builds" | `skill-functions.test.ts`: every skill in at least one area |
| `skills/keystone/ki-skills/SKILL.md` | Add the reciprocal off-ramp to its description, "`ki-knowledge-package` for knowledge packages", since a knowledge package is a skill and both fire on "write a skill about X" (COLL-2) | `ki repo audit --skill ki-skills`, COLL-1 and the COLL-2 read |
| `skills/README.md` | Generated catalogue gains the entry and the count line becomes 65 skills, 54 governance (CAP-2) | `ki repo audit --skill ki-repo-harness` |
| `README.md` | "64 ... 53 governance" becomes "65 ... 54 governance" (CAP-3) | Same |
| `docs/diagrams/skill-map.architecture.json`, `docs/diagrams/skill-area-records-and-code.architecture.json` | Regenerated (CAP-4) | Same |
| `docs/diagrams/skill-map.svg`, `docs/diagrams/skill-area-records-and-code.svg` | Re-exported by `ki-diagrams`' build with `--svg`, which drives the local Chrome headless; no network | `ki repo audit --skill ki-diagrams` |

The four generated rows are written by `ki repo conform --skill ki-repo-harness --repo <harness>` in write mode, which this brief and HOOK-GUARD forbid (see CATALOGUE-WRITE). `ki-repo-kb`'s description is not changed: its notes and a knowledge package differ by kind, and a second off-ramp costs standing tokens in every session; the COLL-2 read decides if it is needed. The website's skills-by-outcome guide changes only at publication (plan step 8).

## The drift criterion

Plan and `specs.md` call for one rubric criterion per owning skill naming the shared rules. The same item in each, judgment only, so it needs no context code:

- **Code and title:** `SPEC-1 [J] - the portable specification keeps the shared rules`
- **Family:** `SPEC`, "Portable specification", standard the skill's own `standards-<name>-spec.md`
- **Description:** "The portable specification keeps the rules the three portable specifications share: one upper-case entry file named for the specification, ASCII names, a closed list of top-level keys, every added field in `metadata` as a string with `metadata.spec` versioning it, three file-reference notations with relative paths resolved from the holding file, one level of validity with size limits warned, and the CC BY 4.0 attribution to Agent Skills." `ki-work-package`'s adds: "and the profile maps every field and state the house standard defines."
- **Judgment:** `judgment('Do the specification's shared rules still agree, word for word in substance, with those of the other two portable specifications and with the current Agent Skills specification?')`, plus for `ki-work-package` "and does the profile cover every house field and state?"

Each run writes its own `spec.ts`; the description text is fixed here so the three agree.

## Verification

Each run, sequentially, in the harness, as its `AGENTS.md` sets:

1. `bun run test` and `bunx tsc --noEmit`.
2. `ki dev skill rubric <skill>` verifies the regenerated `references/rubric.md`.
3. `ki repo audit --skill ki-skills --repo <harness>`: LAY, KI-LINK-1 and 2 (every relative link in the new references resolves), KI-SHAPE-6 (the new names sit in the closed vocabulary), REF-3, SIZE, PORT-1 (the texts name no runtime; "Anthropic" in the attribution is not a runtime term) and, for 6c, KI-CHECKER-5 (the shared module matches the declaration).
4. `ki repo audit --skill <skill> --repo <harness>`: RUBRIC-1 publication and CONFIG-1.
5. 6c only, after its conform write: `ki repo audit --skill ki-repo-harness --repo <harness>` (CAP-2, CAP-3, CAP-4) and `ki repo audit --skill ki-diagrams --repo <harness>`.
6. The judgment reads: KI-LINK-3, REF-2 (each new reference cited from `SKILL.md` with when to read it), COLL-2 for 6c, and SPEC-1 itself against the other two homed texts once all three land.

The pre-commit hook runs lint-staged (rumdl and Biome), `tsc` for staged `.ts` and the staged-snapshot `ki-skills` audit; a commit it refuses is fixed, never bypassed. Fleet findings outside the run's own files are reported apart from failures in its change.

One finding for 6a: `ki-work-package`'s `scripts/shared/rubric.ts` is an older copy than `ki-skills`' provider (it lacks `packageScripts`); `judgment` exists in both, so SPEC-1 does not need it refreshed, and 6a leaves it alone.

## Running the three in parallel

| Run | Writes | Starts |
| --- | --- | --- |
| 6a | `skills/governance/ki-work-package/**` only | After ki.ways-of-working's ENTRY-NAMES harness run |
| 6b | `skills/acquire/ki-acquire/**` only | On SPEC-TEXT |
| 6c | `skills/governance/ki-knowledge-package/**`, `.ki.toml`, `skill-functions.ts`, `ki-skills/SKILL.md`, then the generated `skills/README.md`, `README.md` and four `docs/diagrams/` files | On SPEC-TEXT |

The write sets are disjoint, and 6a and 6b change no description, so the catalogue and diagrams are regenerated once, by 6c, whatever order the three finish in. They share one working tree, so:

- **Commit by path:** each run stages and commits only its own paths, as `git add <paths>` then `git commit -q -m <msg> -- <paths>`, so another run's staged files never ride along.
- **Index lock:** a run that meets `.git/index.lock` waits and retries; it never deletes the lock.
- **Whole-tree gates:** `tsc`, `bun run test` and the hook's snapshot audit see the others' half-written files. A failure only in another run's paths is waited out and rerun, never fixed.

If Kris prefers no shared-tree risk at all, 6b and 6c can chain instead, at the cost of one run's time.

## What graduates

- `design/specs/` (`work.md`, `knowledge.md`, `acquire.md`, `work-house-profile.md`): kept until publication (plan step 8), which publishes from the homed references; then deleted at a mark.
- `design/specs/specs.md`: its shared conventions become SPEC-1 in each skill and its mapping table goes into the three `sources.md` entries; deleted at the mark after 6c lands.
- `design/spec-areas.md`: the plan keeps it until the knowledge skill lands; its inventory of the retired KEP and KIS-0002 material still serves plan steps 9 and 10, so move that inventory into the step 9 handoff record before deleting it.
- This note: deleted at the mark after all three land.

## What needs Kris

Four matters, in the run report's Queries: SPEC-TEXT (already with Kris), HOMING-EDITS (the transform above), CATALOGUE-WRITE (the one write-mode conform), HOMING-REVIEW (records and review route). Everything else above is decided here within SPEC-HOME, KNOWLEDGE-SKILL and WORK-PROFILE.
