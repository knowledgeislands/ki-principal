# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan-ele001-a

**🤖 → 👤 Handoff to supervisor · Run report at 02:55 BST · last mark 02:12 BST**

---

## Done

Verdict: **NOT READY** for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md).

Confidence: **high** — the spike is sound in purpose, but its cross-repository scope, verification and runtime decision procedure are insufficiently concrete, and its documentation assessment is demonstrably stale.

Required plan changes before Ready:

1. Bound both repositories explicitly in Boundary and Files touched: the site's scratch Eleventy fixture/configuration, browser entry and assets, dependency manifests/lockfile, the local elements import/build route and any necessary design-package compatibility edits. Name the exact evidence-note destination under ki-design `docs/` and the site-owned decision destination. Preserve the no-production-change boundary: a Node decision does not authorise switching production scripts or deployment. The successor execution brief must cover both checkouts and registry installation; this review grants no execution authority.

2. Replace Dependencies / blocks “None” with the actual setup and add an initial task for it. Name `@lit-labs/ssr` and `@lit-labs/eleventy-plugin-lit`, their owning site workspace and the resolved versions to record; identify any browser hydration dependency required by the chosen integration. Explain how the private `@knowledgeislands/elements` package and its workspace dependencies reach the site fixture without publishing a package. Dependency installation can be an execution step; its present absence alone does not prohibit Ready once setup is understood and authorised.

3. Make Verify a repeatable pass/fail procedure: name the build command, fixture/output and browser check. Check generated Declarative Shadow DOM containing meaningful glyph and map SVG before JavaScript runs, then demonstrate hydration of that server DOM, a glyph update and map selection/keyboard behaviour without hydration errors. Record runtime/package versions, relevant VM/TypeScript flags and browser evidence. Identify the affected repositories' existing build/check gates. The current [Verify](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:47) permits a generic no-go note to substitute for the experiment.

4. State the decision procedure: attempt the same fixture under Bun first; if Bun fails, separate dependency/configuration mistakes from runtime incompatibility, then try the Node alternative with the same SSR and browser assertions. Record evidence and rationale for the Bun-or-Node choice. A working Node alternative supports the site-owned Decision Record; an untested alternative or an inconclusive experiment remains blocked rather than a completed no-go. Retain the follow-up boundary for shipping SSR.

5. Correct [Documentation impact](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:55): specifications already exist, including [components.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/components.md:13), which explicitly depends on this spike. Say whether its proposed toolkit/SSR wording changes after the result, or justify leaving it unchanged. Name where the reproducible spike procedure and conclusion will live rather than relying on the generic developer guide.

Roadmap shape check: PASS — required sections, documentation subsections and unchecked Steps exist; [the readiness standard](/Users/krisbrown/workspaces/knowledge-islands/ki-design/.agents/skills/ki-work-roadmap/references/standards-work-item-format.md:266) also requires concrete scope and checkable verification.

Baseline check: PASS for Draft/Ready — `baseline_ref: null` is correct until execution starts; set the immutable ki-design HEAD at In progress and capture the site's corresponding HEAD in the evidence, rather than treating the absent baseline as a planning blocker.

Local dependency check: PARTIAL — Eleventy is declared and installed in the site workspace; the two Lit labs packages are absent there. Failure to resolve Eleventy from ki-design does not show that the site's installation is missing.

Documentation check: FAIL — the record's claim that this repository has no specifications contradicts the existing component specification.

Runtime feasibility checks: NOT RUN — this was an offline, read-only planning review; no compatibility verdict is inferred from missing packages.

Repository integrity check: PASS — both tracked working trees were clean when inspected; no repository file, lifecycle state or Git configuration was changed, and no commit was made.

## In Progress

Nothing running. The supervisor owns the listed planning amendments and any consensus-based Ready transition under Kris's conditional authority of 22 October 2026. The record remains Draft; there is no implementation or acceptance in this review.

## Queries

No outstanding queries. The required changes are planning work within the proposed scope, not a request for another general permission round.

### 🤖 → 👤 Handoff to supervisor · since 02:55 BST

🤖 0 running · 👤 0 you · ⛔ 0 blocked

- [handoff] Planning verdict and required amendments for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) · supervisor · since 02:55 BST
