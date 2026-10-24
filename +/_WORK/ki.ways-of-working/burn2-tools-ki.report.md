# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › burn2-tools-ki

**🤖 → 👤 Handoff to supervisor · Run report at 06:57 BST · last mark 05:20 BST**

---

## Done

- [KI-TOOL-KI-CLI-165](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md): in-progress → awaiting-review. The four correction bullets moved from the extra `Independent-review corrections` heading into Change Summary, so the Review packet now has exactly the six required headings; no evidence dropped, no code changed. Commit `0a200642`. Pushed: yes.
- [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md): in-progress → awaiting-review. `baseline_ref` was a mistyped full SHA: its first eight characters match `0e48ca277d7e784affb7806d646df313345742c4`, the sole parent of `df1c24ed`, the record's first delivery commit. `baseline_ref` and Delivered now name it in full, and Delivered names both delivery commits (`df1c24ed`, `a14a328d`). The three provisional choices are left as they are, with Kris under FOOTER-PROVISIONALS. Commit `0a200642` (shared with KI-TOOL-KI-CLI-165). Pushed: yes.
- Remaining open records, all left unchanged, none workable without Kris:
  - [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md): on hold until 16 November.
  - [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md): SRC-PLACEMENT is parked for Kris, and the work needs Chrome-cookie credentials and the HNR Project.
  - [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md): its dependencies have landed, but where the mechanical CLEAN checks live (harness catalogue or tools-ki) is still undecided.
  - [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md): blocked on KI-HARNESS-GOV-199, which is still in progress.
  - [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md) and [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md): Soon; both wait for State of play to confirm the form it wants to read.
  - [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md): CI-EVIDENCE a) needs a connected session to read the CI runs first.
  - [KI-TOOL-KI-CLI-157](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-157-validator-parity.md): under VALIDATOR-HOME a), the shared table is built in ki-agentic-harness first and then vendored here.
  - [KI-TOOL-KI-CLI-159](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md): KI-HARNESS-GOV-223 is Ready but not yet delivered.
- Checks: rumdl passed; commit hooks ran with no bypass, and only the two record paths were committed; full `ki repo audit` on the integrated primary checkout passed with zero failures and the same six warnings as before. Coverage, TypeScript and Biome were not re-run, because the change touches Markdown records only.
- Integration: worked in a worktree on `run/burn2-tools-ki`, fast-forwarded it into local `main` (WORKTREE-INTEGRATE), then removed the worktree and the branch.
- Publication: after fetch and pull with rebase, tools-ki `main` was pushed fast-forward to `origin`. All eight commits pushed were from tonight's programme, 05:40 to 06:54 BST: `f2fdf227`, `75427fa2`, `a14a328d`, `907a627e`, `0c107a9f`, `bc563d56`, `0a200642`, and the concurrent prune-links commit `a37f3151` (pruned KI-TOOL-KI-CLI-151). This clears the tools-ki half of accept2-tools-ki's pending publication. `main` is now level with `origin` on sol.local.
- CAPTURE-GATE: no records created and no new follow-ups, so no `messages.md` line was needed. HOOK-GUARD: no `ki repo conform` was run.

## In Progress

Nothing is running.

- Both records are with an acceptance reviewer. KI-TOOL-KI-CLI-134 also needs Kris's FOOTER-PROVISIONALS answer, which is already in ki.ways-of-working's queries.
- A prune-links session was committing in tools-ki at the same time as this run, despite "nobody else is working tonight". Its commit fast-forwarded cleanly and was pushed with the others.
- ki-principal's earlier unpushed commits are unchanged; this run made no ki-principal commit.

## Queries

No queries.
