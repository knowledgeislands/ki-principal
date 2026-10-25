# wow-release-runs - did recent tools-ki release deliveries fail quietly?

## Goal

Using read-only GitHub calls only, establish whether the last few `tools-ki` releases (at least v0.11.5, v0.12.0 and v0.13.0) delivered cleanly. Kris authorised these read-only calls on 2026-10-25: release and run metadata and job-log reads only.

## Known

wow-release-fanout found locally that a release runs `tools-ki`'s Release workflow. Its tap-notification job uses `ki-tools-release-bot` to dispatch to `knowledgeislands/homebrew-tap`. The tap also polls daily at 06:17 UTC, opens a formula PR and auto-merges it, and its CI notifies the one enrolled consumer, `knowledgeislands/apps-knowledgeislands.info`. The website's `update-tool-release.yml` then updates the catalogue. The bot commits `45393a2`, `a0aec08` and `f31b194` in the tap prove that delivery landed, but not whether it came from the dispatch or the poll.

## Do

With `gh release list`, `gh run list`, `gh run view` and `gh api` GETs, for each release: did the Release workflow's tap-notification job succeed, fail or skip? Did the tap's intake run from the dispatch or from the schedule? Did the tap CI's consumer notification and the website's receiver succeed? Check the harness's `update-ki-pin.yml` runs for the same releases as well.

## Do not

Trigger, re-run or cancel any workflow; change any setting, secret, variable or repository; or read credential values.

## Report

The owner report. Done gives one line per release per hop, saying succeeded, failed, skipped or recovered by poll, each with its run URL. Queries carries anything that needs fixing, each with Context, Query and Options, the recommended option first with its confidence and reason.
