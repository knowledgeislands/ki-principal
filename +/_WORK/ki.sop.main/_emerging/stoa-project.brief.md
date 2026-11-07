# Brief: stoa-project

From ki.sop.main (Knowledge Islands State of play), run `stoa-project`. Work in `~/kis/knowledge-islands/ki-principal`; one line each in other repositories' `messages.md` only as named below.

## Authority

Kris took STOA-PROJECT a) on 2026-11-07 in these words: "Yeah, definitely go ahead on those. I thought we were already doing it." Logged in `+/_WORK/ki.sop.main/decisions.md`. The query's text is under `### STOA-PROJECT` in `+/_WORK/ki.sop.main/discussions.md`.

## Task

1. First check whether a Stoa Project or work package already exists anywhere in the estate (`~/kis/*/*/+/_WORK/*stoa*`, `packages-stoa`, Project notes in `Streams/Projects/`, the ki registry via `ki --help`). If one exists, adopt it rather than duplicate, and say so.
2. Register the Stoa Project in Knowledge Islands Principal the way existing Projects are registered (follow `ki-work-package` and an existing Project note such as Agora's or Ways of working's, including any registry entry `ki` reads). Repository owned: `knowledgeislands/packages-stoa`.
3. Seed its package `+/_WORK/ki.prj.stoa/` with the five files: minimal `work.md` definition (goals from the queued lines, scope Stoa the shared site package), empty queries and decisions, `state.md` with `state: on-hold`, `hold.reason: paused`, `hold.release: when Kris opens this Project work`.
4. Move into its `messages.md` `## Inbound`, in their original order and wording, every Stoa line now in `+/_WORK/ki.sop.main/messages.md` Inbound (STOA-NO-CONSUMERS and addendum, PRINT-LAYOUT, STOA-CANCELLED, STOA-ICAL-MAPPING, STOA-HANDOVER, STOA-HEADER, STOA-THEME-MENU-CONTRAST, STOA-DIAGRAM-OVERLAY, STOA-TOOLING, STOA-LEGAL, MSG-d7d46e9f STOA-LINES, MSG-d56132fe STOA-RELEASE, MSG-8b4360dd PAGE-TYPES-ADOPT) and the STOA-ICONS lines routed on 30 October wherever they sit; remove each moved line from ki.sop.main's messages.md. Leave every other line untouched (MSG-7ab0b624 MAIL-GAPS stays).
5. In `+/_WORK/ki.sop.main/discussions.md`, remove the `### STOA-PROJECT` query section only.
6. Tell each sender once, as a line at the top of its package's `## Inbound` (removing a `None.` placeholder): `- 2026-11-07 · STOA-ROUTED · from ki.sop.main · <HH:MM GMT> · your Stoa lines (<tags>) now sit in ki.prj.stoa (ki-principal `+/_WORK/ki.prj.stoa/`), on hold until Kris opens it`. Senders: hnr.sop.sites, hnr.sop.5ge, hnr.sop.main (all in `~/kis/humans-not-robots/hnr-principal`), lgl.sop.main (`~/kis/legal/legal-principal`), and whoever sent STOA-ICONS. hnr.sop.sites asked for the package id back: its line carries it.

## Commit

In each repository: pull with `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`; `rumdl fmt` then `rumdl check` on touched Markdown; commit by explicit path (git add new files first), lower-case Conventional Commit subject such as `docs(work): ki.prj.stoa seed on hold with routed stoa lines`, trailer `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; push fast-forward only. Never stash, rebase, reset, force or `--no-verify` in any primary checkout; on divergence stop and report. A refused commit is a failure to report. Touch no other session's uncommitted files.

## Report

Write your report where the launcher's footer says: Done, In Progress, Queries; list the package path, each moved line, each sender told, and each commit.
