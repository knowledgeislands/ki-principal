# Specifications plan: from drafts to published specs and the move

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.specifications` · **Date:** 2026-10-19

Written by the run plan under STOCKTAKE-PLAN (Kris, 19 October, 23:28 BST: "Can we take stock on this, and just double-check everything again, see if we can come up with a really solid plan?"). Read only beyond this file; nothing published. Every fact below was checked locally on 19 October against ki-principal, ki-agentic-harness at `f4d6c521`, ki-specifications at `e39fab5` and apps-knowledgeislands.info at `c3c2e81`. The live agentskills.io page was not read: the run's footer forbids network calls, so Agent Skills claims were checked against the harness's local reference, `ki-skills/references/standards-agent-skills.md`, last refreshed against the live page on 2026-09-26.

## Contents

- [Outcome](#outcome)
- [Where it stands](#where-it-stands)
- [Claims checked](#claims-checked)
- [The drafts against Kris's definitions](#the-drafts-against-kriss-definitions)
- [Steps](#steps)
- [Risks](#risks)
- [What the open queries miss](#what-the-open-queries-miss)

## Outcome

Three portable specifications, `work`, `knowledge` and `acquire`, each in the agentskills.io page format and built on progressive disclosure, are held in their owning harness skills, published from the same text at `knowledgeislands.info/specs/{work,knowledge,acquire}`, and handed to KI Specifications to become KIPs when it opens v1.

The move itself depends on Kris restarting KI Specifications, which this Project does not control; MOVE-GATE asks where the Project finishes.

## Where it stands

- Three drafts (`design/specs/`, draft 0.1) and the superseded stocktake (`design/spec-areas.md`) are in hand. Nothing is homed or published.
- Five queries are open (PROJECT-NAME, SPEC-HOME, ENTRY-NAMES, SPEC-VERSION, CONFORMANCE-LEVELS); every next step waits on them.
- HOOK-GUARD stands: no `ki repo conform` without `--dry-run` in any brief until ki.tools-burndown lifts it.

## Claims checked

✓ confirmed · ✗ wrong · ? unverifiable locally.

### PROJECT-NAME

| Claim | | Evidence |
| --- | --- | --- |
| `Streams/Projects/specifications.md` holds a different Project with the quoted outcome, under Model, `lifecycle: paused`, paused with the website on 2026-10-07, no open records | ✓ | The note; no record in ki-principal's Roadmap or ki-specifications' roadmap names `project: specifications` |
| It is registered in `Projects.md` | ✓ | `Projects.md`, "Specifications" section |
| The Model theme page has no entry for it | ✓, but beside the point | No theme page lists Projects (`model.md`, `foundations.md`, `rig.md`, `techne.md`), so state.md's next step 1, "register it ... on the Model theme page", is a step that does not exist |
| The work id `ki.specifications` requires the slug `specifications` | ✓ | `ki-coordination` Work naming: Project work id is `<territory>.<project>` |
| The review's reason, "Kris asked for a new Project" | Partly | Kris's words were "I wonder if I should start a project under model called specifications?": a new Project, and by that name |
| Not in the query: three other Project notes link `[[specifications]]` | Added | `website.md`, `trades-revamp.md`, `specification-review.md`; option c) must rewrite them |
| Not in the query: the paused Project's work is a prerequisite of this Project's last step | Added | KI Specifications today contradicts itself on numbering (`docs/numbering.md`: numbers "are never reused"; `specifications/README.md`: "The next number to assign is `KIS-0001`", a retired number) and still ships the retired Knowledge Package's templates (`minimal/`, `standard/`, `extended/`), schema (`$id` on `knowledgeislands.org`) and examples, named like the new `knowledge` spec |

### SPEC-HOME

| Claim | | Evidence |
| --- | --- | --- |
| Kris gave two homes, the owning skills or `knowledgeislands.info/specs/{work,knowledge,acquire}`, "in similar format to" agentskills.io | ✓ | ki.ways-of-working decisions at `a7872331`, 14:27 BST |
| The opener wrote `knowledgeislands.info/specifications/{name}` | ✓ | OPEN-PROJECT entry; Kris's own path is `/specs/` |
| "I want to get those spec'd within a skill that owns them for now, then we formalise out of them later" | ✓ | 14:17 BST entry |
| The drafts are tool-neutral | Partly ✗ | No tool names, but the `work` draft carries house practice; see [the drafts](#work) |
| `ki-work-package` and `ki-acquire` own two of them | ✓ | `ki-acquire` owns the source-independent acquisition contract; `ki-work-package` the house work package |
| `knowledge` has no owning skill | ✓ | No harness skill mentions a knowledge, context or curated package |
| The stocktake predates Kris's refined definition | ✓ | 14:17 stocktake request, 14:27 definition |
| Another session (Claude Design) works in the website | ? | Not visible locally; the site had 13 commits on 19 October, the last at 23:07 BST |
| The website Project is paused | ✓, but stale in practice | `website.md` says `lifecycle: paused`, yet SITE-046 and SITE-047 landed today |
| KI Specifications is on hold until its v1 | ✓ | Its README: "Do not add KIPs, KIS documents, or wider normative contracts until the overall Knowledge Islands v1 boundary is ready" |
| Not in the query: the site already publishes restated material with provenance | Added | Site `AGENTS.md`: every published page declares its upstream `sources`, gated by `verify:provenance`; teaching pages live in a Docs section declared in `docsSections.json5`. Publishing a skill-held spec fits this pattern exactly |

### ENTRY-NAMES

| Claim | | Evidence |
| --- | --- | --- |
| Agent Skills names the entry file `SKILL.md` | ✓ | Local reference §2 |
| Agent Skills "keeps every other file lower-case" | ? and likely ✗ | The local reference says nothing of it; from memory, the live page's own examples use `references/REFERENCE.md` and `FORMS.md`. SPEC-LIVE-READ settles it |
| The live work-package contract requires lower-case `work.md` and names readers that depend on it | ✓ | `standards-work-package.md`: `ki work status`, the Observatory, `ki agent close`, the rubrics |
| ki.ways-of-working would carry the rename "during its current migration pass" | ✗ stale | The pass has run: 12 packages in ki-principal, 33 `work.md` files across the local checkouts. A rename now is a second estate-wide pass, though installed `ki` 0.11.5 now reads the migrated shape |
| A case-only rename needs a two-step `git mv` on macOS | ✗ | Tested on this machine (APFS, case-insensitive, Git 2.56): one `git mv work.md WORK.md` stages the rename. The real hazard is different: on macOS a reader that still opens `work.md` keeps working by accident, so a missed reader fails only on Linux CI |
| Review: Agent Skills fixes one filename rather than a rule that entry files are upper case | ✓ | Local reference §2 |

### SPEC-VERSION

| Claim | | Evidence |
| --- | --- | --- |
| Agent Skills has no spec-version field | ✓ | Local reference §6: the optional fields are `license`, `compatibility`, `metadata` and `allowed-tools` |
| A skill's own version goes in `metadata.version` | ? | Not in the local reference; from memory the live page's `metadata` example carries `version` |
| The drafts add an optional `spec`, absence meaning version 1 | ✓ | `work.md` line 39, `knowledge.md` 35, `acquire.md` 38 |
| The drafts' validation lists do not check `spec` | ✓ | None of the three Validation sections names it |

### CONFORMANCE-LEVELS

| Claim | | Evidence |
| --- | --- | --- |
| Agent Skills has one level, size and quality being recommendations | ✓ | Local reference §7 and §14 (hard and soft) |
| The retired KIS-0001 had Minimal, Standard and Extended | ✓ | ki-specifications `32fc900`, KIS-0001 README and `conformance.md` |
| Not in the query: the graded templates are still in the tree | Added | `templates/minimal`, `standard`, `extended`, "no KIS document currently defines them normatively" |
| The drafts use one level, soft limits warned | ✓ | Each draft's Validation |

### The drafts' own claims about Agent Skills

Confirmed against the local reference: a package is a directory named for it; `SKILL.md` with YAML front matter and a Markdown body; the `name` rules (1-64, `a-z0-9-`, no leading, trailing or doubled hyphen, matches the directory); `description` non-empty and at most 1,024 characters; `license`, `compatibility` (at most 500), `metadata` (string to string) and experimental `allowed-tools`; optional `references/`, `scripts/` and `assets/`; references one level deep; soft limits of 500 lines and about 5,000 tokens; about 100 tokens of metadata; three disclosure tiers; a contents list over 100 lines; "Run" versus "See" for scripts; `skills-ref validate` checking front matter and naming only; and the `ki-acquire-*` mapping in `specs.md` (`ki-acquire-mutation-boundary: read-only` and `explicit-marker`, `ki-acquire-omissions`).

Wrong or overstated:

- All three list "an upper-case entry file" as reused from Agent Skills unchanged. Agent Skills fixes one name, `SKILL.md`; the general rule is the drafts' own.
- All three say "a reader ignores top-level keys it does not know". That is the drafts' rule, not Agent Skills', whose optional fields are a closed list.

Unverifiable locally, likely wrong:

- `knowledge.md` line 138, "Renamed `KNOWLEDGE.md` to `SKILL.md`, a conforming package is also a valid skill", and `acquire.md` line 148, "An acquire package is a skill whose task is acquisition". From memory, the reference validator `skills-ref` rejects top-level fields outside its allowed set, which `updated`, `acquired-with`, `spec`, `source`, `mutation`, `omissions` and `produces` all are. SPEC-LIVE-READ settles it; until then the claim should go.

## The drafts against Kris's definitions

### `work`

Kris: "essentially what we are doing with work packages, without inferring our ways of working". The shape passes: five files, definition apart from state, routing description, Agent Skills fields. The rules for working the files do not: they are the house's ways of working, restated.

- `messages.md` (lines 136-140): priority order, `IMPORTANT` lines on top taken one at a time, grouping, who may set priority. This is the `ki-coordination` queue discipline.
- `queries.md` (line 125): upper-case mnemonic tags, the recommended option first with its reason. This is the owner-query form.
- `decisions.md` (line 144): "in their own words", "what it authorises", reduction to a one-line pointer. This is the house decisions life cycle.
- `state.md` (line 121): `## Now` at most five lines, `## Next steps`, `## Held`, word caps.
- Disclosure (line 154) and `description` (line 84): a "Register" tier read by "whoever routes new work", and the "Takes ... Not for (neighbour)" formula, are State of play's routing.
- Line 148, "Scripts and tool output do not belong": a house tidy rule.

