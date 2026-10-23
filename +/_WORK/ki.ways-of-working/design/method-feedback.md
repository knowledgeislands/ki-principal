---
note_type: streams/design
title: The smallest changes from 68 method feedback lines
status: draft - October 2026
purpose: Remove covered feedback and isolate the remaining small changes
author: Written with Codex
work: ki.ways-of-working
run: ways-of-working
agent: wow-method-feedback
written_at: 2026-10-23T01:49:13Z
---

# The smallest changes from 68 method feedback lines

14 themes: 11 already handled, 3 changes, 2 high confidence. All 68 physical lines are assigned once below. Overall confidence is medium because the Cloudflare token-type boundary and some product delivery evidence remain unverified.

Proposal for [Ways of working](<../../../../Streams/Projects/ways-of-working.md>), 23 October 2026, under Kris's bounded instruction to review these lines and commit this proposal. His standing steer is to avoid over-engineering. Nothing here enacts a method change, accepts or prunes a record, disposes of a queue line or authorises a credential read.

Already handled means the current method or the existing proposal supplies the behaviour, or the line belongs to an existing receiver's delivery. It does not mean the receiver has completed the work. Keep unresolved receiver obligations in their own queues. The earlier proposal remains a proposal; its choices are not silently treated as adopted policy.

## Evidence

- **Inventory:** [Take-stock report](</Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-take-stock.report.md>), section 1, in listed order, numbered F01-F68 here. Sections 2 and 3 bound the acceptance and prune evidence; neither action is part of this run.
- **L:** [Coordination lessons](<coordination-lessons.md>), lessons 1-23. Lesson numbers below refer to that proposal.
- **C:** [Coordinating-work standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md>), and the actual [coordinator output style](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md>).
- **D:** [Background-run standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md>).
- **K:** [Work-package standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md>), particularly its ownership boundary and Tidying the work folder.
- **WCF:** [Cloudflare hosting standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-website-cloudflare/references/standards-cloudflare-hosting.md>), Branch previews behind Access.

The local harness method baseline is `0aa9c4d2`. Queue links below identify the lines read, not immutable line numbers. Older compacted instructions were checked in the local Git object `20b5fce0bb34c213b3bfcec9c7e437eef5e45e1e`; no remote was consulted. Helper verification read only source and non-secret contract wording, never credential stores, caches or values.

## Themes

### T01 - Refresh notices and regular-work scope

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 12 | C Refreshing; C Reply forms; L2 | Already handled | high |

**Queue:** [F01], [F02], [F19], [F23], [F27], [F32], [F44], [F47], [F50], [F51], [F52], [F55].

The notices ask receivers to use rules already in force. C, Refreshing this guidance, records receipt in `method_read` without a second acknowledgement. C, Levels and forms and Coordinator-only machinery, and L2 already keep regular work conversational. In particular, F52 does not turn regular work into a coordinator: apply the current role boundary when receiving the old banner instruction. Held work waits for its authorised resume. No new refresh protocol or banner rule.

### T02 - Package housekeeping and report retention

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 24 | K Closed list and Tidying; C Pruning | Change P3 | high |

**Queue:** [F07], [F08], [F17], [F20], [F21], [F24], [F25], [F26], [F28], [F29], [F30], [F31], [F33], [F34], [F35], [F45], [F46], [F48], [F49], [F53], [F54], [F56], [F57], [F66].

The dated audit and closed-folder notices mostly require receiver-owned application of the existing rules, with current evidence checked before a repair. They do not revive the old pilot acceptance gate. One genuine inconsistency remains: K, Tidying the work folder, says a five-file package copies queries in full into `queries.md` and can then tidy a homed report before the queries are answered. C, Pruning the work folder / Judgement, and the generated output style still require the report queries to be answered. P3 removes that contradictory extra retention condition. It does not decide which of these receivers may tidy anything now.

### T03 - Handoffs, receipts and stale claims

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 9 | C Claims; Messages; Design notes; L18 | Already handled | high |

**Queue:** [F03], [F04], [F05], [F09], [F11], [F18], [F40], [F63], [F64].

Handoffs already travel as messages, not sender-created roadmap items. C, Claims, requires checking surviving records and ownership directly; Messages between work requires a disposition before removing a line; Design notes keeps anything whose outcome or authority is not homed. L18 already clarifies that a receipt need not mean the requested work is complete. The stale Review, ledger, landed title-check and historical HNR claims need bounded verification or receiver delivery, not new method. Retain bring-up obligations and the Rig rework/integration request until their exact dispositions are established. No automatic close-out or receipt-inference rule.

