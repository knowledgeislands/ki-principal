# Package definition and session freshness: merged report

**Brief:** [frozen brief](<package-definition-freshness-brief.md>) · **Reviews:** [portability](<package-definition-freshness-review-portability.md>), [freshness](<package-definition-freshness-review-freshness.md>) · **Date:** 2026-10-29

**Status:** proposed model for Kris's decision, not adopted method or implementation authority. **Owning work:** `ki.prj.ways-of-working`.

## Summary

Keep a small durable definition of identity, routing, authoritative home and default execution footprint. Preserve the owner's names, including singular `execution_home`. Derive territory and Capital defaults where unambiguous, resolve repository identity independently of checkout location, and keep actual targets and authority with each unit. Recommend removing mandatory stored `title` after reader compatibility is delivered, keeping thematic grouping independent of level, and retaining combined routing descriptions initially. An optional package host requirement describes a genuine constraint, never the current session's seat.

Show current-session elapsed time and evidenced conversation volume separately, with unknown values visible. Recommend a fresh session at a recoverable boundary; no score or elapsed threshold certifies degradation. A proposed reversible reminder can work with one available signal while another remains unknown.

The latest owner steer is controlling: "And we found how things move in work packages. So do not concentrate on that right now. You will have a new update soon. Go back to the things that we discussed, that we were doing before that." This report covers definition fields, routing and session freshness. Package movement, host transfer, cross-host orchestration and further drain-process design await that update. Home declarations need no movement mechanism to be reviewed. Design approval here would authorise neither implementation nor publication, release, a pilot or a work transfer.

## Evidence and corrections to the brief

The docs-only dependency completed in Principal merge `0d6e518e`. Receipts establish provenance only; conclusions below use the brief, the reviews and primary contracts. Frozen inputs are:

| Input | Last content commit | Blob |
| --- | --- | --- |
| Brief | `9fef9813f327b2c09f6cd4f752d3dc2149f7b8bf` | `cdea9ce65efc0de10282a67bd4aac955d196a898` |
| Portability review | `55fa66de1f781449415ad823eeeeb772886cf4cb` | `363b7024abf4ab4f4b86eb337db83827639a43d9` |
| Freshness review | `1d52b3160069c5dbf9b651e416f182e26dc91596` | `e39a30106ed37f980f85c764e8008165cf4244e8` |

Current relevant local product sources still resolve to Harness `99bd8fc078d2a283e037e5d27e14ce01ce96b644` and Tools `76df015a41365591aa56a3b7ac13f9baf7994ac0`, the reviews' frozen revisions. No network, private registry binding or session payload supplied evidence.

- **Creation time:** the brief's optional timestamp summary omits an accepted value: [parser lines 617-618][creation] explicitly allow `null`. Preserve unknown creation time; never fill it with a session start or migration date.
- **Description budget:** [the package table][definition] says at most 500 characters, but [parser lines 813-816][budget] issue a warning beyond that length. Treat 500 as the current soft budget, not a rejection rule or measured routing optimum.
- **Titles:** [Tools lines 230-251][reader] currently reject an absent title and return it alongside label, theme and description. The bare thread footer has not removed those consumers. This establishes migration work, not a reason the owner's proposed removal is wrong. [Naming lines 167-174][naming] already derive ordinary topic names from slugs, with owner-chosen names as an exception.
- **Theme:** [parser lines 605-612][theme-parser] separates level from optional/null theme; [the theme contract][themes] permits grouping regular, Project and ad hoc work. The portability review's Agree and freshness review's Differ on point 5 describe the same substantive conclusion: test the proposed invariant, then reject it in favour of independent grouping.
- **Names and host constraints:** [naming lines 140-174][naming] currently prohibit hosts in ids. The requested `personal.reg.rig-sol` remains an illustrative subject identity, not proof of an inventory binding or an adopted naming exception. HOST below proposes clarifying this boundary explicitly before any later adoption.
- **Freshness and continuation:** [state fields][state] are work evidence; [conditional runtime adapters][sessions] establish neither deployed counters nor a session creation event. Point 8 is too restrictive if it delays even an advisory until a safe boundary. Notice can be pending earlier; actual continuation follows [existing package pick-up][resume].

## Model

### Minimal durable definition

This illustrative draft deliberately leaves repository identities unresolved. `personal-principal` and `chezmoi` are the owner's suggested home labels, not verified keys or URLs. Null here means unresolved, not permission to guess a binding. No actual package or registry is changed.

