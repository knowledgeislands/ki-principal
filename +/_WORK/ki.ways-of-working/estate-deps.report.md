# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › estate-deps

**🤖 → 👤 Handoff to supervisor · Run report at 18:56 BST · last mark 18:12 BST**

---

## Done

RUMDL-ESTATE a) and DEPS-LATEST are complete. Every in-scope repository moved to the latest dependencies and rumdl `^0.3.0`, each through its own gate, and each was pushed fast-forward. After that, the harness template switched MD005 and MD075 back on and adopted `--preflight`. Nothing was published. The net record count is 0 in every repository.

Each repository below got "chore(deps): update dependencies to latest and rumdl to ^0.3.0" unless another commit is noted.

- **mcp-git-audit:** `26f661e`, then `c06a647` "chore(deps): align the boundary checker with the root dependency-cruiser". The `tooling/boundaries` install root had drifted from the root's dependency-cruiser.
- **mcp-gsuite:** `5037a36`, then the same alignment commit as `2deda35`.
- **mcp-housekeeping-claude:** `4691ab7`, then the same alignment commit as `05f10e5`.
- **mcp-acquire-whatsapp:** `bc881b6`.
- **mcp-housekeeping-chatgpt:** `9813b99`.
- **mcp-ki-kb-fs:** `14fd29c`.
- **mcp-ki-kb-notion-mirror:** `c2c0192`.
- **mcp-m365:** `8791e72`.
- **tools-ki:** `47bb069f` and `6864a9a8`.
  - `47bb069f` "docs(roadmap): separate the per-host evidence note in [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md)". rumdl 0.3.0's MD013 reflow had started joining a lazy continuation line into the list item above it. A blank line fixes it.
  - `6864a9a8` is the dependency update.
- **tools-git-almanac:** `2bbc015`.
- **tools-techne:** `044846a`.
- **ki-techne-harness:** `3f74971`.
- **apps-observatory.local:** `75af834`. Mermaid stays at its 12.1.0 pin: 12.2.0 fails the third-party notices test, because `THIRD-PARTY-NOTICES.md` records 12.1.0.
- **hnr-agentic-harness:** `143daa7`.
- **5g-emerge-apex:** `7413952`.
- **5g-emerge-demos:** `ac312b4`, then `d91e740` "fix(deps): restore internal and vendored package references".
  - The recursive update had rewritten the internal and vendored references to `latest`. The fix restores them, and the frozen install and the gate are both green.
  - The update first needed the documented `bun run self:vendor:clone`, at the production pin.
- **5g-emerge-phase2:** `4d579ce` and `6963bc6`.
  - `4d579ce` "docs(site): rejoin a wrapped correction note in the global test register" fixes rumdl 0.3.0's MD018 report on a blockquote continuation line beginning `#1)`.
  - `6963bc6` is the dependency update.
- **5g-emerge-phase3:** `9884fe1`.
- **5g-emerge-testbed:** `789f38a`.
- **infoschematics:** `8a111e8`.
  - Workspace-internal references are kept.
  - `@types/node` stays on the Node 22 line under [GDR-INFOSCHEMATICS-004](/Users/krisbrown/workspaces/humans-not-robots/infoschematics/docs/decisions/GDR-INFOSCHEMATICS-004-promise-the-oldest-supported-node-line.md).
  - Playwright 1.64 needed its headless Chromium shell, so I downloaded it into the user's Playwright cache.
  - The build and self-check failed at baseline (exit 127) and pass now.
- **apps-midnight.ninja:** `84ad475`.
- **apps-rig.midnight.ninja:** `700ffa2`.
- **apps-tower.midnight.ninja:** `b7b29ef`.
- **apps-markhowarth.com:** `1cb454c`.
- **apps-vallearmonia.com:** `3a5e5db`.
  - Vitest and `@vitest/coverage-v8` stay at `^4.1.12`. `@cloudflare/vitest-pool-workers` 0.23.0 requires Vitest `^4.1.0`, and Vitest 5 breaks the Workers pool.
  - happy-dom stays at `^20.14.6`, because 21 fails 15 tests in the sanctuary site-logo suite.
- **ki-principal:** `ec8d86a`.
  - Another session's commit `898df10` "docs(model): show Kris as 👤 and other targets as 🎯 (GLYPH-OWNER)" was stacked beneath it and went with the push.
  - Other sessions' dirty and staged files were left untouched. They include `+/_WORK/ki.chezmoi/decisions.md`, staged deletions under `+/_WORK/ki.ways-of-working/` and `+/_WORK/ki/`, and modified and untracked reports.
