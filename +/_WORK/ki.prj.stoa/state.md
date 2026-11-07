---
id: ki.prj.stoa
state: with-worker
since: 2026-11-07T04:08:00Z
received: null
beat: null
mark: 2026-11-07T02:46:46Z
method_read: 0c498236
---

# ki.prj.stoa state

## Now

- Opened by Kris on 7 November 2026 at 02:44 GMT: "Release Stoa 0.32.0 now under STOA-RELEASE: accept STOA-CMD-001 and cut the release." Logged in [decisions](decisions.md).
- The first release attempt stopped at acceptance: `packages-stoa` had no `.ki.toml` ([report](reports/release-0-32-0.report.md)). Kris answered STOA-ADAPTER at 04:07 GMT: Stoa becomes a KI repository ([decisions](decisions.md)).
- Running: `ki-prj-stoa/ki-repo-0-32-0` declares `packages-stoa` a KI repository on the tools shape and fixes its audit findings, local commits only; `ki-prj-stoa/release-0-32-0` is relaunched, held until it finishes, then accepts STOA-CMD-001, releases 0.32.0 and pushes.
- Sent REPO-SHAPE-PACKAGES (MSG-4b6a0c4e) to ki.sop.main: Kris's idea of a repository-shape skill for package repositories.

## Next steps

1. On the runs' reports: send ki-repo-0-32-0's STOA-SHAPE finding to ki.sop.main for REPO-SHAPE-PACKAGES. Once released: send the release notice through ki.sop.main for hnr.sop.main (ACK MSG-d56132fe, version, re-vendor-and-reconcile line for HNR's consumers) and hnr.sop.5ge (STOA-ICONS), tell ki.reg.main that RELEASE-GO is answered, then remove the STOA-RELEASE and STOA-ICONS lines from [messages](messages.md).
2. Take the remaining [messages](messages.md) lines in queue order: STOA-HEADING-LINKS, STOA-NO-CONSUMERS and its addendum, PRINT-LAYOUT, STOA-CANCELLED, STOA-ICAL-MAPPING, STOA-HANDOVER, STOA-HEADER, STOA-THEME-MENU-CONTRAST, STOA-DIAGRAM-OVERLAY, STOA-TOOLING, STOA-LEGAL, STOA-LINES (MSG-d7d46e9f) and PAGE-TYPES-ADOPT (MSG-8b4360dd).

## Held

None