```yaml
id: personal.reg.rig-sol
description: >-
  Maintains Rig sol configuration. Takes sol-specific chezmoi units.
  Not for terra (personal.reg.rig-terra), the public Rig catalogue and
  rig.midnight.ninja (personal.reg.rig), KI Rig tooling (tools-rig),
  or shared chezmoi practice (ki.prj.chezmoi).
parent: personal.sop.main
level: regular
territory: personal
canonical_home: null
execution_home: null
created_at: null
worker: agent
supervisor: owner
```

`worker` and `supervisor` retain their current holder contract. Conditional `project` and `covers` remain available where current package kinds require them; this regular example needs neither. No `freshness` field, session identifier, live seat, machine-local path or new registry is added. Optional `theme`, `label` and `host_requirement` are extensions described below, not mandatory boilerplate. This draft intentionally cannot resolve homes until verified; it is not valid under today's closed schema.

| Field | Current | Proposed default | Validation |
| --- | --- | --- | --- |
| `id` | Required dotted identity | Required; unchanged | Folder/state agreement; unique work |
| `description` | Required positive and negative routing | Keep combined text | Non-empty; soft 500-character budget |
| `parent` | Conditional coordinating parent | Unchanged | Existing coverage and cycle checks |
| `level` | Territory, regular or project | Unchanged | Typed id agreement |
| `territory` | Not a field | Derive from id; optional assertion | Must match id and governance |
| `canonical_home` | Capital or approved Scope exception | Derive Capital if omitted | One canonical repository; approved exception |
| `execution_home` | Not a field | Unspecified if omitted | One repository identity if supplied |
| `created_at` | Optional timestamp or null | Unknown if omitted/null | Original creation; existing time ordering |
| `title` | Required | Derived display after migration | Read legacy title; preserve custom display |
| `theme` | Optional slug/null | No thematic assignment | Resolve supplied slug independently of level |
| `host_requirement` | Label/unit prose | No package-wide constraint | Typed inventory identity/category |
| `not_for` | Exclusions inside description | No new field initially | Scope resolves routing collisions |

**Homes and identity.** A supplied home is a canonical HTTPS repository identity under the existing registry identity contract, not an absolute path or an unqualified basename. Accept a convenient registered key as authoring input only when it resolves uniquely; write the verified canonical identity. Local registry resolution supplies the checkout path later. [Registry lines 117-124][registry] distinguish key, repository identity and local path; the [path-free projection][projection] does not make an arbitrary alias portable.

Omitted `canonical_home` derives the territory's verified Capital under [the location contract][location]. Explicit null is unresolved and does not silently invoke that default. An explicit Capital identity asserts the default. A regular/ad hoc member exception still needs the existing owner approval and parent coverage, with the Scope declaration retained during migration; a Project remains Capital-homed. Missing, conflicting or duplicate resolution stops resolved use. Metadata neither creates an exception nor moves anything. `territory` is an optional checked assertion, preserving the owner's name without requiring duplicate data on every definition.

**Default execution footprint.** Keep singular `execution_home` for one expected delivery repository. It is a planning/routing hint, never an implicit working directory, permission, exhaustive allowlist or actual target. Omitted/null means unspecified. Work spanning repositories leaves it unspecified and names the relevant repositories in its unit briefs/records; even when a default exists, each unit identifies and authorises its actual targets. This deliberately differs from both reviews' plural `execution_homes`: a list adds maintenance without replacing per-unit authority. Logical work identity, authoritative package home and delivery target remain separate.

**Host.** Propose optional `host_requirement: {kind: host, id: <inventory-id>}` or `{kind: category, id: <inventory-category>}` only for a constraint applying to the whole package. The example does not assert that `sol` resolves. Omission means no declared package-wide restriction, not universal executability. Most machine requirements belong on the relevant unit, allowing planning elsewhere. Preferences stay prose and cannot satisfy a hard constraint. Unknown, renamed or ambiguous required identities block device-dependent execution under [the existing boundary][host]. A subject suffix such as `rig-sol` must never be parsed as a live seat or a constraint: propose allowing an owner-chosen machine-related subject while retaining the prohibition on encoding session placement. This is a proposed naming clarification, not an assertion that the present standard permits it.

**Display without mandatory stored title.** Recommend the owner's removal as the destination model. Derive ordinary display from territory, level, topic slug and Project/theme metadata. Preserve an existing custom non-Project display in optional `label`; recognise legacy `title` while old definitions remain. A supplied label is an explicit display override, not identity or authority. If metadata cannot resolve, show the id with an unresolved-display indication; never fail identity resolution because a human name is missing. Renaming display metadata changes no id. Legacy label host suffixes require preserving their actual constraint in the existing prose or proposed host field before conversion. Continue emitting compatible `title` in reader projections for display consumers until they migrate. Reports keep meaningful headings and the closing thread line remains bare.

