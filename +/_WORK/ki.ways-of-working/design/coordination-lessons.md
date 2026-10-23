---
title: The smallest changes from the 22 October coordination lessons
status: draft - October 2026
purpose: Compare the routed lessons with the current method and propose only the missing sentences
author: Written with Codex
---

# The smallest changes from the 22 October coordination lessons

Proposal for [Ways of working](../../../../Streams/Projects/ways-of-working.md), 23 October 2026. Kris's standing steer, 22 October 23:22: "be careful that we are not over engineering at all times too". This note changes no method and sends no messages.

Keep the current skills, seven states, five-file package and Git message queue. Most lessons need either no change or a short clarification in an existing section. Project addressability needs a bounded exception to package creation rights; reliable unattended waking would need tooling, so it is a separate choice rather than a prerequisite for the prose changes.

## Evidence and citation key

Line citations below refer to these local files as read on 23 October, not to a vendor's current product claims:

- **S:** [Scheduling debrief](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/hnr/design/scheduling-debrief.md>), including the observed failures, proposed remedies and four unverified standing rules.
- **M:** [Coordination model notes](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/hnr/design/coordination-model-notes.md>), including the agreed Project-addressable change and the DRAIN prompt.
- **H:** [HNR decisions](</Users/krisbrown/workspaces/humans-not-robots/hnr-principal/+/_WORK/hnr/decisions.md>), lines 35-48, alongside the five routed messages supplied in this brief. The full COORD-HANDOFF-ASKS wording comes from the brief; H:40 now holds its homing pointer.
- **W:** [Work Process](<../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>), last local change `554bcd8e`.
- **C:** [ki-coordination standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md>), read with its skill entry point.
- **D:** [ki-delegation background-run standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-background-runs.md>), read with its skill entry point. The brief's change-management path is stale; the canonical skill lives under governance.
- **K:** [ki-work-package standard](</Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md>). Latest local commit across C, D and K: `0809ff80`.
- **A:** [Acquire instructions](</Users/krisbrown/workspaces/personal/acquire/AGENTS.md>) and its [intake work definition](</Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/work.md>).

The debrief's vendor comparisons are explicitly inferred (S:5, 63); no network verification was authorised here. Its observed usage-limit and permission stalls support the method lessons without treating those comparisons as verified implementation advice.

## Lessons and smallest changes

### Work, sessions and routing

1. **Lesson:** "When I'm saying thread, I'm actually mean work packages, right? So threads are just the things that operate on work packages".

**Coverage:** Already covered by W:17 and W:126-129: work outlives the session, with its definition and state in the package. M:16-25 also asks for short-lived sessions and distinguishes a conversation from packaged work. **Smallest change:** none to the model; add one operating sentence at C's Picking work up: "Prefer a fresh session once the package contains everything needed to resume." No session-age limit or new session machinery.

2. **Lesson:** Regular work needs a clear role: "what kind of thread type a regular work one is, as well whether it's coordination or not."

**Coverage:** W:48 says regular work is self-coordinating and needs no coordination thread; C:426 and C:432 separate bounded conversational work from coordinator-only machinery. A:27 explicitly makes capture conversational, without background runs, routine banners or heartbeat; A:29 makes the package owner-selected. **Smallest change:** none; send the reply below through the coordinator. A regular id or optional work package does not silently appoint a coordinator.

3. **Lesson:** A Project coordinator is a council member; State of play is the territory council's chair; a conversational session has neither role (M:31-35).

**Coverage:** The operational relationship already exists at W:64-68 and C:697: roles are relative to each handoff, and State of play coordinates coordinators. **Smallest change:** one explanatory sentence at W's Roles using the council metaphor, without adding role fields, authority or a third level of supervision. More machinery would add no useful behaviour.

4. **Lesson:** Work for another package should appear "in the summaries at the bottom about asking if it can send work to another thread".

**Coverage:** C:692 and C:768-771 define the destination and sending contract; C:490 already gives queries their Context / Query / Options form. They do not require this prior ask. **Smallest change:** add at C's Handoffs and rollouts: "Put a proposed transfer of work at the bottom of the Summary's Queries, naming the receiving work package and asking permission before sending, unless Kris has already authorised that transfer." Existing authorised routes, replies and refreshes need no repeated permission. This adds one approval point, expressly requested by Kris, rather than a new routing mechanism.

5. **Lesson:** "I'm wondering if we should have a ways of working skill which covers all of this. And maybe it's an expansion of the K I-coordination skill".

