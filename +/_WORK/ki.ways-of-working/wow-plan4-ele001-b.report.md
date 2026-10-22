# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan4-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 08:31 BST · last mark 02:12 BST**

---

## Done

VERDICT: READY · confidence medium · every required amendment from the three round-3 reviews is met and the facts check out against both repositories. Two edits belong in the Ready commit. Separately, `ki-plan`'s Ready preflight will stop on three warnings from other ki-design records until they are cleared or waived (see Queries).

This was a blind, read-only review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at ki-design `7785bc1`, which differs from `c813003` only in the wow-replan3-ele001 amendment. I checked it against the `ki-work-roadmap` [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-design/.agents/skills/ki-work-roadmap/references/standards-work-item-format.md), the `ki-plan` preflight, ki-git and ki-design `AGENTS.md`. No repository changed and no remote call was made.

### Round-3 required amendments

- **Reviewer a, ELE001-PROJECT: met.** The `project:` frontmatter line is gone, and the roadmap audit reports nothing against ELE-001.
- **Reviewer b, 1 (map text equivalent): met.**
  - Step 4 and Verify have the fixture write its own list outside and next to `<ki-hexmap>`, following GDR-KI-DESIGN-032.
  - The SSR assertion now checks `role="option"` counts and `aria-label`s.
  - The missing text equivalent in the v0 element is recorded as a separate follow-up under Specifications.
  - The element source confirms there is no slot and that `src` is parsed in `willUpdate`, so it runs during SSR.
- **Reviewer b, 2 / reviewer c, 1 (site handoff): met.** The run returns the proposed message line in its report and the supervisor routes it, as the last Step, Files touched, Delegation, Decision Records and Roadmap all say. The site has no `+/_WORK/` (it has only `_AUTHORISATIONS` and `_TRADES`). This matches the standard's hand-over-as-message rule.
- **Reviewer b, 3 (Node version actually used): met.** Step 1 records both versions as invoked and stops on a mismatch. Every Node command in Verify uses `mise exec node@24.22.0`. Verified: bare `node` is v24.21.0, and `mise exec node@24.22.0 -- node --version` gives v24.22.0.
- **Reviewer c, 2 (guide placement): met.** The guide moves to `docs/guides/developer/lit-ssr-spike.md`, with an index entry in the existing `docs/guides/developer/README.md`.

### Ready-commit amendments (required at the transition, not a replan)

1. **Delegation does not yet name the orchestrator's final review.** The work-item format requires Delegation to name "the gate between rounds, and the orchestrator's final review and verification responsibility" ([standard](/Users/krisbrown/workspaces/knowledge-islands/ki-design/.agents/skills/ki-work-roadmap/references/standards-work-item-format.md)). The current section covers only planning review and the return contract.
   - **Change:** append to Delegation: "One round. Before Awaiting review, the supervisor re-runs `verify-html.mjs` and `verify-browser.mjs` against at least one returned output, using the recorded commands. They check each matrix cell against its saved stdout, stderr and exit status. They also confirm that both repositories' root `package.json` and `bun.lock` and `apps/site/package.json` are unchanged, that no production path changed, and that the site branch and scratch directory are gone."
2. **Planning-gate sentences will be stale once the record is Ready.**
   - **Change:** at the Ready commit, rewrite these to record that the three-reviewer gate was met, naming the agreeing runs:
     - [line 105](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:105): "keep this item Draft until the separate readiness decision".
     - [line 107](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:107): "After this amendment … this run neither dispatches …".
     - [line 127](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:127): "stays Draft until the three-reviewer gate is met".

### Recommended, not blocking

3. **Avoid switching the shared site checkout's branch in an unattended run.** The fixture sources are never committed and their durable home is ki-design, so the branch adds nothing. Switching HEAD in the human's primary site checkout, where the site's design-v1 record is awaiting review, is the case ki-git's [worktree rule](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-git/references/standards-git.md:71) points to a worktree for.
   - **Change:** in Boundary, say that an unattended run either uses a runtime-owned linked worktree on `spike/ki-design-ele-001`, or leaves the primary checkout on `main` with the fixture untracked.
   - Whichever it uses, the run restores the primary checkout's HEAD before cleanup.
