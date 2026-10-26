# wow-tap-log - make the release dispatch line visible from the command line

Kris decided this on 26 October; the read-back is the "all" entry at the end of `+/_WORK/ki.ways-of-working/decisions.md` in ki-principal. Read it first.

## Scope

SUMMARY-VISIBLE a): in homebrew-tap, the Notify job also prints "Dispatched <tool> <version> to <consumer>" to its log as well as the job summary; point tools-ki's release guide step 6 at the log line. No behaviour change. Verify with a dry or replayed run that the line appears in `gh run view --log`.

## Limits

- Standing push rule: commit by explicit path, push fast-forward only, never force, never `--no-verify`; stop on divergence.
- No new software. No DNS, Cloudflare Access, routes, Zero Trust or credential changes. No messaging people; no Linear or Notion changes.
- Anything outside scope, or any failure with another cause, becomes a query (Context, Query, lettered Options, recommendation first with confidence); do not widen scope.
- Never remove your own scratch directory with `rm`.

## Report

Owner report: Done, In Progress, Queries.
