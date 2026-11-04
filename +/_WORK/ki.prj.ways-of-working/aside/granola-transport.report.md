# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › granola-transport

**🤖 → 👤 Handoff to supervisor · Run report at 21:18 GMT · last mark 21:18 GMT**

---

## Done

- **What went wrong.** The importer does not talk to Granola itself. It runs `mcporter` with `--no-oauth`, which means "never start a sign-in". mcporter passes the call to its background daemon, which keeps one shared connection open per server. A shared `--no-oauth` connection holds on to the access token it started with. That token was later rejected, and the connection has no way to renew it. Every call on it now fails. `CLIENT_HTTP_NOT_IMPLEMENTED` is just the MCP client library's generic label for "the server returned an error status". It does not mean an unsupported transport.
- **Why your sessions still worked.** The `ki-mcporter` session bridge connects without `--no-oauth`, so its shared connection can renew the token. A plain `mcporter call granola.… ` without the flag also worked.
- **The fix.** Commit `76fcdc48`, on `main` and pushed. The importer now sets `MCPORTER_DISABLE_KEEPALIVE=granola` on its mcporter calls. This is mcporter's documented switch for opening a fresh direct connection instead of the shared one. A fresh connection reads the current saved token each time and still never starts a sign-in. I changed no credential, sign-in, token or `~/.mcporter/mcporter.json`. A new test checks that the importer reaches Granola directly even if the environment already sets that switch for another server. The user guide explains the setting.
- **Checks.** Full suite passed (97 files, 2183 tests). Coverage gate passed. Type check passed. Lint and format passed. Commit hook passed.
- **Dry run for 2026-10-28 against `assistant`, from committed `main`.** It now connects to Granola, plans the day and exits 0. All three meetings are withheld for a separate reason, covered under Queries.

```text
Granola acquisition plan: https://github.com/krisb/assistant
Interval: 2026-10-28 through 2026-10-28 (complete identity enumeration)
Coverage: 3 discovered, 3 selected, 0 routed elsewhere
Routing: 0 unfoldered, 0 intentionally duplicated, 0 flagged without content acquisition
Meetings: 0 new, 0 refreshed, 0 kept, 3 withheld
Withheld: 0ab7a72d-b159-4132-9e79-4e4dd2f7a756 · Granola lists 0 screenshots but the detail names 20 screenshot attachments; not captured until they match
Withheld: 4ffa813b-68a8-4bf0-b798-4793546c4d3a · Granola lists 0 screenshots but the detail names 20 screenshot attachments; not captured until they match
Withheld: 638cd82c-8d2e-48b8-a814-2010c20d6fc4 · Granola lists 0 screenshots but the detail names 12 screenshot attachments; not captured until they match
Omissions: 0
Attachments: 0 screenshots across 0 verified MCP inventories
Acquired: 0 skipped on Acquired folder membership
Boundary: read-only Granola MCP; no source mutation, harvesting, cross-repository write, archive, or deletion.
Dry run: no repository files written.
```

- I ran the dry run from the tools-ki source. The installed `ki` is unchanged, since the brief allowed no release or install, so it still fails the old way until the next release.

## In Progress

Nothing.

## Queries

### Q1 - Granola's meeting list no longer gives a screenshot count

**Context**

The importer only captures a meeting's screenshots when two numbers agree. One is the screenshot count in Granola's meeting list. The other is the number of screenshots named in the meeting's detail. Granola's list no longer has a `screenshot_count` field, so the importer reads it as 0 and withholds every meeting that has screenshots. The list now has an `attachment_count` field instead, and it counts more than screenshots. For 28 October it shows 26, 25 and 12, while the details name 20, 20 and 12 screenshots. Granola's own description says attachments include photos the user attached, as well as shared-screen screenshots. Simply reading the new field would still withhold two of the three meetings. This changes the importer's safety check, which is a judgement call and beyond this transport brief, so I have not changed it.

**Query**

How should the importer check screenshots now that Granola only gives a total attachment count?

**Options**

a) (recommended, confidence medium - this keeps a real cross-check against Granola's own inventory and still withholds on any true mismatch) Treat the full attachment list from Granola's attachment tool as the reference. Check that the screenshots plus photos it returns add up to `attachment_count`, and capture the screenshots. This would be a bounded tools-ki run with tests.

b) Read `attachment_count` and accept a meeting when its screenshots are no more than that count. This is quicker but a weaker check.

c) Leave the importer as it is and ask Granola whether `screenshot_count` is coming back. Meetings with screenshots stay withheld until then.
