---
note_type: streams/design
status: proposal
author: Written with Codex
updated: 2026-10-25
---

# Consumer documentation: information architecture and content plan

This is the Codex proposal for DOCS-PUBLISH, for comparison with the independent Fable proposal and a coordinator-owned merge. It proposes publication work; it changes no website, skill, policy, command or work record. Kris's bounded instruction on 25 October 2026 authorises this design note.

## Findings

### DOCS-IA - Skills first, with visible source status

**Goal:** Kris asked on 25 October 2026 for a consumer documentation architecture explaining what KI provides, skills first, with Archify diagrams and a website review list.

**Scope:** The local website, 64 harness skill declarations and their relevant standards, CLI help and manual, Work Process, Project note and interim design policies; no website edits or external research.

**As of:** 25 October 2026, local source survey completed at 03:02 GMT.

Recommend one Docs destination with feature guides, individual skill explanations, the CLI manual and an ecosystem directory. The website currently snapshots 61 skills and a v0.11.0 command inventory while advertising ki v0.13.0; the current harness has 64 skills. Tending needs substantial coverage with an interim label. The detailed page map, diagram briefs, source controls, delivery units and decisions below are the proposal for review.

## Recommendation

Publish an explanation of using KI, organised around what a person wants to do. The first route is understanding and choosing skills; installation is an available next step. A reader should finish a feature guide able to explain the outcome, recognise when to use it, understand the human decisions and know which skill or command supplies each part, without running anything.

Merge Docs and Projects as a reader destination, under **Docs**. Keep a clearly named **Tools and ecosystem** directory within it. Preserve the Voyage, its Philosophy, Model and Arcadia routes, and the Field Guide. Do not move philosophy into a product manual or create a change-history section in place of documentation.

Use three complementary ways in: **browse a feature**, **choose a skill**, and **look up a command or tool**. They share content and cross-links. They are not three independently maintained accounts of the same behaviour. Technical ownership appears in Sources; it should not force readers to understand repository names before they can choose a page.

The hierarchy is a proposal, not an adopted contract:

```text
Voyage                         unchanged
  Philosophy / Model / Arcadia
Atlas
  Field Guide                  unchanged
  Docs
    Skills                     first: choose, understand, catalogue, skill details
    Ways of working            coordination, delivery, tending and exchange
    Knowledge                  keep, acquire, query and reuse knowledge
    Standards                  what adopting KI gives a repository
    Get started                an optional practical entry
    Harness                    install, activate and use skills in an agent
    ki command                 explanation, tasks and complete reference
    Tools and ecosystem        the present Projects catalogue, at lighter depth
    Prompting / Optional tools / Contribute
```

## What exists and how it is published

### Website survey

The website's tracked `AGENTS.md` was read before its content and build sources. At survey time:

- Header navigation has **Voyage**: Philosophy `/philosophy/`, Model `/model/`, Arcadia `/arcadia/`; and **Atlas**: Field Guide `/field-guide/`, Docs `/docs/`, Projects `/projects/`. The home page `/` and the Arcadia call to action are additional entry points. There is no separate Voyage route to migrate. `/specifications` currently redirects home and must not be advertised as an existing manual.
- Docs declares six sections in `apps/site/src/_data/docsSections.json5`: Get Started, The ki CLI, The Agentic Harness, Prompting, Optional Tools and Contribute. There are 39 Markdown pages: 9 CLI, 10 harness, 14 prompting and 6 optional-tool pages, plus Nunjucks landings. Section membership and prose layout come from directory data; each page has a unique positive `order`. Sections are finite ordered bodies, with derived page counts, a first-page link and a contents footer.
- Projects is a generated directory, backed by `projects.json5` and `projectPages.ts`, rather than a second documentation source. Its 17 entries cover principals, capabilities, standards, five released tools, six MCP services and platforms. `tools.ts` projects released tools from that same registry. Entries carry purpose, audience, capabilities, state, limits and usage; versioned tools also carry release and installation metadata. The website entry already routes home.
- Pages are Markdown with Nunjucks, or Nunjucks templates, in `apps/site/src/`. Eleventy 3 runs on Bun; Tailwind 4 builds CSS; output is `apps/site/dist/`, served as Cloudflare Workers Static Assets. HTML transforms add external-link icons and turn internal `href`, `src` and `srcset` addresses into portable relative output links. A clean build is required after route removals because old output can survive.
- The normal build uses committed snapshots, not live upstream reads. `sync-skill-catalogue.ts` vendors the harness's marker-delimited generated inventory; `sync-cli-commands.ts` parses both SYNOPSIS and COMMAND GROUPS from `man/ki.1`. Both synchronisers fetch immutable upstream refs when explicitly run. Do not run them under a no-remote brief. A local-source import mode would be new work, not an existing option.
- Other generated or vendored material includes `ki-design` tokens, symbols, artwork and chart assets, and Arcadia's dated snapshot from the Capital's territory inventory. This proposal leaves those surfaces alone.
- `layouts/page.njk` renders authored prose, section contents and `partials/sources.njk`. Frontmatter `sources` identifies repository, path, immutable ref, governed material and review date; `sources: original` is an explicit authorship claim. Existing build gates cover tool routes, project fields, source declarations, Docs shape, reachability and prose styling. The optional network provenance sweep detects upstream movement; declaration validity alone does not prove prose remains accurate.

The relevant evidence is the site's `AGENTS.md`, `apps/site/eleventy.config.ts`, `apps/site/package.json`, `_data/{site.ts,docsSections.json5,projects.json5,skillCatalogue.json5,cliCommands.json5}`, `_includes/{layouts/page.njk,partials/sources.njk}`, `redirects.njk`, the sync/verify scripts and `docs/guides/developer/{docs-sections,page-provenance,projects-directory,what-to-publish,prose-styling}.md`.

### Source survey and authority

The local survey anchors are website `2628c4897e7d1024a8aaa4587bf58f22667048e2`, harness `8897008fcee7b2c71a22115735ed038efccf7f32`, tools-ki `2f57c62661a9f521cfc173e090c5365be13e0412` and principal `eea391390bcc98baad625c379777ce423489450f`. These are evidence anchors for this proposal, not recommended publication versions. The Project note and `interim-cover.md` also had local changes at inspection; treat those readings as provisional, not as content already available at the principal commit.

- **Skills:** `ki-agentic-harness/skills/*/*/SKILL.md` supplies the 64 current names, descriptions, kinds, declared dependencies, modes and off-ramps. Relevant references supply the actual procedures and authority boundaries: coordination, background runs, work packages, next/plan/implementation/acceptance, batch and outcome authority, adapters and roadmap shape, design, trades and trade operations, recurring work, recap, knowledge-base modes and Decision Records. The generated capability catalogue is an inventory interface; a description and dependency list do not constitute a complete consumer manual.
- **CLI:** both installed `ki --help` and `man ki` were read; the executable reports 0.13.0. The source manual is `tools-ki/man/ki.1`, with 18 command groups and additional paths, environment, files, development-installation and exit-status sections. It covers repository governance and work records, batches, knowledge search, registry/harness/skill activation, trades, territories, acquisition, background agents, work views, estate operations and local diagnostics. Root help and the manual have different jobs; examples must be checked against the actual command path's help before publication.
- **Work model:** [Work Process](<../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) owns the conceptual levels, roles, seven states, send/receive, hold, views and cascade. A theme is a label. A package holds work above the item level; a work item lives in its own record. Coordinator state, record lifecycle and run state must have distinct diagrams and vocabulary.
- **Programme and policy status:** [Ways of working](../../../../Streams/Projects/ways-of-working.md), [skill set](skill-set.md), [tending](tending.md), [findings](findings.md), [repository metadata](repository-metadata.md) and [interim coverage](interim-cover.md) identify active design and residual gaps. The design folder's other briefs and reviews are historical or prospective evidence, not blanket authority. In particular, older Project diagram descriptions mentioning `ki-pmo`, checkpoints or reply blocks must not become current instructions.
- **Diagram contracts:** `archify` supplies the renderer and reader. Harness `ki-diagrams` supplies committed source, SVG, manifest, freshness and optional committed HTML with a receipt. Its current manifest admits architecture, workflow, sequence, dataflow and lifecycle; all diagrams proposed here fit those five types.

