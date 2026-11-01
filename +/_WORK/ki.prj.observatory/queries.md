# ki.prj.observatory queries

## Open

Consolidated on 1 November under STOCKTAKE; every draft below passed one blind review, which agreed with each recommendation. Order is the proposed priority.

### PUBLICATION-ONE - Decide the published report history once, with Ways of working

**Context:** Two Observatory reports from the 29 October away run name Humans Not Robots jobs and work. They are in the Capital's public Git history, and one is still in the current files after the 1 November move into `reports/`. The Observatory holds three open questions on this (PUBLIC-AUDIENCE, PUBLIC-EXPOSURE, ACCESS-DISPOSITION, the last proposing to make `knowledgeislands/ki-principal` private) and the PROTECTED-PUBLICATION hold, which ordinary syncing has since overtaken. Ways of working holds a parallel question on the same history (PUBLIC-REPORT-AUDIENCE), with the independent review Kris asked for on 30 October already done. Making the repository private would not remove copies already taken.

**Query:** May the Observatory's three publication questions and the hold move to Ways of working's question, to be decided once there?

**Options:**

a) (recommended, confidence high - reviewed: one history needs one decision, and Ways of working already holds the parallel question and its review) Send one line asking Ways of working to take the whole scope, answered as four separate parts: who may see it, what to do about what is already published, future publication controls, and whether to make the repository private, with State of play consulted on that last part. Keep the three questions here as pointers until it acknowledges; meanwhile preserve all evidence and change no history or visibility, and record the hold as overtaken.

b) Move both works' questions to KI State of play (ki.sop.main), since making the repository private affects every work in the Capital.

c) Keep the three questions here and answer them separately now.

### ACQUIRE-VIEW - Start the Acquire intake area as the top feature

**Context:** On 31 October and 1 November Kris asked, as a high priority, for an Acquire area: a read-only view over the local acquire checkout showing the knowledge graph (25 cards, stepping from one to its neighbours), its linkage checks (one checker today), the captures and their review backlog, the territory context, and the roadmap and work package, working the same on terra or sol. The checkout is on this Mac and the Observatory listens only locally, so Personal content stays on the machine. Its place in the five-area layout touches RESTRUCTURE but need not wait for it.

**Query:** Should the Observatory take up the Acquire area now as its top feature?

**Options:**

a) (recommended, confidence high - Kris named it high priority, it only reads a local checkout, and the plan comes back before most of it is built) Write a short plan with slices in Kris's order (graph viewer, linkage findings, captures and backlog, context, roadmap), bring it to Kris, then build the graph viewer first.

b) Skip the plan and build the graph viewer straight away, planning the rest afterwards.

c) Wait until the restructure question settles where it belongs.

### STATUS-FIRST - Bring the work-status repair forward

**Context:** An independent review on 29 October showed the Work, Waiting and Review views can give wrong answers: excluded work coming back, ambiguous short names and missing package homes, because fast views skip the CLI's own reading. The CLI side it needs has since landed ([KI-TOOL-KI-CLI-173](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-173-regular-coordination-readers.md) and the naming change). Reading status across every repository takes over a minute. Replaces STATUS-REPAIR.

**Query:** Should the status repair go forward to adoption and a plan now?

**Options:**

a) (recommended, confidence high - independent test cases show real wrong answers and the prerequisites are in place) Adopt one repair taking status and package home from the CLI across Work, Waiting and Review, keeping the current views; settle the one-minute wait and the CLI boundary in the plan before building.

b) Keep the faults visible and wait for evidence from the running service before adopting.

c) Tie it to the restructure decision instead.

### NEXT-TOOL - Diagram notes before the opener button

**Context:** Two small tools are asked for. Diagram notes (29 October): pin comments on a design diagram and have them reach the worker as feedback; the Observatory already sends feedback into a work's `messages.md`, though comments today attach to text, not diagram points, and design diagrams live outside the folders it lists. The opener button (21 October): serve a work's opening line by state with a copyable launch command; `ki agent prompts` already prints openers, and the request's send and resume lines no longer exist in the method. Both come after the Acquire area.

**Query:** Which should follow the Acquire area?

**Options:**

a) (recommended, confidence high - reviewed: diagram notes fill a gap Kris has no other way round, while openers are already available from the CLI) Diagram notes first, as a small slice on one kind of design diagram through the existing feedback route; the opener button later, built on the CLI's current openers.

b) The opener button first, as the smaller job; diagram notes after.

c) Plan both together as one slice.

### HOST-VIEW - One plan for what the Host area watches

**Context:** Several asks land on the Host area: Rig state (the Bridge leaves it unavailable, though Automation already reads Rig's JSON; replaces BRIDGE-STALE), each Mac's expected sync (Kris, 31 October: every 15 minutes, sol leading Knowledge Islands, Personal and Legal; the Observatory watches, it does not sync), scheduled runs that found problems, and later live agent state from hooks and Claude account scores (whose log does not exist yet). The seats map alone does not say which Mac syncs what or when, so the sync owner must name that source.

**Query:** Should one bounded plan for the Host area be prepared now?

**Options:**

a) (recommended, confidence high - reviewed: one plan with separate slices, scheduled-run problems first, and nothing built without approval) Prepare one plan with separate slices: scheduled-run problems first, then Rig state in the Bridge, then expected host sync from a source the sync owner names, showing missing or stale evidence plainly; agent hooks and account scores later. The Observatory gains no syncing role and nothing waits on the Machine idea.

b) Wait until host sync has run supervised for a week, then plan.

c) Plan only the scheduled-run problems now.

### SCHEDULED-FINDINGS - Failed scheduled runs report themselves truthfully

