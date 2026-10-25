# wow-test-owner - establish who wrote the stray test edit, and commit it only if it is ours

## Goal

The website checkout `/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info` holds an uncommitted 8-line edit to `apps/site/scripts/verify-diagrams.test.ts`. On committed `main`, the test "the full gate detects missing artefacts and stale viewer receipts" fails, because it copies only the command-groups files against a 24-diagram manifest; the edit fixes it. The file was last committed in `d547611` by the run wow-docs-diagrams.

## Scope

- Establish authorship from evidence: the run logs and transcripts under `~/.local/state/ki/agents/ways-of-working/` (status files, launch files, reports and any transcript or session file they point to) and the Claude Code and Codex session logs on this machine for 2026-10-24 and 2026-10-25, searching for writes to `verify-diagrams.test.ts`. Name the run or session that wrote the edit, with the evidence.
- If a ways-of-working run (`wow-*`) wrote it: from a clean temporary clone of `origin/main`, apply the same edit, run the site tests, typecheck and site build, and if they pass commit only that path by explicit path and push `main` fast-forward. Then report the primary checkout's state; do not revert or rewrite the primary checkout's copy, which a fast-forward pull will reconcile.
- If any other session wrote it, or authorship cannot be shown: change nothing and report the evidence.

## Constraints

- No dependency installs, settings changes, force-push or `--no-verify`. Never touch any other file.

## Report

Done: the author with evidence, and the commit if any. Queries: only if authorship is unclear, with the evidence.
