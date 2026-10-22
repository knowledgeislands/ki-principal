# Decisions

## 2026-10-17 23:09 BST - COUNSEL

- COUNSEL - (Kris, 17 October 23:09 BST) "I'm hoping this conversational style is quite useful, by the way. It helps me to sort of express the different things I'm thinking. As a general thing about me, I'll talk through things and give different perspectives on it. I'm not going to say what I want it to be, and I also want to have good counsel given to me by the agentic system as well. It's not me dictating." Applied in briefs: weigh and challenge Kris's model rather than transcribe it.

## 2026-10-18 02:47 BST - UPDATE-SHAPE

- UPDATE-SHAPE - (Kris, 18 October) "Every update, I want to know what's outstanding, what's left on the plan, and what's been done."; applied in this work's timed updates. Its adoption for every coordinator waits for the report-shape review around 21 October, in `state.md` Next steps (its record was cancelled to a message line).

## 2026-10-18 02:49 BST - MECHANICAL

Kris, as received: "I want you to delegate and use mechnical commands as much as possible"

Taken as: every unit is delegated, and each run prefers mechanical commands over hand edits - a generated plan run as a script (`git mv`, `sed`, `ki` subcommands, generators), dry run first, then applied and checked - with hand edits only where judgement is needed.

## 2026-10-18 09:2x BST - owner note, website

> Okay, by the way, I've got Claude Design making some improvements to the website. So don't worry if you see changes there.

Read back as taken: runs leave another session's changes in apps-knowledgeislands.info and ki-design alone. OVERNIGHT-BURNDOWN lifted the stay-out for that burndown only.

## 2026-10-19 - work-package owner words

Kris's words from the work-package design note, kept here when the note was deleted on 20 October, with the read-backs as taken; the behaviour they set is homed in `ki-work-package`, `ki-coordination`, the Work Process note and GDR-KI-PRINCIPAL-009. The note's last text is at <https://github.com/knowledgeislands/ki-principal/blob/fba56feb/+/_WORK/ki.ways-of-working/design/work-package.md>.

### Owner's proposal

Kris, 19 October 2026, 12:09 BST, "owner request, WORK-ROUTING model", speech lightly cleaned:

> your ways of working is really good. You've got multiple reviewers for the recommendations and I don't think other threads are doing that. Also, there's now a number of active threads, and I think somehow we need to mark them as active so that we know that we can push work to them, because we don't want to just create any thread to do any work ... if a thread is parked, that's fine, we can also push work into it ... the state of play decides [which] thread of work and the work package ... you can give me a prompt for me to ask it. If it then decides it's your work, you have to accept it. And as we make improvements to the ways of working, presumably we need a thread to periodically refresh itself from the ways of working ... how would we do that? And also, if a thread has a potential way to improve the way of working, it should also ask me to give that to the ways of working ... ways of working and state of play probably overlap ... Perhaps there's two high-level coordination pieces: one which is state of play, and one which is ways of working. What do you think?

Kris, 19 October 2026, 12:24 BST, "owner answers, WORK-ROUTING and WOW-REFRESH; request WORK-PACKAGE":

> I agree about the split of state of play. I think ways of working goes away and actually then usually state of play is a dispatch agent overall. So actually improvements should really go back to state of play. The exception to that obviously is whilst we're defining the ways of working, that ways of working can directly do that into the other [works], like we say on the refresh, whereas ordinarily that would come from [state of play] ... looking at the work folders ... Are they work packages? ... the work package needs a really clear understanding ... like we talked about before with skills and also with knowledge ... work should have a package idea and it should be clear about what its goals are and maybe a description to help things route it, so we've got that kind of progressive reveal capability ... think about what the file structures are within it, like a skill has. So we have a work.md file which defines what it is. Currently a lot of the work.md files have got loads of stuff in them ... maybe that should be another file so it's really quite straightforward ... like the decisions one, there should be a Q one ... take a bit of a stock take really. Can you take all this into account please and think what we should do? Maybe get a review on it as well from some high-level models.

Read back and taken, same entry:

> - WORK-ROUTING - split agreed, amended: State of play is the single dispatch coordinator; it routes work and receives method improvements from every work. Ways of working is finite: once the method is defined it goes away, and its stewardship passes to State of play.
> - WOW-REFRESH - a) for now: while the method is being defined, Ways of working writes refresh lines straight into live work files; afterwards refreshes come from State of play.
> - WORK-PACKAGE - design the work folder as a package, as a skill is: `work.md` defines the work (name, goals, a routing description for progressive reveal), with state, next steps, queries, decisions and parked items in their own files; settle the name; stocktake every current work folder.

### Owner's answers

Kris, 19 October 2026, 13:37 BST, "owner answers, work package; mark":

> None of the other threads are active at the minute, so I think we [change] the work package to what we've now described with the different files in it. work.md, queries.md, messages.md and decisions.md. Also, I want `ki-work-package` please, where it lives is a folder. Take that into account and then come back with revised queries.

Read back and taken, same entry:

> - PACKAGE-NAME - the idea and its skill are the work package, `ki-work-package` (renamed from `ki-work-folder`); the place it lives is still called the work folder, `+/_WORK/<id>/`.
> - FILES - a work package has four files: `work.md`, `queries.md`, `messages.md` and `decisions.md`. No `state.md`: state, next steps and held items stay in `work.md` (taken; confirmed in the revised queries).
> - MIGRATE-NOW - no other thread is active, so the live folders can move in one pass rather than each at its own mark; the exact steps come back as revised queries before any migration run.

Kris, 19 October 2026, 13:52 BST, "owner answer, STATE-FILE":

> oh - if you suggested state.md then that was my oversight

Read back and taken, same entry:

> STATE-FILE b) - keep `state.md`. A work package has five files: `work.md` (definition: identity, routing description, goals, scope), `state.md` (state fields, Now, Next steps, Held, Queue for territory work), `queries.md`, `messages.md` and `decisions.md`. This brings back the readers-first step (`ki work status` and the Observatory read both shapes before the pass). The rest of the 13:37 answers stand.

Kris, 19 October 2026, 14:02 BST, "owner answers, 13:51 Summary; request WORK-QUEUE-PRIORITY", speech lightly cleaned:

> file to creation ... create them, 'cause then someone can send messages or whatever to that to start queuing work up ... Yes to the recommended [queries] files. Yes, the [parked] ... I agree with the description shape recommendation. The route [receipt] is interesting, so work is actually given from the state of play to that particular work package, and the key thing is that effectively, once it's given it, it has to do something with it, it can't reject it, it can then say it wants it to be given to someone else, and we can pass that message back to the state of play. But we have to be careful about things just [bouncing] in between things, right? So you should try to do what you can with it at least, and give back anything else it feels is not good for it. Yes ... Yes, the pickup reads. Yes, the state history. Ways of working can come back as a project to life if we need to improve the ways of working ... it becomes the model ... potentially it could be ways of working or it could be a more targeted project. The state of play should keep an eye on things if it thinks there's improvements, it should be responsible for coordinating that ... everything should be trying to continually improve and I think that should be coordinated by state of play ... I agree with the [rename]. We just need to get that done as quickly as we can and in parallel. ... [migrate path] makes sense. Do we need to do it in the pilot? ... do as you recommend. Yes migrate gate. Yes migrate self. ... the fields ... I think also we should just do those ... so we can get on with that. Something else ... the priority of work. Whatever the order of priority of work is, it should come into the queue ... an agent working on that work package ... can [group] things to make sense for things like similar work ... But if something's added to the top of it with an important flag, it must be processed in that order and that allows the state of play to tell something to change its way of working, for example.

Read back and taken, same entry:

> - FILES-AT-CREATION a) - all five files exist from creation, so others can queue work into `messages.md` at once.
> - QUERIES-FILE a), PARKED-HOME a) (Held in `state.md`), DESCRIPTION-SHAPE a), REFRESH-TARGET a), INBOX-CHECK a) (taken from "yes" between REFRESH-TARGET and PICKUP-READS), PICKUP-READS a), STATE-HISTORY a).
> - ROUTE-RECEIPT a), amended - a work cannot reject routed work; it does what it can with it and gives back to State of play only the part it judges is not its own, with a reason; a unit is returned once and then goes to Kris, so nothing bounces between works.
> - STEWARD-HOME a), amended - State of play watches for improvements and coordinates continual improvement; a significant change revives Ways of working, or a more targeted Project under the Model theme, as a Project.
> - RENAME-ORDER a) - as fast as possible, in parallel runs.
> - MIGRATE-PATH a) with this work as pilot; MIGRATE-GATE a); MIGRATE-SELF a).
> - WORK-QUEUE-PRIORITY - a work package's incoming work is a queue taken in priority order; the worker may group similar items; a line added at the top with an important flag must be taken first, in that order, which lets State of play change how a work works.

## 2026-10-19 18:19 BST - owner note, LOCAL-MODE

Kris: "btw, both machines are in local mode so if they pull they have the latest tools"

Read back taken: Terra and Sol run the tools from their checkouts, so a pull gives them the current `ki` and harness; no per-machine install step is needed there.

## 2026-10-19 22:17 BST - lesson, half-done harness checkout

link1-baseline: a run editing the harness checkout breaks every island's pre-commit audit while its edit is half-done (22:12 to 22:14 BST, 19 October). Not yet in [Mistakes and Lessons](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Mistakes and Lessons.md>); harness edits run in worktrees since.

## 2026-10-20 03:34 BST - owner answers, NET-DOWN and WIP-CAP

