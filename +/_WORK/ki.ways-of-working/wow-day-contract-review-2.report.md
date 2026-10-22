# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-contract-review-2

**🤖 → 👤 Handoff to supervisor · Run report at 14:48 BST · last mark not read (state.md out of scope)**

---

## Done

- Reviewed [agent-control-contract.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/agent-control-contract.md) against `ki agent` help, the ki-delegation footers and tiers, and tools-ki source; the draft's current-gap claims match the source. No change, commit or remote call.
- Verdict: return named parts for revision first: ACCEPT-AUTHORITY (the accept role's footer), the reconciliation path in dequeue and wake, stop's descendant containment, and BUILD-ORDER (wake split out). STOP-POLICY's grace and no-kill, QUEUE-CANCEL, the WAKE-BOUNDARY rules, ROLE-PINS with gated pins, and precedence are sound as written.
- Confidence: high. The accept-to-prune mapping and the missing reconcile path are concrete defects, not matters of taste.
- Rationale:
  1. Safety: accept maps to the prune footer, which carries push and deletion of records. Because the CLI refuses unless the cited decision covers both, every acceptance would force the owner to grant deletion it never needs. Map accept to the none footer (push only when cited) plus the task's acceptance override.
  2. Safety: every footer says "Never accept work records", and the tier table says no footer authorises acceptance. The brief-over-footer precedence Kris set on 2026-10-17 covers push only. The Harness wording must land before any `--role accept` launch, as a gate, not as a later follow-up.
  3. Correctness: a crash around spawn in dequeue ("unconfirmed claim") and in wake ("delivery-unconfirmed") blocks work until "reconciled", but no reconcile command, evidence rule or owner path is defined. The no-process-search rule also stops anyone finding a child that spawned but was never recorded. Specify one, for example a launch token passed to the child and confirmed by its first write, plus a resolve command with a receipt.
  4. Correctness: SIGTERM to the owned setsid group misses runtime subprocesses that start their own session, so "no owned process remains" can be true while an escaped child still writes. The adapter should prove it contains descendants, or the receipt should say the stop covered the group only.
  5. Minor: the exit code for `already-terminal` (stop and dequeue) is not fixed as 0 (confirmed no-op) or 1.
  6. Minor: the tool cannot check that `--until` is no later than a prose grant. Require the grant to state its expiry in a form the tool can read, or drop the claim.
  7. Scope: wake (detached watcher, leases, delivery journal, two native adapters) on top of process identity, queue transactions and roles is too much for one bounded run, and wake is likely to end unsupported on both runtimes. Build stop, dequeue and defaults first; wake becomes a second run after those are verified.

## In Progress

Nothing.

## Queries

### REVIEW-2-VERDICT - Revise four named parts before build

**Context** The draft's states, fences and precedence are sound. The accept role's footer widens authority, two crash paths have no defined way to recover, and the single build run is oversized.

**Query** Should the draft go back for revision of ACCEPT-AUTHORITY, the dequeue and wake reconciliation, stop's descendant containment and BUILD-ORDER before the tools-ki build?

**Options** a) (recommended, confidence high - removes the authority widening and the undefined recovery states at little cost) Revise those four parts, then accept and build stop, dequeue and defaults first, with wake as a second run. b) Accept all six now and record the four points as build-time constraints. c) Defer the controls entirely.
