# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-day-contract-review-3

**🤖 → 👤 Handoff to supervisor · Run report at 14:50 BST**

---

## Done

- Verdict: **return one named part for revision first, the launch roles (ACCEPT-AUTHORITY)**; accept STOP-POLICY, QUEUE-CANCEL, WAKE-BOUNDARY, ROLE-PINS as role-and-precedence policy only, BUILD-ORDER, and the command and precedence policy as drafted, with local evidence required before any model pin or native wake adapter is enabled.
- Confidence: **high** - every "today's gap" claim checks against tools-ki source (processes port exposes launch, liveness and sleep only; dispatch splices the queue then launches with no claim journal; the event vocabulary and the waiter cursor are as described), and the one defect is a bounded authority mapping.
- Rationale:
  1. Mapping the accept role to the prune footer hands an acceptance run push and deletion authority it never needs; it contradicts the draft's own rule that accepting and pruning are separate actions with a terminal-state commit between them. Change: accept resolves the none footer plus an explicit acceptance declaration; prune stays its own role.
  2. The "owner override of the footer's acceptance ban" has no defined shape in the contract, yet the tools-ki run must refuse on a missing declaration before the Harness follow-up defines it. Change: fix the declaration in the contract now (cited authority reference plus named record identifiers, both in the receipt) so the build has something to validate.
  3. Minor: "refuses runtime/model below the accepted strongest Codex binding" needs a tool-owned ordering; say "other than the accepted pin unless an explicit cited authority overrides".
  4. Stop is sound: ownership verified before SIGTERM, no SIGKILL, timeout left visible, uncertain observation never reported as stopped. Expect macOS ownership proof to be hard; refusal there is the right outcome, not a defect.
  5. Dequeue is sound: the cancellation fence inside the spawn-authorisation transaction and the explicit already-started refusal close the current read-splice-launch race.
  6. Wake is sound and honest: exact session binding, absolute expiry, terminal and query events only, no blind retry after unconfirmed delivery, no new-session fallback, and an unsupported adapter returns as a query rather than a simulated call.
  7. Roles ship dormant until pins are evidenced, since role launches must pin model and effort and refuse without fallback; an explicit valid model satisfies the pin meanwhile. State this plainly in the accepted contract.
- Read-only review; no commit, no file in any repository changed, no remote call.

## In Progress

Nothing.

## Queries

None.
