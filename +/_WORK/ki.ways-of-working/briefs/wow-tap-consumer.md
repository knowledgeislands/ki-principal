# wow-tap-consumer - enrol the harness as a release consumer of the tap

## Goal

Kris decided on 2026-10-25 under HARNESS-CONSUMER: "Add, keep poll". Add `knowledgeislands/ki-agentic-harness` to `.github/tool-release-consumers.json` in `/Users/krisbrown/workspaces/knowledge-islands/homebrew-tap`, so a tools-ki release reaches the harness's `update-ki-pin.yml` by dispatch; keep the harness's daily poll as the backstop.

## Do

- First confirm with read-only `gh` calls that the credential the tap's notify step uses can dispatch to the harness (the App installation covers it, or the token's scope does). If it cannot, change nothing and raise the settings step as a query.
- Confirm the harness workflow's filter matches the tap's payload. Follow the tap's onboarding guide. Use a clean temporary clone from `origin/main`, run the tap's tests and audits, commit by explicit path as a Conventional Commit ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase, push fast-forward only, and watch the tap's main CI until green.

## Do not

Cut a release, change credentials, App installations or required checks, change the harness, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done with commit and CI link, In Progress, Queries with Context, Query and Options, recommended first with confidence and reason.
