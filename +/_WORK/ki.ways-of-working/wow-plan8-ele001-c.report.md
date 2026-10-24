VERDICT: NOT READY · confidence medium · Steps omit the Playwright setup check and repin window that Dependencies / blocks requires before the matrix, and Step 7 implements `verify-browser.mjs` only after the matrix has run; everything else checks out.

## Required changes

1. **Steps, ordering of the browser setup check (blocking).** Dependencies / blocks says "Before the rendering matrix, implement and run `mise exec node@24.22.0 -- node verify-browser.mjs --setup`" and allows exactly one `playwright-core` repin on that check's result. Steps never list the setup check, and the seventh bullet is the first place `verify-browser.mjs` is implemented, after the matrix bullets. A successor following Steps runs the matrix on a possibly unusable Playwright pin, then repins and reinstalls after the matrix evidence, graph and lockfile digest were captured. Exact edit, in `docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md`:
   - Insert a new bullet immediately after the first Steps bullet:
     `- [ ] Implement the \`--setup\` mode of \`verify-browser.mjs\` and run \`mise exec node@24.22.0 -- node verify-browser.mjs --setup\` against the recorded local Chrome executable, headless, served on loopback, with browser downloads disabled, as Dependencies / blocks specifies; save command, exit status and diagnostics. Apply the single authorised \`playwright-core\` repin only here, before any build or matrix run, and record the final exact pin, resolved graph and lockfile digest afterwards. Stop and escalate if the check still fails.`
   - Change the opening of the seventh bullet from `Implement and run \`verify-html.mjs\` and \`verify-browser.mjs\` against every successful matrix output.` to `Implement \`verify-html.mjs\` and the remaining assertions of \`verify-browser.mjs\`, then run both against every successful matrix output.`
   - In Dependencies / blocks, change `Save the resolved transitive graph and lockfile digest` to `After the setup check and any repin, save the resolved transitive graph and lockfile digest` so the saved evidence is the graph the matrix ran on.

2. **Verify, the `DESIGN-2` label (recommended, not blocking).** `DESIGN-2` is defined nowhere in the repository except `docs/briefs/resume-design-thread.md`, which records it as the dependency-cruiser boundary ruleset on which CI is still red. A successor cannot resolve the label from the record. Exact edit: replace `run DESIGN-2 (\`bun run --cwd packages/boundaries test\`)` with `run the boundaries ruleset (\`bun run --cwd packages/boundaries test\`, currently a known pre-existing failure)`.

# Ways of working › wow-plan8-ele001-c

**🤖 → 👤 Handoff to supervisor · Run report at 09:39 BST**

---

## Done

- Blind read of KI-DESIGN-ELE-001 at d345ecd0 against `ki-plan`, `ki-work-roadmap`, `ki-decision-records` and `ki-guides`; no other review read. Read-only, no commits, no network.
- Ready preflight: `ki repo audit --skill ki-work` PASS; `ki repo audit --skill ki-work-roadmap` PASS with no warning; rumdl on the record clean.
- Record shape: frontmatter, four-word title, `size: l` with Delegation, `kind: investigate`, `component: elements` in vocabulary, every Now section present in order, Documentation impact in the exact four-part shape, Discussion last, task-list Steps; all conform.
- Outcomes: go, conditional go, no-go and blocked are each defined, mutually exclusive and reachable within the spike; the no-go cannot be declared on a setup failure, and site-owned decisions are routed only through Queries.
- Decision Record deliverable: the GDR-KI-DESIGN-012 amendment scope removes the pending-spike line and identifier, sets `date` to the amendment date, keeps the decided-on date in prose, converts the two outside links to prose names, rewrites the forward-work Consequences line and aligns the title to the existing filename; the baseline audit shows exactly those three findings on the record (FILENAME-1, BODY-11 ×2) and the plan clears all of them; the optional additional record rules (type by concern, ADR for architecture, next contiguous serial, filename from title, ordered index entry) match the standard.
- Guide deliverable: `docs/guides/developer/lit-ssr-spike.md` sits in an audience folder with an index entry, and its scope (reproduction procedure, fixture sources, pins, digest, matrix, conclusion) fits ki-guides; the gate must also catch GUIDE-4 and GUIDE-6, which the "no new finding" wording already does. Baseline ki-guides audit carries one pre-existing ROUTE-1 failure on `docs/spec`, outside this record.
- ki-design facts: lit 3.3.1 pinned in `packages/elements`, exports `./src/index.ts`, workspace deps on icons and hexmap, private; lighthouse icon exists; `islandmap/v1` schema name correct; `<ki-hexmap>` has the `src` JSON attribute parsed in `willUpdate` (server-safe), `role="option"` cells with `aria-label`, `ki-select`, roving tabindex, Enter and Space, no slot and no text list, so the spec follow-up finding is true; `docs/spec/components.md` carries the proposed-Lit toolkit wording and the text-equivalent rule; both guide indexes and GDR-KI-DESIGN-032 exist; named root scripts exist.
- Site facts: HEAD 31d02de84d91c89452a1de3dad5c764bc3da11f5 on `main`, clean; Eleventy 3.1.6 at `apps/site/node_modules` with `cmd.cjs`; no lit or Lit Labs packages installed; production input `src`, output `dist`, formats njk/md/html, so the fixture never enters the production build; verify gates read `dist/` only; `apps/site/tsconfig.json` includes `**/*.mjs` with `allowJs` and no `checkJs` as stated; workspaces `apps/*` and `packages/*` exclude the fixture path; no `+/_WORK`.
- Runtimes and pins: Bun 1.4.2; Node 24.22.0 installed under mise and pinned by the site's `mise.toml`; Chrome 155.0.8059.85; Bun accepts `--experimental-vm-modules`; cached playwright-core 1.64.1 declares Node >=20 and Chromium 156.0.8078.4 exactly as recorded; the only other cached version, 1.63.0, targets Chromium 153, so a repin would need the registry grant, consistent with the record's wording.
- Not verifiable offline: the three Lit Labs pins and `@types/node` 24.10.0 are not in the Bun cache; their metadata is taken as recorded.

## In Progress

None.

## Queries

None.
