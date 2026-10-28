# Home plan: the three specifications into ki-agentic-harness

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.portable-specifications` · **Date:** 2026-10-20

Written by the read-only run home-plan to prepare [plan](plan.md#steps) step 6 (6a home-work, 6b home-acquire, 6c home-knowledge), so the three runs can start when Kris accepts the texts under SPEC-TEXT. It applies SPEC-HOME, ENTRY-NAMES, KNOWLEDGE-SKILL and WORK-PROFILE in [decisions](../decisions.md). Every fact was checked locally on 20 October against ki-agentic-harness at `5daad99e`, whose working tree was clean; the installed harness `knowledgeislands/ki-agentic-harness` is a link to that checkout, so a new skill resolves without an install step. Nothing was changed outside this file. The run home-amend amended it on 20 October to CATALOGUE-WRITE and HOMING-REVIEW, decided a) under OVERNIGHT-AUTONOMY at 01:13 BST, and to every correction in [query-review-6](https://github.com/knowledgeislands/ki-principal/blob/1e930f1b/+/_WORK/ki.prj.portable-specifications/query-review-6.report.md).

## Contents

- [Gate and order](#gate-and-order)
- [Records, review and acceptance](#records-review-and-acceptance)
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

- **Gate:** SPEC-TEXT accepted, with HOMING-EDITS folded into it, both pending Kris. The approved text is the drafts in `design/specs/` at the commit Kris approves, edited by [the homing transform](#the-homing-transform) and nothing else; each run names that commit in its brief and its skill's `sources.md`.
- **Records:** each step also needs its harness record adopted, planned to Ready and given implementation authority before its run starts; SPEC-TEXT alone does not pass that gate ([Records, review and acceptance](#records-review-and-acceptance)).
- **6b and 6c** start together once SPEC-TEXT is accepted and their records are Ready, each in its own worktree ([Running the three in parallel](#running-the-three-in-parallel)).
- **6a** keeps the ENTRY-NAMES prerequisite: it waits until ki.ways-of-working's queued harness chain, ENTRY-NAMES (`work.md` to `WORK.md`, across the `ki-work-package` contract and its readers), has integrated into the harness's local `main`, because that chain rewrites the same `SKILL.md`, standard, rubric context and `sources.md`. The profile's entry-file lines change with it (see [6a](#6a-home-work-ki-work-package)).

## Records, review and acceptance

HOMING-REVIEW a) sets this route. For this coordinator route it replaces the Steward gate in [plan](plan.md#steps) steps 6a to 6c and its harness review latency risk. The harness's `AGENTS.md` keeps its solo direct-to-`main` workflow apart from its Paperclip local-delivery route, where Wright implements, Steward reviews the exact commit and Convenor integrates; these runs do not enter that route, and nothing here waives or replaces Steward review within it.

1. **Capture.** One run, home-records, deduplicates against the harness roadmap, then captures three triage records under `ki-next`, one each for 6a, 6b and 6c, because each has its own boundary and verification. It re-reads `docs/roadmap/_ISSUES.md` immediately before allocating identities and commits each ledger advance; GOV-227 is the ledger's current high-water mark, not a reservation of the next three. Capture is triage only and authorises no delivery.
2. **Ready.** After SPEC-TEXT, each record is adopted and selected under `ki-next`, planned to Ready under `ki-plan` and given implementation authority before its run starts.
3. **Deliver.** Each run delivers its record under `ki-implement`, from an immutable baseline to Awaiting review, on its own branch in its own worktree, and returns immutable delivery evidence and the six-part review packet.
4. **Review.** One blind Codex review per candidate reviews the exact candidate commit and its combined result with the harness's local `main`, with the harness's sequential `bun run test`, `bunx tsc --noEmit` and the focused audits under [Verification](#verification) run on that combined result; a prose review alone does not pass. A changed candidate returns to review.
5. **Integrate.** Integration into local `main` is serialised, one candidate at a time, after its review passes ([Running the three in parallel](#running-the-three-in-parallel)).
6. **Accept.** Kris accepts each record under `ki-accept`, or a separately evidenced exact closure grant does. Review, integration and any Paperclip completion are not KI acceptance.
7. **Consistency.** Once all three candidates are available, SPEC-1 is read across the three homed texts ([Verification](#verification) step 6).

## The homing transform

Each homed reference is its approved draft with these edits and no others. HOMING-EDITS, folded into SPEC-TEXT and pending Kris, asks Kris to accept these four as part of the approved text, so the homed files count as that text; any other wording change goes back to Kris under SPEC-TEXT. If Kris takes HOMING-EDITS b) instead, each homed file comes back to Kris for approval after its run.

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

**The profile's edits.** Title `# Knowledge Islands work-package profile`. The provenance paragraph shrinks to one sentence: "This profile maps the house work package, as [the work-package standard](standards-work-package.md) defines it, onto [the portable work specification](standards-work-spec.md); it changes neither." Its run history moves to `sources.md`. The absolute-path link to the standard and the link to `work.md` become those two relative links; the "earlier claim in `specs.md`" sentence goes, keeping the list of where the house package fails. Because 6a runs only after ENTRY-NAMES has landed, the `work.md`-to-`WORK.md` lines (the entry-file failure, "Until it lands, the mapping reads `work.md` as `WORK.md`", the Folder and files row and the link rule's entry rename) are rewritten to say the house entry is already `WORK.md` and the rename rule applies only to packages not yet migrated; this is the one change beyond the transform, and the run reports it.

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

