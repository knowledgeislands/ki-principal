# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-repair-gov225

**🤖 → 👤 Handoff to supervisor · Run report at 23:58 BST · last mark 23:05 BST**

---

## Done

[KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) now has `baseline_ref: 76b6e5c51cee6c8a7f34c683b497ea1dc1fad817`, fixed from Git evidence alone. The earlier acceptance run's awaiting-review edit, with Kris's GOV225-CLOSE a) agreement and its review packet, came across unchanged except for the four lines this repair rewrote.

The evidence is three independent lines. First, the session log of the implementing run (`hooks/roll-standards`) shows it created its worktree from `main` at 03:37:22Z and did not reset, check out or rebase before its first commit. Second, the primary checkout's `HEAD` reflog shows `main` at `76b6e5c5` from 02:54:49Z to 03:39:42Z. Third, the original pre-rebase implementation commit, `ac7d5476`, has parent `76b6e5c5`. The current parent of `cea02aa5`, `ba4055ef`, came later and is a rebase destination, not the baseline.

Commit `35ba5120` (`docs(roadmap): repair KI-HARNESS-GOV-225's baseline and await review`) is fast-forwarded into primary `main` and pushed to `origin` fast-forward only, through the admin bypass PRFLOW allows. `main` and `origin/main` were level after the push.

Tests: passed, 1,385 tests with zero failures.

TypeScript: passed.

Focused isolated-home audits of `ki-work-roadmap`, `ki-repo-harness`, `ki-authoring` and `ki-repo`: no failures. Their warnings are fleet findings about other records and the unregistered ki-principal checkout.

Pre-commit hook: passed.

Old worktree `wow-accept-gov225` removed with `git worktree remove` and branch `run/wow-accept-gov225` deleted with `git branch -d`. I first confirmed that its uncommitted edit was fully contained in `35ba5120`, then discarded that copy so the plain remove would work. I also removed my own repair worktree and branch, now merged. No record was accepted or pruned, and no new record was created.

Primary checkout disturbed after my work, not by it. At 23:55:15 BST, test fixtures from the concurrent `hooks/hooks-tools` run wrote into the harness's shared `.git`. Its status line reads: "test fixtures inherited the rebase Git environment". The local config now has `core.bare=true` and `user.name=Hook Test`, and local `main` has moved to fixture commits headed by `41709f93` ("test: second-review.ts"). `35ba5120` remains an ancestor of that `main` and was already on `origin` before the leak. I changed nothing there: the hooks-tools run is recovering it.

## In Progress

Nothing of mine is running. The `hooks/hooks-tools` run (worktree `/Users/krisbrown/.local/state/ki/agents/hooks/worktrees/ki-agentic-harness`, branch `run/hooks-tools`) holds recovery of the harness primary checkout.

Outstanding - no action requested now:

- The record stays awaiting review. A fresh independent acceptance run is next, under GOV225-CLOSE a) and the coordinator's 23:42 BST entry. It should wait until the primary checkout is restored.
- Before any prune, the inbound references in ki-principal must be pinned to the record's final revision. That includes the ki.tools-burndown hooks-standard design and the ways-of-working review material.
- The pre-rebase commit `ac7d5476` is unreachable, so a future `git gc` may remove it. The record also cites the reflog and the session log, which do not depend on it.
- The `hooks-tools` run has its own harness worktree, `run/hooks-tools`, which does not touch this record. I left it alone.

## Queries

### HARNESS-PRIMARY-LEAK - hold harness work until the primary checkout is restored

**Context:** At 23:55:15 BST, after this run had pushed `35ba5120`, fixtures from the `hooks/hooks-tools` run's tests wrote into the shared harness `.git`. Local config now has `core.bare=true` and the test identity `Hook Test <test@example.invalid>`, and local `main` points at fixture commits headed by `41709f93`. Any harness commit, merge or acceptance made now would carry the fixture identity or the fixture history. The local `origin/main` ref still stands at `35ba5120`. The hooks-tools run reports it is inspecting the recorded metadata for recovery.

**Query:** Should the fresh KI-HARNESS-GOV-225 acceptance, and every other harness run, wait until the hooks-tools run restores the primary checkout and the restore is verified?

**Options:**

a) (recommended, confidence high - holding is non-destructive, the repair commit is safe on origin, and the run that caused the leak has the context to undo it) Hold harness launches until hooks-tools reports `core.bare=false`, the test identity removed and local `main` back at `origin/main`, then launch the fresh acceptance.

b) Launch a dedicated recovery run for the harness primary checkout now, coordinated with hooks-tools so the two do not both write.

### 🤖 → 👤 Handoff to supervisor · since 23:58 BST

👤 1 with you · ⛔ 1 blocked · 📥 1 to accept

- [with you] HARNESS-PRIMARY-LEAK · owner · since 23:58
- [blocked] KI-HARNESS-GOV-225 fresh acceptance · harness primary checkout · since 23:58
- [committed] ki-agentic-harness `35ba5120`, pushed
