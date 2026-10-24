# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › harness-standards

**🤖 → 👤 Handoff to supervisor · Run report at 06:20 BST · last mark 05:20 BST**

---

## Done

- WORKTREE-INTEGRATE a): `3f327991 feat(ki-git,ki-delegation): let a worktree run land its own work` adds the `ki-git` "Worktree-run self-integration" subsection and the `ki-delegation` Integration bullet. A run may fast-forward its own branch into local primary `main` once gates pass on the rebased range, with one writer at a time and review before acceptance. A run that cannot fast-forward keeps its worktree and reports it stranded (F1).
- WORKTREE-START a): the same commit adds the `ki-delegation` Worktree trial bullet. Code repositories start now, and Knowledge Islands Principal joins once the registry recognises linked worktrees (F5). `da8e2a49 feat(ki-coordination): sweep worktrees at each mark; admit rendered banner glyphs` adds the `ki-coordination` Worktree sweep (F4). It reports only what it finds and removes nothing.
- WORKTREE-START handoffs: `97630d12 docs(work): send the worktree-flow fixes to ki.tools-burndown and ki.observatory` in ki-principal. It adds one WORKTREE-FIXES line to ki.tools-burndown `messages.md` covering F2, F3, F5 and F6, and one WORKTREE-VISIBLE line to ki.observatory `messages.md` covering F3's Observatory half.
- WORKTREE-AUDIT a): `3f327991` adds the isolated-home recipe with `ki repo repair` first to `AGENTS.md` Verification and to the `ki-delegation` Worktree audit bullet. Validation: 0 FAIL under CI's pinned `ki` v0.11.3 and under the local 0.12.0. Without the recipe the audit fails, and the real home and registry were untouched.
- BANNER-GLYPHS a): `da8e2a49` adds the Rendered glyphs paragraph to the `ki-coordination` standard's Banner section. The emoji stay the written notation, and a rendered surface may use the `@knowledgeislands/icons` line glyphs with the state's words beside them. `SKILL.md` does not restate the notation, so it was left unchanged.
- MATURITY-DECLINE a): `e68d3368 docs(roadmap): settle KI-HARNESS-GOV-223's decline rule and mark it Ready` updates [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md) with a Decline rule section carrying the five conditions. The standard step and Verify line now require the decline rule's wording and the four reader cases. The readiness checks passed and the record is Ready.
- Integration: the three harness commits were fast-forwarded into local `main` (now `e68d3368`). The worktree was removed, `run/harness-standards` deleted and the worktrees pruned. The temporary tools-ki validation worktree was removed too.
- Generated files: `ki dev skill generate ki-coordination --write` regenerated `output-styles/ki-coordinator.md` and nothing else. `ki dev skill rubric` passed for ki-coordination, ki-delegation, ki-git and ki-work-roadmap.
- `bun run test`: 1343 pass, 0 fail on the final head.
- `bunx tsc --noEmit`: passed.
- `rumdl check` on the whole repository: 532 files, no issues.
- Full `ki repo audit` in an isolated home: 0 FAIL, 77 WARN. A PORT-1 failure in the first draft of the recipe was fixed before commit.
- The pre-commit hooks, including the focused audits, passed on every commit, with no `--no-verify`.
- Pushes: none. Harness `origin/main..main` also holds `ae8a1323` (this programme) and two commits from another session, `10897281 chore(hooks): adopt the canonical ki-repo-harness package hooks` and `cea02aa5 feat(hooks)!: compose one canonical hook per shape and compare it exactly`. In ki-principal, other sessions' commits sit between this run's (for example `4737fe20` and `1681df1a`). Because the brief allows pushing only this programme's commits, neither repository was pushed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The harness half of F6, extending the `ki-git` GREEN-MAIN sentence to tools-ki, is not done. The WORKTREE-FIXES line names it as a ki.ways-of-working harness edit.
- The worktree-flow design note `+/_WORK/ki.ways-of-working/design/worktree-flow.md` can graduate now that the fix lines are sent; pruning it is the coordinator's move.
- WORKTREE-INTEGRATE, WORKTREE-START, WORKTREE-AUDIT, BANNER-GLYPHS and MATURITY-DECLINE are answered and applied, so the coordinator can clear them from ki.ways-of-working `queries.md`.
- The harness and ki-principal stacks are unpushed for the reason given in Done.

## Queries

No outstanding queries.
