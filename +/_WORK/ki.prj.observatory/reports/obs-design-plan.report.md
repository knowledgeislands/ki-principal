# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-design-plan

**🤖 → 👤 Handoff to supervisor · Run report at 21:10 BST · last mark 20:20 BST**

---

## Done

The ki-design handoff is now planned in the Observatory roadmap as 18 records, and nothing is built. Every record's acceptance keeps all fifteen tabs, every route, every `?view=` address and every capability working. It also keeps the contrast, density (12 Beacon rows at 800 px) and width (720 px) tests passing unchanged.

Step 1, tokens and glyphs:

1. [KI-OBSERVA-APP-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) Design tokens and glyphs. Next, draft, fully shaped. It takes the colours and type from ki-design instead of ki-website, adds 14 px glyphs to the tabs and Beacon subjects, and updates the tab-width model in the same change. It waits for your Ready decision.

Step 2, shell polish:

2. [KI-OBSERVA-APP-043](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-043-shell-polish-without-regrouping.md) Shell polish without regrouping. Soon. Adds the Observatory mark, the way in on the status line, the five pane states, the filter-not-scope chip, and the four jobs as an optional lens over the tabs. Blocked by step 1.

Step 3, per-tab upgrades, each independent:

3. [KI-OBSERVA-BCN-008](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md) Beacon signal anatomy. Soon. Adds reef and lantern glyphs, kind, condition, freshness and "new", and filters on them, at no cost in rows. Blocked by step 1.
4. [KI-OBSERVA-VIS-030](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) Known Lands chart. Soon. A new sixteenth tab beside the existing ones; read-only flat hex chart. Blocked by step 1.
5. [KI-OBSERVA-BRG-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-003-governed-act-presentation.md) Governed Act presentation. Soon. Redraws the existing Repositories and Rig plan, confirm and receipt steps as declare, confirm, receipt, with the boundary edge and the word "governed". What each operation does stays the same.
6. [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md) Who is working. Soon. Agent runs and commit authors appear in a column in the existing tables.
7. [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md) Tailnet read-only appearance. Triage. Covers only the app's side; it waits for unit 4 and Host network.
8. [KI-OBSERVA-INT-003](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-INT-003-extensions-switchboard.md) Extensions switchboard. Triage. Kept side by side with the live-artifact extension model, and follows EXT-MODEL.

Step 4, converge. All are triage, and each says you approve that one consolidation before it starts:

9. [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) Instrument restructure decision. Whether to converge at all, the job switch, the redirect table and the order.
10. [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md) Library: Knowledge Bases and Documents.
11. [KI-OBSERVA-VIS-033](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-033-waiting-for-you.md) Waiting for you: the review queue and Work's "with you" view.
12. [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md) Streams: Roadmap and Work.
13. [KI-OBSERVA-VIS-035](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-035-trade-routes-as-layer.md) Trade routes as a layer on Known Lands.
14. [KI-OBSERVA-VIS-036](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-036-activity-split.md) Activity split: "what changed" to the Beacon, and its time window to Known Lands.
15. [KI-OBSERVA-VIS-037](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-037-workers-instrument.md) Workers: Sessions and Automation runs.
16. [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md) Machine: Rig, MCP and Automation schedules.
17. [KI-OBSERVA-VIS-039](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-039-decisions-as-council.md) Decisions renamed Council.
18. [KI-OBSERVA-VIS-040](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-040-extensions-instrument.md) Artifacts renamed Extensions.

Two notes on the shape:

- I adopted the step 2 and step 3 drafts at Soon rather than Next. A Next record must carry a full delivery plan, and these still have open design questions.
- I did not plan the handoff's draft 2, Git tracker parity. Your ARTIFACTS-EXTEND decision already keeps Kit Git Repo Audit as the richer extension, with Repositories as the basic built-in view.

Commits and checks:

- Commits `fbd1fbf` (reserves the identifiers) and `87fab2c` (the records) are pushed fast-forward to origin; only my commits were on top.
- Roadmap audit: no new findings. One failure was already there before this run (see Queries).
- Markdown check: clean.
- Full repository audit: no new findings. Three warnings and one failure were already there.
- App test gate: not run, because no code changed.
- No service restart, as briefed.

### Where the board conflicts with what the app already does (the app wins), for the design thread

