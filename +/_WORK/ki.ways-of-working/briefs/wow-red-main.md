# wow-red-main - make the website's and the harness's main build green

## Goal

Kris decided on 2026-10-25 under RED-MAIN: "Fix mains first". Bot pull requests auto-merge only on a green main. The website (`apps-knowledgeislands.info`) has failed its required `build` on every main commit since 2026-10-19, now in the KI repo audit step with one failing check and three findings; the harness (`ki-agentic-harness`) main went red at 08:07 GMT today, also in the KI repo audit step, possibly from harness `fa9c6739` or `0404754a`.

## Do

- Read the latest failing main runs with `gh run view --log-failed` for both repositories, find each cause, and fix it at its source in the repository that owns it. Use a clean temporary clone from `origin/main` for each; never edit a dirty primary checkout. Other runs are pushing to the harness: pull with rebase before each push.
- Run the repository's own tests and audits until they pass, commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, push fast-forward only, and watch main's CI until it is green.
- If any open bot pull request is still current once main is green, let auto-merge take it; do not merge by hand.

## Do not

Change DNS, Cloudflare Access, routes, Zero Trust, credentials or required-check settings; release; install new software; force-push or use `--no-verify`; touch another session's uncommitted files.

## Report

The owner report: Done with commits and the green run links, In Progress, and Queries with Context, Query and Options, recommended first with confidence and reason.