The website inventory pins harness `bd6e29b5e0d567fb5ebb83566ddd46b3f6ba778b`, with 61 entries. Relative to the current 64, it lacks `ki-acquire`, `ki-coordination`, `ki-design-system`, `ki-work-design`, `ki-work-package` and `ki-work-recurring`, and still includes retired `ki-checkpoint`, `ki-design-loop` and `ki-work-housekeeping`. Its command snapshot pins v0.11.0 although the project registry advertises v0.13.0. Those differences require deliberate refresh and semantic review, not just a new displayed count.

### Status the prose must preserve

Use a short visible status note on affected pages: **Available**, **Interim practice**, or **Proposed**. Name the reviewed source revision/date. These labels describe the particular feature, not the whole ecosystem's maturity.

- The core coordination/report contract, five package files and permitted findings storage are carried in the inspected standards. The canonical filenames are `work.md`, `state.md`, `queries.md`, `messages.md` and `decisions.md`; permitted supporting material is governed by the package's closed list. Do not teach five files as an absolute prohibition on findings or design material.
- Tending's full four-level structural and five-level PMO process remains interim. Its care, assignment and other component rules are partly carried, while the complete recurring process and tooling candidates are not a released `ki-tending` skill or a `ki tend` command. The guide must explain the process in detail without inventing either.
- Findings' main report/storage contract has landed; refresh on changed facts, independent settlement/traceability, a directly named run writer and an age warning still have residual choices in the interim assessment. Teach the adopted contract and mark each extension accurately.
- Repository metadata taxonomy, mirror direction, homepage safeguards and checker extensions remain interim in that assessment. Explain present repository standards; place prospective metadata behaviour in a small, labelled subsection, with no made-up configuration fields.
- Planned adapter contracts are not implemented remote workflows: `ki-next` currently stops on GitHub Issues and Linear adapters. Similarly, `ki work status` is a read projection, not authority to transition work. Unattended authority is bounded by the actual grant and standards; examples cannot imply that a tool grants acceptance or deployment permission.

Before each later publication unit, re-read its sources and the owner's latest decisions. This note does not freeze the interim assessment while other work progresses.

## Page map

All paths below are proposed canonical public URLs, except where explicitly retained. Each list gives coverage, reader and production mode. **Authored** means website-owned consumer prose derived from cited sources; **generated** means an exact source projection; **hybrid** means generated facts and navigation with reviewed authored explanation. Every page must state a useful opening claim and answer its promised question on the website.

### Skills: the first destination

- `/docs/skills/`: choose by desired outcome, see the feature-area browser and follow three example journeys. For new and returning KI users. Hybrid: generated membership with authored labels and routing.
- `/docs/skills/how-skills-work/`: what a skill supplies, governance versus process, modes, invocation, required dependencies, optional augmentation, and the difference between a standard and an executable command. For any reader unfamiliar with agent skills. Authored, with a small source-derived dependency example.
- `/docs/skills/catalogue/`: every current skill, filterable by feature and searchable by name, with useful no-JavaScript grouped lists. For readers who know a term or want to inspect coverage. Generated metadata with authored feature assignments; do not substitute the catalogue for explanations.
- `/docs/skills/<skill-name>/`: one hybrid detail page per skill listed below. For the audience named for its family, also reachable from every associated feature guide. Each detail answers: what this gives you; when to use it; what to bring; what happens; outputs and their home; modes with meaningful differences; human decisions; limits; a worked example; related skills/features/commands; status and Sources. Aim for the depth needed to answer those questions, usually 400-800 words, rather than a uniform word quota.

The following is the complete 64-page detail expansion. Every listed path is a page, not a proposed new skill. Family introductions below specify what each covers and for whom; individual distinctions are made explicit where adjacent names are easy to confuse.

**Start and operate a repository:** for someone adopting KI or maintaining an island. Explain installation guidance, universal repository coverage and reusable capability standards respectively.

- `/docs/skills/ki-bootstrap/`: activate KI and choose the supported harness path; the CLI performs installation.
- `/docs/skills/ki-repo/`: universal repository declaration and governance, including which narrower standards apply.
- `/docs/skills/ki-skills/`: what makes a reusable skill conform and how its dependencies and shared concerns work; deeper material for skill maintainers.

**Coordinate work:** for an owner, coordinator or person resuming work. Explain who holds work, what survives a chat and what each handoff actually transfers.

- `/docs/skills/ki-coordination/`: coordinator behaviour, states, reports, queries, marks, message receipt and holds.
- `/docs/skills/ki-work-package/`: the package's five entry files, supporting material, progressive reading and stewardship.
- `/docs/skills/ki-delegation/`: background-run briefs, authority, run packets, reporting and high-risk packets.
- `/docs/skills/ki-recap/`: recap one live session, outstanding work and durable learning routes.

**Select and deliver work:** for an owner, planner, worker or reviewer. Explain the distinct transitions and artefacts instead of presenting a single automatic pipeline.

- `/docs/skills/ki-work/`: select the repository's authoritative forward-work adapter and resolve Projects/themes.
- `/docs/skills/ki-work-roadmap/`: horizons, record shape, dependencies and retained terminal evidence.
- `/docs/skills/ki-next/`: capture substantive deferred work, triage and select/adopt it.
- `/docs/skills/ki-plan/`: enrich selected drafts until Ready, without creating a second tracker.
- `/docs/skills/ki-implement/`: implement an approved Ready record and return verification at Awaiting review.
- `/docs/skills/ki-accept/`: human-approved completion, cancellation and explicitly selected pruning.
- `/docs/skills/ki-batch/`: bind an exact Ready set to bounded authority and record outcomes.
- `/docs/skills/ki-work-design/`: shape an undecided model through brief, independent reviews, merged report and pilot.
- `/docs/skills/ki-work-recurring/`: define recurring work that produces ordinary work when due.
- `/docs/skills/ki-work-github-issues/`: declared adapter contract and current execution limits.
- `/docs/skills/ki-work-linear/`: declared adapter contract and current execution limits.

**Trade between islands:** for a sender or receiver of work or knowledge. Explain delivery, receipt and disposition as separate facts.

- `/docs/skills/ki-trades/`: routes, immutable submissions, receiver authority and observation policy.
- `/docs/skills/ki-trade/`: operate one local side of a trade; receiver decisions route to `ki-next`.

**Keep knowledge:** for island authors, researchers and maintainers. Explain the base model and each specialised overlay's benefit.

