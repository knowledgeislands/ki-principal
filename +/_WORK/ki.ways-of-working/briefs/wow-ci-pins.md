# wow-ci-pins - move every KI CI onto the current ki

## Goal

Every Knowledge Islands repository whose GitHub Actions CI pins a `ki` (tools-ki) version runs the current `tools-ki` release, and its CI is green on the commit that moves it. Kris decided this on 2026-10-25 at 07:20 GMT: "CI pin, yes, move all of the repos onto ... whatever the CIs are, whatever, let's just get it sorted".

## Known

- `apps-knowledgeislands.info` CI pins `ki` v0.8.4 and has been red since 04:22 GMT. Its `ki repo repair` step fails because the v0.8.4 harness lacks the `ki-diagrams` skill its `.ki.toml` now declares. Its AGENTS.md says a pin bump is the fix for this kind of checker drift.
- The current release is whatever `tools-ki`'s latest published tag or release is. Verify it from `tools-ki` and GitHub; don't assume it.

## Do

1. Survey every repository under `/Users/krisbrown/workspaces/knowledge-islands/` for CI workflows that install or pin `ki`. List each one with its current pin.
2. In each, move the pin to the current release. For each repository: make the change in a clean temporary clone of `origin/main`, or in the primary checkout only if it is clean; run the repository's local gates; commit only the pin change, by explicit path, as a Conventional Commit ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; pull with rebase; push fast-forward only.
3. Watch CI on each pushed commit (`gh run watch` or `gh run list`) until it finishes. Green counts as done. If it's red, give the cause in one line. Fix it only when the fix is the pin itself, or a mechanical consequence of the new `ki` within that repository's CI file. Anything else becomes a query.
4. Leave each primary checkout level with its remote, fast-forward only, without touching another session's uncommitted files.

## Do not

- Release or tag `tools-ki`, or change any GitHub, DNS or Cloudflare setting.
- Update dependencies or Bun: DEPS-1 is a separate unit.
- Touch repositories outside the Knowledge Islands workspace.
- Force-push, use `--no-verify`, or commit another session's files.

## Report

The owner report: Done, one line per repository with its old pin, new pin, commit and CI result; In Progress; Queries, each with Context, Query and Options, the recommended option first with its confidence and reason.
