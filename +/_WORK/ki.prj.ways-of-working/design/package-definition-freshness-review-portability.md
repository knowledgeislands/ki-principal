---
work: ki.prj.ways-of-working
run: wow-package-definition-review-a-20261029
agent: codex
written_at: 2026-10-29T20:44:50Z
---

# Package definition and session freshness: review by portability reviewer

**Reviewer:** Codex, `gpt-6.1-sol` (launch record) · **Date:** 2026-10-29 · **Read-only:** yes, except this review

## Own view

Resolve the authoritative repository independently from delivery repositories; constrain units to required machines; observe conversations separately. Repository references and host requirements grant no access, execution, acceptance or stewardship.

Retain titles initially. The stronger immediate improvement is testing existing descriptions against neighbouring work. A separate exclusion field and a freshness score both risk suggesting precision their consumers cannot support.

## Fact check

The brief matches blob `cdea9ce65efc0de10282a67bd4aac955d196a898` at `9fef9813f327b2c09f6cd4f752d3dc2149f7b8bf`. Sources freeze Harness at `99bd8fc078d2a283e037e5d27e14ce01ce96b644`, Tools at `76df015a41365591aa56a3b7ac13f9baf7994ac0`, and Principal metadata at `eb6bf278fee4f960e09041dbe5d28b97bd29c113`, confirming `Ways of working` and `Model`. No newer product source is substituted.

The brief's field set, home exceptions, registry distinction, display consumers, existing exclusions, host boundary and timestamps check out. Local registry keys and conditional bindings do not establish portable identity or deployed counters. No other review, merged report, work queries/decisions, transcript, private report or live registry payload informed this view.

## Points

| Point | Mark | Reason and evidence |
| --- | --- | --- |
| 1 | Add | Resolve canonical identity; allow multiple delivery repositories. |
| 2 | Agree | Preserve authority and deliberate exceptions. |
| 3 | Add | Type host constraints and apply them to the right unit. |
| 4 | Agree | Footer simplification does not remove display consumers. |
| 5 | Agree | The semantic test supports grouping independently of regular level. |
| 6 | Differ | Separate exclusions have not demonstrated a routing improvement. |
| 7 | Add | Require observable provenance and an explicit measurement epoch. |
| 8 | Differ | Recommend early; defer continuation until a safe boundary. |

1. **Identity:** [registry validation, lines 117-124 and 197-200][registry] separates a stable local key, canonical HTTPS GitHub repository identity and physical path. A basename can change or collide between owners. Prefer canonical URLs as identity, keys as hints, and existing registry resolution for paths. A single execution home cannot represent cross-repository delivery; a list describes the expected footprint, while each authorised unit identifies its actual target.

2. **Authority:** [package location, lines 52-58][package] requires one physical package/queue, Capital-homed Projects and deliberate approved regular/ad hoc exceptions. Derive the default from territorial governance, never from the current checkout. An explicit canonical home must match it or an approved exception; metadata cannot create that exception. Derive territory from the id; an optional asserted territory must agree. Missing, duplicate or conflicting resolution stays unresolved.

3. **Hosts:** [boundary, line 425][package] distinguishes concrete hosts from categories and blocks device-dependent execution on unknown, renamed or ambiguous identity. A typed hard constraint is clearer than a label alone, but package-wide constraints overconstrain planning. Prefer per-unit requirements unless every unit truly needs the host; keep preferences separate. `rig-sol` is the requested opaque work identity, not evidence that its suffix resolves an inventory host. The existing no-host-in-id convention also needs explicit reconciliation before any naming rollout.

4. **Titles:** [Tools, lines 230-253][status] rejects missing titles; [naming, lines 167-174][coordination] supplies display meaning. Project metadata cannot supply an arbitrary regular topic's chosen name. Retain title, optional label and backward readers; missing registries display id plus unresolved-name indicator. Renaming changes display, never identity.

5. **Themes:** [theme contract, line 99][themes] explicitly permits themes on regular, Project and ad hoc work. Enforcing `theme: regular` would erase meaningful thematic grouping. Omitted/null means no thematic assignment; `regular` or another slug must resolve an actual theme. Derive the regular display group from `level`, without creating a theme page.

6. **Routing:** [description shape, line 206, and reveal, lines 334-341][package] already provide “Takes”/“Not for”, register routing and Scope disambiguation. A split field is useful only if every register consumer loads it; description-only readers otherwise lose exclusions. Specify precedence, combined size budget and contradictory-neighbour behaviour before adoption. Test identical reveal depth, routing accuracy, abstentions, bytes/tokens loaded and lookup latency; no performance gain is established.

