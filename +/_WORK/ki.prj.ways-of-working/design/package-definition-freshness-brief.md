# Package definition and session freshness: brief

**Owning work:** `ki.prj.ways-of-working`

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Date:** 2026-10-29

## Problem

A portable definition should route work clearly while separating where its authoritative package lives, where delivery happens, and any machine the work requires. Separately, a long-running conversation needs a visible freshness signal and a safe point to continue in a fresh session. Package creation time does not measure the current session's age.

This is preparation for two independent reviews, not an adopted schema or final recommendation. Kris authorised this bounded design review in [the owning decisions log](<../decisions.md>), “Package definition and session freshness design review - 2026-10-29T20:34:32Z”. The current mark remains 2026-10-29T16:18:42Z. The prior request asks for elapsed current-session time and conversation volume beside the bare work id, with a restart recommendation and safe handover after a threshold; metrics, thresholds and storage remain undecided. No package move, session transfer, implementation, registry creation or authoritative package copy is authorised here.

## Owner's proposal

```text
exactly the right names :) can you do some design review and I'll work on getting the threads drained from terra so they are back on here. In some cases we also need to include a host for it:

An example:
id: personal.reg.rig-sol
description: ... (this is used for the progressive disclosure/loading/reveal like skills)
parent: personal.sop.main
level: regular
territory: personal
canonical_home: personal-principal (or whatever we use to look this up in the registry to map to a local path)
execution_home: chezmoi (or whatever we use to look this up in the registry to map to a local path)
theme: regular (all level === regular have a theme === regular)
created_at: ...
freshness: ????

I think we can drop title as we now use:
🧵 <id>

And I think we could improve on skills use of description have a anti field, e.g.

Not for terra (personal.reg.rig-terra), the public Rig catalogue and rig.midnight.ninja (personal.reg.rig), the Rig tooling (KI's tools-rig) or how Rig and KI approach chezmoi changes (KI's ki.prj.chezmoi).
```

## Established facts

The following are observed contracts or source behaviour, not adoption of the proposed fields. Source references freeze the Harness at `99bd8fc078d2a283e037e5d27e14ce01ce96b644` and Tools at `76df015a41365591aa56a3b7ac13f9baf7994ac0`; their selected source trees were clean when checked. Principal Project/theme metadata was checked at `eb6bf278fee4f960e09041dbe5d28b97bd29c113`; no HNR repository, private report or session payload was read. No live registry payload was needed: registry facts below concern its schema and identity contract only.

