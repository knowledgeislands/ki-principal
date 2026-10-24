# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-depcruise

**🤖 → 👤 Handoff to supervisor · Run report at 02:31 BST · last mark 02:12 BST**

---

## Done

- DEPCRUISE-PATH delivered in `db5e3cff`: the engineering skill, DESIGN-2 checker and prepare validation, prepare conform detection, fixtures, generated rubric and guidance now use `tooling/depcruise`; the exact ten intended paths were verified after the hook-backed commit.
- Verification: `bun run test` passed (1,414 tests); `bunx tsc --noEmit` passed; focused engineering audit passed; skills audit passed with 2 warnings; harness audit passed with 16 warnings; authoring audit passed; diagrams audit passed with 12 warnings; pre-commit and commit-message hooks passed.
- Nonblocking findings are diagram freshness, overdue source reviews, the existing roadmap size migration window and the isolated audit registry lacking the principal checkout. No failing criterion remained; no unrelated repairs were made.
- Delivery: the checked commit was fast-forwarded into the designated primary checkout on local `main`; committed paths and working files match. The temporary worktree and branch were removed. No roadmap record was created, accepted or pruned; this direct instruction is ready for coordinator review.

### Migration method

The read-only census covered every repository returned by the local KI registry. Twenty-four have tracked files under the old install root: fourteen in the Knowledge Islands territory and ten elsewhere in the registered estate. No downstream repository was changed.

For each repository below, its next exclusive writer should move the tracked `tooling/boundaries` install root to `tooling/depcruise`, retain the lockfile, and update only references to that install path in the listed operational files. Keep product boundary packages and boundary-test filenames named as they are. Update current guidance that still gives the old install command; preserve historical changelog and evidence references.

`ki repo conform --skill ki-engineering --dry-run` can propose the canonical prepare command after the new root exists; review and apply that bounded proposal, then install the isolated checker from its retained lockfile and run the repository’s full gates and DESIGN-2 audit. Conform does not move this directory or rewrite custom test, CI, graph or cache paths: DESIGN-2 remediation is diagnostic. The move and those reference edits need repository-owned work.

### Knowledge Islands repositories

- [apps-knowledgeislands.info](/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info): migrate by the shared method; update `.dependency-cruiser.ts`, `AGENTS.md`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`. Update the graph configuration and boundary package’s Turbo inputs as well.
- [apps-observatory.local](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local): migrate by the shared method; update `.dependency-cruiser.ts`, `.github/workflows/ci.yml`, `docs/guides/developer/workspace-layout.md`, `docs/specs/boundary.md`, `knip.json`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `turbo.json`. Also update CI, Knip and root Turbo inputs, graph configuration, workspace guide and boundary specification; preserve CHANGELOG history.
- [ki-design](/Users/krisbrown/workspaces/knowledge-islands/ki-design): migrate by the shared method; update `package.json`, `packages/boundaries/src/boundaries.test.ts`. The prepare command and boundary package test are the only tracked old-path references.
- [mcp-acquire-whatsapp](/Users/krisbrown/workspaces/knowledge-islands/mcp-acquire-whatsapp): migrate by the shared method; update `.dependency-cruiser.ts`, `.github/workflows/ci.yml`, `CONTRIBUTING.md`, `package.json`, `scripts/boundaries.ts`, `src/tests/boundaries.test.ts`. Also update graph configuration and the checker wrapper in `scripts/boundaries.ts`.
- [mcp-git-audit](/Users/krisbrown/workspaces/knowledge-islands/mcp-git-audit): migrate by the shared method; update `.github/workflows/ci.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `src/boundaries.test.ts`.
- [mcp-gsuite](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite): migrate by the shared method; update `.github/workflows/ci.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `src/boundaries.test.ts`.
- [mcp-housekeeping-chatgpt](/Users/krisbrown/workspaces/knowledge-islands/mcp-housekeeping-chatgpt): migrate by the shared method; update `.github/workflows/ci.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `src/boundaries.test.ts`.
- [mcp-housekeeping-claude](/Users/krisbrown/workspaces/knowledge-islands/mcp-housekeeping-claude): migrate by the shared method; update `.github/workflows/ci.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `src/boundaries.test.ts`.
- [mcp-ki-kb-fs](/Users/krisbrown/workspaces/knowledge-islands/mcp-ki-kb-fs): migrate by the shared method; update `.github/workflows/ci.yml`, `CONTRIBUTING.md`, `docs/guides/developer/working-on-the-code.md`, `package.json`, `src/boundaries.test.ts`. Also update the developer guide.
- [mcp-ki-kb-notion-mirror](/Users/krisbrown/workspaces/knowledge-islands/mcp-ki-kb-notion-mirror): migrate by the shared method; update `.github/workflows/ci.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `src/boundaries.test.ts`.
- [mcp-m365](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365): migrate by the shared method; update `.github/workflows/ci.yml`, `AGENTS.md`, `CONTRIBUTING.md`, `package.json`, `src/boundaries.test.ts`.
- [tools-git-almanac](/Users/krisbrown/workspaces/knowledge-islands/tools-git-almanac): migrate by the shared method; update `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `docs/guides/developer/definition-of-done.md`, `docs/guides/developer/local-development.md`, `package.json`, `scripts/boundaries.ts`, `src/tests/boundaries.test.ts`. Also update the checker wrapper, both CI/release workflows and current developer guidance.
- [tools-ki](/Users/krisbrown/workspaces/knowledge-islands/tools-ki): migrate by the shared method; update `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `docs/guides/developer/definition-of-done.md`, `package.json`, `src/core/agent/worktrees.ts`, `src/tests/boundaries.test.ts`, `src/tests/cli/agent-worktrees.test.ts`, `src/tests/cli/repo/hooks.test.ts`. Also update `src/core/agent/worktrees.ts` and its worktree/hook fixtures, so new worktrees provision the renamed root; update both CI/release workflows and current developer guidance.
- [tools-techne](/Users/krisbrown/workspaces/knowledge-islands/tools-techne): migrate by the shared method; update `.github/workflows/ci.yml`, `.github/workflows/release.yml`, `docs/guides/developer/README.md`, `docs/guides/developer/definition-of-done.md`, `package.json`, `src/tests/boundaries.test.ts`. Also update both CI/release workflows and current developer guidance.

