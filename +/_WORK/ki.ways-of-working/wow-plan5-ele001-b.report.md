# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan5-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 08:47 BST · last mark 08:24 BST**

---

## Done

VERDICT: NOT READY · confidence high · Every plan4 amendment is met and the Ready preflight is clean. The Decision Record deliverable still conflicts with the `ki-decision-records` standard, and Verify has no check that would catch it.

This was a blind, read-only review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at ki-design `8cf04f4c491d42ba90e817d940961f69f10c868f` on `main`, with a clean tree. The site checkout is at `31d02de84d91c89452a1de3dad5c764bc3da11f5` on `main`, clean, with one worktree. I read only the three named plan4 reports and wow-replan4-ele001. There was no commit, no remote call, and nothing was written outside this report and its status file.

### Finding ELE001-DECISION-RECORD — required amendment

[Files touched](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:57) and [Decision Records](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:121) require a new record with a fixed slug, `lit-ssr-spike`, for every outcome, linked from the guide. The [decision-record standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-decision-records/references/standards-decision-records.md) conflicts with this in four ways:

1. **Filename.** FILENAME-1 requires the filename to be the ID followed by the slugified title. A fixed slug therefore forces the title "Lit SSR spike", which states no decision, or it adds a new audit failure.
2. **Edit in place.** The standard says to edit the record that owns a concern rather than add one beside it. [GDR-KI-DESIGN-012](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-012-shared-web-components.md) owns this concern. Its line "Lit is the proposed implementation, pending the spike KI-DESIGN-ELE-001" is what the spike resolves.
3. **Stale citation.** That same line cites this record's identifier and will go stale on prune. The plan never updates it.
4. **Links.** BODY-11 allows a record to link only to sibling records and external URLs. A natural link from the record to the evidence guide would add a failure.

The [repository gates](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:86) run no decision-record or guide audit, so the "add none" rule cannot be checked for the record's main deliverables. The current full audit already has 30 FILENAME-1 and 71 BODY-11 failures, so a successor copying the existing records would add more without any gate noticing.

**Amendment:**

- **Files touched and Decision Records.** Replace the fixed-slug sentences with: "Record the outcome by editing GDR-KI-DESIGN-012 in place under `ki-decision-records`. Replace its pending-spike line with the evidenced route and its conditions. Name the developer guide in prose, without a relative link. For a conditional go or a no-go, which is a change of direction, return the proposed GDR-KI-DESIGN-012 edit in the report's Queries for owner approval rather than committing it. Create a separate record only if the rendering-route or runtime decision is genuinely independent. Such a record takes the next contiguous GDR serial and a `<ID>-<slugified title>.md` filename."
- **Steps.** Make Step 8 and the Roadmap paragraph consistent with this.
- **Repository gates.** Add `ki repo audit --skill ki-decision-records --repo <ki-design>` and `ki repo audit --skill ki-guides --repo <ki-design>`, run at baseline and again at close. Require no new finding on the changed or new decision records, `docs/guides/developer/lit-ssr-spike.md` or the guides index, and record the counts already present at baseline separately.

### Plan4 required amendments

- **Reviewer a, ELE001-FINAL-REVIEW: met.** [Delegation](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:115) now names the supervisor's final review of every item the finding listed:
  - the matrix against each cell's saved stdout, stderr and exit status;
  - the failure diagnoses;
  - the fixture, manifest, lockfile digest and dependency graph;
  - the browser evidence, gate results and production-path exclusions.

  It also requires independent reproduction before the fixture is removed, a re-run of both verifiers on a preserved output, a reproduction check for a no-go, a correction loop, and cleanup confirmation.
- **Reviewer a, ELE001-PREFLIGHT: met.** Commit `ad76adb` removes `project:` from ART-002, MAP-002 and TIL-002 without changing their lifecycle. No record carries `project:` now.
- **Reviewer b, 1 (final review): met**, as above.
- **Reviewer b, 2 / reviewer c (planning-gate sentences go stale at Ready): met as a transition instruction.** [Delegation](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:111) tells the Ready commit to replace the pending-gate paragraph and update Current state and Roadmap. That is correct while the record is still a draft.
- **Reviewer b, recommendations 3 to 9: met.**
  - 3: the isolation choice is in Boundary.
  - 4: the `git diff --quiet` checks are in Verify.
  - 5: the browser source and the build output are now separate files.
  - 6: Step 2 sets `format: 'esm'` and `target: 'node'`.
  - 7: the site's pending review is described in plain words, and the full handoff contract appears once, with pointers.
  - 8: a typecheck diagnostic the fixture causes counts as a fixture defect.
  - 9: the Playwright and Chrome version gap is treated as a setup block.