### T04 - Catalogue and runtime guidance rollout

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 3 | C Generated surfaces; D Prompt shape | Already handled | high |

**Queue:** [F06], [F62], [F68].

The website catalogue refresh, Rig doctor binding checks and hook rollout are implementation or distribution obligations. C, Generated surfaces, already makes the coordination standard the source for the output style and report surfaces. D, Prompt shape, carries target-repository rules into each brief. A catalogue or doctor still needs its own delivery receipt; current method coverage is not evidence that those products shipped. No extra rollout register or method copy.

### T05 - Theme migration and enforcement cutover

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 2 | C The tolerance window | Already handled | high |

**Queue:** [F12], [F14].

C explicitly accepts Initiative paths and fields with warnings until every territory has moved and phase 5 closes the migration. The feedback asks for that closure and the remaining receiver migrations. It does not justify changing warnings to failures while the declared window is still open. The owner of the migration should establish completion and then remove tolerance through its existing delivery. No competing calendar deadline or new migration mechanism.

### T06 - Central waking and launch defaults

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 2 | C Heartbeat; D Run queue; L14-L19 | Already handled | medium |

**Queue:** [F13], [F58].

A territory tick overlaps L14-L19: bounded away authority, honest session-wake limits, completion watching and explicit choices about message-only pickup. C, Coordinator responsiveness / Heartbeat, and D, Run queue, already name OOS-WAKE; launcher defaults and CONTROL-CONTRACT delivery belong to tools-ki. Compare that candidate with the existing proposal before commissioning more work. No second timer, liveness store or scheduler design here. Confidence is medium because this review does not certify the control-contract implementation.

### T07 - Draining and the visible ending

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 1 | C Putting work on hold; L8-L9 | Already handled | high |

**Queue:** [F22].

The hold procedure already drains and parks work. L8 adds wake cancellation and a truthful running/queued/scheduled check; L9 already isolates the DRAIN ending choice. C, Banner, now closes with the thread line and emits no resume prompt. The receiver must reconcile its old DRAIN line with its own later authority. No new state, duplicated proposal or resurrected resume line.

### T08 - Non-interactive 1Password reads

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 1 | D Authority tiers lacks helper rule | Change P1 | high |

**Queue:** [F15].

D currently bans secret handling by default but does not state the requested read mechanism for a separately authorised run. The local helper source confirms service-account-only mode prevents desktop fallback and returns failure when it cannot read. P1 records that mechanism without granting a credential read. The cache, token files and credential values were not read or exercised.

### T09 - Shared Cloudflare credentials and private inventory

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 1 | D and WCF lack managed-helper pointer | Change P2 | medium |

**Queue:** [F16].

The private, chezmoi-owned guide already names `cf_token`; its source invokes `op_cache` with service-account-only mode. D and WCF do not point authorised runs to that contract. P2 adds the pointer and keeps personal credential inventory out of territory notes. It remains medium: WCF, Branch previews behind Access, currently calls for a user-scoped token, while the helper selects account-owned tokens. This run did not test API compatibility. Preserve the existing token-capability requirement and stop on an unsupported credential rather than silently substituting one.

### T10 - Serving conventions and delivery completion

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 4 | C Claims; Decisions / Rule | Already handled | high |

**Queue:** [F36], [F37], [F38], [F39].

The original serving claim is explicitly corrected in the next line. The retained owner decision concerns source-watch serving and whether Observatory's repository-local finish convention should become an HTTP check with restart as fallback. C, Claims, already prevents acting on the superseded build claim, and Decisions / Decision classes homes a local rule in that repository's `AGENTS.md`. That bounded receiver decision remains open; no universal build/restart requirement belongs in coordination or delegation.

### T11 - Work views, openers and hook consumers

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 4 | C Work naming; Opening work; Surfaces | Already handled | medium |

**Queue:** [F10], [F42], [F43], [F67].

C already defines titles, work identity, bootstrap behaviour and the opener text, while `ki work status` is the derived view. One CLI-owned opener renderer and an Observatory consumer should reuse those sources; older send/resume wording is superseded by the current thread-line contract. The hook-event idea should first compare the existing run events and work-state projection. The routing-view and JSON compatibility choice remains tools-ki's bounded API design; this review does not choose a schema version or certify its delivery. No parallel opener template or agent-state model.

### T12 - CLI grammar, message identity and evidence limits

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 3 | C Work naming; K Messages and Tidying | Already handled | high |

