# [KI > SoP](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › agora-project

**🤖 → 👤 Handoff to supervisor · Run report at 22:53 GMT · last mark 29 Oct 16:17 GMT**

---

## Done

- Opened Project `ki.prj.agora` (commit `46a6ddb4`, ki-principal). Its [Project note](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agora.md) sits under theme Techne, has lifecycle `planned` and points at the repository `knowledgeislands/apps-agora.local`. It also has an entry in the [Projects](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/Projects.md) registry.
- Agora is related to [agent-host](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/agent-host.md), not folded into it, and both notes now say so. The reasons:
  - agent-host owns the `vega` recipe inside the two Techne products and is on hold.
  - Agora is a live app in its own repository that runs on every rig, workstations included.
  - Folding would put live work under an on-hold host recipe.
- The Techne Programme Focus relation is written into the Project note. Agora is the host agent, the always-on presence a host needs. It lives outside `ki-techne-harness` and `tools-techne`, and it runs on the Mac Studio within the Focus's bounds.
- Created the five-file package [`+/_WORK/ki.prj.agora/`](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md). It is On hold, with reason `paused` and release `when Kris opens this Project work`.
  - [work.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) carries the goals and scope, plus focus areas `_emerging`, `send`, `voice`, `jobs` and `identity`.
  - [messages.md](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/messages.md) carries three IMPORTANT lines: the hand-over (design note `host-agent.md` and the reports beside it, pinned to krisb/assistant `5f2655d9`); the four records KI-AGORA-APP-001, KI-AGORA-NET-001, KI-AGORA-TRY-001 and KI-AGORA-WRK-001; and the four open questions BCAST-THREADS, BCAST-AUTHORITY, AGORA-COUNT-PLACE and WORK-ID-TRAILER, for its first Summary.
  - It also carries the five next-work lines: KIV-SEND, ORCA-WAKE, VOICE-BARD, AGORA-JOBS and AGORA-DESIGNER. An AGORA-INSTALL line records that the households install and update Agora under AGORA-INSTALL-GRANT, and a FOCUS-FIT line covers the query below.
- Added `ki.prj.agora` to `ki.sop.main/work.md` `covers`. Removed the AGORA-PROJECT and GRANOLA-HARNESS lines from [ki.sop.main messages](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/messages.md). The commit names both: GRANOLA-HARNESS is in hand by run granola-property.
- Replied to personal.reg.assistant-sol with the package id and opener (commit `cfd1bcbe`, krisb/assistant). The reply went through a temporary worktree from `origin/main`, which has since been removed.
- Repository audit: no findings on the new package, Project note or registry edits. The ki-principal-wide FAIL comes from findings that were already there, in other packages and in older `ki.sop.main` message lines and its `state.md`.
- Work-package audit: `ki.prj.agora` passes. The one fault it raised, the sender form in a message line, was fixed before the commit.

The opener, from `ki agent prompts knowledge-islands`:

```text
# KI > Techne > Agora · ki.prj.agora · Project work under ki.sop.main · on-hold

Bootstrap as ki.prj.agora Project work under ki-coordination.
Role: coordinator only. The coordinator never does substantive work itself; every unit of work goes to a detached background agent; an owner message never pre-empts work in flight. Dispatch, decide with me, report; stay responsive.
Label: KI > Techne > Agora. Work package: +/_WORK/ki.prj.agora/ in ki-principal.
Project: agora; work only this Project's records.
Background agents: run substantive work through `ki agent` in run `ki-prj-agora`; stay responsive.
Steering: my messages steer; stop or abort only when I expressly say so, naming the work.
First step: follow the Bootstrap in ki-coordination, then give the full re-bootstrap report.
```

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `ki.prj.agora` stays On hold until Kris opens it with the opener above.
- Once it opens, it should confirm the take-over to personal.reg.assistant-sol, so that assistant-sol can close its `agora` focus.

## Queries

### FOCUS-FIT - Whether Agora waking workers fits the Techne focus

**Context:** The [Techne Programme Focus](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md) lets agents run on the Mac Studio and `vega` only in sessions the binding owner opens, with no unattended or scheduled agents. Agora is filed under theme Techne. It can wake workers itself: it can start a fresh background run (`ki agent launch`) from a standing brief when a message arrives. The policy strictly governs only the two Techne products, and Agora lives in neither, but it runs on the Mac Studio. This question is also seeded as the FOCUS-FIT line in the new package. It has not been through a blind review.

**Query:** Should Agora starting runs on its own on the Mac Studio, and later `vega`, count as inside the Focus, or does it need an Enactment decision first?

**Options:**

a) (recommended, confidence medium - waking a thread Kris already opened stays within "sessions the binding owner opens", while starting a new run from a standing brief is the unattended case the Focus keeps as an idea) Treat waking threads and live runs Kris opened as inside the Focus. Treat Agora starting new runs from standing briefs on the Mac Studio or `vega` as needing Kris's Enactment decision, raised in the Project's first Summary.

b) Treat Agora as outside the Focus altogether, because it lives in its own repository, and record that on the Project note.

c) Bring Agora inside the Focus explicitly by amending the policy through the Enactment Process now.

### 🤖 → 👤 Handoff to supervisor · since 22:53 GMT

👤 1 with you

- [with you] FOCUS-FIT · owner · since 22:53

🧵 ki.sop.main
