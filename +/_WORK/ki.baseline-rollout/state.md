---
id: ki.baseline-rollout
state: handoff-to-supervisor
since: 2026-10-19T22:27:24Z
received: 2026-10-19T22:27:24Z
beat: null
mark: 2026-10-19T22:27:24Z
method_read: 2026-10-19T18:03:40Z
---

# ki.baseline-rollout state

## Now

- Received `wave1-review` (Codex, high effort, blind): it agrees with WAVE-1 a); confidence lifted to high, marked reviewed. Brief pruned; marked and sent to Kris at 23:28 BST.
- With Kris: WAVE-1.
- Nothing running in run `baseline-rollout`.
- HOOK-GUARD (ki.tools-burndown via State of play, 23:24 BST): never run `ki repo conform` without `--dry-run` on a KI repository until ki.tools-burndown lifts it; every wave brief carries this.

## Next steps

1. On Kris's WAVE-1 answer, record it in `decisions.md`, then launch the read-only first wave through `ki agent` in run `baseline-rollout`: `ki territory audit` for the six territories, a finding-only file sweep (retired theme slugs, issue-ledger form, size declarations), and harness status for KI-HARNESS-GOV-205, KI-HARNESS-GOV-221 and KI-HARNESS-GOV-220 (COORD-1); findings stay in the run state folder.
2. METHOD-READ: at the next re-read of `ki-work-package` and `ki-coordination`, set `method_read` to the harness short revision read (not a UTC time).
3. Stay responsive; Kris's messages steer, and stop or abort only when Kris expressly says so, naming the work.

## Held

- Registering what the territory audit finds missing, until Kris's go.
- Rolling out KI-HARNESS-GOV-205 and KI-HARNESS-GOV-221, until the harness ships them (both still triage).
- Full repository re-audits of personal-principal and the rest, until KI-HARNESS-GOV-220 fixes COORD-1.
- Routing through ki-trades, until trades reopen (on hold, review due 2026-10-21).
