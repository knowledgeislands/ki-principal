# [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) › wow-gov202-blind

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 04:05 GMT**

---

## Done

Completed one blind, read-only review of GOV-202 and its existing generator, diagram, schema and renderer sources; prohibited reports, principal queries/decisions and other reviews were not read.

No repository changes, commits, tests, builds, audits, remote calls or subagents; source inspection only, with no live rendered verification.

## In Progress

Nothing is running. The supervisor holds the delivery-route decision; this review selects and implements nothing.

## Findings

### GOV202-AUTH - A supported presentation exists, but delivery is not yet authorised

**Goal:** Stable stats on each skill-area diagram component.

**Scope:** GOV-202's existing viewer configuration and explicit viewer boundary.

**As of:** 04:05 GMT, 27 October 2026.

No fully authorised implementation route exists today: the [record](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md:34) expressly remains draft after adoption, requires a supported presentation and Ready plan, and forbids viewer implementation changes. Inspection and planning within existing configuration are already permitted; adoption is not delivery authority.

A configuration-only route is technically supported: the [component schema](/Users/krisbrown/.agents/skills/archify/schemas/architecture.schema.json:84) accepts independent `sublabel`, `tag` and `sources`; the [renderer](/Users/krisbrown/.agents/skills/archify/renderers/architecture/render-architecture.mjs:1087) draws the sublabel and tag separately and carries both into node passport metadata. The [generator](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-harness/scripts/rubric/contexts/skill-areas.ts:285) currently emits the concern/trigger sublabel and source path, without a stats tag. The [existing diagram source](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/diagrams/skill-area-acquire.architecture.json) confirms that structure. A tag can therefore carry compact stats without discarding either existing field. It is fine-detail content, so visibility and fit still require the eventual rendered verification; no always-visible badge or custom exact-stat detail panel is proven here.

The unresolved choice is contractual: the [goal](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md:21) says “in place of” the source badge, while the current record says literal SRC is absent and source links must survive. Adding a stats tag is a useful alternative presentation, not evidence of supported source-affordance replacement. Local symlinked delivery removes no boundary and supplies no missing approval; no release cycle is needed merely to choose the configuration route.

## Queries

### GOV202-ROUTE - Presentation decision for the supervisor to take to the owner

**Context:** Existing configuration can show stats while retaining both the concern/trigger sublabel and source metadata. Literal replacement of the viewer's source affordance is not demonstrated by those fields, and viewer changes are explicitly excluded. Implementation still needs a Ready plan under every option.

**Query:** Which presentation contract should the supervisor seek approval to plan?

**Options:**

a) (recommended, confidence high - the existing schema and renderer directly support a separate tag, preserving the current sublabel and source metadata with the smallest change) Accept a compact per-skill stats tag as satisfying the useful outcome, retaining source evidence and concern/trigger text; plan generator/data and diagram changes within existing viewer configuration. Confirm fit once in delivery verification, without adding a release process.

b) Authorise replacing the concern/trigger sublabel with stats, retaining source metadata; this uses existing configuration but deliberately gives up the present visible concern/trigger information and changes its presentation contract.

c) Retain literal replacement of the source badge as the requirement and explicitly widen the viewer boundary before planning a minimal viewer change. Local delivery may remain local; neither the exact viewer patch nor its supported integration route is established by this review.