- NET-DOWN, Kris: "the net downtrend is important ... something we can track and see in the observatory based on the data which is in the roadmap items ... I don't think there's anything we need to actually change at this point. We just need to keep on top of it." Taken as: no rule or tooling now; State of play keeps an eye on it; an Observatory trend view stays an idea.
- WIP-CAP, Kris: "I agree with WIP limits in general ... the more thinking needs to go around ... can we move some things forwards quicker, get things reviewed?" Taken as: WIP limits in principle, no number yet; the effort goes into faster review and acceptance.

## 2026-10-20 05:20 BST - owner answers on the 04:22 send; OVERNIGHT-BURNDOWN

Kris: "first of all, take a mark because I'm reviewing the last input to me." Taken as: mark struck now.

- SINGLE-FIGURES, "we should be trying to be running at that level. We shouldn't be running at hundreds ... we can't see the wood for the trees." Taken as: a), each repository runs under ten as a standing level.
- SWEEP-ACCEPT-OBSERVATORY, "let's sweep through all the acceptance of the observatory, and then get everything that's been accepted so far pruned. Same for the tools burned down, same for the ways of working." Taken as: a) accept the eleven reviewed Observatory-bundle records; SWEEP-ACCEPT-TOOLS-BURNDOWN a) accept the three Rig records, Knip as a message; SWEEP-ACCEPT-WAYS-OF-WORKING a) prepare the five and bring back those that pass; prune every accepted record.
- SWEEP-MERGE, SWEEP-CONVERT, SWEEP-CANCEL, "I agree with sweep merge ... should become message records ... and also cancel the rig record". Taken as: a) on all three.
- SWEEP-RIG-026, "we can cancel the development mode switch ... There's already enough command surface". Taken as: a).
- SWEEP-DELIVER, "They're authorized, so go along with those, fine with which we integrate." Taken as: a), with the reviewed stops.
- WORKTREE-START and WORKTREE-INTEGRATE, "do whatever that needs to be and the work tree order needs to be a case as well". Taken as: a) on both, and WORKTREE-AUDIT a) ("work tree order" read as worktree audit).
- "Any recommendations is when I say agreed." Taken as: "agreed" means the recommended option.
- MATURITY-DECLINE a); RENDER-CHECK a) ("Vendor check fine"); SIZED-EMBEDS a) ("we can go with the recommendation"); TEMPLATE-LINKS a); LINK-REVIEW-NAME a); GFM-HOSTING-RULES a) leave; STASH-DROP a) drop both; CAPTURE-ORIGIN a) drop; MARK-HABIT a).

OVERNIGHT-BURNDOWN, Kris: "I'm not going to enable the other threads ... get all of the tools burnt down and then all of the MCPs burnt down. You're going to have complete control, there's no one else running from now on ... No other threads on any other machines ... If you get stuck on something, the right approach is to ask a high reasoning model what it thinks. You can check both Astra and Fable ... and then do what they say ... follow-ups ... add it to the message list for the area ... a real clear goal here is going to be basically getting the roadmaps down to zero for all of tools, all of MCP, and all of the apps. So, knowledge islands and observatory ... even start to tidy up some of the other ones as well. And then we can have a good run at whatever's left in the agentic harness ... keep you know motoring through them, committing and pushing as you go."

Taken as: this work coordinates an overnight burndown in order tools, MCPs, apps (website and Observatory), other repositories, then the harness. One delivery run per repository, in worktrees, fast-forwarding its own branch and pushing its own commits as it goes. Each delivered record gets an independent blind review; a pass is accepted under this grant and pruned; anything needing Kris's own eyes, an attended action or publication waits for the morning. Stuck items go to Astra and Fable reviews and their answer is followed. Follow-ups go as `messages.md` lines or Idea lines, never new records. Other sessions' stacked commits stay unpushed (PUSH-NOT-WITH-YOU). The earlier stay-out of ki-design and apps-knowledgeislands.info is lifted for this burndown.

## 2026-10-20 22:03 BST - self-serve burndown

SELF-SERVE-BURNDOWN - Kris, 20 October 2026, 22:03 BST: "Is there anything more that you can do by yourself without me? To try and get that vote back down before I re-open lots of other threads? ... roadmap down" Live work is carried in [state.md](state.md) under the [01:55 grant](#2026-10-21-0155-bst---overnight-run-through-grant).

## 2026-10-20 23:30 BST - ENACTMENT-ADMIN

Kris: "ENACTMENT-ADMIN ok lets go safe with a) but we will need to consider it soon"

Taken as: a) after blind review. The gate stays on Admin, Pillars and Resources (SDR-KI-PRINCIPAL-004); the portable gate statements name `Admin/` alongside them, the Great Library's section stays Pillars-only, and the island's Enactment Process widens the owner-instruction stand-in so one approved scope covers a batch of related edits. No new decision record, no harness change. Narrowing the gate (the tiered or Admin-only options) stays open and comes back to Kris soon, carried as an open point in state.md, not a record.

## 2026-10-21 01:40 BST - overnight answers and mark

OVERNIGHT-HOLDS - Kris, 21 October 2026 01:40 BST: the [01:55 grant and its unchanged exclusions](#2026-10-21-0155-bst---overnight-run-through-grant), [queries](queries.md) and [state](state.md) carry the live authority and holds.

## 2026-10-21 01:55 BST - overnight run-through grant

Kris: "Okay, and you can keep going as long as you can on all the roadmap items, get as many things through to approved and even done if you want, and get them pushed. I'm happy for you to just make it all work."

Read back as taken:

- Overnight, runs may take any open roadmap record in the tools-, mcp- and apps- repositories and the work's own records to Ready (approved), deliver it and accept it (done). Each acceptance brief quotes this grant as its override of the standing rule "Never accept work records".
- Runs push their own commits fast-forward only. Other sessions' stacked commits stay unpushed, as Kris set on 2026-10-19 ("I can just push it").
- Unchanged by this grant: the 01:40 answers and their holds (email routing, KI-TOOL-RIG-CORE-053, KI-TOOL-KI-CLI-139, -145, -149, -160, KI-TOOL-RIG-CORE-064, the Observatory follow-ups, BRG-004, BRG-005 and SITE-044); Kris tags and publishes releases; no live applies, credentials, source deletion or new capture beyond approved splits; a record needing Kris's judgement or presence stays as a query for the morning.

## 2026-10-21 02:06 BST - audit home and skip-and-continue (coordinator, under the 01:55 grant)

The first queue runs stopped on prerequisites the planner's briefs set narrower than the standard: tools-ki stopped at its first unclear line (DEFAULTS-CONTRACT, left for Kris), and the Observatory found no prepared isolated audit home (AUDIT-HOME). Under Kris's 01:55 words "I'm happy for you to just make it all work", the coordinator took AUDIT-HOME b): a run prepares one offline isolated audit home from installed local material only, with no download or real-registry change, and the briefs name it. Multi-line runs now skip an unclear line, return it as a query and continue.

## 2026-10-21 03:47 BST - audit home registries

Coordinator, under the 01:55 grant, answering AUDIT-REGISTRIES a) from wow-night-cli-140-plan-d and OPS009-PREFLIGHT's cause from wow-night-tools-ki-queue-d: wow-night-audit-home-registries documents local-only Capital and territory registration in a copied audit home and proves a roadmap audit without ITEM-2 warnings; CLI-140 planning then reruns as wow-night-cli-140-plan-e.

## 2026-10-21 04:21 BST - pre-existing warnings pass

Coordinator, under the 01:55 grant, answering AUDIT-BASELINE a) from wow-night2-obs-vis-042-f and generalising the Rig and Observatory allowances: in every overnight run, an audit warning (not failure) already present on the unchanged baseline is listed in the report and passed, its file unchanged. Failures, and new warnings a run cannot fix in its own work, still stop it. OBS-VIS-042 reruns as wow-night2-obs-vis-042-g.

## 2026-10-21 04:41 BST - Principal receipts dispositions

BRING-UP-TOOLS, BRING-UP-OBSERVATORY and WORKTREE-GUIDANCE - 21 October 2026: pending with [ki.tools-burndown](../ki.tools-burndown/messages.md) (BRING-UP-LEFTOVER, WORKTREE-FIXES) and [ki.observatory](../ki.observatory/messages.md) (BRING-UP-LEFTOVER); receipts and residual audit routing are homed in commits `0b1a0c7f` and `8a3b8c1c`.

## 2026-10-21 14:03 BST - received back, accelerate

Kris: "ok - you are ok still exclusively the thread on all this, can you accelerate getting the roadmap items progressed" and "I'm here for 10 minutes so if you have some questions I'm happy to deal with those". Taken as: this thread still controls KI exclusively; the 01:55 grant stands; put the queries that unblock agent work first.

## 2026-10-21 14:10 BST - owner answers

Kris, in speech: "Release prep: I agree with your recommendations. Rig release version: I agree with your recommendations. The control contact I really like. So yeah, we'll go with the recommendations. And agree with the defaults contract as well. ... Grant interim: we go with recommendations and the OBS Act Visual. Yes, we go with that as well. You can come back to the site source one later. And then the OPS-014 render, I agree with the recommendations for that as well. We'll have to come back to the attended big checks on Solid Terror because I can't do those right now. And the Techne 006 review is going to need me later as well. I think on the design icons we can just go with it, and then I can take a look. ... on the Gov209 owner, I agree with the recommendations. Let's come back to Gov189 scope and And gov202 adopt as well. ... GOV227-schema, I agree with the recommendation on that, which is to do a short design session in its own work. The tags point, I think, needs a lot more review ... Maybe another check into better use of tags, also, how other systems work with tags as well would be interesting on that point. And also I think we need to come back on the emerging concepts as well."

Read back as taken:

