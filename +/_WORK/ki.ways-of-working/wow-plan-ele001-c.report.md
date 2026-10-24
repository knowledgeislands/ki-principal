# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan-ele001-c

**🤖 → 👤 Handoff to supervisor · Run report at 02:57 BST · last mark 02:12 BST**

---

## Done

Verdict: **NOT READY**. Confidence: **high** - the record meets the Now/draft shape but fails the Ready gate on three of its four conditions: the Steps are not concrete enough to stop a wrong no-go, the dependencies are not satisfied (packages uninstalled, and no route by which the private elements package reaches the site's build), and the Verify is an assertion with no command and no observable hydration check.

Blind review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at ki-design HEAD `f603f56`, read only, against ki-design's `AGENTS.md`, the ki-work-roadmap work-item-format and repository-roadmap standards, the ki-plan readiness procedure, the preflight report, the site repository at `31d02de` and the 02:26 triage-and-draft grant. No file changed, no commit, no remote call.

What is sound: the Goal, Boundary and Documentation impact are honest; `size: m`, `horizon: now`, `status: draft` and the Now sections are present in the required order; running the spike across ki-design and apps-knowledgeislands.info is the right shape, because the site is the only Eleventy build and the question is a ki-design capability; installing from the registry and recording a Bun-or-Node decision are the right outputs. The site already pins Node LTS beside Bun in `mise.toml` and builds Eleventy with `bun node_modules/@11ty/eleventy/cmd.cjs`, so a Node comparison run is cheap and needs no toolchain change.

Required plan changes before Ready, in order of weight:

1. **Split the render path so a no-go is not inferred from the wrong thing.** `@lit-labs/ssr`'s in-process `render()` needs only the DOM shim; it is the Eleventy plugin `@lit-labs/eleventy-plugin-lit` that spawns a worker and loads modules through Node VM modules, which Bun lacks. Step 1 must become two steps, each run under Bun and under Node: a shortcode or transform calling `render()` directly, and the plugin. The go/no-go then reports a two-by-two result, and "Bun no-go" means the direct path failed under Bun, not merely the plugin.
2. **Decide how `@knowledgeislands/elements` reaches the site's build.** It is private, unpublished, exports TypeScript source with `.ts` specifiers, and depends on the `icons` and `hexmap` workspace packages. The site has no dependency on it; `sync:design` vendors build outputs only. The record must name the route for the spike (a `link:` or `file:` dev dependency to the local checkout on the spike branch is the least invasive) and state the single-`lit` constraint: the site's `lit` must resolve to the same copy as the elements' `lit` 3.3.1, or server render and hydration both break. Under Node the `.ts` specifiers rely on type stripping; say so, or point at a built entry.
3. **Name the packages, versions and install location, and give the run the authority.** The record names only `@lit-labs/ssr` and "the Eleventy plugin". Name `@lit-labs/ssr`, `@lit-labs/ssr-client` (the hydrate support the browser needs) and `@lit-labs/eleventy-plugin-lit`, pinned, as dev dependencies of `apps/site` in the site repository, with the `bun.lock` change that follows, as an explicit Step with its command. The standard run forbids remote calls, so the dispatching brief must carry a registry-install grant; the record cannot confer it.
4. **Make hydration observable and make Verify a command.** Add to the test page the `lit-element-hydrate-support` import before the element bundle. Verify should assert that the built HTML contains `<template shadowrootmode="open">` and Lit part markers for both elements, then, in a real browser (Declarative Shadow DOM is not in happy-dom), that both elements are defined and adopted their server-rendered shadow root without a second render. Name the browser check tool. Keep the existing wording as the pass condition.
5. **Make Files touched concrete in both repositories, and keep the site's gates clean.** Site: a named spike page under `apps/site/src/`, `apps/site/eleventy.config.ts`, `apps/site/package.json`, `bun.lock`, on a named spike branch, never merged to `main`, never deployed; say whether the branch is kept or deleted after the note is written. The spike page must be excluded from `verify:reachable`, `verify:prose` and `verify:routes`, or built with a separate config, or `ki:site:build` fails. ki-design: name the note's path.
6. **Give the decision a home for both outcomes and frame it precisely.** Documentation impact names a Decision Record only for a no-go. A go is also a decision ki-design's charter records (one decision, one record in `docs/decisions/`): the elements render server-side under Bun. For a no-go, the site owns the DR to move the Eleventy process to Node, and ki-design records the alternative and opens the site-side record in its Roadmap impact. Frame the decision as which runtime runs the Eleventy process and the server render, not the site's whole toolchain: the `verify:*` scripts and the commit gate stay Bun either way.
7. **Classification and Boundary.** The controlling outcome is a finding, so `kind: investigate` fits better than `deliver`; `purpose: learning` likewise. Boundary should add: no change to `sync:design`, no production page, no deploy, no change to the site's `main`, and no interference with the site's KI-WEBSITE-SITE-044 review state.
8. **Dependencies / blocks narrative.** `blocked_by: []` is right, there is no missing build order, but the narrative "None" should name the site baseline commit the spike branches from and the local ki-design checkout it links.

Readiness check: NOT READY, as above. Convention check: PASS on frontmatter and section order; FAIL on Ready-gate concreteness. Repository-integrity check: PASS, working tree untouched. Approval path: the 02:26 grant stands in for ki-plan's user approval only when three strongest-model reviews agree with high confidence; this is one such review.

## In Progress

Nothing. The record stays `draft`; no transition, edit or commit was made in either repository.

## Queries

None.
