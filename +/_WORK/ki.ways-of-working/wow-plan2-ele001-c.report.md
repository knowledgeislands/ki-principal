# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan2-ele001-c

**🤖 → 👤 Handoff to supervisor · Run report at 03:01 BST · last mark 02:12 BST**

---

## Done

Blind re-review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) against the three earlier reviews, the replan report, ki-design's AGENTS.md, the `ki-work-roadmap` item format and the `ki-plan` readiness procedure. Read-only: no edits, no commits, no installs, no remote calls.

**Verdict: NOT READY.**

**Confidence: high.** The record was never amended: the replan run blocked on missing version pins and changed nothing, so the file on disk is byte-identical to HEAD, carries `updated_at: 2026-10-20T22:22:00Z`, and is the same draft all three earlier reviews rejected.

Record-state check: FAIL on the premise. `git diff HEAD` on the record is empty, the working tree is clean, and the last commit touching it predates the reviews. The replan report (`wow-replan-ele001`) states "The record is unchanged" and ends blocked on query ELE001-PINS.

Readiness check against `ki-plan` step 2 (confirmed boundary, understood dependencies, checkable verification): FAIL. Dependencies / blocks still reads "None"; Verify is still prose with no command, fixture, assertion or browser tool; Steps still have one Bun-only render step and no Node step despite the Goal's Bun-or-Node decision.

Convention check against `ki-work-roadmap`: PASS on frontmatter and section order; FAIL on Ready-gate concreteness, as before.

Earlier reviews' required changes, all still outstanding because none were applied:

1. Execution location: Files touched says "a spike branch or scratch page in the site" while Dependencies / blocks says "None". Either a self-contained `examples/ssr-spike/` fixture in ki-design, or a named throwaway site branch with explicit site authority, size `l` and a Delegation section. Not done.
2. Consumption path for private, unpublished `@knowledgeislands/elements` (TypeScript source exports, `workspace:*` dependencies, single `lit` 3.3.1 copy): a bundle step or a `link:`/`file:` route, with the build entry named. Not done.
3. Full dependency set with pinned versions and an isolated install: `@lit-labs/ssr`, `@lit-labs/ssr-client` and `@lit-labs/eleventy-plugin-lit`, compatible with `lit` 3.3.1, installed without touching the root `bun.lock`; the registry install named as an authorised network step in the dispatching brief. Not done, and the pins are still unestablished (the replan's open query).
4. Split render paths and equal Bun and Node steps: direct `render()` from a shortcode or transform, and the Eleventy plugin, each under Bun 1.4.2 and Node v24, with the plugin render mode and any `--experimental-vm-modules` flag recorded, and a go / conditional go / no-go table where a missing package counts as setup failure, never as runtime evidence. Not done.
5. Checkable Verify: built HTML contains `<template shadowrootmode="open">` for both elements; page reads with JavaScript disabled; hydration in a named local headless browser with no mismatch warnings and one post-hydration interaction; `bun test` in `packages/elements` still passes. Not done.
6. Documentation impact: "the repository holds no specifications yet" is wrong; `docs/spec/components.md` and GDR-KI-DESIGN-012 already commit to Declarative Shadow DOM, so a no-go also needs a ki-design decision and spec update, and the site's Bun-or-Node Decision Record is handed over as a `messages.md` line. Name the path of the go/no-go note. Not done.
7. Classification and boundary: `kind: investigate` (and arguably `purpose: learning`); Boundary to add no change to `sync:design`, no production page, no deploy, no change to the site's `main`, and no interference with KI-WEBSITE-SITE-044. Not done.
8. Dependencies / blocks narrative to name the site baseline commit, the spike branch and the local ki-design checkout. Not done.
9. Readiness gate: Ready needs high-confidence agreement from all three reviewers on a revised plan; this review is one high-confidence NOT READY on an unrevised plan.

On tonight's intended run: the record cannot move to Ready, and a cross-repository run installing registry packages is not authorised by anything in the record. The blocking step is the replan's open query ELE001-PINS: supply the three version pins, or grant a successor run read-only registry metadata access, then rerun the replan and the three reviews.

## In Progress

Nothing running. [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) stays `draft`, unchanged.

## Queries

### [ELE001-UNAMENDED - The record under re-review was never amended](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md)

**Context:** This re-review was briefed as judging a "just amended" record, but the replan run stopped blocked on ELE001-PINS without writing anything, and the record is identical to HEAD. Every required change from the three earlier reviews is still open. Re-reviewing again before a replan lands will produce the same verdict.

**Query:** How should the replan be unblocked so a real revision exists to re-review?

**Options:**

a) (recommended, confidence high - clears the only stated blocker within the offline boundary and lets the replan and three reviews run in sequence tonight) Answer ELE001-PINS by supplying the three compatible version pins for `@lit-labs/ssr`, `@lit-labs/ssr-client` and `@lit-labs/eleventy-plugin-lit`, relaunch the replan with the ki-design fixture placement from review b's recommended option, then relaunch the three blind reviews on the amended record.

b) Grant the replan successor read-only registry metadata access to choose and document the pins itself, with no installation, then proceed as in a).

c) Replan without pins, recording the install as an execution step that resolves the latest versions compatible with `lit` 3.3.1 and writes them into the record at In progress; accept that the reviews will likely still require pins.
