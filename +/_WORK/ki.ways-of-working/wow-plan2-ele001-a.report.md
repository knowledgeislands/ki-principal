# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan2-ele001-a

**🤖 → 👤 Handoff to supervisor · Run report at 03:02 BST · last mark 02:12 BST**

---

## Done

Verdict: **NOT READY** for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md); do not promote it to Ready or dispatch implementation tonight in its present form.

Confidence: **high** - the record remains the original three-step draft, and the cited replan report explicitly says the amendments were not made; the substantive readiness gaps remain.

Source check PASS: the record is byte-identical to its current committed version, retains `status: draft` and its 20 October update timestamp; the [replan report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-replan-ele001.report.md) confirms it stopped over unverified dependency pins without editing the record.

Review coverage PASS: checked the requirements in [review a](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-a.report.md), [review b](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-b.report.md) and [review c](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-c.report.md) against the live record, both repositories' instructions, manifests, and ki-design's component specification and decision.

Roadmap shape PASS; Ready gate FAIL under ki-work-roadmap: the immediate-work sections exist, but scope, setup, verification and the runtime decision are not concrete enough to execute and review.

Baseline check PASS: `baseline_ref: null` is correct before implementation; capture immutable ki-design HEAD when starting, with the corresponding site HEAD in the evidence.

Documentation check FAIL: the claim that no specifications exist contradicts [components.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/components.md) and misses the existing commitment in [GDR-KI-DESIGN-012](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-012-shared-web-components.md).

Execution checks NOT RUN: this review permits no installs, builds that write output, browser experiment or remote calls; no runtime compatibility conclusion is drawn from missing packages.

Commits: none; no repository files, lifecycle states, environment or credentials changed. Only this report and the requested status file were written.

### Remaining required changes

1. **Make the two-repository boundary concrete.** Name the site fixture, isolated Eleventy configuration, browser entry, assets, output, manifests and lockfile, any narrowly necessary elements changes, and exact evidence-note and site decision destinations. Choose one isolation and cleanup strategy consistent with the current primary-checkout instructions; resolve the earlier branch-versus-scratch alternatives. The current brief selects cross-repository work, so review b's preferred ki-design-only fixture is an alternative, not an additional requirement. Preserve no production page, deployment, release, publication, production runtime switch or change to `sync:design`; preserve the site's existing review work.

2. **Specify the elements consumption route.** Choose a temporary local link with its workspace dependencies resolved, or a self-contained build with its server and browser entry points explained. Address private, unpublished TypeScript exports, Node's loading/type-stripping requirements or a built JavaScript entry, and one compatible Lit identity on each render path. The source package pins `lit` 3.3.1. State where generated bundles live and what is retained; do not turn the spike into a production dependency or package release.

3. **Make dependency setup executable and authorised.** Name `@lit-labs/ssr`, `@lit-labs/ssr-client` and `@lit-labs/eleventy-plugin-lit`, verified compatible versions, the install command, owning fixture/workspace, and resulting manifest/lockfile changes. Resolve the earlier isolated-lockfile versus site-workspace recommendations into one choice. Record Eleventy and runtime versions, plugin mode and required flags. The successor execution brief must expressly authorise the named registry access/install in the relevant checkout; the plan and consensus review do not themselves lift a run's no-network restriction. Missing installed packages alone are setup work, not evidence of runtime incompatibility; unverified pins must not be invented.

4. **Separate integration paths and define the runtime decision.** Test direct `render()` integration and the Eleventy plugin under Bun and Node using the same fixture, recording all four results and exact commands. Distinguish dependency, configuration, TypeScript, VM and hydration failures from runtime failures. A plugin failure alone cannot establish Bun no-go. Define Bun go, Node-only conditional go, and neither-runtime no-go; record a tested alternative or leave an inconclusive experiment blocked. Frame the choice as the runtime for Eleventy and SSR, with the site's Bun verification and commit tooling outside this decision.

5. **Replace Verify with reproducible observations.** Name build and browser-check commands, fixture data, output and evidence paths. Assert meaningful glyph and map SVG inside Declarative Shadow DOM templates with Lit markers before JavaScript, including readable no-JavaScript output. Load `lit-element-hydrate-support` before defining the elements, then use a real browser to demonstrate adoption of the server shadow roots without replacement or duplicate rendering, no hydration errors, a glyph update, and map selection/keyboard behaviour. Name the affected build, type and test gates in both repositories; isolate the fixture from the site's route, reachability and prose checks or satisfy them explicitly.

6. **Correct documentation and decision ownership for every outcome.** Name the reproducible procedure and conclusion's durable home. Assess the actual component specification and existing shared-components decision: confirm the accepted approach after success, or amend/revisit the SSR commitment and record an alternative after no-go. Name the site's Decision Record destination for a Node-only choice and the follow-on work to ship SSR. Recording a decision does not authorise changing production scripts tonight.

7. **Align classification, size and handoff.** Reclassify the controlling finding as `kind: investigate`, assess `purpose: learning`, and revisit `size: m` against the cross-repository delivery shape. If treated as `l` or delegated work, add the required Delegation section with bounded deliverables, file boundaries, gates and final review responsibility. Replace Dependencies / blocks “None” with the actual local-checkout, site-baseline, dependency and handoff context; retain empty dependency-ID arrays unless a genuine build-order prerequisite exists.

8. **Complete readiness on an actually revised record.** Advance `updated_at` with the amendment, retain Draft while shaping, run the relevant local checks, and obtain the agreed high-confidence model consensus on that same revised plan. Kris's 22 October grant supplies an approval route; it does not waive concreteness, checkable verification or execution authority. This review supplies no READY consensus.

## In Progress

Nothing is running. The supervisor owns completing the replan, resolving the dependency-version evidence raised in the replan report, and obtaining fresh agreement; the record remains Draft.

## Queries

No outstanding queries from this completed review. The replan report's dependency-version query remains with the supervisor; this review neither resolves it nor requests network access.

### 🤖 → 👤 Handoff to supervisor · since 03:02 BST

🤖 0 running · 👤 0 with you · ⛔ 0 blocked

- [handoff] NOT READY verdict and required amendments for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) · supervisor · since 03:02 BST
