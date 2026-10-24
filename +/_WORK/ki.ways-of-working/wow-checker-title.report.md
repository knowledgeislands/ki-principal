VERDICT: blocked · confidence high - Fix and regression pass; the ki launcher cannot start, preventing required audits and commit.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-checker-title

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 02:05 BST · last mark 23:06 BST**

---

## Done

COORD-2 now reads the registered Project note's front-matter title, with the slug as fallback when no non-empty title exists; both flat notes and folder notes resolve. Its warning names the expected title. Changes are in [coordination.ts](/Users/krisbrown/.local/state/ki/worktrees/ki-agentic-harness/wow-checker-title/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.ts:325).

One [regression test](/Users/krisbrown/.local/state/ki/worktrees/ki-agentic-harness/wow-checker-title/skills/change-management/ki-coordination/scripts/rubric/contexts/coordination.test.ts:532) covers `kb.personal-health`, accepting `Personal > Health > Stocktake`, rejecting the slug-derived name while the title exists, and accepting it after the title is removed; the original checker failed this regression.

Worktree: [/Users/krisbrown/.local/state/ki/worktrees/ki-agentic-harness/wow-checker-title](/Users/krisbrown/.local/state/ki/worktrees/ki-agentic-harness/wow-checker-title); branch: `wow-checker-title`; baseline: `fcc0f3833b9295e3d6b35e603ce4223df3fb93fb`; commit: none, because required audits could not run. The primary checkout was not edited.

Baseline harness tests: passed, 1,431 tests.

Changed harness tests (`bun run test`): passed, 1,432 tests.

Type check (`tsc --noEmit`, local executable): passed.

Biome check: passed with one pre-existing non-null-assertion warning in the test helper.

Git whitespace check: passed; only the two intended files are modified and neither is staged.

Isolated audit setup: blocked before bootstrap completed; `ki` cannot parse merge-conflict markers in [tools-ki events.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/agent/events.ts:668). Required focused `ki-coordination`, `ki-skills` and harness audits are unassessed. No hook was bypassed.

## In Progress

Nothing is running.

Outstanding — no action requested now: the implementation and regression remain uncommitted in the retained worktree on this laptop, pending restored verification tooling and supervisor instruction. Temporary audit state and the temporary dependency link have been removed.

## Queries

### KI-CLI-UNAVAILABLE — Restore the required verification gate

**Context:** The installed `ki` launcher loads the separate tools-ki checkout, where an unresolved merge-conflict marker prevents startup. This blocks the required isolated-home audits and the harness pre-commit gate. The harness change passes tests and type checking, but committing it would bypass the repository's required verification. This run made no change to tools-ki.

**Query:** Should this branch be resumed once the responsible tools-ki work restores a working launcher?

**Options:**

a) (recommended, confidence high - the fix already passes independent checks and the remaining blocker is the required launcher) Restore the launcher through its owning work, then resume this branch, rerun the required checks and commit the two intended paths with the actual model's co-author trailer.

b) Retain this worktree for a later supervisor-owned delivery without resuming this run.

### 🤖 → 👤 Handoff to supervisor · blocked · since 02:05 BST

👤 1 with you · ⛔ 1 blocked

- [with you] KI-CLI-UNAVAILABLE · owner · since 02:05 BST
- [blocked] Required audits and local commit · run/wow-checker-title · since 02:05 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
