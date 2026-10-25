# wow-review-pack-4 - review pack to the live site and every open query

## Goal

Bring `+/_WORK/ki.ways-of-working/design/review-pack.md` in Knowledge Islands Principal up to date for Kris's return at 08:00 GMT.

## Scope

- The live site deploys again since fix `904176e` (06:22 GMT). Re-check every address the pack lists with `curl -sIL` (following redirects: Cloudflare redirects each `.html` diagram address to its suffix-less form, which is expected). Replace the "Not answering" note with the current result: remove it if all answer, else list only those that still fail. Add one review line for the deploy fix itself only if it changed anything visible.
- Make the pack's open-queries section match the open section of `queries.md` exactly and verbatim: it now holds 32 queries, fourteen of them new (UNATTENDED-AND-DUE-DATES, DIAGRAM-PRIVATE-CITATIONS, SOP-PROJECT-CARE, SINGLE-THREAD, WAKE-SUBSTRATE, the four UNWRITTEN-RULES queries, SIZE-LABEL, WORK-LABEL and the three PERM-PROMPTS queries). Group them in the walkthrough so Kris meets related queries together, keeping each verbatim, and keep both views where a review disagreed.
- Keep the walkthrough instructions and digest format.

## Constraints

- Write only `design/review-pack.md`. British English, ASCII hyphens only. Commit that path by explicit path and push fast-forward; never force or `--no-verify`.

## Report

Done: what changed, its commit and any address still failing. Queries: only a genuine ambiguity.
