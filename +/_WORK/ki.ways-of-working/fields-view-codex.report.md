# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › fields-view-codex

**🤖 → 👤 Handoff to supervisor · Run report at 08:45 BST · last mark 08:40 BST**

---

## Done

Independent review completed against the [survey](/Users/krisbrown/.local/state/ki/agents/ways-of-working/field-survey.report.md), [owner decisions](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md), five cited standards and [change brief](/Users/krisbrown/.local/state/ki/agents/ways-of-working/_briefs/size-priority-2.md), including harness commit `d9cd8718`.

Source checks: complete; estate counts: not independently reproduced; tests/audits: not run for this semantic review; repository edits, commits and pushes: none.

## In Progress

Nothing is running in this review.

## Queries

### FIELDS-CORE - Keep the core, reduce duplicate authority

**Context:** Adjust. Identity, lifecycle, scheduling, dependencies and acceptance evidence are useful; mirrored dependencies and Project/theme classification add maintenance.

**Query:** Keep the core without adding more mandatory metadata?

**Options:**

a) (recommended, confidence medium - the model covers delivery, but duplicate relationships can drift) Keep purpose/component optional; derive theme from Project and eventually generate blocks from blocked_by. Keep agent assignment in run/work records. Put missing deadline consequences and selection rationale in Context, rather than adding mandatory assignee, due-date or score fields.

b) Keep the current authored relationships unchanged.

### FIELDS-PRIORITY - Define importance and selection order

**Context:** Agree with high/medium/low and absent-as-medium; [selection](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-next/references/standards-next-work.md:74) already ranks within horizons.

**Query:** Clarify meanings and prohibit automatic promotion?

**Options:**

a) (recommended, confidence high - importance cannot confer readiness or authority) High means material consequence from deferral; medium means useful planned progress; low means discretionary benefit. Check adoption, holds and dependencies first, then horizon, then priority. A high Future item prompts a promotion proposal, never jumps the queue automatically. Reconsider priority when consequences change; moving horizon alone need not change it.

b) Leave importance undefined.

### FIELDS-SIZE - Estimate the delivery, not a model's speed

**Context:** Adjust. Fixed durations in the [new definitions](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md:98) vary with model, tooling and parallelism.

**Query:** Use relative end-to-end effort instead?

**Options:**

a) (recommended, confidence high - elapsed time is unstable for agent work) s: one bounded patch; m: coordinated change; l: substantial coupled delivery; xl: needs decomposition. Include implementation, verification, integration and human review; exclude external waiting. Mark capture estimates provisional in Context and revisit before Ready. Size guides splitting and capacity, never importance or automatic dispatch; uncertainty warrants investigation, not an invented estimate.

b) Retain duration-based bands.

### FIELDS-GATES - Make enforcement consistent

**Context:** Adjust. The [checker](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/scripts/rubric/contexts/roadmap-evidence.ts:815) checks size vocabulary without an xl/Ready prohibition.

**Query:** Align deterministic checks across both adapters and tools-ki?

**Options:**

a) (recommended, confidence high - one record must not pass through a weaker entry point) Share conformance cases and severity rules; enforce xl before execution readiness. Warn then fail on missing size and adopted kind. Keep existing harness failures for retired horizons; explicitly document tools-ki's temporary warning bridge. Keep judgment checks distinct.

b) Keep separate validators without parity evidence.

### FIELDS-RETIRE - Remove aliases, preserve meaning

**Context:** Disagree with blanket retirement; agree with the landed exceptions in the [format](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-work-roadmap/references/standards-work-item-format.md:118).

**Query:** Confirm selective retirement?

**Options:**

a) (recommended, confidence high - semantic dependencies outweigh low usage) Retire initiative and purpose adoption. Keep resolution_target for replacement traceability, decide for decisions as outcomes, and optional task_links for qualified external-task identity. Do not force decisions into deliver or discard links because Paperclip is parked.

b) Retire all five and redesign dependent contracts first.

### FIELDS-MIGRATE - Prove completion before enforcement

**Context:** Adjust. The survey's 316 records differ from the earlier 367; an incomplete estate scan cannot establish zero gaps.

**Query:** Define the migration population and evidence?

**Options:**

a) (recommended, confidence medium - inventory coverage remains unverified) Reconcile a named repository/record inventory; unavailable repositories count as unknown. Owners judge size/kind, never blanket-fill m/deliver. Preserve implicit medium. Explicitly exempt historical terminal records from retrospective estimation; never resurrect pruned ones. Close the window only after a complete zero-gap scan and coordinated validator release, retaining migration evidence.

b) Keep the current unqualified estate-wide trigger.

### 🤖 → 👤 Handoff to supervisor · since 08:45 BST

👤 6 with you

- [with you] FIELDS-CORE, FIELDS-PRIORITY, FIELDS-SIZE, FIELDS-GATES, FIELDS-RETIRE, FIELDS-MIGRATE · owner · since 08:45 BST
