---
id: ki.prj.stoa
state: handoff-to-supervisor
since: 2026-11-07T05:22:00Z
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
- Kris took STOA-AUDIT-REST b) at 04:57 GMT. Done on packages-stoa `main`: no portal-framework name left and decision records in the Stoa scope (stoa-names), scripts and tooling on the house conventions (stoa-toolchain), GitHub settings aligned; the repository audit passes ([reports](reports/)).
- Sent STOA-NAMES (MSG-8209439c) to ki.sop.main for HNR and STOA-TOOLCHAIN (MSG-c0ddcf23) to ki.reg.guilds.
- With Kris: STOA-033 in [discussions](discussions.md).

## Next steps

1. On Kris's STOA-033 answer, brief the 0.33.0 release and send its notice through ki.sop.main, with the Breaking `PORTAL_FRAMEWORK_CHECKOUT` change.
2. Take the remaining [messages](messages.md) lines in queue order: STOA-HEADING-LINKS, STOA-NO-CONSUMERS and its addendum, PRINT-LAYOUT, STOA-CANCELLED, STOA-ICAL-MAPPING, STOA-HANDOVER, STOA-HEADER, STOA-THEME-MENU-CONTRAST, STOA-DIAGRAM-OVERLAY, STOA-TOOLING (its item 2 is now done), STOA-LEGAL, STOA-LINES (MSG-d7d46e9f) and PAGE-TYPES-ADOPT (MSG-8b4360dd).
3. Briefs no longer promise "push nothing": the scheduled `mgit sync --push` job publishes any clean repository ahead of `origin` within minutes.

## Held

None
