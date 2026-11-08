# KI > Techne > Agora › kiv-e2e

**🤖 → 👤 Handoff to supervisor · Run report at 20:44 GMT · last mark 00:04 GMT**

---

## New and noteworthy

The KIV viewer's checks now all pass on sol, so [PERSONAL-INBOX-PRO-002](/Users/krisbrown/kis/personal/inbox/docs/roadmap/PERSONAL-INBOX-PRO-002-finish-viewer-waiting-asks.md) is clear to be reviewed for acceptance by another session. No browser test reads the live work packages any more.

## Done

- `a7be881a`: the browser tests now use the same sample data as the unit tests. The sample packages the unit tests wrote inline now live in a new shared file, `packages/kiv/stand-in.ts`. The browser suite's start command now starts two viewers: one serving the checkout on port 4848 and one serving the sample packages on 4849. The Focus, Workers and Packages tests in `e2e/focus.e2e.ts` use the second viewer. Five checks that expected details only the live packages have now expect what the sample shows: the kiv card's title, the "in progress" group (now "active"), the listening badge (dropped), the date-dependent "since" (now "with worker") and the capitalised territory name. The README now describes the second viewer. The viewer's own behaviour is unchanged.
- `a3c69889`: re-baselined the macOS screenshots of the navigation rail, expanded and contracted. The old pictures predated three intended layout changes: the collapse switch moved under the brand (`a32915c1`), the collapsed rail got shorter section labels (`6dd2ab3f`), and the Now page was added to the menu (`ee20d1f2`). The key-page and tray comparisons already passed and were left as they were.
- PRO-002's Verify checks, as the record states them, run on sol with `ki` installed:
  - `bun run self:typecheck`: passed.
  - `bun run test`: passed, 242 of 242.
  - `bun run self:kiv:e2e`: passed, 12 of 12, up from 10 of 12.
  - `bun run self:kiv:e2e:visual`: passed, 3 of 3, up from 2 of 3.
  - Biome on the changed TypeScript: passed.
- Outside the record's checks, rumdl passed on the README.
- Knip, an unused-code checker that is not one of the record's checks, reports two unused exports in viewer code this run did not touch: `PILLARS` and `GlyphName`. Both were there before this run.
- Both commits are pushed.

## In Progress

None.

## Queries

### Q1 - Do the checks also need a run on terra?

**Context:** The record's Verify section says the checks pass "on terra". This run was on sol. The Linux screenshots made in a cloud session were not regenerated, and terra's macOS pictures are now the ones made on sol.

**Query:** Can the session that accepts the record take the sol results, or does it need the four checks rerun on terra first?

**Options:**

a) (recommended, confidence medium - the browser tests no longer depend on which machine runs them, but a different Mac can still render pixels slightly differently) Rerun only `bun run self:kiv:e2e:visual` on terra before acceptance, and accept on the sol results for the rest.

b) Accept on the sol results alone.

c) Rerun all four checks on terra, and regenerate the Linux pictures in a cloud session, before acceptance.

🧵 ki.prj.agora
