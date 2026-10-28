# wow-docs-structure - owner report

## Done

- Commit `6a0cc48` on `main`, pushed fast-forward to `origin/main`; Cloudflare deploy completes after the push.
- Sections `skills`, `ways-of-working`, `knowledge`, `standards` declared in the plan's order with binding files; `verify:docs` accepted the two binding-only sections unchanged (10 sections, 41 pages).
- Pages moved, with 301s for each old address and the eight older `/guidance/` and `/projects/` rules repointed to one hop:
  - `https://knowledgeislands.info/docs/skills/what-a-skill-is/` (was `/docs/ki-agentic-harness/skills/`)
  - `https://knowledgeislands.info/docs/skills/catalogue/` (was `/docs/ki-agentic-harness/skill-catalogue/`)
  - `https://knowledgeislands.info/docs/skills/by-outcome/` (was `/docs/ki-agentic-harness/skills-by-outcome/`)
  - `https://knowledgeislands.info/docs/ways-of-working/roadmap-lifecycle/` (was `/docs/ki-agentic-harness/planning-and-delivery/`)
- Atlas nav is Field Guide, Docs; `https://knowledgeislands.info/docs/` carries the project catalogue below the grid, rendered from `projects.json5` as `/projects/` does.
- `featureAreas.json5` (16 areas, globs written out by name), `verify:features`, `verify:skill-names`, `partials/provided-by.njk` in `layouts/page.njk`, tests for both scripts, guide `docs/guides/developer/feature-areas.md` indexed in the developer README. The sync script comment, the generated catalogue header line and the provenance guide table now name `src/docs/skills/catalogue.md`.
- Retired names fixed where the text was about a skill: `ki-delegate` to `ki-delegation` (prompting index), `ki-mcp` example to `ki-repo-mcp` (naming and locations). Allow-listed with reasons: the six repository names plus `ki-self`, `ki-depends-on`, `ki-chatgpt-capture`, `ki-mcporter`.
- Checks: `ki:site:clean` then `ki:site:build` pass with all eight gates; `bun test scripts` 103 pass; `typecheck` clean; boundaries vitest 15 pass; `ki-repo-website-content` audit PASS; `ki-authoring` audit WARN only (pre-existing `.rumdl.toml` template drift); `ki-engineering` audit FAIL on DEPS-1 only (pre-existing: `@types/node`, `rumdl`, `bun` past the 14-day adoption window; installs are out of scope here), with a pre-existing CI-1 warn.

## In Progress

Nothing. Catalogue refresh is left to the Skills unit as briefed.

## Queries

WOW-DS-1 Multi-page areas. Context: Knowledge bases names two pages and the Standards area names four; the brief's `page` is singular. The script and partial accept a string or a list under `page`. Query: keep `page` as string-or-list, or split into one area per page? Options: a) (recommended, confidence high - no second field, the plan's table maps one area to several pages and the gate already handles both shapes) keep string-or-list; b) split those areas so every area has one page.

WOW-DS-2 Repository standards skill set. Context: the plan writes `ki-repo-*`; I expanded it to the twelve non-kb repo skills, leaving `ki-repo-kb*` to Knowledge bases and Recurring work. Query: should `ki-repo-kb*` also appear under Repository standards? Options: a) (recommended, confidence medium - avoids one skill in three boxes) exclude them; b) include all sixteen.

WOW-DS-3 Allow-list of non-skill names. Options: a) (recommended, confidence high - each is a configuration value or server name a reader types as written) keep `ki-self`, `ki-depends-on`, `ki-chatgpt-capture`, `ki-mcporter`; b) reword those pages instead.

Reply: `ki agent decide ways-of-working "WOW-DS-1 - a; WOW-DS-2 - a; WOW-DS-3 - a"`
