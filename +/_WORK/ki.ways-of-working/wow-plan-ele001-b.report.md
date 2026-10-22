# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 02:54 BST · last mark 02:12 BST**

---

## Done

Blind planning review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) against the `ki-work-roadmap` work-item format, the `ki-plan` readiness procedure, ki-design's AGENTS.md, [GDR-KI-DESIGN-012](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-012-shared-web-components.md), the elements package, and the site's build and [ADR-KI-WEBSITE-001](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/docs/decisions/ADR-KI-WEBSITE-001-vendoring-a-published-inventory.md). Read-only: no edits, no commits, no installs, no remote calls.

**Verdict: NOT READY.**

**Confidence: high.** The direction is sound, but the plan does not name its execution location, its consumption path, its full dependency set or a checkable go/no-go, and its Documentation impact misses ki-design's own decision that the spike tests.

`baseline_ref: null` is correct for a Ready record; it is set when work starts, so the preflight's "no baseline" is not a defect.

### Required plan changes

1. **Choose one execution location and record it in Files touched and Dependencies / blocks.** At present Files touched says "a spike branch or scratch page in the site", while Dependencies / blocks says "None". The roadmap standard requires work in another repository to be named in plain terms under Dependencies / blocks, and handed over as a `messages.md` line rather than written into that repository's roadmap. Recommended: a self-contained fixture in ki-design, for example `examples/ssr-spike/` beside `examples/site-preview/`. It would use the site's Eleventy version (`@11ty/eleventy` ^3.1.6) and its exact invocation (`bun node_modules/@11ty/eleventy/cmd.cjs --config=eleventy.config.ts`). The spike then needs no site change, which keeps its "no production change" boundary. If the site itself is used instead, name the site repository, a throwaway branch or worktree that never merges, and explicit authority for that repository.
2. **State how the page gets the elements.** `@knowledgeislands/elements` is private, exports TypeScript source (`./src/index.ts`), and depends on `workspace:*` packages. The site builds offline without ki-design and only vendors data through `sync:design` (ADR-KI-WEBSITE-001). Also, ki-design's AGENTS.md says consumers take a tagged release, and no release exists. Add a Step that bundles the elements into one self-contained ESM file, for example with `Bun.build`. The same file then serves both the server render and the browser hydration, and works under both runtimes. Say whether that bundle is committed or kept in the spike's temporary directory.
3. **Name every package, its version and how it is installed.** Name `@lit-labs/ssr`, `@lit-labs/eleventy-plugin-lit` and `@lit-labs/ssr-client`, each at a version compatible with the pinned `lit` 3.3.1. The record omits `@lit-labs/ssr-client`, whose `lit-element-hydrate-support` the hydration step cannot pass without. Name the registry install as an authorised network step. Isolate the install so that the root `bun.lock` and the workspace do not change: use the fixture's own `package.json` and lockfile, as `tooling/depcruise` does, or install only in temporary space.
4. **Give equal Steps to Bun and Node, with pinned runtimes and clear criteria.** The Goal says "or decide to build the site under Node", but no Step tries Node. Add a Step that runs the same fixture under Bun 1.4.2 and under Node v24 (the versions installed now). Record the exact command, the plugin's render mode (worker or vm; vm mode needs `--experimental-vm-modules`) and the result for each. Define the outcomes:
   - **Go:** Bun passes.
   - **Conditional go:** only Node passes.
   - **No-go:** neither passes, and the alternative is named. The likely candidate is a direct `@lit-labs/ssr` `render()` call from an Eleventy shortcode or transform, or a build-time pre-render beside `sync:design`. A missing package must count as setup failure, never as evidence against a runtime.
5. **Make Verify checkable.** Replace the prose with assertions:
   - The built HTML contains a `<template shadowrootmode="open">` for both `<ki-glyph>` and `<ki-hexmap>`.
   - The page reads with JavaScript disabled, as GDR-KI-DESIGN-012 requires.
   - The page hydrates in a local headless browser with no hydration-mismatch warnings in the console, and one interaction works after hydration, such as `<ki-hexmap>` keyboard focus.
   - `bun test` in `packages/elements` still passes. Name the browser tool, and confirm it runs against a local server with no network.
6. **Correct Documentation impact.** "The repository holds no specifications yet" is wrong. [`docs/spec/components.md`](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/components.md) line 14 and GDR-KI-DESIGN-012 line 20 already commit ki-design to server rendering with Declarative Shadow DOM. A no-go therefore needs a ki-design decision that revisits GDR-KI-DESIGN-012, plus a spec update, besides any Bun-or-Node Decision Record owned by the site. The site's Decision Record goes to the site's work as a `messages.md` line. Name the path for the go/no-go note, for example `docs/briefs/lit-ssr-spike.md`, or say that it lives in the record's Discussion.
7. **Reclassify and confirm the size.** The controlling outcome is a finding, so `kind: investigate` fits better than `deliver`. `size: m` holds for a ki-design fixture; a run across two repositories is `l` and needs a Delegation section.
8. **Readiness gate.** Under the 02:26 BST decision, Ready needs high-confidence agreement from all three reviewers (Codex xhigh, Opus 5.5 high, Fable 5.1 high) on the revised plan. This high-confidence NOT READY counts as one review. Rerun the three reviews after the changes above.

## In Progress

Nothing is running. [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) stays `draft`, unchanged.

## Queries

### [ELE001-WHERE - Where the spike runs](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md)

**Context:** The brief proposes running the spike across ki-design and apps-knowledgeislands.info. The site's build is offline and vendored, and the record's boundary forbids production change. A ki-design fixture that copies the site's Eleventy version and Bun invocation answers the runtime question without touching the site. Moving the real site build to Node remains a site decision either way.

**Query:** Should the replan place the spike in a ki-design fixture rather than in the site?

**Options:**

a) (recommended, confidence high - one repository, no site change, and the same runtime evidence) Replan with an isolated `examples/ssr-spike/` fixture in ki-design, authorise only its registry install, and hand any Node decision to the site's work as a `messages.md` line.

b) Replan to run in a throwaway site branch or worktree, granting explicit authority for the site repository, and resize the record to `l` with a Delegation section.
