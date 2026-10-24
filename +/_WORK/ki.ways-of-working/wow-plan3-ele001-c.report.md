# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan3-ele001-c

**🤖 → 👤 Handoff to supervisor · Run report at 03:13 BST · last mark 02:12 BST**

---

## Done

VERDICT: READY · confidence high · every required change from the three earlier reviews is met, the plan is bounded to a disposable site fixture and findings in ki-design, and its Verify is a command-and-assertion matrix; two line-level amendments below should land in the Ready commit, and neither changes execution or its safety.

Blind read-only review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at ki-design `c813003` against the work-item format and repository-roadmap standards, the ki-plan readiness procedure, ki-design's AGENTS.md, ki-guides, the elements source, the site checkout at `31d02de` and the local toolchain. No file in either repository changed; no commit; no remote call. Both working trees are clean.

### Earlier required changes, each checked

- Review a, items 1 to 5: met. Both repositories are bounded in Boundary and Files touched; packages, versions and the bundle route are named; Verify is a repeatable pass/fail procedure with gates; the decision procedure separates setup failure from runtime failure; Documentation impact now names the existing component specification and the procedure's home.
- Review b, items 1 to 8: met. Execution location chosen (its option b: a disposable site branch with isolated install, size `l`, Delegation section); `Bun.build` bundle with externalised Lit, kept uncommitted; all seven pins named with isolated `package.json` and lockfile; equal Bun and Node steps with worker and VM modes and go, conditional go and no-go defined; checkable Verify naming `playwright-core` on local Chrome over loopback; Documentation impact corrected; `kind: investigate`; three-reviewer gate recorded.
- Review c, items 1 to 8: met. Direct and plugin paths split into a two-by-two matrix; elements reach the fixture as a generated module with a single-Lit check via `import.meta.resolve` and the metafile; packages pinned (its devDependency-in-`apps/site` request was superseded by review b's isolation requirement, reconciled in Discussion); hydrate support loaded before definitions with DOM-identity assertions in a real browser; Files touched concrete in both repositories with a separate Eleventy configuration keeping the site gates clean; decision homes for every outcome, framed as the Eleventy process only; Boundary carries the five exclusions; Dependencies narrative names both baselines.

### Facts verified

- Bun 1.4.2, Node 24.22.0 (via the site's mise `node = "lts"`; the shell default elsewhere is 24.21.0), Eleventy 3.1.6 in `apps/site`, Chrome 155 installed; no `@lit-labs/*` or `lit` package in the site: PASS, matches Current state.
- Site gates `verify:reachable` and `verify:prose` read `apps/site/dist` only, so the fixture's separate output cannot enter them: PASS.
- Isolated-install precedent: both repositories already run `bun install --cwd tooling/depcruise` with its own `bun.lock`: PASS.
- Elements source supports every assertion the Verify names (`src` JSON attribute, `islandmap/v1` validation, `ki-select` detail, roving tabindex with Arrow, Enter and Space, glyph `name` and `label`): PASS.
- Frontmatter, section order, four-word title, `size: l` with Delegation, `blocked_by: []`, `baseline_ref: null`, timestamps: PASS. rumdl on the record: PASS. `ki repo roadmap list` shows it as `draft` at `now`: PASS.
- `project: ki-design` has no entry in the ki-principal Project registry; this is a warning under the standard, shared by every ki-design record, not a defect of this one.

### Amendments to land in the Ready commit

1. **Message-queue target does not exist.** The site has no `+/_WORK/` folder, so "the site's work `messages.md`" named in Files touched, Delegation, Decision Records and Roadmap has no file to receive the line, and the successor would stop at the end of the run. Amend Delegation (and the Roadmap subsection) to: "If the site has no open work package under `+/_WORK/`, do not create one; record the proposal in the evidence note's handoff section and return it in the run report's Queries for the site owner to capture under `ki-next`."
2. **Procedure placement follows ki-guides.** ki-design declares `ki-guides`, whose guides live under `docs/guides/`; `docs/briefs/` is the collection of art and tile task briefs. Either move the durable procedure to `docs/guides/developer/lit-ssr-spike.md` with an index line in `docs/guides/developer/README.md`, or keep `docs/briefs/lit-ssr-spike.md` and add its row to the briefs README table with a one-line justification in Guides. Apply the same path in Files touched and Documentation impact.

### Recommended, not blocking

- The site's `apps/site/tsconfig.json` includes `**/*.mjs` with `allowJs`, so on the spike branch the site's `typecheck` gate parses every fixture `.mjs` file including `generated/elements.mjs`. Naming the fixture scripts `.js` (the fixture already sets `type: module`) keeps them outside that glob; otherwise state that a typecheck failure caused by the fixture is a fixture defect to fix, not a pre-existing failure.
- `src/assets/browser.mjs` appears both as a fixture source and as the output of `build.mjs`; say which, for example source `src/assets/browser.entry.js` and output under `generated/` passed through by Eleventy.
- Say that Bun may reject `--experimental-vm-modules` and that a rejected flag is recorded as the VM diagnostic, not as a Bun failure.
- Add to the first Step: assert `bun --version` 1.4.2 and `node --version` 24.22.0 inside the fixture before the matrix, since the site pins Node as the floating `lts` alias.
- Boundary names the site record `KI-WEBSITE-SITE-044`; the work-item standard prefers plain words for another repository's work because records are pruned. "the site's pending design-v1 review" suffices.

## In Progress

Nothing. The record stays `draft` and unchanged; the supervisor owns the amendments, the three-reviewer gate and the Ready transition under the 22 October 02:26 BST approval.

## Queries

None. Both amendments are planning text within the approved scope and need no new permission.

### 🤖 → 👤 Handoff to supervisor · since 03:13 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [handoff] READY verdict with two Ready-commit amendments for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) · supervisor · since 03:13 BST
