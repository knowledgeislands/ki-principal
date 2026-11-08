---
id: ki.prj.stoa
state: handoff-to-supervisor
since: 2026-11-08T12:27:00Z
received: null
beat: null
mark: 2026-11-07T02:46:46Z
method_read: d5ede6dd
---

# ki.prj.stoa state

## Now

- Drained for Kris's host move (8 November, 12:22 GMT: "drain down ready to stop working, we are moving host in some way"). No new launches. The away window Kris granted at 12:20 GMT ended with that message.
- `stoa-capture-draft` finished: 15 draft records (10 small, 5 design) are in its [report](reports/stoa-capture-draft.report.md) as finding STOA-DRAFTS, nothing captured yet; STOA-AREAS and STOA-TOOL-SCOPE are with Kris in [discussions](discussions.md). DRAINED: nothing runs.
- HNR released Stoa 0.34.0 and 0.35.0 in packages-stoa on 8 November at Kris's word (STOA-UPSTREAM and STOA-DUOTONE in [messages](messages.md), not yet received).
- Stoa 0.33.0 was released on 7 November at 10:34 GMT by another session (`b378ee1`, tag `v0.33.0`), with the Header top bar and modal frame and this work's clean-up; STOA-033 is moot. Whether its consumer notice went out is unchecked.
- Done earlier: 0.32.0 out, STOA-CMD-001 accepted, packages-stoa a KI repository under MIT with the house toolchain, no portal-framework name, GitHub aligned ([reports](reports/)).

## Next steps

1. Receive STOA-UPSTREAM and STOA-DUOTONE. Then, on Kris's STOA-AREAS and STOA-TOOL-SCOPE answers, review STOA-DRAFTS against 0.35.0, capture the records into `packages-stoa/docs/roadmap/` as this work's capture under STOA-WINDOW, adopt them to `next`, and remove each inbox line it covers, naming the record.
2. Plan the records to Ready under ki-plan, then deliver the small ones in frozen waves to `awaiting-review` (no release, Kris accepts); plan the design ones only (heading links, page types, print layout, diagram overlay). This needs Kris to re-grant a window on the new host.
3. Check whether hnr.sop.main got a 0.33.0 notice with the Breaking `PORTAL_FRAMEWORK_CHECKOUT` change; send one through ki.sop.main if not.
4. Briefs no longer promise "push nothing": the scheduled `mgit sync --push` job publishes any clean repository ahead of `origin` within minutes.

## Held

None
