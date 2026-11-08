# Brief: INDEX-ENTRY in apps-observatory.local

Work: ki.sop.tools (quartermaster). Authority: [OBSERVATORY-READERS](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.tools/decisions.md), Kris's word relayed by personal.reg.inbox on 8 November 2026, under INDEX-ENTRY.

## Goal

Each work package's definition file, `+/_WORK/<id>/work.md`, is being renamed `+/_WORK/<id>/_index.md`. Make `packages/evidence` in apps-observatory.local (`/Users/krisbrown/kis/knowledge-islands/apps-observatory.local`) read `_index.md` first and fall back to `work.md` when `_index.md` is absent.

## Scope

- In: `packages/evidence`, known readers `work.ts`, `work-package.ts`, `review.ts` and `feedback.ts`, but search the whole package, and the rest of the repository, for any other reader of a package's `work.md`. Use one shared resolver rather than repeated checks, following the repository's idiom and `ki-engineering`. Update the tests and the one diagram that names `work.md`.
- The standard says `_index.md` is preferred, `work.md` is accepted during the rollout, and a folder holding both is a failure. Surface a folder holding both as a failure through whatever error or finding path the package already uses. Don't crash the app, and change no other behaviour.
- Boundary tests: only `_index.md`, only `work.md`, both present (failure), neither.
- Out: renaming any file in any work package; tools-ki (another run is changing it); any other repository; releasing, tagging or deploying; anything destructive.

## Done when

- The repository's own checks (lint, typecheck, tests) pass.
- Conventional Commits, staged by explicit path under `ki-git`, are pushed to `origin/main` fast-forward only. Never force-push and never use `--no-verify`. Stop on divergence and report it.

## Report

Report what changed (files and each commit), the checks run with their results, and anything left over or needing a decision, with each query in Context, Query and Options form.