- **Entry file and field set.** The package entry is `+/_WORK/<id>/work.md`, with `state.md`, `queries.md`, `messages.md` and `decisions.md` created alongside it. `work.md` defines work; state lives separately. Its closed definition requires `id`, `level`, `title`, `description`, `worker` and `supervisor`; permits `label`, `project`, `theme`, `parent`, `covers`, `created_at`; and imposes conditional Project/parent/coverage rules. `territory`, either proposed home, `freshness` and an exclusion field are not current definition fields. `created_at` is optional package creation time. Sources: [package form and work file][package-form], [exact mechanical definition field set, lines 51-62][package-parser].
- **Home and authority.** Every package defaults to its territory's Capital; every Project package remains Capital-homed. Owner-approved regular/ad hoc member homes are declared by `Home:` in Scope and referenced by the parent State of play, not by a home frontmatter key. There is one authoritative physical package and incoming queue. Execution ownership, acceptance and permission remain with the receiving repository. A member-repository Project session is a seat for a Capital package, not permission to relocate it. Sources: [location and identity][location], [work naming][naming], [local territorial authority](<../../../../AGENTS.md#territorial-authority>).
- **Identity resolution.** The registry schema is version 1 with keyed records containing canonical HTTPS GitHub `repository` identity and absolute local `path`, plus optional store/boundary metadata. A stable local key and canonical repository URL are distinct; `registryEntry` initially derives a key from a basename, but that is not a universal portable package-home contract. The path-free inventory projection is `ki/registry/v1`. The Harness release's reverse-domain naming rule concerns site repository names, not work identity, hostname, package home or a new lookup algorithm. Sources: [registry validation, lines 104-124, and key creation, lines 197-200][local-registry], [REGISTRY-005][registry-spec], [repository identity][configuration], [repository naming][repo-naming].
- **Titles and themes still have readers.** Bare `🧵 <work-id>` is the closing thread line; it did not remove title, label or report headings. Titles use territory, theme and Project display names; theme is absent from ids. `project` is required at Project level; `theme` is optional or null, with no current rule that regular level implies regular theme. Tools' `workDefinition` rejects a missing/empty title and projects theme and description. Harness checks Project/theme resolution and Project-title agreement. The owning [Project note](<../../../../Streams/Projects/ways-of-working.md>) declares title `Ways of working` and theme `model`; the [theme page](<../../../../Streams/Themes/model.md>) declares title `Model`. Sources: [work naming][naming], [mechanical coordination boundary][coord-checks], [Tools definition reader, lines 228-256][status], [package form][package-form], [Project/theme registry location and display metadata][project-registry].
- **Description already includes exclusions.** The required routing description is third person, followed by “Takes ...” and “Not for ...”, naming neighbouring work ids; its soft limit is 500 characters. Progressive reveal has register frontmatter, definition body, pick-up detail and on-demand reports/design. Scope supplies `In:`/`Out:` when two descriptions match. A separate anti/exclusion field is a proposal, not a missing existing field. Sources: [work file][package-form], [progressive reveal][reveal].
- **Host requirement differs from session seat.** Required hosts/categories may appear in a label, message, brief or record and resolve through the territory's machine inventory; unknown or ambiguous names block device-dependent execution. A session's host seat is excluded from packages, holds and reports. Native bindings belong to machine-local runtime state, establish identity rather than liveness/authority, and are not portable package content. The standard's binding tooling remains described conditionally; this review did not establish deployed session telemetry. Sources: [prohibited payloads and claims][boundaries], [work identity and native sessions][sessions].
- **Freshness is not an existing measurement contract.** `since`, `received`, `beat`, `mark` and `method_read` describe work moves, receipt, heartbeat, mark and guidance read; none is a current-session start or conversation-volume counter. Coordination already says to prefer a fresh session once the package contains everything needed to resume. No reviewed source defines the requested elapsed-session/volume metric pair or its thresholds. No native event, counter accuracy, compaction accounting or cross-client availability was verified by reading session material. Sources: [state file][state-file], [picking work up][pickup], [optional reminder consumer boundary][reminders].

## Reflection

Each numbered paragraph is one provisional claim to test, not a recommendation to adopt its example fields. A reviewer may Agree, Differ or Add, citing evidence for each Differ and keeping open decisions explicit.

1. **Portable homes should resolve independently of execution location.** A test should resolve one canonical package and queue from a portable repository identity after checkout relocation while allowing delivery in a different repository. Review canonical URL versus registered key, explicit versus derived Capital default, and one execution home versus per-unit or multiple execution repositories; none should introduce another registry or package copy.

2. **Home metadata must preserve existing authority and exceptions.** Test a Capital-homed Project, a deliberate member-homed regular package and a receiver-owned delivery: a metadata change alone must neither relocate the package nor grant cross-repository execution/acceptance. Compare explicit exception declarations with derived defaults, and whether proposed `territory` is useful validation or duplicated id data. Missing, conflicting or ambiguous identity should remain unresolved rather than guessed.

3. **A required host can be portable without identifying a live session seat.** Test the same package from a different machine: its inventory host/category requirement should remain meaningful while the reader's seat changes. Compare a structured requirement, the existing label/scope/brief route and per-unit requirements; distinguish a hard device constraint from preference. Reconciliation must use inventory identity and retain the current unknown-host execution block.

