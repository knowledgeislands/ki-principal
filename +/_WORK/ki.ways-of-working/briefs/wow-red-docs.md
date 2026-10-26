# wow-red-docs - clear the document-rule failures in ki-design and ki-principal

Kris decided this on 26 October; the read-back is the "all" entry at the end of `+/_WORK/ki.ways-of-working/decisions.md` in ki-principal. Read it first. This is CI-RED-DOCS a), one bounded owner approval recorded in that log, standing in for an Enactment record for the mechanical fixes.

## Scope

Run `ki repo audit` in both repositories and list every failing finding with its path. Fix the mechanical ones (BODY-11, COORD-7, COORD-12, DEPENDS-4, FILENAME-0/1, FM-6, MD-mech, PRINCIPAL-5, ROUTE-1 and similar), verifying each fix class on one file before applying it widely. Return RECORD-2, FOLDER-1, STRUCTURE-1 and any work-package case as queries, unfixed. BIO-1's configuration migration in ki-design is out of scope; describe it as a query. Do not touch `+/_WORK/ki.ways-of-working/` files other than as a listed finding. Watch both CI runs.

## Limits

- Standing push rule: commit by explicit path, push fast-forward only, never force, never `--no-verify`; stop on divergence.
- No new software. No DNS, Cloudflare Access, routes, Zero Trust or credential changes. No messaging people; no Linear or Notion changes.
- Anything outside scope, or any failure with another cause, becomes a query (Context, Query, lettered Options, recommendation first with confidence); do not widen scope.
- Never remove your own scratch directory with `rm`.

## Report

Owner report: Done, In Progress, Queries.
