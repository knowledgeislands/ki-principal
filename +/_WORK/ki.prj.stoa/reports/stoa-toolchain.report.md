# [Foundations](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/foundations.md) › [Stoa](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/stoa.md) › stoa-toolchain

**🤖 → 👤 Handoff to supervisor · Run report at 05:17 GMT · last mark 05:17 GMT**

---

## Done

- This run was authorised by the decision "STOA-AUDIT-REST b) - everything is Stoa, house conventions throughout" of 7 November 2026. It started from `stoa-names`' work on `main`, which had left no blocking query and no failing check.
- `ki-engineering` failures went from 18 to none. What is left is two warnings, explained under Findings, and the 8 GitHub settings failures that belong to the `stoa-github` run. Nothing new fails.
- Commit `2964479` renames the Calendar feed assets probe from `feed-assets.mjs` to `feed-assets.js`. It still runs under Node, and its syntax checks. Its test is skipped on this machine, as it was before, because no Wrangler 4.151.3 is installed here.
- Commit `7a90989` adds the canonical commit hooks, byte-identical to the house copies, and the house `commitlint.config.ts`.
- Commit `5da3fb0`, marked breaking, does the rest:
  - It adds the house development tools, one `bun add -d` each, at the versions the sibling repositories pin: Commitlint, knip, rumdl, lint-staged, Syncpack, Turborepo, dependency-cruiser and `@types/node`. It also raises Biome to 2.6.3 and `@types/bun` to 1.4.4. Vitest goes into the new boundary workspace.
  - It moves Bun to 1.4.4, which was already installed, and sets `engines.node >=22`.
  - Turborepo now runs each workspace's `test` and `typecheck`, and every workspace has its own `tsconfig.json`.
  - It adds the knip, lint-staged and Turborepo configuration and puts `biome.json` on the shared settings.
  - `.dependency-cruiser.ts` states the unit boundaries: no cycles, no unresolved imports, no package and no Node or Bun built-in in a unit, and no unit importing the tooling, tests, workbench or checks. The new `packages/boundaries` workspace proves each rule against an isolated checker in `tooling/depcruise`.
  - It renames the scripts and updates every caller: `AGENTS.md`, both READMEs and `serve.js`. There is no CI or Workers configuration. `CLAUDE.md` names no commands.
  - It adds one non-breaking line under `## Unreleased` in `CHANGELOG.md`.
- The script names are now `test`, `self:typecheck`, `self:lint`, `self:workbench` and `self:workbench:export`, plus the house `clean`, `prepare` and `ki:deps:update`. No site calls the old names: a read-only search found them only in vendored README copies.
- Checks: `bun run test` passes in all 3 workspaces (252 unit tests, the workbench tests and 9 boundary tests). `bun run self:typecheck` passes. `bun run self:lint` passes, with 10 warnings: the 8 from before and 2 new Biome 2.6 hints in `calendar/element.js`. knip finds nothing. Syncpack finds nothing. Each of the three commits ran the new hooks cleanly. `git status` is clean, and `main` is level with `origin`.
- `apps/workbench/export.js` still uses only relative paths. Its test passes.
- `consumers.json5` is unchanged. No release was cut, and the version is unchanged.

## In Progress

- Candidate for a roadmap record, not created: type the workbench. It was never type-checked, and about 60 errors show once checking is on. Most are untyped parameters in `stories.js`, plus a few in the test fixtures it imports. Its `tsconfig.json` therefore checks only that its modules parse, and says why.
- Candidate for a roadmap record, not created: the closed roadmap record `STOA-CMD-001` still names `bun run typecheck` and `bun run lint` in its acceptance checks. I left it alone because it records what was checked at the time.

## Findings

### STOA-TOOLCHAIN - How the house engineering convention fits a plain-JavaScript package repository

**Goal:** Give the package-repository skill the guild is writing each place where Stoa applied `ki-engineering`'s intent rather than its TypeScript letter.

**Scope:** `packages-stoa` as of commit `5da3fb0`, against `ki-engineering`'s audit and the sibling repositories `ki-design`, `tools-ki` and `apps-knowledgeislands.info`.

**As of:** 7 November 2026, 05:17 GMT.

- Units and tests stay plain JavaScript checked by `tsc --checkJs`. Each workspace `tsconfig.json` sets `allowJs` and `checkJs` and keeps the house invariants. Only the two tool configurations whose names the convention fixes, `commitlint.config.ts` and `.dependency-cruiser.ts`, are TypeScript. The root `tsconfig.json` checks just those two.
- The `.mjs` rule was met by renaming to `.js`, not by porting to TypeScript. The probe has to run under Node beside Wrangler's own engine, and the package declares `"type": "module"`.
- `packages/stoa/tsconfig.json` stands alone and does not extend the root, because sites vendor that folder and an `extends` would resolve to the site's own root.
- The boundary proof `packages/boundaries/src/boundaries.test.js` is JavaScript with JSDoc, run by `vitest run` as the audit requires. Its rules come from `AGENTS.md`'s "no runtime dependency" and from units running in the browser.
- The workbench's `tsconfig.json` sets `checkJs: false`, so it proves only that its modules parse. `rootDirs` maps the `./stoa/` paths that the server and export resolve onto `packages/stoa`.
- `self:lint` is kept although the sibling repositories have no lint script, because this brief and `AGENTS.md` name one. The audit runs Biome as well.
- Warning `TURBO-2` wants a `build` for the workbench. It has none on purpose, because it writes output only when someone runs export with a folder they choose.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · at 05:17 GMT

🤖 0 running · 👤 0 with you

- [done] stoa-toolchain · supervisor · since 05:17 GMT

🧵 ki.prj.stoa