- **Reviewer c, cross-repository identifier: met.** The record contains no site record identifier.

### Ready preflight (read-only)

- **Physical root:** PASS. Git root and physical path agree.
- **`ki repo audit --skill ki-work`:** PASS. The adapter is `roadmap`.
- **`ki repo audit --skill ki-work-roadmap`:** PASS, with no failures or warnings.
- **Record resolution:** PASS. The record resolves inside `docs/roadmap/`.
- **rumdl on the record:** PASS.

### Fact checks

- **Toolchain: PASS.** Bun 1.4.2. Node 24.22.0 through `mise exec node@24.22.0` (bare `node` is 24.21.0). Chrome 155.0.8059.85. The site's Eleventy is 3.1.6.
- **Site layout: PASS.**
  - There is no `apps/site/examples/`, `spike/*` branch, `+/_WORK/` or Lit Labs package.
  - Root workspaces are `packages/*` and `apps/*`, so the fixture is not a workspace member. `tooling/depcruise` is the precedent for a separate lockfile.
  - Production Eleventy input is `src`. Every `verify:*` reads `dist/`, and provenance stays offline without `--network`.
  - `apps/site/tsconfig.json` includes `**/*.mjs` with `allowJs`, as the record states.
- **Elements: PASS.**
  - The package is private and exports `src/index.ts`, which defines both elements on import. That fits Step 3's dynamic import after hydration support.
  - The package uses no decorators.
  - The `src` attribute is parsed synchronously in `willUpdate`.
  - The map renders `role="option"` cells with a roving tabindex and fires `ki-select`. It has no `<slot>`.
- **Baseline drift: PASS.** Since the record's observed `f603f56`, ki-design changed only `docs/roadmap/`.
- **Full `ki repo audit`:** FAIL, with 127 failures and 7 warnings, all already on `main`. It matches wow-replan4-ele001 and none comes from this record.
- **Not run:** registry metadata, because remote calls are forbidden. Installs, experiments, builds, tests and hooks, because this review is read-only.

### Recommended, not blocking

- **Temporary outputs.** [Files touched](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:59) lists the outputs as `out/{bun,node}-{direct,plugin}/`, but Verify also writes `out/{bun,node}-plugin-vm/`. Change the list to "`out/` (every matrix case)".
- **Diff checks under a worktree.** Under the worktree option, run the [Verify diff checks](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:65) against both the worktree and the primary site checkout.

## In Progress

Nothing is running. [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) stays `draft`. The supervisor owns the Decision Record amendment, a fresh three-reviewer round and the Ready transition.

## Queries

### [ELE001-DECISION-RECORD — where the spike's outcome is recorded](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-012-shared-web-components.md)

**Context:** The record requires a new decision record with the fixed slug `lit-ssr-spike`. GDR-KI-DESIGN-012 already holds "Lit is the proposed implementation, pending the spike", and `ki-decision-records` requires edits in place and filenames built from the title.

**Query:** Where should the replan direct the outcome?

**Options:**

a) (recommended, confidence high - the standard's edit-in-place rule and GDR-KI-DESIGN-012's pending line both point here) Edit GDR-KI-DESIGN-012 in place. Return a conditional go or no-go as a proposed edit for owner approval. Add the decision-record and guide audits to Verify.

b) Keep a new record, but drop the fixed slug: use the next GDR serial and a filename built from the decision title, with no link to the guide. Still update GDR-KI-DESIGN-012's pending-spike line, and add the same audits.

c) Keep the plan as written and accept new audit findings, which conflicts with the record's own "add none" rule.

### 🤖 → 👤 Handoff to supervisor · since 08:47 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [handoff] NOT READY verdict with one Decision Record amendment for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) · supervisor · since 08:47 BST
