# sop-mark-2

Kris said "mark" at about 23:46 BST on 19 October. Strike State of play's decisions log, `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md`, under the `ki-coordination` mark rules:

- Delete each decision that a durable home now wholly carries.
- Reduce each decision that still governs live work, but has its home elsewhere, to a one-line pointer.
- Keep everything else, without numbering.

Do these specifically:

- Strike the five CHEZMOI-CARRY entries (FW-DECLARE, FW-DECLARE-NOW, SSH-SPARE-KEY, SEAT-RECORD, TOML-OPENER). ki.chezmoi's own log carries them.
- Strike MODEL-FALLBACK. Kris decided on 19 October that it is struck at this mark.
- Keep the 19 October ANSWERS entry in full.
- If the package has a `design/` folder, delete notes that have graduated or are recorded as superseded, under the standard's guards.

Edit only `decisions.md` and `design/`. Do not touch `state.md`, `queries.md` or `messages.md`. Commit as "docs(work): ki mark, decisions struck".

## Rules

- CAPTURE-GATE (Kris, 19 October): create no roadmap record except one this brief names. List follow-ups in your report.
- HOOKS-MIGRATION: never run `ki repo conform` without `--dry-run`. Do not touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`.
- Commit only your own changes, staged by explicit path under `ki-git`, using Conventional Commits and ending with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>". Do not push. If another session has uncommitted changes in a file you need, leave that file alone and name it in your report.
- British English, ASCII hyphens only.
- Report to the path your run packet names, as an owner report: Done, In Progress, Queries. Each query needs Context, Query and Options, with a) recommended and its confidence.
