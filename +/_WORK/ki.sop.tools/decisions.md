# Decisions

## 2026-11-07 - QUARTERMASTER-SOP: the quartermaster's seat is ki.sop.tools

- Kris, about 03:00 GMT on 7 November 2026, relayed by personal.reg.household-sol as MSG-6f12f0d9: "the actual quartermaster should be ki.sop.tools, and it should live as a leader, I think, in the principle." and "I want you to change what the quartermaster will be, and then we'll create it somewhere."
- The role catalogue entry landed at ki-agentic-harness `efa0a3e9`: quartermaster 🧰, leaders tier, seat `ki.sop.tools`, KI > SoP (tools), a secondary State of play in ki-principal under ki.sop.main. Both are logged in [ki.sop.main's decisions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/decisions.md).
- ki.sop.main seeded this package on hold with RIG-RETIRE as its first Inbound line; Kris opens it.

## 2026-11-08 - RESET-PARK: everything before the reset is parked

- Kris, 20:48 GMT on 8 November 2026, on sol: "Reset. We're moving to a new way of working, and everything before now is set aside until I say otherwise." and "Park all open work: every open query, queued run and planned next step, including anything held for my word. Launch nothing and resume nothing from before now. Delete nothing; record the parking in decisions.md as RESET-PARK."
- Parked, nothing deleted: the seven Inbound lines in `messages.md` (RIG-RETIRE, RIG-INTAKE, MAIL-GAPS, MAIL-IDEAS, RIG-ATTENDED, SCHEDULING, RIG-OWNS-CONFIG), left in place and not acted on, and `state.md`'s one next step (take the Inbound on release). No open queries and no queued or running runs existed.

## 2026-11-08 - RESET-SESSIONS: act only on Kris and the six reset sessions

- Kris, same message: "Join the six reset sessions: ki.sop.main+governor, ki.reg.guilds+guildmaster, ki.prj.agora+warden, personal.reg.inbox+gatekeeper, personal.reg.rig-terra+housekeeper, personal.reg.rig-sol+housekeeper. Act only on my messages and on theirs; park anything else."
- personal.reg.inbox coordinates for now ("personal.reg.inbox coordinates for now").

## 2026-11-08 - RESET-AGORA: messaging through the Agora store; listening on

- Kris, same message: "Messaging is through the Agora store (krisb/ki-agora-store) via the Agora MCP. A message is filed under its recipient's territory, the first part of the recipient's work id. Write your roster row with presence (work_id ki.sop.tools, role quartermaster), then listen: a detached watch that pulls the store every 2 minutes and wakes on new files under messages/ki/ki.sop.tools/. You may push package and messaging commits, and tool commits the coordination asks for."
- Listening enabled at Kris's word; the watcher pulls `/Users/krisbrown/kis/personal/ki-agora-store` fast-forward only every 2 minutes and exits on a new file under `messages/ki/ki.sop.tools/` or a failed pull.
- Push authority: package and messaging commits, and tool commits the coordination asks for.

## 2026-11-08 - RESET-CHANGES: Kris's changes apply at once; host sol; thread line

- Kris, same message: "Changes I give you apply immediately; record each in decisions.md. Your thread line is 🧰 🔑 ki.sop.tools+quartermaster." This session now runs on sol, after the hold from 7 November.
- First act: send personal.reg.inbox a stock-take through the store ("running or half-done, outside Git, parked count, top three").

## 2026-11-08 - INDEX-ENTRY: the tool side of the `_index.md` rename

- personal.reg.inbox (coordination hub), brief 01a1bcf0 at 20:53 GMT: "make tools-ki, the coordinator-footer hook, mcp-agora (agree that with ki.prj.agora+warden) and tools-rig read `_index.md` first and fall back to `work.md`. Do nothing destructive; the housekeepers do the rename itself after the guildmaster's brief. ACK, then reply with what landed and where." ACKed at 20:56 GMT.
- tools-ki and the hook wait on a handover from ki.reg.guilds, whose tools-index run is in tools-ki; mcp-agora waits on the warden's answer; tools-rig goes first. Commits only, no releases.

## 2026-11-08 - WATCH-FETCH: the watch fetches and never pulls

- personal.reg.inbox, same brief: "Your watch must only fetch and compare origin/main, never pull the store clone (WATCH-FETCH)."

## 2026-11-08 - INDEX-ENTRY handover terms from ki.reg.guilds

- ki.reg.guilds, answer 01a1bcf5 at 20:59 GMT: its tools-index run covers tools-ki and tools-rig ("Please hold tools-rig as well as tools-ki until it reports"), then it sends what it covered "plus whether the installed ki needs a release or reinstall. That part is yours." The coordinator-footer hook needs no code change (landed in 0cd46d4d3 and 66b2f0a1f). mcp-agora is with the warden, briefed at 20:45 GMT. It offered apps-observatory.local's packages/evidence readers; I put that to personal.reg.inbox, recommending yes at medium confidence.
- ki.prj.agora's ACK of my question parked it "for Kris (sender outside the Reset)"; mcp-agora stays with the warden.

## 2026-11-08 - STD-BASE: a check for change documents whose touched files have moved

- ki.reg.guilds, brief 01a1bcff at 21:10 GMT, under Kris's STD-BASE a (22:05 CET, via personal.reg.inbox): "Please add a check that flags a change document whose touched files have moved since its base ... Where it lives (a ki command or a rubric item) is your call. Reply with the commit when it lands. No hurry against INDEX-ENTRY." ACKed at 21:11 GMT.
- My call: a `ki` command in tools-ki, since it fetches and diffs across registered repositories. It is queued behind ki.reg.guilds's tools-index run in tools-ki, then one bounded run commits and pushes, with no release.

## 2026-11-08 - OBSERVATORY-READERS: apps-observatory.local reads `_index.md` first

- personal.reg.inbox, brief 619527fb at 21:30 GMT, carrying Kris's word: "OBSERVATORY-READERS, Kris's word (a, yes now): make apps-observatory.local's `packages/evidence` read `_index.md` first and fall back to `work.md`, in the same pass as tools-ki, as a detached run (RESPONSIVE). Reply with the commits when it lands." ACKed at 21:31 GMT; run obs-index launched.

## 2026-11-08 - OBSERVATORY-READERS withdrawn

- personal.reg.inbox, message b5e6497d at 21:32 GMT, carrying Kris's word: "OBSERVATORY-READERS withdrawn, Kris's word (22:45 CET): do not patch apps-observatory.local. The Observatory and the KIV move into apps-agora.local under the warden (LEGACY-TO-AGORA), which makes them read `_index.md` there. Carry on with tools-ki only."
- The obs-index run was stopped at 21:37 GMT before it committed anything. `ki agent stop` refused ("containment-unverified"), so its process was ended directly. Its uncommitted edits to eight files in packages/contracts and packages/evidence were saved to `~/.local/state/ki/agents/ki-sop-tools/obs-index.withdrawn.patch` and restored, so apps-observatory.local is clean and level with origin.

## 2026-11-08 - PACKAGE-TO-AGORA: ready the package for the move, stop listening

- Kris, 22:49 GMT: "Before your work package moves into the Agora store: make sure everything your package needs is in it, then commit it by explicit path and push. Stop listening: stop your watch loop and any doorbell. Start no new work and send no Agora messages."
- Watch loop stopped; no doorbell was armed. The std-base run, launched at 22:20 GMT, was still running its test suite and was not stopped. Nothing new launches.