4. **Make the lockfile boundary checkable.** Add a Verify line after the fixture install and at close: `git -C <site> diff --quiet -- package.json bun.lock apps/site/package.json` and `git -C <ki-design> diff --quiet -- package.json bun.lock`.
5. **Separate the browser source from the build output.** Step 3 says "Build `src/assets/browser.mjs`", but Files touched lists that same path as a source. Name a source entry (for example `src/assets/browser.entry.mjs`) and a build output (for example `generated/browser.mjs`, passed through by Eleventy), so the build cannot overwrite its own input.
6. **Specify the bundle target.** In Step 2, specify `Bun.build` with `format: 'esm'` and a target other than `bun`, so that Node can load the shared `generated/elements.mjs`. Otherwise a bundle-target failure could be misread as a runtime failure.
7. **Use plain words for the site's pending review.**
   - Boundary [line 34](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md:34) names another repository's record by its identifier, which the standard forbids because records are pruned. Write "the site's pending design-v1 review" instead.
   - The handoff paragraph appears five times word for word. Keep it once, in Delegation, and point to it from the other places.
8. **State how fixture-caused gate failures count.** The site's `apps/site/tsconfig.json` includes `**/*.mjs` with `allowJs` (no `checkJs`), so the site typecheck also reads the fixture and generated `.mjs` files. Say that a diagnostic the fixture causes is a fixture defect, not a pre-existing failure.
9. **Flag the browser-driver version gap.** `playwright-core` 1.56.1 is several releases older than the installed Chrome 155; the cached registry metadata lists 1.64.1 as latest. Note that a launch or protocol failure is a setup block, which existing escalation already covers. Alternatively, re-pin after a metadata check.

### Checks

- Checkouts: ki-design `7785bc1` is clean. The site is at `31d02de84d91c89452a1de3dad5c764bc3da11f5` on `main`, clean, with one worktree. The site's design-v1 record is `awaiting-review`. PASS.
- Toolchain: Bun 1.4.2, Node 24.22.0 through mise, Chrome 155.0.8059.85. Eleventy 3.1.6 with `cmd.cjs` is in `apps/site/node_modules`, and no Lit packages are in the site. `bun --experimental-vm-modules` is accepted. PASS.
- Elements: `lit` 3.3.1; the package exports `./src/index.ts`, which defines both elements on import. The workspace dependencies resolve through symlinks in `packages/elements/node_modules`, and `icons.generated.ts` is tracked. `ki-select`, the roving tabindex and the glyph `name` and `label` are present. PASS.
- Registry pins, checked against the local npm metadata cache with no network call: plugin 1.0.6, SSR 4.1.0 (including the `@types/node` peer `>=20.0.0 <25.0.0`), client 1.1.8, `lit` 3.3.1, and the `playwright-core` engine `>=18` all match the record. The plugin declares no Eleventy peer. PASS.
- Referenced decisions and paths: GDR-KI-DESIGN-012, GDR-KI-DESIGN-032 and the developer guides index exist. PASS.
- `ki repo audit --skill ki-work`: PASS.
- `ki repo audit --skill ki-work-roadmap`: FAIL=0, WARN=3. All three are ITEM-2 warnings on ART-002, MAP-002 and TIL-002; none is on ELE-001.
- rumdl on the record: PASS.
- Repository integrity: PASS. There were no edits, installs, commits or remote calls.

## In Progress

Nothing is running. [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) stays `draft`. The supervisor owns the Ready-commit amendments, the preflight warnings, and the Ready transition, which needs agreement from all three reviewers.

## Queries

### [ELE001-PREFLIGHT - Repository-wide warnings stop the Ready transition](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md)

**Context:** `ki-plan`'s preflight stops on any warning from the local adapter audit. That audit runs across the whole repository and currently reports three ITEM-2 warnings: `project: ki-design` is unregistered on KI-DESIGN-ART-002, KI-DESIGN-MAP-002 and KI-DESIGN-TIL-002. ELE-001 itself is clean, but its transition still stops.

**Query:** How should the preflight be cleared before ELE-001 is set to Ready?

**Options:**

a) (recommended, confidence medium - this is the same fix ELE-001 already received and it leaves the preflight unchanged) In a separate planning commit, remove the unregistered `project:` line from those three records, then re-run the audit.

b) Register a `ki-design` Project in the Capital's registry so that the existing values resolve.

c) Record an owner waiver for these specific warnings and proceed with the transition.

### 🤖 → 👤 Handoff to supervisor · since 08:31 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [handoff] READY verdict with two Ready-commit amendments and the preflight query for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) · supervisor · since 08:31 BST