- `/docs/skills/ki-repo-kb/`: zones, query/save/update, linking, metadata, extraction and digest.
- `/docs/skills/ki-repo-kb-principal/`: Capital governance, Charter, Known Lands and Enactment.
- `/docs/skills/ki-repo-kb-streams/`: place flat work records within a knowledge base.
- `/docs/skills/ki-repo-kb-activities/`: durable Activity definitions and scheduling evidence.
- `/docs/skills/ki-repo-kb-live-artifacts/`: keep Markdown and rendered HTML views in sync.
- `/docs/skills/ki-acquire/`: acquisition contract, sources, packets and ownership before assimilation.
- `/docs/skills/ki-acquire-chatgpt/`: readable ChatGPT conversation acquisition under that contract.
- `/docs/skills/ki-acquire-granola/`: Granola meeting acquisition under that contract.
- `/docs/skills/ki-pulse/`: prepare a bounded briefing from available sources; explain configuration and source limits.

**Write, decide and verify:** for anyone maintaining useful knowledge; engineering pages also serve repository maintainers.

- `/docs/skills/ki-authoring/`: house Markdown/TOML presentation and durable placement.
- `/docs/skills/ki-decision-records/`: typed rationale, ownership and decision lifecycle.
- `/docs/skills/ki-guides/`: reader-facing procedures and guide organisation.
- `/docs/skills/ki-specs/`: accepted behaviour, normative language and evidence.
- `/docs/skills/ki-diagrams/`: living Archify sources, SVG/HTML, receipts and freshness.
- `/docs/skills/ki-engineering/`: TypeScript/Bun standards, boundaries and verification.
- `/docs/skills/ki-git/`: commit boundaries, shared-tree safety and publication authority.

**Choose a repository type:** for an adopter deciding which standards to declare. Each detail explains its particular structure, checks and outputs, linking back to the universal repository page.

- `/docs/skills/ki-repo-project/`: general project repository.
- `/docs/skills/ki-repo-harness/`: reusable agentic capability repository.
- `/docs/skills/ki-repo-tools/`: executable distribution and readiness.
- `/docs/skills/ki-repo-mcp/`: MCP implementation and engineering seams.
- `/docs/skills/ki-repo-specifications/`: a normative specification corpus.
- `/docs/skills/ki-repo-homebrew-tap/`: formulae and release transport.
- `/docs/skills/ki-repo-dotfiles-chezmoi/`: managed personal configuration and safe rendering.
- `/docs/skills/ki-repo-website/`: portable website lifecycle.
- `/docs/skills/ki-repo-website-content/`: content-site implementation.
- `/docs/skills/ki-repo-website-app/`: interactive app-site implementation.
- `/docs/skills/ki-repo-website-cloudflare/`: hosting overlay and its explicit operational boundaries.

**Configure and inspect an agent environment:** for a user selecting a supported runtime or a configuration maintainer. Portable policy and runtime evidence must be clearly distinguished.

- `/docs/skills/ki-binding/`: portable MCP inventory and client targeting.
- `/docs/skills/ki-binding-chatgpt/`: Codex MCP projection and drift.
- `/docs/skills/ki-binding-claude/`: Claude MCP projections.
- `/docs/skills/ki-binding-chezmoi/`: managed rendering of the portable inventory.
- `/docs/skills/ki-tokenomics/`: context budgets and model-purpose policy.
- `/docs/skills/ki-tokenomics-chatgpt/`: local Codex evidence, with effective-session limits.
- `/docs/skills/ki-tokenomics-claude/`: corresponding Claude evidence.
- `/docs/skills/ki-housekeeping-chatgpt/`: local-store evidence, memory and reviewed session cleanup.
- `/docs/skills/ki-housekeeping-claude/`: corresponding Claude housekeeping.

**Collaborate, design and keep watch:** for users choosing how to organise agent work, create an interface or review model/tool developments.

- `/docs/skills/ki-subagents/`: portable roles and task boundaries for in-session helpers.
- `/docs/skills/ki-subagents-chatgpt/`: Codex-specific evidence and constraints.
- `/docs/skills/ki-subagents-claude/`: Claude-specific evidence and constraints.
- `/docs/skills/ki-agent-coordination-paperclip/`: KI's Paperclip operating model; optional, not a prerequisite for normal coordination.
- `/docs/skills/ki-design-inspiration/`: visual exploration and reference-led design choices.
- `/docs/skills/ki-design-system/`: a coherent interface language and reusable design decisions.
- `/docs/skills/ki-agentic-radar/`: review developments in agent systems and record relevant evidence.
- `/docs/skills/ki-model-radar/`: review model developments against an explicit purpose.

### Ways of working

These are authored feature guides with cited standards, realistic worked examples and the diagrams specified later. They serve owners and practitioners before runtime operators. Each names the supplying skills and the relevant CLI page without making a command necessary to understand it.

- `/docs/ways-of-working/`: the work model, levels/forms, roles, states and five views. For everyone organising work; diagram FIG-01.
- `/docs/ways-of-working/coordination/`: when coordination helps, receiving/sending, steering, queries, Summary/recap/full summary, marks, hold/drain/resume and finishing. For owners and coordinators; FIG-02.
- `/docs/ways-of-working/work-packages/`: the five files, optional closed-list material, messages, findings, resumption and durable knowledge boundaries. For anyone handing work over or picking it up; FIG-03.
- `/docs/ways-of-working/background-runs/`: when to delegate, a good brief, exact authority, a run's progress/report, receipt and close-out. For supervisors and workers; FIG-04.
- `/docs/ways-of-working/agent-teams/`: detached runs, in-session subagents and optional Paperclip, with their different lifetimes and authority. For people choosing an execution arrangement; an authored comparison, linking FIG-04.
- `/docs/ways-of-working/roadmap-lifecycle/`: triage, selection, horizons, Draft/Ready/In progress/Awaiting review/Done or Cancelled, and separate retention/pruning. For owners, planners and reviewers; FIG-05.
- `/docs/ways-of-working/work-design/`: when a question needs design before a record, independent reviews, decisions and a pilot. For owners of an undecided model; FIG-06.
- `/docs/ways-of-working/batch-work/`: exact-set reviewed-item versus outcome authority, expiry, verification and return. For owners considering a bounded autonomous window; a worked envelope, linking FIG-05.
- `/docs/ways-of-working/trades/`: knowledge/work trades, preparation, submission, receipt, receiver choice and sender observation. Distinguish an operational handoff message from a durable trade. For island owners sharing material; FIG-07.
- `/docs/ways-of-working/findings-and-reports/`: outcomes, findings and questions, Goal/Scope/As of, confidence, storage, decisions and current residual choices. For owners reviewing investigations and agents reporting them; FIG-08.
- `/docs/ways-of-working/tending/`: the complete structural and PMO tracks, how captures move upward, focus rule, six dispositions and a worked pass. For owners maintaining a repository or territory. Label interim practice and separate available checks from candidate automation; FIG-09 and FIG-10.
- `/docs/ways-of-working/regular-work/`: regular versus Project work, durable Activity/recurring definitions, occurrences and On hold/more expected. For owners adopting recurring obligations; FIG-11.
- `/docs/ways-of-working/unattended-work/`: prepare a bounded window, distinguish approval from eligibility, handle a stop and return reviewable outcomes. For owners delegating while away. Cite the current adopted contract and label unsettled fields; no invented scheduler feature.

### Knowledge and standards

These are authored guides. Examples use a small fictional island, generic file paths and ordinary knowledge work rather than Kris's live packages or private runtime identifiers.