1. Row and type scale. The boards use 31 px rows of 14/20 text, 20/26 titles and 44/38/38/26 px bands. The app uses 25 px rows of 13/16 text and 19/24 titles. The app's scale stands, and the density test decides.
2. Frame gutter. The boards use 16 px wide and 8 px narrow; the app uses 24 px and 12 px. The app's values stand.
3. Tab glyph size. The instruction says 14 px and the spec's §2 says 16 px. The plan uses 14 px, so the design should settle on one.
4. Tab glyphs are named for the ten future instruments, not today's fifteen tabs. [KI-OBSERVA-APP-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) proposes one glyph for each existing tab.
5. Subject glyphs by name prefix (`tools-*`, `mcp-*`, `apps-*`). The app reads `ki` data rather than guessing a repository's kind from its name, and no `ki` data states the kind. So it draws the generic `island` glyph until a contract says the kind; that gap is for `ki` to close.
6. "No emoji". The Work tab prints the ki-pmo banner glyphs (🤖 🧑 👤 ⏸️ 🏁) exactly as the standard writes them. Carried as a query.
7. The handoff names PDR-KI-OBSERVA-007 for the visual changes, but 007 is already taken (feedback). The next free number is 008.
8. The ki-design role colours and washes are the values this app derived and holds by test, hex for hex. Re-vendoring changes where the values come from, not what the screen shows, and the app's contrast record remains the evidence.
9. Draft 2 (Git tracker parity) is overtaken by ARTIFACTS-EXTEND. Kit Git Repo Audit stays the richer extension, and Repositories links to it rather than replacing it.
10. Draft 1's tailnet listener, `tailscale serve` and ACL belong to unit 4 and the Host network Project, and they are connection-critical. The Observatory plans only the app's read-only side.
11. Draft 5's switchboard overlaps the live-artifact extension model: manifest keys, "Extended by", the directory, and tokens passed to the frame. Both are kept side by side under PUSH-ALL.
12. Act. The board's declare, confirm, receipt already matches what the app enforces. Where they differ, the app's authority specification wins.
13. Draft 7 and the handoff README still say fourteen tabs. There are fifteen, and Known Lands makes sixteen before any consolidation.
14. "Agents are never a dashboard of their own". The Sessions tab is a runs view today, and it stays until the Workers consolidation is approved.

## In Progress

Nothing is running. Step 1 is ready to build once you approve it.

## Queries

**DESIGN-READY**

**Context:** [KI-OBSERVA-APP-042](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-042-design-tokens-and-glyphs.md) is fully shaped. The roadmap rules need your explicit approval before a record becomes Ready, and DESIGN-APPLY said you see the plan before any build.

**Query:** Approve step 1 to Ready as shaped?

**Options:** a) (recommended, confidence high - the re-vendoring changes no colour on screen, and its risks are already stops in the plan) Approve: mark it Ready and deliver it next. b) Change the tab glyph mapping or the scope first. c) Keep it in draft until the §11 questions are answered.

**DESIGN-WORK-GLYPHS**

**Context:** The Work tab prints the ki-pmo banner glyphs (🤖 🧑 👤 ⏸️ 🏁), the same notation used in every report. The design says no emoji.

**Query:** Keep the standard's banner glyphs in the Work tab, or draw them as line glyphs?

**Options:** a) (recommended, confidence medium - one notation everywhere the owner reads it) Keep them, and ask the design thread whether to change the ki-pmo notation itself. b) Draw line glyphs with the words beside them in the app only. c) Drop the glyphs and show only the words.

**DESIGN-RELAY**

**Context:** The handoff asks the Observatory to record "the app wins" differences in ki-design, by an issue or a note in the hand-off README. This run was told not to open issues there.

**Query:** How should the list above reach the design thread?

**Options:** a) (recommended, confidence high - no write to another repository without its owner) The coordinator passes it to the design thread through Messages, and that thread writes its own README note. b) This thread opens a ki-design issue, which needs separate authority for a GitHub call. c) This thread writes the note in the ki-design hand-off README.

**ROADMAP-VIS-022**

**Context:** The roadmap audit now fails on [KI-OBSERVA-VIS-022](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-022-judge-overdue-against-each-job-schedule.md), whose title is longer than four words. It is a triage record from 17 October, not part of this run, so I left it alone.

**Query:** Shorten its title?

**Options:** a) (recommended, confidence high - clears the only roadmap failure) Retitle it "Overdue against job schedules". b) Leave it for its own thread.

**DESIGN-RESTRUCTURE (spec §11)**

