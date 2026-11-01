# Brief: sweep-legal-principal (ki.prj.ways-of-working) - move-only sweep

Kris decided on 1 November 2026 (logged in `/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/decisions.md`): TOP-LEVEL-NOW (reports live in `+/_WORK/<id>/reports/`; harness `58e1d128`, ignore exception `c273a1fb`), TOP-LEVEL-SWEEP-DELETE (only each steward deletes reports), TOP-LEVEL-SWEEP-MOVE and SWEEP-SCOPE "All 17" (one move-only run per repository).

Repository: `/Users/krisbrown/kis/legal/legal-principal`.

1. Fetch and fast-forward. Make sure the repository's `.gitignore` re-includes `+/_WORK/*/reports/` (the managed block from `ki-repo`); if not, add the two exception lines `!/+/_WORK/*/reports/` and `!/+/_WORK_REVIEW/*/reports/` straight after the `reports/` rule, in its own commit.
2. For each `+/_WORK/<id>/` folder, list top-level `*.report.md` files. Skip any folder whose work has a live run (`ki agent status`) and say so. Move each report into that folder's `reports/` with `git mv` if tracked, or `mv` then `git add` if untracked. On a name clash in `reports/`, leave both and report it. Delete nothing.
3. Repoint links to each moved report: search the repository for the old path (absolute and relative) and update it to the new one; do not edit the meaning of any text.
4. One commit per work folder, by explicit path, `docs(work): <id> move reports into reports/`. Then add one line to each touched folder's `messages.md`: `- 2026-11-01 · REPORTS-MOVED · Ways of working (ki.prj.ways-of-working): <n> top-level reports moved into reports/ under TOP-LEVEL-SWEEP-MOVE (Kris, 1 Nov); nothing deleted; prune at your next mark.`, in that folder's commit.
5. Push `main` fast-forward only; on a pull that cannot fast-forward, merge `origin/main` in a temporary worktree (never rebase). Never force, never `--no-verify`, never stash, rebase or reset. Other sessions' uncommitted changes outside the reports you move: leave untouched.

Report as your run packet directs: per folder, the count moved, any skipped and why, clashes, links repointed.
