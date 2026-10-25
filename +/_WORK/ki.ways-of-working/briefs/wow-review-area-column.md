# wow-review-area-column - blind review of one documentation choice

Read-only review. Make no edits and no commits in any repository.

## Context

The Knowledge Islands website (`/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info`) publishes a skill catalogue page, `/docs/ki-agentic-harness/skill-catalogue/`, generated from a pinned snapshot of the KI Agentic Harness (`/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, revision 8897008f). The harness groups its 64 skills by 8 source concerns (the folders under `skills/`) and also assigns each skill one or more of 10 functional areas. The functional-area table exists only inside the harness's generator code; the harness `skills/README.md` carries the concern grouping but not the area table. The website's Markdown gate treats a Nunjucks loop that emits rows as not being a Markdown table, so a generated area table cannot be a plain Markdown table on the page.

## Query

How should the website show which functional areas each skill belongs to?

## Options (unranked)

- Keep the page grouped by source concern and add an area finder table (skill, source concern, functional area) rendered as inline HTML from the synced snapshot.
- Ask the harness to publish the functional-area table in its `skills/README.md` generated block, so the website can sync it and render the page as plain Markdown.

## Report

Give your recommendation, its confidence (high, medium or low) and a one-line reason, plus any risk the other option avoids. Inspect the website's `apps/site` catalogue page and sync script, and the harness generator, as you see fit.