**Queue:** [F59], [F60], [F65].

Remaining grammar departures belong with the next affected command change. C, Work naming / Title and label, already identifies a work sender's authoritative title; whether the command resolves an explicit sender id or takes a validated argument is CLI design. K already leaves report deletion to judgement over named candidates and keeps open or unhomed material, so a prune command needs explicit report selection rather than an inferred sweep. The host-evidence request already distinguishes mechanical facts, judgement and unavailable facts. No new method field, deletion heuristic or blanket grammar rewrite.

### T13 - Worktree audit workaround

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 1 | D Coordination / Worktree audit | Already handled | high |

**Queue:** [F61].

D explicitly requires the isolated-home audit recipe until linked worktrees give the registered repository's verdict. F61 says retiring that recipe remains unverified. The smallest action is an exact replacement-verification receipt through tools-ki, followed by a bounded edit to that existing paragraph if it passes. This review supplies no such receipt and proposes no speculative removal, broader registry change or new worktree policy.

### T14 - Visual sizing preflight

| Lines | Coverage | Disposition | Confidence |
| --- | --- | --- | --- |
| 1 | Owning plan and existing preflight | Already handled | high |

**Queue:** [F41].

The line asks the owner of the next planning pass to supply missing sizes. It is a planning-completeness defect, not evidence for a new coordination or delegation rule. Keep it with Observatory's existing preflight and records; no extra method gate or repeated waiver.

## Proposed changes and exact homes

### P1 - Non-interactive 1Password access - high

**Home:** `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md`, Authority tiers, one paragraph after the default credential prohibition. This is an additional condition on an explicitly authorised read, not an authority grant.

**Smallest wording:** In Kris's managed environment, when a brief separately authorises a 1Password read, use the managed `op_cache` helper with `OP_CACHE_SERVICE_ACCOUNT_ONLY=1`, never call `op` directly, and use `op_cache --tag <tag>` for discovery. If the helper cannot read without a desktop prompt, stop and report; do not fall back to interactive access. Keep values out of output and tracked files.

**Why high:** F15 carries the owner's dated choice. The helper source confirms the fail-closed mode and tag discovery. This is one reversible prose addition about an existing tool, with no helper, environment or credential mutation. The default secret-handling ban remains in force for every run without separate authority. The runtime-owned helper is currently `~/bin/chezmoi/op_cache`; the method should name the managed contract rather than duplicate its implementation or private inventory.

### P2 - Shared Cloudflare read contract - medium