The fix: the spec states the files and their minimum format (one entry per query, message or decision, with what each entry must carry) and recommends nothing about how a team works them; the house disciplines move into the house profile in `ki-work-package`. Separately, the four-value `state` and the `name` and `updated` fields mean the house package does not conform as built (`specs.md` lines 53-66): `id` would become `name`, `since` `updated`, seven states would map to four and `work.md` might become `WORK.md`. Nothing asks whether the house must conform; WORK-PROFILE does.

### `knowledge`

Kris: a reader "should be able to understand from the description ... that this knowledge package effectively is the thing to give me that information", then "a collection of Markdown files ... in a similar way to the way that skills work". The draft meets the test: the description names the topic and its edges, the questions it answers, its close neighbours and the asker's words (lines 69-77), and the body is a set of Markdown files in `references/` listed from a Contents section. Gaps:

- Kris's example is learning a topic, not only answering a question. The description guidance has no cue for audience or depth (introductory or reference), which is what tells a learner whether the package suits them.
- Currency sits outside the first tier: `updated` is not read with `name` and `description` (line 116), though the draft says a reader weighs a package by it. Put `updated` in tier 1.
- The package is "kept current by someone who stands behind it" (line 9), but nothing names that someone. Recommend `metadata.owner` or a Sources line.
- The "also a valid skill" claim should go unless SPEC-LIVE-READ confirms it.

