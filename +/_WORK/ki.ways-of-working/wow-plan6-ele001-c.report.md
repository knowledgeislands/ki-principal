# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan6-ele001-c

VERDICT: NOT READY · confidence medium · facts, pins and preflight all check out; two small Documentation impact edits are needed first (guide scope under ki-guides, Decision Record date on amendment)

**🤖 → 👤 Handoff to supervisor · Run report at 09:11 BST · last mark 08:24 BST**

---

## Done

- Reviewed [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at `732aa10f` blind: no other reviewer report or earlier round was opened.
- Section order and content match the `ki-work-roadmap` format: Goal, Context, Boundary, Current state, Steps, Files touched, Verify, Dependencies / blocks, Delegation, Documentation impact, Discussion all present; frontmatter valid, status draft, no dependencies, so the `ki-plan` dependency rule is satisfied.
- Preflight passed with no warning: `ki repo audit --skill ki-work` PASS; `ki repo audit --skill ki-work-roadmap` PASS (15/15 evaluated, 11 judgment, 0 warnings).
- Every repository fact checked out against the working trees: ki-design root scripts (`build`, `self:typecheck`, `test`), the `packages/boundaries` vitest gate (DESIGN-2), `packages/elements` Lit pin 3.3.1 and the `ki-hexmap` `src` attribute with inline `islandmap/v1` JSON and no rendered text equivalent; site HEAD `31d02de8` clean on `main`, `apps/site/examples` absent, Eleventy 3.1.6 installed under `apps/site`, `apps/site/tsconfig.json` includes `**/*.mjs` with `allowJs` and no `checkJs`, `eleventy.config.ts` input `src`, site scripts `ki:site:build`, `self:typecheck`, `test`; both repositories' pre-commit hooks run lint-staged and syncpack; `mise.toml` node lts, bun 1.4.2.
- Every pin checked out offline from the local npm cache (packuments cached 22 Oct): lit 3.3.1; @lit-labs/ssr 4.1.0 (peer @types/node >=20 <25, node >=13.9); @lit-labs/ssr-client 1.1.8 exporting `lit-element-hydrate-support.js`; @lit-labs/eleventy-plugin-lit 1.0.6 (ssr ^4.0.0); @11ty/eleventy 3.1.6; @types/node 24.10.0; playwright-core 1.56.1 (node >=18). Runtimes present: Bun 1.4.2, `mise exec node@24.22.0` gives v24.22.0, Chrome 155, rumdl and ki installed. No install, registry or network call made.
- Decision Record deliverable: [GDR-KI-DESIGN-012](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-012-shared-web-components.md) is the correct living owner; the plan to edit it in place, replace the pending-spike line, name the guide in prose and route direction changes through Queries meets `ki-decision-records`. Its baseline audit findings (FILENAME-1, BODY-11 ×2) are pre-existing and the record already requires aligning title, H1 and metadata with the existing filename.
- Audit baselines confirmed so "no new finding" is checkable by diff: `ki-decision-records` 116 pre-existing FAILs, `ki-guides` 1 pre-existing FAIL (ROUTE-1 for `docs/spec`).
- Isolation arrangement re-checked: the either/or (linked worktree or untracked fixture on `main`) is acceptable because `ki agent launch --worktree` installs dependencies and Verify and cleanup already cover both cases; left as a recommendation, not a required change.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The "22 October 02:26 BST approval" cited in Delegation could not be verified in this review; it reads as a coordinating-thread decision and is not a repository fact.
- playwright-core 1.56.1 against local Chrome 155 is already flagged in the record as a risk to take on the `verify-browser` step.
- The record's planning observation `8cf04f4c` predates HEAD `732aa10f`; the record already instructs the successor to re-check, and nothing material changed between them.

## Queries

### ELE001-GUIDE-SCOPE - Guide must not carry a handoff section

**Context:** Documentation impact line 133 makes `docs/guides/developer/lit-ssr-spike.md` carry "the full temporary fixture sources, evidence and handoff section". `ki-guides` guides hold the self-contained practical how and may not carry forward work or roadmap references, and line 123 and line 137 already route proposals and direction changes to the run report's Queries. A handoff section in the guide contradicts both.

**Query:** Limit the guide to procedure, fixture sources, matrix results and conclusion, and keep proposals in the Queries route.

**Options:** a) (recommended, confidence medium - aligns the guide with `ki-guides` and with the record's own Queries route) Replace in line 133 "the durable reproduction procedure and conclusion for developers, including the full temporary fixture sources, evidence and handoff section;" with "the durable reproduction procedure and conclusion for developers, including the full temporary fixture sources, lockfile digest, matrix results and VM diagnostic, with no forward-work or handoff content, which stays in the run report's Queries;". b) Keep the wording and accept a guide that fails `ki-guides` self-containment on first audit.

### ELE001-DR-DATE - Decision Record amendment must advance its date

**Context:** Line 123 asks for GDR-KI-DESIGN-012 to be edited in place, "keeping the record self-contained and current", but names neither the `date` field nor the "(decided 18 October 2026)" phrase. `ki-decision-records` treats `date` as the current as-of date of a living record; Verify has no check for it.

**Query:** Make the date advance explicit so the DR audit gate is checkable.

**Options:** a) (recommended, confidence medium - small, makes the Verify gate concrete) In line 123 replace "keeping the record self-contained and current." with "keeping the record self-contained and current, setting its `date` to the amendment date and restating the decided-on date in prose." and add to the decision-audit gate in Verify: "GDR-KI-DESIGN-012 `date` equals the amendment date." b) Leave it implicit and rely on the implementer reading the standard.

### ELE001-ISOLATION - Select the untracked fixture on main (recommendation only)

**Context:** Line 32 defers the site isolation choice to the successor brief. The site primary checkout is clean on `main`, the fixture lives under an untracked path, and the worktree path adds a second dependency install, a disposable branch, double working-tree checks in Verify line 65 and worktree cleanup in line 36.

**Query:** Select the untracked fixture in the primary checkout now and drop the worktree alternative.

**Options:** a) (recommended, confidence low - a simplification, not a readiness defect) In line 32 replace "the successor brief must select either a runtime-owned linked worktree on disposable branch `spike/ki-design-ele-001`, outside repository and estate-discovery roots, or an untracked fixture in the primary checkout kept on `main`." with "the fixture is an untracked directory in the primary site checkout, which stays on `main` at its recorded HEAD."; in line 36 delete "and any disposable worktree and branch; do not merge the site branch"; in line 65 delete the sentence beginning "If using a disposable site worktree"; in line 111 delete "the selected site isolation arrangement,". b) Keep the either/or and let the brief select, as the record already provides for.

### 🤖 → 👤 Handoff to supervisor · since 09:11 BST

🤖 0 running · 👤 1 with you

- [review] KI-DESIGN-ELE-001 blind planning review, verdict NOT READY with two required edits · with you · since 09:11 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
