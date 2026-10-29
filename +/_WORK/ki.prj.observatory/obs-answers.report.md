# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-answers

**🤖 → 👤 Handoff to supervisor · Run report at 08:07 BST · last mark 20:20 BST**

---

## Done

The Observatory roadmap now has the two-way bridge and the Git view. Three records cover it, and each waits on [KI-OBSERVA-APP-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md):

- [KI-OBSERVA-VIS-041](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-041-git-view-replaces-repositories.md) "Git view replaces Repositories" is new, in triage. Every Repositories capability, governed operation and `?view=repositories` address is listed and carries over. Some things stay out until they are decided separately: commit and bulk writes, the `askClaude` commit suggestion, and opening the repository in VS Code or GitHub Desktop.
- [KI-OBSERVA-INT-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-004-outbound-live-artifact-adapter.md) "Outbound live-artifact adapter" is new, in triage. It takes Observatory views out to Claude Desktop, read-only. The Git view is the first view it carries.
- [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md) is revised and retitled "Inbound live-artifact adapter". The switchboard stays inside it, side by side, and keeps its file name.

Each medium-and-up answer is written into the record that owns it:

- [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md): DESIGN-RESTRUCTURE, DESIGN-AUTOMATION, DESIGN-ACT-NAME and DESIGN-NARROW, plus a note that the Git view replaces Repositories.
- [KI-OBSERVA-BRG-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-003-governed-act-presentation.md): DESIGN-ACT-MARK and DESIGN-ACT-NAME.
- KI-OBSERVA-INT-003: DESIGN-SWITCH.
- [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md): DESIGN-POSITIONS and DESIGN-CAPITAL.
- [KI-OBSERVA-VIS-039](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-039-decisions-as-council.md): DESIGN-CAPITAL.
- [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md): DESIGN-LIBRARY-SEARCH.
- [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md): DESIGN-TAILNET-BRIDGE.
- [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md): where `?view=automation` lands.

DESIGN-WORK-GLYPHS was already recorded in KI-OBSERVA-APP-042. [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md) is retitled "Overdue against job schedules". Nothing was adopted, and no record changed state.

The [design note](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/live-artifacts.md) is reworked around the two-way bridge. Its worked case now has Kit Git Repo Audit becoming the Git view, with the full carry-over listed and the 18 October reading kept for the record. The Mermaid block is untouched. Under it I added the pending line: the diagram predates EXT-MODEL and the bridge is not drawn until DIAGRAM-STANDARD is settled. There was no pending line before, so I read "with its pending line" as an instruction to add one.

Commits and checks:

- apps-observatory.local: `40c47a2` (reserves the identifiers), `c188f9a` (the records) and `e48645e` (the answers). All three are pushed fast-forward to origin; only my commits were on top.
- ki-principal: `973807d` (the design note) is committed but not pushed. Three commits from other sessions sit under it (`7aa0739`, `e7e30c0` and `ff513b9`, from ki.ways-of-working and the aesthetics lore sheet), so a push would carry them too.
- Roadmap audit: passes, so the KI-OBSERVA-VIS-022 failure is cleared.
- Full repository audit: no failures. The three warnings were already there.
- Markdown check: clean in both repositories.
- App test gate: not run, because no code changed.
- No service restart.

## In Progress

Nothing is running. Two relay lines are not sent, both stopped as the brief says (see Queries).

## Queries

**DESIGN-THREAD-HOME**

**Context:** I looked for the design thread's work file. Neither `ki-principal/+/_WORK/` nor `ki-design/+/_WORK/` has one: no work file names ki-design, and ki-design's `+/` holds only `README.md`, `_TRADES` and `art`. So I sent nothing. Three things wait to go to the design thread: the "app wins" list, the ask to reconsider the banner notation (DESIGN-WORK-GLYPHS), and the ask for a Capital glyph (DESIGN-CAPITAL).

**Query:** Where should the relay to the design thread go?

**Options:** a) (recommended, confidence medium - ki-design's `+/_TRADES` is that repository's own inbound route, so it needs no other repository's work file) Send it as a trade into ki-design through `ki-trade`. b) Open a `ki.design` work file in ki-principal and put the Messages line there. c) You pass it to the design thread in person.

**OVERDUE-TITLE-HOME**

**Context:** OVERDUE-TITLE is not in the ki.ways-of-working work file. It sits in the territory work file, [ki/work.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/work.md), line 46. The brief made the line depend on the ways-of-working file holding it, so I wrote nothing.

**Query:** Should the "resolved by the KI-OBSERVA-VIS-022 retitle" line go to the territory work file instead?

**Options:** a) (recommended, confidence high - that is where the message was raised) Yes, the coordinator appends it to `ki/work.md` Messages. b) Leave it until that work file is next tidied.

**PUSH-PRINCIPAL**

**Context:** My `973807d` in ki-principal sits on three unpushed commits from other sessions.

**Query:** Push ki-principal with all four commits?

**Options:** a) (recommended, confidence medium - all four are local documentation commits on main, and nothing is lost) Push once their sessions or you agree. b) Leave it for the next interactive session to settle.