**Coverage:** C:60 already owns coordinator behaviour; D:43-45 owns the run side; W:15 owns the model. **Smallest change:** expand the existing coordination standard with the missing availability and wake sentences, linking delegation's existing authority rules. A new umbrella skill or rename adds routing and duplicate guidance without changing behaviour; it is not worth it.

6. **Lesson:** Make a Project addressable on first arrival of work, initially On hold until Kris opens it: "agreed, this is what I was working on too" (M:26).

**Coverage:** Not yet covered. C:691 says a dormant Project needs no folder, C:705 gives seeding to State of play, and K:91 permits another work only its message line. The cap already excludes On hold work (C:703). **Smallest change:** replace the dormant-folder sentence and extend Seeding: the sender or the territory's State of play may create an absent, registered Project's package solely to queue its first message, within the receiving repository's authority. Create all five files, with minimal definition, empty queries and decisions, and `on-hold`, reason `paused`, release "when Kris opens this Project work"; preserve W:160 and W:222 rather than inventing a three-file package or an automatically releasing hold. Add the same narrow creation exception at K's Entry points and a pointer at W's Routing. This changes write rights and deserves explicit wording, but needs no new tool or cap.

7. **Lesson:** Generate the active-work-packages view from package state rather than maintain another list (M:27).

**Coverage:** Already covered by C:701 and C:711 and W:279: `ki work status` derives the register and state views. **Smallest change:** use that existing surface, including On hold packages when finding message destinations. No second register, dashboard or generator is warranted; this review does not certify the implementation's completeness.

### Draining and responsive work

8. **Lesson:** DRAIN shut work down "really nicely": finish near-complete runs, stop the rest safely, preserve the package and park queries (M:39-60).

**Coverage:** Already covered by W:99 and C:878-890, including the roughly 15-minute finish allowance, safe stopping, mark and parked queries. **Smallest change:** at C's Putting work on hold, add "Read IMPORTANT messages first, cancel every wake held by this session, and report whether anything remains running, queued or scheduled." Reuse the current hold procedure; no separate DRAIN lifecycle, new skill or copy of the old prompt. Routing during a drain still follows the transfer authority in lesson 4, and publication follows current authority rather than the historical prompt's wording.

9. **Lesson:** Give "a very clear demarcation at the end so that I know it's all done" (M:60; H:48).

**Coverage:** C:891-892 distinguish a completed hold from inability to drain, but C:320 and C:891 require the thread line last. M:52-55 instead puts DRAINED / NOT DRAINED last. **Smallest change:** choose one placement explicitly. Recommend a narrow exception at C's hold-report paragraph: only an explicitly requested DRAIN check adds its truthful DRAINED / NOT DRAINED result after the thread line. Ordinary holds keep their current ending. This is one presentation exception, not another report form; Kris's choice is below.

10. **Lesson:** A single permission prompt can silence an idle-only wake, even when bypass mode was selected (S:11, 57-58).

**Coverage:** C:182, C:184 and C:188 already require short calls and delegate substantive work, but do not explicitly exclude a prompt-blocking call. **Smallest change:** add at Coordinator responsiveness: "Never issue a coordinator command that may wait for a permission prompt; put deletion and housekeeping in a bounded run or the existing close operation, and report a denied action instead of waiting unattended." This does not authorise bypassing a permission gate. The cause of the historical bypass prompt remains unestablished; investigating that belongs in runtime guidance, not a new coordination rule.

11. **Lesson:** Timed updates must use the real clock; the debrief observed stale clock labels (S:36).

**Coverage:** C:190 requires timestamps but does not name their source. **Smallest change:** append to Cadence: "Take each timed update's local time from the clock in that turn, never from recalled labels." No timer or timestamp field is needed.

12. **Lesson:** Do authorised work without making Kris approve it again (S:171, 175-186).

**Coverage:** Already substantially covered by C:688, D:45 and C:770: approvals precede their authorised work, and existing authority becomes next steps. **Smallest change:** one clarification at C's Decisions: "A logged, unrevoked owner decision authorises its stated scope across sessions; ask again only for a new decision, an explicit later gate or a changed boundary." It neither converts a relay into approval nor overrides a repository's narrower gate. Do not edit multiple AGENTS files merely to duplicate it; any genuinely conflicting local gate needs its owner's bounded resolution.

13. **Lesson:** Deferral for agent capacity is not a handoff requiring Kris (S:172, 187).

**Coverage:** W:84-89 and C:489 already distinguish worker-held work, supervisor handoff and outstanding matters needing no owner action. **Smallest change:** append at C's States and moves: "Authorised work waiting for worker capacity stays with the worker; send to the supervisor only for an actual decision or review." No new state or queue.