### Other registered KI repositories

These also carry `.ki.toml` and the old tracked install root, so they are included for completeness; their owners retain migration authority.

- [5g-emerge-apex](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-apex): migrate by the shared method; update `AGENTS.md`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`.
- [5g-emerge-demos](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-demos): migrate by the shared method; update `AGENTS.md`, `apps/site/src/tests/boundaries.test.ts`, `package.json`.
- [5g-emerge-phase2](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase2): migrate by the shared method; update `AGENTS.md`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`.
- [5g-emerge-phase3](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-phase3): migrate by the shared method; update `AGENTS.md`, `biome.json`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`.
- [5g-emerge-testbed](/Users/krisbrown/workspaces/humans-not-robots/5g-emerge-testbed): migrate by the shared method; update `AGENTS.md`, `biome.json`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`.
- [apps-markhowarth.com](/Users/krisbrown/workspaces/valle-armonia/apps-markhowarth.com): migrate by the shared method; update `apps/site/scripts/boundaries.test.ts`, `package.json`.
- [apps-midnight.ninja](/Users/krisbrown/workspaces/personal/apps-midnight.ninja): migrate by the shared method; update `AGENTS.md`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`.
- [apps-rig.midnight.ninja](/Users/krisbrown/workspaces/personal/apps-rig.midnight.ninja): migrate by the shared method; update `AGENTS.md`, `package.json`, `packages/boundaries/src/boundaries.test.ts`, `packages/boundaries/turbo.json`.
- [apps-vallearmonia.com](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com): migrate by the shared method; update `package.json`, `site/scripts/boundaries.test.ts`.
- [infoschematics](/Users/krisbrown/workspaces/humans-not-robots/infoschematics): migrate by the shared method; update `.dependency-cruiser.ts`, `.github/workflows/ci.yml`, `AGENTS.md`, `README.md`, `apps/site/src/boundaries.test.ts`, `docs/decisions/references/design-architecture.md`, `package.json`, `scripts/boundaries.ts`, `scripts/dependency-boundaries.test.ts`, `turbo.json`.

### References without an old tracked install root

- [ki-agentic-harness](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness): the shared contract is corrected by this delivery; it has no repository-local isolated checker folder to move.
- [ki-principal](/Users/krisbrown/workspaces/knowledge-islands/ki-principal): only the hooks design note and this work’s decisions log mention the old path. No install migration; retain the decisions log’s historical wording and refresh the design note when its owner next edits it.
- [apps-tower.midnight.ninja](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja): the tracked root is already renamed, as reported in `32c99fa`; an old untracked directory and a retention-evidence reference remain. No tracked folder migration is needed. Do not delete either tonight. Tower was not re-audited by this run.

## In Progress

Nothing is running. Outstanding: the coordinator’s independent review and later owner-serialised downstream migrations. In particular, tools-ki’s worktree provisioning still names the old folder and must move with its own repository migration; Tower’s next writer should re-run DESIGN-2 against the corrected harness.

## Queries

None.

### 🤖 → 👤 Handoff to supervisor · since 02:31 BST

🤖 0 running · 🎯 1 handed off · ⛔ 0 blocked

- [handoff] DEPCRUISE-PATH review and migration scheduling · ways-of-working coordinator · since 02:31 BST