- RELEASE-PREP a): prepare tools-ki v0.13.0, pinning the pushed Harness revision; Kris tags.
- RIG-RELEASE-VERSION a): prepare tools-rig v0.8.0; Kris tags.
- CONTROL-CONTRACT a) and DEFAULTS-CONTRACT a): the coordinator has the stop, dequeue, wake and launch-defaults contract drafted for Kris's acceptance, then one run builds it.
- GRANT-INTERIM a): `--allow` ships in the tools-ki release; the interim sentence goes once it is installed.
- OBS-ACT-VISUAL a): Kris makes the live KI-OBSERVA-BRG-005 check; the record stays awaiting review until then.
- OPS-014-RENDER a): Kris runs the four client checks; the Observatory's dropped heading fragment is an accepted fallback.
- DESIGN-ICONS: proceed to independent acceptance of KI-DESIGN-ICO-001 now ("just go with it"); Kris looks at the contact sheet afterwards and any redraw comes back as new work.
- GOV209-OWNER a): ki-repo-kb-principal owns, requires and conforms the `+/_ACQUIRED/` scaffold; triage guidance in ki-repo-kb.
- GOV227-SCHEMA a): a short design session in its own work; a run prepares a draft schema for it.
- TAGS: not decided; a research run reviews better use of tags and how other systems use them, then the query returns.
- Parked, come back later: SITE-SOURCE, RIG-ATTENDED, TECHNE-006-REVIEW, GOV189-SCOPE, GOV202-ADOPT, EMERGING.
- Not yet answered: CANDIDATE-PRINCIPLES, STRUCTURE-TODOS.

## 2026-10-21 14:11 BST - mark, afternoon unattended run

Kris: "I'm hoping that can allow you to get on with some things. Maybe you can take that on board, do a mark at this point as well. I'll go away and push everything, and then you can come back with me if there's any questions you want to do, so that you can do another unattended one for the next few hours, please." Taken as: mark now; Kris pushes every repository; the 01:55 grant runs unattended for the next few hours on the answered work; questions wait for Kris's return. The decisions strike and design/ review owed at this mark go to a run (wow-day-mark-tidy).

## 2026-10-21 14:35 BST - push state out of reports

Kris: "quite often I'm getting things like unpushed or pushed or comments like that in a summary. Is that what we really want to be doing? ... generally speaking, I'm pushing things on a regular basis between the machines. So I don't think you need to keep reminding me in each of them of the common push things that I'm doing, because that's going to be based on state that's outside of the thread." Taken as: owner reports and banners stop carrying `[unpushed]`, "pushed" and other push-state notes, since push state lives outside the thread; runs still push only their own commits, never another session's. The method change to the ki-coordination standard and the coordinator output style goes to a KI Agentic Harness run after wow-day-gov-209-accept; this thread applies it from now.

## 2026-10-21 14:35 BST - CANDIDATE-PRINCIPLES and STRUCTURE-TODOS

Kris: "Both candidate principles and structure to-dos option A's, which are the recommended ones, are agreed." Read back as taken:

- CANDIDATE-PRINCIPLES a): adopt both candidates in Engineering Practice Principles as qualified decision criteria (neutrality extended without lowest-common-denominator limits; FOSS-First and Inspectable where practical); this grants no implementation or product expansion. The explicit owner instruction stands in for an Enactment record.
- STRUCTURE-TODOS a): make Port a settled section of Structure citing GDR-KI-PRINCIPAL-010; keep the Routes and Customs to-do with pointers to the Territories and Archipelagos route paragraph and `ki-trades`.

## 2026-10-21 14:35 BST - mark

Kris: "mark". Mark struck at 14:35 BST; the afternoon unattended run continues under the 01:55 grant.

## 2026-10-21 14:43 BST - release continuations and contract draft

RELEASE-CONTINUATIONS - 21 October 2026 14:43 BST: live release decisions and dossier links are in [queries](queries.md); the contract graduated to the [accepted build contract](design/agent-control-contract.md).

## 2026-10-21 14:46 BST - triple-checked approval while Kris is away

Kris: "I'll away now for the next hour. So, can you make sure that you keep tracking on with as much as you can? If you've got to a point where you think some of the things can get reviewed, matters done, and pruned off, if you want to do that and triple check them with higher level reasoning models, I'm happy to accept that as being a suitable approval." Taken as: for the next hour, where work has reached a reviewable point, three independent reviews on the strongest reasoning models, at least one under a different runtime, stand in for Kris's approval when all three agree; on that basis records may be accepted to Done and pruned, and CONTRACT-ACCEPT may be settled. Any disagreement goes to Kris. Not covered: tagging and publishing releases (Kris tags), RIG-RELEASE-REVIEW-BOUNDARY, parked queries, live applies, credentials and source deletion.

## 2026-10-21 15:16 BST - contract accepted on two fixes; KI-DESIGN-ICO-001 pruned

CONTRACT-ACCEPT - 21 October 2026 15:16 BST: the [accepted contract](design/agent-control-contract.md) carries both fixes and the [14:46 approval](#2026-10-21-1446-bst---triple-checked-approval-while-kris-is-away); completed icon prune e456873d has last revision 85a42bf1.

## 2026-10-21 15:21 BST - tools-rig green, GOV-227 draft ready

RIG-RELEASE / GOV227-SCHEMA - 21 October 2026 15:21 BST: [queries](queries.md) carries the release boundary and dossier; the [GOV-227 draft](design/gov-227-storage-schema.md) holds the five reserved owner decisions.

## 2026-10-21 15:27 BST - contract accepted, build and tags research

CONTRACT / TAGS - 21 October 2026 15:27 BST: the [accepted contract](design/agent-control-contract.md), [tags draft](design/tags-model.md) and [queries](queries.md) carry the live work; contract acceptance was committed as 03954f4c.

## 2026-10-21 17:47 BST - contract build received, coverage continuation

wow-day-contract-build preserved the first-stage draft d6df59d9 on branch `wow-day-contract-build`; every gate passes except the 100% coverage threshold, so it was not integrated. Under Kris's 01:55 grant ("I'm happy for you to just make it all work") the coordinator takes COVERAGE-GATE a) (complete coverage in the preserved worktree, rerun all gates, then integrate) and RECORD-HOME b) (the accepted contract is the first-stage authority; no roadmap association, per CAPTURE-GATE), and launches wow-day-contract-coverage. CONTROL-EVIDENCE a) and DEFAULTS-HANDOFF a) wait until the first stage is verified and independently reviewed: then separate native-evidence runs and one Harness alignment line.

## 2026-10-21 18:19 BST - first stage integrated, implementation review

CONTROL-EVIDENCE / DEFAULTS-HANDOFF - 21 October 2026 18:19 BST: delivery cb165c20 and the [accepted contract](design/agent-control-contract.md) carry the first stage; [state](state.md) carries independent review, native evidence and Harness alignment still to do.

## 2026-10-21 19:15 BST - re-review, second fix run

Re-reviews of 166f0cbc: wow-day-impl-rereview-1 and -2 changes needed, -3 accept. All seven original findings are fixed; the fix introduced new blocking defects in event publication and lock recovery (unreadable event evidence treated as absent, post-spawn publication refusal reporting a started worker as failed, leftover locks wedging a run). Under Kris's 01:55 grant, "I'm happy for you to just make it all work", wow-day-impl-fix-2 fixes them with failing-first regression tests, adds release on interrupt for both locks and bounded waiting for foreground launch and queue, and fast-forwards local main without pushing; three fresh reviewers then re-review. Publication still waits for acceptance, as taken at 19:04.

## 2026-10-21 19:21 BST - mark-strike relaunch

wow-mark-strike-2 launched with an empty brief after a coordinator script error and finished without changing the repository; the prune and strike for the 19:18 mark is relaunched as wow-mark-strike-3 with the full brief.

## 2026-10-21 19:44 BST - second fix received, re-review

wow-day-impl-fix-2 fast-forwarded tools-ki local main to 7eb0f017: every new blocking finding and advisory from the re-reviews is fixed with regression tests (38 of 43 fail before the fix), 1,823 tests pass at 100% coverage and all gates pass. Under the 01:55 grant and the 14:46 triple-check approval, three fresh blind reviewers (Codex xhigh, Opus 5.5, Fable 5.1) re-review the whole first stage; publication still waits for their acceptance.

## 2026-10-21 20:05 BST - third fix run

Three fresh re-reviews of 7eb0f017 (wow-day-impl-rereview2-1 to -3) all return changes needed; under the 01:55 grant this run fixes every blocking finding, then three fresh reviewers re-review; publication still waits for acceptance. Logged late: the ki-principal rebase blocked commits from 19:59 to 23:30.

## 2026-10-21 20:44 BST - third fix received, re-review

wow-day-impl-fix-3 fixed every blocking finding from the second re-review round at 6c498f3a (1,882 tests, 100% coverage, all gates); three fresh blind reviewers re-review; publication waits for acceptance. Logged late, as above.

## 2026-10-21 20:59 BST - fourth fix run

Re-reviews of 6c498f3a return Codex changes needed, Opus changes needed, Fable accept. Each round has found new edge cases in event evidence and held-attempt liveness, so this round fixes the findings and closes the class with systematic fault injection rather than one site at a time. Logged late, as above.

## 2026-10-21 23:27 BST - work opener button; rebase fixed

Kris, on an Observatory work package explorer with a prompt-creator button serving the ki-coordination opener templates: "Would that make sense?", then "yes" to routing it as message lines to ki.observatory (button and explorer) and ki.tools-burndown (`ki work opener <id>`, one source for the templates) once the rebase cleared. On REBASE-STALL: "want to fix the rebase then also". wow-fix-rebase completed the stopped rebase at 23:30 (one queue-line union in `+/_WORK/ki/messages.md`, all 103 commits replayed, no push); local main is 103 ahead and 6 behind origin/main, other sessions' commits.

## 2026-10-21 23:40 BST - fourth fix received, re-review

Wow-day-impl-fix-4 fixed every blocking finding and advisory from the third re-review round at 6c4d2a1a and closed the class with a fault-injection matrix (22 flows, 505 mutation points, 3,568 injected fault cells, 1,002 SIGKILL cells; 2,018 tests, 100% coverage, all gates); three fresh blind reviewers re-review; publication waits for acceptance.

## 2026-10-22 00:07 BST - mark and tidy

Kris: "mark and tidy up your work package please". The coordinator rewrites state.md for the 00:08 BST mark; wow-mark-strike-4 prunes the work folder and strikes decisions, without pushing.

## 2026-10-22 00:25 BST - fourth re-review received, fifth fix

Re-reviews of 6c4d2a1a return Codex changes needed (R4-ARCHIVE, R4-RESERVATION, R4-DISPATCH), Opus changes needed (an interrupted event append wedges a run), Fable accept with six advisories, one the same append wedge. Under the 01:55 grant and the 14:46 triple-check approval, one fifth fix run fixes every blocking finding and extends the fault matrix to the crash windows they expose, then three fresh blind reviewers re-review; publication waits for acceptance. If the fifth round still finds blocking defects, the coordinator raises convergence to Kris as a query rather than starting a sixth fix.

## 2026-10-22 01:20 BST - fifth fix: rebase onto origin/main

wow-day-impl-fix-5 stopped at integration because tools-ki origin/main gained 51725e8b ("fix(agent): home each report once and honour renamed work folders", touching events.ts, thread.ts, background-agents.md, CHANGELOG.md and agent-events.test.ts) from another session, while local main holds this work's unpublished 6c498f3a and 6c4d2a1a. Under the 01:55 grant, "I'm happy for you to just make it all work", the coordinator directs the run to finish its fixes, fetch, rebase only this work's unpublished commits and its own fix onto origin/main, keeping 51725e8b's behaviour intact and resolving conflicts in favour of both, then re-run the full suite, coverage and fault matrix on the rebased head. No push and no force-push; publication still waits for three accepting re-reviews.

## 2026-10-22 02:00 BST - mark, deep tidy, queries, overnight

Kris: "Can you take a mark and can you tidy up any old reports? Looks like there's quite a few. Just generally make the work package nice and tidy please. And then can you ask me the queries again, I'll give you answers to those. And then can you do anything else that you also need to do in preparation to be able to run unattended overnight?" Taken as TIDY-DEEP a): one tidy run deletes every report and brief whose run has finished and whose outcome is homed, listing anything in doubt; the coordinator then marks and re-asks every open and parked query.

