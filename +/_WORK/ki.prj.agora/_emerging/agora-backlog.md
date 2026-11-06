---
work: ki.prj.agora
run: ki-prj-agora
agent: consolidate
written_at: 2026-11-06T03:19:49Z
---

# KI > Techne > Agora › consolidate › backlog

One backlog for Agora, gathered on 6 November 2026 at about 03:15 GMT from the work package `ki.prj.agora` and its Git history since 3 November, `apps-agora.local` (README, `AGENTS.md`, records, design), the six run reports, personal.reg.inbox-sol's decisions, spec and research, household-sol's two plans, and the coordination standard at `3ffd23bc`. It decides nothing.

**How to read it.** Each item gives what it is, its sources (Kris's words and dates where they exist), its record, its focus area, what it depends on, and its state: **done**, **built-not-adopted** (code exists, record not accepted), **designed** (scoped or planned on paper), **captured** (a record or inbound line exists, not designed), or **idea**. **Owner** says when the item is really coordination (personal.reg.inbox-sol's, under COORD-SOLE and TOPIC-HOMES) or another owner's, with Agora only an input or a builder.

Records live in [apps-agora.local `docs/roadmap/`](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/). The conflicts these items raise are in [agora-alignment.md](agora-alignment.md), cited as C1 to C21.

## Summary

| Focus | Items | Done | Built, not adopted | Designed | Captured | Idea |
| --- | --- | --- | --- | --- | --- | --- |
| `send` | 13 | 0 | 0 | 1 | 6 | 6 |
| `jobs` | 6 | 0 | 0 | 1 | 4 | 1 |
| `voice` | 1 | 0 | 0 | 0 | 1 | 0 |
| `identity` | 2 | 0 | 1 | 0 | 0 | 1 |
| `_emerging` | 9 | 1 | 2 | 0 | 2 | 4 |
| **All** | **31** | **1** | **3** | **2** | **13** | **12** |

Twelve of the 31 are really coordination or another owner's (marked **Owner** below). Settled answers that need no work are listed at the end, not counted.

## `send` — getting messages and signals to sessions

### B1 · Mark broadcast

- **What:** one tray action that has every listening session, on every rig, strike its mark and give its Summary; a fourth broadcast kind, `mark`, beside `away`, `ping` and `message`, with `only` and `no art` flags and the ping's acknowledgement path.
- **Sources:** MARK-ALL, Kris 3 November about 23:25 GMT and, as urgent, about 23:40 GMT: "it's underpinning how we are all interacting and getting a clear understanding ... adding to Agora the ability to broadcast a mark, that seems very important". Scoped by run mark-all-scope (4 November 01:47 GMT, received at the 6 November 00:04 mark). Kris's answers about 00:30 GMT on 6 November: DEFAULTS a (tray only; acknowledged like a ping; new Agora on every Mac first), MARK-LATE b (the broadcast's sending time is the mark), MARK-HOLD b (a held session strikes and gives its hold report). MARK-WORDS open: "Let's come back to this one".
- **Record:** none; mark-all-scope proposed KI-AGORA-TRY-002.
- **Focus:** `send` ⭐.
- **Depends on:** MARK-WORDS; capture of the record; the standard line for ki.sop.main, which must be redrafted because mark-all-scope's draft says the opposite of MARK-LATE b and MARK-HOLD b (C10, C11); B9 (sessions told to read broadcasts at all); every Mac upgraded before the first mark (MARK-ROLLOUT).
- **State:** designed.

### B2 · Rename the doorbell to Agora's call

- **What:** rename the `doorbell/` state folder, README and `AGENTS.md` wording, the view schema field and the tray words to "call", with a transition so sessions waiting on `doorbell/<work-id>` keep working, then tell the live sessions the new path.
- **Sources:** AGORA-CALL, Kris about 01:20 GMT on 4 November: "an [agora] doesn't have a [doorbell] ... a better name that fits with the [Agora] ethos"; Kris chose **Call**. LISTEN-HOW (about 01:45 GMT): "'Agora's call' is the name". Spec part 1 already defines the term as "renamed from doorbell". Inbound line, not taken.
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** AGORA-START (which slice comes next); C6 (the standard still says doorbells are deferred).
- **State:** captured.

### B3 · Say how each session listens

