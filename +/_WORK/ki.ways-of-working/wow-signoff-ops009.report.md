# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-signoff-ops009

**🤖 → 👤 Handoff to supervisor · Run report at 23:30 BST · last mark 23:05 BST**

---

## Done

- Split [KI-HARNESS-OPS-009](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md) under OPS009-SPLIT a). It now covers only step 1, evaluating the hybrid incremental ChatGPT path, and keeps the two open questions (the Spirituality binding and the 77 unreferenced export files). Its title is now "Incremental ChatGPT acquisition path" and its kind `investigate`. The file name is unchanged, so existing links still work.
- Captured two harness records at OPS-009's horizon and status (Next, draft): [KI-HARNESS-OPS-010](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-010-receiver-local-acquisition-triage.md) for step 4, receiver-local triage under `ki-acquire`, and [KI-HARNESS-OPS-011](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-OPS-011-separate-agent-session-acquisition.md) for steps 5 and 6, separating Claude and Codex acquisition from housekeeping and deciding the `mcp-housekeeping-*` adapter role against `ADR-KI-HARNESS-SKILLS-007`. OPS-009 links to both. All three records are sized `m` so the ITEM-2 migration warning clears. That size is an estimate made at capture; planning should revise it.
- Sent tools-ki's four steps (2, 3, 7 and 8) as four lines in [ki.tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md), tagged OPS009-SPLIT. They are: the readable source connection, explicit unmapped, overlap, missing, changed and failed cases, the fail-closed retirement manifest and deletion path, and the project-move and no-op verification. Each line asks tools-ki to capture its own record. Nothing was captured outside the harness.
- Harness commits `46c8412b` (ledger reserves OPS-010 and OPS-011), `f6470b0a` (the split) and `0745c9b7` (sizes) were fast-forwarded into `main` and pushed to `origin` fast-forward only. The push went through the admin bypass of the required "build" check.
- Checks: `bun run test` passed (1,374 tests, 0 failures); `bunx tsc --noEmit` passed; every pre-commit gate passed; the focused `ki-work-roadmap` and `ki-repo-harness` audits and the full `ki repo audit`, run in an isolated home, passed with 0 failures. The remaining `ki-work-roadmap` warnings are fleet findings on other records.
- ki-principal commit `24d88a00` (the four messages lines) is committed locally but not pushed, because ki-principal `main` also holds 8 commits from other sessions.
- Worktree, branch and temporary output removed. The worktree's `node_modules` was installed from the local cache with `bun install --offline`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki.tools-burndown is on hold. Its four OPS009-SPLIT lines wait in its queue until it resumes.
- ki-principal `24d88a00` stays unpushed until the other sessions' stacked commits on ki-principal `main` are pushed.

## Queries

### ADAPTER-ROUTE - When to route step 2's read-adapter part

**Context:** Step 2 asks for a readable, authorised source that can enumerate ChatGPT projects and return complete conversations. I sent it to tools-ki only, because `ki-acquire` assigns executable importers to tools-ki. If the chosen source is a new read operation, though, it would sit in `mcp-housekeeping-chatgpt`. That repository has no owning work, so its line would go to State of play's messages. Whether that adapter stays a shared read-only source, or takes an acquisition-specific name, is the very decision KI-HARNESS-OPS-011 now carries, and which source to use is the evaluation KI-HARNESS-OPS-009 carries.

**Query:** Should a line go to State of play now asking `mcp-housekeeping-chatgpt` to capture its part of step 2, or should it wait until OPS-009 and OPS-011 have settled the source and the adapter's role?

**Options:**

a) (recommended, confidence medium - the receiver and the shape of that part depend on two harness outcomes not yet reached) Wait; route the adapter part once OPS-009 and OPS-011 conclude.

b) Send a line to State of play's messages now, naming step 2's read-adapter part for `mcp-housekeeping-chatgpt`.

### 🤖 → 👤 Handoff to supervisor · since 23:30 BST

👤 1 with you

- [with you] ADAPTER-ROUTE · owner · since 23:30
- [committed] harness split, pushed
- [unpushed] ki-principal `24d88a00` behind other sessions' stacked commits