**Routing and theme.** Keep third-person purpose, "Takes ..." and "Not for ..." in the one register-loaded description; use Scope's `In:`/`Out:` when neighbours still overlap. An optional `not_for` could make authoring boundaries clearer, but no reviewed evidence demonstrates improved routing, and description-only readers would miss it. Do not maintain two competing exclusion texts. Any later split would need one source of truth, an automatically combined compatibility projection and the same combined budget. Keep regular as a level/display group, with optional independent theme; do not manufacture a `regular` theme page.

### Current-session evidence and footer

Durable definition carries package creation, identity and routing. Existing package state carries resumable work, authority references and outstanding ownership. Current-session age, message counts, observation coverage and compactions belong to runtime evidence, never `work.md` or work-state timestamps. Package age can be years while the session is minutes old; omit package age from the freshness footer.

Use wall-clock elapsed time from an evidenced conversation start, including idle. Do not call it active time. Prefer conversation volume as user-plus-assistant messages, counting each committed message event once, excluding system/tool events and deduplicating retries; label a different source's units explicitly rather than converting them into invented turns. A proposed adapter must evidence that counting contract. Unknown start or incomplete history means unknown full-session totals; a partial count can say "since observation". Tokens are optional supplementary evidence only when their scope is known: cumulative processed tokens, retained context and capacity are different quantities. Never estimate occupancy from message count.

Resume of the same evidenced conversation preserves its epoch. Idle increases elapsed time without increasing volume. An observed compaction keeps the conversation epoch and requires re-anchoring; a count is not evidence of lost understanding. A verified new conversation or full conversation reset starts another epoch; a counter/adapter reset alone starts an observation segment, not a new conversation. A client/model switch preserves totals only with continuity evidence; otherwise mark coverage unknown/new segment. None of these events changes package `created_at`, the work mark or authority.

Every signal has provenance, coverage and observation time. Owner-reported start is labelled owner-reported. A stale sample retains its last observation label; a lost clock or counter is unknown, never zero. Proposed display examples use invented observations only; they claim no deployed telemetry:

```text
Session 2h10m (owner-reported start) · volume unknown · as of 14:10 GMT
🧵 personal.reg.rig-sol
```

```text
Session 45m · 38 user/assistant messages (adapter, complete) · as of 14:10 GMT
🧵 personal.reg.rig-sol
```

```text
Session unknown · 12 messages since observation 13:50 GMT · restart check pending
🧵 personal.reg.rig-sol
```

Recommend volatile counters/observations only for the active session segment. No transcript scraping, content, native identifiers or portable host seat is required. If existing runtime evidence disappears, report unknown. No new persistent store or historical telemetry retention is proposed; persistence, if later justified, needs separate bounded expiry and privacy decisions. Uncertain adapter capability must not block a truthful indicator with unknowns.

### Restart recommendation

Prefer a fresh session once the existing package contains everything needed to resume. A proposed, reversible reminder heuristic is **four elapsed wall-clock hours or 100 evidenced user/assistant messages**, whichever available signal crosses first; no crossing may be claimed from unknown evidence. These are trial policy values, not proven limits, measured degradation or universal telemetry. Idle alone can trigger the elapsed reminder, which the owner may defer. Without either signal, show unknown and recommend checking resumability at the next natural unit boundary rather than claiming a numerical crossing.

A notice can say "fresh-session check pending" during a tool or run. Actual continuation waits for results and ownership to be reconciled and a verified resumable unit boundary. Use [the current resume lifecycle][resume] and [re-anchoring contract][reanchor]: exact work identity, five package files and open findings, current state/next steps, queries, decisions, queue receipt and outstanding run/write ownership. Never abandon a tool, duplicate a run, seize a contested index, move the mark or restart automatically. This applies existing safe resumability; it designs no package move, drain process or cross-host handover.

## Agreement and difference

Marks below report each review against the brief, not votes on this model. P is portability; F is freshness.