Kris then reported `ki` failing on conflict markers in tools-ki events.ts. A `git pull --rebase` begun at 01:19 in the primary tools-ki checkout, by no run of this work, had stopped on a conflict in events.ts. With no live process and `ki` itself unable to launch a repair run, the coordinator ran `git rebase --abort`, restoring main to 6c4d2a1a; nothing was lost. The rebase onto origin/main 51725e8b stays with a follow-up run after wow-day-impl-fix-5 reports, in a worktree, as decided at 01:20.

## 2026-10-22 02:03 BST - ki-principal rebase abort

The same 01:19 `git pull --rebase` had also stopped in ki-principal, on a conflict in this work's messages.md after 41 of 111 picks, and the 02:00 entry above had been committed onto that detached state. With no live process, the coordinator ran `git rebase --abort`, restoring main, and re-appended the entry here; wow-tidy-deep had stopped before pruning and is relaunched. Integrating origin/main into local main goes to one rebase run after the tidy, as wow-fix-rebase did on 21 October; no push.

## 2026-10-22 02:07 BST - deep prune disposition

Under the 02:00 TIDY-DEEP decision, wow-tidy-deep-2 removed 85 finished reports with verified committed homes and no outstanding report queries, plus 17 obsolete briefs. The five package files, the two live briefs and all 24 design files remain; other reports are retained where query reception, complete outcome homing or live dependencies remain uncertain. No work record was accepted or deleted.

## 2026-10-22 02:11 BST - tidy, third pass

wow-tidy-deep-2 pruned 85 reports and 17 briefs but kept 283 reports, mostly because their old queries are not in queries.md. Every live query of this work is in queries.md (3 open, 7 parked); the rest were answered or superseded, with their answers in Git history of decisions.md. Under Kris's 02:00 words, "tidy up any old reports ... make the work package nice and tidy", one third pass deletes every untracked report in the work folder whose run has finished and which has a byte-identical copy in the runtime folder, keeping only reports of running runs and any report with no runtime copy, which it lists.

## 2026-10-22 02:15 BST - principal rebase without fetch

wow-principal-rebase stopped before acting: its brief asked for a fetch that its rules forbid (REBASE-FETCH-AUTHORITY). The cached origin/main 80860d92 already carries the 10 remote commits, so the coordinator answers b) in substance without widening authority: wow-principal-rebase-2 rebases onto the cached origin/main with no remote call; anything newer on the remote is picked up at the next integration.

## 2026-10-22 02:17 BST - fifth fix received, integration

wow-day-impl-fix-5 fixed all four blocking findings (R4-ARCHIVE, R4-RESERVATION, R4-DISPATCH, the event-append wedge) and Fable's advisories except PID-only liveness, at eb0e8b2e on its retained branch: 2,046 tests, 100% coverage, matrix 26 flows, 4,674 fault cells and 1,302 SIGKILL cells. It raised HISTORY-ADMISSION; the coordinator answers a), as decided at 01:20: wow-toolski-integrate rebases 6c498f3a, 6c4d2a1a and eb0e8b2e onto the cached origin/main 51725e8b in a fresh worktree, keeping both changes, re-runs the full suite, coverage and matrix, and moves local main to the result only if it still reads 6c4d2a1a. No fetch, no push. Three fresh blind re-reviews then follow; if they still find blocking defects, convergence goes to Kris.

## 2026-10-22 02:22 BST - principal rebase, third attempt

The 02:17 entry above was committed while wow-principal-rebase-2 was replaying, and its abort discarded it; it is restored here, and the coordinator makes no ki-principal commit while a rebase run is active. wow-principal-rebase-2 aborted cleanly at abcae497 on a front-matter conflict in ki.chezmoi's state.md (REBASE-STATE-METADATA). The coordinator answers it with a mechanical rule: where a work's state.md front matter conflicts, keep the whole front-matter block from the side with the later `since`, then the later `mark`; body sections keep both sides. wow-principal-rebase-3 retries under that rule, aborting on any other unresolvable conflict; no fetch, no push.

## 2026-10-22 02:21 BST - principal rebase received

wow-principal-rebase-3 rebased ki-principal's local main onto the cached origin/main under the 02:22 rule: 117 local commits preserved in order, every conflict resolved by the stated union or later-since rule, now 117 ahead and 0 behind. No push.

## 2026-10-22 02:25 BST - owner answers and release grant

Kris: "Yep, you can tag and publish whatever tools you need to do to get this up and running and especially if you've got anything with high confidence, I'm happy for you to keep going with it, right? And also with the reviews, if you get high confidence on the reviews that they meet what we expected, we can also get those things burnt down as well. I agree with what you said about tags. Site sauce is fine, really attended. What do you need me to do if it's really simple? I can just run it now and walk away. ... Technique 006 review as you recommend, narrow the Gov 189 scope as you recommend adopt gove 2 or 2. Yeah, it's interesting what we did about the emerging concepts, we don't want to lose them, so we need to put them somewhere. Obviously, the entire site needs a really good review, so maybe we can have a think about future concepts or something like that, emerging concepts, and just make it appear somewhere in the site if it makes sense. ... happy to go with what you think. Again, we can try what you think I know get as well. I'm pretty relaxed. Let's just get as much of this down and done as we can."

Read back as taken:

- Release grant: the coordinator may tag and publish tools releases needed to get the agent host running where confidence is high; this lifts the tagging and publishing exclusion of the 14:46 grant for high-confidence releases.
- Review grant: high-confidence reviews that confirm work meets what was expected stand in for acceptance and burn-down, as under 14:46.
- TOOLSKI-TAG a): tag and publish tools-ki v0.13.0 from the dossier.
- TAGS a): optional controlled `topic/*` subject tags; a 20-30-note KI Principal pilot with a retrieval comparison.
- SITE-SOURCE a): KI-WEBSITE-SITE-044 stays awaiting review until ki-design is readable, then Kris's visual checks.
- RIG-ATTENDED: Kris runs the attended checks now if simple; one run prepares the copy-paste steps, CORE-069 then CORE-068, CORE-047 and CORE-062.
- TECHNE-006-REVIEW a): KI-TOOL-TECHNE-CLI-006 released to Ready; TECHNE-006 is no longer held.
- GOV189-SCOPE a): narrow KI-HARNESS-GOV-189 to the level check and `[behind]`.
- GOV202-ADOPT a): adopt KI-HARNESS-GOV-202 to Next.
- EMERGING: adopt Fictional Lineage into Background and keep all four concepts in a findable Emerging Concepts home in the Philosophy pillar, flagged for the whole-site review to decide whether it appears on the site.
- NO-GATE a): staged, check-only `ki repo audit --skill ki-repo` as the project-shape commit gate.
- RIG-RELEASE-REVIEW-BOUNDARY: not named; asked in one line.

## 2026-10-22 02:28 BST - overnight roadmap burn-down

