# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › stocktake

**🤖 → 👤 Handoff to supervisor · Run report at 00:46 GMT · last mark 15:47 GMT (29 October)**

---

## Done

- Took stock, read-only, of all 39 lines in [messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/messages.md) (9 marked important, one of them, REFRESH, mid-line; the brief's 37 and 7 predate the last two arrivals) and all 10 open [queries](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/queries.md), checked against apps-observatory.local, ki-design, tools-ki, acquire, the Rig launch job and the Ways of working package.
- In short: 19 lines are settled or overtaken and can go; the other 20 and nine live queries fall into seven groups. Three facts have moved since 29 October. The publication hold no longer holds anything back: everything it guarded, both protected report versions included, is already on the remote. Kris answered the sync direction on 31 October in Ways of working: the Observatory watches and does not sync. And the work-status producer's prerequisites (regular readers, naming) have landed.
- Proposed order: publication first, the Acquire intake view second, status correctness third, then diagram feedback and the opener button, then Host observation, with design convergence last and a housekeeping run alongside.
- Roadmap audit rerun in apps-observatory.local (`ki repo audit --skill ki-work-roadmap`): FAIL 0, WARN 1, the warning being that this machine's registry has no local checkout for the Capital.
- Nothing edited, adopted, removed, sent or pushed; no commits.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Package links still point at `/Users/krisbrown/workspaces/...`, which no longer exists on this machine; checkouts are under `/Users/krisbrown/kis/`. Folded into the housekeeping query.
- The coordinator's `method_read` (`df3f5503`) is four harness commits behind; the REFRESH line (`fb19794d`) is among them.

## Findings

### SETTLED - Lines settled, overtaken or belonging elsewhere

**Goal:** Say for every message line whether it is settled, live or another work's, with evidence (STOCKTAKE, 1 November 2026).

**Scope:** All 39 lines of messages.md, numbered by file line; checked against local Git and files only, no fetch.

**As of:** 1 November 2026, 00:44 GMT; remote facts are as of the local `origin/main` refs, not a fresh fetch.

| Line | Tag | Verdict | Evidence |
| --- | --- | --- | --- |
| L4 | SERVE-STALE-BINARY | Settled | Corrected by L5; the launch job `uk.me.kris.rig.observatory` runs `bun --watch run src/main.ts --no-open` (its plist arguments) |
| L5 | SERVE-STALE-BINARY-CORRECTION | Settled | Same plist; serving from source with watch is live |
| L7 | LOCAL-SYMLINKS · DELIVERY-COORDINATION | Settled notice | Redesign ownership exercised: [PDR-KI-OBSERVA-010](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/decisions/PDR-KI-OBSERVA-010-four-areas-replace-the-tab-bar-and-the-observatory-opens-on-what-waits-for-its-owner.md) on main; the items it names stay with Ways of working |
| L8 | NAMING-REORIENT | Settled | Package lives at `ki.prj.observatory`; NAMING-DONE (L37) received 29 October |
| L11 | OPS003-DELIVERED | Settled | Record pruned; only the finish-wording residual remains, carried by L6 |
| L12 | OBS-ACCEPT2-FOLLOWUPS | Settled | KI-OBSERVA-OPS-003 and VIS-027 pruned; [KI-OBSERVA-BRG-006 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/2006196/docs/roadmap/KI-OBSERVA-BRG-006-feedback-to-messages-file.md) pruned at `91795c3`; [KI-OBSERVA-BRG-005 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/36abae9a540bf39785d3dd91811fda12ff759ec3/docs/roadmap/KI-OBSERVA-BRG-005-act-board-missing-parts.md) terminal; its Act-plan visual check is overtaken by the five-area redesign (no Act board left in the site source) |
| L13 | ISLAND-CONDITION (20 Oct) | Superseded | By L15, which carries the live part |
| L14 | BRING-UP-LEFTOVER | Overtaken | The bring-up pack no longer exists (old `ki.ways-of-working` folder gone); Beacon has a `stuck` signal (`packages/contracts/src/beacon.ts:127`); [KI-OBSERVA-BCN-008 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/22ea8dc/docs/roadmap/KI-OBSERVA-BCN-008-beacon-signal-anatomy.md) accepted and pruned. A one-line "overtaken" reply to ki.prj.ways-of-working is owed |
| L16 | VIS-SIZES | Settled | [KI-OBSERVA-VIS-028](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/ideas/KI-OBSERVA-VIS-028-retire-sessions-readers.md) is now an idea, not a record; [KI-OBSERVA-VIS-030 (pruned)](https://github.com/knowledgeislands/apps-observatory.local/blob/36abae9/docs/roadmap/KI-OBSERVA-VIS-030-known-lands-chart.md) pruned at `865cc84`; audit rerun shows no size finding |
| L19 | ROADMAP-AUDIT | Settled | Both failing records pruned; rerun today FAIL 0 (the one warning is the registry gap) |
| L20 | TIDY | Duplicate | Same findings as L21; L21 and L41 carry the live tidy |
| L24 | USABILITY-THREAD | Overtaken | Focus deleted by PDR-KI-OBSERVA-010 (L25) |
| L25 | REDESIGN-LANDED | Settled notice | PDR-KI-OBSERVA-010 on main |
| L28 | TYPED-ID-CONSUMER | Assessed | Done by the 29 October consumer assessment ([report](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/reports/away-consumer-gap.report.md)); the repair it found is the STATUS-REPAIR query |
| L30 | COORD-REGULAR-STATUS | Assessed | Same assessment; [KI-TOOL-KI-CLI-173](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-173-regular-coordination-readers.md) is done; carried by STATUS-REPAIR |
| L32 | NAMING-PAUSE | Settled | Released by L37 |
| L33 | MGIT-SYNC-JOB | Overtaken | Kris, 31 October 13:14 GMT, in Ways of working: "the observatory is watching, it's not doing the syncing"; the 15-minute plan went to personal.reg.rig-sol and personal.reg.rig-terra (HOST-SYNC-SEND) |
| L34 | OBSERVATORY-SYNC | Overtaken | Same answer |
| L36 | ACCESS-ADMINS | Not applicable | The Observatory listens on 127.0.0.1 only (`apps/site/src/main.ts:80`); no Access application or `/admin` exists. A one-line reply to ki.sop.main is owed; the tailnet appearance idea would reopen it |
| L37 | NAMING-DONE | Settled | Barrier released 29 October |

Partly another work's: L26 ESTATE-IDENTITY. The Observatory side is done (it reads around and names the checkouts); the retired Notion mirror island is gone (ki-design `6fe3557`); the 5G Emerge checkout identities belong to hnr.sop.5ge; the `ki work status` latency is carried by STATUS-REPAIR.

### LIVE - Live lines by group

**Goal:** Group every live line and query into a few items Kris can decide.

**Scope:** The 20 lines not settled above and the nine live queries.

**As of:** 1 November 2026, 00:44 GMT.

| Group | Lines | Queries |
| --- | --- | --- |
| G1 Publication and protection | L9 PROTECTED-PUBLICATION | PUBLIC-AUDIENCE, PUBLIC-EXPOSURE, ACCESS-DISPOSITION |
| G2 Acquire intake area | L10 ACQUIRE-INTAKE-VIEW | - |
| G3 Status correctness | (L28, L30 carried), L26 latency part | STATUS-REPAIR |
| G4 New tools: diagram notes and the opener | L38 DIAGRAM-FEEDBACK, L17 WORK-OPENER | - |
| G5 Host, sync and automation observation | L29 HOST-RESPONSIBILITY, L31 SCHEDULED-RESULTS, L39 ROUTE-TRIAGE-SPECIMENS, L18 AGENT-HOOKS-OBSERVATORY, L27 CLAUDE-ACCOUNT-SCORES | SYNC-DIRECTION, BRIDGE-STALE |
| G6 Design convergence | L3 OBS-LANDED-VIS030, L15 ISLAND-CONDITION (21 Oct) | RESTRUCTURE, TEN-COMMITS, MERMAID-HANDLER |
| G7 Housekeeping | L6 SERVE-WATCH (finish wording), L21 WOW-TIDY-NIGHT, L22 ROUTE-1, L23 GH-LIVE, L35 NAMING-TO-KI, L40 REFRESH, L41 REPORTS-MOVED | - |

Notes on live lines:

- L10: the acquire checkout exists at `/Users/krisbrown/kis/personal/acquire` (`0b9e3e1`, 1 November) with 25 knowledge cards; `prototype/kig/` holds `term_check.py` but no `concept_check.py`, so the linkage findings slice reads one checker today. Its contents are Personal; the Observatory's 127.0.0.1-only serving keeps them local, and "from either machine" means each Mac's own Observatory over its own checkout.
- L17: there is no `ki work opener`; `ki agent prompts` already prints each thread's opener (tools-ki `src/core/work/prompts.ts`), so the button can render from it.
- L31: commit `90a94a6` specified the existing contract in [automation.md](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/docs/specs/automation.md), which accepts a `findings` status and never reads a run's detail text; the reply hnr.reg.email-routing asked for is still owed.
- L22: ki-design still has `docs/spec/`, not `docs/specs/`. L23 cannot be checked without a GitHub call.
- L6: product [AGENTS.md](/Users/krisbrown/kis/knowledge-islands/apps-observatory.local/AGENTS.md) line 14 still finishes deliveries with `launchctl kickstart`, though the service now watches its source.
- L35: the rule names site repositories by reversed hostname; applied literally it would rename `apps-observatory.local` to `apps-local.observatory`. No deadline.
- L21: the parent is declared (`parent: ki.sop.main`); 42 reports in `reports/` and several queue lines over 60 words (L10, L29, L30, L31, L34) remain.

### CHANGES - What moved for each query since 29 October

**Goal:** Say whether anything since 29 October changed each open query.

**Scope:** The ten open queries; product Git, Principal Git and the Ways of working, Rig and tools-ki packages.

**As of:** 1 November 2026, 00:44 GMT; apps-observatory.local has no commit since 29 October 01:36 UTC.

| Query | Changed? | What changed |
| --- | --- | --- |
| QUEUE | Answered | STOCKTAKE, 1 November; this run |
| RESTRUCTURE | No | No product or design-thread change |
| TEN-COMMITS | No | - |
| MERMAID-HANDLER | No | - |
| BRIDGE-STALE | Context only | The Host area now has a decided thing to watch: per-host sync every 15 minutes, primary map seeded from the seats (Ways of working, 31 October) |
| STATUS-REPAIR | Strengthened | Producer prerequisites landed: KI-TOOL-KI-CLI-173 done and the naming migration received; nothing on the Observatory side |
| SYNC-DIRECTION | Answered elsewhere | Kris, 31 October 13:14 GMT: "the observatory is watching, it's not doing the syncing ... In the future it might be able to ... do the ad hoc sync"; execution went to the Rig host threads |
| PUBLIC-AUDIENCE | Facts moved | Every commit the hold guarded, tip `542dcbc8` included, is now an ancestor of `origin/main` (`37a872d2`, 1 November); both protected report versions are in remote history (`ccbd06dd`, `c5c3d3b3`), and one is current at `reports/away-jobs-evidence.report.md`, re-committed by the 1 November move (`3b09eba9`). Ways of working holds a parallel PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY on the same history; Kris asked on 30 October for an independent review before answering, and that review exists |
| PUBLIC-EXPOSURE | Facts moved | As above |
| ACCESS-DISPOSITION | No | Still proposes making `knowledgeislands/ki-principal` private; its "moderate" confidence is not one of the three allowed levels |

The brief's premise that PROTECTED-PUBLICATION blocks Principal pushes no longer holds in practice: Principal has been pushed since, and nothing it guarded remains unpublished.

### PRIORITY - Groups, decisions and order

**Goal:** Give a priority order across the groups with blockers and dependencies.

**Scope:** The seven groups above.

**As of:** 1 November 2026, 00:44 GMT.

| Order | Group | Decision | Why this place | Depends on | Draft query | Blind review |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | G1 Publication | One decision, one owner, for the published report history | A protected report is current at the public head and is re-committed whenever it moves; deciding costs nothing to build | Ways of working's parallel query; ACCESS-DISPOSITION affects the whole Capital | PUBLICATION-ONE | Yes, medium |
| 2 | G2 Acquire intake | Take it up now, plan first, graph slice first | Kris's explicit high priority; reads one local checkout and is independent of every other group | Placement in the five-area shell touches RESTRUCTURE, but need not wait for it | ACQUIRE-VIEW | No, high |
| 3 | G3 Status correctness | Bring STATUS-REPAIR to adoption and a plan | Demonstrated wrong answers in views Kris uses daily; producer prerequisites have landed | tools-ki producer; latency evidence | STATUS-FIRST | No, high |
| 4 | G4 Diagram notes and opener | Which new tool first | Asked for by Kris; both build on paths that exist (feedback to messages, `ki agent prompts`) | Diagram notes reuse the accepted feedback route | NEXT-TOOL | Yes, medium |
| 5 | G5 Host observation | Close SYNC-DIRECTION; prepare one Host-area observation plan; answer the HNR scheduled-results question | Rig host sync is only starting supervised and the account-score log does not exist yet | Rig host threads; seats map; ki.prj.chezmoi for any wrapper change | SYNC-CLOSE, HOST-VIEW, SCHEDULED-FINDINGS | HOST-VIEW and SCHEDULED-FINDINGS, medium |
| 6 | G6 Design convergence | One design pass with Kris over the delivered design | Parked with the design thread; nothing else waits on it | Kris's design time | DESIGN-PASS | Yes, medium |
| alongside | G7 Housekeeping | One local tidy run | Cheap, local, runs beside anything; clears the queue and stale links | GH-LIVE and the rename need their own go | TIDY-RUN | No, high |

The work transfer ESTATE-ROUTE (L26's checkout part to hnr.sop.5ge) is a separate query, medium, for blind review.

### REMOVALS - Lines proposed for removal

**Goal:** List the lines the coordinator may dispose of as settled.

**Scope:** Lines whose verdict above is settled, overtaken, superseded, duplicate or assessed.

**As of:** 1 November 2026, 00:44 GMT.

| Lines | Precondition |
| --- | --- |
| L4, L5, L7, L8, L11, L12, L13, L16, L19, L20, L24, L25, L32, L37 | None; evidence in SETTLED |
| L28, L30 | None; STATUS-REPAIR carries the outcome |
| L33, L34 | Close SYNC-DIRECTION at the same time (SYNC-CLOSE) |
| L14 | Send the one-line "overtaken" reply to ki.prj.ways-of-working |
| L36 | Send the one-line "not applicable, local only" reply to ki.sop.main |
| L26 | After ESTATE-ROUTE is answered |
| L9 | Only once G1's decision records the owning disposition |

## Queries

### PUBLICATION-ONE - Decide the published report history once, in one place

**Context:** Two Observatory reports from the 29 October away run name Humans Not Robots jobs and work. They are in the Capital's public Git history, and one of them is still in the current files (it was moved into `reports/` on 1 November, which committed it again). The Observatory has three open questions about this (PUBLIC-AUDIENCE, PUBLIC-EXPOSURE, ACCESS-DISPOSITION, the last proposing to make the whole `knowledgeislands/ki-principal` repository private), plus an important message, PROTECTED-PUBLICATION, asking it to decide before any push. That push has since happened through ordinary syncing, so the hold no longer holds anything back. Ways of working holds a parallel question on the same history (PUBLIC-REPORT-AUDIENCE and PUBLIC-REPORT-RECOVERY); on 30 October Kris asked for an independent review before answering it, and that review has been done. Two places deciding one repository's history risk conflicting answers.

**Query:** Should the Observatory's three publication questions and the hold be decided together with Ways of working's parallel question, as one decision?

**Options:**

a) (recommended, confidence medium - one history needs one decision, but the right home is a judgement) Fold them into Ways of working's PUBLIC-REPORT-AUDIENCE, which already has the independent review; the Observatory retires its three questions and the hold line once that work acknowledges the transfer, and does nothing to the history or access meanwhile.

b) Move the whole matter, both works' questions, to KI State of play (ki.sop.main), because making the repository private affects every work in the Capital.

c) Keep the Observatory's three questions here and answer them separately now.

