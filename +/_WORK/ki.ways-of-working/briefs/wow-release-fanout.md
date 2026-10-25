# wow-release-fanout - what does a tools-ki release update?

## Goal

Find out, read-only, what happens when a `tools-ki` release is cut, and why the website's CI was still pinned to `ki` v0.8.4. Kris believes, in their words on 2026-10-25: "when a release was cut, it did go to all those repos. I thought there was some kind of GitHub app that did that, including pushing it to homebrew tap and such."

## Do

1. Read `tools-ki`'s release workflows and scripts (`.github/workflows/`, release scripts, package scripts) and any GitHub App or token they use. List everything a release updates: the Homebrew tap formula, harness copies, consuming repositories' CI pins, anything else.
2. Check `homebrew-tap`'s history to see whether recent `tools-ki` releases reached it automatically.
3. For `apps-knowledgeislands.info`, find where its CI sets the `ki` version and whether any automation has ever bumped it, using `git log` on that file.
4. Check the last few `tools-ki` release runs on GitHub (`gh run list`, `gh release list`) for any fan-out step that failed or was skipped.
5. Note any written design for release fan-out in `tools-ki` docs, the harness or ki-principal Decision Records.

## Do not

Change, commit or push anything; trigger any workflow; or change GitHub settings. Another run, wow-ci-pins, is moving the CI pins now, so leave the workflow files alone.

## Report

The owner report. Done gives the findings plainly: what fans out today, what doesn't, and why the website pin lagged, each with its evidence path. Queries carries anything Kris must decide, each with Context, Query and Options, the recommended option first with its confidence and reason.