| Brief point | P / F | Settlement | Owner choice |
| --- | --- | --- | --- |
| 1. Portable homes | Add / Add | Canonical identity; singular default plus unit targets | HOMES, EXECUTION |
| 2. Authority/defaults | Agree / Agree | Capital and approved exceptions survive | HOMES |
| 3. Required host | Add / Add | Typed optional whole-package constraint; units otherwise | HOST |
| 4. Title removal | Agree / Agree | Remove after compatible displays; readers are migration constraints | DISPLAY |
| 5. Regular theme | Agree / Differ | Same semantic result: independent grouping, no invariant | THEME |
| 6. Exclusions | Differ / Add | Combined description now; no unmeasured improvement claim | ROUTING |
| 7. Freshness | Add / Add | Separate runtime age/volume, provenance and unknowns | SIGNAL |
| 8. Safe continuation | Differ / Add | Advisory early; continue only at recoverable boundary | RESTART |

Corrections cite primary evidence above. The principal design departures from both reviewers are singular default execution footprint and a clear title-removal destination. Retaining today's title forever or waiting for both metrics before displaying anything would confuse compatibility or uncertainty with a design veto.

## Rollout plan

This is a later plan only: no fixture run, pilot, record creation or schema change is authorised here. After owner decisions and separate delivery authority, capture bounded records in the owning repositories through the existing lifecycle. One fixture pilot precedes migration; it is verification of the chosen design, not another open-ended design review.

Fixtures cover missing/conflicting home identity, derived Capital and approved member exception, one default with multiple unit targets, unresolved host/category, legacy and title-free displays, missing/renamed Project/theme metadata, and ambiguous Rig neighbours at register depth. Measure misroutes/clarifications and loaded bytes/tokens against the existing combined description; no performance gain is assumed. Freshness fixtures cover old package/new session, idle, compaction, reset, client switch, stale/partial/unknown observations and pending tool/run/index ownership. Verify the capability of the one selected runtime from its actual events; unsupported signals stay unknown rather than delaying all display work.

Affected readers include Harness closed-field/identity/display validation, coordination naming/report consumers, Tools `workDefinition` and work-status schema/projections, Observatory displays/openers and register-routing consumers. Order later work as dual-reading compatible readers/projections first, then explicitly selected definition conversions, then removal of mandatory stored title. Preserve legacy inputs, custom names, exclusions, authority and existing exceptions throughout. No actual repository binding or machine-local root is supplied by this report. No parallel rollout wave precedes the first pilot's evidence.

## Decisions

Each choice approves or edits the proposed design only. None grants implementation, pilot execution, publication, release or transfer authority.

### HOMES - Repository identity and defaults

**Context:** Existing packages default to the territory Capital, with approved regular/ad hoc exceptions. Local keys and canonical repository identities differ. Explicit metadata must not create a new home or permission.

**Query:** Use canonical repository identities, a derived Capital default and optional checked `territory`?

**Options:**

a) (recommended, confidence high - portable identity and existing authority remain distinct) Use the HOMES model above: optional matching `territory`, omitted `canonical_home` derives Capital, explicit null stays unresolved, supplied identities must resolve uniquely and exceptions retain their approval requirements.

b) Keep home declarations only in current Scope and omit both new fields; retain the current resolution contract.

### EXECUTION - One default delivery footprint

**Context:** Both reviews prefer plural execution repositories. A list still cannot authorise actual unit targets and requires maintaining a second inventory. The owner proposed singular `execution_home`.

**Query:** Keep one optional default, with actual and additional targets declared per unit?

**Options:**

a) (recommended, confidence high - preserves the owner's name and avoids duplicating unit scope) Keep singular `execution_home`, unspecified when absent/null, as one repository hint; every unit declares its authorised targets, including additional repositories.

b) Depart to plural `execution_homes` as an optional list of anticipated repositories; units still declare their actual authorised targets.

### HOST - Required machine versus session seat

**Context:** Device constraints already resolve through inventory, while live placement stays out of packages. Most constraints belong to units. The current naming ban needs clarification for the owner's illustrative machine-related subject id.

**Query:** Add an optional whole-package host/category requirement and distinguish subject naming from live placement?

**Options:**

a) (recommended, confidence high - explicit constraints do not imply placement or authority) Adopt the optional typed `host_requirement` design, normally using unit constraints instead; unresolved required identities block device-dependent execution. Permit owner-chosen machine-related subjects such as illustrative `rig-sol`, with no inferred binding and no live-seat encoding.

b) Retain all constraints in existing labels/Scope/unit prose and retain the current host-in-id prohibition; choose a different subject id before any adoption.

### DISPLAY - Remove mandatory stored title compatibly

**Context:** Readers currently require title, but ordinary names are derivable and the owner wants a smaller definition. Custom labels and report headings must keep their meaning.

**Query:** Approve title removal as the destination, after compatible readers and preserved display overrides?

**Options:**

