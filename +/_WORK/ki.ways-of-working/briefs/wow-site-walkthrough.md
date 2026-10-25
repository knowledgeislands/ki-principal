# wow-site-walkthrough - one report to walk the site and review what changed

## Goal

Kris on 2026-10-25: "a report for all of the stuff that's changed in these recent releases, so I can walk through the site and review everything." Write `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/site-walkthrough.md`: everything the Ways of working work changed from the start of the overnight window on 2026-10-24 (find its start in this work's `decisions.md`) to now, laid out as a walk through <https://knowledgeislands.info>.

## Shape

- A short opening: what period it covers, what was released (tools-ki, mgit, rig and any other versions), and how to use the walk.
- **Walk the site**: one section per live page or section in the order a reader would visit it, each with its live URL, what changed in a sentence or two, the commit that changed it, and what Kris should check (wording, diagrams, links, anything a run flagged as uncertain). Confirm each URL answers 200 with a read-only request; mark any that does not.
- **Changed but not on the site**: harness standards and skills (each with what changed and the decision behind it, by its words and date), tools-ki and other tool releases, CI pins across the repositories, workflow and settings changes, each with a GitHub link.
- **Known gaps**: anything red, unfinished or still with a run as of writing (the red website and harness main `build`, runs still queued), stated plainly.
- British English, ASCII hyphens only, every commit and file a GitHub link (`knowledgeislands/<repo>`), no internal jargon left unexplained.

## Do

Use `git log` across the repositories under `/Users/krisbrown/workspaces/knowledge-islands/`, this work's `decisions.md` and `state.md`, the run reports under `~/.local/state/ki/agents/ways-of-working/`, read-only `gh` and `curl`. Change nothing outside the report. Commit it by explicit path as `docs(work): ki.ways-of-working site walkthrough` ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase, push fast-forward only.

## Do not

Change any site, repository, setting or other file; force-push; use `--no-verify`.

## Report

The owner report: Done with the report's GitHub link, In Progress, Queries with Context, Query and Options, recommended first with confidence and reason.
