# wow-sm-polish - finish and beautify the Archify work state machine

Kris finds the Mermaid sketch (`design/work-state-machine.mmd`) ugly; it holds the agreed shape. Bring the Archify version (`design/work-state-machine.{html,svg,md}`, `archify` skill, `ki-diagrams` standard) up to that shape and make it look excellent:

- Apply WORKING-EXIT (decisions.md): inside Working add a final state End (work); `conclude` arcs into it from With worker and from With supervisor; the only exit from Working is End (work) -stop · drain, portable-> At rest (move the stop arc to leave from End (work)).
- Draw Handoff to supervisor and Handoff to worker as transitional states, visibly lighter (dashed or muted) than the stable With worker and With supervisor; say so in the States table and legend.
- Keep everything already there: Start (wp) -open-> Bootstrap -ready-> Start (work) -[work clearly defined] pick up / [needs more clarity] refine->; the inform/receive/direct/receive cycle; At rest with holding · waiting · moving; resume -> Bootstrap; finish -> Finished (terminal); roles legend.
- Layout for legibility: the four-state cycle as a clear square loop inside Working, entry on its left, exit on its right; no crossing arcs; label every arc; use Archify's best quality setting and pass all its gates. Export the SVG as the standard describes.
- Update the note's tables for End (work) and conclude, with preconditions, work and postconditions.

Change nothing else. Commit only those files by explicit path (`docs(work): ki.prj.ways-of-working polish work state machine`); pull ff-only, else `git merge origin/main` (never rebase, stash, reset or force); push ff-only. Be quick.
