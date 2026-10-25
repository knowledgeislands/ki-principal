---
note_type: streams/design
title: Website docs - information architecture, Fable proposal
status: draft - October 2026
updated: 2026-10-25T03:10:00Z
author: Written with Claude
---

# Website docs: information architecture and content plan (Fable)

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Run:** wow-docs-design-fable · **Date:** 2026-10-25

**Authority:** DOCS-PUBLISH, Kris, 25 October 2026 02:52 GMT, in the work's [decisions log](../decisions.md): publish "what is", not what changed, for a reader who uses Knowledge Islands rather than develops it; skills first; diagrams made with the `archify` skill; Docs and Projects probably merge; the Voyage and the Field Guide stay. This note proposes. It changes nothing on the website; the Codex proposal is its sibling and the merge brief settles between them.

## Contents

1. [What the website is today](#1-what-the-website-is-today)
2. [The sources of truth](#2-the-sources-of-truth)
3. [Principles](#3-principles)
4. [Section structure and page list](#4-section-structure-and-page-list)
5. [Diagram list](#5-diagram-list)
6. [How pages stay true to their sources](#6-how-pages-stay-true-to-their-sources)
7. [The feature-area list](#7-the-feature-area-list)
8. [Docs and Projects](#8-docs-and-projects)
9. [Order of delivery](#9-order-of-delivery)
10. [Review list for Kris](#10-review-list-for-kris)
11. [Decisions made in this proposal](#11-decisions-made-in-this-proposal)

## 1. What the website is today

Surveyed at the local checkout of `apps-knowledgeislands.info`, 25 October 2026.

**Shape.** Eleventy 3, Nunjucks and Markdown on Bun, Tailwind 4, built to a portable `apps/site/dist/` served by Cloudflare Workers Static Assets. The header carries two groups, after the `ki-design` site structure: the **Voyage** (Philosophy, Model, Arcadia), read once in order, and the **Atlas** (Field Guide, Docs, Projects), returned to. The call to action is Enter Arcadia.

**Docs** is governed by `ADR-KI-WEBSITE-003`: everything that teaches lives in a Docs section, a finite ordered sequence a reader works through. A section is a directory `apps/site/src/docs/<section>/` bound by a directory data file, declared in `docsSections.json5` with only a slug, title and description; counts and first pages are derived at build. Six sections today: Get Started (1 hand-built page), The ki CLI (9), The Agentic Harness (10), Prompting (14), Optional Tools (6), Contribute (1). Every Markdown page needs `title`, `description`, a unique positive `order`, an opening claim of at least 120 characters before the first heading, no hand-off link text ("the full guide", "see the README"), and a `sources` declaration. Every page closes with its section's contents in reading order, so the landing grid links only each section's first page and `verify:reachable` proves the rest navigable.

**Projects** is the catalogue: one registry, `projects.json5`, 19 public repositories across six kinds (principal, capability, standard, tool, mcp, platform), each generated page answering five reader questions (problem, audience, capabilities, state, limits) plus how to start; released tools carry version, installer and manual, and `/install/<tool>` redirects to the pinned installer. A project whose slug matches a Docs section links to it in one sentence. `ADR-KI-WEBSITE-003` records the two questions as different: Projects answers "what is this", Docs answers "how do I".

**Truth-keeping.** Every published page declares its upstream in frontmatter (`repository`, `path`, `ref` pinned to a tag or 40-character commit, `governs`, `reviewed`) or `sources: original`; `partials/sources.njk` renders it as a provenance footer. `verify:provenance` gates the shape offline and, with `--network`, warns when a pinned ref is behind the newest release or the cited file has moved. Two pages are vendored rather than written: the skill catalogue (`sync:skills` parses the marker-delimited block in the harness `skills/README.md` into `skillCatalogue.json5`) and the command reference (`sync:cli` parses `man/ki.1` into `cliCommands.json5`). The Field Guide and `/arcadia/` vendor the symbol library, the painting and a dated islands snapshot the same way. Nothing is fetched during a build. The build runs `verify:routes`, `verify:projects`, `verify:provenance`, `verify:docs`, `verify:reachable` and `verify:prose` in sequence.

**What is stale.** The harness section was written for the harness as it stood on 11 October (`bd6e29b5`). Its skills page still names `ki-delegate`, lists six source domains where the harness now has eight (Acquire and Design were added), and says nothing of `ki-coordination`, `ki-work-package`, `ki-delegation`, `ki-work-design`, `ki-work-recurring`, `ki-diagrams`, `ki-trades` or the work model. The by-outcome page is hand-written and unchecked against the catalogue. The planning-and-delivery page describes the lifecycle as turning an audit into roadmap work, not the model Kris now runs. The ki section has no page on `ki agent` or `ki work`, which are the two groups a user of the work model meets first.

**Diagrams.** The site embeds no diagrams today beyond the drawn Arcadia chart and the Field Guide glyphs. `verify:prose` requires every element a Markdown page emits inside `.prose-ki` to be styled; `img` is, and inline `svg` and `figure` are exempt as generated chrome, so an SVG figure passes without a new rule. The harness already keeps living Archify diagrams under `docs/diagrams/` to the `ki-diagrams` standard: a manifest `diagrams.toml`, a committed source JSON, a self-contained SVG, and, under `commit_html = true`, the finalized interactive HTML and its receipt. It holds twelve today: the skill map, ten functional-area maps (Fundamentals, Records and code, Coordination, Work and delivery, Repository types, Agentic systems, Environment, Acquire, Signals, Design) and the thread model. Knowledge Islands Principal embeds `work-model.svg` beside the Work Process note. The standard's embedding rule is: a diagram is embedded as its SVG, never a screenshot, and the figure links onward to the interactive view, on a site "as an Interactive control that opens the viewer in an overlay, or in a new tab on a modified click". Nothing in the site's build consumes these yet; the website declares `ki-repo-website` and its content and Cloudflare deltas but not `ki-diagrams`.

## 2. The sources of truth

| Source | Where | What it fixes for the docs |
| --- | --- | --- |
| Skills | `ki-agentic-harness/skills/<domain>/<skill>/SKILL.md` and `references/standards-*.md`; 65 skills in eight source domains: acquire (4), agentic-systems (4), change-management (13), design (2), environment (9), governance (13), keystone (3), repo-structure (17) | Each skill's name, description, kind (governance or process), applicability, arguments, dependencies and runtime; the standards the feature pages restate |
| Generated catalogue | `skills/README.md`, marker-delimited, already vendored by the site | The per-skill inventory and counts |
| Functional areas | `skills/README.md` and `docs/diagrams/`, derived by `skill-graph.ts` | Ten skill groupings by function, each with a committed Archify diagram |
| `ki` | `ki --help`, `man ki` (`tools-ki/man/ki.1`, 17 command groups from General to Development, including Background agents, Work model, Batch records, Trades and Territory management), `ki agent --help`, `ki work --help` | The command surface and what each group may change |
| Work Process | `ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md`, canonical under `GDR-KI-PRINCIPAL-009` | The work model: levels, roles, the seven states, send and receive, the package, routing, decisions, the banner, Observatory fields |
| Coordination and package standards | `ki-coordination/references/standards-coordination.md`, `ki-work-package/references/standards-work-package.md`, `ki-delegation/references/standards-background-runs.md` | Reply forms, owner report, marks, On hold, run packet, authority footers |
| Interim policies | `+/_WORK/ki.ways-of-working/design/tending.md`, `findings.md`, `repository-metadata.md`, and `interim-cover.md`, which says rule by rule what the standards now carry and what does not yet have a home | Tending (two tracks, four structural and five PMO levels, captures upward); findings (what counts, the section, carrying, settlement) |
| Project note | `Streams/Projects/ways-of-working.md` | The outcome the docs serve and the dated ideas still open (graduate tending, finish findings graduation, GIT-SURFACE) |

## 3. Principles

1. **"What is", in the present tense.** A page says what a thing is, what it provides and how to use it. No changelog, no "formerly", no "now also". The provenance footer's `reviewed` date is the only date a page carries.
2. **The reader uses Knowledge Islands.** They run a Capital or a Project repository with the harness and `ki`, coordinate work with agents, and have not cloned the harness. Developer material (how to author a skill, the rubric engine, CI) stays in the repositories; the site carries it only where the reader needs it to act.
3. **Skills first, then the features they provide, then the command.** Three bodies: what a skill is and how the set hangs together; one page per feature area saying how to leverage it and which skills and commands provide it; the `ki` command as the thing you type.
4. **Text plus a diagram on every structural page.** Each feature page opens with a claim, then one diagram that shows how its parts sit together, then the prose.
5. **Carry, vendor, link**, under `GDR-KI-WEBSITE-002` and the site's own test: inventories are vendored at a pinned ref; explanations are carried with pinned `sources`; executable contracts and release artefacts are linked.
6. **Interim policy is published as interim.** Tending and findings are live practice on two territories and Kris named them; they are published with a one-line standing note ("interim policy, pioneered on Valle Armonia and Personal; graduation is an open idea in the Ways of working Project") rather than withheld.

## 4. Section structure and page list

The nav stays two groups. The Voyage is untouched. The Atlas becomes **Field Guide · Docs**, with Projects folded into Docs as section 8 below. The Docs landing grid runs in this order.

### 4.1 Get Started - `/docs/get-started/`

Unchanged in shape: one hand-built page. Its "first thing worth doing" paragraph points at Skills rather than at the harness internals. No new pages.

### 4.2 Skills - `/docs/skills/` (new section; skills first)

For: anyone deciding which skill to invoke, or wanting to see the whole set at once.

| Order | Path | Covers |
| --- | --- | --- |
| 1 | `/docs/skills/what-a-skill-is/` | What a skill is (the open Agent Skills standard, `SKILL.md`, Claude Code and Codex discovery); the two kinds, governance with EDUCATE, AUDIT, CONFORM and REFRESH plus a mechanical checker, and process; how a skill fires (trigger or `/name`), arguments and modes, what to do when the wrong one loads; `ki-self`. Merges today's "Skills and journeys" and "Use skills", rewritten. |
| 2 | `/docs/skills/how-the-skills-fit-together/` | The map: eight source domains, ten functional areas, dependencies (`ki-depends-on`), and which skills a Capital, a Project repository and a website typically declare. Carries the vendored skill map and functional-area diagrams. Links each functional area to the feature pages it serves. |
| 3 | `/docs/skills/catalogue/` | The vendored inventory, as today, refreshed to the current harness ref, with one addition per entry: the feature areas it serves, derived from the site's crosswalk (section 6). |
| 4 | `/docs/skills/by-outcome/` | Route a plain-language outcome to the smallest skill, rewritten against the current set and mechanically checked so every skill it names exists. |

### 4.3 Feature areas - `/docs/features/` (new section; the core of the work)

For: a reader who wants to leverage a capability and needs to know what it is, how it works, what to say, and which skills and commands do it. Every page has the same skeleton: an opening claim; one diagram; **What it is**; **How it works**; **How you use it** (what you say in a session, which skill fires, which `ki` command does what); **What it provides** (the artefacts: files, reports, records); **Boundaries** (what it deliberately does not do and which feature owns that); a generated **Provided by** box naming skills and commands; the provenance footer.

| Order | Path | Covers | For |
| --- | --- | --- | --- |
| 1 | `/docs/features/the-work-model/` | The unit is work. Territory, regular and Project work and work items; worker and supervisor; holder; the seven states and the two moves; On hold with its two reasons; the banner glyphs; themes; State of play as the hub that routes and stewards the method; the Capital and Known Lands as the territory's home. From the Work Process note. | Everyone; read first |
| 2 | `/docs/features/work-packages/` | The work folder `+/_WORK/<id>/` and its five files, what each holds and when it is read; the message queue; the decisions life cycle (logged, struck at a mark, reduced to a pointer); Git as the logbook and move commits; reports, briefs and design notes beside the package; tidying and close-out; `ki work status` and the five views. | Coordinators and anyone picking work up cold |
| 3 | `/docs/features/coordination/` | The coordinating thread as worker to Kris and supervisor of its runs; the responsive coordinator and its turn budget; the three reply forms; the owner report (heading, form line, Done, In Progress, Findings, Queries with lettered options, the banner and thread line); Summary, recap and full summary; the mark; On hold and the hold report; re-anchoring after compaction. | Anyone running or reading a coordinating thread |
| 4 | `/docs/features/delegation-and-background-runs/` | Detached runs under `ki agent`: the run packet, the brief and its authority footer, launch, queue and dispatch, status, wait and watch, send, the status line and report, receive and close, sweep; what a run may and may not do; the default deny list; the decisions log and `ki agent decide`. | Coordinators and anyone writing a brief |
| 5 | `/docs/features/the-roadmap-lifecycle/` | Flat work records, horizons and statuses; `ki-next` captures and selects, `ki-plan` readies, `ki-implement` delivers to awaiting review, `ki-accept` closes and prunes with approval; `ki-batch` as one authority envelope; adapters (`ki-work`: roadmap, Streams, GitHub Issues, Linear); the same states one level down from the work model; `ki link`. | Anyone who owns a roadmap |
| 6 | `/docs/features/recap/` | Closing a session: what `ki-recap` summarises, where learning goes, how it hands unfinished work to `ki-next`; the session digest in a knowledge base. Short. | Everyone |
| 7 | `/docs/features/trades/` | Directional trades of work and knowledge between repositories: routes, trade records, authority, receipt, decisions, release and pruning; `ki-trades` governs, `ki-trade` performs one side, `ki-next` disposes on receipt; `ki trade` commands; how a trade differs from a message between works. | Anyone moving work across repositories |
| 8 | `/docs/features/findings/` | An owner-requested investigation reported as a finding: tag, Goal, Scope, As of, the table; carried in full until a mark or until Kris is content; `findings/<tag>.md`; prompts to hand on; settlement with one disposition; findings and queries as independent. Marked interim; what is carried and what is still open, from the coverage assessment. | Coordinators and reviewers |
| 9 | `/docs/features/decision-records/` | Durable rationale: the typed records (ADR, GDR, ODR and the rest), where they live and how they are indexed; when a decision warrants a record and when the decisions log suffices; how a logged decision is struck once a record carries it; `ki-decision-records`. | Owners and anyone citing a decision |
| 10 | `/docs/features/tending/` | Continual tending of a territory: the structural track (four levels, mechanical to master checklist) and the PMO track (five levels, bottom up); how captures move upward; running a pass (skip empty levels, collapse repeats, shared repositories, no-remote briefs, where a run may not write); the lightweight report. Marked interim, with the pioneer evidence and the graduation idea named. | Capital stewards |
| 11 | `/docs/features/repository-standards/` | What makes a repository a Knowledge Islands repository: `.ki.toml`, the primary shapes (project, knowledge base, website, harness, MCP, tools, specifications, dotfiles, Homebrew tap) and their deltas; EDUCATE, AUDIT, CONFORM and REFRESH; `ki repo audit` and `conform`; which rubric an audit resolved; drift between declaration and reality; `ki-self`. Today's "Repositories" page, moved and rewritten. | Anyone onboarding or maintaining a repository |
| 12 | `/docs/features/knowledge-bases/` | A knowledge base's zones (Calendar, Pillars, Resources, Streams, `+` and `-`), index notes, Streams and the roadmap adapter, Activities and recurring work, live artifacts, the Capital overlay (Charter, Known Lands, memory root), acquisition and pulse. | Anyone keeping a knowledge base |
| 13 | `/docs/features/runtimes-and-context/` | Bindings (the portable MCP inventory and its Claude, Codex and chezmoi adapters), tokenomics and the standing surface, housekeeping, subagents; absorbs today's "Tune an agent session". Lighter depth. | Anyone tuning a runtime |

Thirteen pages. Pages 1 to 5 are the spine and ship first; 6 to 10 are the practices Kris named; 11 to 13 carry material the site already has, rehoused and corrected.

### 4.4 The ki CLI - `/docs/ki/` (kept, extended)

For: the reader at the keyboard.

| Order | Path | Change |
| --- | --- | --- |
| 1 | `/docs/ki/getting-started/` | Keep; refresh ref. |
| 2 | `/docs/ki/command-groups/` | Rewrite against the manual's 17 groups, each in one or two sentences, grouped by what it may change: your machine, one repository, the territory, the work. Diagram: the command-group tree. |
| 3 | `/docs/ki/work-and-agents/` | New: `ki work status` and its views; `ki agent` end to end (new, launch, queue, dispatch, status, wait, watch, send, decide, reconcile, home, close, sweep, recover, stop); `ki link`; `ki territory`. Written for the reader of the feature pages, which link here. |
| 4 | `/docs/ki/naming-and-locations/` | Keep. |
| 5 | `/docs/ki/commands/` | Vendored reference; refresh to the current release. |
| 6 | `/docs/ki/capability-lifecycle/` | Keep. |
| 7 | `/docs/ki/update-upgrade/` | Keep. |
| 8 | `/docs/ki/local-commands/` | Keep. |
| 9 | `/docs/ki/operator-guides/` | Keep; add trades, acquisition and estate where the manual documents them at release length. |
| 10 | `/docs/ki/chatgpt-local-capture/` | Keep. |

### 4.5 The Agentic Harness - `/docs/ki-agentic-harness/` (kept, narrowed)

For: the reader who wants to know what the harness is as an installed artefact. The skills pages move to Skills; repositories and tuning move to Feature areas; planning-and-delivery is retired into the roadmap lifecycle page. What remains: how the harness works (1), harnesses and installing one (2), onboarding a repository (3). Three pages, with redirects from the seven moved addresses. Its description on the grid changes to match.

### 4.6 Prompting, 4.7 Optional Tools, 4.8 Contribute

Unchanged.

### 4.9 Projects - `/projects/` (catalogue, joined to Docs)

See section 8. The catalogue stays at its addresses; the Docs landing gains it as its last block, "The projects: what each repository is and ships", and the nav entry goes. The other tools (mgit, git-almanac, rig, techne, the MCP servers) are documented at lighter depth here and nowhere else: their five questions and how to start are already what the catalogue carries.

### 4.10 Redirects

Every moved page keeps its old address with a 301 to its new home in one hop, as the site did for `/guidance/` and `/tooling/`: the seven harness pages, and nothing else moves.

## 5. Diagram list

Two provenances. **Vendored** diagrams already exist upstream under `ki-diagrams` and are taken at a pinned ref. **Site-owned** diagrams are authored in the website repository with the `archify` skill under the same standard. Each site-owned diagram is traced to the standards or note the page cites, and its `stale_when` names them.

| Page | Diagram | Archify type | Shows | Provenance |
| --- | --- | --- | --- | --- |
| Skills: how they fit together | Skill map | architecture | Every skill in its source domain, its functional areas and shape | Vendored: harness `skill-map` |
| Skills: how they fit together | Ten functional-area maps | architecture | For each area, its skills and the dependencies in and out | Vendored: harness `skill-area-*`, shown as a gallery with one open at a time |
| Features: the work model | The work model on one page | architecture | Territory, regular and Project work, work items, Kris, State of play; who sends what to whom | Vendored: ki-principal `work-model.svg` with its source, or redrawn site-owned if the source is not committed |
| Features: the work model | The seven states | lifecycle | With worker, Handoff to supervisor, With supervisor, Handoff to worker, Handoff to target, On hold (paused, more expected), Finished; the send, receive, pause, resume and finish transitions | Site-owned |
| Features: work packages | The work folder | tree | `+/_WORK/<id>/` with its five files, reports, briefs, `design/`, `findings/`; what each holds | Site-owned |
| Features: coordination | One coordinating turn | sequence | Kris, the coordinator, `messages.md`, a run and the report: message in, queue read, launch, status, receive, owner report, banner | Site-owned |
| Features: coordination | The thread model | workflow | Master and Project threads, background runs, what each may do | Vendored: harness `thread-model` |
| Features: delegation and background runs | A run's life | workflow | brief, `ki agent launch` or `queue`, run packet, status line, report, `wait`, receive, decisions log, `close`, `sweep`; the stop and recover branches | Site-owned |
| Features: the roadmap lifecycle | A record's statuses | lifecycle | triage, draft, ready, in-progress, awaiting-review, done, cancelled, hold; which skill makes each move; prune | Site-owned |
| Features: the roadmap lifecycle | The four skills in order | workflow | recap, next, plan, Ready, implement, Acceptance, accept, Done; `ki-batch` as the envelope around implement | Site-owned |
| Features: trades | One trade | sequence | Sender's `ki trade` offer, the route, the receiver's receipt and `ki-next` disposition, release and pruning | Site-owned |
| Features: findings | A finding's life | lifecycle | Requested, open and carried, refreshed, settled (homed in record, design note or log, or dropped) | Site-owned |
| Features: decision records | From decision to record | workflow | Kris's words logged, struck at a mark, homed as a Decision Record or standard, cited back | Site-owned |
| Features: tending | The two tracks | architecture | Structural levels 1 to 4 and PMO levels 1 to 5, the repository and territory they read, and the upward capture flow | Site-owned |
| Features: repository standards | The audit-conform cycle | workflow | Declare in `.ki.toml`, educate, audit, conform with confirmation, refresh; where CI runs it | Site-owned |
| Features: repository standards | Repository shapes | tree | Primary shapes and their deltas, with the skills each declares | Site-owned, derived from the catalogue's applicability |
| Features: knowledge bases | A knowledge base's zones | tree | Calendar, Pillars, Resources, Streams, `+`, `-`; Admin on a Capital | Site-owned |
| ki: command groups | The command groups | tree | The 17 groups by what each may change | Site-owned, derived from `cliCommands.json5` |

Eighteen diagrams, four vendored and fourteen site-owned (thirteen if the work model source is committed upstream). Each embeds as its SVG figure linking to the interactive viewer; see section 6.

## 6. How pages stay true to their sources

Three classes, and a check for each.

**Vendored.** The skill catalogue, the command reference and the upstream diagrams. A sync script fetches the artefact at an immutable ref, parses it strictly, writes a data file with its own provenance header, and the page renders it inside authored framing. Existing: `sync:skills`, `sync:cli`. New: `sync:diagrams`, which reads the upstream `docs/diagrams/diagrams.toml` at the pinned ref, copies each named SVG and, where `commit_html = true`, the HTML and receipt, into `src/_data/diagrams/<repo>/`, verifies the receipt's hashes against what it copied, and writes a manifest with the ref. Drift check: `verify:provenance --network` already warns when the pinned ref is behind; the page's `sources` entry names the manifest path.

**Generated skeleton with authored prose.** The feature pages. A site-owned crosswalk, `src/_data/featureAreas.json5`, lists each feature area once: slug, title, one-line description, the skills that provide it, the `ki` command groups it uses, its diagrams and the standards it restates. The page template renders the **Provided by** box, the catalogue renders "serves: ..." on each skill entry, and the Docs landing's Feature areas card and the by-outcome page draw their lists from the same file. The prose between the generated parts is authored. New gate, `verify:features`, run in the build: every skill the crosswalk names exists in `skillCatalogue.json5`; every command group exists in `cliCommands.json5`; every catalogue skill appears in at least one feature area or in an explicit `unassigned` list with a reason; every diagram the crosswalk names exists in the manifest; every feature page in `src/docs/features/` has a crosswalk entry and the reverse.

**Authored, with pinned sources.** The what-a-skill-is page, the feature pages' prose, the command-groups page. Each declares `sources` at a 40-character commit of the standard or note it restates (the harness standards, the Work Process note, the design notes for the interim policies), with `governs` naming the section drawn from and `reviewed` the date. New gate, `verify:skill-names`: every code span matching `ki-[a-z-]+` across `src/docs/` that is not in the catalogue fails the build, and every `ki <group>` span not in the command inventory warns; this is what would have caught `ki-delegate` and keeps a renamed skill from surviving in prose. The existing no-hand-off rule and opening-claim rule stay.

**Diagrams on the site.** The website declares `[skills.ki-diagrams]` and keeps its own diagrams under `docs/diagrams/` to the standard: source JSON, SVG, HTML and receipt, `commit_html = true` because the site serves them. The build passthrough-copies `docs/diagrams/*.svg` and `*.html` to `dist/diagrams/`. A page embeds a diagram with a `figure` shortcode that emits the SVG inline (so it follows the site's night toggle through the `ki` and `ki-night` forms, or the `dual` form if one SVG can carry both), a caption, and an **Interactive** link opening `/diagrams/<slug>.html` in a new tab; an overlay can follow later. `ki repo audit --skill ki-diagrams` becomes part of the site's gate, so a diagram whose receipt no longer matches its source fails before deploy. `verify:reachable` treats `dist/diagrams/` as assets, not pages. The refresh rule is the standard's: a change inside `stale_when` means regenerate and re-export; outside it, review and advance `last_checked`.

**Refresh cadence.** One sweep per harness or `ki` release: run the three syncs at the new refs, re-read every authored page whose `governs` section changed, advance `reviewed`, rebuild. The provenance sweep's warnings are the to-do list.

## 7. The feature-area list

The browsable list a reader meets on the Docs landing and at the head of the Feature areas section, in this order, each a page in section 4.3: **the work model** · **work packages** · **coordination** · **delegation and background runs** · **the roadmap lifecycle** · **recap** · **trades** · **findings** · **decision records** · **tending** · **repository standards** · **knowledge bases** · **runtimes and context**. The crosswalk gives each its skills and command groups; the catalogue shows the reverse. The harness's ten functional areas are a skill-centric grouping and stay on the Skills map page; the feature areas are reader-centric and site-owned, and each feature page names the functional areas it draws on.

## 8. Docs and Projects

Recommendation: **merge the navigation, keep the addresses.** The Atlas becomes Field Guide and Docs. The Docs landing adds a final block, the catalogue, listing the 19 projects by kind with their taglines, and the Projects landing gains the `← Docs` up-link. `/projects/` and `/projects/<slug>/` stay, because `/install/<tool>` and the machine routes, the redirects from `/tooling/`, and external links all resolve there, and because the catalogue is paginated from the registry rather than being a Docs section with an `order`. The "other tools at lighter depth" requirement is met by the catalogue entries as they are, so no new tool pages are written. The alternative, moving the catalogue under `/docs/projects/` with 301s, buys one less top-level path at the cost of a second redirect generation and a change to the tool-release sync; it can follow later without touching content.

## 9. Order of delivery

Units a single run can finish and verify, each ending with `bun run ki:site:build` green, the three `ki repo audit` gates passing, a commit by explicit path, and a push under DOCS-PUBLISH. Units 1 and 2 are prerequisites; 3 to 9 can run in parallel pairs where they touch different directories.

| Unit | Delivers | Verifies |
| --- | --- | --- |
| 1 Structure | `docsSections.json5` with Skills and Feature areas; directory data files; the Agentic Harness narrowed and its seven moved pages given redirects; nav merge and the catalogue block on the Docs landing; `featureAreas.json5` with all thirteen entries and `verify:features`; `verify:skill-names`. Existing pages moved, not yet rewritten. | Build green, every redirect resolves in one hop, gates pass |
| 2 Diagram pipeline | `[skills.ki-diagrams]` declared; `docs/diagrams/` with manifest and README; `sync:diagrams` vendoring the harness's twelve diagrams and ki-principal's work model at pinned refs; passthrough to `dist/diagrams/`; the `figure` shortcode; `ki-diagrams` audit in the gate; one site-owned diagram (the seven states) end to end as the proof | Build green, audit clean, the figure renders in both themes |
| 3 Skills | The four Skills pages, catalogue refreshed to the current ref with "serves" lines, by-outcome rewritten | `verify:skill-names` clean, provenance refs current |
| 4 Features A | The work model, work packages, coordination, with their five diagrams | Pages meet the skeleton, diagrams receipted |
| 5 Features B | Delegation and background runs, the roadmap lifecycle, recap, with three diagrams | As above |
| 6 Features C | Trades, findings, decision records, with three diagrams | As above |
| 7 Features D | Tending, repository standards, knowledge bases, runtimes and context, with four diagrams | As above |
| 8 ki | Command groups rewritten with its diagram; the new work-and-agents page; commands reference refreshed to the current release; operator guides extended | `sync:cli` at the release tag, provenance clean |
| 9 Review pack | The self-contained review prompt under REVIEW-DIGEST, pointing at the published pages, with the checklist and the digest shape | Kris can paste it; nothing else |

Nine units. A unit that cannot finish leaves its pages uncommitted and says where it stopped.

## 10. Review list for Kris

Pages to look at, in this order, once units 1 to 4 have landed:

1. `/docs/` - does the grid read as "skills first, then what you can do with them", and does the catalogue block at the foot feel like a merge or an afterthought?
2. `/docs/skills/how-the-skills-fit-together/` - is the vendored skill map legible on the site, in both themes, and is the Interactive link the right affordance?
3. `/docs/features/the-work-model/` - is this the page you would hand to a new territory owner, and does the states diagram match the Work Process note as you hold it?
4. `/docs/features/coordination/` and `/docs/features/delegation-and-background-runs/` - do the sequence and the run's life read as the practice you run, not as the standards paraphrased?
5. `/docs/features/tending/` and `/docs/features/findings/` - is the interim standing note the right weight?
6. `/docs/ki/work-and-agents/` - is this what you would want a reader to find when they type `ki agent --help` and want more?
7. `/projects/` - does it still make sense reached from Docs rather than from the nav?

Design questions to steer, in Kris's words rather than code:

- **Section names.** "Skills" and "Feature areas" are proposed; "Ways of working" was considered for the second and rejected as the Project's name rather than the reader's. Which words?
- **Feature-area set.** Thirteen pages are proposed. Should recap fold into the roadmap lifecycle, and runtimes and context into the harness section, to make eleven?
- **Interim standing.** Publish tending and findings now with a standing note, or hold them until the Project graduates them?
- **Diagram interaction.** New-tab Interactive link first, overlay later; or build the overlay in unit 2?
- **The catalogue's place.** Navigation merge with addresses kept (proposed), or a full move under `/docs/projects/`?
- **Theme forms.** One dual-theme SVG per diagram, or a `ki` and a `ki-night` export each? This decides whether the figure shortcode swaps files or lets CSS do it.
- **Depth of the ki pages.** The command reference is vendored and complete; the proposal adds one narrative page for work and agents. Is a narrative page per command group wanted, or is the manual enough beyond that?

## 11. Decisions made in this proposal

Each with the recommendation taken and a confidence.

| Tag | Decision | Recommendation | Confidence |
| --- | --- | --- | --- |
| IA-SKILLS-SECTION | Skills as their own Docs section, second on the grid, rather than pages inside the harness section | Own section; the owner said skills come first and the harness section is about the artefact | high |
| IA-FEATURES-SECTION | Feature areas as a Docs section of thirteen pages rather than a tag-style browse or a single long page | Section; `ADR-KI-WEBSITE-003` makes a section the unit a reader works through, and the gates already exist for it | high |
| IA-FEATURE-SET | Which feature areas get a page | The ten Kris named plus repository standards, knowledge bases, and runtimes and context, because the site already carries that material and it must be rehoused | medium |
| IA-RECAP-PAGE | Recap as its own short page | Own page; Kris listed it, and folding it would bury the one skill every session ends with | medium |
| IA-INTERIM | Publish tending and findings as interim | Publish with a standing note; the owner named tending explicitly and the coverage assessment says what is carried | medium |
| IA-PROJECTS-MERGE | How Docs and Projects merge | Navigation merge, addresses kept; the machine routes and redirects depend on `/projects/` | medium |
| IA-OTHER-TOOLS | Where the other tools are documented at lighter depth | The catalogue entries as they are, reached from Docs; no new pages | high |
| IA-HARNESS-NARROW | The harness section narrowed to three pages with redirects | Narrow; the moved pages are stale and belong to Skills and Features | high |
| IA-CROSSWALK | A site-owned `featureAreas.json5` as the generated skeleton behind feature pages, the catalogue's "serves" lines and the landing | Site-owned; the harness's functional areas are skill-centric and serve the map page instead | medium |
| IA-DIAGRAMS-STANDARD | The website adopts `ki-diagrams` for its own diagrams and vendors upstream ones by a sync at pinned refs | Adopt and vendor; one standard, one audit, receipts prove freshness | high |
| IA-DIAGRAM-EMBED | SVG figure inline with an Interactive link to the served viewer in a new tab | Figure plus link now, overlay later; matches the standard's embedding rule and needs no script | medium |
| IA-NAME-GATE | A build gate that fails on a skill name not in the catalogue | Add it; it is cheap and would have caught the present staleness | high |
| IA-SOURCES-PIN | Pin feature pages to standards at commit refs, including design notes for interim policy | Pin to commits; the provenance sweep then names the refresh owed | high |
| IA-NAV | Keep the two nav groups, Atlas reduced to Field Guide and Docs | Keep; the Voyage and the Field Guide stay per the owner | high |
| IA-URLS | `/docs/skills/`, `/docs/features/`, `/docs/ki/`, `/docs/ki-agentic-harness/` | As listed; only the harness pages move | high |
| IA-UNITS | Nine delivery units with structure and pipeline first | As listed; features can then run in parallel pairs | medium |