- `/docs/knowledge/`: the zones and the internal Pillars/external Resources boundary, working areas, links and the role of a Capital. For prospective and new island users; FIG-12.
- `/docs/knowledge/query-save-update/`: find an answer, save a useful note, update an existing one and preserve provenance. For daily knowledge users; show before/after notes, not tool internals.
- `/docs/knowledge/acquiring-knowledge/`: source capture, acquired packet, review, triage and assimilation, including available ChatGPT/Granola adapters. For researchers and meeting-note users; FIG-13.
- `/docs/knowledge/live-artifacts/`: source/rendered pairs, when a live view is useful and what keeps it honest. For people maintaining a queue, tracker or status view.
- `/docs/knowledge/recaps/`: end a session with outstanding work and route durable learning to its owner. For all agent users; contrast single-session recap with the coordinator's recap since the mark.
- `/docs/standards/`: what repository standards provide, audit/conform/educate/refresh, mechanical versus judgement evidence, and choosing applicable overlays. For adopters and maintainers; FIG-14.
- `/docs/standards/engineering/`: the practical guarantees of the engineering standard, verification boundaries and evidence a reviewer should expect. For code-repository maintainers.
- `/docs/standards/writing/`: authoring, guides, specifications and their different purposes, with examples. For knowledge authors; link relevant skill details rather than repeating their complete rules.
- `/docs/standards/decision-records/`: a worked typed record, how durable rationale differs from a package's decision log and when to consolidate. For owners and reviewers; FIG-15.
- `/docs/standards/diagrams/`: how a living diagram is read, traced and refreshed; SVG versus interactive HTML and source status. For readers first, with a short maintainer subsection.

### Retained harness and getting-started pages

Retain `/docs/get-started/` and `/docs/contribute/`. Get Started offers a readable end-to-end example before the installation path. Contribution explains how proposed improvements reach their owner. Neither becomes a prerequisite to browsing features.

Retain these existing harness routes, with authored refreshes and Sources: `/docs/ki-agentic-harness/installing-a-harness/` for someone installing a supported harness; `/docs/ki-agentic-harness/onboarding/` for repository adopters; `/docs/ki-agentic-harness/repositories/` for understanding declarations and type overlays; `/docs/ki-agentic-harness/how-the-harness-works/` for the skills/CLI/runtime relationship, with FIG-16; `/docs/ki-agentic-harness/using-skills/` for invocation and activation; `/docs/ki-agentic-harness/tuning/` for a user adjusting context and runtime behaviour. Their role is practical adoption, not a second work-process manual.

Merge the old `skills-by-outcome` material into `/docs/skills/`, `skills` into `/docs/skills/how-skills-work/`, `skill-catalogue` into `/docs/skills/catalogue/` and `planning-and-delivery` into `/docs/ways-of-working/roadmap-lifecycle/`. Redirect each old route directly to its final equivalent. Preserve useful fragments with explicit anchors or a fragment migration map; a server redirect alone cannot rename a fragment.

### The ki command

Keep the existing `/docs/ki/` family. Explain its features as a tool for applying and inspecting the model. Readers must be able to judge scope and expected effects without a terminal. All task pages are authored; syntax and option inventories are generated from a single reviewed version.

- `/docs/ki/command-groups/`: retain and expand as the CLI overview: user, repository, territory and development scopes; why skills and commands coexist; task-to-command map. For a new CLI user; link FIG-16.
- `/docs/ki/getting-started/`: retain installation, first inspection, first repository activation and a worked expected result. For someone choosing to install.
- `/docs/ki/commands/`: retain the complete command inventory, including precise options/help coverage and explicit availability. For look-up users. Generate exact grammar; authored examples link to task pages.
- `/docs/ki/capability-lifecycle/`: retain harness installation, activation and skill/repository projection. For someone enabling capabilities.
- `/docs/ki/naming-and-locations/`: retain conceptual names, portable configuration, local registry and state locations, selection and refusal examples. For a user diagnosing which object a command targets.
- `/docs/ki/update-upgrade/`: retain the supported update paths and the distinction between CLI, harness and local development checkout. For installed users.
- `/docs/ki/local-commands/`: retain diagnostics, inventory, doctor, cleanup, completion and help, separating read-only inspection from apply/repair. For everyday operators.
- `/docs/ki/chatgpt-local-capture/`: retain capture format and available import behaviour. For users of that acquisition route; link the acquisition feature guide.
- `/docs/ki/operator-guides/`: retain as a task index, replacing repository handoffs with links to answers on the site. For returning users.
- `/docs/ki/repositories/`: add selection, init/repair, audit/conform/educate, explicit scope and expected outcomes. For repository maintainers.
- `/docs/ki/work-and-batches/`: add work views versus record operations, roadmap commands and exact-set batch commands. For coordinators/operators; no implication that `ki` chooses priorities or grants acceptance.
- `/docs/ki/background-agents/`: add new/launch/list/watch/report/close and the run lifecycle, with full task-help verification before writing examples. For someone operating detached runs; link FIG-04 rather than duplicate its conceptual account.
- `/docs/ki/trades/`: add the command journey for one local side and its expected receipts. For trade operators; link FIG-07.
- `/docs/ki/knowledge-and-acquisition/`: add provisioned KB search and acquisition commands, their inputs and limits. For knowledge users who choose CLI access.
- `/docs/ki/territories-and-estate/`: add discovery, registry, territory and estate concepts and effect scopes. For multi-repository users; make read-only and mutating examples explicit.
- `/docs/ki/manual-details/`: add the omitted manual material: exit status, configuration/environment reference, paths and version-specific development behaviour. For troubleshooting; generate literal reference facts and author their explanation.

The root reference and command-path help must agree with the pinned source manual before publishing. A parser that currently extracts only invocation and description must be extended or the richer reference must be split into honest supported sections; do not claim existing `cliCommands.json5` already contains every option and manual section.

### Tools and ecosystem, prompting and optional integrations

Use `/docs/ecosystem/` as the merged catalogue landing, generated from the existing project registry with an authored introduction. Keep its present purpose/audience/capabilities/state/limits/usage structure. Each entry is a short adoption explanation, not an implementation guide. These are the canonical detail paths and audiences:

- `/docs/ecosystem/ki-principal/`: philosophy/model authority, for readers seeking the source model; links to Voyage and knowledge guides.
- `/docs/ecosystem/ki-agentic-harness/`: reusable skills and supported adoption, for agent users; links to Skills and Harness.
- `/docs/ecosystem/ki-specifications/`: portable contracts and present publication state, for integrators; do not imply a complete website corpus exists.
- `/docs/ecosystem/ki/`: the runtime-neutral command host, for prospective CLI users; links to the deep CLI documentation.
- `/docs/ecosystem/mgit/`: multi-repository Git use, for estate maintainers.
- `/docs/ecosystem/git-almanac/`: repository/history reporting, for people reviewing Git activity.
- `/docs/ecosystem/rig/`: agent/tool configuration and skill delivery, for users managing an agent environment.
- `/docs/ecosystem/techne/`: engineering tooling's present capabilities and limits, for maintainers considering it.
- `/docs/ecosystem/mcp-ki-kb-fs/`: file-backed KB access, for users choosing an integration.
- `/docs/ecosystem/mcp-ki-kb-notion-mirror/`: the declared Notion mirror, for users evaluating a derived surface.
- `/docs/ecosystem/mcp-git-audit/`: Git inspection, for repository reviewers.
- `/docs/ecosystem/mcp-housekeeping-claude/`: the Claude housekeeping service, for relevant runtime users.
- `/docs/ecosystem/mcp-gsuite/`: Google Workspace integration, for users evaluating that optional route.
- `/docs/ecosystem/mcp-m365/`: Microsoft 365 integration, for users evaluating that optional route.
- `/docs/ecosystem/ki-techne-harness/`: Techné's reusable capabilities, for engineering-agent users.
- `/docs/ecosystem/homebrew-tap/`: release transport, for users choosing installation and upgrades.

