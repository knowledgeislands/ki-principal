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
