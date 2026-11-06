---
work: ki.prj.agora
run: ki-prj-agora
agent: consolidate
written_at: 2026-11-06T03:19:49Z
---

# KI > Techne > Agora › consolidate › alignment

Where what Kris has said or decided, and what Agora has been told, pull against each other. Gathered on 6 November 2026 at about 03:20 GMT; it decides nothing. Each conflict quotes its sources with dates, says why they conflict, and says what would resolve it. Item numbers (B1 to B31) refer to [agora-backlog.md](agora-backlog.md). Times are GMT.

**Note on quotations.** Kris's words are quoted as the logs record them. Q30's answer (C2) is recorded in personal.reg.inbox-sol's decisions as taken, "asked in plain English", not word for word.

## The five that shape everything else

C2, C3, C5, C15 and C20 decide what most other items mean. C2 and C3 together decide whether the whole `jobs` focus stays with Agora.

## Conflicts

### C1 · The Techne focus against Agora running work

- **Techne Programme Focus** (policy, updated 19 October): agents run on sol and vega "only in sessions the binding owner opens, with no unattended or scheduled agents"; every other piece of Techné work "is kept as an idea ... not as a work record"; each host's "Claude login [is] the binding owner's own identit[y] ... a machine identity is decided only when unattended agents are taken up".
- **FOCUS-FIT a** (Kris about 00:30, 6 November): Agora may wake sessions and runs Kris opened; anything that starts a fresh agent on its own, scheduled or not, on any Mac, waits for an Enactment decision.
- **AGORA-SCHEDULER** (Kris 01:50, 4 November, and MSG-9556f9a6, 00:12, 6 November): Agora runs the rig's scheduled jobs; five of the thirteen first jobs in KI-AGORA-WRK-004 start an agent, Route Triage among them.
- **CSWAP-AGORA** (Kris 08:00, 4 November): one decider switches accounts; KI-AGORA-WRK-002's candidate rules include "hold `robots` back for unattended work".
- **The Agora Project note** (3 November): "Agora lives in neither [Techne repository], and runs on the Mac Studio within its bounds", while the Project sits under theme Techne.
- **Why they conflict:** the job whose silent failure started AGORA-SCHEDULER, Route Triage, is an agent job that runs unattended on terra today under launchd; under FOCUS-FIT a, Agora can never take it over, while launchd keeps running it outside any focus rule. The focus names only sol and vega, yet FOCUS-FIT a extends it to terra for Agora alone. A `robots` account for unattended work presumes the unattended agents the focus rules out on sol, and may be the "machine identity" the policy defers. If the focus binds Agora as Techné work, records for work beyond the two hosts (terra, the group) would strictly be `Idea:` lines, not records. Keep-awake (KI-AGORA-WRK-003) itself starts nothing and does not conflict.
- **What would resolve it:** Kris says whether the Techne focus binds `apps-agora.local` at all (or whether Agora belongs under another theme), and whether agent jobs stay with launchd outside Agora until an Enactment decision.

### C2 · Scheduled jobs: Agora runs them, or each session watches its own