**Context:** HNR email routing asked on 28 October whether the Observatory should read the Failures section of each Route Triage summary, or the job wrapper should report the outcome (a chezmoi change through ki.prj.chezmoi). Some runs record success while their summary lists failures. The Observatory already accepts a `findings` result and ranks it above success, and by design never reads a run's free text, which here holds mail details. Changing the wrapper does not correct old records.

**Query:** Which answer should go back to hnr.reg.email-routing?

**Options:**

a) (recommended, confidence high - reviewed: the producer knows whether its work succeeded and the Observatory's contract already carries the result) The wrapper reports a truthful outcome: failed when required work failed, findings for partial or non-fatal problems, success only when it can show success; the Observatory just shows it. Old misleading records are a separate later choice.

b) The Observatory reads the Failures section itself, with tests over the terra specimens read in place.

### SYNC-CLOSE - Close the sync-direction question as answered

**Context:** SYNC-DIRECTION asked who should run the regular cross-Mac Git sync. On 31 October, in Ways of working, Kris said "the observatory is watching, it's not doing the syncing", with ad hoc sync through it a later idea; the 15-minute plan went to the sol and terra Rig threads. Queue lines MGIT-SYNC-JOB and OBSERVATORY-SYNC asked the same.

**Query:** Should SYNC-DIRECTION close as answered by Kris's 31 October words, with the two lines removed?

**Options:**

a) (recommended, confidence high - Kris's own words answer it and the plan is with the Rig threads) Close it with that answer, keep ad hoc sync from the Observatory as an idea, and remove the two lines.

b) Keep it open until host sync has run for a while.

### DESIGN-PASS - One design pass over the delivered layout

**Context:** Open design items: RESTRUCTURE (prepare the remaining convergence choices within the five areas), TEN-COMMITS (the Git list overlaps newer lists but holds history they lack), MERMAID-HANDLER (a hardening follow-up with no shown bypass), the Known Lands chart's look reserved for Kris, and how island maturity (declared intent) and health (audit evidence) should show. Nothing changed since 29 October and nothing waits on them. Kris's standing words: lose nothing until he approves a consolidation; converge step by step with his go.

**Query:** Should these be prepared as one design pass with Kris, after the Acquire area and the status repair?

**Options:**

a) (recommended, confidence high - reviewed: one prepared comparison saves Kris repeated context, with each choice still answered on its own) One pass: a comparison of present and proposed places with a lose-nothing check for each change; the commit list kept until Kris approves a shown replacement; Known Lands look and condition as separate choices, maturity and health never merged into one score; the Mermaid follow-up parked until an unsafe label or bypass is reproduced.

b) Leave all of them parked until the design thread asks.

### TIDY-RUN - One local housekeeping run alongside

**Context:** Small items have piled up: the coordinator's method reading is behind; 42 reports await pruning and several queue lines run over 60 words; package links point at `/Users/krisbrown/workspaces/...`, gone on this Mac; the product's AGENTS.md still says to restart the service after each delivery though it now reloads itself; ki-design still has `docs/spec/` rather than `docs/specs/` (ROUTE-1); the ideas list still calls Focus the front page; this Mac's registry has no Capital checkout. The ki-design GitHub settings (GH-LIVE) need a GitHub call and the rename to `apps-local.observatory` (NAMING-TO-KI) touches every Mac, so both are left out.

**Query:** Should one local run do the housekeeping, leaving GitHub settings and the rename for later?

**Options:**

a) (recommended, confidence high - local, reversible, and it clears noise from every later report) One run: refresh the method reading, prune homed reports, shorten long queue lines, repoint links to `/Users/krisbrown/kis/`, change the AGENTS.md finish line to "confirm the service answers", rename ki-design's `docs/spec/`, fix the ideas wording, and send the registry gap to ki.prj.tools-burndown.

b) Do only the work-package tidy now.

### ESTATE-ROUTE - Ask 5G Emerge to check its checkout identities

**Context:** On 27 October strict estate reads failed on four 5G Emerge checkouts declaring other identities. The Observatory now reads around them and names them, so its part is done; whether the identities are wrong or intended is unverified, and checkouts are not Observatory work.

**Query:** May this go as one line to the 5G Emerge State of play, hnr.sop.5ge?

**Options:**

a) (recommended, confidence high - reviewed: the checkouts are 5G Emerge's, and the line asks them to verify rather than declaring a fault) Send one line to hnr.sop.5ge giving the four expected and declared identities and asking whether they are intended; remove ESTATE-IDENTITY here once it acknowledges, keeping the Observatory's read warning until the source changes.

b) Send it to hnr.sop.main instead.

c) Keep it here until someone checks the identities.

## Folded

These remain open only as part of the consolidated queries above, which carry their content; their full text is in Git at the commit before this one.

- PUBLIC-AUDIENCE, PUBLIC-EXPOSURE, ACCESS-DISPOSITION - in PUBLICATION-ONE.
- STATUS-REPAIR - in STATUS-FIRST.
- BRIDGE-STALE - in HOST-VIEW.
- SYNC-DIRECTION - in SYNC-CLOSE.
- RESTRUCTURE, TEN-COMMITS, MERMAID-HANDLER - in DESIGN-PASS.
- QUEUE - answered by STOCKTAKE, 1 November.

## Parked

No unanswered choice has been selected. Council/consolidation order, Waiting/Review, Work's destination and Rig declaration versus observed-health scope are separate downstream design questions, gated by their preparation decisions above. HOST-MEANING is receiver-owned at Ways of working, not an additional decision requested here. ACCEPT remains closed in the [sourced receipt](decisions.md#2026-10-29---accept-closed).
