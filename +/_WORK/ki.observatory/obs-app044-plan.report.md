# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-app044-plan

**🤖 → 👤 Handoff to supervisor · Run report at 00:35 BST · last mark 22:50 BST**

---

## Done

- [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) planned and promoted to `now`, still `draft`: Current state, Steps, Files touched and Dependencies confirmed against the code, the release of KI-OBSERVA-VIS-032, VIS-034, VIS-045 and VIS-038's consolidation named, and the open decisions set out under Discussion, Planning. Nothing implemented.
- Holds of [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) and [KI-OBSERVA-VIS-029](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-029-sessions-from-every-host.md) reworded to "Host network's tailnet service-name decision lands", in frontmatter, Shaping and Discussion, with a ROADMAP-CENSUS-2 note.
- One commit, 063b585, local and unpushed; repository audit FAIL=0, its six warnings all existing ones on other records; Markdown lint clean.

## In Progress

- Nothing. KI-OBSERVA-APP-044 cannot go Ready until RESTRUCTURE is answered, and its first step still waits for step 3: KI-OBSERVA-VIS-030 is in progress, KI-OBSERVA-BRG-005 is a draft and KI-OBSERVA-VIS-044 awaits review.

## Queries

### RESTRUCTURE

**Context** The code check found that an unknown `?view=` address falls back to the Beacon today. The server page, the shell and `--view` each read the view, so a redirect table belongs in `resolveInstrument`. Council is a pure rename, but Waiting for you takes Work's "with you" view, so it waits on where Work goes (DESIGN-WORK). The Council rename and the Waiting for you rename each still need your own go.

**Query** How should KI-OBSERVA-APP-044 decide the restructure?

**Options**

a) (recommended, confidence medium - it follows DESIGN-RESTRUCTURE a) and keeps every tab reachable) Converge one consolidation at a time, with the ten instruments as a direction rather than a commitment. Keep the optional job lens until three consolidations have landed. Order: Council, Waiting for you, Streams, Library, Workers, Machine, Extensions. Fold Work into Streams and send its "with you" view to Waiting for you (low confidence on this part). Use one redirect table read by `resolveInstrument` (high confidence). The record then goes Ready with its first step gated on step 3.

b) As a), but keep the order Shaping proposes, with Waiting for you first, and keep Work as its own Observe tab, renaming only the Review queue.

c) Adopt the ten instruments as the target now, with a job switch replacing the lens as part of this decision.

d) Do not converge: keep today's tabs and the lens, and stop at the Council and Waiting for you renames.