4. **Removing stored title requires preserving every display consumer's meaning.** Test register listing, routing, Project/theme lookup, report heading and thread footer with no stored title. Compare deriving titles from existing Project/theme metadata against retaining a display title or label for non-Project work. The footer alone is insufficient evidence that all readers can lose title; review missing registries, renamed displays and backward-readable packages before proposing a migration.

5. **The regular-theme invariant needs an explicit semantic test.** Test regular umbrella and ad hoc work with omitted, null, regular and another theme. Compare enforcing `theme: regular`, deriving a regular grouping from `level`, and keeping thematic grouping independent of level. Establish whether “regular” denotes work type, a real theme registry entry or a display group before choosing any invariant; do not invent a theme page to make the example pass.

6. **Separating exclusions should improve routing at register depth.** Test ambiguous Rig-like neighbours using only the same reveal level each reader actually loads: descriptions that both match should route better with exclusions without needing every package body. Compare one description including “Not for”, separate positive/anti fields and structured neighbour references. Measure duplicate/contradictory exclusions, character-budget effects and what existing description-only readers miss; field naming and precedence remain open.

7. **Session freshness should be measurable without confusing package age with session age.** Test a new session on an old package, a long idle session, compaction, model/client switch and unavailable counters. Compare wall-clock versus active elapsed time; turns/messages versus token/context volume; runtime-local counters versus derived display evidence and any minimal portable handover marker. Specify reset semantics, evidence provenance, privacy, retention and unknown/stale display behaviour before choosing storage. No transcript scan, new session store or package telemetry field follows by assumption.

8. **A freshness threshold should trigger an actionable safe handover recommendation.** Test a threshold reached during a running tool, unreceived run and contested Git write: the work must reach a verified resumable boundary before recommending continuation in a fresh session. Compare advisory display, bounded warning/escalation and deferral until the current safe boundary; distinguish recommendation from automatic restart or work-state transition. Verify current state, next steps, queries, decisions, queues and run ownership can be recovered through existing contracts without copying a conversation, moving a mark without authority or silently abandoning work.

## Independent review instructions

Both reviewers use this same brief at its immutable delivery commit, fact-check only the named source contracts and selected identity definitions, and form their view before reading any other review. Each returns Agree, Differ or Add for all eight claims, exact evidence for corrections, fair alternatives and unresolved questions. Neither selects a schema, metric threshold or rollout. No HNR/private payload, broad inventory scan, host move, runtime mutation or package implementation belongs to either review.

**Lens A - portable definition, routing and authority.** Stress canonical/execution resolution, defaults and exceptions, Project/theme and title readers, host requirements and positive/exclusion reveal. Try counterexamples for claims 1-6 and test whether claims 7-8 accidentally introduce portable session state or a second authority.

**Lens B - session evidence, freshness and continuity.** Stress what elapsed time and conversation volume can truthfully mean across clients, idle periods, compaction and restart; unknown evidence, privacy/storage boundaries, threshold behaviour and safe continuation. Try failure cases for claims 7-8 and test whether claims 1-6 supply sufficient identity and routing for a fresh session without duplicating package authority.

The coordinator may merge the independent reviews later, settling factual differences on source evidence and returning unresolved choices to Kris. This brief freezes the questions, not their answers.

[package-form]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#work-file
[location]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#location-and-identity
[reveal]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#progressive-reveal
[boundaries]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#prohibited-payloads-and-claims
[sessions]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#work-identity-and-native-sessions
[state-file]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#state-file
[reminders]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#optional-runtime-reminder-consumers
[package-parser]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/scripts/rubric/contexts/work-package.ts#L51
[naming]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#work-naming
[coord-checks]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#mechanical-boundary
[pickup]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#picking-work-up
[configuration]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/keystone/ki-repo/references/standards-configuration.md#L99
[repo-naming]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/keystone/ki-repo/references/standards-repository.md#repository-naming
[local-registry]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/storage/local-registry.ts#L104
[registry-spec]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/docs/specs/registry.md#registry-005--path-free-machine-inventory
[status]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/work/status.ts#L228

[project-registry]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-work/references/standards-project-registry.md#location
