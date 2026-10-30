# ki.prj.orca-evaluation queries

## Open

### ORCA-OPTIN - This package opts in to Orca dispatch for the trial

**Context:** ORCA-REACH (30 October) lets a package use Orca only after a logged decision, and only on attended Macs. Until that decision, ki.prj.orca-evaluation launches through `ki agent`. The plan needs Orca for units 1 to 3, all on sol, with you present, in a new Run for this Project (the Mac Studio Run `run_0de85069bc1d` would not be reused).

**Query:** Does ki.prj.orca-evaluation opt in to Orca dispatch for its trial units?

**Options:**

a) (recommended, confidence high - it is exactly the bounded opt-in ORCA-REACH provides for and the plan keeps every bound) Opt in for the trial units only: sol, attended, one new Run. The opt-in ends when the ORCA-SKILL proposal is received or at the 6 November ORCA-REACH follow-up, whichever comes first. All other work in this package stays on `ki agent`.

b) Opt in for all of this package's dispatch on attended Macs until you revoke it.

c) Do not opt in yet. Wait for the ORCA-FIT notes and the second brief's line to arrive first.

### TRIAL-UNITS - The units and their order

**Context:** The plan proposes three units, all real work this package owns. Unit 1 (WAKE, legs A and B) proves `check --wait` in Claude Code and Codex while doing the Orca setup inventory. Unit 2 (LIVE) maps Orca's recovery, queue, ack and status verbs and commits that map in ki-principal. Unit 3 (SKILL, optional) drafts the ORCA-SKILL proposal under Orca. Leg B needs you to open a Codex session on this package. Units 1 and 2 should land before 6 November.

**Query:** Do you adopt units 1, 2 and 3 in that order, with unit 3 optional?

**Options:**

a) (recommended, confidence high - reviewed, the blind review agreed; units 1 and 2 cover WAKE-SESSION and the plan069 failure, but whether to dogfood the proposal is a judgement call) Run 1A, 1B and 2. Then decide on unit 3, or draft the ORCA-SKILL proposal through `ki agent`, once unit 2's evidence is in.

b) Run all three in order, with unit 3 under Orca as planned.

c) Run unit 1 only, then come back with its evidence before anything else.

### TRIAL-PUBLISH - How a trial worker publishes in ki-principal

**Context:** ki-principal's pre-commit hook runs lint-staged, which creates and drops a backup stash. In plan069, a no-stash rule in the brief collided with that stash. The run's `worker_done` read `failed` although the work had succeeded, and you then granted a bounded exception for the report-only commit. Units 2 and 3 each produce a design note, and the trial workers share the checkout with other sessions.

**Query:** How should units 2 and 3 publish their notes?

**Options:**

a) (recommended, confidence high - reviewed, the blind review agreed; it tests the worker-commit path the adapter needs while keeping the exception narrow and stated up front) Each brief carries a bounded exception from the start. The worker commits its own note by explicit path inside a write window granted by ask, and the repository's hook may create and drop lint-staged's backup stash. The worker itself never runs `git stash`. The coordinator pushes at receive.

b) No worker commits. The worker writes the note and its report, and the coordinator commits both at receive.

### TRIAL-ASK - How a question only you can answer travels

**Context:** An Orca ask blocks the worker. It times out after 10 minutes by default (30 at most), and a question left unanswered at timeout stays pending and can be resumed by message id. In plan069, an ask timed out after ten minutes and escalated, and you answered it in chat instead. The ORCA-FIT draft's OF-OWNER-ASK has not been handed over yet; its recommended option ends the worker's attempt with a blocking query.

**Query:** During the trial, how does a worker raise a question only you can answer?

**Options:**

a) (recommended, confidence high - reviewed, the blind review agreed; it keeps the ask for what the coordinator can answer and needs no one to stay attentive for half an hour) The coordinator answers its own asks with `--timeout-ms 1800000`, resuming by message id on timeout. A question only you can answer ends the attempt: the worker raises it as a blocking query, `worker_done --outcome failed` names its tag, and the coordinator records it in `queries.md` and retries after you answer.

b) The worker keeps the ask open while the coordinator relays it to you, and resumes the same message after each 30-minute timeout.

### TRIAL-PRACTICE - Provisional working practice until the ORCA-FIT notes arrive

**Context:** The units need a working rule for ids, specifications, liveness and reports. The ORCA-FIT draft recommends one for each: ids go on a `state.md` Now line; the specification is the full rendered prompt; liveness comes from Orca heartbeats only; and reports go outside the repository, named by `--report-path`. That draft has not been handed to this package. The plan uses these rules for the trial only and decides none of the open choices.

**Query:** Do the units run on the ORCA-FIT draft's recommended practice as a provisional, trial-only rule?

**Options:**