Kris: "The goal will be that when I come back in the morning, the roadmap is at least half what it is now. It's at 61, so I'd like it to be well under 30. Ideally speaking, I'd love to do it on single figures, right? So you can just keep pushing, chipping away, come up with what you think is at least some effort on those points and keep it working away."

Taken as: the overnight target is the territory roadmap from 61 open records to well under 30, single figures if possible, by delivering, accepting under three agreeing high-confidence reviews and pruning, or closing records that are superseded or done, under the 14:46 and 02:25 grants. One planning run inventories and batches the 61; the coordinator dispatches one writer per repository, about three at a time. No new records (CAPTURE-GATE), no live applies, credentials or source deletion; attended and Kris-only items are left listed for the morning.

## 2026-10-22 02:26 BST - triage and draft records may move forward

Kris: "Also, if you want to take things that are in tree ice or draft and move them forwards, if you get consensus from the higher order models, you can do that."

Taken as: "tree ice" is triage. A triage or draft record may be adopted, replanned to Ready and delivered when three reviewers on the strongest models (Codex xhigh, Opus 5.5 high, Fable 5.1 high) agree with high confidence; held records and the 02:25 exclusions are unchanged.

## 2026-10-22 02:26 BST - overnight, Rig attended steps to the morning

Kris: "I think you'd have to take me through the things you've got about the big steps and I can't do that now, I'm off to bed ... keep going and keep doing as much as you can do and progress it as much as you can please overnight."

Taken as: "big steps" are the Rig attended steps; they wait for the morning, walked through with Kris. Unattended work continues all night under the 02:25 and 02:28 grants and the triage-and-draft grant above.

## 2026-10-22 02:26 BST - DEPCRUISE-PATH dispatched

The IMPORTANT messages line DEPCRUISE-PATH (rename `tooling/boundaries` to `tooling/depcruise` in ki-engineering, then migrate KI repositories) goes to run wow-depcruise in a ki-agentic-harness worktree; the line is removed.

## 2026-10-22 02:41 BST - WEBSITE-GATE taken by the coordinator

wow-apps-depcruise could not commit the website's dependency-cruiser migration because DEPS-1 already fails on an overdue knip. Taken as a), confidence high, under "make it all work": a bounded maintenance pass updates knip, then commits the migration (run wow-website-maint). Not a publication; no deploy.

## 2026-10-22 02:45 BST - Rig batch received

wow-burn-rig-gate: KI-TOOL-RIG-CORE-053 and KI-TOOL-RIG-CORE-062 back at awaiting-review with fresh evidence, each still carrying an attended item (053's live owner check, 062's terra check and rollout), so not reviewable for pruning tonight; KI-TOOL-RIG-CORE-064 cancelled under SWEEP-CONVERT and its scan routed as a line to ki.chezmoi's messages.md. Coordinator takes RIG069-ROUTE a) and RIG068-GATE a), both high: CORE-069 and CORE-068 stay in draft for the morning walk-through. Three blind reviews of the CORE-064 cancellation follow.

## 2026-10-22 02:47 BST - tools-ki integration: RENAME-REPLAY

wow-toolski-integrate rebased fix-5 onto 51725e8b (tip 4cd0ab87, not admitted) and failed one renamed-folder fixture against the preserved event history; its audit preparation was incomplete. Coordinator takes RENAME-REPLAY a), confidence high: a focused fixture update, full fix-5 audit preparation and every gate, in run wow-toolski-integrate-2; then three blind reviews before admission.

## 2026-10-22 02:49 BST - reviews refused KI-OBSERVA-VIS-030 and KI-TOOL-RIG-CORE-064

KI-OBSERVA-VIS-030: two reviews refused, high (dangling references to the removed phases; ideas unhomed). The coordinator narrows KI-OBSERVA-VIS-030 to its delivered minimal chart and interaction under the 02:28 burn-down grant and "make it all work", the later consolidation phases kept as ideas, not dropped; run wow-fix-vis030 applies the reviews' fixes, then three fresh reviews.

KI-TOOL-RIG-CORE-064: two reviews refused, high: SWEEP-CONVERT names this record as its one exception, so the cancellation was wrong. Run wow-fix-rig064 restores it; the coordinator withdrew the ki.chezmoi messages line. The plan's class B for CORE-064 was mistaken.

## 2026-10-22 02:54 BST - Harness batch received

KI-HARNESS-GOV-189, KI-HARNESS-OPS-010 and KI-HARNESS-OPS-011 delivered to awaiting-review; KI-HARNESS-GOV-202 adopted to Next; KI-HARNESS-GOV-209's rollout homed. Three blind reviews follow. Coordinator takes SPEC-HOMING a) (KI-HARNESS-GOV-228 and KI-HARNESS-GOV-229 wait on SPEC-TEXT and ENTRY-NAMES) and GOV202-RENDER's recommended keep-draft course, both high. NO-GATE-OWNER: no owning record exists and CAPTURE-GATE forbids one, so Kris's 02:25 NO-GATE a) stands as a bounded owner instruction needing no record; a later harness run delivers the staged check-only gate.

## 2026-10-22 03:00 BST - Harness reviews and KI-PRINCIPAL-ECO-013

Harness reviews did not reach three agreeing high-confidence verdicts on any record; run wow-fix-harness fixes every finding and delivers NO-GATE a) under Kris's 02:25 answer, then fresh reviews. KI-PRINCIPAL-ECO-013: two reviews refuse pruning (high): the overnight grant does not plainly approve this cancellation, the ki-accept step was skipped and a link survives; it stays cancelled and unpruned, for a morning query.

## 2026-10-22 03:04 BST - VIS-030 homed, Techne CLI-006 delivered

wow-vis030-home homed the chart's later ideas in the Observatory Project note (ki-principal c88355d0) and repaired KI-OBSERVA-VIS-030's references (apps-observatory.local 8f090308). wow-burn-techne delivered KI-TOOL-TECHNE-CLI-006 offline to awaiting-review (tools-techne 41b6fd40). Three fresh blind reviews of each follow; acceptance and pruning only on three agreeing high-confidence accepts, under Kris's 14:46 grant.

## 2026-10-22 03:07 BST - ELE001-PINS taken, replan received

The coordinator took ELE001-PINS b), confidence high: read-only registry metadata, no install. wow-replan2-ele001 amended KI-DESIGN-ELE-001 with the three planning reviews' changes and verified pins (ki-design c813003), still draft. Three fresh planning reviews follow; Ready only on three agreeing high-confidence READY verdicts, under Kris's triage-and-draft grant.

## 2026-10-22 03:11 BST - KI-OBSERVA-VIS-030 second review round

Reviews: a REFUSE high (an unreadable first territory leaves the chart with no keyboard tab stop), b REFUSE high (the island-condition follow-up has no durable home; stale "not yet supplied upstream" wording), c ACCEPT high. The coordinator takes both refusals' recommended fixes, confidence high, under "make it all work": run wow-fix-vis030-2 repairs the keyboard defect with a test, homes the island-condition idea in the Observatory Project Notes and corrects the wording; then three fresh reviews.

## 2026-10-22 03:13 BST - KI-TOOL-TECHNE-CLI-006 reviews

Reviews: a REFUSE high (contradictory repository evidence can be reported clean; twelve surviving links block pruning), b ACCEPT high, c ACCEPT high. The coordinator takes the refusal's fix, confidence high, under "make it all work": run wow-fix-cli006 repairs the defect with a regression test in tools-techne; the inbound links are left for the prune run. Then three fresh reviews.

## 2026-10-22 03:15 BST - KI-DESIGN-ELE-001 third planning round

Reviews: a NOT READY high (the Project front matter names no registered Project), b NOT READY high (map text-equivalent assertion, site handoff destination, Node version invoked), c READY high with two line-level amendments. The coordinator takes every amendment, confidence high: run wow-replan3-ele001 applies them, still draft; then three fresh planning reviews.

## 2026-10-22 03:17 BST - VIS-030 fixes held on the island-wide Principal baseline

wow-fix-vis030-2 fixed the keyboard defect (regression test, every Observatory gate green) and homed the island-condition idea, but committed nothing because the full ki-principal rumdl and audit fail on 386 pre-existing findings outside its file. The coordinator takes neither option, confidence high: ki-principal's gate for a single-note edit is its own commit hooks plus note lint and a before-and-after audit showing no new finding, as wow-vis030-home used for c88355d0; the island-wide baseline is pre-existing and not this work's to clear tonight. Run wow-commit-vis030 finishes both commits on that basis.

## 2026-10-22 03:19 BST - Harness fixes received

wow-fix-harness repaired every review finding on KI-HARNESS-GOV-189, KI-HARNESS-OPS-010, KI-HARNESS-OPS-011 and KI-HARNESS-GOV-209, delivered NO-GATE a) (52a719ec) under Kris's 02:25 answer, all gates green, pushed. Three fresh blind reviews follow (wow-rev2-harness); pruning only on three agreeing high-confidence accepts.

## 2026-10-22 03:21 BST - tools-ki AUDIT-BASELINE, ELE-001 amended, CLI-006 fixed

wow-toolski-integrate-2: fixture and the full suite pass; the audit fails because the active Harness requires `tooling/depcruise` and tools-ki still uses `tooling/boundaries`. The coordinator takes b), confidence high: the tools-ki depcruise migration was already due under DEPCRUISE-PATH, so run wow-toolski-integrate-3 lands it and the fixture on the integration branch, every gate green, no admission and no push; rereview5 follows.

wow-replan3-ele001 applied every planning amendment to KI-DESIGN-ELE-001, still draft; wow-fix-cli006 fixed the contradictory-evidence defect in KI-TOOL-TECHNE-CLI-006 with regressions. Three fresh reviews of each follow.

