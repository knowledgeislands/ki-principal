# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md) › conform-mcp-git-audit

**🤖 → 👤 Handoff to supervisor · Run report at 02:10 GMT · last mark 02:10 GMT**

---

## Done

- Audit before: 3 failures (PKG-6, lint-staged ran `biome --write` and `rumdl --fix`; SCR-11, the hook ran `lint-staged` without `--no-stash`; FILES-6, the managed ignore block was not reconciled) and 4 warnings, including HOOK-4 (hook not the canonical text).
- `e0a5002` chore(repo): adopt check-only commit gate and work-report ignore exception. The hook now runs `lint-staged --quiet --no-stash` (HOOK-STASH a), lint-staged is check-only, and the managed block carries the TOP-LEVEL-NOW `reports/` exception for `+/_WORK/*/reports/` and `+/_WORK_REVIEW/*/reports/`.
- Two of conform's proposed writes were left out: it would have set `packageManager` back from Bun 1.4.3 to 1.4.2, undoing the recent toolchain adoption, and it would have rewritten `.rumdl.toml` comments (the ki-authoring OWN-1 warning, outside this brief).
- Checks: tests 247/247 pass with 100% coverage; typecheck, Biome, rumdl and syncpack clean; the commit passed the new hook. No TEST-5 failure.
- Audit after: no failures and 3 warnings, none of them in this brief's scope.

## In Progress

- Nothing. Warnings left as they are: ALIAS-1 (`.ki.toml` still declares the deprecated `ki-agent-coordination-paperclip`), MATURITY-1 (no `maturity` declared) and OWN-1 (`.rumdl.toml` comments differ from the house template).

## Queries

### Q1 - Conform would downgrade the Bun pin

**Context**

In this repository, `ki repo conform` for ki-engineering wants to set `packageManager` to Bun 1.4.2, but the repository adopted Bun 1.4.3 in its latest toolchain commit and the engineering audit passes on 1.4.3. I kept 1.4.3.

**Query**

Should the harness's Bun pin in its toolchain template move to 1.4.3, so other repositories' conform runs stop proposing this downgrade?

**Options**

a) (recommended, confidence medium - the fleet seems to be adopting 1.4.3, and a stale pin will keep producing this diff) Raise the template pin to 1.4.3 in ki-agentic-harness as separate work.

b) Leave it; conformance runs keep skipping the pin change by hand.