### `acquire`

Kris: "how we would go about acquiring knowledge. So not knowledge at rest, but knowledge acquisition itself ... based on how you use a particular tool". The draft is about acquisition itself, and covers a tool both as the source and as the means (`source`, line 78, with "git command-line help and man pages" as an example). Gaps:

- Its required sections come from `ki-acquire`'s archival capture contract: enumerate every identity, reconcile counts, checksums, coverage levels. That fits bulk capture (meetings, trackers) but over-specifies the lighter case Kris named, learning a tool from its own help. Keep Output and Verification required, and make checksums and coverage levels recommended.
- Curation, the step that turns a run's capture into a knowledge package, belongs to neither spec. `produces` and `acquired-with` link the two ends, but nothing says what curation must do or record. One paragraph in `knowledge` (Sources) would cover it.
- Its required top-level `source` and `mutation`, like `knowledge`'s added fields, need the SPEC-LIVE-READ answer before the "is a skill" sentence stands.

### Shared

- The shared conventions are restated in each spec. Keep each spec self-contained, as Agent Skills is, and add a drift check (one rubric criterion per owning skill naming the shared fields) rather than a fourth shared document.
- The text follows the agentskills.io page closely, in structure and in some sentences. Before publication, its licence and the attribution it needs must be known (in SPEC-LIVE-READ).

