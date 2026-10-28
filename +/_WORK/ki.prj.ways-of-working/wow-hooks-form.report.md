# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-hooks-form

**🤖 → 👤 Handoff to supervisor · Run report at 23:06 GMT · last mark 23:06 GMT**

---

## Done

- FORM-VS-RUMDL a) landed in harness commit 26ad77f1: the query form in `ki-coordination` and `ki-delegation` uses separate paragraphs, the coordinator style and run-prompt assets were regenerated, and the banner test and a rumdl proof against ki-principal's `.rumdl.toml` both passed. `RUMDL_DEFAULT` is unchanged.
- COMMIT-VS-CI a) landed in harness commit d174adbc: the `ki-repo` composer drops the focused staged audit and the quiet helper from every canonical hook, so no hook calls `ki`; the twelve hook assets, this repository's hook and its lint-staged block are check-only (`biome check --no-errors-on-unmatched`, `rumdl check`, `syncpack format --check`, plus `shellcheck`, `bash -n`, `mandoc -T lint` for tools and `ruby -wc` for the tap).
- Each shape content criterion (harness GATE-1 and GATE-2, kb, specifications, homebrew-tap, project GATE-1, tools SHELL-HOOK) now fails a hook that runs `ki repo audit`, `ki repo conform`, `ki repo repair`, `--fix` or `--write`; `ki-engineering` PKG-6 fails a rewriting lint-staged block and the CONFORM template is check-only; SCR-11, HOOK-4 guidance, the ki-repo, engineering, authoring and six shape standards, AGENTS.md and a dated amendment to ADR-KI-HARNESS-SKILLS-017 say the same, and the nine rubrics were regenerated.
- Checks on the combined result: `bun run test` 1466 pass, 0 fail; `bunx tsc --noEmit` clean; Biome and rumdl clean on the changed files; focused audits for ki-repo, ki-engineering, ki-authoring, ki-repo-harness, ki-repo-project, ki-skills, ki-coordination and ki-delegation report no FAIL, the only WARNs being pre-existing fleet findings (MATURITY-1 on `.ki.toml`, LONG-3 source-refresh cadence); ki-repo-kb, ki-repo-specifications, ki-repo-homebrew-tap and ki-repo-tools are not declared by this repository, so their change is covered by their unit tests, not a focused audit here.
- Harness `main` fetched, fast-forward pulled and pushed; local and `origin/main` are level at d174adbc.
- Downstream line queued: ki-principal commit 94e674a4 appends HOOKS-CHECK-ONLY to `+/_WORK/ki.tools-burndown/messages.md`, asking tools-ki to align its canonical-hook, hooks and estate hook tests and the lint-staged rendering in `src/core/repository/operations/conform.ts`, then release so `ki repo conform` rolls the check-only hooks and lint-staged block across the estate; ki-principal `main` pushed and level. Thirty other uncommitted files in ki-principal belong to other sessions and were left untouched.

## In Progress

Nothing is running. Until tools-ki releases, repositories that already carry the old canonical hook keep calling `ki repo audit --staged` at commit time and will fail HOOK-4 against the new assets once their `ki` reads the harness's hook bytes; `ki repo conform` after the release rewrites them.

## Queries

No outstanding queries.
