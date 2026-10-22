# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan9-ele001-c

VERDICT: NOT READY · confidence medium · three bounded wording gaps would mislead delivery: site gates are unrunnable as written under the permitted worktree arrangement, the "evidence note" the Steps and Verify write to is never defined, and the go edit to GDR-KI-DESIGN-012 can be read as adopting a rendering route the owner has not approved.

**🤖 → 👤 Handoff to supervisor · Run report at 09:56 BST · last mark 09:56 BST**

---

## Done

- Reviewed [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at ki-design `225af635` (working tree clean), read-only, no commits.
- Ready preflight: `ki repo audit --skill ki-work` PASS, `--skill ki-work-roadmap` PASS, no warning, offline.
- Decision and guide audit baselines: `ki-decision-records` FAIL with 116 pre-existing findings (three on GDR-KI-DESIGN-012: FILENAME-1 and two BODY-11, all of which the planned amendment removes); `ki-guides` FAIL with one pre-existing ROUTE-1 finding on `docs/spec`. The plan's "no new finding on changed records" rule handles both.
- Record shape: frontmatter, section order, Documentation impact subsections, task-list Steps and trailing Discussion all conform to the work-item format.
- Steps order: each Step's inputs exist when it runs (install before the setup check, elements bundle before the browser graph, verifiers before the matrix, gates and audits before delivery edits).
- Decision procedure: go, conditional go, no-go and blocked are mutually exclusive and jointly cover every two-by-two and verifier outcome; VM cells never gate the outcome.
- Decision Record deliverable: in-place amendment, `date` as amendment date with the decided-on date in prose, prose names instead of links, References omitted when empty, title aligned to the existing filename, no work identifier or forward work; this meets the decision-records standard and the record's own Verify.
- Guide scope: developer audience, outcome-first opening, procedure with success and recovery, prose names for the Decision Record, specification and work record, index entry; meets ROUTE-2 and ROUTE-4 as planned.
- Repository facts verified: `packages/elements` is private with `lit` 3.3.1 and workspace deps; `willUpdate` parses `src` so server rendering of cells is reachable; `role="option"`, `aria-label`, roving `tabindex`, Arrow, Enter, Space and `ki-select` all exist; no slot on the host; `docs/spec/components.md` carries the proposed-Lit toolkit wording; GDR-KI-DESIGN-032 and GDR-KI-DESIGN-002 exist; `rumdl` is installed; the ELE ledger reserves `001`.
- Site facts verified at `31d02de8` on `main`: Eleventy 3.1.6 installed under `apps/site`, no `@lit-labs` or `lit` installed, no `apps/site/examples`, no `+/_WORK`, Eleventy input `src`, verifiers read `dist`, `apps/site/tsconfig.json` includes `**/*.mjs` with `allowJs` and no `checkJs`, `tsconfig.tsbuildinfo` untracked, root `@types/node` ^26.
- Runtime and browser facts verified: Bun 1.4.2; mise node 24.22.0 installed and `mise exec node@24.22.0 -- node --version` returns v24.22.0; Chrome 155.0.8059.85; Bun cache holds `playwright-core` 1.64.1 with engines `node >=20` and Chromium 156.0.8078.4 in `browsers.json`; Bun accepts `--experimental-vm-modules` without error. The three Lit Labs pins and `@types/node` 24.10.0 are not in the cache; the record states they were checked by registry metadata, which this offline review could not repeat.

## In Progress

Nothing. The review is complete.

## Queries

### Query 1 — site gates and typecheck under the worktree arrangement

**Context** Boundary permits a runtime-owned linked worktree outside the repository root. A linked worktree carries no `node_modules`, so `bun run ki:site:build`, `bun run self:typecheck` and `bun run test` cannot run there without a root `bun install --frozen-lockfile`, which the plan's "isolated registry installation" grant covers only for the fixture. Running the gates in the primary checkout instead contradicts Verify, which says the fixture's `.mjs` files enter site typecheck and any new diagnostic is a fixture defect.

**Query** Which checkout runs the site gates when the worktree arrangement is selected, and is a frozen-lockfile root install in that worktree inside the grant?

**Options** a) (recommended, confidence high - closes the gap without widening the fixture grant) Append to Boundary paragraph one, after "isolated registry installation.": "Under the worktree arrangement the site gates and typecheck run in that worktree after one `bun install --frozen-lockfile` at its root, which the brief grants separately and which must leave the worktree's `package.json` and `bun.lock` unchanged; under the untracked-fixture arrangement they run in the primary checkout." And in Verify, after "so the fixture and its generated modules also enter site typecheck.", add "Run that typecheck in the checkout that holds the fixture." b) Drop the worktree option from Boundary and keep only the untracked fixture in the primary checkout on `main`. c) Leave as is and rely on the successor brief to resolve it.

### Query 2 — the "evidence note" has no home

**Context** Current state, the HTML assertions and Step 9 write to "the evidence note", but Files touched names only the guide, GDR-KI-DESIGN-012, the spec, the package README and this record. A worker could create an unauthorised file for it, or put run-specific baselines in the guide, which ROUTE-2 reserves for procedure.

**Query** Confirm the evidence note is this record's Review packet.

**Options** a) (recommended, confidence high - matches the work-item format, where Delivered holds baselines and Verification holds outcomes) Add to Files touched paragraph one, after "reproduction commands and matrix.": "The evidence note is this record's `## Review` packet: Delivered records both immutable baselines and the site's full HEAD, and Verification records the matrix, VM diagnostic, glyph and cell counts, input map, gate outcomes and the location of preserved screenshots; the guide holds the reproduction procedure and expected results, never run-specific baselines." b) Define the evidence note as the guide itself and move the site HEAD and baselines out of it. c) Leave undefined.

### Query 3 — the go edit must not read as adopting a route

**Context** Documentation impact says "On go, the committed edit records the evidenced route, limitations and conditions while Lit keeps its _proposed_ status". GDR-KI-DESIGN-012 currently decides only Declarative Shadow DOM server rendering and proposes Lit; direct versus plugin rendering and the Eleventy runtime are not decided anywhere. A worker who writes "the site renders both elements through direct SSR under Bun" into the Decision section settles an unapproved route, and the Goal itself calls the route a recommendation.

**Query** Confirm the go edit states the route as evidenced and proposed, not adopted.

**Options** a) (recommended, confidence medium - keeps the go path committable while leaving adoption to the owner) Replace that sentence with: "On go, the committed edit records the route the evidence supports, its limitations and conditions, carrying the same _proposed_ status as Lit under GDR-KI-DESIGN-002 and stated as what the spike showed rather than as the adopted production route; adopting the route is returned in the run report's Queries with Lit's status." b) Return every go edit to the owner through Queries before commit, like the other outcomes. c) Leave as is.
