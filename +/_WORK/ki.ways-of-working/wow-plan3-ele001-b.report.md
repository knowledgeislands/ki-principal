# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan3-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 03:13 BST · last mark 02:12 BST**

---

## Done

VERDICT: NOT READY · confidence high · the plan is now close to Ready and meets nearly every earlier required change, but three verified defects would let an unattended run reach a wrong or unauthorised result: the map text-equivalent assertion, the site handoff destination and the Node version actually invoked.

This was a blind, read-only review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at ki-design `c813003`. I checked it against the `ki-work-roadmap` [work-item format](/Users/krisbrown/workspaces/knowledge-islands/ki-design/.agents/skills/ki-work-roadmap/references/standards-work-item-format.md), ki-design `AGENTS.md`, the elements source, the [components](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/components.md) and [maps](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/maps.md) specifications, and the site checkout at `31d02de`. I made no edits, commits, installs or remote calls.

### Required amendments

1. **Say where the map's text equivalent comes from.** The current wording means an unchanged element fails on every path. Verify asserts that "the map's text equivalent names the fixture's cells", and in the no-JavaScript browser check that "the map's text equivalent is readable". The [components spec](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/spec/components.md:30) says `<ki-hexmap>` always renders a text equivalent. The v0 element does not: [`hexmap.ts` `render()`](/Users/krisbrown/workspaces/knowledge-islands/ki-design/packages/elements/src/hexmap.ts:216) emits only SVG with per-cell `aria-label`s, and it has no `<slot>`. So light-DOM text inside the host is hidden by the declarative shadow root. Read naturally, the assertion fails under all four runtime-and-path combinations, for a reason that has nothing to do with SSR or the runtime. The record forbids package-source edits, so the result would be "record the defect and replan" rather than a valid go or no-go.
   - **Amendment:** in the fourth Step and in Verify, say that the fixture page writes the text equivalent as its own list outside and next to `<ki-hexmap>`, as [GDR-KI-DESIGN-032](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/decisions/GDR-KI-DESIGN-032-living-map-without-javascript.md) does for the Living Map.
   - The SSR assertion for the map then becomes: the shadow root contains the expected number of `role="option"` cells, and their `aria-label`s name the fixture's cells.
   - Record, as a separate spike finding that does not decide the matrix, that the v0 element does not render the text equivalent the components specification says it does. That gap is a follow-up under Documentation impact, not a spike failure.

2. **Name the destination for the site handoff, or return the line instead of writing it.** The record routes a site-owned runtime decision "to the site's work `messages.md`". No such file exists: `apps-knowledgeislands.info` has no `+/_WORK/`. Work packages live in `ki-principal/+/_WORK/<id>/`, and no work package there visibly owns the site. Writing there would touch a third repository, but the Boundary covers only ki-design and the site.
   - **Amendment:** in the last Step, Files touched, Documentation impact › Decision Records and Roadmap, and Delegation, replace "route … to the site's work `messages.md`" with this: the run returns the proposed message line in its report, and the supervisor posts it to the work that owns the site. Alternatively, name the exact `ki-principal/+/_WORK/<id>/messages.md` path and add it to the Boundary and to the successor brief's write grant.

3. **Run and record the Node version the comparison claims.** The record pins Node 24.22.0 and runs bare `node …` commands. In a non-interactive agent shell, `node` resolves to the mise global, 24.21.0, even inside the site checkout. The site's `mise.toml` `lts` resolves to 24.22.0 only when mise is activated. An unattended run would compare against 24.21.0 and report 24.22.0.
   - **Amendment:** in the first Step, add "record `bun --version`, and `node --version` as invoked, and stop on a mismatch with the pins".
   - In Verify, invoke Node through mise for every Node command, including both verifiers, for example `mise exec node@24.22.0 -- node node_modules/@11ty/eleventy/cmd.cjs …`. Record the reported version beside each matrix cell.

### Recommended, not blocking

4. Say whether the site fixture sources are ever committed on `spike/ki-design-ele-001`.
   - If they stay untracked, as the reproducibility homing in ki-design implies, the branch adds a checkout switch in a shared primary checkout for no benefit. That checkout also holds KI-WEBSITE-SITE-044, which is `awaiting-review`. Prefer leaving the site on its current HEAD with the fixture untracked, or a runtime-owned worktree.
   - If they are committed, the site's lint-staged Biome run covers `apps/**` and applies to them.

