# Model › [KI > Model > Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md) › obs-lane-sweep

**🤖 → 👤 Handoff to supervisor · Run report at 00:01 BST**

---

## Done

- Triage sweep (steps 1–2): the lane has no records in triage. All ten [ki-design](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/) records already have a horizon (7 Now, 2 Next, 1 Hold). The website's one design-adoption record, [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md), is In progress. Every `apps-observatory.local` record also has a horizon, following `dff8890`. Nothing was adopted, so nothing new moved to Now for delivery.
- Acceptance sweep (step 3): no record in the lane or in `apps-observatory.local` is Awaiting review. The two queries below cover what is close.
- No repository was changed, so no commit or audit was needed. Nothing was pushed.

## In Progress

Nothing.

## Queries

### LANE-TRIAGE

**Context:** The lane has no triage records. Five ki-design Now records ([KI-DESIGN-ICO-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/85a42bf13ddd7396ae28b83bc645c0767d06454d/docs/roadmap/KI-DESIGN-ICO-001-icon-seed-set.md), [KI-DESIGN-MAP-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-MAP-001-hexmap-v0.md), [KI-DESIGN-SYM-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-SYM-001-symbol-library-data.md), [KI-DESIGN-TIL-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-TIL-001-tile-set-contract.md) and [KI-DESIGN-TOK-001 (pruned)](https://github.com/knowledgeislands/ki-design/blob/e1d20b6b96770c35ac1c1c3186c672fb710aa969/docs/roadmap/KI-DESIGN-TOK-001-tokens-v0.md)) shipped v0 in `04b2761`. Each now has only one or two confirming tests or checks left. Two other Now records have not been started: [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md), the licence decision, and [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md), the Lit SSR spike.

**Query:** Should the five nearly finished ki-design Now records go to delivery as one batch?

**Options:** a) (recommended, confidence high - each needs only small checks against code that has already shipped) the coordinator launches one `ki-plan` then `ki-implement` run over the five; b) leave them for the design thread to schedule; c) hold them until the Observatory design convergence settles.

### LANE-ACCEPT

**Context:** [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) still says In progress and says its work is uncommitted on `feat/design-v1`. In fact the work is on `main` in `5370af7` and `bc6dbdf`, that branch is fully merged, and later commits build on it. Only the step "commit the ledger advance, then this change" is left unticked, and that commit has already been made. Separately, in `apps-observatory.local`, [KI-OBSERVA-VIS-033 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/94f1db12709fc7db2d3c5e9d04f7cec91d5a0886/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) is Cancelled, as approved under TRIAGE-MERGE, and can now be pruned. There are no ideas to home in a Project note.

**Query:** How should [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) be closed, and should [KI-OBSERVA-VIS-033 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/94f1db12709fc7db2d3c5e9d04f7cec91d5a0886/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) be pruned?

**Options:** a) (recommended, confidence high - the delivery is on `main` and the record is simply out of date) one short run brings [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md)'s record up to date and moves it to Awaiting review, then you accept it; prune [KI-OBSERVA-VIS-033 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/94f1db12709fc7db2d3c5e9d04f7cec91d5a0886/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) in the same pass; b) accept [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) directly and correct its record during acceptance; c) return [KI-WEBSITE-SITE-044 (pruned)](https://github.com/knowledgeislands/apps-knowledgeislands.info/blob/ae886e2b/docs/roadmap/KI-WEBSITE-SITE-044-design-v1.md) so its steps can be checked again against the current site.
