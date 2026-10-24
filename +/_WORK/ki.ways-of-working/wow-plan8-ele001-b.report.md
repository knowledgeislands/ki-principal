VERDICT: NOT READY · confidence high · Outcome classification contradicts itself, and go-path and guide edits can commit an unapproved settlement of a Proposed decision.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan8-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 09:39 BST · last mark 08:24 BST**

---

## Done

- Blind planning review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at `d345ecd0`. Read-only; no commits, installs or network calls.
- Ready preflight (`KI_REPO_OFFLINE=1`): `ki-work` passed and `ki-work-roadmap` passed, with no warnings in either.
- The baseline audits the plan depends on: `ki-decision-records` fails 116 times before any change. GDR-KI-DESIGN-012 has three of those failures (FILENAME-1 and two BODY-11), and the plan's in-place edit fixes all three. `ki-guides` fails once before any change (ROUTE-1 on `docs/spec`). The plan's rule of "no new finding" can be checked against both.
- These repository facts and pins check out: Bun 1.4.2; `mise exec node@24.22.0` reports v24.22.0; Chrome is 155.0.8059.85. `playwright-core` 1.64.1 is in the Bun cache at `~/.cache/.bun/install/cache`, needs Node >=20 and targets Chromium 156.0.8078.4. The site is clean on `main` at `31d02de8`, with Eleventy 3.1.6, `**/*.mjs` included with `allowJs` and no `checkJs`, and workspaces `packages/*` and `apps/*`, so the fixture falls outside every workspace. The production Eleventy input is `src`, and the `verify:*` gates read `dist/`. In ki-design, `lit` is 3.3.1; the elements, icons and hexmap packages all export TypeScript; the index graph has no `node:` imports; `<ki-hexmap>` has no slot and renders no text equivalent; the `src` JSON attribute exists. All the named gate scripts exist.
- Three defects block Ready. The exact edits are below.

### Required change 1 - the outcome rules contradict each other, so neither go nor conditional go is reliably reachable

The Node step (Steps item 6) says "A setup failure leaves the experiment blocked." Read across the whole experiment, that withholds a go whenever any non-Bun-direct cell (for example the plugin against Eleventy 3.1.6) is blocked at setup. But the decision procedure says a passing Bun direct path is a go. Read per cell, the other way, the conditional-go definition ("no complete Bun path passes but at least one Node path passes") would recommend moving Eleventy to Node because of a Bun setup problem. That contradicts the Goal's word "evidenced" and the no-go rule's ban on setup causes. The four failure classes are also never sorted into setup and runtime.

- Steps item 6: replace "Separate package/configuration, bundle resolution, VM/worker and component-lifecycle failures before attributing a failure to a runtime. A setup failure leaves the experiment blocked." with "Classify each failed cell as **setup**, **runtime** or **component lifecycle**. **Setup** means a package, configuration or bundle fault that the fixture could still correct within its grant. **Runtime** means a difference between Bun and Node behaviour, worker or VM semantics, or module resolution, reproduced with the identical fixture. **Component lifecycle** means a fault in the unchanged elements that appears under both runtimes. An unresolved setup failure leaves that cell blocked; the decision procedure below sets the overall outcome from every cell."
- Decision procedure: replace "**Conditional go** means no complete Bun path passes but at least one Node path passes;" with "**Conditional go** means neither Bun path passes, each Bun failure is diagnosed as runtime or component lifecycle rather than setup, and at least one Node path passes;". After "A plugin failure with a passing Bun direct path is a Bun go, not a Bun no-go." add: "A go needs only its passing Bun path. Every other cell is recorded with its diagnosis or blocked state and does not withhold the go. Where no Bun path passes and any Bun cell is blocked at setup, the overall outcome is blocked."

### Required change 2 - a go can commit a settlement of Lit's Proposed status that the owner has not approved

Only conditional go, no-go and a "change of direction" go back to the owner. On go, the worker commits GDR-KI-DESIGN-012 directly, replacing "Lit is the proposed implementation, pending the spike" with "the evidenced rendering route". Under GDR-KI-DESIGN-002, only agreement with the owner moves something from Proposed to Agreed. The component specification also marks Lit _proposed_. An investigation record closes on a finding; it does not decide on the owner's behalf. Separately, under conditional go or no-go, the specification, guide and package README edits have no approval gate. So the direction could land in those files while the decision record waits.

- Documentation impact › Decision Records: replace the final sentence ("For conditional go, no-go or any change of direction, ...") with: "On go, the committed edit records the evidenced route, its limitations and conditions, while Lit keeps its _proposed_ status under GDR-KI-DESIGN-002. Moving Lit to Agreed needs the owner's agreement and is returned in the run report's Queries. For conditional go, no-go or any change of direction, return the proposed owning-record edit in the run report's Queries for owner approval, together with the matching wording for the specification, the guide and `packages/elements/README.md`. Commit none of it without that approval."
- Documentation impact › Specifications: replace "If no route passes, link the reconsideration of GDR-KI-DESIGN-012 and retain the no-JavaScript requirement pending its owner's decision." with "If no route passes, leave the toolkit wording and the no-JavaScript requirement unchanged until the owner approves the proposed GDR-KI-DESIGN-012 edit."
- Verify › Decision and guide gates: after "Confirm that conditional-go, no-go or other direction-changing edits remain proposals in the report Queries until owner approval" insert "and that a go edit keeps Lit marked proposed unless the owner has agreed".

### Required change 3 - the guide's scope duplicates the decision and has no judgement check under `ki-guides`

Documentation impact › Guides makes the developer guide "the durable reproduction procedure and conclusion". Under ki-guides ROUTE-2, a guide holds practical procedure, not duplicated rationale or forward work. The route conclusion belongs to GDR-KI-DESIGN-012. The mechanical audit covers links (GUIDE-4) and the opening (GUIDE-6), but nothing in Verify judges ROUTE-2 to ROUTE-4. The plan does this for the decision record but not for the guide.

- Documentation impact › Guides: replace "is the durable reproduction procedure and conclusion for developers, including the full temporary fixture sources, final exact dependency pins, lockfile digest, matrix results and VM diagnostic;" with "is the durable reproduction procedure for developers. It opens with what the reader can do: rebuild the fixture and reproduce the runtime matrix and both verifiers. It holds the full temporary fixture sources, the final exact dependency pins, the lockfile digest, and the expected and observed matrix results and VM diagnostic as its success check. It names GDR-KI-DESIGN-012, the component specification and this work record in prose without links, and leaves the rationale and recommendation for the rendering route to GDR-KI-DESIGN-012;"
- Verify › Decision and guide gates: append "In the same final review, judge the guide against ki-guides ROUTE-2 to ROUTE-4: a practical procedure with verifiable success and recovery, no duplicated rationale or forward work, and no link text standing in for content."

## In Progress

Nothing.

## Queries

None. Disclosure: while checking the report-heading format, a `head` of the most recent reports in the run directory showed the first line of `wow-plan8-ele001-a`. I read nothing further from it, and this verdict rests only on the evidence above.