a) (recommended, confidence high - reviewed, the blind review agreed; it lets the trial generate evidence for those choices without settling them early) Yes, provisionally and for the trial only. The units' evidence then goes back to the ORCA-FIT choices when the notes arrive.

b) No. Wait for the ORCA-FIT notes and settle those choices before any unit runs.

### NEST-TRIAL - Prove run nesting inside the trial

**Context:** Orca nests a run under its coordinator only when it started the run itself (`orca orchestration worker-start` or `dispatch`), which records the coordinator as parent; the coordinator's row then gets a collapsible "N agents" group, and the Agents-list switch "Show child agents" (off on sol) reveals the child rows. Detached `ki agent` runs cannot claim a parent, so they stay flat. This is read from Orca's code and has not been seen on screen. The trial already plans Orca-dispatched units, and the Orca launcher proposal (ORCA-SKILL) follows them.

**Query:** Should the trial's next Orca-dispatched unit check the nesting on screen, and ORCA-SKILL count it as a benefit of the Orca launcher?

**Options:**

a) (recommended, confidence high - reviewed, the blind review agreed; it costs nothing extra and settles what the code suggests) Yes: switch "Show child agents" on and record what the coordinator's row shows in the trial evidence; `ki agent` runs stay flat until the launcher decision.

b) Try the low-level route now instead: run an agent in an Orca terminal and attach an orchestration Task to it, keeping `ki agent`'s lifecycle; untested, and Orca's guide calls it unsupervised.

### NEST-FR - Ask Orca for a supported way for outside sessions to declare a parent

**Context:** Today only Orca's orchestration records give a row a parent; a session Orca did not start, such as a `ki agent` run, has no supported way to declare a parent or a display name. A feature request would ask for one (an `orca agent attach --parent ... --name ...` command or a documented hook variable). Views differ: the investigating run would fold nesting into the trial and not ask yet; the blind review would ask now, so that runs keeping `ki agent`'s lifecycle could nest. If you take Orca as the launcher for this work, the request matters less. It could go together with the sidebar request (ORCA-SIDEBAR-FR). Sending it is an outbound action.

**Query:** Should a feature request for outside sessions to declare a parent go to Orca now?

**Options:**

a) (recommended, confidence medium - views differ: the review favours asking now, but your steer towards Orca's own launcher lowers its value) Hold it until trial unit 1 has shown nesting on screen, then decide, bundled with any other Orca feedback.

b) Send it now, bundled with the sidebar request.

### ORCA-IDENTITY-LEAK - Stop `ki agent` runs inheriting the coordinator's Orca identity

**Context:** `ki agent` passes its whole environment to each run, so a run started from an Orca chat coordinator carries the coordinator's Orca session id and spawn token. `orca status` from inside this run reports it as the coordinator, live. Orca uses that id to work out who is calling an orchestration command, so an `orca orchestration check`, `send` or `ask` from a run would act as the coordinator, for example taking the coordinator's Run mail. A coordinator in an Orca terminal pane would pass on its pane and hook variables too. Fixing it means changing `ki agent`, which ki.prj.ways-of-working owns. If terra's runs appear only through inherited pane variables, removing those variables may also take the runs out of terra's list.

**Query:** Should this Project send ki.prj.ways-of-working a message asking `ki agent` to remove inherited Orca identity variables from the runs it starts?

**Options:**

a) (recommended, confidence high - reviewed, the blind review agreed; the leak was seen directly, but how removing the variables affects terra's list is unverified) Send the message. It asks `ki agent` to drop `ORCA_AGENT_SESSION_ID`, `ORCA_AGENT_SESSION_SPAWN_TOKEN`, `ORCA_STRUCTURED_SESSION`, `ORCA_PANE_KEY`, `ORCA_TAB_ID`, `ORCA_WORKTREE_ID` and the `ORCA_AGENT_HOOK_*` variables from the runs it starts, and to check terra's list afterwards.

b) Hold it until the attended terra check shows how terra lists the runs, then decide.

c) Leave `ki agent` unchanged and add a brief rule that runs must not call `orca orchestration` commands.

### ORCA-SIDEBAR-FR - Feature request for a clearer way to show hidden items

**Context:** Hiding is one click on the item itself. Showing it again is only possible from Settings > Appearance > Sidebar, or for Mobile from the Mobile page's toolbar, and the sidebar itself gives no hint of either. The message shown after hiding Mobile also points to the wrong Settings page. The control exists, so this is about how easy it is to find, not a missing feature.

**Query:** Should a short feature request go to Orca asking for an obvious way to show hidden items?

**Options:**

a) (recommended, confidence medium - the control exists but you could not find it, which is the usability gap a request would fix) Send one short request. It would ask that hiding an item shows a message linking to Settings > Appearance > Sidebar, or that the sidebar's right-click menu lists hidden items to show again, and that the "Settings > Mobile" message is corrected.

b) Do not send a request. Note the Settings location in the Orca evaluation and move on.

## Parked

None.
