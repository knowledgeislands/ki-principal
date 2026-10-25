# wow-fleet-green - clear dependency and toolchain drift so fleet CI goes green

## Goal

Under Kris's CI-PIN answer on 2026-10-25 ("let's just get it sorted") and the unattended rule that upgrading an existing library or tool needs no check, clear the CI failures caused by dependency and toolchain drift across the Knowledge Islands repositories under `/Users/krisbrown/workspaces/knowledge-islands/`:

- DEPS-1: bun 1.4.2 to 1.4.3, `@types/node`, `rumdl`.
- DESIGN-2: the `prepare` script must install `tooling/depcruise` or `tooling/boundaries`.
- TEST-5: `dependency-cruiser` `^18.6.0` against `^18.7.0`, in `mcp-acquire-whatsapp`, `mcp-ki-kb-fs` and `tools-git-almanac`.
- shellcheck SC2015 in `tools-mgit` `bin/mgit` at lines 3286 and 3312.

Affected: apps-observatory.local, ki-techne-harness, mcp-housekeeping-chatgpt, tools-ki, tools-mgit, tools-techne, ki-design (DEPS-1 and DESIGN-2 only), ki-principal (DEPS-1 only), and the mcp-* and tools-git-almanac repositories. `apps-knowledgeislands.info` and `ki-agentic-harness` are excluded: wow-red-main has fixed them, so follow its approach.

## Do

- Use `ki repo audit` and `ki repo repair` where they fix a rule, rather than hand edits. Use a clean temporary clone from `origin/main` per repository, never a dirty primary checkout. Another session may be committing to `tools-ki`; pull with rebase before each push.
- Run each repository's tests and audits, commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, push fast-forward only, and watch main's CI. Leave document-rule failures alone and list them.
- Keep about three repositories in flight; a slow coverage suite may be left to CI.

## Do not

Install new software (upgrades of existing dependencies only), change DNS, Cloudflare, credentials, required checks or GitHub settings, release, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done with one line per repository (commit, CI result), In Progress, Queries with Context, Query and Options, recommended first with confidence and reason.