**Context:** The design marks the ten instruments under four jobs as Open. [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) holds the decision.

**Query:** Converge on the ten instruments at all?

**Options:** a) (recommended, confidence medium - the reskinned app will show which groupings help) Decide after steps 1 to 3, one consolidation at a time. b) Adopt the target now and order the consolidations. c) Keep the fifteen tabs and use the job lens only.

**DESIGN-WORK (spec §11)**

**Context:** Work landed after the design brief. The design folds it into Streams and sends its "with you" view to Waiting for you.

**Query:** Where should Work go?

**Options:** a) (recommended, confidence low - Work is new and its use is still settling) Keep its own tab until the Streams consolidation is reviewed. b) Fold it into Streams as the design proposes. c) Give it its own instrument for good.

**DESIGN-AUTOMATION (spec §11)**

**Context:** Automation splits between Workers (runs) and Machine (schedules).

**Query:** Which one should `?view=automation` open?

**Options:** a) (recommended, confidence medium - a job is defined by its schedule) Machine, as the spec proposes. b) Workers.

**DESIGN-ACT-NAME (spec §11)**

**Context:** The job's name, Bridge or Causeway, is not settled.

**Query:** Keep "Act" on screen until it is?

**Options:** a) (recommended, confidence high - a plain verb, and no change needed later) Yes, "Act". b) Bridge, matching the app's `bridge` component and its decision record. c) Causeway.

**DESIGN-ACT-MARK (spec §11)**

**Context:** The boards mark Act with a boundary-colour edge and the word "governed"; boards 4 and 5 also add a top rule.

**Query:** Are the edge and the word enough?

**Options:** a) (recommended, confidence medium - the app already uses the boundary colour for every control edge, so a top rule makes the difference clear) Edge, word and a top rule in the boundary colour. b) Edge and word only.

**DESIGN-STALE (spec §11)**

**Context:** The pane needs a stale state.

**Query:** When does an observation become stale?

**Options:** a) (recommended, confidence low - instruments refresh at very different rates) A threshold per instrument, with one default. b) One fixed age for all.

**DESIGN-SWITCH (spec §11)**

**Context:** Switching an extension off can hide something that contributes to the Beacon.

**Query:** Is a switch a preference or an Act operation with a receipt?

**Options:** a) (recommended, confidence medium - it changes only what is shown) A host preference, with the Beacon naming any contributors switched off. b) An Act operation with a receipt.

**DESIGN-CAPITAL (spec §11)**

**Context:** The Capital has no glyph. The chart draws it as Library plus Council Hall, and the Beacon uses the Council Hall.

**Query:** Ask ki-design for a Capital glyph?

**Options:** a) (recommended, confidence medium - one civic mark that reads at 14 px) Yes, and use Library plus Council Hall until it exists. b) Keep the two-glyph drawing for good.

**DESIGN-POSITIONS (spec §11)**

**Context:** Known Lands needs island positions to stay where you learnt them, and nothing stores them today.

**Query:** Where should positions live?

**Options:** a) (recommended, confidence medium - it keeps the browser away from the filesystem) A host preference in XDG state, behind the backend. b) A tracked file in each territory's principal repository.

**DESIGN-WORKERS-CHIP (spec §11)**

**Query:** Should the workers chip count only agent runs at work, or people with commits today as well?

**Options:** a) (recommended, confidence low - runs are the evidence that is live) Agent runs only. b) Runs and today's commit authors.

**DESIGN-LIBRARY-SEARCH (spec §11)**

**Query:** Should the merged Library search documents as well as notes?

**Options:** a) (recommended, confidence medium - one reader should have one search) Yes, when the Library consolidation is approved. b) Notes only.

**DESIGN-NARROW (spec §11)**

**Context:** PDR-KI-OBSERVA-002 already requires every table to declare which columns survive and which drop at 760 px, and a test enforces it.

**Query:** Who declares the columns for the new tables?

**Options:** a) (recommended, confidence high - this is already how the app works) Each record declares its own tables at delivery, and the design thread follows. b) The design thread declares them first.

**DESIGN-TAILNET-BRIDGE (spec §11)**

**Query:** Acting over the tailnet: plan it now, or later in a separate decision record?

**Options:** a) (recommended, confidence high - acting from another machine needs the least-privilege design first) A later, separate decision record, after the read-only listener. b) Plan it now with [KI-OBSERVA-OPS-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-OPS-004-tailnet-read-only-appearance.md).
