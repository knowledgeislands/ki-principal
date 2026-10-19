---
id: ki.baseline-rollout
state: with-worker
since: 2026-10-19T22:39:56Z
received: 2026-10-19T22:39:56Z
beat: null
mark: 2026-10-19T22:27:24Z
method_read: 2026-10-19T18:03:40Z
---

# ki.baseline-rollout state

## Now

- Kris answered WAVE-1 at 23:30 BST, "go with recommendations": wave 1 launched read-only at 23:40 BST in run `baseline-rollout`.
- Running: `wave1-audit` (territory audits, installed `ki` versions, harness status; brief `brief-wave1-audit.md`) and `wave1-sweep` (roadmap conformance sweep; brief `brief-wave1-sweep.md`), both Claude at high effort, read-only.
- REFRESH-BANNER (ways-of-working, 23:35 BST) applied: banner on every state-moving reply; pushes only as `[unpushed]` housekeeping; clean hold banners.
- HOOK-GUARD: never run `ki repo conform` without `--dry-run` on a KI repository until ki.tools-burndown lifts it; every wave brief carries this.

## Next steps

1. On each wave 1 report, receive it, copy its queries into `queries.md`, and once both are in give Kris a fresh Summary, sending medium- and low-confidence queries through one blind review first.
2. METHOD-READ: at the next re-read of `ki-work-package` and `ki-coordination`, set `method_read` to the harness short revision read (not a UTC time).
3. Stay responsive; Kris's messages steer, and stop or abort only when Kris expressly says so, naming the work.

## Held

- Registering what the territory audit finds missing, until Kris's go.
- Rolling out KI-HARNESS-GOV-205 and KI-HARNESS-GOV-221, until the harness ships them (both still triage).
- Full repository re-audits of personal-principal and the rest, until KI-HARNESS-GOV-220 fixes COORD-1.
- Routing through ki-trades, until trades reopen (on hold, review due 2026-10-21).