a) (recommended, confidence medium - feasible from naming rules, but compatibility needs fixture proof) Remove mandatory stored `title` after dual-reading readers can derive names, preserve custom display in optional `label`, expose compatible display projections and fall back visibly to id when metadata is unresolved.

b) Retain required stored `title` as the permanent authoring contract, updating it from display metadata as today.

### THEME - Independent grouping

**Context:** Regular is a work level; theme is optional thematic grouping. Requiring `theme: regular` would replace meaningful grouping or require an invented theme.

**Query:** Keep theme independent and derive a Regular work display group from level?

**Options:**

a) (recommended, confidence high - preserves both meanings without extra metadata) Keep optional/null `theme`, validate supplied theme slugs, and derive regular grouping from `level`; impose no regular-theme invariant.

b) Make regular level imply `theme: regular`, deliberately replacing independent grouping for those packages and requiring a separately authorised real theme definition.

### ROUTING - One exclusion source

**Context:** Description already includes exclusions at register depth. A separate `not_for` could improve authoring clarity but has no demonstrated routing gain and risks hidden or conflicting boundaries.

**Query:** Keep the combined description as the proposed routing contract?

**Options:**

a) (recommended, confidence high - simplest design matching the actual reveal boundary) Retain purpose, Takes and Not for in `description`, the combined soft 500-character budget and Scope collision handling; add no anti field in this design.

b) Introduce optional text `not_for` as the sole exclusion source when present, with positive-only authored description, a combined legacy projection and the same total soft budget; migrate all register readers before conversion.

### SIGNAL - Truthful session indicator

**Context:** No reviewed source proves universal telemetry. Package timestamps cannot supply session age. Useful partial evidence can coexist with explicitly unknown signals.

**Query:** Display separately evidenced age and volume with volatile runtime observations and explicit unknowns?

**Options:**

a) (recommended, confidence high - useful without fabricating counters or adding package state) Use elapsed wall-clock age and user/assistant message volume where evidenced, with coverage, provenance and observation time; preserve the epoch/reset rules above, unknown/stale labels and no new persistent telemetry store.

b) Show only a qualitative resumability reminder until one client can evidence both full-session age and volume; keep numerical freshness display deferred.

### RESTART - Advisory policy and safe continuation

**Context:** Neither review establishes a universal threshold. Waiting for perfect telemetry would delay a useful reminder; automatic restart could abandon work. Existing package pick-up already defines resumability.

**Query:** Approve the reversible four-hour/100-message reminder policy as a proposed pilot heuristic?

**Options:**

a) (recommended, confidence medium - actionable trial values, with no evidence they predict degradation) Propose a pending reminder at four elapsed hours or 100 evidenced user/assistant messages; unknown signals cannot cross a threshold. Continue only at the existing verified resumable boundary, never automatically; with no counters, check there qualitatively. Separate authority is required to run the pilot.

b) Use the same truthful display and safe-boundary recommendation without numerical reminders; let the owner request a fresh session or choose a heuristic later.

## Changes after review

- Freshness review clarified accepted null creation time and the parser's warning-only description budget; both are now explicit.
- Both reviews' evidence preserved authority/defaults, independent theme, existing exclusions and unknown telemetry; their differing point-5 marks were reconciled by semantic content and primary sources.
- Both reviews favoured plural execution hints; this synthesis keeps the owner's singular field as a default, with per-unit scope doing the remaining work.
- Both reviews retained title initially; this synthesis makes removal the destination and compatibility a migration condition, preserving custom display rather than treating current readers as a veto.
- Portability review's host/id warning became an explicit naming clarification choice; no actual host binding is inferred from the illustration.
- Portability review's early-advisory correction and freshness review's recoverable-boundary rule are combined. Numerical values are explicitly proposed and reversible; neither telemetry research nor missing counters blocks a truthful unknown indicator.
- The latest steer excludes movement, transfer, orchestration and new drain-process design. Earlier drain-related provenance grants no such design or execution authority here.

[definition]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L184
[creation]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/scripts/rubric/contexts/work-package.ts#L617
[budget]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/scripts/rubric/contexts/work-package.ts#L813
[reader]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/work/status.ts#L230
[naming]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#L140
[theme-parser]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/scripts/rubric/contexts/work-package.ts#L605
[themes]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-work/references/standards-project-registry.md#L99
[state]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L223
[sessions]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L367
[registry]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/storage/local-registry.ts#L117
[projection]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/docs/specs/registry.md#registry-005--path-free-machine-inventory
[location]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L50
[host]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L423
[resume]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L406
[reanchor]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#re-anchoring-after-compaction
