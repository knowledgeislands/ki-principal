# wow-state-machine - the work state machine, drawn and defined (ki-work-design)

You work for ki.prj.ways-of-working. Kris decided WORK-STATE-MACHINE and WORK-FOLDER-PURPOSE on 2026-10-29; read both, and DRAIN-MEANS, in the package's `decisions.md` - they are your requirements, in Kris's words.

Read: `Pillars/Philosophy/Model/Processes/Work Process/Work Process.md` (states, moves, banner); in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, the `ki-coordination` standard (`skills/change-management/ki-coordination/references/standards-coordination.md`: receive words, hold, drain, Finished, re-anchoring) and `ki-work-package` (entry points, tidy, close-out); the package's existing `design/work-model.architecture.json` and `design/work-model.svg`.

Produce, with the `archify` skill (lifecycle/state diagram):

1. `+/_WORK/ki.prj.ways-of-working/design/work-state-machine.html` and a static `design/work-state-machine.svg` on disk. States: Bootstrap (new; entered at bootstrap and re-bootstrap, exits to With worker or With supervisor), With worker, With supervisor, Handoff to supervisor, Handoff to worker, Handoff to target, On hold, Finished. Arcs labelled with their transition names (send, receive, hold, release, finish, ...; name each one, reusing words the standard already uses).
2. `design/work-state-machine.md`, embedding the SVG at the top, then: a table of states (meaning, who holds the move, banner glyph, what must be true while in it); a table of transitions (name, from, to, trigger/owner words, entry conditions, procedure run on the way - e.g. drain and the DRAIN-MEANS portability checks before On hold - and what is committed); where Handoff to target goes (target replies, target takes ownership, target refuses); how a host move maps onto the machine; and the WORK-FOLDER-PURPOSE folder layout (five root files; named purpose folders such as reports/, briefs/, design/, findings/).
3. A short `## Decisions for Kris` section: each genuine open choice as a tagged decision (stable mnemonic tag) with **Context:**, **Query:**, **Options:**, `a) (recommended, confidence <level> - <reason>)` first. Keep it to what the evidence leaves open.

Design only: change no standard, skill, other package file or repository. Commit only those three files by explicit path (`docs(work): ki.prj.ways-of-working work state machine design`), pull ff-only, push ff-only; another run (wow-drain-tidy) is tidying the same folder, so on a non-fast-forward pull, fetch and retry once, then stop. British English, ASCII hyphens only.