**Home:** the same D file and Authority tiers paragraph, immediately after P1, plus one cross-reference in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-website-cloudflare/references/standards-cloudflare-hosting.md`, Branch previews behind Access, its credential step. Keep the reusable rule in D; do not copy a private token register into either standard or add a new rubric family.

**Smallest wording:** In Kris's managed environment, an explicitly authorised Cloudflare credential read uses `cf_token`, following the private, runtime-owned Cloudflare credential guide. Keep his 1Password item ids, token ids and names, and personal token permission inventory out of territory notes. If the helper cannot supply a credential with the capabilities the task requires, stop and report; do not use direct `op` access or silently substitute a token type.

**Why medium:** F16 supplies the uniformity and privacy requirement; source confirms `cf_token` selects through `op_cache` in service-account-only mode. However, WCF's preview procedure requires a user-scoped token and the helper's documented register is account-owned. Before enactment, reconcile that exact use case with the helper owner. Keep WCF's existing capability requirement until proved compatible. No new universal permission set, token roll, provider call or policy-enforcement tool is proposed. The private guide is owned by chezmoi at `docs/guides/tools/cloudflare-tokens.md`; only its contract pointer belongs in reusable guidance.

### P3 - One report-retention rule - high

**Home:** `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md`, Pruning the work folder / Judgement; the retention phrase in Mechanical boundary; and the pruning sentence in Generated surfaces / `output-style`. Regenerate `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/output-styles/ki-coordinator.md` from that source in the same later delivery. K, Tidying the work folder, remains the authority and needs no rule change.

**Smallest wording:** For a five-file package, a report becomes eligible for the owning steward's tidy when its outcome has a durable home and each query has been copied in full into `queries.md`; copied queries need not already be answered. Keep the existing single-file tolerance rule, which waits for answers, and keep every report with an unhomed outcome.

**Why high:** K states both cases explicitly at lines 100-102. C's Judgement paragraph and the generated style currently carry the old answered-query condition into five-file packages. Replacing that condition and linking to K removes a contradiction without changing package shape, deletion authority or any open query. The FOLDER-2 scanner remains a conservative candidate list; its current answered-tag heuristic is not the retention rule and never authorises deletion. No scanner rewrite or deletion is needed for this prose repair. Verify the regenerated surfaces and the existing banner checks when enacting it.

## High-confidence enactment set

- **P1:** one conditional paragraph in D, Authority tiers, recording the existing non-interactive helper contract. No new credential authority.
- **P3:** align C's retention wording and generated output style with K's existing five-file rule; preserve the old-shape exception and conservative scanner.

P2 stays outside that set until its token-type compatibility is settled. Themes T01 and T03-T07 and T10-T14 add no method change. No new skill, state, package field, timer, ledger, acknowledgement mechanism or blanket audit is warranted by these lines.

## Queue source key

Each F number preserves the inventory order. Theme membership is exhaustive and exclusive: 68 lines across 14 themes, with no line removed from its source queue.

[F01]: <../../ki/messages.md#L3> "ki: REFRESH, first notice"
[F02]: <../../ki/messages.md#L5> "ki: REFRESH, handoffs and acceptance bundles"
[F03]: <../../ki/messages.md#L7> "ki: Roadmap Review and body order"
[F04]: <../../ki/messages.md#L9> "ki: HANDOFF-AS-MESSAGE"
[F05]: <../../ki/messages.md#L11> "ki: MARK-FOLLOWUP"
[F06]: <../../ki/messages.md#L15> "ki: WEBSITE-SKILL-SYNC"
[F07]: <../../ki/messages.md#L17> "ki: AUDIT-FINDINGS, this package"
[F08]: <../../ki/messages.md#L19> "ki: AUDIT-FINDINGS, unowned folder and authoring drift"
[F09]: <../../ki/messages.md#L23> "ki: MOD-LEDGER"
[F10]: <../../ki/messages.md#L29> "ki: WORK-STATUS-FORM"
[F11]: <../../ki/messages.md#L33> "ki: HNR method handoff"
[F12]: <../../ki/messages.md#L37> "ki: INITIATIVES-RESIDUE"
[F13]: <../../ki/messages.md#L39> "ki: CENTRAL-TICK"
[F14]: <../../ki/messages.md#L45> "ki: THEME-REGISTRY-ENFORCE"
[F15]: <../../ki/messages.md#L47> "ki: OP-CACHE-RULE"
[F16]: <../../ki/messages.md#L49> "ki: CF-UNIFORM"
[F17]: <../../ki/messages.md#L53> "ki: AUDIT-OUTSIDE-LANE"
[F18]: <../../ki/messages.md#L61> "ki: COORD2-RUBRIC"
[F19]: <../../ki.agent-host/messages.md#L3> "ki.agent-host: REFRESH"
[F20]: <../../ki.agent-host/messages.md#L7> "ki.agent-host: AUDIT-FINDINGS"
[F21]: <../../ki.agent-host/messages.md#L8> "ki.agent-host: AUDIT-OUTSIDE-LANE"
[F22]: <../../ki.agent-host/messages.md#L9> "ki.agent-host: DRAIN"
[F23]: <../../ki.baseline-rollout/messages.md#L3> "ki.baseline-rollout: REFRESH"
[F24]: <../../ki.baseline-rollout/messages.md#L4> "ki.baseline-rollout: FOLDER-CLOSED"
[F25]: <../../ki.baseline-rollout/messages.md#L5> "ki.baseline-rollout: AUDIT-FINDINGS"
[F26]: <../../ki.baseline-rollout/messages.md#L6> "ki.baseline-rollout: AUDIT-OUTSIDE-LANE"
[F27]: <../../ki.estate-factorisation/messages.md#L3> "ki.estate-factorisation: REFRESH"
[F28]: <../../ki.estate-factorisation/messages.md#L4> "ki.estate-factorisation: AUDIT-FINDINGS"
[F29]: <../../ki.estate-factorisation/messages.md#L5> "ki.estate-factorisation: AUDIT-OUTSIDE-LANE"
[F30]: <../../ki.knowledge-acquisition/messages.md#L3> "ki.knowledge-acquisition: AUDIT-FINDINGS"
[F31]: <../../ki.knowledge-acquisition/messages.md#L4> "ki.knowledge-acquisition: AUDIT-OUTSIDE-LANE"
[F32]: <../../ki.mac-studio-setup/messages.md#L3> "ki.mac-studio-setup: REFRESH"
[F33]: <../../ki.mac-studio-setup/messages.md#L5> "ki.mac-studio-setup: FOLDER-CLOSED"
[F34]: <../../ki.mac-studio-setup/messages.md#L6> "ki.mac-studio-setup: AUDIT-FINDINGS"
[F35]: <../../ki.mac-studio-setup/messages.md#L8> "ki.mac-studio-setup: AUDIT-OUTSIDE-LANE"
[F36]: <../../ki.observatory/messages.md#L4> "ki.observatory: SERVE-STALE-BINARY"
[F37]: <../../ki.observatory/messages.md#L5> "ki.observatory: SERVE-STALE-BINARY-CORRECTION"
[F38]: <../../ki.observatory/messages.md#L6> "ki.observatory: SERVE-WATCH"
[F39]: <../../ki.observatory/messages.md#L7> "ki.observatory: OPS003-DELIVERED"
[F40]: <../../ki.observatory/messages.md#L12> "ki.observatory: BRING-UP-LEFTOVER"
[F41]: <../../ki.observatory/messages.md#L14> "ki.observatory: VIS-SIZES"
[F42]: <../../ki.observatory/messages.md#L15> "ki.observatory: WORK-OPENER"
[F43]: <../../ki.observatory/messages.md#L16> "ki.observatory: AGENT-HOOKS-OBSERVATORY"
[F44]: <../../ki.paperclip-capture-and-rebuild/messages.md#L3> "ki.paperclip-capture-and-rebuild: REFRESH"
[F45]: <../../ki.paperclip-capture-and-rebuild/messages.md#L4> "ki.paperclip-capture-and-rebuild: AUDIT-FINDINGS"
[F46]: <../../ki.paperclip-capture-and-rebuild/messages.md#L5> "ki.paperclip-capture-and-rebuild: AUDIT-OUTSIDE-LANE"
[F47]: <../../ki.portable-specifications/messages.md#L3> "ki.portable-specifications: REFRESH"
[F48]: <../../ki.portable-specifications/messages.md#L4> "ki.portable-specifications: AUDIT-FINDINGS"
[F49]: <../../ki.portable-specifications/messages.md#L5> "ki.portable-specifications: AUDIT-OUTSIDE-LANE"
[F50]: <../../ki.regular/messages.md#L3> "ki.regular: FIRST-STEP"
[F51]: <../../ki.regular/messages.md#L4> "ki.regular: REFRESH"
[F52]: <../../ki.regular/messages.md#L5> "ki.regular: REFRESH-BANNER"
[F53]: <../../ki.regular/messages.md#L6> "ki.regular: AUDIT-FINDINGS"
[F54]: <../../ki.regular/messages.md#L7> "ki.regular: AUDIT-OUTSIDE-LANE"
[F55]: <../../ki.timelines/messages.md#L3> "ki.timelines: REFRESH"
[F56]: <../../ki.timelines/messages.md#L5> "ki.timelines: AUDIT-FINDINGS"
[F57]: <../../ki.timelines/messages.md#L6> "ki.timelines: AUDIT-OUTSIDE-LANE"
[F58]: <../../ki.tools-burndown/messages.md#L3> "ki.tools-burndown: TAKE-STOCK"
[F59]: <../../ki.tools-burndown/messages.md#L4> "ki.tools-burndown: CLI-DEPARTURES"
[F60]: <../../ki.tools-burndown/messages.md#L5> "ki.tools-burndown: CAPTURE-FOLLOWUPS"
[F61]: <../../ki.tools-burndown/messages.md#L6> "ki.tools-burndown: WORKTREE-FIXES"
[F62]: <../../ki.tools-burndown/messages.md#L7> "ki.tools-burndown: RIG-REMINDER-DOCTOR"
[F63]: <../../ki.tools-burndown/messages.md#L8> "ki.tools-burndown: BRING-UP-LEFTOVER"
[F64]: <../../ki.tools-burndown/messages.md#L10> "ki.tools-burndown: RIG-056-INTEGRATE"
[F65]: <../../ki.tools-burndown/messages.md#L15> "ki.tools-burndown: CLEAN-HOST-EVIDENCE"
[F66]: <../../ki.tools-burndown/messages.md#L16> "ki.tools-burndown: AUDIT-OUTSIDE-LANE"
[F67]: <../../ki.tools-burndown/messages.md#L17> "ki.tools-burndown: WORK-OPENER"
[F68]: <../../ki.tools-burndown/messages.md#L18> "ki.tools-burndown: HOOK-ROLLOUT"