### ACQUIRE-VIEW - Start the Acquire intake area

**Context:** Kris asked on 31 October and 1 November, as a high priority, for an Acquire area in the Observatory: a read-only view over the local acquire checkout showing the knowledge graph (25 cards, stepping from one to its neighbours), the linkage checks on that graph (one checker, `term_check.py`, exists today), the captures and their review backlog, the territory context, and the roadmap with its work package. The checkout exists on this Mac and the Observatory only listens locally, so Personal content stays on the machine. Where it sits in the five-area layout touches the open restructure question, but need not wait for it.

**Query:** Should the Observatory take up the Acquire intake area now as its top feature?

**Options:**

a) (recommended, confidence high - Kris named it high priority, it only reads a local checkout, and the plan comes back before the rest is built) Write a short plan with slices in Kris's order, graph viewer first, then linkage findings, captures and backlog, context, roadmap; bring the plan to Kris, then build the graph slice first.

b) Skip the plan and build the graph viewer slice straight away, planning the other slices afterwards.

c) Wait until the restructure question settles where it belongs.

### STATUS-FIRST - Bring the work-status repair to adoption

**Context:** An independent review on 29 October showed the Observatory's Work, Waiting and Review views can show wrong answers: excluded work coming back, ambiguous short names, and missing package homes, because fast views bypass the CLI's own reading. Since then the CLI side it relies on has landed (the regular coordination readers, [KI-TOOL-KI-CLI-173](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-173-regular-coordination-readers.md), and the naming change). Two queue lines from Ways of working asking for this check are answered by that review. The estate-wide status read takes over a minute, which a plan must account for.

