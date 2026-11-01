# [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md) › conform-tools-techne

**🤖 → 👤 Handoff to supervisor · Run report at 02:14 GMT · last mark 02:14 GMT**

---

## Done

- Audit before: 3 failures (PKG-6, SCR-11, FILES-6), 5 warnings. Audit after: 0 failures, 4 warnings.
- `ee97b67` chore: conform commit gate to current harness. The pre-commit hook now runs `lint-staged --quiet --no-stash` and no longer runs the staged audit; lint-staged runs Biome and rumdl check-only; `.gitignore` gains the work-folder `reports/` exceptions. Pushed to `main`.
- I kept conform from downgrading `packageManager` to Bun 1.4.2, which would itself have failed DEPS-1. The repository stays on 1.4.3.
- Checks: tests with coverage, typecheck, build, release-package test, manual-page lint, Biome and rumdl all pass.

## In Progress

Nothing. These four warnings are outside this brief and stay as they are:

- ALIAS-1: `.ki.toml` still declares the deprecated `ki-agent-coordination-paperclip` skill.
- OWN-1: `.rumdl.toml` has drifted from the house template. Conform proposed a rewrite, which I held back as out of scope.
- CI-1: `ci.yml` pins `KI_VERSION` inline.
- MATURITY-1: `.ki.toml` declares no maturity.

## Queries

None.
