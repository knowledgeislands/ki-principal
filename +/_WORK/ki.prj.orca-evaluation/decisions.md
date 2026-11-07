# ki.prj.orca-evaluation decisions

## 2026-10-30 - ORCA-EVAL

- Kris approved this Project on 30 October: "I'm actually okay with that ... I'd like to keep those ones open." It takes over the Orca trial evidence and ORCA-HOST from ki.prj.mac-studio-setup and the ORCA-FIT notes from ki.prj.ways-of-working as each sends them; the landscape study feeds in. Received at bootstrap; disposition in `state.md` next steps.

## 2026-10-30 - ORCA-HOST

- Passed here from ki.prj.mac-studio-setup under ORCA-HANDOVER. Kris's words of 29 October, for that Project: "for this Project, dispatch runs through Orca orchestration instead of `ki agent`. ... Create one Run for this Project, then dispatch with `orchestration worker-start --worktree current --agent codex`, and wait with `orchestration check --wait`. Every other ki-coordination rule still applies. The work package stays the record." Mac Studio setup ran one unit (plan069) under it and returned to `ki agent` on 30 October (KI-AGENT-DISPATCH); Run `run_0de85069bc1d` stays on sol. Whether this Project dispatches through Orca needs its own logged opt-in under ORCA-REACH; until then it uses `ki agent`.

## 2026-10-30 - ORCA-SKILL

- Kris's go of 30 October: after two or three units, crystallise the trial into a proposal for an Orca launcher under ki-delegation and ki-coordination. The remaining units are this Project's to plan.

## 2026-10-30 - ORCA-REACH

- Kris took a) on 30 October, "as recommended but follow up in weeks time" (follow-up due 6 November 2026): Orca only on attended Macs, packages opting in by logged decision; `ki agent` stays the only launcher on `vega`; Orca on `vega` comes back as its own decision with remote-delivery proof; an always-on Orca server goes through the Enactment Process.

## 2026-10-30 - WAKE-SESSION

- Kris took a) on 30 October: one contract verb, `wait`, implemented natively by each launcher, one detached waiter at a time, bounded at five minutes and re-armed after each wake; wake and acknowledgement proved per runtime and launcher, no seen event lost; session wakes best effort. This Project owns the Orca half: prove `orca orchestration check --wait` under that contract in Claude Code and Codex.

## 2026-10-30 - WAKE-DURABLE

- Kris took a) on 30 October: the headless coordinator pass stays the durable wake; Orca automations are not adopted as the durable wake and stay out of the trial's wake design.

## 2026-10-30 - RESET-DUP

- Withdrawn before it reached Kris: the blind review found unpublished local commits beside the two duplicates, so a reset would lose work. Resolved instead by the bounded run `resolve-merge`, merging origin/main in its own worktree and pushing fast-forward; no reset.

## 2026-10-30 - ORCA-OPTIN (steer)

- Kris, 11:28 GMT: "that's why we need to be using the [Orca] capability to create subagents and not the KI agent one. But I presume that's something which has been looked at by ways of working." Taken as direction toward Orca dispatch; asked whether it answers ORCA-OPTIN and with which scope, a) or b).

## 2026-10-30 - RESOLVE-BRIEF

- Coordinator's own call, within the work package: the add/add conflict on the spent resolve-push brief is resolved by deleting it in the merge, and resolve-merge is relaunched to publish.

## 2026-10-30 - ORCA-OPTIN

- Kris, 11:29 GMT: "ORCA-OPTIN - b)". Read back: ki.prj.orca-evaluation opts in to Orca dispatch for all of its runs on attended Macs, under ORCA-REACH, until Kris revokes it; one new Orca Run for this Project (not Mac Studio's `run_0de85069bc1d`); never on `vega`; no Orca automations as wakes (WAKE-DURABLE). Runs already launched through `ki agent` finish there; new units launch through `orca orchestration worker-start`.

## 2026-10-31 - BOOTSTRAP-MESSAGES

- Coordinator's dispositions at re-bootstrap, 23:20 GMT: the two REFRESH lines are taken (`method_read` to `df3f5503`); ORCA-DISPATCH-LEARNINGS and ORCA-MOVE-LESSON go to the evidence-homing run (next step 4); ORCA-SUBAGENT-PILOT folds into trial unit 1 with NEST-TRIAL; ORCA-REMOTE-VIEW becomes an ORCA-HOST investigation run; ORCA-CARD-BUG, which Kris authorised on 31 October ("Yes, via the Orca evaluation work"), and ORCA-SETTINGS-READ join the bundled Orca request draft (next step 3), the card bug sendable on its own authority; ORCA-ENV-LEAK-LANDED narrows ORCA-IDENTITY-LEAK to the remaining variables. Launches wait on ORCA-RUN-REBIND, since the Project's Run is bound to the previous session.

## 2026-11-01 - STOCK-TAKE

- Kris, 00:40 GMT: "I've been using Orca a little while now ... I think it is the way forwards ... let's take stock and really look to see where there are some things that are consolidated now." Taken as the go for ORCA-RUN-REBIND a), a new Run for this Project with the old `run_30f79294698c` retired (Kris may revert), and as authority for a read-only stock-take run proposing consolidated queries, a reshaped plan and transfers to ki.prj.ways-of-working.

## 2026-11-01 - STOCK-TAKE received 00:52 GMT