The catalogue, the root counts and the diagram JSON sources are written by one write-mode `ki repo conform --skill ki-repo-harness`, under [the bounded conform write](#the-bounded-conform-write); the SVGs by the separate diagram build. `ki-repo-kb`'s description is not changed: its notes and a knowledge package differ by kind, and a second off-ramp costs standing tokens in every session; the COLL-2 read decides if it is needed. The website's skills-by-outcome guide changes only at publication (plan step 8).

### The bounded conform write

CATALOGUE-WRITE a) allows 6c's brief exactly one write-mode `ki repo conform --skill ki-repo-harness`, run against 6c's worktree; every other `ki repo conform`, in 6c and in every other run, stays `--dry-run`. It is a scoped exception for this one brief, not a lifting of any other brief's ban. HOOK-GUARD is recorded as superseded by HOOKS-MIGRATION in ki.tools-burndown and ki.mac-studio-setup, while ki.ways-of-working and ki.timelines carry the earlier guard and ki.baseline-rollout a non-dry-run caution; those stand for their own work. HOOKS-MIGRATION constrains hook conversion and grants no conform write, and nothing here assumes the estate migration has finished.

1. **Audit first:** `ki repo audit --skill ki-repo-harness --repo <worktree>`, recording its findings before anything is generated.
2. **Dry-run:** `ki repo conform --skill ki-repo-harness --repo <worktree> --dry-run`.
3. **Check the complete proposed path set and diff.** The briefed set is `skills/README.md`, `README.md`, `docs/diagrams/skill-map.architecture.json` and `docs/diagrams/skill-area-records-and-code.architecture.json`, with hunks that only add `ki-knowledge-package`, its counts and its diagram nodes. The publisher can also propose `.ki.toml` and the diagram JSON of any functional area it finds stale, and a skill selector is not a path allow-list: a proposed path outside the briefed set, a hunk beyond the new skill, or any write or command the brief does not name stops the run, which reports it and writes nothing.
4. **Write:** the one `ki repo conform --skill ki-repo-harness --repo <worktree>` without `--dry-run`. The dry-run is a preview, not an approval given just before the live command: the CLI stages its writes and applies them once its own initial audits pass. The run therefore checks the worktree's changed paths and hunks against the briefed set and the dry-run diff straight after, and stops on any other, such as the `.rumdl.toml` rewrite and `rumdl --fix` reflow ki.tools-burndown has seen conform make elsewhere; a stopped run reports and leaves its worktree as it stands.
5. **Re-audit** `ki-repo-harness` after generation.
6. **Export the SVGs** with `ki-diagrams`' build and `--svg`, a separate step the publisher does not take, then re-audit `ki-repo-harness` and `ki-diagrams`.

Package manifests, lockfiles and hook directories stay outside this authority whatever any step proposes. Hand-maintaining the generated output could satisfy the exact generated-content checks, but it is the more error-prone route, which is why the bounded write is preferred. If local `main` moves under 6c before it integrates, as ENTRY-NAMES would by changing `ki-work-package`'s description, the generated paths are regenerated on the rebased branch through steps 1 to 6 and the changed candidate returns to review.

## The drift criterion

Plan and `specs.md` call for one rubric criterion per owning skill naming the shared rules. The same item in each, judgment only, so it needs no context code:

- **Code and title:** `SPEC-1 [J] - the portable specification keeps the shared rules`
- **Family:** `SPEC`, "Portable specification", standard the skill's own `standards-<name>-spec.md`
- **Description:** "The portable specification keeps the rules the three portable specifications share: one upper-case entry file named for the specification, ASCII names, a closed list of top-level keys, every added field in `metadata` as a string with `metadata.spec` versioning it, three file-reference notations with relative paths resolved from the holding file, one level of validity with size limits warned, and the CC BY 4.0 attribution to Agent Skills." `ki-work-package`'s adds: "and the profile maps every field and state the house standard defines."
- **Judgment:** `judgment('Do the specification's shared rules still agree, word for word in substance, with those of the other two portable specifications and with the current Agent Skills specification?')`, plus for `ki-work-package` "and does the profile cover every house field and state?"

Each run writes its own `spec.ts`; the description text is fixed here so the three agree.

## Verification

Each run, in its own worktree, runs these sequentially, as the harness's `AGENTS.md` sets, and its review and integration run them again on the combined result with local `main` ([Records, review and acceptance](#records-review-and-acceptance)):

