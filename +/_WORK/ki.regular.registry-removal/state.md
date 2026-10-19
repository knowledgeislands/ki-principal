---
id: ki.regular.registry-removal
state: on-hold
hold:
  reason: paused
  release: sol's exact-key check
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-15T12:19:09Z
method_read: null
---

# ki.regular.registry-removal state

## Now

- On hold, paused, since 04:30 BST on 18 October; released by sol's exact-key check. Nothing running.
- Done on terra; the registry is machine-local, so terra's change does not reach sol through Git.
- The state-of-play hold of 15 October set this work to drained without its own drain; the next steps below are those it already had.

## Next steps

1. On sol, fetch and reconcile the checkout with origin/main without overwriting local changes; nothing is waiting on once this handoff is fetched.
2. Read this package and its [decisions](decisions.md).
3. Check sol's machine-local register (`ki registry list --format json`) for the exact key `apps-childhealthyorkshire.co.uk`; if present, remove it with `ki registry remove apps-childhealthyorkshire.co.uk` under the existing instruction, then verify absence with another exact-key check.
4. Report at rest. Start no other work.
5. Other sessions own the remaining terra primary-checkout reconciliation; do not reset, stash or publish their work from this work.

## Held

None.