- **What:** each session's footer and its `workers:` register entry say how it listens: Agora's call, polling at an interval, on open (cloud sessions such as Claude Design), or not listening; Agora and the KIV show the same values.
- **Sources:** LISTEN-HOW, Kris about 01:25 GMT on 4 November: "when it says it's listening, it says how it's listening ... either Agora's call or ... some kind of polling-based approach ... things that can't wait for Agora's call, such as Claude Design sessions can indicate how they're listening." Forwarded by ki.sop.main as "footer content being yours under FOOTER-AGORA". Spec part 3 repeats it. Inbound line, not taken.
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** B4 (who owns the footer); Q21 in inbox-sol's spec (what counts as listening).
- **State:** captured.
- **Owner:** the wording is contested between Agora, ki.sop.main and personal.reg.inbox-sol (C5); Agora's own part is showing the value it reads.

### B4 · The footer: what it shows and where its rules live

- **What:** decide what the footer's art and lines carry, from what Agora actually provides; drop the sync line (now done in the standard) and drop the listening line once Agora can wake every session.
- **Sources:** FOOTER-AGORA, Kris about 23:40 GMT on 3 November, via household-terra: the footer is Agora's to decide, liaising with ki.sop.main. FOOTER-ART (4 November): Kris's KNOWLEDGE ISLANDS art opens it. SYNC-LINE-OFF, Kris about 18:00 GMT on 4 November (inbound, not taken): the sync line comes out. FOOTER-RADIATOR, Kris about 09:45 GMT on 4 November: the footer is "the information radiator that I need when I'm interacting", and its home is unclear. Spec part 5 and Q7 (open); spec send-out list: "the footer's rules in one place" to ki.sop.main and ki.prj.agora. The standard at `3ffd23bc` repeats FOOTER-AGORA and has already removed the sync line.
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** C5 (one owner); B11 (waking every session) before the listening line can go.
- **State:** captured; the sync-line half is done by ki.sop.main.
- **Owner:** coordination (shared; see C5).

### B5 · Agora's send side for the KIV

