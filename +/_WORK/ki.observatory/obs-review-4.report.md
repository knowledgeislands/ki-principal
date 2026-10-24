# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-review-4

**🤖 → 👤 Handoff to supervisor · Run report at 00:39 BST · last mark 22:50 BST**

---

## Done

Recommend **option a, with amendments** for [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md). **Confidence medium - incremental convergence preserves working capabilities, but the code does not establish that splitting Work improves the experience.** Keep ten instruments as a direction, retain the optional lens, and review the navigation after three approved changes without promising a job switch. Council first is reasonable as a bounded starting point; each later move still needs its own demonstration and approval.

Change a)'s Work commitment: retain Work and its present Attend/Observe mapping until the Streams proposal demonstrates where all five views, reports, feedback and Beacon destinations will live. Decide DESIGN-WORK then. The [Streams record](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md:41) already allows Roadmap alone to move if Work retains its tab. Neither a permanent separate Work tab nor its absorption needs deciding now.

Context correction: Waiting for you need not wait on DESIGN-WORK if this step only renames the Review queue. The queue already derives its handoff rows directly from Work's with-you view ([evidence](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/evidence/src/review.ts:311)). It links those rows and report queries into Work ([navigation](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/packages/instruments/src/review.ts:109)); Work supplies state, holder, report reading and feedback. Those links show that the two screens are not interchangeable. Moving or retiring Work requires the later decision; renaming Review does not. Council's pure rename and the unknown-view fallback are consistent with the code.

Keep the shared redirect table in the instrument package, read by resolveInstrument, but explicitly adapt every consumer. The [shell](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/shell.ts:142) currently reads raw IDs, including on history navigation, and does not call resolveInstrument. The [CLI](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/main.ts:56) rejects a supplied ID whenever resolution changes it. Adding table rows alone therefore leaves aliases broken. Preserve unknown-ID rejection in the CLI, canonicalise known aliases in the shell, and verify old complete addresses, filters, report parameters and Beacon destinations as each consolidation lands. Also correct the record's renderer name to [renderShell](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/page.ts:294).

Change a)'s automatic Ready transition: record the owner's approval first and reconcile the record's promotion condition with its gated first step. Its [Shaping section](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md:60) explicitly requires step 3 to have shipped before promotion. Retain Draft under that condition; allowing Ready earlier requires an explicit amendment. Neither rename's own go follows from approving the restructure direction.

Read-only review and exact source checks completed; the local resolver check passed for all sixteen current instruments and confirmed unknown IDs resolve to Beacon. No repository file changed, no commit created and no remote call made. The full application test suite was not run.

## In Progress

Nothing is running. Outstanding - no action requested now: implementation remains with the Observatory coordinator, behind step 3 and each change's separate approval; DESIGN-WORK remains deferred to the Streams proposal.

## Queries

### [RESTRUCTURE - adopt bounded convergence](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md)

**Context:** The existing lens already reaches every tab. Both initial renames can preserve today's capabilities without settling Work's final home; later mergers still need evidence from the reskinned app.

**Query:** Which restructure direction should the coordinator record?

**Options:**

a) (recommended, confidence medium - preserves the accepted incremental approach while leaving the unproven Work split open) Adopt option a with Work deferred, Waiting for you limited to the Review rename, explicit shell and CLI alias handling, and the current step-3 promotion gate retained. Review the lens after three approved changes; authorise neither rename yet.

b) Adopt option b, keeping Work permanently separate and putting the Review rename first.

c) Adopt option c, committing to ten instruments and replacing the lens now.

d) Adopt option d, stopping convergence after the two renames.

### 🤖 → 👤 Handoff to supervisor · since 00:39 BST

🤖 0 running · 👤 1 with you

- [with you] RESTRUCTURE recommendation · supervisor · since 00:39 BST