- **AGORA-SCHEDULER** (Kris 01:50, 4 November): "maybe it's the agora that should be scheduling the jobs. It should be effectively the thing that sits there running for us." MSG-9556f9a6 (Kris 00:12, 6 November): "Agora runs the scheduled jobs Rig declares on its host ... and reports any failure or missed run the same day; ... tools-rig adds an Agora engine in place of launchd." Captured as KI-AGORA-WRK-004.
- **Q30** (Kris about 02:12, 6 November, in inbox-sol's spec): "a job on a timer is watched by its own session, which sets the timer, shows its next run, reads what it found and flags a missed run, and nothing central is added".
- **AGORA-FOCUS** (Kris about 02:15, 6 November): "keep agora really focused on what it is ... only meant to send messages to other sessions".
- **Why they conflict:** two hours apart, the same question got opposite answers in two different packages: a central engine in Agora, or nothing central at all. KI-AGORA-WRK-004's own scope also has Agora take over "listening and checkout refresh outside threads" and the housekeeping due check, both central. SCHED-REPORT a (ring the owning package) fits either answer.
- **What would resolve it:** Kris chooses: Agora as the engine (KI-AGORA-WRK-004 stands), each owning session watching its job with Rig and launchd as the engine (KI-AGORA-WRK-004 shrinks to reporting, or is cancelled), or a split (Agora reports missed and failed runs; sessions own their jobs). tools-rig's engine request (MSG-14f2a17c) follows the answer.

### C3 · What Agora is: the focused messenger, or the manager of the rig

- **AGORA-FOCUS** (Kris about 02:15, 6 November): "Agora is not meant to be a chat client ... It's only meant to send messages to other sessions running in other ways or help promote intercommunication. It's a place for coming together and talking. It's not a replacement ever for Orca ... keep agora really focused on what it is ... Maybe it's time to have a specification for that."
- **Spec part 4** (Kris 22:10 and 22:12, 4 November): Agora gets messages into "a heterogeneous environment of different tools", and "does not host or own sessions itself".
- **On the other side:** COORDINATION-MODEL-PLAYBACK (Kris 09:40, 4 November): "Agora as the manager"; spec goal 6: "Agora as the manager on each rig and a proper app as its face, so new capability has somewhere to attach"; AGORA-OWNS-STATE (Kris about 01:20, 3 November): Agoras "understanding fully [the] state [of] all things that [are] running"; `AGENTS.md` and the Project outcome: run-once jobs, floating doers, waking workers through `ki agent`; and the asks since: scheduled jobs, account switching, keep-awake, host settings, a settings screen, the KIV send side, a voice path.
- **Why they conflict:** each ask since 4 November adds a duty that is not messaging (running programs, switching accounts, holding power, checking host settings), while Kris's latest word narrows Agora to messages and togetherness. "Manager on each rig" and "only meant to send messages" cannot both set the boundary.
- **What would resolve it:** the specification Kris asked for (B26): one page saying what Agora is and is not, then each of B14 to B19, B5, B20 and B25 kept, moved (to Rig, the housekeepers, the KIV or the Observatory) or dropped against it; `AGENTS.md`, the Project outcome and `work.md` then follow.

### C4 · "Agora never ..." against the new duties

- **`AGENTS.md`** (current): Agora never writes to Git beyond fetch and a clean fast-forward; never types into anything but the one thread a watched package names, and only the fixed wake line; never edits knowledge; "installs nothing"; "`ki agent` stays the only way Agora starts or steers a run"; messages "are only signals: a lost or refused message costs latency, never state".
- **KI-AGORA-LVL-001** (KEEP-AWAKE, Kris 23:50, 5 November): "where agreed keeps" the host's settings, which changes host configuration that Rig and the housekeepers own; the record itself says the "Agora never" list does not allow it.
- **KI-AGORA-WRK-004:** Agora runs each job's own program; Route Triage commits without pushing; the territory dispatcher starts agents "through each Activity's own wrapper", not through `ki agent`.
- **KI-AGORA-WRK-002:** one decider on one Mac runs `cswap switch` "on each Mac over Agora's peer link", so a peer message changes state on receipt.
- **Run-once claims** (AGORA-RUN-ONCE option a, host-agent design): "a claim and lease committed in Git"; Kris's own answer put the register in chezmoi, where "Git settles races" by someone's commit.
- **ORCA-WATCH a:** outbound GitHub API calls, new for an app that otherwise talks only to its peers and local tools.
- **Why they conflict:** each needs Agora to change state outside Git's fast-forward (host settings, accounts, programs that commit, claims), or to start agents another way than `ki agent`.
- **What would resolve it:** per duty, either an `AGENTS.md` amendment Kris approves, or the duty stays with its current owner (Rig applies settings; chezmoi's housekeepers commit register moves, as the jobs plan has it; jobs keep their wrappers under launchd). C3's answer settles most of these at once.

### C5 · Who owns the footer and the listening words

- **FOOTER-AGORA** (Kris about 23:40, 3 November, via household-terra): "every decision about what the report footer shows is now Agora's ... liaise with ki.sop.main". The standard at `3ffd23bc` says the same.
- **LISTEN-HOW** (Kris 01:25, 4 November), forwarded by ki.sop.main as "footer content being yours under FOOTER-AGORA".
- **FOOTER-RADIATOR** (Kris 09:45, 4 November): the footer is "the information radiator that I need when I'm interacting", and its home is unclear; inbox-sol's spec Q7 (open) and its send-out list ("the footer's rules in one place" to ki.sop.main and ki.prj.agora).
- **COORD-SOLE and TOPIC-HOMES** (Kris via ATER-010 and ATER-009, 00:16, 5 November): "coordination and communication" go to personal.reg.inbox-sol.
- **`work.md`** (this package): "Out: ... coordination method and message words (ki.prj.ways-of-working)", a fourth claimant.
- **The words themselves differ:** the standard's mode line is `👂 listening` or `🔇 not listening`; LISTEN-HOW proposes `🎧 listening · Agora's call`, `· polling <interval>`, `· on open`, `🎧 not listening`, with register values `agora-call`, `poll`, `on-open`, `off`.
- **Why they conflict:** the footer is a communication radiator, so TOPIC-HOMES gives it to inbox-sol, while FOOTER-AGORA, written a day earlier and repeated in the standard, gives it to Agora; ki.sop.main keeps the standard either way.
- **What would resolve it:** Kris names one owner for the footer's rules (inbox-sol's spec, written into the standard by ki.sop.main), with Agora owning only which facts it supplies; FOOTER-AGORA is then amended in the standard and `work.md`'s Out line corrected.

### C6 · Doorbell or Agora's call

- **AGORA-CALL** (Kris about 01:20, 4 November): "an [agora] doesn't have a [doorbell]"; Kris chose **Call**. LISTEN-HOW (01:45): "'Agora's call' is the name". Spec part 1 defines "Agora's call ... (renamed from 'doorbell', 4 November)".
- **What still says doorbell:** Agora's code (11 source files), README, `AGENTS.md`, the view schema, the state path `~/.local/state/ki/agora/doorbell/`, this package's `state.md`, KI-AGORA-WRK-004 and SCHED-REPORT ("ring the doorbell").
- **The standard** (`3ffd23bc`, Heartbeat): "doorbells and extra liveness fields stay deferred" (WAKE-SUBSTRATE, 26 October), though Agora's doorbell has woken sessions since 3 November.
- **Q26** (Kris 01:56, 6 November): "Agora posting its call to a Claude session's inbox", so "call" now names a delivery as well as a file.
- **Why they conflict:** the agreed name is used in the spec and in speech; the built thing and the standard use the old word or call it deferred.
- **What would resolve it:** the rename slice (B2) with a transition; ki.sop.main removing "doorbells ... stay deferred" from the standard; one sentence saying "call" means Agora telling a session something arrived, by whatever route.

### C7 · Listening: Agora's call, the session's own watcher, and State of play acting for idle work

- **AGORA-OWNS-STATE** (Kris about 01:20, 3 November): "super important [to] no longer have [to] rely on agents themselves dealing [with] this"; the README: sessions "wait on a local doorbell file rather than running their own fetch loop".
- **The standard's inbox watch** (`3ffd23bc`): the session's own loop "every couple of minutes ... fetches and fast-forwards local `main` silently"; a session listens only when Kris expressly asks.
- **SOP-ACTS-FOR-IDLE** (Kris, raised 15:50 5 November, landed `3ffd23bc`): State of play acts for a package only while its `listening_status` is not `on`.
- **This package:** `listening_status: on` since 4 November, yet six inbound lines from 4 November wait two days unacted; Claude Code's own watch dies at two hours (PROCESS-FINDINGS), so "on" can go stale unseen.
- **Q21** (proposed, Kris about 18:20, 4 November: "listen right and nothing by accident"): a session counts as listening only when its `state.md`, its rig's Agora watch and its answers agree.
- **Why they conflict:** the standard still describes the session's own fetch loop that Agora replaced; and a package that says it listens but does not gets neither its own session nor State of play acting for it.
- **What would resolve it:** ki.sop.main updates the inbox watch to "wait on Agora's call where the rig runs Agora"; Q21 agreed, with Agora's ping or roll call as the third check; `listening_status` set `off` when a session's watch lapses.

### C8 · Run-once jobs: the register, the scheduler and the claims

- **AGORA-RUN-ONCE** (Kris 01:15, 3 November): "we keep [a] list [of] all scheduled jobs and [the] hosts ... some ... must uniquely run, or singleton ... we just put it into dot files [as the] coordination point". Household-sol's jobs register plan: chezmoi holds it, a housekeeper moves a job after Kris decides, Agora "raises; it never moves a job itself"; Kris deferred JOBS-HOME ("why have we decided on the word jobs and not workers?"), JOBS-GUARD and JOBS-HOSTS, and left JOBS-MOVER open (3 November, about 09:05).
- **KI-AGORA-WRK-001:** run-once claims with Route Triage as pilot, Agora handing a claim over after a lease (the host-agent design's option a).
- **KI-AGORA-WRK-004 and SCHED-ONE-RIG a:** keep Rig's host selection now, claims later.
- **KI-AGORA-WRK-002:** one decider on one host, overlapping the claims.
- **Q30** (C2): nothing central.
- **This package's** `work.md` scope names "the run-once jobs register with personal.reg.household-sol (AGORA-JOBS)" as in scope, and `state.md` next step 9 says household-sol "keeps the housekeeping register".
- **Why they conflict:** four places describe who decides where a job runs, with different movers (Kris and a housekeeper, Agora by lease, Rig's profiles) and one answer saying nothing central at all.
- **What would resolve it:** after C2, one model: the register (chezmoi, housekeepers) says where; Rig says how; Agora reads and reports; claims by lease only if Kris later chooses JOBS-MOVER c. KI-AGORA-WRK-001's claims part is then kept or dropped.

### C9 · Who owns Agora's settings file

- **AGORA-RIG-GO** (Kris about 09:00, 3 November: "Yes, land it"): chezmoi renders `~/.config/agora/config.toml` from `rigs.yaml`; the README: "Rig is to render this file from the rig list". The jobs plan adds `[jobs]` and `rigProfile` keys to the same render.
- **Kris's settings-screen ideas** (about 09:10, 3 November): a permissions check, a OneDrive-like switchable tree of territories and repositories, an assignments view; AGORA-TERRITORIES: "It should be configurable by each host".
- **Why they conflict:** if both write the file, chezmoi undoes the screen's changes at its next apply.
- **What would resolve it:** CONFIG-OWNER (open; recommended a: chezmoi writes first-run defaults, then the app owns the file).

### C10 · MARK-LATE: the sending time against the standard's mark

- **MARK-LATE b** (Kris about 00:30, 6 November): a session acting on a late mark takes the broadcast's sending time as its mark, "so every thread's mark lines up".
- **The standard** (`3ffd23bc`, The mark): the mark is "struck by the owner at a moment of their choosing"; "only the owner moves the mark, by saying `mark` or `mark only`"; at the mark the session strikes decisions, prunes and commits.
- **mark-all-scope's draft line for the standard** (4 November): "strikes when it acts ... skips it when its own mark is later".
- **Why they conflict:** b fits "the owner's moment" but leaves three gaps: the tidy happens hours after the timestamp it is dated to, so the next Summary repeats what happened between sending and acting; a session Kris marked directly after the broadcast would move its mark backwards unless a "skip if later" rule survives; and the only drafted standard line says the opposite of b. The standard also knows only spoken marks, not a broadcast.
- **What would resolve it:** a redrafted line for ki.sop.main: a `mark` broadcast is the owner saying "mark" at its sending time; a session whose own mark is later skips it; the Summary runs to the time it acts.

### C11 · MARK-HOLD: striking against the hold rules

- **MARK-HOLD b** (Kris about 00:30, 6 November): a session on hold strikes the mark and gives its hold report.
- **The standard:** "On hold nothing is armed", so a held session hears nothing until reopened; a hold report is given when entering a hold; SOP-ACTS-FOR-IDLE: State of play acting for a package changes none of its "mark, hold or decisions", and "an On hold package stays on hold". ki.sop.main's hold-states design (HOLD-IDLE, HOLD-LISTEN, HOLD-FOOTER) is still with Kris and would split "on hold" into "waiting for work" and "paused until".
- **Agora's Orca wake** types its line into any watched session's terminal between turns; it does not read hold.
- **mark-all-scope's draft line:** "a thread on hold acknowledges without striking", the opposite of b.
- **Why they conflict:** b needs a held session to act, which the hold rules prevent; State of play cannot act for it; and Agora could wake a held session that the standard says has nothing armed.
- **What would resolve it:** a standard line that a held session strikes at its next opening, dated per C10; Agora not waking a package whose `state.md` says On hold (reading only); revisit after the hold-states decision.

### C12 · Electron against GPUI, and the window that would trip the watch

- **SHELL-WATCH** (Kris about 23:00, 5 November): "keep a close eye on GPUI in the future and say that we can consider moving away from Electron at any point"; a trigger is "the settings screen or a KIV/Agora window grow[ing] into a large always-open view", and each time window work is planned "a run checks GPUI's current state online first".
- **The Electron side:** host-agent design (Kris 22:35, 2 November): "this needs [to] be [an] Electron app"; MORNING-FEEDBACK: the KIV becomes an Electron app; spec part 6: "an actual proper Electron app".
- **Spec Q8** (open): is the app Agora itself, with an "IDE mode" window that opens the KIV?
- **Why they conflict:** not head-on, but Q8's yes would fire SHELL-WATCH's trigger and also cut against AGORA-FOCUS ("not ... a chat client") and `AGENTS.md` ("Agora never views the estate"). Every background run's rules also forbid network calls, so the online GPUI check SHELL-WATCH requires can only run under a task that grants web reads; gpui-fit could not make it.
- **What would resolve it:** answer Q8 inside the Agora, KIV and Observatory design (C19); grant web reads explicitly in any brief that plans window work.

### C13 · Names: thread or session, host or rig, workers or jobs, housekeeping

- **Session:** spec Q1 (Kris 09:55, 4 November): "session" replaces "thread". Agora's README and `AGENTS.md`, this package, its records and the standard still say "thread".
- **Host:** HOST-WORD (Kris about 02:45, 6 November): "no rig and host mean the machine that the session is on", reversing Q31; the Agent Host Protocol's "host" (the app that owns sessions: Orca, T3 Code, Claude Desktop) still needs a word of ours, while AHP-FIRST makes that protocol central. The Project note calls Agora "the host agent".
- **Jobs or workers:** JOBS-HOME (Kris, 3 November): "why have we decided on the word jobs and not workers?"; the spec defines a worker as a session attached to a package; `AGENTS.md` says "floating doers"; KI-AGORA-WRK-004 is titled "scheduled jobs".
- **Housekeeping:** the housekeeper rename is agreed (household-sol); AGORA-HANDOFF asks whether a rig's timed tasks are "housekeeping activities", while "housekeeping" also names chezmoi's `docs/housekeeping/` templates and the housekeepers' `housekeeping⏰` focus.
- **Why they conflict:** the same word means different things in Agora, the spec and AHP, and Agora is about to build on AHP.
- **What would resolve it:** inbox-sol's spec part 8 naming, sent to ki.sop.main and Agora together; Agora renames in one slice with B2.

### C14 · Renamed ids still in use

- **INBOX-RENAME** (Kris, 6 November): `krisb/assistant` is `krisb/inbox`; `personal.reg.assistant-*` became `personal.reg.inbox-*`; KIV-HOME a (6 November) folded `personal.reg.inbox-terra.kiv` into personal.reg.inbox-sol's `kiv` focus. MESSAGE-IDS retired `ASOL-nnn`, `ATER-nnn` and `HTERRA-nnn`.
- **Still using old names:** Agora's README (watch, call and broadcast examples use `personal.reg.assistant-sol` and `krisb/assistant`), its examples and test fixtures; KI-AGORA-TRY-001 ("`personal.reg.assistant-sol`, which owns Agora's design and build"); this package's `state.md` (next steps 4 and 6) and `work.md` (Out: "assistant-terra.kiv"); WAKE-ARCHITECTURE ("Reply to assistant-sol"); household-sol's two plans (`personal/assistant/.../async/host-agent.md`, a path that no longer exists).
- **Why it matters:** the KIV send side's waiting consumer is now personal.reg.inbox-sol, not assistant-terra.kiv; old links point at paths that moved.
- **What would resolve it:** B28 for Agora's repository; the package trim in [consolidate.package.md](consolidate.package.md); household-sol for its plans.

### C15 · Two packages may answer Legal

- **LEGAL-AUTOMATION-AGORA-20261104** (lgl.sop.main, 4 November): Kris authorised "the Sol assistant, or Agora as fallback"; "take ownership or coordinate ownership with that assistant; do not run duplicate competing fixes"; reply with the owner and the verified limits.
- **WAKE-NOTE a** (this package, raised 6 November): Agora writes the wake note and answers Legal.
- **Inbox-sol's spec:** "Legal's wake request ... Receipted; answered by this spec"; the send-out list has "The answer to Legal's wake request" going from inbox-sol to lgl.sop.main; Q13 asks whether to withdraw WAKE-ARCHITECTURE from Agora; its index still lists WAKE-ARCHITECTURE as "Awaiting ACK", which Agora never sent.
- **Why they conflict:** exactly the duplicate Legal asked to avoid: both packages hold the request and each plans to answer.
- **What would resolve it:** Kris answers WAKE-NOTE and Q13 as one question; the other package then ACKs and drops its line. Legal is On hold (LGL-HOLD, 4 November), so the answer waits in its messages.

### C16 · Posting to Orca

- **AGORA-WAKE c** (Kris about 03:25, 3 November): "ask Orca upstream for chat send (run `orca-chat-send`, public issue authorised by this answer)".
- **NO-EXTERNAL-POSTING** (Kris about 19:40, 5 November): "Any posting to external repositories in my name, such as the one that's done to Orca issue 33114, is not allowed without my express permission." Q28 (01:59, 6 November): no further comment.
- **ORCA-UPSTREAM** (Kris about 21:15, 5 November): the post "was really important".
- **Why they conflict:** the 3 November answer was read as permission; the 5 November rule says that post needed express permission; the same evening Kris called it important. Settled for the future by the rule; the history is mixed.
- **What would resolve it:** nothing further; any later post goes to Kris as a query with its exact text. ORCA-WATCH stays read-only.

### C17 · Broadcasts the method does not yet mention

- **The README and `AGENTS.md`:** sessions read the broadcast file at each call; "An `away` broadcast is Kris's words opening an unattended window", recorded under `ki-coordination`'s rules.
- **BCAST-THREADS and BCAST-AUTHORITY:** still open as inbox-sol's Q37 and Q38.
- **The standard** (Away grants): a window records its end, "work, permitted actions, exclusions, wake and stop words"; an Away broadcast carries only an end time and "within your existing authority".
- **Why they conflict:** Agora's documents state as settled what is still an open question, and the mark broadcast (B1) depends on sessions reading the file.
- **What would resolve it:** Kris's answers to Q37 and Q38, then one `ki-coordination` line; until then the README marks both as proposed.

### C18 · Three things keeping checkouts level

- **AGORA-OWNS-STATE** (3 November) and the README: Agora keeps every checkout level; "no household needs a push pass of its own".
- **The standard's inbox watch:** each listening session fetches and fast-forwards its own `main`. SYNC-LINE-OFF (Kris about 18:00, 4 November): "Agora keeps the machines in sync through each machine's household work package".
- **Spec part 10 roles:** the housekeeper keeps "the rig's checkouts level with their remotes"; Q22 (proposed, open) splits writer, Agora and housekeeper. Inbox-sol on 3 November: "households keep push passes, because Agora never pushes".
- **Why they conflict:** each of three parties is described as keeping checkouts level, with no stated hand-off.
- **What would resolve it:** Q22 agreed and written once: the writer pushes, Agora fast-forwards and flags, the housekeeper fixes what Agora flags; the standard's watcher stops fetching where Agora runs (C7).

### C19 · Agora, the KIV and the Observatory

- **HOST-AGENT-HOME a** (Kris 22:52, 2 November): two apps; the Observatory becomes an Electron app with the KIV as one area; `AGENTS.md`: "Agora never ... views the estate".
- **MORNING-FEEDBACK** (Kris about 10:40, 3 November): the KIV becomes "an Electron app as a cut-down, portable Observatory that later sends prompts through Agora".
- **Spec Q8** (open): is that app Agora itself, quiet in the menu bar with an "IDE mode" window?
- **AGORA-FOCUS** (6 November): "What are the differences between agora, KIV and observatory, and what are our plans for them? ... an overarching design for them."
- **Why they conflict:** three apps, two plans for which hosts the KIV, and an open question whether Agora grows a window, against Agora's own rule that it never views.
- **What would resolve it:** the overarching design Kris asked for (B26), owned jointly with the KIV's holder (personal.reg.inbox-sol `kiv`) and ki.prj.observatory.

### C20 · Spec first, or build slices now

- **Kris** (about 18:05, 4 November): "I want to solve all the problems in the specification and then get you guys to all go off and solve it and make it work"; SPEC-FIRST in inbox-sol (nothing sent until agreed); AGORA-FOCUS: "it needs some more thought".
- **Against it:** MARK-ALL "urgent ... take it next" (3 November); CSWAP-AGORA "high priority" (4 November); KI-AGORA-WRK-004 high; AGORA-START a recommends KIV-SEND next; `state.md` plans "the next build slice" with five items.
- **Why they conflict:** Agora is building ahead of a spec that will define what it is, while the wake pilots, T3 Code and AHP work (B8, B12, B13) wait for that spec.
- **What would resolve it:** Kris says which slices go ahead before the spec (the mark broadcast and the small fixes look independent of it) and which wait.

### C21 · The package's own scope and focus against its records

- **`work.md` Scope** lists four records in scope; seven are assigned or held here (KI-AGORA-WRK-002, WRK-003, WRK-004 and LVL-001 are missing).
- **`work.md` Focus** has no line for Agora's core (presence, keeping level, watch and call), so B27 and B31 sit in `_emerging`; host settings (KI-AGORA-LVL-001) sit under `jobs`; floating doers and routing (B19) have no line.
- **FOCUS-LIST a** (Kris about 00:30, 6 November) set the five focus lines one hour before AGORA-FOCUS narrowed what Agora is.
- **What would resolve it:** after C3, rewrite Scope and Focus together; a `core` line if Agora's core work is to be tracked.

## Stale in the work package

Lines that are no longer true, 24 in all. Text for the coordinator is in [consolidate.package.md](consolidate.package.md).

### `work.md` (5)

1. Scope In names only KI-AGORA-APP-001, NET-001, TRY-001 and WRK-001; WRK-002, WRK-003, WRK-004 and LVL-001 are missing.
2. Scope In: "the run-once jobs register with personal.reg.household-sol (AGORA-JOBS)": the register is household-sol's and held; the `jobs` focus is now scheduled jobs, accounts and keep-awake.
3. Scope Out: "coordination method and message words (ki.prj.ways-of-working)": now personal.reg.inbox-sol under COORD-SOLE and TOPIC-HOMES, with ki.sop.main keeping the standard.
4. Scope Out: "the KIV app itself (assistant-terra.kiv)": now personal.reg.inbox-sol's `kiv` focus (KIV-HOME a).
5. Focus 1: "the KIV send side": its waiting consumer is now personal.reg.inbox-sol, not assistant-terra.kiv.

### `state.md` (10)

6. Now 4: "its open points are with Kris as DEFAULTS, MARK-WORDS, MARK-LATE and MARK-HOLD": three were answered at about 00:30; only MARK-WORDS is open.
7. Now 4: "its five design points are with Kris": four; SCHED-FOCUS-HOST was settled with FOCUS-FIT.
8. Now 5: "follows the baseline ... (ASOL-005)": the baseline's focus-line rules were replaced by COORD-SOLE, and `ASOL-` ids are retired.
9. Now 6: "Agora now decides what the report footer shows (FOOTER-AGORA)": contested since FOOTER-RADIATOR and TOPIC-HOMES (C5).
10. Next 2: "drop the sync line now Agora keeps checkouts level": done by the standard at `db5dcab3`.
11. Next 3: "beside PERSONAL-DOTFILES-UE-137": cancelled and pruned; now KI-AGORA-WRK-004.
12. Next 4: "assistant-terra.kiv's KIV-ELECTRON waits on it": now personal.reg.inbox-sol's `kiv`.
13. Next 6: "as AGORA-RUN-ONCE set in assistant-sol's decisions": renamed; and the register is household-sol's to land.
14. Next 7: "after AGORA-COUNT-PLACE": overtaken by the delivered identity, which put the count in the menu's first line.
15. Next 13: "SYNC-LINE-OFF go[es] into the next build slice": nothing to build; ki.sop.main has done it.

### `messages.md` (3)

16. SYNC-LINE-OFF: done by the standard; the line can be taken.
17. WAKE-ARCHITECTURE: "Reply to assistant-sol": now personal.reg.inbox-sol, which may withdraw it (Q13).
18. TERRITORY-NAMES: still unACKed two days on, and Agora's README still says `ki territory roots` "fails a whole territory over one member it cannot resolve", which this line says is no longer so.

### `decisions.md` (4)

19. AGORA-DOORBELL: "listening on the doorbell waits on Kris's word (LISTEN)": settled by ASOL-005.
20. SUMMARY-NOW: "until `ki-coordination` carries it": it does.
21. FOCUS-FIT (4 November): "lifted to high": answered a on 6 November.
22. ASOL-005 and ASOL-011: "`coordination🔗` first on the focus line" and "`coordination` stays first": both replaced by COORD-SOLE.

### `discussions.md` (2)

23. AGORA-COUNT-PLACE: overtaken by KI-AGORA-TRY-001's delivered design (option a in effect).
24. AGORA-START context: "four focus lines and three triage records ... Nothing is running": now five focus lines and seven triage records.

### Outside the package, for their owners

- Agora's README, Forward work: "signing the app and waking workers": six more records exist. Its call, watch and broadcast examples use old ids (C14).
- The [Agora Project note](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md): "How Agora waking workers fits the focus's bound ... is a question for the Project's first Summary": answered as FOCUS-FIT a; `lifecycle: planned` while the Project is open.
- The coordination standard: "doorbells ... stay deferred" (C6); the inbox watch's own fetch loop (C7).
- Inbox-sol's spec: Q24 and Q25 still "Open" though Q32 and Q33 closed them; the index lists WAKE-ARCHITECTURE as "Awaiting ACK".
- Household-sol's plans: links to `personal/assistant/.../async/host-agent.md`, which no longer exists.
