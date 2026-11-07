---
id: ki.prj.stoa
state: with-worker
since: 2026-11-07T04:58:00Z
received: null
beat: null
mark: 2026-11-07T02:46:46Z
method_read: 0c498236
---

# ki.prj.stoa state

## Now

- Stoa 0.32.0 was released by ki.sop.main at 03:59 GMT (tag `v0.32.0`, commit `d534135`), in parallel with this work; this work's release run stood down without changing anything.
- `ki-prj-stoa/ki-repo-0-32-0` made `packages-stoa` a KI repository (`ki-repo-project` shape, `roadmap` adapter) in five commits after the release ([report](reports/ki-repo-0-32-0.report.md)).
- STOA-CMD-001 is `done`, accepted by `ki-prj-stoa/accept-cmd-001` in packages-stoa `c4d49ba` ([report](reports/accept-cmd-001.report.md)); the run is closed.
- Sent: STOA-0.32.0-NOTICE (MSG-bd634a00) to ki.sop.main for HNR, RELEASE-GO (MSG-4efdad1a) to ki.reg.main, STOA-SHAPE (MSG-6adb77c9) to ki.reg.guilds.
- Stoa is MIT-licensed, copyright Kris, in packages-stoa `a50b307` ([report](reports/licence-mit.report.md)); GitHub's licence field clears once GitHub reads the pushed file.
- Kris took STOA-AUDIT-REST b) at 04:57 GMT: everything is Stoa, house conventions throughout ([decisions](decisions.md)). Running in sequence: `stoa-names` (no portal-framework name left, decision records into the Stoa scope), `stoa-toolchain` (scripts and tooling on the house conventions) and `stoa-github` (GitHub settings and the final audit).

## Next steps

1. On the three runs' reports: send the old-to-new decision-record ids and the Breaking `PORTAL_FRAMEWORK_CHECKOUT` change to HNR through ki.sop.main, send stoa-toolchain's adaptations to ki.reg.guilds for the package-repository skill, and ask Kris whether to release 0.33.0 for the vendored changes.
2. Take the remaining [messages](messages.md) lines in queue order: STOA-HEADING-LINKS, STOA-NO-CONSUMERS and its addendum, PRINT-LAYOUT, STOA-CANCELLED, STOA-ICAL-MAPPING, STOA-HANDOVER, STOA-HEADER, STOA-THEME-MENU-CONTRAST, STOA-DIAGRAM-OVERLAY, STOA-TOOLING, STOA-LEGAL, STOA-LINES (MSG-d7d46e9f) and PAGE-TYPES-ADOPT (MSG-8b4360dd).
3. Briefs no longer promise "push nothing": the scheduled `mgit sync --push` job publishes any clean repository ahead of `origin` within minutes.

## Held

None
