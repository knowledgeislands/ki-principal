# wow-review-mgit-failed

## Goal

Give an independent view on one design question. Read nothing under `+/_WORK/` in ki-principal (no queries, decisions, reports or design notes); you may read `tools-mgit` source at `/Users/krisbrown/workspaces/knowledge-islands/tools-mgit` read-only.

## Context

A proposed mgit feature: `mgit --to-cache <sweep>` records the set of checkouts the sweep shows as needing attention (for example `st` lists only non-level checkouts), valid for five minutes; `mgit --from-cache <command>` then runs the command only in that set, for example `mgit --to-cache st && mgit --from-cache push`. A sweep can fail in a checkout, for example on an `index.lock`, a missing upstream or a broken worktree. The sweep's own exit status is 1 when any checkout fails, which already stops an `&&` chain, so `--from-cache` is reached after a failure only by `;` or a separate command. The follow-up may be destructive (for example `reset --hard`).

## Query

Should checkouts whose sweep failed be included in the cached set?

## Options (unranked)

- Include them, and show the count of failed candidates in the age line.
- Exclude them, so the set holds only checkouts that ran and printed something.
- Make `--from-cache` refuse to run while the set records any failed checkout, until the sweep is repeated clean.

## Report

Owner report. Done gives your choice, a confidence (high, medium, low) and the reasons in three lines at most; name any option you would add. Write nothing anywhere.