The seventeenth registry entry, `ki-website`, keeps its existing home route `/`; it needs no duplicate ecosystem page. The registry remains the source for all 17 entries. Claims on the lighter-depth tool/service pages must be checked against their owning public documentation in their delivery unit; this survey has not audited those tools' behaviour.

Retain the existing 14 model-specific `/docs/prompting/<slug>/` pages and `/docs/prompting/`. Add authored `/docs/prompting/choosing-and-reviewing-models/` for purpose, context budgets and radar skills, not a new unsupported model ranking. Retain all six `/docs/optional-tools/` pages and add authored `/docs/optional-tools/agent-environment/` to explain bindings, MCP, runtime projections and housekeeping. Existing optional-tool routes are `chezmoi`, `codex-skill-discovery`, `headroom-ai`, `mcp-access`, `under-observation` and the section index. Their claims and status still require their own provenance review.

Retire the separate Projects header item. Redirect `/projects/` to `/docs/ecosystem/`, and generated project details to the paths above; the website's existing `/` route remains home. Repoint already-retired `/tooling/`, `/guidance/` and project-guide aliases straight to final targets to avoid chains. Keep `/install/<tool>` and release transport unchanged. The migration unit must produce an exact old-to-new route and fragment inventory from the build, not rely on this prose as a complete redirect file.

## Feature areas a reader can browse

The feature browser is an authored many-to-many classification over generated skill membership. Do not label these as new skill domains or automatically infer them from folders. Each area shows its guide, skills, outcomes and related commands:

1. **Understand and choose skills:** what a capability provides, governance/process, modes and dependencies.
2. **Coordinate and resume work:** work states, relative roles, messages, packages and progressive reveal.
3. **Delegate and run in the background:** briefs, authority, run monitoring, receipts and close-out.
4. **Select, plan, deliver and review:** the roadmap lifecycle, horizons, dependencies and human acceptance.
5. **Design before delivery:** reviews, owner decisions and pilots when the shape is undecided.
6. **Bound autonomous work:** exact-set batches and unattended windows, with their distinct authority.
7. **Tend a repository or territory:** four structural levels, five PMO levels, upward capture and dispositions.
8. **Run regular obligations:** Activities, recurring definitions, occurrences and more expected.
9. **Share work and knowledge:** message handoffs, trades, receipt, receiver choice and observation.
10. **Investigate and decide:** findings, queries, confidence, reports, decision logs and typed records.
11. **Build and maintain an island:** zones, indexes, metadata, source ownership and principal overlays.
12. **Acquire and reuse knowledge:** capture, review, query/save/update, digests and source mirrors.
13. **Keep live views and learning:** live artifacts, recap and durable learning routes.
14. **Adopt repository standards:** universal contract, type overlays, engineering, Git and evidence.
15. **Write and explain:** authoring, guides, specifications and living diagrams.
16. **Configure an agent environment:** bootstrap, harnesses, bindings, MCP and housekeeping.
17. **Choose an agent arrangement and models:** subagents, optional Paperclip, tokenomics and radars.
18. **Design an interface:** inspiration and design-system skills, with a clear off-ramp from work-model design.

Three test journeys anchor the prose: a new owner understands a feature before installing; a coordinator resumes a package, commissions a run and reviews the return; a maintainer tends an island, fixes a bounded issue and routes larger work. Every journey links to the exact skills and commands involved, and explains what requires the owner's decision.

## Archify diagram plan and embedding

Create diagrams with the `archify` skill, under the living-diagram contract. Prefer a small diagram that answers one question. Existing harness diagrams aimed at skill authors may be useful evidence; their dependency graphs are not substitutes for a consumer journey.

- **FIG-01 - Where work sits**, architecture, on Ways of working: territory coordination, regular and Project work, work items and runs; themes as labels and attention returning upward. Source: Work Process and coordination. Do not portray repositories as command authority over one another.
- **FIG-02 - Who holds the work**, lifecycle, on Coordination: the seven work states, send/receive, steering without a move, blocked return, drain/hold/release and Finished. Source: Work Process and coordination. Do not merge this with record status.
- **FIG-03 - What survives a session**, architecture, on Work packages: the five files, permitted findings/design support, runtime run state and durable knowledge owners, with separate boundaries. Source: package standard and coordination.
- **FIG-04 - A background run and its return**, sequence, on Background runs and linked from the CLI: owner, coordinator, launcher, run and owning repository; bounded brief, launch, progress, report, receive and close. Source: delegation and current CLI help/manual. Show authority as supplied, not created by launch.
- **FIG-05 - A work record's journey**, lifecycle, on Roadmap lifecycle: triage/draft/ready/in-progress/awaiting-review/done/cancelled, the four process skills on transitions, horizons as a separate dimension and pruning after terminal retention. Source: roadmap and process references. Exceptions and human approval must remain visible.
- **FIG-06 - Shape an undecided model**, workflow, on Work design: brief, independent reviews, merged findings, owner decisions, pilot and graduation into ordinary work. Source: work-design standard.
- **FIG-07 - A trade without transferred ownership**, sequence, on Trades: sender preparation/submission, receiver receipt, receiver disposition/local work or knowledge, sender observation. Source: trades/trade/next. Distinguish receipt from acceptance.
- **FIG-08 - Evidence and a decision**, dataflow, on Findings and reports: requested question to finding, report and query; answer to decision log and durable owner, with separate finding/query settlement status. Source: adopted coordination/package rules; draw residual interim extensions distinctly or omit those edges with an explicit note.
- **FIG-09 - Structural tending**, workflow, on Tending: mechanical checks, judgement review, repository checklist and territory checklist, using fresh lower-level results. Source: interim tending and coverage assessment. Label the whole figure Interim practice.
- **FIG-10 - PMO tending and disposition**, workflow, beside FIG-09: packages, records, Projects, themes and territory; fix, record, idea, message, drop-with-reason or query, with owner-only structural choices. Source: interim tending. Do not depict all dispositions as record creation.
- **FIG-11 - A regular occurrence**, lifecycle, on Regular work: definition, due occurrence, ordinary work, review and more-expected rest, contrasting finite Project completion. Source: Work Process, Activities and recurring-work standards; distinguish definition state from occurrence state.
- **FIG-12 - An island's knowledge**, architecture, on Knowledge: the five zones, inbound/outbound working areas, internal/external boundary and useful links. Source: KB standard and principal overlay.
- **FIG-13 - Capture becomes useful knowledge**, dataflow, on Acquiring knowledge: external source, readable capture, acquired packet, review/triage, canonical note and optional derived search/mirror. Source: acquire and KB references; avoid suggesting capture automatically enacts knowledge.
- **FIG-14 - Standards apply in layers**, architecture, on Standards: universal repository contract, repository-type overlays and specialised concerns, with audit/conform/educate roles. Source: skill declarations and repository standards. Use a readable example, not all 64 nodes.
- **FIG-15 - Decision log to durable rationale**, workflow, on Decision Records: answer, package log, consolidation judgement, typed durable record and affected sources. Source: decision-record and coordination references.
- **FIG-16 - Skill, harness, command and runtime**, architecture, on Harness: skills supply policy/procedures, harness packages capabilities, `ki` installs/projects/hosts operations, runtime conducts the session and repositories retain authority. Source: harness/bootstrap/binding declarations and tools-ki manual. Include one example connecting a feature to both a skill and a command.

