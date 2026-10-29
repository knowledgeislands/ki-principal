# wow-sm-refine - three quick refinements to the work state machine

Edit `+/_WORK/ki.prj.ways-of-working/design/work-state-machine.md`, `.html`, `.svg` (and its architecture JSON if any), using the `archify` skill, per STATE-MACHINE-REFINE in the package's `decisions.md`:

1. `hold` arcs from With worker, With supervisor and Handoff to supervisor into On hold (drain stops runs on the way); drop "said while work runs, the word is first a receive".
2. Replace `release` (On hold → Handoff to worker) with `resume` On hold → Bootstrap; release condition is its precondition; update the host-move paths to hold → On hold → resume on the new host → Bootstrap → pick up; drop "not from On hold" from re-bootstrap. Adjust HOST-MOVE-PATH context if needed.
3. Remove the `drain blocked` arc: a hold that cannot meet its postconditions does not complete; the work stays in its source state, marked blocked, and the report says what blocks (`NOT DRAINED`). Say this in the hold row and the portability checks.
4. Diagram: each arc's preconditions and postconditions appear on click or hover in the HTML; the SVG stays a clean overview with short guard labels where they matter (e.g. `portable` on hold).

Be quick: change only what these need. Commit only those files by explicit path (`docs(work): ki.prj.ways-of-working refine work state machine`), pull ff-only, push ff-only; stop on divergence. British English, ASCII hyphens only.
