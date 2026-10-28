# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-area-column

**🤖 → 👤 Handoff to supervisor · Run report at 04:10 GMT · last mark 01:07 GMT**

---

## Done

Read-only review completed; no repository edits or commits, and no remote calls.

Source inspection: confirmed the concern-grouped catalogue, inline HTML finder, two-source sync and pinned harness publication generator.

Snapshot checks: passed — 64 matching skill names, 8 concerns, 10 areas, every skill assigned, and matching pin; three skills serve multiple areas.

Executable parser check: unavailable because local `json5` could not resolve; no dependencies installed. Independent snapshot checks passed; no build or gates run.

## In Progress

Nothing running.

## Findings

### AREA-PUBLICATION - Publish the area finder upstream

**Goal:** Answer the owner's 25 October 2026 question: how should the website show which functional areas each skill belongs to?

**Scope:** Website [catalogue](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/apps/site/src/docs/skills/catalogue.md:21), [sync parser](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/apps/site/scripts/sync-skill-catalogue.ts:252), snapshot, and harness generator and README at revision `8897008f`; no implementation or visual review.

**As of:** 25 October 2026, 04:10 GMT.

**Recommendation: ask the harness to publish the functional-area table in its generated README block, then sync the emitted Markdown. Confidence: high.**

**One-line reason:** A published upstream table gives the website a stable consumption boundary instead of coupling it to generator implementation details.

Keep the catalogue grouped by source concern and add a supplementary finder with skill, source concern and every functional area. Generate it from the existing area table, preserving multiple memberships and useful capability-group labels. Consume completed Markdown rather than reconstructing rows through a Nunjucks loop.

The pinned [area module](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-harness/scripts/rubric/contexts/skill-functions.ts:1) calls areas a diagram reading aid rather than published skill metadata. The website currently promotes that internal table into a public catalogue field. Its parser depends on an exact TypeScript declaration and literal array, so an upstream refactor can break sync without changing membership. The harness [publication function](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-harness/scripts/rubric/contexts/capability-publication.ts:140) is the appropriate place to make this reading aid an explicit published projection.

**Risk the inline HTML option avoids:** It avoids waiting on upstream work and expanding the harness's public publication contract. The existing same-revision sync and membership checks already reduce drift risk; HTML itself is not the objection. The recommendation needs a coordinated generator, parser and rendering change, and a new pin containing the table.

Queries raised: none; this is advice, not implementation approval.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 04:10 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] AREA-PUBLICATION recommendation · supervisor · since 04:10 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