### Availability, wakes and delivery

14. **Lesson:** Unattended work needs a bounded away grant, not an assumption that silence means permission (S:90-100).

**Coverage:** C:191 already records the agreed OOS-WAKE autonomy-window watcher, and D:146 says grants are not implied. Neither supplies the proposed availability contract. **Smallest change:** one short paragraph at C's Coordinator responsiveness: record the explicitly granted end time, work, permitted actions, exclusions, wake and stop words in the existing decisions log; park decisions outside that scope; stop starting unattended work at expiry, explicit return or "stop the wake", then report. An ordinary steering message does not automatically cancel a window. Add one pointer beside W:101: availability changes neither the seven states nor authority. No Present / Away / Returning state fields, grant asset or standing global deny-list is needed.

15. **Lesson:** A schedule must be visible, have an end and have plain stop words (S:128-143).

**Coverage:** C:191 governs the worker heartbeat, and C:772 explicitly adds no wake where none is armed; neither defines a separately requested schedule. **Smallest change:** one paragraph beside Heartbeat requiring an explicit request or away grant, and a `[scheduled]` banner item naming the mechanism, observed next firing, session-only or durable lifetime, expiry and "stop the wake". Stop it at the window boundary or drain. This is a banner item, not an eighth work state; generated coordinator surfaces must follow the canonical change in the same later delivery.

16. **Lesson:** An on-time trigger is not successful coordination; session-only and idle-only waking failed overnight (S:11-15).

**Coverage:** C:191 already recognises the out-of-session gap and the owner-approved OOS-WAKE watcher; D:193 connects that watcher to completion events. **Smallest change:** state there that a session wake is best effort and cannot promise an unattended service. Use the existing watcher direction for run completion first. A launchd shell pre-check plus headless coordinator could cover closed sessions and message-only arrivals, but adds a scheduler binding, liveness, locking, authority and cancellation work. It is worth building only if Kris requires that wider unattended service; do not introduce it merely to tidy the method. Its implementation belongs to tools-ki and Rig, after a routing ask, and this note neither establishes that the watcher has shipped nor installs anything.

17. **Lesson:** Usage limits can consume the whole window even when every wake fires (S:26, 59).

**Coverage:** C:191's heartbeat and autonomy window do not describe usage-limit failure. **Smallest change:** add to the availability paragraph: "An unattended window promises only the authorised attempt; report usage-limit stops, missed processing and failed runs on return, and never mark a trigger as processed work." Reuse existing status and reports. A shell pre-check is a sensible economy if durable waking is chosen, not a reason to build it now or to add a new budget subsystem.

18. **Lesson:** The sender needs to distinguish a line sent from work received and dealt with (S:115, 122).

**Coverage:** C:769 already requires a recorded disposition and a removal commit naming the line; C:714 shows unread count and age. **Smallest change:** clarify in Receiver that the named disposition/removal commit is the receipt and is not necessarily completion of the requested work. A retained line can point to its open query. Do not add `inbox_read_at`: a read timestamp would not establish disposition, would extend K's state schema and would duplicate weaker evidence.

19. **Lesson:** The queue lacks an immediate doorbell and a guarantee that the receiver is still waking (S:108, 116, 121-123).

**Coverage:** C:772 covers pickup on an armed wake and explicitly leaves non-waking work to State of play's unread-age view. **Smallest change:** retain that honest limit and surface urgent unread work through C:714. Doorbell files, a ring command, `last_wake` stamps and twice-the-period checks add delivery infrastructure; they are not worth adding independently of a chosen durable-wake service. If that service is approved, assess its existing signals before adding any of them. No extra acknowledgement message or liveness field now.

### Rules whose authority needs checking

20. **Lesson:** "No DNS, Access, route, Builds or Zero Trust change without Kris's go" was treated as standing, without a standing source found (S:164).

**Coverage:** D:146 requires explicit remote authority for runs; it does not prove this broader standing instruction for every session. **Smallest change:** retain the actual per-action limits; if Kris confirms a broader rule, home it once in the cross-project personal guidance and link the owning infrastructure guidance. Do not infer a new universal ban from the debrief.

21. **Lesson:** "No mcporter or chezmoi config change without approval" was overstated beyond the written run and source-store boundaries (S:165).

**Coverage:** D's authority tiers and Grants already bound run environment changes; the principal's AGENTS source-store rule governs its particular apply. **Smallest change:** none unless Kris confirms a broader personal rule. Put a confirmed cross-project rule in the chezmoi-managed personal guidance, rather than duplicating it in coordination and delegation.

