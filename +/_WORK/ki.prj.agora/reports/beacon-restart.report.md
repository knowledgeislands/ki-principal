# KI > Techne > Agora › beacon-restart

**🤖 → 👤 Handoff to supervisor · Run report at 03:14 GMT · last mark 00:04 GMT**

---

## New and noteworthy

The Beacon opens its local stream before startup synchronisation and its first review. The Atlas accepted each startup state as live, replacing its last full picture with empty collections. The existing timing.reviewedAt already records review completion but was not used by the feed.

Lands and fallback jobs read local sources, not the Beacon, so its outage does not itself make those reads fail. Their refreshes nevertheless had no reconnect trigger.

## Done

Commit `0d057c2` marks startup views as warming, preserves the Atlas’s last reviewed picture through outages and warming, and shows that picture’s time in the existing Beacon status.

Recovery refreshes lands and jobs immediately after the full view is accepted; subsequent live updates keep the normal intervals.

Tests cover restarting the test server, retained pictures, first-launch warming, older Beacons, recovery ordering, status wording and the warming flag; README and the view contract are updated.

`bun run self:check`: passed against committed main plus this run’s files in an isolated temporary copy.

`bun run test`: passed in that same copy, all 537 tests across 55 files.

Commit hooks passed; inspection confirmed only the twelve intended paths were committed. No app was installed, packaged, launched, stopped or replaced.

The reserved guild and skill-table files were left untouched; the fast-forward pull explicitly disabled rebase and autostash to preserve them.

## In Progress

Nothing running. Delivery awaits the supervisor’s review.

Outstanding — no action requested now: shared-checkout checks encounter the other run’s guild changes: self:check reports a missing findSkills export, and the guild table test fails. Isolated verification excludes those four reserved files’ uncommitted changes.

## Queries

None.

🧵 ki.prj.agora
