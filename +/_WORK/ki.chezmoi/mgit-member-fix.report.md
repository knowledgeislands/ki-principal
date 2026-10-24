# tools-ki › mgit-member-fix

**🤖 → 👤 Handoff to supervisor · Run report at 23:01 BST**

---

## Done

- `ki` now accepts mgit's external members such as `../../.local/share/chezmoi`. The rule matches mgit's: one or more leading `../` segments, then a safe relative path, allowed only for a repository member in a group-free manifest. Each external repository is selected once, even when several workspaces reach it or it is also a local member. A path that resolves back inside its workspace is rejected and the error names the local member to declare instead. Every other unsafe path still gets the existing error. The change is all in `src/core/repository/mgit.ts`, with a new test in `src/tests/cli/repo/targets.test.ts`.
- Commit `1d199a77` `fix(repo): accept mGit external members`, made in a linked worktree and fast-forwarded into primary `main`. Not pushed.
- Gate: typecheck passed, Biome passed, and all 1,827 tests passed with 100% coverage. The commit hooks passed, including the staged audit. The full `ki repo audit --repo .` has one FAIL, ki-engineering DESIGN-2 (the `prepare` script should install `tooling/depcruise`). That FAIL is already on clean `main` before this change and is not part of it.
- Live check: `ki repo roadmap summary` now succeeds in `~/workspaces/personal` and lists chezmoi (`dotfiles`) once. It also still succeeds in `~/workspaces/knowledge-islands`.

## In Progress

Nothing.

## Queries

None. The existing ki-engineering DESIGN-2 audit failure in tools-ki is separate work, if you want it picked up.