## 2026-10-22 08:24 BST - mark; waiter lapse

The coordinator's waiter lapsed after 03:21 and was not re-armed, so nothing was received or launched between 04:02 and 08:22. Received at the mark: wow-commit-vis030 (KI-OBSERVA-VIS-030 fixes committed in apps-observatory.local a591c48d and ki-principal 2e8c6cd0; its push blocked as PRINCIPAL-RECONCILE); wow-toolski-integrate-3 (fixture b3fec501 and depcruise migration a9aba774 on the integration branch, every gate green, not admitted); wow-rev2-harness-a refused every Harness item for pruning (surviving links, unverified hosted citations, and the NO-GATE audit can contact GitHub against the offline hook contract); wow-rev2-harness-b and -c ended without reports. Kris, 08:22: "take a mark, then give me an update of whats happened since we last talked and any queries".

## 2026-10-22 08:31 BST - Harness second fix, ki-principal diagnosis

The coordinator takes the Harness review's refusals, confidence high, under "make it all work": run wow-fix-harness-2 makes the NO-GATE hook audit offline (no GitHub contact) and readies KI-HARNESS-GOV-189, KI-HARNESS-OPS-010, KI-HARNESS-OPS-011 and KI-HARNESS-GOV-209 for pruning without pruning them. Run wow-principal-diagnose reads why ki-principal is 127 ahead and 16 behind origin, read-only, before any ki-principal push.

## 2026-10-22 08:35 BST - KI-DESIGN-ELE-001 fourth planning round