Each diagram brief names its audience and question in `diagrams.toml`, traces the particular source paths and records `last_checked`. Keep reusable skill diagrams canonical in harness `docs/diagrams/`, consistent with the Project's existing diagram ownership decision; keep a Work Process-owned model figure in its existing principal home if it is that exact figure. A receiving repository owns its own implementation unit. This proposal authorises no cross-repository diagram edits.

For the website, vendor a pinned, privacy-checked SVG, committed HTML and matching receipt from that owner. Set `commit_html = true` upstream when the website needs the viewer. Do not edit generated HTML or generate it afresh during an ordinary website build. Retain the Archify candidate and source/HTML receipt in the owning repository; record their immutable ref and digests in the website's import manifest.

**Default embed:** a readable responsive SVG figure, a useful caption/short textual equivalent and a clearly labelled **Open interactive diagram** link to `/assets/diagrams/<slug>.html`. Add a dedicated passthrough copy for that directory: the site currently copies images and JS, not a diagram HTML directory. Raw viewer bytes must bypass Eleventy/Nunjucks and both HTML transforms; otherwise script/template content or receipt hashes may change. The explicit link also makes a copied HTML viewer reachable to the existing link-based gate; an iframe `src` alone may not.

**Optional enhancement after the pilot:** a user-opened, lazy iframe or overlay on the same site, preserving the standalone link. Test keyboard entry/exit, Escape, focus return, mobile sizing, captions, colour modes, reduced motion, search/focus/deep links and export. Avoid an automatic heavy iframe on every page: the current standard estimates a viewer at roughly 800 KB. If an opaque `srcdoc` host is later used, Archify's reading-link-template seam needs a separate tested decision. Do not hand-patch the viewer to add it. A single SVG-plus-link pilot is sufficient for first publication.

A diagram delivery passes Archify finalize's validation, delivery, strict check and browser check, the owner repository's `ki-diagrams` receipt/privacy/freshness checks, and the website's import/hash, portable-route and reachability checks. Inspect desktop and mobile output visually before claiming it is readable. A rendered viewer without those checks is not a completed diagram unit.

## Keeping prose true to its sources

### Production rules

1. **Generate exact facts:** skill identity/kind/dependencies/modes where structured, inventory membership, CLI invocations/options, released-tool metadata and route lists. Preserve the existing inventory interfaces where adequate. Extend source contracts deliberately for missing facts; do not scrape arbitrary prose headings and call them a stable API.
2. **Author the explanation:** feature benefits, scenarios, how to choose, worked examples, boundaries and human decisions. Website prose is a consumer interpretation with citations, not copied SKILL.md instructions addressed to an agent.
3. **Generate a skeleton, then review the prose:** a skill detail starts with source facts and its required question headings. It becomes publishable only when the authored sections contain meaningful answers. Do not ship empty scaffolds, boilerplate limits or invented modes to achieve catalogue coverage.
4. **Preserve source authority:** the Work Process owns the model, each skill/reference owns its contract, tools-ki owns commands and each tool/service owns its behaviour. A website example cannot silently change those contracts. Prefer a visible unresolved status over a false unified answer.

Use a small website content manifest in the future implementation, separate from generated snapshots: canonical URL, content kind, feature assignments, exact source paths/refs, source content digests, reviewed date and diagram imports. Preserve the existing `sources` frontmatter/footer contract; the manifest supplies coverage and drift information, not a rival authority. Use public repository-relative references in published data, never local absolute paths or runtime identities.

### Drift and coverage checks

- **Every build, offline:** existing build gates plus exact current-snapshot membership-to-detail coverage, valid feature links, no orphan/duplicate/retired skill detail, no placeholder sections, generated facts matching their pinned input and source-ref agreement between catalogue, page footer and import manifest. While staged delivery is incomplete, catalogue entries without a finished detail use the existing complete inventory description; the final coverage gate requires all 64 details. Never link an unpublished skeleton.
- **CLI coherence:** advertised `ki` version, command snapshot and manual-details pin must refer to the same reviewed release. Compare the manual's two inventories as today, and validate task examples against pinned command-path help. The 0.13.0 root-help observation is evidence, not proof the installed manual or every website example matches that release.
- **Authoring refresh:** compare per-source content digests, not only a repository HEAD. A changed reference marks all its dependent guides, skill details and diagrams **needs review** in a maintainer report; it does not rewrite prose, bump `reviewed` or silently publish new assertions. Renames/removals require a deliberate page/redirect decision. Fail the publication unit if one of its affected pages remains unresolved; unrelated source movement should be reported without blocking an offline build of pinned content.
- **Upstream monitoring:** retain the optional network provenance sweep for an authorised refresh or CI process. Add a read-only local comparison against explicit source checkouts for no-remote runs; this is proposed tooling. Normal builds stay reproducible and make no upstream call. Treat unavailable upstream evidence as unknown, not current.
- **Semantic review:** check that examples, authority language, available versus interim status, lifecycle edges and off-ramps agree with the source. Machines can flag movement and missing sections; they cannot prove that a paraphrase is truthful.
- **Diagrams:** compare copied HTML/SVG/receipt hashes with the reviewed import; check candidate/source receipt upstream, and use traced-path history to flag stale explanations. Do not update a freshness date merely because the SVG still renders.
- **Routes and usability:** clean then build after a migration; check all former URLs and important fragments, no redirect chains, generated Nunjucks-page provenance, section order/counts, tool install routes, reachability, SVG/interactive links and no-JavaScript navigation. Existing provenance checks focus on Markdown and explicitly named special pages, so generated skill/ecosystem pages need explicit coverage rather than an assumption that a `.njk` template is already checked.

The consumer-facing status note stays concise. Detailed hashes and drift machinery belong in source declarations and maintenance reports, not an ordinary reader's workflow.

## Delivery order: finishable and verifiable units

These are proposed implementation units for the receiving owners, not new work records. Route them as messages to the relevant work, following HANDOFF-AS-MESSAGE; the receiver chooses priority, records and acceptance. Each run receives an exact file/page set, source revision and verification boundary. It ends with a verified commit and reviewable pages, or reports the precise unfinished boundary. No unit accepts or prunes another work record.

### Establish the publication path

1. **P1 - Merge this design and Fable's:** settle the named decisions below, the source-status boundary and route map. Output: one agreed architecture and the owner review itinerary. Check: all requested feature areas, all 64 skills and all retained routes have a destination. No website implementation before this merge.
2. **P2 - Source and coverage foundation:** implement the skill detail data/skeleton seam and content/import manifest, plus meaningful offline tests for missing/retired membership, bad source pins and unpublished placeholders. Preserve current complete pages. Check: fixtures prove gates fail on those cases; normal offline site build passes. This run publishes no empty detail pages.
3. **P3 - One diagram pilot:** FIG-16 and the existing harness explanation page, canonical upstream output followed by a separate website import unit. Check upstream finalize/receipt/privacy, then passthrough-byte equality, SVG/standalone access, portable links and desktop/mobile visual reading. Keep iframe enhancement out of this first unit.
4. **P4 - Skills landing and choice:** publish Skills landing, how skills work and catalogue, refresh the inventory to one reviewed harness ref and add the feature browser. Check current membership and the three reader journeys, including useful no-JavaScript navigation. Preserve old harness aliases until their destinations exist.

