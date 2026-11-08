# Brief: STD-BASE check in tools-ki

Work: ki.sop.tools (quartermaster). Authority: [STD-BASE](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.tools/decisions.md), a brief from ki.reg.guilds on 8 November 2026 under Kris's STD-BASE a. Where it lives, a `ki` command, was the quartermaster's call.

## Goal

Every change document now carries `Base: ki-agentic-harness@<commit>` and `Touches:` lines (ki-agentic-harness 30c5a9daf: ki-authoring, `standards-knowledge-promotion.md#document-types`; read it first). Add a `ki` command in tools-ki (`/Users/krisbrown/kis/knowledge-islands/tools-ki`) that flags a change document whose touched files have moved since its base.

## What the command does

- Reads every `*.change.md` under `+/_WORK/**` in each registered repository (use the existing registry resolution in tools-ki; change documents live outside the harness too, for example in the Personal Inbox), plus any `*.design.md` carrying a `Base:` line during the migration.
- Takes the `Base:`, `Touches:` and, where present, `Status:` lines from each, skipping graduated documents.
- Resolves `<base>` and `origin/main` in a fetched harness clone. If the base commit is missing or unpushed, it reports "unknown", never a pass.
- Runs `git diff --name-only --find-renames <base>..origin/main -- <touched files>`, so that renamed or deleted touched files are reported too.
- Reports per document: moved (with the files), current, or unknown (with the reason), with a human-readable default and a `--json` form, and an exit code that distinguishes clean from flagged, following the CLI's existing conventions.

## Scope

- In: the new command, its wiring in the CLI's help and man page where the repository keeps them, and boundary tests: a document whose files moved, one renamed, one deleted, one current, a graduated document skipped, a missing base reported as unknown, and a document missing its `Base:` or `Touches:` line.
- Choose the command's name and place to fit the existing `ki` command tree, and say in the report why you chose it.
- Out: changing any change document; the harness or any other repository; releasing, tagging or reinstalling `ki`; anything destructive. ki.reg.guilds's `_index.md` change just landed in tools-ki (b537df2e), so build on it and don't change it.

## Done when

- The repository's own checks (lint, typecheck, tests) pass.
- Conventional Commits, staged by explicit path under `ki-git`, are pushed to `origin/main` fast-forward only. Never force-push and never use `--no-verify`. Stop on divergence and report it.

## Report

Report the command and why you chose it, what changed (files and each commit), the checks run with their results, a sample run against the real registry if one is safe (read-only), and anything left over or needing a decision, with each query in Context, Query and Options form.
