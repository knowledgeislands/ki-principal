---
id: ki.prj.stoa
state: handoff-to-supervisor
since: 2026-11-07T02:50:52Z
received: null
beat: null
mark: 2026-11-07T02:46:46Z
method_read: 0c498236
---

# ki.prj.stoa state

## Now

- Opened by Kris on 7 November 2026 at 02:44 GMT: "Release Stoa 0.32.0 now under STOA-RELEASE: accept STOA-CMD-001 and cut the release." Logged in [decisions](decisions.md).
- Blocked: the release run `ki-prj-stoa/release-0-32-0` passed every check but stopped at acceptance, because `packages-stoa` has no `.ki.toml` for `ki-accept`; nothing was released. Its [report](reports/release-0-32-0.report.md) is homed, and STOA-ADAPTER is with Kris in [discussions](discussions.md).

## Next steps

1. On Kris's STOA-ADAPTER answer, relaunch the release brief as he directs. Once released: send the release notice through ki.sop.main for hnr.sop.main (ACK MSG-d56132fe, version, re-vendor-and-reconcile line for HNR's consumers) and hnr.sop.5ge (STOA-ICONS), tell ki.reg.main that RELEASE-GO is answered, then remove the STOA-RELEASE and STOA-ICONS lines from [messages](messages.md).
2. Take the remaining [messages](messages.md) lines in queue order: STOA-HEADING-LINKS, STOA-NO-CONSUMERS and its addendum, PRINT-LAYOUT, STOA-CANCELLED, STOA-ICAL-MAPPING, STOA-HANDOVER, STOA-HEADER, STOA-THEME-MENU-CONTRAST, STOA-DIAGRAM-OVERLAY, STOA-TOOLING, STOA-LEGAL, STOA-LINES (MSG-d7d46e9f) and PAGE-TYPES-ADOPT (MSG-8b4360dd).

## Held

None
