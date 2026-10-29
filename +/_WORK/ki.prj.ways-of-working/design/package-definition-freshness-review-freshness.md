# Package definition and session freshness: review by freshness

**Reviewer:** Codex / gpt-6-astra, confirmed from this run's launch record · **Date:** 2026-10-29 · **Read-only:** yes, except this review artefact

**Working mark:** draft, independent review · **Owning work:** `ki.prj.ways-of-working` · **Coordinator mark:** 2026-10-29T16:18:42Z

## Own view

Keep the portable definition about work; make freshness a qualified observation about the current session. Neither age nor volume proves degradation or safe continuation. An old, idle conversation can have little content; a new conversation can already contain a large imported context. Better handover evidence matters more than an attractive freshness score.

This view was formed without another review, merged report, work queries/decisions, vendor transcript or private report. The working brief byte-matched commit `9fef9813f327b2c09f6cd4f752d3dc2149f7b8bf`. Product evidence below uses only the frozen Harness and Tools revisions; no newer product behaviour or OpenAI telemetry is asserted. No network or private registry payload was used.

## Fact check

- **Definition and homes confirmed:** [Harness package contract][package], lines 50-58 and 164-209, separates one physical package/queue from receiver-owned execution. Projects remain Capital-homed; regular/ad hoc exceptions require owner approval, `Home:` and parent coverage. [Parser][parser], lines 51-62, excludes proposed homes, territory, freshness and anti fields.
- **Display and routing confirmed:** [Tools reader][reader], lines 228-252, rejects a missing title and projects theme and description. [Naming][naming], lines 140-173, separates titles from ids; the bare footer does not supersede display consumers. Package lines 205-209 and 328-341 already provide exclusions and progressive loading. Its 500-character limit is mechanically a warning, not rejection: parser lines 813-816.
- **Identity clarified:** [Registry parser][registry], lines 104-124, binds a local key to canonical HTTPS repository identity and a local path; [path-free projection][registry-spec] omits paths. A convenient local key is not independently a portable identity guarantee.
- **Freshness confirmed absent:** package lines 223-252 describe work-state timestamps, not session counters. Lines 367-388 make bindings identity-only and reminder adapters conditional. One small omission: parser lines 617-618 explicitly accept null `created_at`; unknown package creation need not be fabricated.

## Points

| Point | Mark | Reason and evidence |
| --- | --- | --- |
| 1 | Add | Resolve canonical identity once; execution may span repositories. See definition below and registry evidence. |
| 2 | Agree | Capital default and approved exceptions survive; metadata grants no authority. Package lines 50-58. |
| 3 | Add | Separate hard host requirements from preferences and live seat. Package lines 423-425. |
| 4 | Agree | Preserve display meaning before removal; retain title for this pilot. Reader lines 228-252. |
| 5 | Differ | Reject the proposed mandatory regular theme. Type and theme are independent; parser lines 605-612. |
| 6 | Add | Existing exclusions are real; compare representations at equal loading depth, not by field count. |
| 7 | Add | Age, volume and observation coverage need separate provenance and reset semantics. See FRESH-EVIDENCE. |
| 8 | Add | Threshold crossing can flag a pending recommendation; safe continuation needs a verified boundary. |

Point 5 differs from the proposed invariant, not from the brief's request to test alternatives. Omitted/null theme means no thematic grouping; `regular` or another slug requires a real theme if supplied. Derive a Regular work display group from level without inventing a registry theme. Umbrella and ad hoc packages share the level but retain distinct scope.

## Proposed definition

Illustration only, not valid under today's closed field set or evidence that these bindings exist:

```yaml
id: personal.reg.rig-sol
parent: personal.sop.main
level: regular
title: Personal > Rig sol
theme: null
description: >-
  Maintains Rig sol's machine configuration. Takes sol-specific chezmoi work.
  Not for terra (personal.reg.rig-terra), the public Rig catalogue and
  rig.midnight.ninja (personal.reg.rig), KI Rig tooling (tools-rig),
  or shared chezmoi practice (ki.prj.chezmoi).
canonical_home:
  repository_key: personal-principal
execution_homes:
  - repository_key: chezmoi
host_requirement:
  kind: host
  inventory_key: sol
  strength: required
worker: agent
supervisor: owner
created_at: null
```

The id is canonical work identity; its territory prefix is ownership, not access permission. Omit duplicated `territory`; if introduced, mismatch must fail validation. Resolve each illustrative key through the existing registry to canonical repository identity; committed portable homes should carry that verified identity rather than assume aliases agree across machines. No raw path or new registry is needed.

Absent canonical home derives the verified territory Capital. An explicit member exception needs existing owner approval and parent reference; contradictory declarations stop resolution. Execution homes describe anticipated footprint, never a default working directory or authority. Omission means unspecified, not canonical-home execution; units may name narrower or additional authorised repositories.

