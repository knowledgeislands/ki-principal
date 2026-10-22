# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan2-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 03:00 BST · last mark 02:12 BST**

---

## Done

Verdict: **NOT READY** for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md).

Confidence: **high** - the record has not been amended: it is byte-for-byte the plan the three earlier reviews rejected (`updated_at` 2026-10-20T22:22Z, last commit `bfb6a45`, the same in every ki-design worktree), because [wow-replan-ele001](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-replan-ele001.report.md) stopped blocked on package pins and changed nothing.

Amendment check: FAIL - none of the required changes from reviews [a](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-a.report.md), [b](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-b.report.md) and [c](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-c.report.md) is present.

Repository-integrity check: PASS - ki-design clean at `f603f56`; no file changed, no commit, no remote call.

Required changes before Ready, merged from the three reviews and all still outstanding:

1. Execution location and Boundary: run across ki-design and apps-knowledgeislands.info on a named, never-merged, never-deployed site spike branch from a named site baseline; name every touched path in both repositories (spike page, `apps/site/eleventy.config.ts` or a separate spike config, `apps/site/package.json`, `bun.lock`, browser entry); keep the spike page out of `verify:reachable`, `verify:prose` and `verify:routes`; no change to `sync:design`, production pages, deploy or site `main`; size `l` with a Delegation section.
2. Elements route: state how the private, TypeScript-source `@knowledgeislands/elements` (with `workspace:*` dependencies) reaches the site build without publishing - a self-contained `Bun.build` ESM bundle or a `link:`/`file:` dev dependency - and the single-`lit` 3.3.1 constraint.
3. Dependencies: name `@lit-labs/ssr`, `@lit-labs/ssr-client` and `@lit-labs/eleventy-plugin-lit`, the install command and workspace, the registry install as an authorised step, and the resolved versions to record; replace Dependencies / blocks "None" with the site baseline and the linked local ki-design checkout.
4. Decision procedure: split the direct `render()` path from the Eleventy plugin path, each under Bun and Node v24 (plugin render mode and `--experimental-vm-modules` recorded), giving a two-by-two result; define go, conditional go (Node only) and no-go with the named alternative; a setup or missing-package failure is never runtime evidence; frame the decision as the runtime of the Eleventy process and server render only.
5. Verify as commands: built HTML holds `<template shadowrootmode="open">` and Lit part markers for both elements; the page reads without JavaScript; in a named local headless browser, `lit-element-hydrate-support` loads first, both elements hydrate with no mismatch warnings and one post-hydration interaction works (hexmap keyboard focus or glyph update); `bun test` in `packages/elements` and the site's gates still pass.
6. Documentation impact: correct "no specifications" - [components.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/components.md) and [GDR-KI-DESIGN-012](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-012-shared-web-components.md) already commit to Declarative Shadow DOM, so a no-go revisits both; record a go as a ki-design decision too; name the note path; send the site-owned Bun-or-Node Decision Record to the site as a `messages.md` line.
7. Classification: `kind: investigate`, `purpose: learning`.

Readiness gate: this is one high-confidence NOT READY; the consensus route needs a completed replan and a fresh round of three reviews.

## In Progress

Nothing running. The record stays `draft`; the supervisor owns the unblocked replan.

## Queries

### [ELE001-PINS - Unblock the replan without pre-known pins](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md)

**Context:** The replan stopped because no reviewer supplied exact versions and it could not reach the registry. None of the three reviews needs versions known before execution: they ask that the packages be named, installed from the registry by an authorised step, and their resolved versions recorded. The lockfile pins them at install time, and the record can require versions compatible with `lit` 3.3.1 as a pass condition.

**Query:** Should the successor replan write the dependency step as "install the current releases compatible with `lit` 3.3.1 and record the resolved versions from `bun.lock`", instead of waiting for pins?

**Options:**

a) (recommended, confidence high - meets all three reviews' dependency requirement with no remote call during planning) Relaunch the replan with that wording and the other six changes above, then rerun the three reviews.

b) Grant the replan read-only registry metadata access to fix exact pins first, then rerun the three reviews.

### 🤖 → 👤 Handoff to supervisor · since 03:00 BST

🤖 0 running · 👤 0 you · ⛔ 0 blocked

- [handoff] Re-review verdict for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md): NOT READY, record unamended · supervisor · since 03:00 BST