### Publish skills first

The following detail batches are disjoint and exhaustive: 64 pages in 14 units, each with 2-6 authored details, their Sources and related feature links. Shared generation is P2; each batch is an editorial and verification unit. A page may link to an existing catalogue anchor until a deeper guide is available. Do not expose dead links for planned guides.

- **S1:** `ki-bootstrap`, `ki-repo`, `ki-skills`.
- **S2:** `ki-coordination`, `ki-work-package`, `ki-delegation`, `ki-recap`.
- **S3:** `ki-work`, `ki-work-roadmap`, `ki-next`, `ki-plan`.
- **S4:** `ki-implement`, `ki-accept`, `ki-batch`, `ki-work-design`.
- **S5:** `ki-work-recurring`, `ki-work-github-issues`, `ki-work-linear`, `ki-trades`, `ki-trade`.
- **S6:** `ki-repo-kb`, `ki-repo-kb-principal`, `ki-repo-kb-streams`, `ki-repo-kb-activities`, `ki-repo-kb-live-artifacts`.
- **S7:** `ki-acquire`, `ki-acquire-chatgpt`, `ki-acquire-granola`, `ki-pulse`.
- **S8:** `ki-authoring`, `ki-decision-records`, `ki-guides`, `ki-specs`, `ki-diagrams`.
- **S9:** `ki-engineering`, `ki-git`, `ki-repo-project`, `ki-repo-harness`, `ki-repo-tools`, `ki-repo-mcp`.
- **S10:** `ki-repo-specifications`, `ki-repo-homebrew-tap`, `ki-repo-dotfiles-chezmoi`, `ki-repo-website`, `ki-repo-website-content`, `ki-repo-website-app`.
- **S11:** `ki-repo-website-cloudflare`, `ki-binding`, `ki-binding-chatgpt`, `ki-binding-claude`, `ki-binding-chezmoi`.
- **S12:** `ki-tokenomics`, `ki-tokenomics-chatgpt`, `ki-tokenomics-claude`, `ki-housekeeping-chatgpt`, `ki-housekeeping-claude`.
- **S13:** `ki-subagents`, `ki-subagents-chatgpt`, `ki-subagents-claude`, `ki-agent-coordination-paperclip`.
- **S14:** `ki-design-inspiration`, `ki-design-system`, `ki-agentic-radar`, `ki-model-radar`.

For every S unit: verify the authored outputs and authority boundaries against SKILL.md and the cited references; exercise one representative invocation or read-only example where meaningful; validate metadata/dependencies, content completeness, links, formatting and site build. Do not run a mutating example just to document it. S5 must demonstrate the remote-adapter limitation honestly. After S14, require exact 64-of-64 detail coverage and absence of retired names as active capabilities.

### Publish the feature journeys

After the relevant S unit, publish each guide below as its own run. A guide with a new diagram is two linked units: the source owner finalises one diagram, then the website run imports it and authors the page. These are bounded by one diagram and one principal feature page, not an entire feature family.

- **F1-F4:** Ways of working with FIG-01; Coordination with FIG-02; Work packages with FIG-03; Background runs with FIG-04. These establish the central journey.
- **F5-F8:** Roadmap lifecycle with FIG-05; Work design with FIG-06; Trades with FIG-07; Findings and reports with FIG-08.
- **F9-F10:** Tending introduction/structural track with FIG-09, then the same page's PMO track and complete worked pass with FIG-10. F9 must explicitly say which half is available; F10 completes the feature. Preserve interim status in both commits.
- **F11-F15:** Regular work with FIG-11; Knowledge with FIG-12; Acquiring knowledge with FIG-13; Standards with FIG-14; Decision Records with FIG-15.
- **F16:** Agent teams, batch work and unattended work, using existing diagrams and independently sourced examples; maximum three pages.
- **F17:** Query/save/update, live artifacts and recaps; maximum three pages with concrete note examples.
- **F18:** Engineering, writing and diagrams; maximum three pages explaining the practical guarantees and evidence.
- **F19:** Refresh the retained harness/get-started/contribution pages in groups of at most three pages per run; replace duplicate explanations with useful scoped summaries and direct links. Add agent-environment and model-review introductions as two separate page units. Existing model-specific advice is retained, not silently revalidated without its sources.

Each F website unit checks an opening claim, one full reading-only scenario, source status, human decisions, relevant skills/commands, figure equivalent text, links and a clean build. A diagram is visually inspected in the actual page context. F9-F10 must never imply that candidate tending automation is implemented.

### Then deepen the CLI and finish the merger

- **C1:** refresh the command inventory and version coherence, plus the CLI overview. Verify against one reviewed tools-ki release and both manual inventories. Do not mix source-main-only grammar with a released version label.
- **C2:** extend generated reference coverage for options and manual details, with parser failure fixtures. Publish manual details; check paths, exit codes and each included reference section against the same pin.
- **C3-C6:** author task pages in pairs: repositories/work-and-batches; background-agents/trades; knowledge-and-acquisition/territories-and-estate; and refresh getting-started/capability-lifecycle. Each pair has independent task-help evidence and an offline build.
- **C7-C8:** refresh naming-and-locations/update-upgrade, then local-commands/operator-guides/chatgpt-local-capture. Check all examples against the reviewed command surface and keep conceptual explanation on the feature pages.
- **E1:** audit existing public metadata for the five tools and six services, in batches of at most four entries per run, using their owning published sources under an appropriately authorised brief. Resolve unsupported capabilities before copying them into the new directory. This is lighter-depth documentation, not tool implementation work.
- **E2:** move the reviewed generated catalogue to `/docs/ecosystem/`, merge the navigation and implement the exact redirect/fragment map in one website unit. Preserve registry ownership and install routes; check generated-page provenance and a clean build's complete route reachability.
- **E3:** final editorial/visual review of the itinerary below, complete skill/feature coverage, current source-status labels, all 16 diagrams, old URLs and portable/no-JavaScript behaviour. Return defects to their specific unit; do not announce completion while a promised feature or skill still has only a skeleton.

P3 may be piloted early to remove embedding uncertainty. Full CLI depth and the catalogue move follow usable skill/feature coverage, preserving Kris's skills-first priority. Within the feature sequence, finish the relevant guide before asking Kris to review it; no run is assigned the whole architecture or an unbounded polish pass.

## Kris's review itinerary

These are proposed destinations to review after their delivery units, not claims that the pages already exist. Review the consumer result and steer the model below; code review is not requested.