**Query:** Should the status repair (the open STATUS-REPAIR question) go forward to adoption and a plan now?

**Options:**

a) (recommended, confidence high - independent fixtures show real wrong answers, and the prerequisites are now in place) Adopt one repair that takes status and package home from the CLI across Work, Waiting and Review, keeping the current views; settle the one-minute latency and the CLI's boundary in the plan before building.

b) Keep the defects visible and wait for evidence from the running service before adopting.

c) Tie it to the restructure decision instead.

### NEXT-TOOL - Choose the next new tool

**Context:** Two requests from Ways of working add small tools. Diagram notes: Kris wants to pin comments on a design diagram (the Archify pages in a work's `design/`) and have them reach the worker as feedback (29 October); the Observatory already sends feedback into a work's `messages.md`, so the notes can use that route. The opener button: a work explorer that serves the right opening line for a work by its state, with a copyable launch command (21 October); `ki agent prompts` already prints these, so the button needs no new CLI command. The retirement receipt of 30 October suggested putting diagram notes first. The Acquire area comes before both.

**Query:** Which of the two should follow the Acquire area?

**Options:**

a) (recommended, confidence medium - Kris asked for it directly and it closes the feedback loop in design work, but the opener is smaller) Diagram notes first, using the existing feedback route; the opener button after it.

