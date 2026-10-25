# Website documentation plan - the merged design

Design note of [KI > Model > Ways of working](../work.md), written by the `wow-docs-merge` run on 25 October 2026 from the Fable and Codex proposals (`design/website-docs-fable.md` at `7700e558` and `design/website-docs-codex.md` at `0c177a7e`, both removed in the commit that adds this note) under DOCS-PUBLISH, REVIEW-DIGEST, "REVIEW-DIGEST refined" and DOCS-IA-MERGE in the [decisions log](../decisions.md). Kris delegated the design choices to this merge and steers by reviewing published pages through the [review pack](review-pack.md). Delivery runs follow the briefs in [`briefs/`](../briefs/wow-docs-order.md).

The reader is a user of Knowledge Islands, not a developer of it. Every page says what a thing is, how it works, how the reader uses it and what it provides, in a form readable without running the tools. The website shows only the settled current state. It never mentions open owner queries; an interim practice is described as it works now and labelled interim.

## Contents

- [Section structure](#section-structure)
- [Page list](#page-list)
- [Diagram list](#diagram-list)
- [Staying true to the sources](#staying-true-to-the-sources)
- [Feature areas](#feature-areas)
- [Docs and Projects](#docs-and-projects)
- [Decisions settled](#decisions-settled)

## Section structure

Voyage is untouched: Philosophy, Model and Arcadia. Atlas becomes two entries, Field Guide and Docs; the Projects catalogue keeps its address and is reached from the Docs landing page (see [Docs and Projects](#docs-and-projects)).

Docs holds nine sections, in this reading order on the landing grid. The first six exist today; three are new. Every section is declared in `apps/site/src/_data/docsSections.json5` and bound by its directory data file, as the website's docs-sections guide requires.

| Order | Section | Slug | What it answers |
| --- | --- | --- | --- |
| 1 | Get Started | `get-started` | Where to begin, unchanged |
| 2 | Skills | `skills` | What a skill is, how the sixty-four fit together, which one serves which outcome |
| 3 | Ways of working | `ways-of-working` | How work is defined, held, moved, delegated, traded, tended and finished |
| 4 | Knowledge | `knowledge` | How an island keeps, queries, acquires and hands over knowledge |
| 5 | Standards | `standards` | What every repository, record, codebase, document and diagram conforms to |
| 6 | The ki CLI | `ki` | The command surface at its pinned release, from a user's view |
| 7 | KI Agentic Harness | `ki-agentic-harness` | Installing, running and tuning a harness and its agent environment |
| 8 | Prompting | `prompting` | Unchanged |
| 9 | Optional tools | `optional-tools` | Unchanged |
| 10 | Contribute | `contribute` | Unchanged |

Skills comes first after Get Started because Kris asked for skills first, then the `ki` command and tools from a user's view. The three new sections sit between Skills and the CLI because they explain what the skills and commands do; the CLI and harness sections then show the surfaces that do it.

## Page list

Each new Markdown page follows one skeleton: an opening claim of at least 120 characters saying what the reader will be able to do; one figure where a diagram answers a question prose cannot, two at most; `## What it is`, `## How it works`, `## How you use it`, `## What it provides`, `## Boundaries`; a `Provided by` box generated from the feature-area crosswalk naming the skills and commands; and the provenance footer the prose layout renders from `sources`. An interim practice carries a one-paragraph `Interim` callout directly under the opening claim, saying what is settled, what is in use and where the standard will live.

Moved pages keep a `301` in `apps/site/src/redirects.njk`. Pages not named here are unchanged. Every page's `sources` pin the harness at `8897008f`, `tools-ki` at `v0.13.0` or `ki-principal` at the commit the delivery run reads, with `reviewed` set to the delivery date.

### Skills, `/docs/skills/`

| Order | Path | Page | Sources |
| --- | --- | --- | --- |
| 1 | `/docs/skills/what-a-skill-is/` | Kinds of skill, the Educate, Audit and Conform modes, applicability, where a skill lives and how a runtime loads it. Moved from `/docs/ki-agentic-harness/skills/` and rewritten | `ki-skills`, `ki-repo-harness` |
| 2 | `/docs/skills/how-the-skills-fit-together/` | The ten functional areas, which skills each gathers and how they rely on one another; carries the skill map and the ten area diagrams | harness `skills/README.md`, `docs/diagrams/` |
| 3 | `/docs/skills/catalogue/` | The vendored capability catalogue, refreshed to `8897008f` with 64 skills, grouped by functional area with the source concern beside each. Moved from `/docs/ki-agentic-harness/skill-catalogue/` | harness `skills/README.md` between the catalogue markers |
| 4 | `/docs/skills/by-outcome/` | Which skill to reach for by what the reader wants to achieve. Moved from `/docs/ki-agentic-harness/skills-by-outcome/` and rewritten against the 64 | the catalogue and the crosswalk |

### Ways of working, `/docs/ways-of-working/`

| Order | Path | Page | Sources |
| --- | --- | --- | --- |
| 1 | `/docs/ways-of-working/the-work-model/` | The unit is work; supervisor and worker; the seven states; send and receive; the mark | Work Process note |
| 2 | `/docs/ways-of-working/work-packages/` | The work folder `+/_WORK/<id>/`, its five files, `design/`, `briefs/`, findings, tidy and close-out | `ki-work-package` |
| 3 | `/docs/ways-of-working/coordination/` | The responsive coordinator, its turn budget, the owner report, queries and options, the banner and thread line, the three reply forms | `ki-coordination` |
| 4 | `/docs/ways-of-working/background-runs/` | Detached runs, the run packet, status and report files, authority tiers, grants and the deny list, unattended windows, the run queue | `ki-delegation`, `tools-ki` `ki agent` |
| 5 | `/docs/ways-of-working/roadmap-lifecycle/` | Work adapters, horizons, record statuses, the four lifecycle skills and batches. Moved from `/docs/ki-agentic-harness/planning-and-delivery/` and rewritten | `ki-work`, `ki-work-roadmap`, `ki-next`, `ki-plan`, `ki-implement`, `ki-accept`, `ki-batch` |
| 6 | `/docs/ways-of-working/work-design/` | Shaping an undecided model: brief, independent reviews, merged report, owner decisions, piloted rollout | `ki-work-design` |
| 7 | `/docs/ways-of-working/trades/` | Directional work and knowledge trades between repositories: routes, records, receipt, release | `ki-trades`, `ki-trade` |
| 8 | `/docs/ways-of-working/recurring-work/` | Regular occurrences, Activity notes, how a recurrence is adopted and evidenced | `ki-work-recurring`, `ki-repo-kb-activities` |
| 9 | `/docs/ways-of-working/findings/` | Interim. A finding's file, table and dispositions as they work now | `design/findings.md`, `ki-coordination` Findings |
| 10 | `/docs/ways-of-working/tending/` | Interim, in depth. The two tracks, four structural and five PMO levels, upward capture, the focus rule, write boundaries and lightweight reporting | `design/tending.md`, `interim-cover.md` |

### Knowledge, `/docs/knowledge/`

| Order | Path | Page | Sources |
| --- | --- | --- | --- |
| 1 | `/docs/knowledge/knowledge-bases/` | Zones: Calendar, Pillars, Resources, Streams, `+` and `-`; index notes; the Capital and principal overlay; live artifacts | `ki-repo-kb`, `ki-repo-kb-principal`, `ki-repo-kb-live-artifacts` |
| 2 | `/docs/knowledge/query-save-update/` | The working loop: querying, saving, updating, linking and session digests | `ki-repo-kb` |
| 3 | `/docs/knowledge/acquiring-knowledge/` | Exception-based capture from agent sessions, ChatGPT, Granola and pulses into an island | `ki-acquire` and its adapters, `ki-pulse` |
| 4 | `/docs/knowledge/recap-and-handover/` | Recapping a live session and routing durable learning, as the skill works at the pinned ref | `ki-recap` |

### Standards, `/docs/standards/`

| Order | Path | Page | Sources |
| --- | --- | --- | --- |
| 1 | `/docs/standards/repository-standards/` | `.ki.toml`, shapes, the universal contract, the audit and conform loop, `+` and `-`; an Interim section on repository metadata as it works now | `ki-repo`, `ki-repo-*`, `design/repository-metadata.md` |
| 2 | `/docs/standards/decision-records/` | Typed records, when a decision warrants one, the path from a logged decision to durable rationale | `ki-decision-records` |
| 3 | `/docs/standards/engineering-and-git/` | TypeScript and Bun engineering, Conventional Commits, explicit staging, shared-tree safety | `ki-engineering`, `ki-git` |
| 4 | `/docs/standards/writing/` | Markdown, TOML, READMEs, guides and specifications: how KI documents are written and placed | `ki-authoring`, `ki-guides`, `ki-specs` |
| 5 | `/docs/standards/diagrams/` | Archify, the five types, committed forms, the manifest, embedding, privacy and regeneration | `ki-diagrams` |

### The ki CLI, `/docs/ki/`

The nine existing pages stay at their addresses and are refreshed to `v0.13.0`: `sync:cli` at that tag, every version mention and `sources.ref` advanced, prose checked against the manual. Three pages are added so that all eighteen manual groups have a home.

| Order | Path | Change |
| --- | --- | --- |
| 1-9 | existing pages | Refreshed; `command-groups` is rewritten around the eighteen groups and carries the command-groups diagram |
| 10 | `/docs/ki/work-and-agents/` | Work model, Background agents and Batch records groups from a user's view |
| 11 | `/docs/ki/repositories-and-territory/` | Registry, Repository management, Repository options, Harness management, Territory management and Estate convergence |
| 12 | `/docs/ki/trades-and-acquisition/` | Trades, Acquisition and Knowledge Base search |

### KI Agentic Harness, `/docs/ki-agentic-harness/`

Six pages stay: how-the-harness-works, installing-a-harness, onboarding, repositories, using-skills, tuning, each refreshed to `8897008f`. Four leave with redirects: `skills`, `skills-by-outcome` and `skill-catalogue` to the Skills section, `planning-and-delivery` to `/docs/ways-of-working/roadmap-lifecycle/`. One is added.

| Order | Path | Page | Sources |
| --- | --- | --- | --- |
| 7 | `/docs/ki-agentic-harness/agent-environment/` | Bindings, tokenomics and housekeeping: the portable MCP inventory, context budgets and runtime adapters for Claude and Codex | `ki-binding*`, `ki-tokenomics*`, `ki-housekeeping-*` |

## Diagram list

Every diagram is an Archify diagram under the `ki-diagrams` standard: one of the five manifest types, a committed JSON source, a committed SVG and, because the website serves the interactive view, `commit_html = true` with the HTML and receipt beside it. Twelve are vendored from the harness at `8897008f`; the rest are owned by the website in its own `docs/diagrams/` with `docs/diagrams/diagrams.toml`, the website declaring `[skills.ki-diagrams]` in `.ki.toml`. A site-owned diagram that explains a model rather than code lists the notes or skill files it draws from in `traced`, as the standard's island rule allows.

| Slug | Type | What it shows | Source | Page |
| --- | --- | --- | --- | --- |
| `skill-map` | architecture | Every skill by source concern, functional area and shape | vendored, harness | how-the-skills-fit-together |
| `skill-area-fundamentals` and the other nine `skill-area-*` | architecture | One functional area's skills and what they rely on | vendored, harness | how-the-skills-fit-together |
| `thread-model` | workflow | A coordinating thread, its runs and its returns | vendored, harness | coordination |
| `work-model` | architecture | Supervisor, worker, the work, its package and the two moves | site, traced to the Work Process note | the-work-model |
| `seven-states` | lifecycle | The seven states and the moves between them | site, Work Process note | the-work-model |
| `work-folder` | architecture | `+/_WORK/<id>/` with its five files, `design/`, `briefs/`, findings and the review holding area | site, `ki-work-package` | work-packages |
| `coordinating-turn` | sequence | Owner message, coordinator turn, launch, wake, receive, report | site, `ki-coordination` | coordination |
| `background-run` | sequence | Brief, launch, status marks, report, receive, prune | site, `ki-delegation` | background-runs |
| `record-lifecycle` | lifecycle | A record from captured through adopted, ready, awaiting review, done and pruned | site, `ki-work-roadmap` | roadmap-lifecycle |
| `work-design-loop` | workflow | Brief, independent reviews, merge, decisions, pilot | site, `ki-work-design` | work-design |
| `trade` | sequence | A trade between two repositories without transferred ownership | site, `ki-trades` | trades |
| `recurring-occurrence` | workflow | A recurrence adopted, scheduled, evidenced and reviewed | site, `ki-work-recurring` | recurring-work |
| `finding-life` | lifecycle | A finding opened, carried, settled and homed, as practised now | site, `design/findings.md` | findings |
| `tending-tracks` | architecture | The structural and PMO tracks, their levels and upward capture | site, `design/tending.md` | tending |
| `tending-pass` | workflow | One tending pass from focus to report | site, `design/tending.md` | tending |
| `kb-zones` | architecture | An island's zones and the directional areas | site, `ki-repo-kb` | knowledge-bases |
| `query-save-update` | workflow | The knowledge loop within a session | site, `ki-repo-kb` | query-save-update |
| `acquisition-flow` | dataflow | Capture sources through the acquire adapters into an island | site, `ki-acquire` | acquiring-knowledge |
| `recap-handover` | workflow | A recap's routes for changes, decisions and learning | site, `ki-recap` | recap-and-handover |
| `repository-shapes` | architecture | Shapes and overlays a `.ki.toml` can declare | site, `ki-repo` | repository-standards |
| `audit-conform` | workflow | Educate, audit, conform and re-audit | site, `ki-repo` | repository-standards |
| `decision-to-record` | workflow | From a logged owner decision to a typed record | site, `ki-decision-records` | decision-records |
| `standards-layers` | architecture | Universal contract, shape overlays, repository choices | site, `ki-repo`, `ki-engineering` | engineering-and-git |
| `diagram-regeneration` | workflow | Source, build, export, receipt, freshness check | site, `ki-diagrams` | diagrams |
| `command-groups` | architecture | The eighteen manual groups and what each operates on | site, `man/ki.1` at `v0.13.0` | ki/command-groups |
| `agent-environment` | architecture | Portable inventory, runtime bindings and budgets | site, `ki-binding`, `ki-tokenomics` | agent-environment |

Embedding, from the standard: the SVG is placed inline by a `figure` shortcode, never as a screenshot, with a caption and an `Interactive` link opening the committed HTML in a new tab from `/diagrams/<slug>.html`, served by passthrough copy so no Eleventy transform touches it. An overlay viewer is later work. The SVG form is `ki`, the `ki-design` day palette, placed on a parchment panel so it reads under both the day and night charts; the interactive view carries Archify's own dual theme.

## Staying true to the sources

Three kinds of page, one rule each.

- **Vendored** pages (`catalogue`, `commands`, the diagrams) reproduce an upstream artefact through a sync script at an immutable ref and never reword it. `sync:skills` and `sync:cli` exist; `sync:diagrams` is new and copies the twelve harness diagrams, their HTML and their manifest entries into `apps/site/src/assets/diagrams/vendored/ki-agentic-harness/` with a generated `src/_data/vendoredDiagrams.json5` recording the ref. A page's declared `sources.ref` must equal the snapshot's ref, and `verify:provenance` already fails the build when they disagree.
- **Authored** pages restate a source for the reader and declare it in `sources` with `governs` and `reviewed`. The refresh sweep is `verify:provenance -- --network`, run by a person, which warns when a pinned source has moved.
- **Generated skeleton with authored prose**: the `Provided by` box on each feature page is rendered from `apps/site/src/_data/featureAreas.json5`, the crosswalk, so a skill rename upstream fails a check rather than leaving stale prose.

Three new gates run inside `bun run ki:site:build` after the existing six.

| Gate | What it refuses |
| --- | --- |
| `verify:skill-names` | Any `ki-[a-z-]+` token in `src/docs/` that is not a skill in the vendored catalogue or a command in the vendored inventory |
| `verify:features` | A crosswalk area naming a skill absent from the catalogue or a page that does not exist; a page in the three new sections claimed by no area or by two |
| `verify:diagrams` | A figure whose slug is in neither the site manifest nor the vendored data; a site diagram whose receipt fails `build-html.ts --check`; a vendored diagram whose ref differs from the page's declared harness ref |

The three audits the website already runs stay the acceptance bar for every unit: `ki repo audit --skill ki-repo-website-content`, `--skill ki-engineering` and `--skill ki-authoring`, with `--skill ki-diagrams` added once the manifest exists.

Versions are coherent by construction: the site describes `tools-ki` at `v0.13.0` only, the last reviewed release, although its `main` is nineteen commits further on; the harness at `8897008f`, the commit the skill set was read from. Advancing either is one change touching the sync, the `sources` and the prose together.

## Feature areas

The feature-area list is a planning view: the areas the reader must be able to understand, each mapped to the skills and commands that provide it and to the page that explains it. It lives in the crosswalk file and is what `verify:features` checks. Sixteen areas: the thirteen Fable proposed, with Codex's work design, recurring work and acquisition added because each is a skill of its own with a distinct outcome, and Fable's recap and runtimes kept as Knowledge and harness pages respectively.

| Area | Skills and commands | Page |
| --- | --- | --- |
| The work model | `ki-coordination`, `ki-work-package`, Work Process note | the-work-model |
| Work packages | `ki-work-package` | work-packages |
| Coordination | `ki-coordination`, `ki-subagents*` | coordination |
| Delegation and background runs | `ki-delegation`, `ki agent` | background-runs |
| Roadmap lifecycle | `ki-work`, `ki-work-roadmap`, `ki-work-github-issues`, `ki-work-linear`, `ki-next`, `ki-plan`, `ki-implement`, `ki-accept`, `ki-batch`, `ki batch` | roadmap-lifecycle |
| Work design | `ki-work-design` | work-design |
| Trades | `ki-trades`, `ki-trade`, `ki trade` | trades |
| Recurring work | `ki-work-recurring`, `ki-repo-kb-activities` | recurring-work |
| Findings, interim | `ki-coordination` Findings section | findings |
| Tending, interim | the two tracks in `design/tending.md`, `ki-repo-kb`, `ki-work-roadmap`, `ki-accept` | tending |
| Knowledge bases | `ki-repo-kb`, `ki-repo-kb-principal`, `ki-repo-kb-streams`, `ki-repo-kb-live-artifacts` | knowledge-bases, query-save-update |
| Acquisition | `ki-acquire`, `ki-acquire-chatgpt`, `ki-acquire-granola`, `ki-pulse`, `ki acquire` | acquiring-knowledge |
| Recap | `ki-recap` | recap-and-handover |
| Repository standards | `ki-repo`, `ki-repo-*`, `ki-bootstrap`, `ki repo` | repository-standards |
| Decision records, engineering, writing, diagrams | `ki-decision-records`, `ki-engineering`, `ki-git`, `ki-authoring`, `ki-guides`, `ki-specs`, `ki-diagrams` | the other four Standards pages |
| Agent environment | `ki-binding*`, `ki-tokenomics*`, `ki-housekeeping-*`, `ki-agentic-radar`, `ki-model-radar` | agent-environment |

### Tending in depth

The tending page is the one place the whole practice is written for a reader, labelled interim throughout because its standard home is not yet chosen. It covers, from `design/tending.md` and the INTERIM-TENDING finding in `design/interim-cover.md`: the two tracks, structural and PMO; the four structural levels and five PMO levels and what each looks at; how each level picks up the captures of the level below; the focus rule that keeps a pass to one question; the write boundaries, which files a pass may change and which it may only report on; the lightweight report a pass ends with; and the running pass as practised in the Capital, Valle Armonia and the personal territory, described without naming private repositories or people. The `tending-tracks` architecture and the `tending-pass` workflow carry it. Nothing on the page proposes tooling or a future home.

## Docs and Projects

Kris's steer was that Docs and Projects can probably go together. They do, by navigation rather than by moving pages.

- Atlas shows Field Guide and Docs. Projects leaves the navigation.
- The Docs landing page gains a catalogue block below the section grid: every project card, generated from `projects.json5` as `/projects/` generates them today, with its one-sentence ownership line.
- `/projects/` and every `/projects/<slug>/` keep their addresses. They are the catalogue, the target of the `/install/<tool>` and `/tooling/` redirects and the `projectPages.ts` generator; a project page links to its Docs section in one sentence as it does now.
- Nothing moves to `/docs/ecosystem/`. Moving seventeen pages and their redirects would change addresses without changing what a reader understands.

## Gate baseline

Decided by the coordinator under DOCS-PUBLISH at 04:23 GMT on 25 October 2026. The engineering audit's DEPS-1 dependency-age failure (`@types/node`, `rumdl` and Bun past the adoption window) and its CI-1 warning are the pre-existing baseline. Every delivery unit commits and pushes under them once the site build with all its gates, the tests, the typecheck and the website-content, authoring and diagrams audits pass, and names DEPS-1 in its report. No unit installs or updates dependencies: that is separate maintenance outside the night's window. Commit only your own paths by explicit path; other units may be working in the same checkout.

## Linking back from Skills by outcome

Decided by the coordinator under DOCS-PUBLISH at 04:42 GMT on 25 October 2026. `/docs/skills/by-outcome/` names the Ways of working, Knowledge, Standards and Harness pages as unlinked text until they exist. The unit that lands each page adds its link in `apps/site/src/docs/skills/by-outcome.md` in the same commit, and points the two Design rows at their page if it lands one.

## Decisions settled

Where the proposals agreed the agreement is adopted; where they differed the choice and its reason are one line each.

| Tag | Decision | Reason |
| --- | --- | --- |
| IA-SKILLS-FIRST | Skills is the first section after Get Started; the CLI and harness follow the three explanatory sections | Kris's order: skills, then the command and tools from a user's view |
| IA-SECTION-NAMES | Three sections named Ways of working, Knowledge and Standards rather than one "Feature areas" | A reader looks for how work moves or how knowledge is kept; "feature area" is the plan's word, not theirs |
| IA-PAGE-COUNT | Nineteen new explanatory pages, Fable's skeleton on each, plus three CLI and one harness page | Fable's thirteen left acquisition, work design and recurring work with no home; Codex's fifty-odd made no unit finishable in one run |
| IA-PER-SKILL | No per-skill pages | The vendored catalogue already carries each description without drift; sixty-four pages would restate SKILL.md |
| IA-PROJECTS | Navigation merge, addresses kept, catalogue block on the Docs landing | Install routes, redirects and the generator all address `/projects/`; a move changes URLs, not understanding |
| IA-HARNESS | Harness section keeps six pages and gains agent-environment; the three skills pages and planning-and-delivery move out | The harness section is about running a harness; what you get and how work moves belong to Skills and Ways of working |
| IA-CLI | Nine existing CLI pages refreshed to `v0.13.0`, command-groups rewritten, three pages added for the groups nothing covered | Eighteen groups need a home without a page per group |
| IA-CLI-RELEASE | The site describes `tools-ki` at `v0.13.0` only | A page citing `main` records nothing a sweep can compare, and the open preview question is not published |
| IA-HARNESS-REF | Skills, catalogue and every skill-sourced page pin harness `8897008f` | The current pin lacks six live skills and carries three retired ones |
| IA-INTERIM | Interim practices are published as they work now with one `Interim` callout; no "proposed" label anywhere | The website shows only the settled current state and never mentions open queries |
| IA-DIAGRAM-TYPES | Only the five manifest types; tree-shaped things are drawn as architecture | The `ki-diagrams` audit validates `type` against the five |
| IA-DIAGRAM-HOME | Harness diagrams vendored at the pinned ref through `sync:diagrams`; every other diagram owned by the website under its own manifest | A diagram lives with the repository whose change would make it stale |
| IA-WORK-MODEL-SVG | The `work-model` diagram is site-owned and traced to the Work Process note, not vendored from `ki-principal` | `ki-principal` has no diagrams manifest, so nothing there can be checked for freshness |
| IA-DIAGRAM-EMBED | Inline SVG through a `figure` shortcode with an `Interactive` link to the committed HTML in a new tab; overlay later | The standard's embedding rule, with the smallest first step |
| IA-SVG-FORM | `ki` form on a parchment panel; interactive view dual-themed | One static form per diagram, legible under both charts |
| IA-GATES | `verify:skill-names`, `verify:features` and `verify:diagrams` join the build | Each catches a drift that no existing gate sees |
| IA-EXAMPLES | Worked examples use a fictional island and fictional people | The diagrams privacy rule and the public site both forbid naming a private repository or a person |
| IA-REDIRECTS | One `301` per moved page, in `redirects.njk` beside the existing blocks | Every published address keeps resolving in one hop |
| IA-UNITS | Ten delivery units, structure and diagram pipeline first, then Skills, then the CLI, each finishable by one run | A unit changing a generator or shared layout precedes the pages that use it |
| IA-REVIEW | Kris steers from the review pack, not from queries; the pack lists the choices most worth his steer | DOCS-IA-MERGE: no design choice reaches `queries.md` |
