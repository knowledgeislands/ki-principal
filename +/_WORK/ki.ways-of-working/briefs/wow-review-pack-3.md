# wow-review-pack-3 - final review pack for the finished site

## Goal

All ten documentation units are live on <https://knowledgeislands.info>. Bring `+/_WORK/ki.ways-of-working/design/review-pack.md` in Knowledge Islands Principal to the finished state, so that a chat model can walk Kris through it at 08:00 GMT.

## Scope

- Website review list: read the website's `git log origin/main` since 2026-10-25 01:00 GMT in `/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info` and the plan `design/website-docs.md`. Add every page and diagram published since the pack was last written (Ways of working pages 6 to 10, Knowledge, Standards, and any changed landing or crosswalk pages), each with its <https://knowledgeislands.info> address and one line on what Kris should judge: design and use, never code. Remove every pending marker.
- Confirm each listed address answers with HTTP 200 using `curl -sI`; list any that do not in the pack's opening under a short "Not answering" note, and in your report.
- Open queries: re-read `queries.md` and make the pack's query section match it exactly, verbatim, as the pack already does.
- Keep the walkthrough instructions and the digest format.

## Constraints

- Write only `design/review-pack.md`. Never edit any other work-package file or the website checkout.
- British English, ASCII hyphens only, under `ki-authoring`.
- Commit that one path by explicit path and push fast-forward; never force or use `--no-verify`.

## Report

Done: what changed and its commit, and any address not answering. Queries: only a genuine ambiguity.
