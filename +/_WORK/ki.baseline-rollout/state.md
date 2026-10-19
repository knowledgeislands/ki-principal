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
- `wave1-audit` received 23:45 BST: five territories healthy; Techmedix audit blocked by an archived unregistered member; three undeclared HNR repositories; Homebrew `ki` one release behind. Queries TERRITORY-TECHMEDIX, REGISTER-HNR and KI-BREW copied to `queries.md`; report kept as `report-wave1-audit.md` until its queries are answered.
- Running: `wave1-sweep` (roadmap conformance sweep), and blind reviews `review-territory-techmedix` and `review-register-hnr` (Codex, high effort).
- REFRESH-BANNER (ways-of-working, 23:35 BST) applied: banner on every state-moving reply; pushes only as `[unpushed]` housekeeping; clean hold banners.
- HOOKS-MIGRATION (State of play, 23:41 BST, replaces HOOK-GUARD): the estate moves from Husky to `.githooks` tonight after the new ki release; this work holds no uncommitted `package.json`, `bun.lock`, `.husky/` or `.githooks/` changes, and wave briefs still never run `ki repo conform`.

## Next steps

1. On each wave 1 report, receive it, copy its queries into `queries.md`, and once both are in give Kris a fresh Summary, sending medium- and low-confidence queries through one blind review first.
2. METHOD-READ: at the next re-read of `ki-work-package` and `ki-coordination`, set `method_read` to the harness short revision read (not a UTC time).
3. Stay responsive; Kris's messages steer, and stop or abort only when Kris expressly says so, naming the work.

## Held

- Registering what the territory audit finds missing, until Kris's go.
- Rolling out KI-HARNESS-GOV-205 and KI-HARNESS-GOV-221, until the harness ships them (both still triage).
- Full repository re-audits of personal-principal and the rest, until KI-HARNESS-GOV-220 fixes COORD-1.
- Routing through ki-trades, until trades reopen (on hold, review due 2026-10-21).
