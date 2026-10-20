# Decisions

## 2026-10-14 - thread-model owner words

Kris's words from the two thread-model design notes, kept here when the notes were deleted on 20 October; the behaviour they set is homed in the `ki-coordination` and `ki-delegation` standards, and GDR-KI-PRINCIPAL-009 superseded the thread model.

- Banner request, relayed by the Master on 14 October: "every coordination-thread summary or owner report ends with a multi-line status banner modelled on the ki-recap banner. The banner states plainly whether the thread is AT REST (all work concluded, nothing in progress, no open queries) or not, and why. The banner carries one copyable resume line Kris can paste back into the thread later".
- Scope, 14 October: the Master gives this work "the whole thread-working model - how coordination threads work, their skills, hooks, the banner, re-bootstrap and inter-thread messaging".
- THREAD-TERMS, Kris's question of 14 October: "What is the terminology that we're using? Is it a thread, a session, or a chat? I think a thread is the right word at this moment in time ... I think we've got three kinds of threads. I think we've got normal threads, we've got coordination threads, and then we've got state of play threads, which effectively are coordination threads of coordination threads ... I think we should formally define the type of thread that we've got. Normal threads could be something like conversational threads as well."
- Durable decisions, the same question: "We still need to get to the bottom of what we do about decisions and then being durable knowledge ... This also includes these so-called design folders and what we do with those as they are under a project currently in streams/projects/<project-id>/design."
- BANNER-LETTERS, Kris at the Master on 14 October: "a conversational thread can be considered done. That's the end of the conversation. But a coordination thread can either be busy or at rest. Whether or not it then ends up being done is more a situation about the project itself, and in effect, it's when we say that project's closed and pull out and tidy up all of the stuff that's been happening."
- BANNER-MARK, Kris at the Master on 14 October: "BANNER-MARK: confirmed. The resume line is the equivalent of a compaction for the checkpoint and coordination thread, and may also trigger a real compaction."
- Cross-session visibility, Kris at the Master on 14 October: "Kris sees no Zed rendering of cross-session messages: the threads appear idle, or show x (failed) since the outage, although their backends replied. The messaging interface goes to ways-of-working."
- Handoffs, Kris's rule: a handoff "counts as done only when Kris expressly says so".
- DESIGN-RETENTION, before the answer (a): "DESIGN-RETENTION - I guess if this is truly a working area, it should be stored in the `+` working area under some kind of design heading in terms of then the durability of it later on."

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

## 2026-10-19 18:19 BST - owner note, LOCAL-MODE

Kris: "btw, both machines are in local mode so if they pull they have the latest tools"

Read back taken: Terra and Sol run the tools from their checkouts, so a pull gives them the current `ki` and harness; no per-machine install step is needed there.

## 2026-10-19 - CAPTURE-GATE

Kris took CAPTURE-GATE a) on 19 October: "runs never create records; the owning work's coordinator captures only a blocker, a defect seen failing or a Kris request; ideas go to Project notes; small audit fixes need no record". Homed in `ki-delegation`'s background-run standard and `ki-next`; a standing rule on every brief, with no roadmap cap.

## 2026-10-19 22:17 BST - lesson, half-done harness checkout

link1-baseline: a run editing the harness checkout breaks every island's pre-commit audit while its edit is half-done (22:12 to 22:14 BST, 19 October). Not yet in [Mistakes and Lessons](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Operations/Mistakes and Lessons.md>); harness edits run in worktrees since.

## 2026-10-19 23:22 BST - owner direction, PUSH-NOT-WITH-YOU

Kris: "By the way, I'm sick and tired of having with me saying pushing stuff, right? That's not an issue. Can we get that removed? Why'd you need to put that against me? I can just push it. Also this is on hold, but it says on hold pushed to agentic harness. You're not on hold on if you're waiting on something."

Read back taken: a push of stacked commits is never a "with you" item or query; it shows only as `[unpushed]`, naming other sessions' commits once in Done. With HOLD-CLEAN, homed in the `ki-coordination` standard and output style (harness `f4d6c521`) and the Work Process note (`be2e6ec6`).

## 2026-10-20 03:34 BST - owner answers, HANDOFF-AS-MESSAGE, NET-DOWN and WIP-CAP

- HANDOFF-AS-MESSAGE, Kris: "Handoffs are not roadmap items ... A rollout that needs people to make those changes sooner rather than later must go as a message ... we push the need to roll things out into other projects triage folders, and that's not what this is for." Taken as: rollouts and handoffs go as `messages.md` lines, never records; only genuinely deferred work the receiver owns may be a record. Homed in the standards (harness `76b6e5c5`) and the choreography sections of ki-principal, KI Specifications, the Techne Harness and tools-techne.
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

## 2026-10-20 - acceptance grant

Kris, 20 October, granting overnight acceptance: "if you can quickly now accept ... accepting new things that are waiting with you and pruning those ... getting the roadmaps down to zero". Quoted in every overnight acceptance brief; each acceptance was by an independent reviewer that did not deliver the work.

## 2026-10-20 09:27 BST - send to owner

The overnight burndown is drained, and the mark is struck at 09:27 BST. Nineteen queries go to Kris; the six medium or low ones were blind-reviewed by Codex. Other sessions' commits keep ki-principal, the harness, specifications, Observatory and others unpushed, and the pending prunes wait on those pushes.

## 2026-10-20 22:03 BST - self-serve burndown

Kris: "Is there anything more that you can do by yourself without me? To try and get that vote back down before I re-open lots of other threads? ... roadmap down"

Taken as: "vote" read as "load". Carry the overnight burndown on with only what needs nothing from Kris: independently reviewed acceptances of records already awaiting review (KI-HARNESS-GOV-219, KI-HARNESS-GOV-224) under the 20 October acceptance grant, the ECO-013 audit recheck, this work's design-note graduation, and a read-only sweep of every remaining roadmap for records workable without Kris, delivered on its findings. The 19 queries stay with Kris; other sessions' stacked commits stay unpushed.
