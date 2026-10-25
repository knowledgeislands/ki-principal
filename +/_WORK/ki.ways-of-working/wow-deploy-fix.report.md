# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-deploy-fix

**🤖 → 👤 Handoff to supervisor · Run report at 06:33 GMT · last mark 06:32 GMT**

---

## Done

- Cause: the site deploys through a Git-connected Cloudflare Workers Build that runs `bun run ki:site:build` then `bun run ki:site:deploy` in a clone holding only this repository. Commit `d547611` appended `verify:diagrams` to the build, and that step resolved the harness `ki-diagrams` skill to run the canonical `build-html.ts --check`; with no skill installed it threw "Install the KI harness diagram skill or set KI_DIAGRAMS_HOME", the build exited 1, and no deploy ran. Evidence: the Cloudflare check run on `6a0cc48` is `success` and on `d547611` and every later `main` commit through `31f4ba3` is `failure`; a clean clone of `31f4ba3` built with an empty home reproduced the exact failure, and the same clone built clean with the skill present.
- Fix: commit `904176e` on `main`, `fix(site): check diagram receipts in-repo so the deploy build needs no harness skill`. It restates the ki-diagrams receipt check in `apps/site/scripts/lib/diagrams.ts` (schema 1 receipt naming slug and type, SHA-256 and byte count of source and viewer), runs it for every committed site diagram in `verify-diagrams.ts`, and keeps the canonical `build-html.ts --check` as a cross-check only where the skill is installed. A new `lib/diagrams.test.ts` covers the match, stale viewer, stale source, malformed receipt, wrong slug and missing-file cases, and the Verification paragraph of `docs/guides/developer/diagrams.md` describes the new behaviour. Pushed fast-forward to `origin/main` at 06:20 GMT.
- Gates on the clean clone: site build with every verifier PASS in both the skill-present and the skill-absent environments; typecheck PASS; Biome PASS; `ki repo audit` ki-repo-website-content PASS, ki-diagrams PASS, ki-authoring WARN (pre-existing, identical in the primary checkout), ki-engineering FAIL on DEPS-1 with CI-1 WARN (the known baseline, unchanged).
- Tests: the three new tests pass; `bun run test` still fails on one pre-existing test, "the full gate detects missing artefacts and stale viewer receipts" in `verify-diagrams.test.ts`, which fails identically at `31f4ba3` before my change because it copies only the command-groups files against a manifest of 24 diagrams. The other session's uncommitted edit to that file is the fix for it; I did not touch the file.
- Live: the Cloudflare check run on `904176e` completed `success` at 06:22 GMT. `https://knowledgeislands.info/docs/standards/writing/` answers 200. `https://knowledgeislands.info/diagrams/site/work-model.html` answers 307 to `/diagrams/site/work-model`, which answers 200 with the full viewer (818,976 bytes); browsers follow it, and every page's "Interactive" link therefore works. The redirect is the Workers Static Assets default `html_handling` dropping the `.html` suffix, not a repository defect, so I made no change for it.
- GitHub Actions CI stays red on every commit since `d547611`, including `904176e`, at the `ki repo repair` step: the pinned `ki` v0.8.4 harness does not provide the `ki-diagrams` skill `.ki.toml` declares. That is the CI-1 checker-drift case AGENTS.md describes, owed to a `tools-ki` pin bump, and it does not gate the Cloudflare deploy. Left as is.

## In Progress

- Nothing. The temporary clone remains at `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-deploy-fix/work` because the tool refused to remove a directory it was running in; `ki agent close` or `rm -rf` of that literal path clears it. Nothing in it needs to survive.

## Queries

None.