- **legal-principal:** `50660b00`.
  - This repository runs npm, so I used its own `npx npm-check-updates -u` and `npm install` rather than `bun install`. `--no-workspaces` was needed because its `.ncurc.cjs` sets `workspaces: true` without a workspaces field.
  - The config's reject list was honoured; TypeScript is already at the latest, 7.0.2.
  - `package.json` and `package-lock.json` were committed.
- **ki-agentic-harness:** `fda24ea2` "feat(ki-authoring): re-enable MD005 and MD075 and adopt rumdl --preflight".
  - MD005 and MD075 leave the `disable` list in `.rumdl.toml` and in its canonical template. Their 0.2.54 comments are gone.
  - The CONFORM command, the harness `lint-staged` and the `ki-engineering` scaffold's `lint-staged` default become `rumdl check --fix --preflight`.
  - The template test now asserts that both rules are enabled.
  - `standards-authoring.md` and `sources.md` record the move, the re-enable and the two new 0.3.0 findings.
  - Results: tests 1255 pass, TypeScript clean, `ki-authoring` and `ki-skills` audits pass. The `ki-engineering` audit has only the known pre-existing SCR-11 hook-binding failure.
  - GitHub reported its usual bypass of the pull-request rule for this direct-to-`main` repository.
- **Failures that predate this run:** each failed at both baseline and after, so none is a regression from this run.
  - tools-ki: the manual and changelog inventory test.
  - ki-techne-harness: TypeScript TS18003 (no inputs).
  - 5g-emerge-phase2: Biome, 2 errors.
  - apps-rig.midnight.ninja: Biome.
  - apps-tower.midnight.ninja: tests.
  - apps-vallearmonia.com: typecheck, 101 errors.
  - ki-principal: rumdl, 11 findings, all in other sessions' uncommitted reports.
  - legal-principal: rumdl, 68 findings, the same set before and after.
- **Not updated:**
  - hnr-principal: its `package.json` declares no dependencies.
  - techmedix apps-yorkphotosoc.org: a yarn and turbo toolchain with no rumdl, outside the house Bun toolchain.
  - hnr-backend, hnr-frontend, kw-website and paperclip: they carry no `.ki.toml`, so they are not KI-managed.
  - apps-knowledgeislands.info and ki-design: excluded by the brief. Both still pin rumdl `^0.2.78`.
- **Glyph:** this report shows Kris as 👤 under GLYPH-OWNER (`898df10`), in place of the 🧑 the brief's form line used.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Under PKG-6, the `ki-engineering` audit still accepts plain `rumdl check --fix` in a consumer's `lint-staged`. Consumers pick up `--preflight` when they next conform; they are not forced to.
- 5g-emerge-demos `self:vendor:check` reports that its vendored dev-server state needs a refresh. This is local state, not a gate.
- The failures listed under Done that predate this run belong to their own repositories' work, not this run.

## Queries

### RUMDL-EXCLUDED - Website and ki-design on rumdl 0.2.78

**Context:** apps-knowledgeislands.info and ki-design still pin rumdl `^0.2.78`, which rejects `--preflight` with exit 2. The house template now requests `rumdl check --fix --preflight`, so a conform run in either would propose a command that fails there.

**Query:** Should each of the two move to rumdl `^0.3.0` and the latest dependencies once its current work allows, through its own gate?

**Options:**

a) (recommended, confidence medium - the move was clean in 27 repositories, but neither of these has been gated on 0.3.0) Move each one when Claude Design's work in it finishes, as one run per repository through its own gate.

b) Leave both on 0.2.78 for now, and skip the house formatting conform in them until they move.

### DEPS-HOLDS - Upstream-blocked holds

**Context:** Four updates are held below latest:

- observatory: Mermaid stays at 12.1.0, because the notices file records that version.
- infoschematics: `@types/node` stays on the Node 22 line, by its own decision record.
- vallearmonia: Vitest stays on 4.x, until `@cloudflare/vitest-pool-workers` supports 5.
- vallearmonia: happy-dom stays on 20.x, because 21 fails 15 site-logo tests.

**Query:** Should the observatory Mermaid and vallearmonia happy-dom holds be cleared by follow-up work in those repositories, with the other two left as they are?

**Options:**

a) (recommended, confidence medium - both are local fixes, while the other two are a deliberate policy and an upstream dependency) Raise one roadmap item in each repository: in observatory, refresh its notices to Mermaid 12.2.0; in vallearmonia, adapt the site-logo tests to happy-dom 21. Revisit the Vitest hold when the Workers pool supports Vitest 5.

b) Keep all four holds until the next estate dependency run.

### 🤖 → 👤 Handoff to supervisor · since 18:56 BST

👤 2 with you

- [with you] RUMDL-EXCLUDED · owner · since 18:56
- [with you] DEPS-HOLDS · owner · since 18:56
- [committed] 28 repositories, pushed