1. `bun run test` and `bunx tsc --noEmit`.
2. `ki dev skill rubric <skill>` verifies the regenerated `references/rubric.md`.
3. `ki repo audit --skill ki-skills --repo <harness>`: LAY, KI-LINK-1 and 2 (every relative link in the new references resolves), KI-SHAPE-6 (the new names sit in the closed vocabulary), REF-3, SIZE, PORT-1 (the texts name no runtime; "Anthropic" in the attribution is not a runtime term) and, for 6c, KI-CHECKER-5 (the shared module matches the declaration).
4. `ki repo audit --skill <skill> --repo <harness>`: RUBRIC-1 publication and CONFIG-1.
5. 6c only, before and after its [bounded conform write](#the-bounded-conform-write) and again after the SVG export: `ki repo audit --skill ki-repo-harness --repo <worktree>` (CAP-2, CAP-3, CAP-4), and after the export `ki repo audit --skill ki-diagrams --repo <worktree>`.
6. The judgment reads: KI-LINK-3, REF-2 (each new reference cited from `SKILL.md` with when to read it), COLL-2 for 6c, and SPEC-1 itself against the other two homed texts once all three land.

The pre-commit hook runs lint-staged (rumdl and Biome), `tsc` for staged `.ts` and the staged-snapshot `ki-skills` audit; a commit it refuses is fixed, never bypassed. Fleet findings outside the run's own files are reported apart from failures in its change.

One finding for 6a: `ki-work-package`'s `scripts/shared/rubric.ts` is an older copy than `ki-skills`' provider (it lacks `packageScripts`); `judgment` exists in both, so SPEC-1 does not need it refreshed, and 6a leaves it alone.

## Running the three in parallel

| Run | Writes | Starts |
| --- | --- | --- |
| 6a | `skills/governance/ki-work-package/**` only | Once ki.ways-of-working's ENTRY-NAMES harness run has integrated and its record is Ready |
| 6b | `skills/acquire/ki-acquire/**` only | On SPEC-TEXT, once its record is Ready |
| 6c | `skills/governance/ki-knowledge-package/**`, `.ki.toml`, `skill-functions.ts`, `ki-skills/SKILL.md`, then the generated `skills/README.md`, `README.md` and four `docs/diagrams/` files | On SPEC-TEXT, once its record is Ready |

The write sets are disjoint, and 6a and 6b change no description, so the catalogue and diagrams are generated by 6c alone. Parallel agents in one repository each use their own Git worktree, under the background-run standard's isolation rule, and Git integration is serialised:

- **Worktrees:** each run works in `~/.local/state/ki/agents/<run>/worktrees/ki-agentic-harness`, on its own branch from local `main` at its immutable baseline, never in the primary checkout. Before it reports `DONE` it removes the worktree with `git worktree remove`; its branch is deleted only once merged.
- **Commit by path:** each run stages and commits only its own paths and never bypasses the hook; a commit the hook refuses is fixed.
- **Gates in isolation:** `tsc`, `bun run test` and the hook's snapshot audit see only the run's own worktree. Findings outside the run's own files are reported apart from failures in its change.
- **Serialised integration:** after its review passes, each candidate integrates into the primary checkout's local `main` one at a time, inside the serialised Git write window `ki-git` requires: brought onto current `main` by rebase or a `--no-ff` merge, the [Verification](#verification) gates rerun on the combined result, then `main` advanced without force and the resulting commit recorded. A step that meets `.git/index.lock` waits and retries; it never deletes the lock.
- **Moved `main`:** a candidate whose content changes in integration returns to review; an unchanged candidate on a moved `main` needs revalidation, not fresh approval. 6c regenerates its generated paths if `main` has moved under it ([the bounded conform write](#the-bounded-conform-write)).

## What graduates

- `design/specs/` (`work.md`, `knowledge.md`, `acquire.md`, `work-house-profile.md`): kept until publication (plan step 8), which publishes from the homed references; then deleted at a mark.
- `design/specs/specs.md`: its shared conventions become SPEC-1 in each skill and its mapping table goes into the three `sources.md` entries; deleted at the mark after 6c lands.
- `design/spec-areas.md`: the plan keeps it until the knowledge skill lands; its inventory of the retired KEP and KIS-0002 material still serves plan steps 9 and 10, so move that inventory into the step 9 handoff record before deleting it.
- This note: deleted at the mark after all three land.

## What needs Kris

- **SPEC-TEXT**, with HOMING-EDITS folded into it, is with Kris and pending: accepting it accepts [the homing transform](#the-homing-transform) as part of the approved text.
- **Acceptance** of each delivered record under `ki-accept` comes to Kris after review and integration.
- **Decided:** CATALOGUE-WRITE (the one bounded write-mode conform) and HOMING-REVIEW (the records, review and acceptance route) were decided a) under OVERNIGHT-AUTONOMY at 01:13 BST on 20 October, after query-review-6 lifted both to high confidence, and this note carries their corrections. Everything else above is decided here within SPEC-HOME, KNOWLEDGE-SKILL and WORK-PROFILE.
