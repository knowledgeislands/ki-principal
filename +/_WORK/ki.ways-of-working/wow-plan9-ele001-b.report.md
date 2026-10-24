VERDICT: NOT READY · confidence high · a classification gap and an unhandled blocked outcome leave outcomes unreachable or undirected; a go edit settles the route; worktree site gates cannot run offline

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-plan9-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 09:57 BST · last mark 08:24 BST**

---

## Done

- Blind planning review of [KI-DESIGN-ELE-001](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md) at `225af635`, read-only; nothing written in any repository, no install or network call.
- Ready preflight: both offline audits (`KI_REPO_OFFLINE=1`) passed with no warning.
- Repository facts and pins hold: the elements API the fixture relies on (`defineElements()` on import, `ki-glyph` `name`/`size`/`label`, `ki-hexmap` `src` attribute, `role="option"` cells with `aria-label`, roving tabindex, `ki-select` `{q, r, structure}`, Arrow/Enter/Space, no slot); the ki-design pre-commit hook; the site's build, verify and typecheck scripts, `apps/site/tsconfig.json` (`**/*.mjs`, `allowJs`, no `checkJs`), Eleventy 3.1.6; Bun 1.4.2, Node 24.22.0, Chrome 155.0.8059.85, and the cached `playwright-core` 1.64.1 manifest (Node `>=20`, Chromium 156.0.8078.4).
- Step order fits Dependencies and Verify: setup check and single repin come before the matrix, and the build comes before both runtime cases.
- The GDR-KI-DESIGN-012 amendment plan covers the standard's findings I checked (FILENAME-1 title/H1 alignment, the two BODY-11 References links, the forward-work Consequences line, the `date` as amendment date). The guide plan meets `ki-guides` (audience folder, outcome-first opening, self-contained, prose-only record names, index entry).
- Five defects below block or would mislead delivery. Each comes with its exact edit to the record.

## Required changes

1. **Failure classes leave conditional go and no-go unreachable for toolchain faults.** Line 53 defines only setup, runtime and component lifecycle. A diagnosed fault in the pinned Lit SSR, plugin or Eleventy packages that reproduces under both runtimes and that the fixture cannot fix fits none of them. Example: Bun direct fails as runtime; the plugin fails identically under Bun and Node; Node direct passes. That should be conditional go, but line 92 forces blocked.
   - Line 53, after the **Component lifecycle** sentence, insert: "**Toolchain** means a fault in the pinned Lit SSR, Eleventy plugin or Eleventy packages that appears under both runtimes with the identical fixture and that the fixture cannot correct within its grant."
   - Line 92, conditional go: replace "diagnosed as runtime or component lifecycle rather than setup" with "diagnosed as runtime, toolchain or component lifecycle rather than setup".
   - Line 92, no-go: replace "attributed to a runtime or component-lifecycle cause" with "attributed to a runtime, toolchain or component-lifecycle cause".
2. **A go result commits an unapproved rendering route.** Line 127 ("On go, the committed edit records the evidenced route, limitations and conditions while Lit keeps its _proposed_ status") and line 133 commit the route into the owning record and specification without owner approval. Only Lit is held at Proposed, so the route reads as settled under GDR-KI-DESIGN-002.
   - Line 127: replace that sentence with "On go, the committed edit records the evidenced route, limitations and conditions marked _proposed_ under [GDR-KI-DESIGN-002](../decisions/GDR-KI-DESIGN-002-status-labels.md), and Lit keeps its _proposed_ status." Replace the next sentence with "Moving Lit or the route to Agreed needs the owner’s agreement and is returned in the run report’s Queries."
   - Line 133: replace "with the evidenced route and conditions while retaining Lit’s proposed status" with "with the evidenced route and conditions marked _proposed_, retaining Lit’s proposed status".
   - Line 90: replace "a go edit keeps Lit marked proposed" with "a go edit keeps Lit and the evidenced route marked proposed". Line 141: replace "Go preserves Lit’s proposed status" with "Go preserves the proposed status of Lit and the evidenced route".
3. **The site gates cannot run in the linked-worktree option.** Line 32 offers a fresh linked worktree, but line 88 runs `bun run ki:site:build`, `bun run self:typecheck` (`bunx tsc …`) and `bun run test` without naming the checkout. A fresh worktree has no `node_modules/`: Eleventy is missing and `bunx tsc` would fetch from the registry, outside the install grant. The fixture's own install does not install the site root.
   - Line 88, after "with no deploy command.", insert: "Run the site gates in the checkout that holds the fixture. In a disposable linked worktree, first run `bun install --frozen-lockfile` at the worktree root under the successor's isolated-install grant, then confirm with the protected-path checks in Verify that no manifest or lockfile changed; if the grant does not cover that install, select the primary-checkout arrangement."
   - Line 32: after "authorise the bounded local writes and isolated registry installation", add "(for a linked worktree, including the frozen root install named under Repository gates)".
4. **A blocked outcome has no documentation or lifecycle handling.** Line 92 defines blocked, but Steps 10, Documentation impact and Delegation cover only go, conditional go and no-go. Line 36 tells the worker to clean up the fixture after review. A worker could replace the pending-spike wording, write a guide with no success check, remove the fixture or move the record to Awaiting review.
   - Line 92, append: "On blocked, commit no change to GDR-KI-DESIGN-012, `docs/spec/components.md`, `packages/elements/README.md` or the guides; keep the pending-spike wording. Preserve the fixture, every saved cell output and the blocking diagnosis, and return them with a proposed replan in the run report's Queries. Leave this record In progress rather than moving it to Awaiting review; the supervisor decides whether to replan, retry or remove the fixture."
   - Line 36, after "before removing the fixture.", insert: "On a blocked outcome, keep the fixture until the supervisor decides under the decision procedure."
5. **"Evidence note" is undefined, and ki-design-owned follow-ups have no home.** Lines 40, 55 and 84 write to an "evidence note" that no section names, and line 40 writes to it at the In progress transition, before the guide exists. Line 133 says to "Record separately" the missing text equivalent in the v0 element, and line 141 says a go "identifies separately planned follow-up". But the guide may hold no forward work (line 137), the Decision Record must stay present-state, and site follow-ups alone have a route.
   - Line 40: replace "in the evidence note" with "in `docs/guides/developer/lit-ssr-spike.md` (the evidence note), drafted uncommitted from the In progress transition". Lines 55 and 84: replace "the evidence note" with "`docs/guides/developer/lit-ssr-spike.md`".
   - Line 133: replace "Record separately that" with "Return in the run report's Queries, for the supervisor to capture under `ki-next`, the finding that". Then replace "This is a follow-up finding under Documentation impact" with "This follow-up finding is".
   - Line 55: replace "and identify receiver-owned follow-up work" with "and return receiver-owned follow-up work, including ki-design-owned follow-ups, only in the run report's Queries for supervisor capture under `ki-next`, never in the guide, Decision Record or specification".

## In Progress

Nothing is running.

**Outstanding - no action requested now**

- The registry metadata for the Lit Labs pins and for `@types/node` 24.10.0 was not re-verified, because this run was offline. The record's 22 October registry evidence stands unchallenged but unconfirmed.
- The ki-design boundaries gate's "known pre-existing failure" was taken from the record as stated. It was not run, to stay read-only.

## Queries

No outstanding queries. The supervisor applies the five edits and re-dispatches the planning gate.

### 🤖 → 👤 Handoff to supervisor · since 08:24 BST

1 run reported · 0 queries · 5 required changes

- wow-plan9-ele001-b: KI-DESIGN-ELE-001 NOT READY (high); 5 plan edits required before the three-reviewer gate.

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
