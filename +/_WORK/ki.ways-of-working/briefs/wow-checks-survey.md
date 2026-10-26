# wow-checks-survey - what runs at commit time, and why Markdown slips through

## Goal

Kris, 26 October: "can we take a good look at the GitHubs? Because I think some of them are running things like repo audit and conforms as part of a pre-commit. And I don't see why we'd ever want to be doing that, really." And: "some things that are writing markdown files are broken, either not passing the rumdl lint, which I suspect it should have done already."

Read-only survey. Change nothing in any repository.

## Scope

1. **Commit-time checks.** For every repository in the local KI registry (`ki registry` / `ki repo list` or the territory registries) under `/Users/krisbrown/workspaces/`: list what its Git hooks run (`.githooks/`, `core.hooksPath`, `.git/hooks/`, lefthook, husky, `package.json` scripts they call), and what its GitHub Actions workflows run. Flag every place `ki repo audit`, `ki repo conform`, `ki repo repair` or similar runs in a pre-commit or pre-push hook, how long it takes (time one commit-equivalent run on two or three representative repositories), and where the hook comes from: which harness standard, template, `ki repo conform` step or chezmoi file installs it. Note any hook that writes files.
2. **Markdown that fails rumdl.** Run the repository's own rumdl check (or `rumdl check` with its `.rumdl.toml`) across every repository; list failing files and rules. For each failing file, use `git log` to find which commit and writer produced it: a `ki` generator (`ki dev skill generate`, conform, catalogue or rubric generation), a background run, a website sync, a hand edit. Explain for each class why no check caught it: no rumdl in the hook or CI, rules differing between the generator and the lint, files excluded, checks skipped.
3. Give one table per part and a short plain-language summary Kris can read in two minutes.

## Queries

Return the decisions Kris needs as queries (Context, Query, lettered Options, the recommendation first with its confidence and reason), at least: what should run at commit time versus in CI, and where generated Markdown should be linted (in the generator, in the hook, in CI). Name the owning repository and standard for each change.

## Limits

- Read-only: no commits, no pushes, no hook or config changes, no installs. Do not run `ki repo conform` or `repair` in any repository.
- No messaging people; no Linear or Notion.
- Never remove your own scratch directory with `rm`.

## Report

Owner report: Done (the two tables and summary), In Progress, Queries.
