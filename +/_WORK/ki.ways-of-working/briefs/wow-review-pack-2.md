# wow-review-pack-2 - bring the review pack up to date

## Goal

Bring `+/_WORK/ki.ways-of-working/design/review-pack.md` in Knowledge Islands Principal up to date, so that a chat model can walk Kris through every open query and the website review list when he returns at 08:00 GMT and produce a digest he pastes back.

## Scope

- Read the pack as it stands, then `queries.md` in the same work folder. Every open query in `queries.md` must appear in the pack in full, with its tag, Context, Query and Options exactly as `queries.md` gives them, the recommended option first with its confidence and reason. Add the queries the pack lacks (among them TIDY-GAPS, AREA-COLUMN, ACCEPT, REPO-STANDARDS-SET and DEPS-1) and drop any the pack holds that `queries.md` no longer does. Where `queries.md` shows two views after a blind review, keep both.
- Website review list: read `design/website-docs.md` and the website's `git log origin/main` in `/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info` since 2026-10-25 01:00 GMT. For each page or diagram now live, give its <https://knowledgeislands.info> URL and one line on what Kris should judge there: design and use, never code. Mark the sections still being written (Ways of working pages beyond what is live, Knowledge, Standards) as pending, without URLs.
- Keep the pack's existing walkthrough instructions for the chat model and its digest format; correct only what is now wrong.

## Constraints

- Write only `design/review-pack.md`. Never edit `queries.md`, `decisions.md`, `state.md` or `messages.md`, and never touch the website checkout, which other runs are working in.
- British English, ASCII hyphens only, under `ki-authoring`.
- Commit that one path by explicit path and push fast-forward; never force or use `--no-verify`.

## Report

Done: what changed in the pack and its commit. Queries: only a genuine ambiguity in the queries or the URLs.
