# ways-of-working › wow-cadence-blind

**🤖 → 👤 Handoff to supervisor · Run report at 01:44 BST · last mark not supplied**

---

## Done

Reviewed only the two permitted coordination sections; blind-review boundary preserved. No repository writes, commits, network calls or agents.

Prepared independent recommendations for both questions; neither recommendation has been enacted.

## In Progress

None. Parent Theme/Project links and last-mark time were not supplied and have not been inferred or looked up.

## Queries

### COMMIT-CADENCE

**Context**: The present event-based cadence leaves intervening package writes uncommitted and does not cover heartbeat wakes.

**Query**: Adopt a write-and-wake cadence across the standard, output style and hook line?

**Options**

a) (recommended, confidence high - It closes the persistence gap that leaves shared work packages stale.) Yes: commit each completed package write by explicit path before its turn ends; at every wake, check for outstanding owned changes and reconcile and publish safely. Pull with rebase only when safe for the shared checkout, preserve other sessions' uncommitted work, and stop on conflicts. A clean wake needs no empty commit. Publication remains subject to the applicable push authority.

b) Keep the existing send/receive/mark/hold/finish cadence.

### PACKAGE-PUSH

**Context**: Even promptly committed work remains local when another session's package-only commit sits beneath it.

**Query**: Permit fast-forward publication of other sessions' commits when every changed path in those commits lies under `+/_WORK/`?

**Options**

a) (recommended, confidence medium - A narrow package-only exception removes the routine publication bottleneck while retaining the boundary for other changes.) Yes: inspect every unpublished commit and its actual changed paths, including both sides of renames; permit the stack only when every other session's commit is confined to `+/_WORK/`. Preserve any explicit publication restriction, stop on divergence or uncertain contents, and never force-push. Keep own-commits-only authority for all other stacked commits.

b) Keep own-commits-only pushing for every stack.

🤖 → 👤

### Awaiting review

1 awaiting review · 2 queries

- [with you] Decide COMMIT-CADENCE and PACKAGE-PUSH · Kris · since 01:44 BST

🧵 Coordination thread · ways-of-working (ways-of-working)
