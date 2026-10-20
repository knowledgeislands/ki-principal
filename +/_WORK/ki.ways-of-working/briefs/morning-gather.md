# morning-gather - collect the queries the overnight runs left for Kris

Work: `ki.ways-of-working` (KI > Model > Ways of working), package `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/`.

Kris returns this morning to a full Summary. Every query a run left for Kris must be in `queries.md` first, in the house shape.

## Do

1. Read `state.md`, `queries.md` and `decisions.md` in the package. Then read every report in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/` modified since 2026-10-20 00:00 BST, especially the burn-*, burn2-*, accept*-*, prune-links*, specifications and harness reports.
2. List every query or owner-only check still open, that is, not answered or settled in `decisions.md`. Known examples:
   - SITE-SOURCE (KI-WEBSITE-SITE-044 citation remedy and 1440/390 px checks);
   - SPEC-SKETCH (already reviewed, high);
   - ki-design's MAP-002 timing, sizes tidy and stale dispositions;
   - Rig attended checks (KI-TOOL-RIG-CORE-047, -062, -068, -069);
   - KI-PRINCIPAL-OPS-014 render checks;
   - KI-TOOL-TECHNE-CLI-006 review;
   - KI-TOOL-RIG-CORE-053's observe-only shape;
   - GRANT-INTERIM.

   Confirm each against its source rather than trusting this list.
3. Write each into `queries.md` under its stable mnemonic tag, in this shape:
   - `### <TAG> - <plain title>`;
   - `**Context:**`, enough to decide without reading anything else, with every record linked by absolute local path;
   - `**Query:**`, in one sentence;
   - `**Options:**` with lettered lines, `a) (recommended, confidence <level> - <reason>) ...` first.

   Group several attended checks on one repository into one query where that reads better. Keep FOOTER-PROVISIONALS and OBS-ACT-VISUAL. Leave `## Parked` alone.
4. Note under each query whether it has already been blind-reviewed (and by which run) or still needs it.
5. Commit only `queries.md` by explicit path, with the hook in force. Do not push.

## Bounds

- Do not edit `state.md`, `decisions.md` or `messages.md`.
- Create no record and change no repository other than this commit.
- Write British English with ASCII hyphens only.

## Report

The owner-report shape at your report path: Done, In Progress, Queries. Under Done, list the tags written and which still need review.
