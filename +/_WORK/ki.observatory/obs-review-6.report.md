# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-review-6

**🤖 → 👤 Handoff to supervisor · Run report at 01:37 BST · last mark 22:50 BST**

---

## Done

Recommend original option b): capture a triage record to harden label sanitising before a handler can become active in the frame, retaining the existing content policy and final-output checks.

Confidence: medium - earlier prevention would strengthen containment, but this review establishes neither a policy bypass nor the precise transient insertion responsible.

Containment review: the frame permits only the two named scripts and forbids inline handlers; the smoke check allows the resulting `script-src-attr` refusal while still rejecting retained handlers, `javascript:` addresses, title changes and other script refusals. This supports the existing smoke-check allowance and does not make the follow-up a blocker.

Sanitising review: Mermaid already sanitises labels and sanitises the returned SVG in strict mode; the bootstrap then inserts that SVG. A follow-up must investigate the intermediate rendering path rather than merely add another final-output filter. See [bootstrap](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/mermaid.ts:71), [frame policy](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/server.ts:296) and [hostile-label checks](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/apps/site/src/browser.smoke.ts:896).

Factual contradictions: none found in the supplied containment account. The current code alone does not identify exactly where the transient handler originates; its precise lifetime was not independently reproduced.

Verification: source review only; no browser or test run, repository changes, triage record or commits.

## In Progress

Nothing running.

## Queries

No outstanding queries. The recommendation is returned for disposition under the read-only brief.
