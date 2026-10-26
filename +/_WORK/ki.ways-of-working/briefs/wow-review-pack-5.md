# wow-review-pack-5 - one readable page for Kris

## Goal

Kris asked: "is there somewhere I can easily read and understand all of this?" Replace the stale `+/_WORK/ki.ways-of-working/design/review-pack.md` in ki-principal with one document Kris can read top to bottom, in plain British English, without opening anything else. Written for someone who has been away: define every term on first use (State of play, package, steward, route, pin, DESIGN-2 and so on), no unexplained jargon, short paragraphs.

## Sources

`state.md`, `decisions.md` (especially every entry from 25 and 26 October), `queries.md`, the briefs in `briefs/`, the report copies in the work folder and the design notes in `design/` (for mgit: `design/mgit-cache.md`; for the work model: `design/model-shape-report.md`; for unattended work: `design/unattended-work.md`). `ki agent status ways-of-working` for what is running.

## Shape

1. **In one page** - five or six bullets: where things stand and what Kris needs to do.
2. **What has been done** since 24 October, by theme (website docs, unattended rules, getting repositories green, the release, design work), each item in plain words with a link to the live page, commit or record, and failures stated beside the item.
3. **Decided today** - every answer Kris gave on 26 October, one line each, and what it set going.
4. **In flight** - each run launched or queued today and what it will deliver (the release v0.14.1 and fleet pins, hnr levelling and owner tracing, two harness batches, document-rule fixes, MOD-009 acceptance and the Valle Armonia pilot proposal, the tap log line).
5. **Your open decisions** - the ten queries still in `queries.md`, grouped by theme: mgit cache (MGIT-CACHE-SCOPE, MGIT-CACHE-FAILED); work model (STEWARD-FIELD); unattended work (UNATTENDED-AND-DUE-DATES, UNATTENDED-FIELD); website (AREA-COLUMN, REPO-STANDARDS-SET); standards (CLI-PREVIEW, LEGACY-PREFIX, PARTIAL-REPOS). Each theme opens with **The idea in brief**: what problem it solves, how it works today, and what the choice changes, with a worked example. For mgit in particular Kris asked "what are routes?" and to "deal with the concept first": explain the cache concept from scratch, then each of the six routes as one short paragraph with an example command, then which routes the two open queries choose between. Then each query verbatim from `queries.md`: Context, Query and Options, the recommendation first with its confidence. Do not change the options or recommendations.
6. **Glossary** of the terms used.

## Limits

- Write only `design/review-pack.md`; do not edit `queries.md`, `decisions.md`, `state.md` or any other repository.
- Commit by explicit path, push fast-forward only, never force or `--no-verify`.
- Never remove your own scratch directory with `rm`.

## Report

Owner report: Done (path to the pack and its section list), In Progress, Queries.