b) The opener button first, because it is small and its source already exists; diagram notes after.

c) Plan both together as one Work-area slice.

### SYNC-CLOSE - Close the sync-direction question as answered

**Context:** The Observatory's SYNC-DIRECTION question asked who should run the regular cross-Mac Git sync. On 31 October, in Ways of working, Kris said "the observatory is watching, it's not doing the syncing", with ad hoc sync through it a later idea; the 15-minute plan went to the sol and terra Rig threads. Two queue lines (MGIT-SYNC-JOB, OBSERVATORY-SYNC) asked the same thing.

**Query:** Should SYNC-DIRECTION be closed as answered by Kris's 31 October words, and the two sync lines removed?

**Options:**

a) (recommended, confidence high - Kris's own words answer it and the plan is already with the Rig threads) Close it with that answer, record ad hoc sync from the Observatory as an idea, and remove the two lines.

b) Keep it open until the Rig host sync has run for a while.

### HOST-VIEW - Plan what the Host area watches

**Context:** Several requests ask the Host area to show more. The Rig status reader exists but the Bridge does not use it yet (BRIDGE-STALE; an independent review advised keeping this parked while the Machine view is still an idea). Kris wants it to expect each Mac's sync, by which territories it leads (decided on 31 October: every 15 minutes, sol leading Knowledge Islands, Personal and Legal). Scheduled jobs should show when a run found problems. Later asks are live agent state from Claude Code and Codex hooks, and Claude account scores (their log does not exist yet).