## Steps

| Step | Deliverable | Repository | Gate | Runs beside |
| --- | --- | --- | --- | --- |
| 1. live-check | Dated note `design/agentskills-check.md`: the live specification, its examples' file names, `metadata.version`, `skills-ref`'s handling of unknown fields, and the licence of the spec text | ki-principal (this work folder) | SPEC-LIVE-READ | 2 |
| 2. project-note | `specifications.md` conformed or renamed as PROJECT-NAME sets, its `Projects.md` entry, the `outcome` linked from `work.md` Goals; no theme-page entry, since theme pages list no Projects | ki-principal (Streams) | PROJECT-NAME, MOVE-GATE (for the outcome's last clause) | 1. If PROJECT-NAME b) renames this folder, everything after waits for it |
| 3. revise-drafts | `design/specs/` at draft 0.2: the answers to ENTRY-NAMES, SPEC-VERSION, CONFORMANCE-LEVELS and WORK-PROFILE; the live-check findings; the gaps under [The drafts](#the-drafts-against-kriss-definitions); validation checking `spec`; the house profile mapping in `specs.md` rewritten to the WORK-PROFILE answer | ki-principal (this work folder) | Those four answers, and step 1 | Nothing: it rewrites the same files |
| 4. drafts-review | One blind review of draft 0.2 against Kris's definitions and the live check, under Codex at high effort | ki-principal (this work folder) | Kris accepting this plan | Nothing |
| 5. text-approval | Kris approves the three texts, or sends them back | Owner | A new query, SPEC-TEXT, raised with step 4's report | Nothing |
| 6a. home-work | `ki-work-package/references/standards-work-spec.md`, linked from `SKILL.md`, with rubric and sources lines, beside the house standard, which it does not change | ki-agentic-harness | SPEC-HOME a), step 5; a harness record under `ki-next`, Steward review | 6b, 6c; chained after any ki.ways-of-working run writing `ki-work-package` |
| 6b. home-acquire | `ki-acquire/references/standards-acquire-spec.md`, same pattern | ki-agentic-harness | SPEC-HOME a), step 5; harness record | 6a, 6c |
| 6c. home-knowledge | The new skill KNOWLEDGE-SKILL names, with `references/standards-knowledge-spec.md`, rubric and sources | ki-agentic-harness | SPEC-HOME a), KNOWLEDGE-SKILL, step 5; harness record | 6a, 6b; the generated catalogue is regenerated once, after the last of 6a-6c |
| 7. house-profile | Only if WORK-PROFILE asks for conformance: a line to ki.ways-of-working's `messages.md` for the house renames, and the reader changes it needs (`ki work status`, the Observatory, `ki agent close`, the rubric) routed through it to ki.tools-burndown and ki.observatory | Other works | WORK-PROFILE | After 6a |
| 8. publish | A handoff record in the website's roadmap: three pages at `/specs/work/`, `/specs/knowledge/`, `/specs/acquire/` (or the path SPEC-PUBLISH sets), each declaring its skill reference as its `sources`; Kris approves before anything deploys | apps-knowledgeislands.info | A new query, SPEC-PUBLISH (go-ahead and path), raised after step 6; the website's own owner session | Step 9 |
| 9. specs-readiness | The paused Project's repository review and the KBEP and KBIP dispositions, plus the numbering contradiction and the retired Knowledge Package's templates, schema and examples, so the move lands in a consistent repository | ki-specifications | PROJECT-NAME a); Kris lifting its pause | Step 8 |
| 10. move | A blocking handoff record in ki-specifications' roadmap for three KIPs, each citing its skill reference as the reference implementation; on acceptance the skills and the site point at the KIS | ki-specifications | MOVE-GATE; Kris restarting KI Specifications at its v1 boundary | Nothing |

