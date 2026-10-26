# wow-rel-0141 - ship ki v0.14.1 and turn the fleet green

## Goal

Publish ki v0.14.1 and move the fleet onto it, so the twelve repositories and the website that fail DESIGN-2 alone go green. Kris decided this on 26 October under REL-MACOS-OOM, TOOLSKI-DEPCRUISE and WEB-BUILD-ORDER (see the three entries at the end of `+/_WORK/ki.ways-of-working/decisions.md` in ki-principal).

## Background to read first

- `+/_WORK/ki.ways-of-working/wow-ki-pin-release.report.md` and `wow-review-rel.report.md`: the failed v0.14.0 release (run 40192625875), its cause and the release steps.
- `+/_WORK/ki.ways-of-working/wow-fleet-green.report.md`: which repositories fail DESIGN-2 alone and how their pins are set.
- tools-ki's release guide and `.github/workflows/release.yml`.

## Scope, in order

1. **tools-ki memory fix.** On tools-ki main, cut `src/tests/cli/agent-control.test.ts`'s memory footprint: split the file or free fixtures and retained state between groups, whichever the evidence supports. Give the package job's test step in `release.yml` a `NODE_OPTIONS=--max-old-space-size` ceiling matched to the runner. All three package jobs must still run the full suite before publishing; do not weaken the gate.
2. **Checker-root rename (TOOLSKI-DEPCRUISE).** Rename tools-ki's `tooling/boundaries` to `tooling/depcruise` everywhere it is named: `ci.yml`, `src/core/agent/worktrees.ts` (about line 47), `src/tests/cli/agent-worktrees.test.ts` (about line 61), `package.json` and the boundary tests. It may land in the same release commit set.
3. **Release.** Verify locally (tests, typecheck, `ki repo audit`), push fast-forward, wait for tools-ki main CI green, then tag `v0.14.1` and run the Release workflow. Watch every job. Leave `v0.14.0` unpublished and its tag untouched. Confirm the tap and the release fan-out to consumers.
4. **tools-ki's own pin.** Once v0.14.1 installs, bump tools-ki's own `KI_VERSION` to v0.14.1 and confirm its CI is green.
5. **Fleet pins.** Bump `KI_VERSION` to v0.14.1 in each repository wow-fleet-green left red on DESIGN-2 alone, and in the website `apps-knowledgeislands.info`. In the website's commit, also move `bun run ki:site:build` before `bun run test` in `.github/workflows/ci.yml` (WEB-BUILD-ORDER). Watch each CI run and the website's Cloudflare deploy.

## Limits

- Standing push rule: commit by explicit path, push fast-forward only, never force, never `--no-verify`, never move a published tag. Stop on divergence.
- No new software; upgrading what is already installed is fine. No DNS, Cloudflare Access, routes, Zero Trust or credential changes. No messaging to people, and no changes in Linear or Notion.
- If a step fails for a cause other than the ones above, stop that step and raise a query with Context, Query and lettered Options, the recommendation first with its confidence; do not widen scope to fix it. Carry on with independent steps where safe.
- Never remove your own scratch directory with `rm`; leave it for `ki agent close`.

## Report

Owner report: Done (each repository with its CI result and link), In Progress, Queries. Name any repository still red and why.
