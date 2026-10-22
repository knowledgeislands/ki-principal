# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-impl-review-2

**🤖 → 👤 Handoff to supervisor · Run report at 18:30 BST · last mark 14:35 BST**

---

## Done

Verdict: CHANGES NEEDED

This is an independent review of tools-ki commits d6df59d9 and cb165c20 against the [agent control contract](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md), first stage. The shape is right: every native capability is disabled rather than faked, there is no wake path and no SIGKILL, `ki agent reconcile` is untouched, and no lock is ever stolen by age or PID. However, the new per-run control lock regresses the role-free path, and a leftover lock has no recovery route. Line numbers refer to cb165c20.

Findings:

1. Blocking: the busy lock kills hold and dispatch processes, which regresses the role-free path. Lines: `src/core/agent/control-store.ts:320` (about 2 s of retries, then `control-transaction-busy`) and `src/core/agent/runs.ts:828-829` (each 30 s hold wake takes the transaction). Any transaction longer than about 2 s makes the role-free `--wait-for` hold process and the dispatcher exit 1. Long transactions are normal: a worktree launch keeps the lock through `git worktree add` and the node_modules copy (`runs.ts:409`), and a future stop would keep it through up to 120 s of grace. In a probe, a launch with `control.lock` present exited 1 with `control-transaction-busy`. Before this change there was no lock. Fix: never hold the transaction across long effects or the grace sleep. Journal the intent, release the lock, perform the effect, then reacquire to record what was observed. Holds and dispatch should also retry on busy rather than exit.
2. Blocking: a leftover lock wedges the run permanently. `control-store.ts:311-345` removes the lock only in `finally`, so an interrupt that re-raises SIGINT or a crash leaves `control.lock` in place. After that, role-free `launch`, `queue` and `dispatch`, and also `stop`, `dequeue` and `recover resolve`, all refuse indefinitely. The error message cites "verified local recovery", but no such route is implemented or documented. I confirmed this by probe. Fix: write a holder identity (token, attempt, birth identity) into the lock and add an explicit, documented recovery that releases the lock only after verifying that holder is gone. Do not steal by age or PID. Also release the lock on interrupt.
3. Blocking for the role path, latent today: a refusal after the claim wedges the queue. `runs.ts:1350` marks the entry `claimed` and journals a spawn intent; `runs.ts:1383` then rethrows a role refusal from `launchAgent`. In a probe, I queued `--role build`, launched the same name directly, then dispatched. The definite pre-spawn refusal ("prior scope is not verified empty and fenced") was replayed as an uncertain spawn and the entry became `unconfirmed`. From then on, every dispatch reports `claim-unconfirmed`, dequeue exits 1 (`controls.ts:341`), and `recover resolve` cannot prove anything because the adapter never saw the operation. Roles are dormant on the host, so this only bites once launch evidence exists. Fix: when the refusal is known before the adapter runs, record a not-started receipt and return the entry to `queued`, or move the claim and intent to just before the spawn.
4. Advisory: role-free requests silently ignore `--authority` and `--acceptance` (`src/core/agent/selection.ts`, `resolveSelection`). A probe with `/nonexistent` paths exited 0. Fix: refuse `--acceptance` without `--role accept`, and refuse or record `--authority` on role-free requests.
5. Advisory: lower roles accept elevated footers. `selection.ts:299` constrains only accept, prune and release. `--role review --rules release --authority <file>` produced no refusals, although the contract says an elevated footer cannot turn a review into an implementation run. Fix: refuse footers above the role's ceiling for review (and plan or mechanical where the contract caps them), or require a separately cited authority.
6. Advisory: the `claim-unconfirmed` receipt from dequeue omits the recovery command. At `controls.ts:339-341`, only `already-started` adds a next command. Fix: add `ki agent recover inspect <run> --operation <id>`, as the contract specifies.
7. Advisory: text receipts omit the effective selection. `src/commands/agent/index.ts` (launch and queue text paths) shows role, footer, profile and refusals only with `--json` or `--dry-run`. Fix: print the effective selection in the text receipt.
8. Advisory: the compatibility proofs are not durable regression tests. The help test in `src/tests/cli/agent-control.test.ts` does not compare against the baseline for runs literally named `inspect` or `resolve`. The role-free `--rules` test (`agent-control.test.ts:2521`) checks the prompt and selection, but not baseline receipts and side effects. The brief's external baseline comparisons passed, but nothing in the suite guards them. Fix: add golden-baseline cases for both.
9. Advisory, minor: `inspectRecovery` crashes with a raw error when `control.journal.jsonl` is missing (`controls.ts:361`). Fix: return a typed refusal. Separately, `verifyWorkHome`'s `^id:` match at `control-store.ts:245` accepts any line in `work.md`. Fix: confine the match to the frontmatter.

Contract checks:

1. Attempt identity is immutable: there is a fresh token and scope per attempt, receipts are written with `wx`, and the journal is append-only. The `.launch.json` and history projections are mutable, which is acceptable because they derive from the journal.
2. Containment refusal and stop: met in a disabled form. `hostAgentProcesses` has no control adapter, so stop always returns `containment-unverified`.
3. Dequeue: tombstones and the claim journal are present, but see findings 3 and 6.
4. Spawn reconciliation: replay fences unfinished spawns as `unconfirmed`, and `recover resolve` returns `reconciliation-unconfirmed` without an adapter. `recover` is a separate namespace from `reconcile`.
5. Launch defaults: met. Every role is `profile-dormant` without evidence, and accept refuses with `acceptance-contract-unavailable`.
6. No wake: met.
7. Events: `stopped` and `dequeued` are deduplicated by operation and rebuilt from operations.

Check results:

1. Typecheck in a scratch clone at cb165c20: passed.
2. Targeted agent tests: 310 of 310 passed.
3. Full suite in scratch: 1736 passed and 2 failed. The 2 failures are in `src/tests/boundaries.test.ts` because depcruise is not installed in the clone; this is an environment artefact, and I did not install it.
4. Probes P1-P5 confirmed findings 1-5.
5. Coverage caveat: the tests use an injected mock adapter, so they show the contract's logic but no native containment or launch capability. That matches the decision to keep those capabilities disabled.

## In Progress

Nothing is running. The scratch clone and probe file remain in `/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-day-impl-review-2/`. The brief forbids deletion, so that folder needs clearing before `ki agent close`.

## Queries

**Context:** Finding 3 only affects role launches, and every role is dormant on the host until launch evidence exists. **Query:** Should finding 3 block this stage or be fixed before the first profile is enabled? **Options:** a) (recommended, confidence medium - it corrupts queue state permanently, but nothing can reach it today) Treat it as a gate for enabling any profile, tracked with the build that adds launch evidence. b) Block this stage on it along with findings 1 and 2.

**Context:** The contract says an elevated footer cannot make a review into an implementation run, but it does not list each role's footer ceiling. **Query:** What footer ceiling should review, plan, build and mechanical roles have? **Options:** a) (recommended, confidence medium - this follows the contract's wording most closely) Review and plan are capped at `none` or `local`, build and mechanical at `push`, with prune and release reserved for their own roles. b) Leave the footer unconstrained and rely on the cited authority file.
