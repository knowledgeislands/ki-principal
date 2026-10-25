# wow-docs-ki - the ki CLI section at v0.13.0

Unit 4 of the website documentation plan. It follows wow-docs-diagrams, which drew the `command-groups` diagram. It touches only `apps/site/src/docs/ki/`, `cliCommands.json5`, `projects.json5`'s `ki` entry and `featureAreas.json5`, so it may run alongside wow-docs-skills; it does not touch `diagrams.toml`.

## Task

1. Refresh the command inventory: `bun run --cwd apps/site sync:cli -- --ref v0.13.0` reading `/Users/krisbrown/workspaces/knowledge-islands/tools-ki` (`--from` if needed). If the parser refuses a construct the manual gained since `v0.11.0`, extend it strictly and add the test case. Advance every `ki` page's `sources.ref`, `reviewed` and every version mention to `v0.13.0`; the released `ki` entry in `projects.json5` pins its installer tag, leave it unless `verify:routes` requires the change.
2. Rewrite `command-groups.md` around the eighteen groups in `man/ki.1` at `v0.13.0` (General, Global options, Installation, Local management, User management, Repository options, Repository management, Batch records, Knowledge Base search, Registry management, Harness management, Trades, Territory management, Acquisition, Background agents, Work model, Estate convergence, Development), one short paragraph each saying what the group operates on and when a user reaches for it, keeping the `command-groups` figure.
3. Write three pages at the plan's addresses and orders 10 to 12, each following the skeleton and reading the manual sections, `docs/guides/user/` in `tools-ki` at `v0.13.0` and the skills they serve at harness `8897008f`:
   - `work-and-agents.md`: Work model, Background agents and Batch records from a user's view: a work package's commands, launching, queueing, status, wait and prompts for runs, and a batch envelope.
   - `repositories-and-territory.md`: Registry, Repository management, Repository options, Harness management, Territory management and Estate convergence.
   - `trades-and-acquisition.md`: Trades, Acquisition and Knowledge Base search. Each links the Ways of working, Knowledge or Standards page it serves only where that page exists at your pull.
4. Check the nine existing pages against the manual for commands renamed or added between `v0.11.0` and `v0.13.0` and correct them; keep each page's scope.
5. In `featureAreas.json5`, add each page's commands to the areas the plan names.

## Commit and report

Commit as `docs(site): refresh the ki CLI section to v0.13.0 and add three pages` by explicit path. Report the three new URLs, the command-groups URL and the command count after the sync.

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

## Relaunch note (04:26 GMT)

CLI-PREREQUISITES a) is granted. You start after wow-docs-diagrams has committed `command-groups.md` and the pipeline. In scope: repair the roff parser for the new escapes, and add local Git input to the CLI sync script and its tests, reading the `tools-ki` checkout at `/Users/krisbrown/workspaces/knowledge-islands/tools-ki` at its `v0.13.0` tag (read only; never edit or tag tools-ki). Commit only your own paths; wow-docs-skills may be working in the same checkout.
