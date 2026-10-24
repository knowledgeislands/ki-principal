VERDICT: NOT READY · confidence high · the no-go branch cannot be reached inside this spike, and the GDR-KI-DESIGN-012 amendment scope omits content its own Verify check forbids

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan7-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 09:27 BST · last mark 08:24 BST**

---

## Done

- I reviewed [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) blind, as committed at `2db3f385`. I made no commits and wrote nothing in any repository.
- Ready preflight: the `ki-work` audit passes, and the `ki-work-roadmap` audit passes with no warning.
- Decision and guide audits: these fail before any delivery edit. Decision Records has 116 failures; GDR-KI-DESIGN-012 itself has FILENAME-1 and two BODY-11 findings. Guides has 1 failure (ROUTE-1 on `docs/spec`). The plan's baseline-and-no-new-finding gate handles all of these.
- Repository facts and pins all check out:
  - Both checkouts: the site is at `31d02de` on `main`, clean, with no `+/_WORK/`. The Eleventy production input is `src`, and the `verify:*` scripts read only `src/` and `dist/`. The site's `tsconfig.json` includes `**/*.mjs` with `allowJs` and no `checkJs`.
  - Fixture install: `tooling/depcruise` already uses a nested standalone `bun.lock`, which is a precedent for installing the fixture in isolation.
  - Elements: the elements package works as described (`src` attribute, no slot, `role="option"`, roving tabindex, `ki-select`, Enter and Space). Its isolated-linker workspace links resolve from `packages/elements`.
  - Runtimes: Bun is 1.4.2, and `mise exec node@24.22.0` gives Node 24.22.0. Eleventy 3.1.6 is installed, and no Lit Labs package is installed in the site.
  - Browser: local Chrome is 155.0.8059.85. The cached `playwright-core` 1.64.1 declares Node `>=20` and targets Chromium 156.0.8078.4. The only other cached version, 1.63.0, targets Chromium 153, so any repin would need registry metadata under the install grant, which the plan already allows.
- Not checked: the registry-only pins (`@lit-labs/ssr`, `@lit-labs/ssr-client`, `@lit-labs/eleventy-plugin-lit`, `@types/node` 24.10.0) are not in the offline cache, so I could not confirm them without a network call.

### Required change 1: the no-go outcome cannot be reached

The decision procedure says no-go needs "an evidenced alternative" and that "an untested alternative … stays blocked". In the same sentence it puts evaluation of those alternatives in "separately approved work". So a fully diagnosed failure of all four cells can only end blocked. The no-go deliverables in Documentation impact, and the supervisor's no-go review step, can never apply, which leaves an investigation unable to close on its most negative finding.

- **Verify, Decision procedure.** Replace:

  > **No-go** requires completed, diagnosed failures of both paths under both runtimes and an evidenced alternative; evaluate build-time pre-rendering beside `sync:design` or a changed component lifecycle in separately approved work. An untested alternative, unresolved setup problem or inconclusive result stays blocked rather than being declared completed no-go.

  with:

  > **No-go** means completed, diagnosed failures of both paths under both runtimes, each attributed to a runtime or component-lifecycle cause rather than to setup. It records the diagnosed limitation and proposes, in the run report's Queries, separately approved work to evaluate build-time pre-rendering beside `sync:design` or a changed component lifecycle; this spike evaluates neither, and the no-go finding does not wait for them. An unresolved setup problem, undiagnosed failure or inconclusive result stays blocked rather than being declared completed no-go.

- **Delegation, final paragraph.** Replace "For a completed no-go, independently reproduce the diagnosed failures and check the evidenced alternative instead;" with "For a completed no-go, independently reproduce the diagnosed failures and check each diagnosis instead;".
- **Documentation impact, Roadmap.** Replace "no-go identifies the tested limitation and alternative work" with "no-go identifies the diagnosed limitation and proposes the alternative work".

### Required change 2: the GDR-KI-DESIGN-012 amendment leaves forbidden content in place

Verify requires the delivered record to contain no TODO and no relative link outside sibling Decision Records. GDR-KI-DESIGN-012 currently has two such things:

- The Consequences line "The exception to PDR-002 is to be recorded in a later Observatory decision record, not yet written", which is forward work.
- Two References links, to `../spec/components.md` and `../../packages/elements/README.md`, which are the existing BODY-11 findings.

Documentation impact authorises replacing only the pending-spike line, so the worker must either exceed the stated edit or fail its own check.

- **Documentation impact, Decision Records, first paragraph.** After "…or canonical external sources.", insert:

  > The same edit brings the rest of the record to that standard without changing its settled meaning: restate the Consequences line saying the exception to PDR-KI-OBSERVA-002 "is to be recorded in a later Observatory decision record, not yet written" as a present-state fact with no forward-work wording, and replace the References links to `docs/spec/components.md` and `packages/elements/README.md` with prose names, omitting `## References` if nothing remains. Route the Observatory's need for that decision only through the run report's Queries.

Once both edits are in, I'd expect READY. Everything else meets `ki-plan`, `ki-work-roadmap`, `ki-decision-records` and `ki-guides`: Goal, scope, Steps, Verify, Delegation, guide scope and the browser setup check.

## In Progress

Nothing.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 09:27 BST

👤 1 with you

- [with you] KI-DESIGN-ELE-001 planning review b: NOT READY, two required edits · supervisor · since 09:27 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
