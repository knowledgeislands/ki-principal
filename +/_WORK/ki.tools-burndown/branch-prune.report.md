# [Platform foundations](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/platform-foundations.md) › [tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/tools-burndown.md) › branch-prune

**Run report at 22:27 BST · last mark none**

---

## Done

- Checked the branch content: `origin/paperclip/aligned-20260926/KIS-46-ki-dev-skill-rubric-resolves-the-dev-linked-primary-checkout-never-the-cwd-worktree-si` held one commit, `3a10a702` ("fix(cli): bound rubric publication to the caller's working tree"). Its 286 changed lines across 11 files match `3ec53d54` exactly, and `3ec53d54` is already on `origin/main`. All 11 files exist on main. `git cherry` marked the commit `+` only because `3ec53d54` also contains the [KI-TOOL-CLI-109 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/4aec065e1b23d9c1b5fbbddbef303cbd5ce2f16a/docs/roadmap/KI-TOOL-CLI-109-bound-rubric-publication-root.md) record update and was applied with different surrounding context, so its patch-id differs. No commit was missing from main.
- Deleted the branch on origin with `git push origin --delete` and then ran `fetch --prune`. There was no local branch with that name, so nothing was deleted locally.
- Left `origin/fix/granola-retention-20261014` in place for [KI-TOOL-KI-CLI-128](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-128-granola-retention-safeguards.md).
- Did not touch the tools-ki working tree, index, HEAD or rebase. The other session's rebase is still in progress, with `KI-TOOL-KI-CLI-139` unmerged. Made no commits.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Receiver-owned work: the other session is still rebasing in tools-ki (detached at `3ff05a5e`, with a conflict on [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md)).
- Retained material: this report is uncommitted, as briefed.

## Queries

No outstanding queries.

```text
╭─ run report · 2026-10-17T21:27:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · run branch-prune done   │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · KIS-46 branch deleted   │
│  █  █ █▄▄▄ ▄▄▄█   █    · granola branch kept     │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] nothing running or queued
- [untouched] tools-ki rebase owned by another session
- [uncommitted] this report, as briefed

Resume line: `Resume Fnd: tools-burndown under current ki-pmo and ki-delegation since 2026-10-17T21:27:00Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.`
