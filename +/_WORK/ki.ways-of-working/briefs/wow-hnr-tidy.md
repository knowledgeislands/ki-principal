# wow-hnr-tidy - level hnr-principal and find two owners

Kris decided this on 26 October; the read-back is the "all" entry at the end of `+/_WORK/ki.ways-of-working/decisions.md` in ki-principal. Read it first.

## Scope

1. HNR-LEVEL: confirm `/Users/krisbrown/workspaces/humans-not-robots/hnr-principal` is clean, has no stash, and that its one local commit `6043f001` adds only a line present byte-identical on `origin/main` (`bb404954`). If so, fetch and run `git -C /Users/krisbrown/workspaces/humans-not-robots/hnr-principal reset -q --keep origin/main`. If anything differs, stop and query.
2. TIDY-GAPS, read-only: from Git history and the work packages, find which work owns `+/_WORK/ki.specifications/` in ki-principal (it has no work.md), and where `radar-confirm-2.report.md` cited by KI-HARNESS-REV-012 in ki-agentic-harness came from and where it should live. Report the evidence and a recommended owner for each as queries. Change nothing for this step.

## Limits

- Standing push rule: commit by explicit path, push fast-forward only, never force, never `--no-verify`; stop on divergence.
- No new software. No DNS, Cloudflare Access, routes, Zero Trust or credential changes. No messaging people; no Linear or Notion changes.
- Anything outside scope, or any failure with another cause, becomes a query (Context, Query, lettered Options, recommendation first with confidence); do not widen scope.
- Never remove your own scratch directory with `rm`.

## Report

Owner report: Done, In Progress, Queries.