7. **Freshness:** [creation time, line 202, state timestamps, lines 249-253, and bindings, lines 369-388][package] support none of the proposed universal counters. Package age and work heartbeat are not session age or conversation volume. Observability needs a client capability contract, not inference from a start-like hook or package date.

8. **Continuation:** [resume, lines 406-415][package] reconstructs work, not the preceding conversation. An advisory can appear while a tool runs, saying continuation is pending; requiring safety before even recommending delays useful notice. Actual continuation must reconcile results, unreceived/queued runs, write ownership and package state, next steps, queries, decisions, messages and findings. Never abandon a tool, duplicate a run, seize an index, transfer a host or move the mark automatically.

## Proposed definition

Illustrative candidate; private repository/inventory identities remain unresolved:

```yaml
id: personal.reg.rig-sol
level: regular
title: 'Personal > Rig configuration'
parent: personal.sop.main
theme: null
description: >-
  Maintains the selected Rig configuration. Takes configuration units.
  Not for terra (personal.reg.rig-terra), public Rig (personal.reg.rig),
  Rig tooling (KI tools-rig) or shared practice (ki.prj.chezmoi).
canonical_home: {key: personal-principal, repository: null}
execution_homes:
  - {key: chezmoi, repository: null}
host_requirement: {kind: host, id: sol}
worker: agent
supervisor: owner
```

`repository` is the canonical HTTPS identity; null explicitly means unknown and blocks resolved use, even when a key suggests a candidate. Confirm the mapping rather than guessing an owner URL. `key` is an optional local hint, never an alternative authority. Missing canonical home derives the Capital subject to approved member exceptions; explicit null does not invoke that default. Missing/empty execution list declares no default target; per-unit authority remains required. The illustrative hard `sol` requirement needs inventory confirmation and applies only if adopted for the whole package; otherwise move it to relevant briefs. Omitted host means no declared device constraint, not universal executability. Omit unknown `created_at`; never substitute today's date. No portable live seat or `freshness` field. These additions would require a versioned closed-schema migration; current definitions reject them.

## Freshness alternatives

- **Elapsed hours:** requires a trusted current-session start, clock and observation time. Wall time includes idle; active time additionally needs evidenced activity intervals. Resume preserves the epoch; a verified new conversation/reset starts another. A client/model/host switch alone proves neither.
- **Turns/messages:** requires documented roles, counting rules and complete events since that epoch. Tool messages, retries and branches need explicit treatment. Missing history means a partial count or unknown, never zero.
- **Tokens/context:** requires runtime-supplied usage and a defined denominator. Cumulative processed tokens, current retained context and remaining capacity are different measures; cached/repeated input can inflate totals. No exact cross-client value is established here.
- **Compactions:** requires explicit, deduplicated events and a known counting baseline. Compaction may reduce retained context while preserving conversation age; it must not reset age automatically. Event counts do not measure lost understanding.

All observations need provenance, coverage/reset semantics and observation time. Stale data stays labelled stale; unavailable data stays unknown. Use existing runtime evidence only when independently validated, with local minimal counters, bounded retention and deletion on epoch disposal. Do not infer transcript scraping, provider telemetry or a second permanent session store. No OpenAI product-mechanics claim or universal safe threshold is made.

## Findings

### PORTABILITY - Separate identity from resolution

**Goal:** Review portability and routing for Kris's 29 October proposal.

**Scope:** Frozen contracts/code and brief; no private registry payload or source mutation.

**As of:** 29 October 2026.

Local keys need canonical identity confirmation. Keep title and independent theme grouping; test existing exclusions before splitting fields. Home and host metadata confer no authority. Raises SCHEMA and ROUTING.

### FRESHNESS - Preserve uncertainty

**Goal:** Assess a useful freshness signal and safe continuation.

**Scope:** Measurement requirements and recovery contracts; no verified client telemetry.

**As of:** 29 October 2026.

Display age and volume separately with provenance or unknown. Keep recommendations advisory and continuation conditional on a verified boundary. Raises FRESHNESS.

## Unresolved decisions and minimal pilot

Owner choices: SCHEMA (URL/hints, delivery cardinality, host granularity), ROUTING (prose versus split field), FRESHNESS (metrics, retention, advisory policy).

After approval, pilot one proposed definition offline against old/new readers and ambiguous Rig neighbours; simulate relocated checkouts, absent/conflicting identity, new/idle/compacted sessions, unknown counters and in-flight work. Compare routing accuracy and loading cost before schema adoption. Separately validate one runtime's actual event/counter capability. Choose any trial advisory trigger explicitly as an experiment, never a safety guarantee; implement no automatic restart.

[registry]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/storage/local-registry.ts#L117
[status]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/work/status.ts#L230
[package]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md#L52
[coordination]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#L167
[themes]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-work/references/standards-project-registry.md#L99
