---
note_type: stream-roadmap
id: KI-PRINCIPAL-MOD-012
area: MOD
title: Hold states and values
priority: medium
size: s
status: triage
assignee: owner
blocks: []
blocked_by: []
created_at: 2026-11-07T05:32:00Z
updated_at: 2026-11-07T05:32:00Z
---

# Hold States and Values in the Work Process Note

## Goal

The [Work Process](<../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note draws how work flows between its seven states, says what each kind of hold lets through and who may set it, including the worker's own idle hold, and holds the work model's shared values once, for work packages to link.

## Context

ki.reg.guilds drafted the changes and asked, in MSG-fa716bdc of 7 November 2026, that they reach Knowledge Islands Principal under one Enactment record. The draft is pinned at [enactment-hold-and-values.md at ki-agentic-harness `f488f951`](https://github.com/knowledgeislands/ki-agentic-harness/blob/f488f951/+/_WORK/ki.reg.guilds/skills/enactment-hold-and-values.md); its exact proposed wording governs, and this record summarises it.

It carries decisions Kris took on 7 November 2026 in the guilds' interactive pass: HOLD-STATES a), whose Work Process note changes go "under one Enactment record"; VALUES-HOME a), "Write once in the Work Process note under an Enactment record, and give `work.md` an optional one-line `## Values` section linking them and adding any of its own"; and HOLD-DIAGRAM a), "Mermaid, the diagram written as text, in the Work Process note under the seven states, with a plain-text version beside it". SNOOZE, SNOOZE-STATE and SNOOZE-HEADING of 6 November 2026 already renamed "more expected" to Snoozing in the note. The harness side has landed in `ki-coordination`'s Putting work on hold and `ki-work-package`'s Work file sections; the note follows their words where they overlap.

## Boundary

- In: the note's seven states section and a new Values section in its Overview.
- Out: levels, roles, homes and the banner section, beyond the Snoozing heading's idle form.
- Out: the harness standards, already landed, and every work package's own `work.md`, each adopting the optional `## Values` line in its own time.

## Proposed changes

1. **Seven states table.** The On hold row reads "On hold, paused or snoozing", entered when agreed and drained, or by the worker's own idle hold with nothing running, queued or in handoff; the sentence under the table adds the worker's idle hold as the one exception to "only the supervisor's receive and hold are set".
2. **On hold paragraph.** Add the idle hold, `💤 Snoozing (on hold) · idle`, which a worker may set only when nothing runs or is queued, nothing is handed off, no message is unread, no query is with the supervisor and everything is pushed; it needs no drain or hold report, and the supervisor's `pause`, `done for now` or `snooze` turns it into the supervisor's form. Say a paused hold stays closed to every line, urgent and important included, an important line going to the supervisor as a `resume` question; and that before any hold the work folder keeps nothing already dealt with. In Stuck and heartbeat, listening stops while draining and while paused, and a snoozing hold, idle included, keeps listening where the thread's listening is switched on.
3. **State flow.** Under the seven states table, a Mermaid flow diagram with a plain-text version beside it, drain shown as an activity inside With worker, never a state.
4. **Values.** A `## Values` section in the Overview holding the five values once: start finishing, stop starting; deliver often and soon ready; you build it, you run it; continual improvement; and cross-functional work, adopted by Kris from Humans not Robots' development process on 3 November 2026 under VALUES-UP-FRONT and homed here under VALUES-HOME on 7 November 2026.

The draft also records an exception, HOLD-TERRA a): `personal.reg.household-terra` set its own hold on 3 November 2026 before the note allowed one; it stands and is re-recorded as an idle hold, or returned to the supervisor if it no longer meets the five conditions. That is the household package's own move and no change to canonical content.

## Steps

- [ ] Kris adopts this record and reviews the draft's exact wording through the Enactment Process.
- [ ] Re-ground the draft against the current note, whose Stuck and heartbeat wording has moved on since the draft quoted it, and confirm the four changes still apply.
- [ ] Apply the four changes to the Work Process note, then check the diagram renders and matches the plain-text version and the harness wording.
- [ ] Present the change for separate review and acceptance.

## Verify

`rumdl check` passes on the note; the Mermaid block renders; each relative link resolves; the note's wording matches `ki-coordination` and `ki-work-package` where they overlap.

## Governance

This roadmap record adheres to the [Enactment Process](<../../Admin/Operations/Processes/Enactment Process.md>). Move content to `Admin/`, `Pillars/`, or `Resources/` only on user approval of a `ready` record. Kris's HOLD-STATES a) answer of 7 November 2026 asks for this record; adoption, the exact wording and acceptance are separate owner decisions.
