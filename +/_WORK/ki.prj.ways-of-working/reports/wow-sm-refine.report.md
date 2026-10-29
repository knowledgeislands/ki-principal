# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-sm-refine

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 21:20 GMT · last mark 21:20 GMT**

---

## Done

- Refined the [work state machine](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md) under STATE-MACHINE-REFINE. The changes are in the note, the [HTML](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.html) and the [SVG](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/work-state-machine.svg). There is no architecture JSON for this diagram.
  1. `hold` now starts from With worker, With supervisor or Handoff to supervisor, and the drain stops runs on the way. The "first a receive" wording is gone.
  2. `release` is replaced by `resume`, On hold → Bootstrap, with the release condition as its precondition. The planned host move now reads hold → On hold → resume on the new host → Bootstrap → pick up. "Not from On hold" is gone from re-bootstrap. The HOST-MOVE-PATH option and the ARC-NAMES context are updated to match.
  3. The `drain blocked` arc is removed. The hold row and the portability checks now say that a hold that cannot drain does not complete: the work stays in its source state, marked blocked, and the report gives `NOT DRAINED` and what blocks.
- Diagram: guard labels added (`hold · portable` and `resume · released`), with `finish` kept short. To fit the width limit, On hold now sits on the main row between With supervisor and Finished, and the state sublabels were dropped. The diagram passed all of Archify's automated checks, and I looked over the exported SVG myself.
- Committed as 1228b82d (`docs(work): ki.prj.ways-of-working refine work state machine`), local only. The repository audit hook passed.
- Not published: the pull would not fast-forward. Local `main` has two commits that are not on origin: 2457c0a2, the coordinator's STATE-MACHINE-REFINE log entry, and my 1228b82d. Origin has five newer commits that change `decisions.md`, `queries.md` and `state.md` in this package. I stopped there, as the brief says.

## In Progress

Nothing is running.

Outstanding - no action requested now: the arc pre- and postconditions on click or hover (part of item 4) are not in the HTML. See ARC-HOVER. Until then, the note points readers to the Transitions table.

## Queries

### PUSH-DIVERGED - Rebase the two unpublished package commits onto origin

**Context:** Local `main` in ki-principal has the coordinator's 2457c0a2 and this run's 1228b82d, and origin has five newer commits. Both sides touch the `ki.prj.ways-of-working` package, and `decisions.md` changes on both. My commit touches only the three `design/work-state-machine.*` files, which origin has not changed. The brief allows only fast-forward, and a rebase would carry the coordinator's own commit, which is outside this run's ownership.

**Query:** Should a bounded resolve run rebase both unpublished commits onto origin and push?

**Options:**

a) (recommended, confidence medium - my files do not overlap origin's, and only `decisions.md` might conflict, an append-only log) Launch a bounded resolve run that runs `git pull --rebase --no-autostash`, stops on any conflict in another session's content and pushes fast-forward.

b) The coordinator rebases its own 2457c0a2 first, then this commit follows.

### ARC-HOVER - How to show arc conditions on click or hover

**Context:** Archify's lifecycle diagram can attach a note to an arc, but it still makes room for the note in the layout even when the note is hidden until you zoom in or focus the arc. Notes with the pre- and postconditions made the diagram 2447px wide, against a 1395px limit, and it failed its checks. The only other route is to add tooltips to the HTML after Archify's checks have run, which would invalidate its record that the HTML passed them.

**Query:** How should the arc conditions be shown in the interactive view?

**Options:**

a) (recommended, confidence low - keeps the HTML as Archify checked it, and the table already holds every condition) Leave the conditions in the note's Transitions table, linked from the diagram, and raise arc notes that don't take layout space as an Archify feature request.

b) Add hover tooltips to the HTML after Archify's checks run, accepting that its record of the passed checks no longer matches the file.
