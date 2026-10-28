# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-docs-work-c

**🤖 → 👤 Handoff to supervisor · Run report at 05:37 GMT · last mark 05:37 GMT**

## Done

- Published two interim Ways of working pages, each with one Interim callout under its opening claim, the five sections, a Provided by box and a provenance footer: `https://knowledgeislands.info/docs/ways-of-working/findings/` (order 9) and `https://knowledgeislands.info/docs/ways-of-working/tending/` (order 10). Deploy completes after the push.
- Drew three site-owned diagrams with manifest entries, README sections, committed HTML and receipts, traced to the two design notes at ki-principal `f3297dcb`: `https://knowledgeislands.info/diagrams/site/finding-life.html`, `https://knowledgeislands.info/diagrams/site/tending-tracks.html`, `https://knowledgeislands.info/diagrams/site/tending-pass.html`.
- Set `page` on the `findings` and `tending` feature areas; both keep `interim: true`.
- Site build, site tests and typecheck passed; audits ki-repo-website-content, ki-authoring and ki-diagrams passed; ki-engineering failed only on the pre-existing DEPS-1 baseline (`@types/node`, `rumdl`, Bun) with the CI-1 warning, as the plan's Gate baseline allows.
- Committed `de1b44e` `docs(site): publish findings and tending as interim practices` by explicit path, 17 files, and pushed it fast-forward to `origin/main`; the remote reported its usual bypassed branch rules. The one other uncommitted file, `apps/site/scripts/verify-diagrams.test.ts`, is not this unit's and was left untouched.

## In Progress

- None; Cloudflare deploys `de1b44e` from the push.

## Queries

### WOW-C-1 - Form of the Interim callout

- Context: the brief set no form for the callout. Both pages use a blockquote, `> **Interim.** This practice is in use, and its standard home is not yet chosen.`, which the gates accept and the layout styles. Query: keep the blockquote, or add a dedicated callout partial for interim pages?
- Options: keep the blockquote (recommended, high confidence: no new template, consistent across both pages, easily removed when a home is chosen); add a callout shortcode and restyle, a design change outside this unit.

### WOW-C-2 - Tending's second source

- Context: the tending page cites the harness `ki-repo` REVIEW procedure as a second source because structural level 3 reads its lenses; the design note is the first. Query: keep that second source, or cite the design note alone until a standard home exists?
- Options: keep it (recommended, medium confidence: the page names the lenses and a reader can trace them); drop it.

```text
Received wow-docs-work-c: findings and tending published at de1b44e. WOW-C-1 keep the blockquote. WOW-C-2 keep the second source.
```
