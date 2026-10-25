# wow-docs-work-a - Ways of working, pages 1 to 5

Unit 6 of the website documentation plan. It follows wow-docs-harness. It touches `apps/site/src/docs/ways-of-working/`, `diagrams.toml`, `docs/diagrams/` and `featureAreas.json5`, so it runs alone.

## Task

Write five pages at the plan's addresses and orders, each following the skeleton, and draw their diagrams with `archify`, each with a manifest entry, finalised with `diagrams:build` and embedded with the `figure` shortcode.

| Order | Page | Sources to read | Diagrams |
| --- | --- | --- | --- |
| 1 | `the-work-model.md` | `ki-principal` `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md` at its HEAD when you read it; `ki-coordination` standard | `work-model` (architecture: supervisor, worker, the work, its package, send and receive), `seven-states` (lifecycle), both traced to the note |
| 2 | `work-packages.md` | `ki-work-package` SKILL.md and references | `work-folder` (architecture: the five files, `design/`, `briefs/`, findings, `+/_WORK_REVIEW/`) |
| 3 | `coordination.md` | `ki-coordination` standard and its reply forms, owner report and banner sections | vendored `thread-model`; `coordinating-turn` (sequence: owner message, turn, launch, wake, receive, report) |
| 4 | `background-runs.md` | `ki-delegation` `standards-background-runs.md`; `tools-ki` `ki agent` manual section at `v0.13.0` | `background-run` (sequence: brief, launch, status marks, report, receive, prune) |
| 5 | `roadmap-lifecycle.md` (rewrite of the moved page) | `ki-work`, `ki-work-roadmap`, `ki-next`, `ki-plan`, `ki-implement`, `ki-accept`, `ki-batch` | `record-lifecycle` (lifecycle: captured, adopted, ready, in delivery, awaiting review, done, pruned) |

Describe the seven states and the receive words exactly as the note and standard name them. Describe unattended windows, grants and the deny list under background runs as the standard sets them, with no reference to any particular night or owner. Set each area's `page` in `featureAreas.json5`. Where `by-outcome` or a CLI page named this section without a link, add the link now.

## Commit and report

Commit as `docs(site): publish Ways of working pages 1 to 5` by explicit path. Report the five URLs and the five or six interactive diagram URLs.

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