22. **Lesson:** "Drafts only in Linear, Notion and Slack" had no written source found (S:166).

**Coverage:** The reviewed method does not establish that standing provider policy. **Smallest change:** keep the existing task-specific authority; if Kris confirms the rule, home it in cross-project personal guidance with pointers to the applicable integration guidance. No draft-enforcement tool or new permission layer.

23. **Lesson:** A confidential site's privacy restriction needs its own durable owner (S:167).

**Coverage:** The debrief found an item-specific restriction, not a general rule; no claim is made here to have inspected private site content. **Smallest change:** the owning repository should retain any confirmed confidentiality rule in its AGENTS or existing access policy. Do not identify the site in a public method, spread the rule to unrelated repositories or invent a privacy guard.

## REGULAR-WORK-ROLE: reply for Acquire intake

Regular work is self-coordinating, so its id or work package does not make a session a coordinator; coordination is an explicitly opened role for territory or Project work. Acquire intake remains the conversational, receipt-first work defined in its work.md and AGENTS.md: do bounded intake directly, preserve receipts and route material, without coordinator banners, heartbeat or background-run ceremony. Keep its existing package for continuity where selected, use ordinary replies and the applicable completion report, and propose Project work only if a request outgrows those bounds.

This is ready for the Ways-of-working coordinator to send to Acquire intake's messages.md; this run is authorised to write only this design note.

## Queries for Kris

### METHOD-HOME - Extend the existing skill

**Context:** The model, coordinator behaviour and run authority already have distinct homes. The missing behaviour fits short additions to those homes; a new Ways of working skill would mostly repeat their routing.

**Query:** Should the follow-up keep ki-coordination as the existing home and make only the prose changes described here?

**Options:**

a) (recommended, confidence high - the existing ownership already fits) Extend ki-coordination, make the small linked Work Process and package-entry changes, and create no umbrella skill or new fields.

b) Design a separate Ways of working skill before changing the method.

### AWAY-GRANT - Explicit unattended windows

**Context:** The overnight failures showed that a wake does not guarantee processing. Existing authority and the agreed OOS-WAKE window offer a base, without inventing availability states or a grant template.

**Query:** Should unattended work require a spoken, bounded window with an end, scope, exclusions and stop words recorded in decisions.md?

**Options:**

a) (recommended, confidence high - it makes the boundary explicit without extra machinery) Require an explicit window, preserve all existing action limits, stop unattended starts at expiry or explicit return, and report missed processing on return.

b) Keep unattended availability entirely as per-task instructions, without a common window paragraph.

### WAKE-SUBSTRATE - Decide how much reliability is needed

**Context:** The existing method already points to an OOS-WAKE watcher for finished runs. That does not cover message-only arrivals or guarantee overnight processing; a durable Rig wake with a shell pre-check and headless pass would add a wider service and its operational obligations.

**Query:** Is the existing completion-watcher direction enough for the next step, or must we design durable unattended pickup of messages too?

**Options:**

a) (recommended, confidence medium - smallest scope, but it leaves message-only unattended pickup unguaranteed) Pursue the already-agreed watcher direction first, label session wakes best effort, and defer launchd, doorbells and extra liveness fields.

b) Ask permission in the next Summary to route a bounded tools-ki and Rig design for durable message and completion pickup, with a shell pre-check, cancellation, authority and failure reporting agreed before implementation.

### DRAIN-END - Keep the clear final demarcation

**Context:** The successful DRAIN prompt puts DRAINED / NOT DRAINED last, while the current standard requires the thread line last. Most of draining is already specified; only that ending and wake cancellation are missing.

**Query:** Should an explicitly requested DRAIN check have the final-line exception?

**Options:**

a) (recommended, confidence medium - honours the requested visible ending with one narrow exception) Put the truthful DRAINED / NOT DRAINED result after the thread line only for an explicit DRAIN check; keep the ordinary hold report unchanged.

b) Keep the thread line last in every case and put the explicit drain result in Done.

### UNWRITTEN-RULES - Confirm only actual standing instructions

**Context:** The debrief found no standing source for the broad infrastructure-go-ahead rule, general mcporter/chezmoi approval, drafts-only provider policy or generalised confidentiality claim. Existing task and repository restrictions still apply.

**Query:** Are any of those four claims intended as standing instructions beyond their existing local scope?

**Options:**

a) (recommended, confidence high - avoids turning inferred practice into owner policy) Leave them unadopted as global claims; name any that should be standing, and have the owning work home only those confirmed words in the appropriate personal or repository guidance.

b) Confirm all four as standing instructions and ask their owning works to propose the exact wording and homes.
