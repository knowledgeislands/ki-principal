---
id: ki.prj.stoa
state: with-worker
since: 2026-11-08T12:20:00Z
received: null
beat: null
mark: 2026-11-07T02:46:46Z
method_read: d5ede6dd
---

# ki.prj.stoa state

## Now

- Draining for Kris's host move (8 November, 12:22 GMT: "drain down ready to stop working, we are moving host in some way"). No new launches. The away window Kris granted at 12:20 GMT ended with that message.
- Running: `ki-prj-stoa/stoa-capture-draft`, drafting roadmap records for the 14 Stoa inbox requests; it writes no repository, and its report carries the drafts (finding STOA-DRAFTS) so they travel with this package.
- Stoa 0.33.0 was released on 7 November at 10:34 GMT by another session (`b378ee1`, tag `v0.33.0`), with the Header top bar and modal frame and this work's clean-up; STOA-033 is moot. Whether its consumer notice went out is unchecked.
- Done earlier: 0.32.0 out, STOA-CMD-001 accepted, packages-stoa a KI repository under MIT with the house toolchain, no portal-framework name, GitHub aligned ([reports](reports/)).

## Next steps

1. Receive `stoa-capture-draft`: review its STOA-DRAFTS, capture the records into `packages-stoa/docs/roadmap/` as this work's capture under STOA-WINDOW, adopt them to `next`, and remove each inbox line it covers, naming the record.
2. Plan the records to Ready under ki-plan, then deliver the small ones in frozen waves to `awaiting-review` (no release, Kris accepts); plan the design ones only (heading links, page types, print layout, diagram overlay). This needs Kris to re-grant a window on the new host.
3. Check whether hnr.sop.main got a 0.33.0 notice with the Breaking `PORTAL_FRAMEWORK_CHECKOUT` change; send one through ki.sop.main if not.
4. Briefs no longer promise "push nothing": the scheduled `mgit sync --push` job publishes any clean repository ahead of `origin` within minutes.

## Held

None