**Query:** Should one bounded plan for the Host area be prepared now?

**Options:**

a) (recommended, confidence medium - it gathers five asks into one plan, but the review of the Rig reader advised waiting) Prepare one plan covering Rig state from its existing reader, expected host sync from the seats, and scheduled-run problems, with agent hooks and account scores as later slices; nothing is built until Kris approves it.

b) Keep the Host area as it is until the Rig host sync has run supervised for a week, then plan.

c) Plan only the scheduled-run problems now, as the smallest slice.

### SCHEDULED-FINDINGS - Answer how failed scheduled runs become visible

**Context:** The HNR email routing work asked (28 October) whether the Observatory should read the Failures section of each Route Triage summary, or whether the job wrapper should report a `findings` result instead, a chezmoi change through ki.prj.chezmoi. The Observatory's automation specification already accepts `findings` as a result and ranks it, and deliberately never reads a run's free text. The original specimens stay on terra and hold mail details, so they are read in place only.

**Query:** Which answer should go back to hnr.reg.email-routing?

**Options:**

a) (recommended, confidence medium - it keeps the Observatory's no-free-text rule and the result type already exists, but it moves work to the wrapper) The wrapper reports `findings` when the summary lists failures, through ki.prj.chezmoi; the Observatory needs no change beyond showing it.

b) The Observatory reads the Failures section itself, with a parser and tests over the terra specimens read in place.