1. **First encounter:** `/docs/skills/`, then `/docs/skills/how-skills-work/`, then one detail such as `/docs/skills/ki-next/`. Can you tell what you gain before installing, and choose a feature without already knowing the skill's name? Steer D01, D03 and D04.
2. **The working model:** `/docs/ways-of-working/`, `/coordination/`, `/work-packages/` and `/background-runs/` within that section. Do the figures make work, sessions, packages, runs and holders distinct? Is it obvious what survives the session and what the owner decides? Steer D05 and D08.
3. **Delivery and exchange:** `/docs/ways-of-working/roadmap-lifecycle/`, `/batch-work/` and `/trades/`. Can you follow an example from selection to review without mistaking a receipt, readiness or run completion for acceptance? Steer D05.
4. **Tending:** `/docs/ways-of-working/tending/`, reading both figures and the worked pass. Does it explain the process you use, including the upward PMO pass and the focus rule? Is interim status visible without overwhelming the explanation? Steer D06.
5. **Evidence and rationale:** `/docs/ways-of-working/findings-and-reports/` and `/docs/standards/decision-records/`. Are findings, queries, answers and durable decisions easy to distinguish, including the residual choices? Steer D06 and D07.
6. **Knowledge use:** `/docs/knowledge/`, `/acquiring-knowledge/` and `/recaps/` within that section. Can a non-developer understand capture, canonical knowledge and durable learning without learning implementation details? Steer D04 and D12.
7. **Tool use:** `/docs/ki/command-groups/`, `/docs/ki/background-agents/` and `/docs/ki/commands/`. Does the explanation stand alone, and can a user move from a feature to the right command and its effects? Steer D09 and D10.
8. **Merged destination:** `/docs/` and `/docs/ecosystem/`, with one tool and one optional-service entry. Is one Docs destination clearer, and are the lighter-depth entries sufficient to decide whether a tool is relevant? Steer D02 and D11. Confirm Voyage and Field Guide still read as their existing separate experiences.

Source controls and diagram placement need a maintainer decision rather than a website aesthetic judgement; their choices are D13-D16 below. The coordinator should offer this itinerary as real links only as the pages become available.

## Decision register

These are recommendations for the Fable/Codex merge, not owner decisions. Confidence measures the strength of this recommendation from the inspected evidence; it does not imply that consumer usability has been tested. This register names the substantive choices made in this proposal. Ordinary wording and slug choices follow the named architecture choices.

- **D01 - Primary orientation:** put skills and feature outcomes first, with installation as an optional next step. **Recommendation:** adopt. **Confidence: high**, because it directly matches DOCS-PUBLISH and avoids requiring terminal use to understand the model. Alternative: installation-first documentation.
- **D02 - Docs and Projects merger:** one Docs header destination, with the catalogue at `/docs/ecosystem/`; preserve Voyage/Field Guide and redirect previous catalogue URLs. **Recommendation:** adopt after skill content is usable. **Confidence: medium**, because the owner favours a merger but the exact public label and route remain a navigation judgement. Alternative: merge only navigation while retaining `/projects/` as the canonical directory.
- **D03 - Individual skill depth:** one useful detail page for every current skill, with common questions, rather than only a generated inventory. **Recommendation:** adopt the 64-page target with bounded editorial batches. **Confidence: high**, because the owner asks what each skill does/provides and the present inventory demonstrably misses current capabilities. Alternative: family guides plus anchored catalogue entries, with less room for per-skill examples.
- **D04 - Two browsing views:** authored feature areas over generated skill membership, with reference details separately searchable. **Recommendation:** adopt the 18 areas and cross-links; tune names after the first reading tests. **Confidence: medium**, because task grouping is an editorial hypothesis, not a property of skill directory names. Alternative: browse by the harness's source domains only.
- **D05 - Separate lifecycles and artefacts:** distinguish work state, item status/horizon, run state, receipt and acceptance; retain the existing ownership boundaries in every example. **Recommendation:** adopt. **Confidence: high**, because the Work Process and skill procedures make these distinctions explicit. Alternative: a simplified linear story, at the cost of misleading authority and state.
- **D06 - Publish interim practices honestly:** document tending fully now with an interim label, and mark residual findings/metadata/unattended choices locally. **Recommendation:** adopt; do not invent a skill, command or field. **Confidence: high**, because the current coverage assessment explicitly preserves gaps. Alternative: delay those guides until graduation, leaving a requested feature unexplained.
- **D07 - Source precedence:** source model and adopted standards govern; the dated interim notes explain residual practice; Project history and old diagrams are context. **Recommendation:** adopt and refresh this assessment per unit. **Confidence: high**, because inspection found partially outdated prose and live uncommitted assessment material. Alternative: publish the latest design text as though all proposals were adopted.
- **D08 - Diagram form:** use 16 focused Archify diagrams of the five currently governed types; begin with SVG and a standalone interactive link. **Recommendation:** adopt, pilot FIG-16, and defer iframe polish. **Confidence: high** for the rendering/embedding pattern, **medium** for the exact number of figures until reader review. Alternative: one large dependency graph or automatic inline viewers throughout.
- **D09 - Preserve useful namespaces:** keep `/docs/ki/` and practical `/docs/ki-agentic-harness/` pages, add consumer feature/skill sections and merge only duplicate pages. **Recommendation:** adopt. **Confidence: high**, because it preserves existing finite sections and reduces avoidable URL churn. Alternative: rename every harness/CLI route during the same migration.
- **D10 - CLI reference policy:** pin one reviewed release across advertised version, command data and manual details, with generated grammar and authored task explanation. **Recommendation:** adopt before claiming reference completeness. **Confidence: high**, because the inspected site mixes v0.11.0 commands with v0.13.0 advertising. Alternative: a clearly labelled development reference in parallel, which is extra scope.
- **D11 - Other-tool depth:** use the existing rich project registry for short adoption pages, retaining install/release ownership in each tool and verifying claims before migration. **Recommendation:** adopt. **Confidence: medium**, because those source repositories were not behaviour-audited in this task. Alternative: commission full manuals for every tool/service before merging the catalogue.
- **D12 - Example world:** use a small fictional island and reading-only examples, with effect/authority statements for command tasks. **Recommendation:** adopt. **Confidence: high**, because it serves consumers and avoids teaching through private or transient live work. Alternative: literal screenshots/packages from Kris's running territory.
- **D13 - Generation boundary:** generate exact facts and scaffolds, author meaning and examples, reject unpublished placeholders. **Recommendation:** adopt. **Confidence: high**, because the current site already separates source snapshots from owned prose. Alternative: copy SKILL.md wholesale or generate all explanation without editorial review.
- **D14 - Drift policy:** keep pinned offline builds, add digest-based coverage/import checks and a maintainer review queue, and use network checks only in authorised refresh contexts. **Recommendation:** adopt, with unit-level publication blocking for unresolved affected pages. **Confidence: high** on the policy, **medium** on the new checker implementation until fixtures prove it. Alternative: declare provenance sufficient or fetch latest content at every build.
- **D15 - Diagram ownership:** reusable skill diagrams remain in harness `docs/diagrams/`; the website vendors reviewed immutable outputs and leaves the Work Process's own model figure with its owner. **Recommendation:** adopt. **Confidence: high**, because the Project already assigns skill-diagram ownership and `ki-diagrams` supports committed HTML/receipts. Alternative: create a second website-owned canonical skill-diagram set.
- **D16 - Delivery and review boundary:** approve a merged design first, then bounded source-owner and website units, skills before deep CLI work, ending in a page-based owner itinerary. **Recommendation:** adopt the P/S/F/C/E sequence and split further whenever a source contract is unresolved. **Confidence: high**, because it respects receiver authority and gives each run an inspectable result. Alternative: one bulk rewrite with a final review of the entire site.

No execution blocker prevents this proposal. Navigation labels, the exact figure count and any change to an adopted contract belong to the merge/owner review; this run does not settle them by implementation.
