# wow-docs-work-b - Ways of working, pages 6 to 8

Unit 7 of the website documentation plan. It follows wow-docs-work-a. It touches `apps/site/src/docs/ways-of-working/`, `diagrams.toml`, `docs/diagrams/` and `featureAreas.json5`, so it runs alone.

## Task

Write three pages at the plan's addresses and orders, each following the skeleton, and draw their diagrams with `archify`, each with a manifest entry, finalised with `diagrams:build` and embedded.

| Order | Page | Sources to read | Diagram |
| --- | --- | --- | --- |
| 6 | `work-design.md` | `ki-work-design` SKILL.md and references | `work-design-loop` (workflow: brief, independent reviews, merged report, owner decisions, piloted rollout) |
| 7 | `trades.md` | `ki-trades` and `ki-trade`; `tools-ki` Trades manual section at `v0.13.0` | `trade` (sequence: sender, route, record, receiver disposition, receipt, release, with ownership never transferred) |
| 8 | `recurring-work.md` | `ki-work-recurring`, `ki-repo-kb-activities` | `recurring-occurrence` (workflow: adopt, schedule, run, evidence, review) |

Describe trades as the skills define them today; say nothing about their standing or future. Set each area's `page` in `featureAreas.json5` and add the links other pages left as plain section names.

## Commit and report

Commit as `docs(site): publish Ways of working pages 6 to 8` by explicit path. Report the three URLs and the three interactive diagram URLs.

## Common rules for every wow-docs unit

- Work in the website repository `/Users/krisbrown/workspaces/knowledge-islands/apps-knowledgeislands.info` on `main`. Read its `AGENTS.md`, `docs/guides/developer/docs-sections.md`, `page-provenance.md`, `what-to-publish.md` and `prose-styling.md` first, then the merged plan `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/website-docs.md`, which settles every design question; do not reopen one. Do not edit `ki-principal`, the harness or `tools-ki`.
- The reader is a user of Knowledge Islands, not a developer. Each new Markdown page follows the plan's skeleton: an opening claim of at least 120 characters, at most two figures, `## What it is`, `## How it works`, `## How you use it`, `## What it provides`, `## Boundaries`, the generated `Provided by` box and the provenance footer. No hand-off link text. British English, ASCII hyphens only, no em-dashes or en-dashes. Worked examples use a fictional island and fictional people; never name a private repository or a person.
- The website shows only the settled current state. Never mention an open owner query, a proposal or future work. An interim practice carries one `Interim` callout under the opening claim and is described as it works now.
- Pin sources: harness pages `repository: knowledgeislands/ki-agentic-harness`, `ref: 8897008f` (use the full 40-character SHA from `git -C /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness rev-parse 8897008f`); `tools-ki` pages `ref: v0.13.0`; `ki-principal` pages the full SHA of the commit you read. Quote `governs` and `reviewed`; `reviewed` is today's date.
- Every `ki-...` skill name you write must exist in the vendored catalogue at `apps/site/src/_data/skillCatalogue.json5`. Read the skill's `SKILL.md` and `references/` in the harness checkout at the pinned ref (`git -C <harness> show 8897008f:skills/<concern>/<skill>/SKILL.md`), not the working tree.
- Diagrams follow the `ki-diagrams` standard (`skills/governance/ki-diagrams/` in the harness) and are drawn with the `archify` skill: one of the five manifest types, JSON source, `svg_form = "ki"` SVG, `commit_html = true` with HTML and receipt, a `diagrams.toml` entry with `question`, `audience`, `traced`, `stale_when`, `regenerate` and `last_checked`. Embed with the `figure` shortcode the diagram pipeline unit added. Finalise with `bun run --cwd apps/site diagrams:build -- --svg <slug>` as that unit documents.
- Checks, all of which must pass before you commit: `bun run ki:site:build` from the repository root (it runs every `verify:*` gate), `bun run --cwd apps/site test`, `bun run --cwd apps/site typecheck`, then `ki repo audit --skill ki-repo-website-content --repo .`, `ki repo audit --skill ki-engineering --repo .`, `ki repo audit --skill ki-authoring --repo .` and, once `.ki.toml` declares it, `ki repo audit --skill ki-diagrams --repo .`. If `node_modules` is missing, stop and report rather than installing. After removing or moving a route run `bun run ki:site:clean` and build again.
- Commits: Conventional Commits with scope `site`, local, staged by explicit path only, ending with the co-author trailer naming your model. Never `--no-verify`, never a force-push, never touch another session's uncommitted files.
- Publishing: after the checks pass, `git fetch -q`, `git pull -q --ff-only`, then `git push -q origin main` fast-forward only. Pushing `main` deploys the site. Stop on divergence and report it; do not rebase, reset or stash.
- No other network call: no GitHub API, no package installs, no `verify:provenance -- --network`.
- Report in under 30 lines in owner-report form: Done with the commit identifiers and one line per check, In Progress, Queries. Name every published URL as `https://knowledgeislands.info<path>`, noting that the deploy completes after the push. Put a design choice you had to make that the plan did not settle in Queries with a recommended option; do not block on it.

## Gate baseline note (04:47 GMT)

Follow the plan's Gate baseline section in `design/website-docs.md`: the engineering audit's DEPS-1 dependency-age failure and CI-1 warning are the pre-existing baseline. Once the site build with every gate, the tests, the typecheck and the website-content, authoring and diagrams audits pass, commit only your own paths by explicit path and push fast-forward, naming DEPS-1 in your report. Never install or update dependencies. Other units may be working in the same checkout: never stage, revert or touch their files. Also follow the plan's Linking back from Skills by outcome section.

## Draft ownership (05:23 GMT)

The uncommitted Work design, Trades and Recurring work pages under `apps/site/src/docs/ways-of-working/`, the work-design-loop, trade and recurring-occurrence diagrams with their manifest entries and receipts, the feature-area entries and the earlier-page links were written by your own first attempt, whose report at 05:21 GMT lists them as its prepared work. Adopt them, re-run the gates, and commit those paths under the Gate baseline above. wow-docs-work-c is writing in the same checkout at the same time, and `apps/site/scripts/verify-diagrams.test.ts` belongs to neither of you: never stage, revert or touch either.
