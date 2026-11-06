---
id: ki.prj.agora
state: handoff-to-supervisor
since: 2026-11-06T00:04:42Z
received: null
beat: null
mark: 2026-11-06T00:04:42Z
listening_enabled: true
listening_status: on
method_read: 3ffd23bc
---

# ki.prj.agora state

## Now

- Opened by Kris on 3 November 2026 at 23:00 GMT, releasing the hold it was created under. The hand-over from personal.reg.assistant-sol is taken: its `agora` focus, design note [host-agent.md](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/agora/host-agent.md) and briefs and run reports in [agora/](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/agora) are this Project's now.
- Records held in apps-agora.local: [KI-AGORA-APP-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-APP-001-package-and-relaunch.md), [KI-AGORA-NET-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-NET-001-observatory-read-endpoint.md) and [KI-AGORA-WRK-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-001-wake-workers.md) in triage; [KI-AGORA-TRY-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-TRY-001-menu-bar-identity.md) awaiting review, which State of play brings in its acceptance bundle.
- Households install and update Agora on each rig under AGORA-INSTALL-GRANT ([decisions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/decisions.md)); this Project builds and releases only.
- mark-all-scope received at the 6 November mark: a `mark` broadcast kind beside `away` and `ping`, tray only; its open points are with Kris as DEFAULTS, MARK-WORDS, MARK-LATE and MARK-HOLD. Nothing is running. Scheduled jobs are captured as [KI-AGORA-WRK-004](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-004-run-the-rigs-scheduled-jobs.md), triage, high; its five design points are with Kris. Orca #33114 and #33115 are recorded as an external dependency of KI-AGORA-WRK-001 (ORCA-UPSTREAM); a read-only watch is proposed to Kris as ORCA-WATCH. CSWAP-AGORA is captured as [KI-AGORA-WRK-002](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-002-switch-claude-accounts.md), triage, high; its switching strategy is settled with Kris before any work.
- Coordination is the one topic for now (ASOL-005, Kris about 18:15 GMT), held by personal.reg.inbox-sol; this package no longer lists `coordination` (COORD-SOLE); coordination and communication questions go to personal.reg.inbox-sol (TOPIC-HOMES) and follows the baseline: `## Inbound` and `## Outbound` with ids and ACKs, listening on Agora's call.
- Agora now decides what the report footer shows (FOOTER-AGORA); the Summary model is in `ki-coordination`.
- The thread listens on Agora's call, `~/.local/state/ki/agora/doorbell/ki.prj.agora` until AGORA-CALL renames it (ASOL-005).
- Queries with Kris are in [discussions](discussions.md).

## Next steps

1. On Kris's answers, plan and build the mark broadcast slice (MARK-ALL); tell personal.reg.inbox-terra when the mark broadcast lands or what blocks it.
2. `send`: the footer, under FOOTER-AGORA and FOOTER-ART: drop the sync line now Agora keeps checkouts level, drop the listening line once Agora can wake every thread including Orca chats (KI-AGORA-WRK-001), and agree the footer with ki.sop.main, which notifies every package.
3. `jobs`: design, with Kris, Agora as the scheduler of the rig's jobs, saying when one fails or stops (AGORA-SCHEDULER, beside PERSONAL-DOTFILES-UE-137); nothing is built until the design is agreed.
4. `send`: build Agora's send side for the KIV Electron app (KIV-SEND; assistant-terra.kiv's KIV-ELECTRON waits on it), and wake Orca chat threads from Agora (ORCA-WAKE, Orca #33114); nothing is posted to Orca or any other owner's repository or service without Kris's express permission for that post (NO-EXTERNAL-POSTING).
5. `voice`: the voice bard path (VOICE-BARD).
6. `jobs`: the run-once jobs register with personal.reg.household-sol, as AGORA-RUN-ONCE set in assistant-sol's [decisions](https://github.com/krisb/assistant/blob/5f2655d9/%2B/_WORK/personal.reg.assistant-sol/decisions.md) (AGORA-JOBS).
7. `identity`: take on a designer doer (Claude Design) for Agora's identity (AGORA-DESIGNER), after AGORA-COUNT-PLACE and the review of KI-AGORA-TRY-001.
8. Take Kris's answers to the open queries; AGORA-START sets what follows MARK-ALL.
9. AGORA-HANDOFF (household-sol, Kris about 23:30 GMT): Agora owns its design and roadmap; household-sol installs and runs it on sol and keeps the housekeeping register. Take the [Rig install plan](https://github.com/krisb/dotfiles/blob/main/+/_WORK/personal.reg.household-sol/housekeeping/agora-rig-plan.md) (AGORA-RIG-GO a, AGORA-LOGIN a, every territory configurable), Kris's settings-screen ideas (permissions check, OneDrive-like tree of territories and repositories, assignments view), Agora's architecture in `apps-agora.local` docs, the naming question (workers, housekeeping activities, housekeeper) and the held [jobs register](https://github.com/krisb/dotfiles/blob/main/+/_WORK/personal.reg.household-sol/housekeeping/jobs-register-plan.md) questions JOBS-HOME, JOBS-GUARD, JOBS-HOSTS and JOBS-MOVER; raise CONFIG-OWNER with Kris.
10. AHEAD-RING-NOISE (seen 4 November, 23:27-23:38 GMT): the `ahead, push it` call rings this package for every transient ki-principal commit another session pushes seconds later; settle briefly before ringing and ring only the committing session's package (by its `Work-Id`). Fold into the next Agora slice.
11. SHELL-WATCH: keep Electron, keep the shell in `src/main.ts`, and re-check GPUI online (with web reads allowed) before planning the settings screen or any larger window, or when another trigger in the decisions log holds.
12. KEEP-AWAKE: settle the open points in [KI-AGORA-WRK-003](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-003-keep-host-awake-while-work-runs.md) and [KI-AGORA-LVL-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-LVL-001-check-host-settings-against-rig.md) with Kris before any build.
13. Inbound not yet acted on: LEGAL-AUTOMATION and WAKE-ARCHITECTURE wait on WAKE-NOTE; AGORA-CALL, LISTEN-HOW, TERRITORY-NAMES and SYNC-LINE-OFF go into the next build slice after AGORA-START.

## Held

None
