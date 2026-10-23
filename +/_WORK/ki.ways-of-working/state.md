---
id: ki.ways-of-working
state: handoff-to-supervisor
since: 2026-10-23T03:23:00Z
received: 2026-10-22T07:24:00Z
beat: null
mark: 2026-10-23T01:10:00Z
method_read: eff6163b
---

# ki.ways-of-working state

## Now

- 04:25 BST: every run from Kris's 02:10 unattended grant has finished. Nothing is running.
- Pushed: Harness main (method refinements, two record prunes), tools-ki main (admission of the agent-state compatibility work, 9 commits), tools-techne, ki-principal and ki-design.
- tools-ki admission: the pinned offline audit passed and the dispatcher was restarted on the new code; `ki agent status` reads all 16 threads. The f4ce77b8 migration stays held.
- State of play has a STALE-PACKAGES line on eleven quiet work packages.

## Next steps

- Kris: DRAIN-END and SORT-ARM in queries.md; the RIG-ATTENDED walk-through (parked).
- Coordinator: on SORT-ARM a), route the cancellation to ki.tools-burndown as a messages line; remove the leftover tools-ki and Harness run worktrees once nothing needs them.

## Held

- PAPERCLIP-REQ, on hold while Kris gets KI stable (2026-10-19).
- Email-routing records stay with hnr.email-routing.
- tools-rig v0.8.0 tag, held until the review gates settle.