- **What:** a way for the KIV app to send prompts and messages through Agora.
- **Sources:** KIV-SEND, handed over by ki.sop.main on 3 November; Kris about 10:40 GMT on 3 November (MORNING-FEEDBACK): the KIV "becomes an Electron app as a cut-down, portable Observatory that later sends prompts through Agora". The KIV's KIV-ELECTRON waits on it (the KIV is now personal.reg.inbox-sol's `kiv` focus, KIV-HOME a, 6 November). AGORA-START a recommends it next. Spec part 6 and Q8 (is the app Agora itself, with an "IDE mode" window?) are open.
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** the Agora, KIV and Observatory design Kris asked for under AGORA-FOCUS (B26, C3, C19); a write path into Agora, which is a new security surface (Agora's local endpoint is read-only today).
- **State:** idea.

### B6 · Wake Orca chats

- **What:** wake a session opened as an Orca chat once Orca ships `orca chat send`, keeping Agora's own between-turns check because Orca offers no idle-only option.
- **Sources:** ORCA-WAKE (ki.sop.main, 3 November); AGORA-WAKE c, Kris about 03:25 GMT on 3 November; ORCA-UPSTREAM, Kris about 21:15 GMT on 5 November: the Orca post "was really important ... in terms of where we're going and therefore something we're tracking externally". Run orca-upstream recorded stablyai/orca#33114 (open) and #33115 (open, last updated 2 November).
- **Record:** [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) (Dependencies).
- **Focus:** `send`.
- **Depends on:** Orca merging and releasing #33115. Q28 (Kris, 01:59 GMT on 6 November): no comment goes to #33114.
- **State:** captured (waiting on Orca).

### B7 · Watch the Orca chat-send work

- **What:** a read-only check of Orca #33114 and #33115 that tells Kris of a new reply, a merge or a release.
- **Sources:** ORCA-UPSTREAM's suggestion (household-sol, 5 November); query ORCA-WATCH (a: inside Agora on its review interval; b: as a rig housekeeping job; c: by hand).
- **Record:** KI-AGORA-WRK-001 (Discussion, proposed).
- **Focus:** `send`.
- **Depends on:** Kris's ORCA-WATCH answer; outbound GitHub reads would be new for Agora (C4).
- **State:** idea.

### B8 · Wake pilots for Claude and Codex sessions

- **What:** pilot a Claude Code `asyncRewake` hook on Agora's call (no two-hour limit), Agora posting its call into a Claude session's inbox, and `codex queue` for a Codex chat in Orca; and run detached runs as Orca orchestration workers so Orca wakes the coordinator when they finish.
- **Sources:** inbox-sol spec part 3; Kris about 20:37 GMT on 4 November (Q16 "both pilots ... run by ki.prj.agora"; Q17 yes, "a build item for tools-ki and ki.prj.agora"); Kris about 01:56 GMT on 6 November (Q26 yes). Evidence: [wake-research.md](/Users/krisbrown/kis/personal/inbox/+/_WORK/personal.reg.inbox-sol/coordination/wake-research.md).
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** SPEC-FIRST: inbox-sol sends nothing until the spec is agreed, so none of this has reached Agora as a message yet. Q17 is shared with tools-ki through ki.sop.main.
- **State:** idea (agreed in the spec, not sent).
- **Owner:** routes decided by coordination; Agora builds.

### B9 · Tell sessions to read broadcasts, and what an Away grants

- **What:** whether the coordination method tells every session to read Agora's broadcast file at each call (`mark` included), and whether an Away broadcast opens an unattended window within existing authority.
- **Sources:** BCAST-THREADS and BCAST-AUTHORITY, handed over on 3 November, sent to inbox-sol as AGORA-002 on 5 November; now inbox-sol's Q37 and Q38, open, recommended yes. The README and `AGENTS.md` already describe both as if answered yes (C17).
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** Kris's answer through inbox-sol; then a `ki-coordination` line from ki.sop.main.
- **State:** captured.
- **Owner:** coordination.

### B10 · Quieter "ahead, push it" calls, and the Work-Id trailer

- **What:** settle briefly before ringing `ahead, push it`, and ring only the package that made the commit, read from its `Work-Id:` trailer; and whether the house adopts that trailer.
- **Sources:** AHEAD-RING-NOISE, seen 4 November 23:27 to 23:38 GMT (every short-lived ki-principal commit rang this package); WORK-ID-TRAILER, handed over 3 November, now inbox-sol's Q39 (open, recommended yes); WORK-ID-OWN (assistant-sol uses the trailer since 3 November).
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** Q39 for the house rule; the Agora fix stands alone.
- **State:** idea (the fix); captured (the rule).
- **Owner:** the house rule is coordination's; the fix is Agora's.

### B11 · Answer Legal, and the wake architecture note

- **What:** one note, with a diagram, of how each surface Kris uses (Orca chat and terminal with Claude Code and with Codex, Claude Desktop, Claude Design) is reached and woken today, what is proven, and the target route through Agora; and the answer Legal asked for: the accountable owner and the verified limits.
- **Sources:** WAKE-ARCHITECTURE, Kris about 09:30 GMT on 4 November: "map out an architecture for this ... fully understood in the [Agora] project". LEGAL-AUTOMATION-AGORA-20261104 (lgl.sop.main, 4 November): "take ownership or coordinate ownership with that assistant; do not run duplicate competing fixes". Query WAKE-NOTE (open). Inbox-sol's Q13 (open): keep WAKE-ARCHITECTURE with Agora, or withdraw it since the spec now maps waking; its send-out list has inbox-sol answering Legal itself (C15).
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** Kris answering WAKE-NOTE and Q13 together.
- **State:** captured (two inbound lines, unacknowledged).
- **Owner:** contested between Agora and coordination.

### B12 · Built around the Agent Host Protocol

- **What:** Agora delivers to sessions through the Agent Host Protocol where a tool speaks it, falling back to each tool's own route (Orca terminal send, Claude inbox, `codex queue`, T3 Code) where it does not; an adapter contract of address, deliver, acknowledge and presence.
- **Sources:** AHP-FIRST, Kris about 02:30 GMT on 6 November: "Agora becomes something which would utilize the AHP. Now, in the interim of systems that don't support AHP, we can fall back to one of our other methods. But yes, fundamentally, I think we should be focused around it." Q33 (our own MACP dropped); Q32 (no ACP client use: "Agora is not meant to be a chat client"). Spec Evidence: neither Orca nor T3 Code is known to speak AHP.
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** spec part 4 ("Agora, the manager", to do); HOST-WORD (what we call AHP's "host", C13).
- **State:** idea.
- **Owner:** the contract is drafted in coordination's spec; Agora builds it.

### B13 · Deliver to T3 Code

- **What:** add T3 Code as a tool Agora can deliver to (`t3 thread send` or its MCP server) and trial one Codex coordinator in it.
- **Sources:** T3-CODE, Kris 22:08 GMT on 4 November ("an alternative to Orca as the session host"); Kris 22:10 GMT: Agora is complementary to either; Q27, Kris about 01:56 GMT on 6 November: "yes, one trial". TOOL-LANDSCAPE (22:40 GMT): Vercel Labs' Agent Desktop and REA to look at too.
- **Record:** none.
- **Focus:** `send`.
- **Depends on:** SPEC-FIRST (not yet sent to Agora); B12.
- **State:** idea.

## `jobs` — running the rig's timed work

### B14 · Run the rig's scheduled jobs

- **What:** Agora runs the jobs Rig declares for its host, on schedule, and reports a failure or a missed run the same day; Rig keeps the declarations and tools-rig gains an Agora engine in place of launchd. Includes the housekeeping due check and moving the in-session refresh loop out.
- **Sources:** AGORA-SCHEDULER, Kris about 01:50 GMT on 4 November: "maybe it's the agora that should be scheduling the jobs. It should be effectively the thing that sits there running for us, that just sits nicely and quietly in the tray"; MSG-9556f9a6, Kris about 00:12 GMT on 6 November, closing PERSONAL-DOTFILES-UE-137 as moved here (cancelled and pruned in chezmoi); PROCESS-FINDINGS (household-terra): Route Triage and the WhatsApp refresh failed silently for days. Queries SCHED-FIRST, SCHED-REPORT, SCHED-PAUSED, SCHED-ONE-RIG open; SCHED-FOCUS-HOST settled a with FOCUS-FIT.
- **Record:** [KI-AGORA-WRK-004](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-004-run-the-rigs-scheduled-jobs.md), triage, high.
- **Focus:** `jobs`.
- **Depends on:** Q30 in inbox-sol's spec, answered about 02:12 GMT on 6 November the other way (C2); the Agora engine in tools-rig (MSG-14f2a17c to ki.prj.mac-studio-setup); FOCUS-FIT for any job that starts an agent; the four SCHED queries.
- **State:** captured.

### B15 · Jobs register and run-once claims

- **What:** which jobs may run on which Macs, which must run on exactly one, and where each runs now; a run-once claim so another Mac can take over safely.
- **Sources:** AGORA-RUN-ONCE, Kris 01:15 GMT on 3 November: "we keep [a] list [of] all scheduled jobs and [the] hosts they're running on ... some ... must uniquely run, or singleton ... we just put it into dot files [as the] coordination point"; AGORA-JOBS (handed over 3 November); household-sol's [jobs register plan](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-sol/housekeeping/jobs-register-plan.md), where Agora reads the register and "never moves a job itself"; Kris, 3 November about 09:05 GMT: JOBS-SYNC a; JOBS-HOME "why have we decided on the word jobs and not workers?"; JOBS-GUARD and JOBS-HOSTS deferred; JOBS-MOVER open. KI-AGORA-WRK-001 holds run-once claims with Route Triage as pilot; SCHED-ONE-RIG a would keep Rig's host selection for now; KI-AGORA-WRK-002 overlaps.
- **Record:** [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) (claims); the register has none.
- **Focus:** `jobs`.
- **Depends on:** C8 (one model for jobs); household-sol landing the register.
- **State:** designed (register, held); idea (claims).
- **Owner:** the register is household-sol's; Agora reads it.

### B16 · Switch Claude accounts from one decider

- **What:** one periodic decider, run from Agora, picks each Mac's Claude account by Kris's own rules and runs `cswap switch`, replacing the two `cswap auto` agents.
- **Sources:** CSWAP-AGORA, Kris about 08:00 and 08:10 GMT on 4 November: "a single point of running ... some logic around something which we run periodically, which then runs from Agora", high priority; HTERRA-005 re-sent it; PERSONAL-DOTFILES-UE-139 cancelled as moved.
- **Record:** [KI-AGORA-WRK-002](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-002-switch-claude-accounts.md), triage, high.
- **Focus:** `jobs`.
- **Depends on:** the switching strategy settled with Kris first; B14 or B15 (which host runs the decider); C4 (a command run on a peer).
- **State:** captured.

### B17 · Keep the host awake while work runs

- **What:** hold an idle-sleep assertion while Agora sees work running on its host, and release it when all is idle.
- **Sources:** KEEP-AWAKE (1), Kris about 23:50 GMT on 5 November: "while Agora sees work running on its host ... it holds a macOS system-sleep assertion, as `caffeinate -i` does ... no new tool".
- **Record:** [KI-AGORA-WRK-003](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-003-keep-host-awake-while-work-runs.md), triage, medium.
- **Focus:** `jobs`.
- **Depends on:** its two open points (which work counts; whether the tray shows it); B14 for scheduled jobs counting.
- **State:** captured.

### B18 · Check host settings against Rig

- **What:** compare the host's settings with what Rig declares, power first, report drift, and keep a setting level only where Kris agrees.
- **Sources:** KEEP-AWAKE (2), same message: "Agora checks, and where agreed keeps, the host's settings against what Rig declares the host should be, power settings first, and reports drift."
- **Record:** [KI-AGORA-LVL-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-LVL-001-check-host-settings-against-rig.md), triage, medium.
- **Focus:** `jobs` (filed with keep-awake; no focus names host settings).
- **Depends on:** its three open points; C4 ("keeps" against `AGENTS.md`).
- **State:** captured.

### B19 · Floating doers, territory routing and starting workers through `ki agent`

- **What:** the rest of KI-AGORA-WRK-001: wake live runs with `ki agent send`, a per-host list of doers waiting for work with a work-in-progress cap, and routing work by territory.
- **Sources:** `AGENTS.md` (later slices); host-agent design (2 to 3 November), which also had Agora start runs with `ki agent launch` from standing briefs; FOCUS-FIT a, Kris about 00:30 GMT on 6 November: Agora may wake threads and runs Kris opened, and anything that starts a fresh agent on its own waits for an Enactment decision; AGORA-TERRITORIES b later ("only the territories live on that host ... once Agora routes work by territory").
- **Record:** KI-AGORA-WRK-001.
- **Focus:** `jobs` (by its record area; no focus line names it).
- **Depends on:** C1 and C3 (whether this is still Agora's after AGORA-FOCUS).
- **State:** idea.

## `voice`

### B20 · The voice bard path

- **What:** a path by which Kris, speaking to a voice assistant, reaches his sessions through Agora.
- **Sources:** VOICE-BARD (ki.sop.main, 3 November, one line, no detail); Kris about 10:40 GMT on 3 November: "the bard is any voice mode (ChatGPT or Claude)"; the Project note's test: "a thread on any rig, reached by voice or text, wakes and acts on news without polling"; spec goal 1 names ChatGPT voice; spec part 3's wake table: voice is woken by "Kris speaking".
- **Record:** none.
- **Focus:** `voice`.
- **Depends on:** a definition of what Agora's part is; C3.
- **State:** captured (a name only).

## `identity`

### B21 · Menu-bar identity, review and acceptance

- **What:** the meeting-ring symbol and its twelve states, the app icon, the reordered tray menu and the notifications, already on `main`; it waits for review and acceptance. The group count already moved to the menu's first line, which is AGORA-COUNT-PLACE's option a.
- **Sources:** the brief from assistant-sol, 3 November; AGORA-COUNT-PLACE (handed over 3 November, still open in discussions, overtaken by the delivered design).
- **Record:** [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md), awaiting review; State of play brings it in its acceptance bundle.
- **Focus:** `identity`.
- **Depends on:** a look on a Mac and `ki repo audit` (outstanding in the record).
- **State:** built-not-adopted.

### B22 · A designer doer for Agora's identity

- **What:** take on a Claude Design doer for Agora's look under this Project.
- **Sources:** AGORA-DESIGNER (ki.sop.main, 3 November).
- **Record:** none.
- **Focus:** `identity`.
- **Depends on:** B21's review; B26 (the app's shape).
- **State:** idea.

## `_emerging`

### B23 · Package, sign and relaunch

- **What:** a Developer ID signature and notarisation, and confirming relaunch on a signed build; the ad-hoc packaged app, its launch agent and its install script are already built and installed.
- **Sources:** HOST-AGENT-ALIVE a and AGORA-RELAUNCH a (Kris, 2 and 3 November); Kris about 02:45 GMT on 3 November: run Agora "as [a] proper app without me having [to] start [it] up myself"; AGORA-INSTALL-GRANT (3 November about 02:50 GMT): this thread sends AGORA-READY when a package lands.
- **Record:** [KI-AGORA-APP-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-APP-001-package-and-relaunch.md), triage.
- **Focus:** `_emerging`.
- **Depends on:** an Apple Developer ID and authority to package for distribution.
- **State:** built-not-adopted (ad-hoc build); the signing half is captured.

### B24 · Observatory and KIV read endpoint

- **What:** `GET /v1/state` and `/v1/events` on `127.0.0.1:1677`, the live picture for the Observatory and the KIV.
- **Sources:** Kris through assistant-sol, 3 November; the KIV's Now page already reads it.
- **Record:** [KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md), triage, "Delivered, awaiting adoption".
- **Focus:** `_emerging`.
- **Depends on:** Kris adopting it, then review.
- **State:** built-not-adopted.

### B25 · Settings screen and who owns the settings file

- **What:** a settings window with a macOS permissions check, a OneDrive-like tree of territories and repositories (managed by default, with exceptions), and a view of assignments (workers to packages, housekeeping to rigs); and who owns `~/.config/agora/config.toml` once the app can write it.
- **Sources:** Kris about 09:10 GMT on 3 November, via AGORA-HANDOFF; query CONFIG-OWNER (open); AGORA-TERRITORIES, Kris about 09:00 GMT on 3 November: "It should be configurable by each host"; SHELL-WATCH (re-check GPUI online before planning this).
- **Record:** none.
- **Focus:** `_emerging`.
- **Depends on:** CONFIG-OWNER (C9); B26.
- **State:** idea.

### B26 · What Agora is: its specification and the Agora, KIV and Observatory design

- **What:** a specification of Agora's purpose and limits, its architecture written in the repository, and one overarching design that separates Agora, the KIV and the Observatory.
- **Sources:** AGORA-FOCUS, Kris about 02:15 GMT on 6 November: "Agora is not meant to be a chat client ... It's only meant to send messages to other sessions running in other ways or help promote intercommunication. It's a place for coming together and talking. It's not a replacement ever for Orca ... I think we need to keep agora really focused on what it is ... Maybe it's time to have a specification for that. What are the differences between agora, KIV and observatory ... Maybe that's time to have an overarching design for them." Kris, 22:10 and 22:12 GMT on 4 November (spec part 4): Agora gets messages "into a heterogeneous environment of different tools", and does not host or own sessions. Kris asked for Agora's architecture in its repository's docs (AGORA-HANDOFF, 4 November). Spec part 4 (to do), Q6 (what Agora is responsible for) and Q8 (is the app Agora itself), all open. HOST-AGENT-HOME a (2 November): Agora and the Observatory are two apps.
- **Record:** none.
- **Focus:** `_emerging`.
- **Depends on:** Kris's direction now; nearly every other item waits on its answer (C3).
- **State:** idea.
- **Owner:** shared: the coordination model is inbox-sol's spec; Agora's own specification and architecture are Agora's.

### B27 · Keeping level: drop the territory fallback, add the run guard

- **What:** remove the fallback that keeps a territory's resolvable checkouts when `ki territory roots` fails, now that the command lists every resolvable member; use `ki agent status --format json` (`ki/agent-status/v1`) so Agora never fast-forwards a checkout a live run is working in.
- **Sources:** TERRITORY-NAMES (inbound, ki.sop.main via inbox-sol, 09:27 GMT on 4 November; tools-ki `6992ba1e`, `c55e8fab`); AGORA-RUN-GUARD; the host-agent design: fast-forward "only when the checkout is clean and no run is working in it".
- **Record:** none.
- **Focus:** `_emerging` (no focus names keeping level).
- **Depends on:** AGORA-START (which slice).
- **State:** captured.

### B28 · Follow the Inbox rename in Agora

- **What:** replace `personal.reg.assistant-*` and `krisb/assistant` in Agora's README, examples and test fixtures with the Inbox names.
- **Sources:** INBOX-RENAME, MSG-505228fc (Kris, 6 November): "carry out the cleanup pass ... references here and in the other repositories with each owner told first"; "apps-agora.local examples and fixtures naming the old ids are your choice". Taken: "updated in the next build slice".
- **Record:** none.
- **Focus:** `_emerging`.
- **Depends on:** the next build slice.
- **State:** captured.

### B29 · Install Agora on each rig through Rig

- **What:** chezmoi renders Agora's configuration from `rigs.yaml`, Rig declares the app, and each housekeeper builds and installs it.
- **Sources:** AGORA-RIG (Kris about 01:35 GMT on 3 November: "Can we get it installed via rig"); household-sol's [Rig install plan](/Users/krisbrown/.local/share/chezmoi/+/_WORK/personal.reg.household-sol/housekeeping/agora-rig-plan.md); Kris about 09:00 GMT on 3 November: AGORA-RIG-GO "Yes, land it", AGORA-LOGIN "App's own login item"; AGORA-UNREGISTER settled by Agora `c2c3ee9`.
- **Record:** none in Agora.
- **Focus:** `_emerging`.
- **Depends on:** household-sol; CONFIG-OWNER for later.
- **State:** done for the app's own part (login item, unregister); the chezmoi side is household-sol's.
- **Owner:** household-sol.

### B30 · Names: session, host, workers, jobs, housekeeping

- **What:** one naming pass Agora follows: "session" for "thread"; "host" and "rig" both mean the machine; a word of our own for the app that owns sessions; "jobs" or "workers"; "housekeeping" for both timed tasks and chezmoi's templates; "floating doers".
- **Sources:** spec Q1 (Kris 09:55 GMT on 4 November: "session" replaces "thread"); HOST-WORD, Kris about 02:45 GMT on 6 November: "no rig and host mean the machine that the session is on"; JOBS-HOME (Kris, 3 November): "why have we decided on the word jobs and not workers?"; AGORA-HANDOFF's naming question; household-sol's housekeeper rename (agreed).
- **Record:** none.
- **Focus:** `_emerging`.
- **Depends on:** inbox-sol's spec part 8 naming; C13.
- **State:** idea.
- **Owner:** coordination; Agora follows it in its words, code comments and records.

### B31 · Who keeps checkouts level, and who counts as listening

- **What:** the hand-off between Agora's fast-forward, each housekeeper's audit and fix of what Agora flags, and each session pushing its own work; and a roll call that checks a session is listening only when its `state.md`, its rig's Agora watch and its answers agree.
- **Sources:** inbox-sol spec Q22 (proposed, Kris asked who owns it, 20:50 GMT on 4 November) and Q21 (proposed: "listen right and nothing by accident", about 18:20 GMT); spec part 10 roles give housekeepers "keeping the rig's checkouts level"; ki.sop.main's WATCH-AGORA query (is `ki work watch` still wanted now Agora calls).
- **Record:** none.
- **Focus:** `_emerging`.
- **Depends on:** C7, C18.
- **State:** idea.
- **Owner:** coordination (Q21, Q22) and ki.sop.main (WATCH-AGORA).

## Open queries with Kris, by item

| Query | Where | Item |
| --- | --- | --- |
| MARK-WORDS | discussions | B1 |
| AGORA-START | discussions | which item follows B1 |
| WAKE-NOTE | discussions | B11 (with inbox-sol's Q13) |
| ORCA-WATCH | discussions | B7 |
| CONFIG-OWNER | discussions | B25 |
| SCHED-FIRST, SCHED-REPORT, SCHED-PAUSED, SCHED-ONE-RIG | discussions | B14, B15 |
| AGORA-COUNT-PLACE | discussions | B21; overtaken by the delivered design |
| KI-AGORA-WRK-002's switching strategy; KI-AGORA-WRK-003's and KI-AGORA-LVL-001's open points | the records | B16, B17, B18 |
| Q37, Q38, Q39 | inbox-sol | B9, B10 |
| Q6, Q7, Q8, Q13, Q21, Q22 | inbox-sol | B26, B4, B5, B11, B31 |
| JOBS-HOME, JOBS-GUARD, JOBS-HOSTS, JOBS-MOVER | household-sol | B15 |
| gpui-fit Q1 (check GPUI online) | run report only, never raised | SHELL-WATCH; taken in effect as a) |

## Settled, no work left

- **Done in Agora:** presence and trust, events and fallback, watch and call, keeping level, review and state, broadcasts with Away, I'm back and Ping, the Orca terminal wake (AGORA-WAKE-THREAD, AGORA-WAKE-CODEX), the login item and launch agent, the read endpoint (B24).
- **Answered:** FOCUS-FIT a and SCHED-FOCUS-HOST a; FOCUS-LIST a; DEFAULTS a; MARK-LATE b; MARK-HOLD b; LISTEN (by ASOL-005); COORD-SOLE (coordination dropped from Focus); LOCAL-VERSIONS (nothing to change); NO-EXTERNAL-POSTING (in every brief); ORCA-UPSTREAM (recorded on KI-AGORA-WRK-001); SHELL-WATCH (keep Electron, watch GPUI); SYNC-LINE-OFF (done in the standard at `db5dcab3`).
