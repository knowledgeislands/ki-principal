# ki.prj.agora decisions

## 2026-11-04 · Overnight messages taken (01:46 GMT)

- MARK-ALL (Kris, 3 November, 23:25 and 23:40 GMT, via personal.reg.assistant-terra): Agora gets a `mark` broadcast, urgent, taken next. Taken as: scope it now in run `ki-prj-agora` (mark-all-scope), bring the slice to Kris, then build.
- MARK-EXPECTED (Kris, 3 November, 23:30 GMT): replaced by SUMMARY-NOW; removed.
- REFRESH (ki.sop.main, MARK-STATUS): read `ki-coordination` at `f85ce21a`; `method_read` set.
- SUMMARY-NOW (Kris, 4 November, about 01:05 GMT, and in this thread at 01:45 GMT): follow the mark, summary and footer model in [summary-model.design.md](https://github.com/krisb/dotfiles/blob/29dc51c/+/_WORK/personal.reg.household-terra/_emerging/summary-model.design.md) from this session until `ki-coordination` carries it.
- FOOTER-AGORA (Kris, 3 November, 23:40 GMT, via personal.reg.household-terra): what the footer shows is Agora's to decide, with ki.sop.main; the sync line drops now, the listening line once Agora can wake every thread. FOOTER-ART (4 November): the footer opens with Kris's KNOWLEDGE ISLANDS art. Taken as: next steps under `send`.
- AGORA-DOORBELL (personal.reg.household-sol): sol's Agora watches this package; listening on the doorbell waits on Kris's word (LISTEN).
- AGORA-SCHEDULER (Kris, 4 November, about 01:50 GMT): "maybe it's the agora that should be scheduling the jobs". Taken as: a design to agree with Kris under `jobs`; nothing built.
- FOCUS-FIT: ki.sop.main's blind review chose the same course; lifted to high.
- HEARTBEAT (personal.reg.household-terra): replied live, SUMMARY-NOW taken.

## 2026-11-04 · ASOL-005 baseline (20:21 GMT)

- ASOL-005 (Kris about 18:15 GMT, via personal.reg.assistant-sol, COORDINATION-ONLY): ACKed in personal.reg.assistant-sol's Inbound; messages split into Inbound and Outbound; `coordination🔗` first on the focus line; listening on Agora's call (settles LISTEN, a); no focus folders, so no `index.md` needed yet.
- ASOL-011 (Kris, 22:26 GMT, NO-LINK-MARK and UNACKED-IN-LIST): ACKed; `coordination` stays first on the focus line with no 🔗; unACKed sends go in the banner list as `[awaiting ACK]`.
- HTERRA-005 (CSWAP-AGORA re-sent, Kris 4 November about 08:00 and 08:10 GMT): ACKed at 22:39 GMT; capture delegated to run cswap-capture; the record id goes to personal.reg.household-terra once captured; the switching strategy is settled with Kris before any work.
- MSG-242412d7 AGORA-HANDOFF (household-sol, Kris about 23:30 GMT): ACKed; taken into next steps; CONFIG-OWNER raised with Kris.
- MSG-b381c14a COORD-SOLE (Kris via ATER-010, 00:16 GMT): ACKed; `coordination` dropped from Focus; under TOPIC-HOMES, BCAST-THREADS, BCAST-AUTHORITY and WORK-ID-TRAILER sent to personal.reg.assistant-sol as AGORA-002 and removed from discussions.
- MSG-0a7adcb9 REFRESH (ki.sop.main, 5 November): read `ki-coordination` and `ki-work-package` at `db5dcab3`; `method_read` set; important lines moved above ordinary ones; the earlier SUMMARY-NOW REFRESH (`d9dbdd9c`) is covered by it and removed. ACKed to ki.sop.main.
- MSG-62c4932a LOCAL-VERSIONS (Kris, 5 November about 08:20 GMT): ACKed; the Macs run KI tools from their `main` checkouts, not Homebrew releases. Agora already calls `ki` from PATH and assumes no released version; nothing to change.
- MSG-a73179f9 NO-EXTERNAL-POSTING (Kris, 5 November about 19:40 GMT): ACKed; no post of any kind on another owner's repository or service in Kris's name without his express permission for that post; a recommendation to post is a query carrying the exact text. Every Agora brief carries this.
- MSG-79dd4cca ORCA-UPSTREAM (Kris about 21:15 GMT, via household-sol): ACKed; run orca-upstream records Orca #33114/#33115 on KI-AGORA-WRK-001 and proposes a read-only watch for Kris; read-only only.

## 2026-11-05 · SHELL-WATCH (Kris, about 23:00 GMT)

- Kris: "we should keep a close eye on GPUI in the future and say that we can consider moving away from Electron at any point". Taken as: Agora stays on Electron for now (gpui-fit, 22:57 GMT); the shell stays confined to `src/main.ts` so it can be swapped at any time; GPUI is watched, and the move is reconsidered whenever a trigger holds: GPUI gains tray, notification or login-item support or a stable release; Agora's memory use matters (Swift shell first); Linux or Windows rigs (Tauri); or the settings screen or a KIV/Agora window grows into a large always-open view. Each time Agora's window work is planned, a run checks GPUI's current state online first.
- MSG-81782869 KEEP-AWAKE (Kris about 23:50 GMT, via household-terra): ACKed; run keep-awake-capture captures two triage records: holding an idle-sleep assertion while work runs, and checking host settings against Rig, power first.
- keep-awake-capture received: the run held the capture under CAPTURE-GATE and drafted both records; the coordinator captured them as [KI-AGORA-WRK-003](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-003-keep-host-awake-while-work-runs.md) and [KI-AGORA-LVL-001](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-LVL-001-check-host-settings-against-rig.md), areas WRK and LVL. Briefs no longer ask runs to create records; KI-AGORA-WRK-002 was created by a run against the gate and stands.

## 2026-11-06 · MARK (Kris, about 00:05 GMT)

- Kris: "maybe we can take a mark and understand what it is that you're focused on". Mark struck; mark-all-scope received, its six queries copied to discussions (three as DEFAULTS); WAKE-NOTE raised for the two waiting 4 November requests.
- MSG-9556f9a6 AGORA-SCHEDULER (Kris about 00:12 GMT, via household-terra): ACKed; Agora runs the scheduled jobs Rig declares and reports failures and missed runs the same day; PERSONAL-DOTFILES-UE-137 moved here. Run scheduler-draft drafts the record for the coordinator to capture; the design is agreed with Kris before any build, and any job that starts an agent waits on FOCUS-FIT.
- MSG-505228fc INBOX-RENAME (Kris, 6 November, via personal.reg.inbox-terra): ACKed in the renaming package's Inbound (still `personal.reg.assistant-terra` on sol at 00:20 GMT). `krisb/assistant` is `krisb/inbox`; personal.reg.assistant-* become personal.reg.inbox-*. Old ids in apps-agora.local examples and fixtures are updated in the next build slice; sol's checkout keeps its old path until household-sol aligns it.
- scheduler-draft received: the coordinator captured [KI-AGORA-WRK-004](/Users/krisbrown/kis/knowledge-islands/apps-agora.local/docs/roadmap/KI-AGORA-WRK-004-run-the-rigs-scheduled-jobs.md); SCHED-FIRST, SCHED-REPORT, SCHED-FOCUS-HOST, SCHED-PAUSED and SCHED-ONE-RIG copied to discussions; household-terra told.

## 2026-11-06 · Query pass (Kris, about 00:30 GMT)

- FOCUS-FIT, taken as a): Agora may wake threads and runs Kris opened; anything that starts a fresh agent on its own, scheduled or not, on any Mac, waits for Kris's decision through the Enactment Process. This also settles SCHED-FOCUS-HOST as a).
- FOCUS-LIST, taken as a): Focus rewritten: `send` ⭐, `jobs` (scheduled jobs, account switching, keep-awake), `voice`, `identity`, `_emerging`.