Host requirement names an inventory identity/category, never the current seat. Omission means no package-wide constraint; unit-specific constraints still apply. A preference cannot satisfy a hard requirement. `sol` is only an illustrative unverified key here: unknown, renamed or ambiguous identity blocks device-dependent execution. No home field permits source access, relocation or acceptance.

Retain title until non-Project labels and missing/renamed registry displays have tested fallbacks. Keep the current description including exclusions for compatibility. A separate anti field risks invisible exclusions in description-only readers; structured neighbour ids could improve validation but require one defined source of truth and projections. Test ambiguous examples, wrong-route rate, clarification rate, loaded bytes/tokens and retrieval time at the same reveal level. Do not claim measured improvement. Load Scope on collision, package detail on pick-up, reports only on demand.

## Findings

### FRESH-EVIDENCE - Observe a session, not package age

**Goal:** Truthful freshness signals.

**Scope:** Client adapters and their display evidence.

**As of:** Frozen source revisions, 29 October 2026.

| Candidate | Reliable evidence required | Limit |
| --- | --- | --- |
| Elapsed hours | Verified session creation event and clock basis | Includes idle; says nothing about volume. |
| Active hours | Defined activity intervals, sleep/idle accounting | Foreground time is not reasoning time. |
| Turns/messages | Defined event types, complete ordered coverage, deduplication | Tools, retries and edits need explicit rules. |
| Tokens/context | Provider usage with scope, or measured current-context usage/capacity | Cumulative usage is not context occupancy. |
| Compactions | Explicit successful compaction events within known coverage | Count cannot measure retained meaning. |

No selected evidence establishes universal availability across clients. Expose value, unit, provenance, coverage start and observation time; unavailable stays unknown, stale stays visibly stale, never zero. A manually witnessed start is labelled owner-reported. Adapter start/resume/compact events must not silently become session creation.

Idle increases wall-clock age only. Compaction changes context but does not reset session age; count it only when observed. Model/client/host changes require continuity evidence or a new observation segment, not guessed cumulative totals. A new session resets session counters, never `created_at`. Lost instrumentation is a coverage gap, not a fresh conversation.

Prefer derived, volatile runtime observations; no package telemetry, transcript scraping or second permanent session store. If opt-in local persistence proves necessary, retain only minimal counters/provenance for the active segment, remove them on retirement, and agree a bounded stale-entry expiry before enabling it. Exclude content, native identifiers and host seat from portable output. Unknown telemetry should encourage checking continuation evidence, not block ordinary work indefinitely.

### SAFE-CONTINUATION - Prepare a recoverable boundary

**Goal:** Continue without abandoned work or lost authority.

**Scope:** Advisory warnings and existing package pick-up.

**As of:** Frozen package contract, lines 390-415.

A threshold is an owner-selected reminder policy, not a universal safety limit. Flag pending attention during a running tool; do not interrupt, restart or move work state automatically. Receive or explicitly retain ownership of runs, finish the verified unit, and leave a contested index untouched. At the safe boundary, verify current state, next steps, open questions, decisions, queue receipt and outstanding run ownership in the existing package. Preserve the mark unless authorised to move it. A fresh session resumes the work, not the previous conversation; a host change additionally requires applicable checkout and source-access checks, never package copying.

## Unresolved decisions and minimal pilot

Recommend, subject to owner decision: retain title and independent theme; prefer verified repository identities with plural execution hints; keep combined routing text initially; show age and any evidenced volume separately, with unknowns explicit. Remaining choices are structured host requirements versus existing unit prose, exclusion representation, event/count definitions, retention and advisory thresholds.

Run one bounded, read-only fixture pilot before implementation: old package/new session, idle, compaction, client/host switch, missing counters, routing collisions and disputed home/host identities. Include running-tool, unreceived-run and contested-index continuation cases. Record observability and handover omissions, not a fabricated freshness score. Owner review of that evidence precedes adapter/schema changes or a numerical threshold.

[package]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/references/standards-work-package.md
[parser]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/governance/ki-work-package/scripts/rubric/contexts/work-package.ts
[reader]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/work/status.ts#L228
[naming]: https://github.com/knowledgeislands/ki-agentic-harness/blob/99bd8fc078d2a283e037e5d27e14ce01ce96b644/skills/change-management/ki-coordination/references/standards-coordination.md#work-naming
[registry]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/src/core/storage/local-registry.ts#L104
[registry-spec]: https://github.com/knowledgeislands/tools-ki/blob/76df015a41365591aa56a3b7ac13f9baf7994ac0/docs/specs/registry.md#registry-005--path-free-machine-inventory
