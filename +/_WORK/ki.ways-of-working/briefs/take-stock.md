# take-stock

Work: ki.ways-of-working. Authorised by Kris at 02:10 BST: "Okay, they've all done that now. Can you have a look at it?", after TAKE-STOCK ("let's just take stock on what's working well and what's not working well so we can improve our ways of working").

## Task

1. Find every `+/_WORK/*/design/retro-2026-10-20.md` across `/Users/krisbrown/workspaces` (about 10 files; list any live work folder in a capital that has none). Read each in full, and each work's `state.md` front matter for context.
2. Write `+/_WORK/ki.ways-of-working/design/take-stock-2026-10-20.md` in ki-principal:
   - one line per source, linked by absolute path;
   - Working well: the themes worth keeping, each with how many works raised it and one cited incident;
   - Not working: themes ranked by how many works raised them and how much they cost (lost time, blocked commits, wrong work), each with cited incidents and its likely root cause (tooling, standard, coordinator behaviour, shared checkout, owner interface);
   - Would change: proposed changes grouped by owner (harness standard, `ki` CLI, Rig, coordinator style, Kris's interface), deduplicated, each with which theme it fixes.
3. In the report, put the five to eight highest-value changes as queries, each with a recommendation and confidence. Do not apply any change.

## Rules

- Read-only except the one design file. Commit it by explicit path in ki-principal; do not push if other sessions' commits are stacked, and name them once in Done. Never `--no-verify` or force-push.
- HOOK-GUARD: never run `ki repo conform` without `--dry-run`. CAPTURE-GATE: no new records.
- Stay out of ki-design and apps-knowledgeislands.info. British English, ASCII hyphens, they/them.

## Report

Owner-report shape: Done, In Progress, Queries (`<TAG> - <title>`, Context, Query, lettered Options with confidence).