In short: answers first, then steps 1 and 2 together, then 3, 4 and 5 in a line; then the three homing runs together; then publication and the ki-specifications clean-up together; the move last. Every brief carries HOOK-GUARD.

`design/spec-areas.md` graduates at step 6c: its framing is superseded, but its inventory of the retired KEP and KIS-0002 material serves steps 9 and 10, so it is kept until the knowledge skill lands, then deleted.

## Risks

- **Agent Skills facts are second-hand.** The local reference was last refreshed on 26 September. Three claims (lower-case files, `metadata.version`, unknown fields) rest on memory until step 1.
- **Copied text and licence.** The drafts follow agentskills.io closely; publishing a near copy without its licence's attribution is outward-facing and hard to take back.
- **One name, three meanings.** "Knowledge package" has meant the retired KIS-0001, acquire's sealed capture (the KEP, still named "Knowledge Exchange Package" in tools-ki's `docs/specs/acquisition.md` and capture guides) and now the curated `knowledge` package; ki-specifications still ships the first under that name. Readers will confuse them at publication and at the move unless step 9 clears the old ones.
- **KI Specifications contradicts itself on numbering**, and its schema `$id` sits on `knowledgeislands.org` while the site is `knowledgeislands.info`.
- **The house moves under the spec.** ki.ways-of-working keeps changing `ki-work-package` (GFM, banners, method reads). Without the drift check, the portable `work` and the house standard part company.
- **`work` absorbs ways of working.** The draft already restates house practice; every revision risks more. Step 4's review checks this first.
- **Case-insensitive file system.** Any entry-file rename is masked on macOS and surfaces on Linux CI.
- **The website is busy.** Its Project is marked paused but is committed to daily; publication must go through its own owner session and roadmap, not a run from here.
- **Harness review latency.** Each homing candidate needs the harness Steward's independent review.
- **No validator.** Until rubric criteria land in the owning skills, nothing checks a package; `ki repo audit` sees skills, not arbitrary packages.

## What the open queries miss

- **WORK-PROFILE**: whether the house work package must conform to `work`, and when. ENTRY-NAMES is one part of it; `id`, `since` and the state values are the rest.
- **KNOWLEDGE-SKILL**: SPEC-HOME a) needs "a new skill for `knowledge`", but nothing names it or places it.
- **SPEC-LIVE-READ**: authority for the one read-only network check that three claims and the licence rest on.
- **MOVE-GATE**: whether the Project finishes at publication with a blocking handoff to KI Specifications, or stays open until KI Specifications restarts.
- **Corrections**: PROJECT-NAME gains Kris's own words and the fact that the paused Project's work is a prerequisite of the move; ENTRY-NAMES loses the "every other file lower-case" claim (unverified), the two-step rename (wrong) and the current migration pass (already run).
- **Later queries, raised when their step comes**: SPEC-TEXT (step 5) and SPEC-PUBLISH (step 8).
- **Decided here, no query needed**: each portable spec sits in its skill as `references/standards-<name>-spec.md`, inside `ki-skills`' closed references vocabulary and apart from the house standard; each spec stays self-contained with a drift check.
