# Brief: INDEX-ENTRY in tools-rig

Work: ki.sop.tools (quartermaster). Authority: [INDEX-ENTRY](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.tools/decisions.md), a brief from personal.reg.inbox, the coordination hub, on 8 November 2026 under Kris's INDEX-ENTRY order.

## Goal

Each work package's definition file, `+/_WORK/<id>/work.md`, is being renamed `+/_WORK/<id>/_index.md`. Make every place in tools-rig (`/Users/krisbrown/kis/knowledge-islands/tools-rig`) that reads or locates a work package's `work.md` read `_index.md` first and fall back to `work.md` when `_index.md` is absent.

## Scope

- In: tools-rig source, tests and its own docs that describe the lookup. Find every reference to `work.md` as a package file (search the code, not only the obvious modules). Prefer one shared resolver over repeated checks, following the repository's existing idiom and `ki-engineering`.
- Add or extend boundary tests covering: only `_index.md`, only `work.md`, both present (`_index.md` wins), neither.
- Out: renaming any file in any work package; changing the standard or its checks (ki.reg.guilds owns that); any other repository; releasing or tagging; anything destructive.

## Done when

- The repository's own checks (lint, typecheck, tests) pass.
- One Conventional Commit, staged by explicit path under `ki-git`, is pushed to `origin/main` fast-forward only. Never force-push and never use `--no-verify`. Stop on divergence and report it.
- If tools-rig has no reference to a package's `work.md`, change nothing and say so.

## Report

Report what changed (files and the commit), the checks run with their results, and anything left over or needing a decision, with each query in Context, Query and Options form.