5. Note that the site's [`apps/site/tsconfig.json`](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info/apps/site/tsconfig.json) includes `**/*.mjs` with `allowJs`. Repeating `self:typecheck` with the fixture present therefore takes in the fixture, `generated/` and `out/` scripts. Record any fixture-caused diagnostic as fixture-caused, or run the closing site gates after cleaning `generated/` and `out/`.

6. After the fixture install, check that both repositories' root `package.json` and `bun.lock` and `apps/site/package.json` are unchanged (for example `git diff --quiet -- …`), so that "do not change either repository's root manifest or lockfile" can be checked as well as instructed. The precedent of `tooling/depcruise` with its own lockfile supports the isolation.

7. In the browser verifier, block and fail any request that is not to loopback. This turns "the components make no network calls" into an assertion rather than an assumption.

8. In the Delegation section, name the supervisor's final review of the returned evidence: re-running both verifiers on at least one output before Awaiting review. At the Ready transition, rewrite the planning-gate sentences in Delegation and Roadmap ("After this amendment…", "stays Draft until the three-reviewer gate is met"), which will be stale by then.

### Earlier required changes

- **[wow-plan-ele001-a](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-a.report.md):**
  - Items 1, 2, 4 and 5 are met.
  - Item 3 is met in substance; amendments 1 and 3 above close its remaining gaps.
- **[wow-plan-ele001-b](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-b.report.md):**
  - Items 2, 3, 5, 6 and 7 are met.
  - Item 1 is met through option b (a site branch, size `l`, a Delegation section), except for the handoff destination in amendment 2.
  - Item 4 is met except for enforcing the Node pin, amendment 3.
  - Item 8, the three-reviewer gate, is in progress.
- **[wow-plan-ele001-c](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-plan-ele001-c.report.md):**
  - Items 1 to 8 are met.
  - Item 3 places the install in the fixture rather than in `apps/site`. That is a reasoned reconciliation recorded in Discussion, and I accept it.
  - Item 6's handoff home is affected by amendment 2.

### Checks

- Shape check: PASS. Frontmatter, the four-word title, `kind: investigate`, `purpose: learning`, `component: elements` (declared in `.ki.toml`), size `l` with a Delegation section, unchecked Steps, and the full Documentation impact shape are all in place.
- Readiness check: FAIL on amendments 1 to 3. Everything else is concrete and checkable.
- Fact check: PASS on the site HEAD `31d02de…`, Eleventy 3.1.6 installed in `apps/site`, no `@lit-labs` packages present, Bun 1.4.2, Chrome 155.0.8059.85 installed, the elements' `src` attribute, `ki-select`, roving tabindex and Enter/Space handling, the `packages/boundaries` test script, the ki-design and site gate scripts, and the site verify scripts reading only `dist/` and `src/_data`.
- Fact check: FAIL on `node` resolving to 24.21.0, and on the site work `messages.md` being absent.
- Registry pins: NOT RUN. Remote calls were forbidden, so the planner's registry evidence is unconfirmed by me.
- Repository integrity: PASS. Both checkouts were left untouched.

## In Progress

Nothing is running. [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) stays `draft`. The supervisor owns the amendments and the re-review gate.

## Queries

### [ELE001-HANDOFF - Where the site runtime proposal goes](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md)

**Context:** The record sends any Node-runtime or alternative proposal to "the site's work `messages.md`". The site repository has no work folder, and no `ki-principal/+/_WORK/` package visibly owns the site.

**Query:** Should the spike write the handoff line itself, or return it for the supervisor to route?

**Options:**

a) (recommended, confidence high - keeps the run inside its two-repository boundary and leaves routing with the owner of the work map) The run returns the proposed message line in its report, and the supervisor posts it to the owning work's `messages.md`.

b) Name the exact `ki-principal/+/_WORK/<id>/messages.md` in the record, and add ki-principal to the Boundary and to the successor brief's write grant.

### 🤖 → 👤 Handoff to supervisor · since 03:13 BST

🤖 0 running · 👤 1 you · ⛔ 0 blocked

- [handoff] NOT READY verdict, three required amendments and the handoff-routing query for [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) · supervisor · since 03:13 BST