- report at ~/.local/state/ki/agents/ki-prj-orca-evaluation/stock-take.report.md. Coordinator consolidated the ten queries to four: ORCA-RUN-REBIND answered; NEST-TRIAL overtaken by ORCA-SUBAGENT-PILOT; TRIAL-UNITS into TRIAL-SHAPE; TRIAL-PUBLISH, TRIAL-ASK, TRIAL-PRACTICE and ORCA-IDENTITY-LEAK into SCOPE-SPLIT; NEST-FR, ORCA-SIDEBAR-FR and LABEL-FIRST into ORCA-UPSTREAM, which goes to blind review first (medium). The `state.md` Run id line conflicts with ORCA-ROUTING; kept as a known exception until a machine-local routing record exists.

## 2026-11-01 - ORCA-CARD-BUG send

- On Kris's authorisation of 31 October ("Yes, via the Orca evaluation work"), the card line-break bug is filed alone through run `file-card-bug`; the blind review of ORCA-UPSTREAM (report review-upstream) recommended it go on its own, one report per problem, and ORCA-UPSTREAM now asks only about the other four.

## 2026-11-01 - ORCA-CARD-BUG filed

- Run `file-card-bug` filed [stablyai/orca#36830](https://github.com/stablyai/orca/issues/36830) at 00:47 GMT; no duplicate found; nothing else sent. Receipt sent to ki.prj.ways-of-working.

## 2026-11-01 - TRIAL-SHAPE

- Kris, 01:29 GMT: "we do now see that they're nested under coordinator's row. And yes, Orca's wait command does work like that. And then a chat coordinator can release a finished worker. Yep, and whether a worker survived, I don't know. Other than the last one, just seems like more of a technical detail to me." Read back: nesting, the wait-command wake in a Claude Code chat and release from a chat are proved by Kris's own observation; survival of a worker when its coordinator chat ends is left as a technical detail for first live use. No pilot unit; unit 1 is now evidence homing only, then unit 2.

## 2026-11-01 - ORCA-SKILL-NOW

- Kris, 01:29 GMT: "go with what you recommend on the Orca skills now." Read back: a) - draft the Orca launcher proposal straight after unit 1 lands, as a design note in this package, then a message to ki.prj.ways-of-working for adoption.

## 2026-11-01 - ORCA-LAUNCHER sent

- Unit 2 received 01:33 GMT; proposal committed as `trial/orca-launcher.md` and handed to ki.prj.ways-of-working for adoption under ORCA-SKILL-NOW a). The trial is complete apart from worker survival, left to first live use (TRIAL-SHAPE).

## 2026-11-01 - WORKER-THREADS

- Kris, 09:38 GMT: ephemeral Orca worker threads ("You are working inside Orca, a multi-agent IDE. You are a dispatched worker.") crowd the ChatGPT app's recents; "once they're finished with, I think they should just be deleted ... How does Orca suggest we deal with that?" Taken as a read-only investigation run, worker-threads; nothing deleted until Kris decides.

## 2026-11-01 - WORKER-THREADS received 09:43 GMT

- investigation and blind review back; the review agreed with archive-through-Codex plus an Orca request but at medium, since archiving from the command line is not yet shown to clear the ChatGPT list. Split into THREADS-TRY, THREADS-SWEEP and THREADS-FR. Orca itself offers nothing for this.

## 2026-11-02 - HANDOVER-ASSISTANT received 15:23 GMT

- Kris asked "I thought this was wrapped up or moved - was it". Not yet: the IMPORTANT handover line of 1 November landed after this thread's last send and was not acted on, since the thread was not listening. Acting on it now under Kris's ASSISTANT-NOW and FOCUS-ASSISTANT words of 1 November: handover note through run handover, then a line to personal.reg.assistant-terra and a hold pending close-out. ORCA-AUTO-RELEASE goes into the handover.

## 2026-11-02 - HOLD

- Handover note received 15:24 GMT and sent to personal.reg.assistant-terra as an IMPORTANT line; ORCA-AUTO-RELEASE passed with it. The three REFRESH lines are taken (`method_read` to `b3c631c2`). Five queries parked and carried by the assistant; work on hold pending close-out.

## 2026-11-03 - DRAIN-TO-SOP

- Kris, 03:10 GMT: "drain down because we're gonna move all of the work to be coordinated through the SOP main." Read back: this thread stops coordinating; the work was already drained and on hold (handed to personal.reg.assistant-terra on 2 November), nothing running, no unreleased Orca workers; close-out and any further coordination pass to ki.sop.main by a message line.

## 2026-11-03 03:25 GMT - SOLE-THREAD acknowledgement

class: operational

- Coordination taken up by ki.sop.main, 3 Nov, (Kris, 3 Nov about 03:10 GMT: "move all of the work to be coordinated through the SOP main"; SOLE-THREAD in ki.sop.main, 03:14 GMT). The work stays On hold; every parked discussion stays parked, unanswered, for ki.sop.main to bring to Kris. Hold reason set to `paused` (AUDIT-FIXES); the release keeps the close-out once personal.reg.assistant-terra acknowledges the handover. Run handover-intake.

## 2026-11-07 02:28 GMT - ORCA-HOME routing

class: operational

- Kris took ORCA-HOME a) on 7 November (ki.reg.guilds MSG-8125375d, logged in ki.sop.main): the guild takes SCOPE-SPLIT's four method questions; Orca usage evidence and feedback to the Orca team go to the Inbox under ORCA-CLOSE-HOME. ki.sop.main, acting for this held package, routed TRIAL-PUBLISH, TRIAL-ASK, TRIAL-PRACTICE and ORCA-IDENTITY-LEAK to ki.reg.guilds' `messages.md` (ki-agentic-harness `84f660d3`), which settles SCOPE-SPLIT's handover in place of the five lines it proposed to Ways of working, and removed SCOPE-SPLIT from `discussions.md`. ORCA-UPSTREAM, THREADS-TRY, THREADS-SWEEP, THREADS-FR and the `trial/` notes stay for ORCA-CLOSE-HOME.
