# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/work.md) › conform-tools-mgit

**🤖 → 👤 Handoff to supervisor · Run report at 02:02 GMT · last mark 02:02 GMT**

---

## Done

- Audit before: 2 failures (FILES-6 managed `.gitignore` block not reconciled; SHELL-HOOK, the pre-commit hook ran a staged `ki repo audit`) and 4 warnings, including HOOK-4 (hook not the canonical text).
- `e84b055` chore(repo): conform commit gate and managed ignores to harness. The pre-commit hook is now the canonical no-package hook from the harness (`fd3403b4`), copied byte-exact and check-only. The managed ignore block now carries the TOP-LEVEL-NOW `reports/` exception for `+/_WORK/*/reports/` and `+/_WORK_REVIEW/*/reports/`.
- PKG-6 and HOOK-STASH a do not apply: mgit has no `package.json` or lint-staged by design.
- Audit after: no failures and 3 warnings, none of them in this brief's scope.
- Checks: shellcheck, `bash -n`, mandoc lint and `git diff --check` passed; the Bats suite passed 153 tests, with the real-producer proof skipped as usual. There is no TEST-5 failure.

## In Progress

Nothing. Three warnings are left because they are outside the commit-gate rules:

- ALIAS-1: `.ki.toml` still declares the deprecated `ki-agent-coordination-paperclip` skill.
- MATURITY-1: `.ki.toml` declares no `maturity`.
- OWN-1: `.rumdl.toml` differs from the house template. Conform would delete the repository's documented MD005 and MD075 notes. That is an authoring decision, so I put the file back after conform rewrote it.

## Queries

None.
