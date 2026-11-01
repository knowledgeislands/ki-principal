# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › conform-mcp-ki-kb-fs

**🤖 → 👤 Handoff to supervisor · Run report at 02:20 GMT · last mark 01:41 GMT**

---

## Done

- Audit before (harness `fd3403b4` or later): FAIL=3. The failures were FILES-6 (the managed `.gitignore` block was not reconciled), SCR-11 (the pre-commit hook lacked `--no-stash`) and PKG-6 (lint-staged ran `biome check --write` and `rumdl check --fix`). HOOK-4 warned that the hook was not canonical.
- `caa8e97` chore(gate): make the commit gate check-only and reconcile ignore blocks. It adds the TOP-LEVEL-NOW `reports/` exceptions (FILES-6), makes the hook run `lint-staged --quiet --no-stash` byte-exact with the canonical hook (SCR-11, HOOK-4, HOOK-STASH a), and removes `--write`/`--fix` from lint-staged (PKG-6). GATE-1 needed no mechanical change.
- `ki repo conform` also rewrote `packageManager` from `bun@1.4.3` to `bun@1.4.2`. That would have undone the Bun 1.4.3 adoption and caused new DEPS-1 and MISE-2 findings, so I reverted it by hand and did not commit it. This looks like a conform defect in tools-ki or the harness, and other repositories on Bun 1.4.3 will probably hit it.
- Audit after: PASS, FAIL=0, WARN=2. Both warnings are outside this brief and listed below.
- Checks: `tsc --noEmit` pass; `bun run test` pass; `test:coverage` pass, so there was no TEST-5 failure to investigate; `build` pass; `ki:test:smoke` pass; the pre-commit gate passed on the commit.
- Pushed `main` fast-forward to `origin`.

## In Progress

- Nothing. Two warnings remain, both outside the commit-gate scope:
  - ALIAS-1: `.ki.toml` still declares the deprecated `ki-agent-coordination-paperclip`. It should declare `[skills.ki-delegation-paperclip]` instead.
  - MATURITY-1: `.ki.toml` declares no `maturity`. Choosing one is the owner's call.

## Queries

### Q1 - Conform lowers the Bun pin

**Context**

When `ki repo conform` writes `package.json`, it puts back an older Bun version (`bun@1.4.2`) in place of the repository's current `bun@1.4.3`. That would break the dependency checks. I undid it here, but other conform runs in this window may commit the downgrade without noticing.

**Query**

Should the tool defect be captured as work for the tools-ki burndown?

**Options**

a) (recommended, confidence high - the rewrite is reproducible and affects every repository already on Bun 1.4.3) Capture it as a triage record under ki.prj.tools-burndown, and tell the remaining conform runs to check the `packageManager` line before they commit.

b) Leave it, and rely on each run's after-audit to catch the DEPS-1 failure.