Reviews: a NOT READY high (three Ready-preflight warnings; Delegation omits the supervisor's final delivery review), b READY medium (two edits for the Ready commit; preflight stops on three warnings from other ki-design records), c READY high (two line-level edits). The coordinator takes every amendment, confidence high: run wow-replan4-ele001 applies them and clears the three preflight warnings where they are bounded record fixes in ki-design, still draft; then three fresh reviews.

## 2026-10-22 08:37 BST - THREAD-FOOTER

Kris: "in the footer, I want a thread to say if is a coordination or state of play thread too ... every footer is putting out a prompt that I can copy, but I'm not sure that I ever use it, so maybe that could be replaced with effectively the thread type and its name for the work package it relates to, something like that."

Taken as: the glyph banner gains a closing thread line naming the thread type and its work, `🧵 Coordination thread · <label> (<id>)` for Project work and `🧵 State of play thread · <label> (<id>)` for territory work; the copyable send and resume lines are dropped from every banner, handoff and hold report, the thread line taking their place. The coordinator renders it from now on; run wow-thread-footer changes `ki-coordination`, the Work Process Banner section and the generated coordinator style.

## 2026-10-22 08:39 BST - KI-TOOL-TECHNE-CLI-006 accepted, prune waits

Reviews a, b and c all find the delivery meets KI-TOOL-TECHNE-CLI-006 with high confidence; a refuses pruning only because 18 to 21 ki-principal links would be orphaned. Under Kris's 14:46 grant the three agreeing reviews stand in for acceptance: run wow-accept-cli006 records it accepted in tools-techne. The link repair and prune wait for the ki-principal reconciliation.

## 2026-10-22 08:42 BST - PRINCIPAL-RECONCILE: isolated integration first

wow-principal-diagnose: ki-principal is 127 ahead (123 this work's, four ki.chezmoi's) and 52 behind origin; a rebase conflicts on six work-package paths; nothing is mid-operation. The coordinator takes an isolated, non-publishing step, confidence high: run wow-principal-integrate rebases the range onto origin/main in a separate clone, resolves each conflict preserving both sides, revalidates and reports; the primary checkout and origin stay untouched. Publishing the combined history, which carries ki.chezmoi's commits, goes to Kris as a query afterwards.

## 2026-10-22 08:47 BST - ki-principal integration prepared

wow-principal-integrate rebased all 127 local commits onto origin/main 07df4b3e in a separate clone (branch `integrated`, tip 2d010c86): every commit is kept one-to-one, and the conflicts in six work-package files were resolved by keeping both sides in time order. The primary checkout is untouched. Publishing it carries ki.chezmoi's four commits, so it goes to one blind review and then to Kris as PRINCIPAL-PUBLISH.

## 2026-10-22 08:54 BST - KI-DESIGN-ELE-001 fifth planning round

Reviews: a READY high, b NOT READY high (the Decision Record deliverable conflicts with the `ki-decision-records` standard, and Verify has no check for it), c READY high (only the record's own Draft-stage sentences remain). No consensus, so no Ready move. The coordinator takes b's amendments, confidence high: run wow-replan5-ele001 reconciles the Decision Record deliverable with `ki-decision-records`, adds a Verify check for it and folds in c's line edits, still draft; then three fresh reviews.

## 2026-10-22 09:00 BST - Harness third review round

Reviews a, b and c all accept KI-HARNESS-GOV-189, KI-HARNESS-OPS-010 and KI-HARNESS-OPS-011 with high confidence, and confirm KI-HARNESS-GOV-209's earlier acceptance. Pruning is not agreed: a and c refuse every prune on surviving links; b would prune only KI-HARNESS-OPS-010 and KI-HARNESS-OPS-011. NO-GATE: a and b accept; c refuses, confidence medium, because the offline audit passes the directory basename as the repository identity and FILES-2 fails spuriously when `.ki.toml` is staged in a hosted repository. Under Kris's 14:46 grant the three agreeing reviews stand in for acceptance: run wow-accept-harness-3 records the three accepted, fixes the NO-GATE repository identity, and prunes nothing. Link repair and pruning wait for the ki-principal reconciliation.

## 2026-10-22 09:08 BST - ki-principal integration unsafe; ancestry-preserving repair

wow-rev-principal-integrate: UNSAFE, confidence high. All 127 commits replay one-to-one, but the conflict unions restore three messages this work had consumed (CLI-156-POLICY, AUDIT-OUTSIDE-LANE, DEPCRUISE-PATH), combine ki.chezmoi's successive state snapshots as simultaneous instructions, and leave out the primary's later commit 4a54e691. The coordinator takes its safe sequence, confidence high: run wow-principal-repair merges origin and the primary's current tip into a repair branch in the integration clone, preserving original ancestry so both can fast-forward; keeps consumed messages removed; resolves ki.chezmoi's state to its newest coherent snapshot and tells ki.chezmoi by a line in its `messages.md`; verifies; publishes nothing. The coordinator commits nothing more in ki-principal until publication, so the primary tip stays fixed. Publication then goes to blind review and to Kris as PRINCIPAL-PUBLISH.

## 2026-10-22 09:12 BST - Harness accepted; KI-DESIGN-ELE-001 sixth round

wow-accept-harness-3: KI-HARNESS-GOV-189, KI-HARNESS-OPS-010 and KI-HARNESS-OPS-011 are done (03d41563); NO-GATE now takes the hosted identity from the configured origin, offline (408f9992); every gate green; nothing pruned.

KI-DESIGN-ELE-001 sixth round: a READY high; b NOT READY high (`playwright-core` pinned at 1.56.1, far behind local Chrome 155, and the plan forbids repinning, so browser setup is likely to block); c NOT READY medium (guide scope under `ki-guides`, and the Decision Record date on amendment). The coordinator takes both, confidence high: run wow-replan6-ele001 applies them, still draft; then three fresh reviews.

## 2026-10-22 09:17 BST - ki-principal repair: finish against live origin

wow-principal-repair took P 573faa53, removed the three consumed messages, set ki.chezmoi's state to its newest snapshot, told ki.chezmoi, and merged P with ancestry kept (833dd21f); audits add no finding. It stopped at the stability gate: the coordinator's own decisions-log appends and four deleted briefs changed the primary during the run, and origin moved 14 commits to 868c6721. The coordinator commits its log now and takes the completion run, confidence high: wow-principal-repair-2 recaptures the primary tip, merges live origin keeping newly arrived messages and the latest coherent ki.chezmoi state, and reruns every check; appends to this decisions log and changes under this work's `briefs/` during the run are the coordinator's own and do not fail stability. Publication still goes to blind review and Kris.

## 2026-10-22 09:20 BST - tools-ki integration fifth review round

Reviews of 51725e8b..a9aba774: a REFUSE high (an older failed event without terminal metadata is replayed as an ending during upgrade, consuming a later completion and suppressing its event and report homing; strict test fences also keep the full gate from going green); b REFUSE high (a9aba774 moves the checker to `tooling/depcruise`, which CI's pinned released Harness does not yet accept, so the pushed audit would go red; admission over the two superseded local commits is not a fast-forward); c ACCEPT high. The coordinator takes both refusals, confidence high: run wow-toolski-fix-6 fixes the legacy replay defect with regressions, and orders the branch so the range up to the fix can be admitted with CI green while a9aba774 waits for a tools-ki release whose Harness pin accepts `tooling/depcruise`; then three fresh reviews.

## 2026-10-22 09:24 BST - ki-principal completion: widen the stability allowance

wow-principal-repair-2 merged the primary tip f2778b86 (bce02d0e) and fetched origin 868c6721, then stopped on stability: run reports homed into this work folder as new untracked files. The origin merge conflicts in ki.agent-host's `messages.md` and ki.chezmoi's `state.md` (origin now has ki.chezmoi on hold since 07:51). Untracked files cannot alter the merge and the collision check already covers them, so the coordinator takes the run's option a), confidence high: wow-principal-repair-3 resumes from bce02d0e with stability meaning `main` still at P and tracked changes only appended to this decisions log, any untracked file allowed if the final collision check passes; it resolves both conflicts to the latest coherent state, keeping unconsumed queue lines, and reruns every check.

## 2026-10-22 09:27 BST - KI-DESIGN-ELE-001 seventh round

a READY high, c READY high with no edit; b NOT READY high: the no-go branch cannot be reached inside the spike, and the GDR-KI-DESIGN-012 amendment scope omits content its own Verify check forbids. The coordinator takes b's two amendments, confidence high: run wow-replan7-ele001 applies them, still draft; then three fresh reviews.

## 2026-10-22 09:31 BST - KI-DESIGN-ELE-001 seventh amendment received

wow-replan7-ele001 applied review b's substitutions only (d345ecd0); the Ready preflight passes and the audit adds no finding. Limitation: its first full audit ran without `KI_REPO_OFFLINE=1` and made read-only GitHub calls against the no-network bound; it reran offline. Three fresh reviews follow; review briefs now name `KI_REPO_OFFLINE=1` for any audit.

## 2026-10-22 09:32 BST - ki-principal candidate ready for review

wow-principal-repair-3 produced F 7eb98927 on `repair-wow-principal` in the integration clone: live origin and primary P f2778b86 are both ancestors, all 127 originals kept, consumed messages stay removed, ki.agent-host's queue and ki.chezmoi's state resolved, no added audit finding, no collision. Publication carries ki.chezmoi's commits, so run wow-rev-principal-final gives one blind Codex review before PRINCIPAL-PUBLISH reaches Kris.

## 2026-10-22 09:40 BST - KI-DESIGN-ELE-001 eighth round

a READY high; b NOT READY high (outcome classification contradicts itself; the go path and guide edits could settle a Proposed decision without approval); c NOT READY medium (Steps omit the Playwright setup check and repin window that Dependencies requires before the matrix; Step 7 builds `verify-browser.mjs` only after the matrix runs). The coordinator takes all of them, confidence high, and asks for a whole-record consistency pass so the next round converges: run wow-replan8-ele001, still draft; then three fresh reviews.

## 2026-10-22 09:43 BST - ki-principal final review: restore queue lines

wow-rev-principal-final: UNSAFE, confidence high. History, audit and the dirty-primary update path pass, but pending lines in ki.observatory's and ki.tools-burndown's `messages.md` were replaced by summaries rather than kept as their unconsumed source lines. The coordinator takes its QUEUE-LINES repair, confidence high: run wow-principal-repair-4 restores every unconsumed original line verbatim on `repair-wow-principal`, rechecks every queue the same way, and reruns all checks; then one fresh blind review.

## 2026-10-22 09:55 BST - ki-principal candidate repaired

wow-principal-repair-4 restored 17 pending queue lines verbatim and the territory queue's source order; F is now 3a6b7bf8, every check passing. Run wow-rev-principal-final-2 gives one fresh blind Codex review before PRINCIPAL-PUBLISH reaches Kris.

## 2026-10-22 09:58 BST - KI-DESIGN-ELE-001 ninth round

a READY high; b NOT READY high (a classification gap and an unhandled blocked outcome; a go edit settles the route; worktree site gates cannot run offline); c NOT READY medium (site gates unrunnable under the permitted worktree arrangement; the "evidence note" is never defined; the go edit to GDR-KI-DESIGN-012 can be read as adopting an unapproved route). b and c now converge on the same defects, so the coordinator takes one more amendment, confidence high: run wow-replan9-ele001 applies both. If the tenth round still lacks three high READYs, the record goes to Kris as a query rather than another round.

## 2026-10-22 10:06 BST - ki-principal: correct three inherited decision inversions

wow-rev-principal-final-2: UNSAFE, confidence high, on one gate only: three decision blocks inherited from the source histories are out of time order. Ancestry, retention, queues, state, conflict markers, offline audit and checkout preservation all pass, and it names the exact primary update. The coordinator takes its option a), confidence high, since reordering keeps every word: run wow-principal-repair-5 moves the three blocks into time order on `repair-wow-principal`, reruns the checks, and one fresh blind review follows before PRINCIPAL-PUBLISH reaches Kris.

## 2026-10-22 10:16 BST - ki-principal candidate reordered

wow-principal-repair-5 moved the three inherited blocks into time order with every byte kept; F is now 13e94479, P f2778b86 and origin 868c6721 are ancestors, and every check passes, including time order in all four touched decision logs. Because F's Ways of working decisions log now differs from P's committed copy while the primary carries my uncommitted appends, the earlier direct fast-forward command no longer stands as proved. Run wow-rev-principal-final-3 gives one fresh blind Codex review, which must also prove an exact primary update that keeps those appends, before PRINCIPAL-PUBLISH reaches Kris.

## 2026-10-22 10:22 BST - KI-DESIGN-ELE-001 tenth round goes to Kris

a READY high; b NOT READY high (a VM diagnostic result has no place in the outcome classes; nobody is named to finish a completed run after the supervisor's review, nor to complete the six-part Review packet; the site tsbuildinfo is called tracked but is gitignored); c NOT READY high (the boundaries test is called a known failure but passes; the same tsbuildinfo fact). Every required edit is given as exact text. Under the 09:58 decision this goes to Kris as ELE001-CONVERGE rather than another round; the coordinator's recommendation is medium, so run wow-qrev-ele001-converge gives it one blind review first.

## 2026-10-22 10:27 BST - ELE001-CONVERGE reviewed

wow-qrev-ele001-converge, blind: course b (park as draft), confidence high. It verified b's and c's factual fixes but found b's exact handoff text conflicts with the Boundary's review-before-cleanup order, its Files touched insertion breaks a sentence, b and c replace the same phrase differently, and the last amendment grew rather than shrank, so the reviews are not converging. The coordinator's medium recommendation for one last exact-text amendment is withdrawn on that evidence; ELE001-CONVERGE goes to Kris recommending parking, with the amendment as the alternative.

## 2026-10-22 10:33 BST - primary stability breach corrected

The coordinator's ELE001-CONVERGE edit to `queries.md` broke the primary stability the ki-principal review relies on, and wow-rev-principal-final-3 stopped its guarded trial before publication. The edit is reverted, its 12 added lines held outside the repository in `/Users/krisbrown/.local/state/ki/agents/ways-of-working/ele001-converge.query.md` until publication; until then the coordinator touches nothing in the primary but appended decisions. A fresh review follows if final-3 ends unsafe on this alone.

## 2026-10-22 10:36 BST - ki-principal: settle the remaining candidate faults

wow-rev-principal-final-3: UNSAFE, confidence high. Ancestry, history conservation, hygiene, offline audit and collisions pass, and its guarded update script succeeded end-to-end on a scratch copy. It fails on: 17 origin blocks of the Ways of working decisions log missing from F (15 headings, two bodies); four pending queue lines in ki.observatory's and ki.tools-burndown's queues still reformatted (APP044-STALE, BRG004-NEAR, explicit-outcomes, OPS009-SPLIT); ki.chezmoi's state front matter off the state schema though byte-identical to its owner's latest commit; and the coordinator's own primary edit, now reverted. The coordinator's mark at 08:24 struck decisions, so some missing blocks may be deliberate strikes rather than loss. Run wow-principal-repair-6 classifies each of the 17 against P's history, restores any not deliberately struck, restores the four queue lines verbatim, and leaves ki.chezmoi's state to its owner as pre-existing, with a line in its queue; then one fresh blind review.

## 2026-10-22 10:39 BST - tools-ki sixth review round

wow-toolski-fix-6 fixed review a's F1 (legacy failures classified before terminal ownership is trusted) with regressions that upgrade untouched 51725e8b state, and reordered the range 51725e8b..219968a0 so the depcruise migration 219968a0 comes last after fix a7c80cd8. Full suite 2,078 tests at 100% coverage, TypeScript, Biome, build, and offline audits at both the candidate Harness and CI's pinned v0.12.0 all pass. Its staged plan: admit through a7c80cd8 by a guarded compare-and-swap from 6c4d2a1a, hold the migration, release a KI version pinning a Harness revision with db5e3cff, then admit the migration with the CI pin bump. Runs wow-rereview6-toolski-a/b/c give three fresh blind reviews of admission through a7c80cd8 and of that plan.

## 2026-10-22 10:51 BST - ki-principal candidate settled

wow-principal-repair-6: F is now 7200dd9b. All 17 origin decision differences are the work's own mark outcomes (15 strikes, two pointer rewrites) and none was lost through the merge, so nothing is restored; the four pending queue lines are restored verbatim; ki.chezmoi's state is left byte-identical to its owner with a line in its queue. Seven works' state files, ki.chezmoi's among them, carry closed-schema faults identical to their owners' commits; those are their owners' to fix, not this candidate's. Run wow-rev-principal-final-4 gives one fresh blind Codex review, judging only faults the candidate introduces, before PRINCIPAL-PUBLISH reaches Kris.

## 2026-10-22 11:09 BST - ki-principal: fix two queue envelopes

wow-rev-principal-final-4: UNSAFE, confidence high, on one check only: the two lines this reconciliation added to ki.chezmoi's `messages.md` (lines 3 and 4) fail RECORD-2's message-envelope schema. Ancestry, retention, decisions, state, hygiene, audit, primary safety and the rehearsed update all pass. Run wow-principal-repair-7 rewrites those two lines to the envelope schema, keeping their meaning, reruns every check, and one fresh blind review follows.

## 2026-10-22 11:14 BST - ki-principal: the primary is a live shared checkout

wow-principal-repair-7 stopped before editing: ki.baseline-rollout's session has since edited nine tracked report files in the primary, so the review's exact primary baseline no longer holds. The coordinator answers its PRINCIPAL-BASELINE query itself, confidence high: the primary is shared and will keep moving, so the candidate repair must not be gated on it. Run wow-principal-repair-8 fixes the two envelope lines and reruns the candidate checks; for the primary it reports only whether any current tracked edit or untracked path overlaps a path F changes from P. The live update is guarded at the moment of publication, in a writer window Kris approves.

## 2026-10-22 11:22 BST - ki-principal candidate envelopes fixed

wow-principal-repair-8: F is now 32f3efb2; the two ki.chezmoi queue lines meet the envelope schema with their words, senders and sending times kept, no other added line needed change, and candidate checks 1 to 7 pass. Run wow-rev-principal-final-5 gives one fresh blind Codex review, treating the primary as a live shared checkout, before PRINCIPAL-PUBLISH reaches Kris.

## 2026-10-22 11:32 BST - owner request, MGIT-LEARN-SHAPE

Kris: "on the `mgit learn`, how do we deal with params that might change... e.g. `mgit ci -am "<msg>"` so learn needs to think about the command structure, i.e. 1. expand the alias, which is just `ci` -> `commit` in this case (note that `st` is `status -sb`) 2. state which params are considered in the match, e.g. -a is optional/ignored, -m is the key one to make this a match, but its value, i.e. `"<msg>"` is ignored ... that will need dispatching or roadmap item creating". tools-mgit has no roadmap record or work package for this, so this explicit instruction lifts the capture gate for it: run wow-mgit-learn-shape, in tools-mgit, finds how `mgit learn` matches commands today and captures one draft roadmap record there for command-shape matching, without implementing it.

## 2026-10-22 11:38 BST - ki-principal candidate safe; PRINCIPAL-PUBLISH to Kris

wow-rev-principal-final-5: SAFE, confidence high. F 32f3efb2 keeps both source histories and every pending instruction and adds no fault; its guarded update command, rehearsed on scratch copies, discovers the primary's state at run time, refuses any overlap before pushing, and preserves staged, unstaged and untracked files. The only overlap now is this log's own uncommitted appends. PRINCIPAL-PUBLISH goes to Kris, recommending: set these appends aside, a push run executes the reviewed command, then the appends go back on F's log and are committed. The blind review this publication query requires is final-5 itself. ELE001-CONVERGE stays held outside the repository until then.

## 2026-10-22 11:41 BST - MGIT-LEARN-SHAPE captured

wow-mgit-learn-shape captured KI-TOOL-MGIT-CLI-031 (learn command shapes) in tools-mgit as a draft, size m, with Kris's words quoted and six open design questions; all gates pass, no implementation. Today `learn` keys on every expanded argument, flag spelling, order and value, with no shape declaration or short-flag splitting.

## 2026-10-22 11:57 BST - tools-ki seventh fix

Sixth round so far: a REFUSE high (launcher-like failure text is still taken as terminal without corroboration, so legacy replay can lose a completion; release.yml's packaging jobs check out the tag without the history the new upgrade tests need); c ACCEPT medium (two non-blocking legacy-classifier gaps to fix before release); b still running past an hour, its progress reporting that an upgrade refuses whole runs after a failed-then-relaunched worker. The coordinator takes a's findings and c's gaps, confidence high, without waiting further for b: run wow-toolski-fix-7 fixes them, checks b's reported case, keeps the migration last, and folds in b's report if it lands meanwhile; then three fresh reviews.

## 2026-10-22 12:25 BST - tools-ki sixth round complete

b REFUSE high: the new legacy-failure classifier permanently refuses `status` and `wait` for ordinary old runs (a worker `failed:` progress line followed by any later status, or a legacy `could not launch:` failure), and the release workflow's shallow checkout breaks the baseline-upgrade tests. Both are already in wow-toolski-fix-7's brief, which takes b's report as it lands; no new run.

## 2026-10-22 13:12 BST - tools-ki seventh fix received; seventh review round

wow-toolski-fix-7 resolved every sixth-round finding in two new commits, `22e0ea9c` and `3a3407e0`, with the migration rebased last as `d4849813`; every gate passes and it raised no queries. The admission tip is now `3a3407e0`, with the migration held back until a KI release carries the new depcruise rule. Three fresh blind reviews (a, b, c) of `51725e8b..3a3407e0` follow; admission is a guarded compare-and-swap from `6c4d2a1a` only if all three accept.

## 2026-10-22 14:06 BST - tools-ki seventh round refused; eighth fix

a REFUSE high: legacy replay and checkpoint recovery remain unsafe (concurrent checkpoint replacement loses interrupted append evidence) and the offline audit is red. c REFUSE high: the tip permanently refuses ordinary crashed legacy runs, including this work's live run, which every earlier version reads. b still running. wow-toolski-fix-8 launched under "make it all work" (01:55), told to step back to the simplest design that reads every run `51725e8b` reads and to prove it against a copy of real agent state; it takes b's findings as they land.

## 2026-10-22 14:12 BST - AUDIT-BOUNDARY settled by the coordinator; fix-8 relaunched

wow-toolski-fix-8 stopped before patching, asking which audit contract gates the pre-migration tip. Settled within "make it all work" (01:55) as b: the CI-pinned contract (KI `v0.12.0`, Harness `f4d6c521`) gates the admission tip, as CI on tools-ki `main` runs it; the migration tree is audited under the current Harness. The reviewers' red audit was the current Harness's `tooling/depcruise` rule, which only the held migration satisfies. Review b REFUSE also folded in (crashed legacy runs; pre-event seeded terminal snapshots). Relaunched as wow-toolski-fix-8b with the amended brief.

## 2026-10-22 14:27 BST - tools-ki seventh round complete

b REFUSE high: `22e0ea9c` turns a worker that exited without DONE into a permanent refusal, blocking a copy of this work's live run, and the offline audit fails on `3a3407e0` without `d4849813`. All three refuse; wow-toolski-fix-8b already carries all three reports and the settled audit boundary.

## 2026-10-22 16:17 BST - tools-ki eighth fix received; eighth review round

wow-toolski-fix-8b fixed every seventh-round finding; admission tip `0fd85a08`, migration held as `f4ce77b8`. `51725e8b`, `0fd85a08` and `f4ce77b8` each read 17/17 copied real runs; all gates pass, admission audit under the CI-pinned contract and migration audit under the current Harness. Containment exception: its early comparator wrote fourteen untracked report copies into ki-principal and acquire; it proved them its own by hash and creation time, moved only those to quarantine, and left tracked and pre-existing files alone. Three fresh blind reviews (a, b, c) of `51725e8b..0fd85a08` follow, which also confirm containment read-only.

## 2026-10-22 17:22 BST - tools-ki eighth round complete; receiver provenance first

Eighth round on `51725e8b..0fd85a08`: b ACCEPT medium (no blocking finding; a mixed-version refusal after a checkpoint-unaware append, judged non-genuine but not blocking); c ACCEPT high (every gate passes, 28 regressions fail before and pass after, 17/17 real runs read); a REFUSE high, on containment alone: about 850-870 untracked report copies across ki-principal work folders, three in acquire and nine tracked `ki.baseline-rollout` reports changed at 11:09 BST, all byte-identical to runtime reports, with no proven source. c and b date the copies across the day and read them as report homing; c also asks that the swap wait for a quiet point in the live dispatcher, which runs the tools-ki primary's source. Admission stays held. The coordinator launched wow-provenance-receivers, read-only, to establish what wrote them and propose a disposition per group; no receiver file is touched without Kris's word.

## 2026-10-22 17:47 BST - receiver copies traced to verification; disposition to Kris

wow-provenance-receivers (high): the stray reports were written by verification, not by the candidate. Comparison runs during the tools-ki fixes copied agent state but kept absolute report homes, so old builds homed reports into the real receivers: 391 untracked copies (119 ki.chezmoi copies at 10:55, 269 ki-principal and three acquire copies at 11:09), and the archived primary `6c4d2a1a` overwrote nine tracked `ki.baseline-rollout` reports at 11:09:46. `0fd85a08` overwrites none. The 485 other untracked reports in this work's folder are ordinary homing. The blind review wow-rev-receivers agreed on every finding but narrowed the removal: three copies (burnrig, acceptgit, mgit-prune) are linked from retained runtime reports and stay. Deleting other works' files and restoring tracked ones goes to Kris as RECEIVER-COPIES and BASELINE-REPORTS; tools-ki admission stays held until the clean-up and a fresh containment check.

## 2026-10-22 22:50 BST - mark; tidy every working area and commit across the territory

Kris: "Can you take a mark at this point and can you go over the work folder? I think you can delete the work review one for example and then also just tidy up the inbound and outbound working areas in general. But for example, I can see a diagram/slash change management skills that probably needs to be tidied up, all of the work packages under the plus slash underscore work needs tidying up. So just get as much tidy as you can. You don't need to check with me, you just need to make it happen on those ones and get everything fully committed across all of the knowledge islands repos and then we'll have a look at what's outstanding?"

Taken as: a mark now; delete `+/_WORK_REVIEW`; tidy `+` and `-`, including `+/diagrams/change-management-skills`; prune every work package under `+/_WORK`, which answers RECEIVER-COPIES a) (remove the 388 verification copies, keeping the three linked ones, after fresh checks) and BASELINE-REPORTS a) (restore the nine `ki.baseline-rollout` reports from Git); commit everything across the Knowledge Islands repositories by explicit path, without asking first. Commit, not push. It lifts the coordinator's own hold on ki-principal tracked files, so the integration candidate `32f3efb2` will need refreshing before PRINCIPAL-PUBLISH. Two runs: wow-tidy-principal (ki-principal and the three acquire copies) and wow-commit-territory (every other Knowledge Islands repository), in parallel.
