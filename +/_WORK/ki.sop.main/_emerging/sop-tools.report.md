# [Knowledge Islands](/Users/krisbrown/kis/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › sop-tools

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 03:17 GMT · last mark 00:03 GMT**

---

## Done

- Drafted the five-file package [ki.sop.tools](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.tools/work.md) in ki-principal, modelled on ki.sop.main as no secondary State of play exists in the estate: `work.md` (`role: quartermaster`, `level: territory`, `parent: ki.sop.main`, title KI > SoP (tools), routing description, goals and scope from the catalogue row), `state.md` (`on-hold`, `paused`, release "when Kris opens this work", `workers: []`), `discussions.md` (empty), `decisions.md` (one QUARTERMASTER-SOP entry citing Kris's words and harness `efa0a3e9`) and `messages.md`; `rumdl check` passes. **Left uncommitted**: see the query below.
- Queued RIG-RETIRE as the first Inbound line. No sent RIG-RETIRE line exists anywhere in the estate (only decisions entries in household-sol, ki.sop.main and ki.reg.guilds), so the brief's fallback text is used: `- 2026-11-07 · RIG-RETIRE · from Personal > Household > sol (personal.reg.household-sol) · Rig cannot retire a job that leaves a Mac's profile; first item for the quartermaster, per QUARTERMASTER-SOP`.
- Not done, because of the block: registration in ki.sop.main's `covers`, the opener check, the SOP-TOOLS-READY line to household-sol, and every commit and push. No file outside the new package was touched.

## In Progress

Nothing is running. The drafted package sits untracked at `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.tools/`; until it is committed or removed, `ki work status` and `ki agent prompts` in ki-principal print one warning for it and do not list it.

Outstanding - no action requested now:

- `ki agent prompts` finds threads by reading every `+/_WORK/*/work.md` itself; there is no separate registration step, so a valid package is listed as a secondary under ki.sop.main without any other edit.
- Brief step 4 asked to add `ki.sop.tools` to ki.sop.main's `covers`. `ki` refuses that: a State of play's `covers` may not name a secondary State of play (`tools-ki/src/core/work/status.ts`, read from code, not tried, so ki.sop.main was not put at risk), and the standard keeps the main's `covers` for Project, regular and ad hoc work. The secondary's own `parent: ki.sop.main` is the link, so that edit should be dropped, not retried.

## Queries

### SOP-TOOLS-COVERS - What the quartermaster's State of play covers

**Context:** Kris set the quartermaster's seat as `ki.sop.tools`, a secondary State of play under ki.sop.main (QUARTERMASTER-SOP, 7 November 2026). The standard and the `ki` tool both require a secondary State of play to list at least one piece of work it coordinates in its `covers` field; with none, `ki` rejects the package ("covers must list the work ids this State of play coordinates") and it does not appear among the territory's openers. The obvious candidate, [ki.prj.tools-burndown](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/work.md), is part of the open question with Kris about moving tools-burndown, the Rig intake and the mail backlog, which this run was told not to settle. The package is drafted and checked, waiting only on this field.

**Query:** Should ki.sop.tools cover ki.prj.tools-burndown now so that it is valid, or should the tooling first be changed to allow a State of play that covers no work?

**Options:**

a) (recommended, confidence medium - a quartermaster coordinating the tools Project is the natural fit and is a one-line change, but it settles part of the open move question and has not had a blind review) Give ki.sop.tools `covers: [ki.prj.tools-burndown]` and change that Project's `parent` to ki.sop.tools in the same commit, then commit the package, check the opener and tell household-sol.

b) Ask ki.reg.guilds and tools-ki to allow a secondary State of play with no covered work (a seat whose remit is tools rather than packages), and commit the package once that lands.

c) Remove the draft and create the package later, when Kris settles the tools-burndown move.

### 🤖 → 👤 Handoff to supervisor · blocked · at 03:17 GMT

👤 1 with you

- [with you] SOP-TOOLS-COVERS · owner · since 03:17

🧵 ki.sop.main