### DESIGN-PASS - Hold one design pass over the delivered layout

**Context:** The open design questions are RESTRUCTURE (prepare the remaining convergence choices against the five-area layout), TEN-COMMITS (recheck the commit list and keep history), MERMAID-HANDLER (a hardening follow-up with no shown bypass), the Known Lands chart's look and positions reserved for Kris, and how island maturity and health from the CLI should show on it. Nothing has changed on any of them since 29 October and nothing else waits on them.

**Query:** Should these be taken together in one design pass with Kris, after the Acquire area and the status repair?

**Options:**

a) (recommended, confidence medium - grouping saves Kris separate sessions, but the earlier reviews were each medium) One pass: prepare RESTRUCTURE's remaining choices, recheck the commit list, and propose the Known Lands look and island condition; keep the Mermaid follow-up parked as non-blocking.

b) Leave all of them parked until the design thread next asks.

### TIDY-RUN - Authorise one local housekeeping run

**Context:** Small items have built up: the coordinator's method read is behind (REFRESH); 42 reports wait to be pruned and several queue lines are over 60 words; package links point at `/Users/krisbrown/workspaces/...`, which no longer exists here; the product's AGENTS.md still says to restart the service after each delivery, though it now reloads itself; ki-design still has `docs/spec/` instead of `docs/specs/` (ROUTE-1); the ideas list still calls Focus the front page; and this Mac's registry has no Capital checkout. The ki-design GitHub settings (GH-LIVE) need a GitHub call, and the repository rename (NAMING-TO-KI, to `apps-local.observatory`) touches every machine, so both are left out.

**Query:** Should one local run do the housekeeping, leaving the GitHub settings and the rename for later?

**Options:**

a) (recommended, confidence high - local, reversible, and it removes noise from every later report) One run: refresh the method, prune homed reports, shorten long queue lines, repoint links to `/Users/krisbrown/kis/`, change the AGENTS.md finish line to "confirm the service answers", rename ki-design's `docs/spec/`, fix the ideas wording, and send the registry gap to ki.prj.tools-burndown; GH-LIVE and the rename wait for their own go.

b) Do only the work-package tidy now and leave the product and ki-design changes.

### ESTATE-ROUTE - Pass the 5G Emerge checkout identities to their owner

**Context:** On 27 October the redesign thread found strict estate reads fail on four 5G Emerge checkouts that declare other identities. The Observatory now reads around them and names them, so its part is done; fixing the checkouts is not Observatory work. The missing Notion mirror checkout has since been retired.

**Query:** May this part go as one line to the 5G Emerge State of play, hnr.sop.5ge?

**Options:**

a) (recommended, confidence medium - the checkouts are HNR's, but whether their identities are wrong or intended is unverified) Send one line to hnr.sop.5ge describing the failing reads, then remove ESTATE-IDENTITY.

b) Send it to hnr.sop.main instead, as HNR's main State of play.

c) Keep the line here until someone checks whether the identities are intended.

### 🤖 → 👤 Handoff to supervisor · since 00:46 GMT

👤 10 with you

- [with you] PUBLICATION-ONE · owner · since 00:46 GMT
- [with you] ACQUIRE-VIEW · owner · since 00:46 GMT
- [with you] STATUS-FIRST · owner · since 00:46 GMT
- [with you] NEXT-TOOL · owner · since 00:46 GMT
- [with you] SYNC-CLOSE · owner · since 00:46 GMT
- [with you] HOST-VIEW · owner · since 00:46 GMT
- [with you] SCHEDULED-FINDINGS · owner · since 00:46 GMT
- [with you] DESIGN-PASS · owner · since 00:46 GMT
- [with you] TIDY-RUN · owner · since 00:46 GMT
- [with you] ESTATE-ROUTE · owner · since 00:46 GMT

🧵 ki.prj.observatory
