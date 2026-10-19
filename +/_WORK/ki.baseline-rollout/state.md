---
id: ki.baseline-rollout
state: with-worker
since: 2026-10-19T23:00:07Z
received: 2026-10-19T23:00:07Z
beat: null
mark: 2026-10-19T22:56:26Z
method_read: 2026-10-19T18:03:40Z
---

# ki.baseline-rollout state

## Now

- Kris, 23:59 BST: "Anything high confidence can be done." Eight queries answered a); REGISTER-HNR (medium) stays with Kris.
- Routed: CHECKER-GAPS to ki.ways-of-working and ki.tools-burndown, TERRITORY-TECHMEDIX to ki.tools-burndown, one `messages.md` line each.
- Running in run `baseline-rollout`: `raise-hnr`, `va-plan`, `ki-brew`; queued: `raise-tmx` (after ki-brew), `raise-va` (after va-plan), `raise-capitals` (after raise-tmx), `sizekind-1` (after raise-hnr), `sizekind-2` (after raise-va). Records are captured as triage and committed locally, never pushed.
- HOOKS-MIGRATION: the estate moves from Husky to `.githooks` tonight; briefs keep off `package.json`, `bun.lock`, `.husky/`, `.githooks/` and non-dry-run conform.

## Next steps

1. Receive each run's report, copy its queries into `queries.md`, blind-review any medium or low one, and give Kris a Summary when all have finished: records raised per repository, the two size-and-kind proposal tables for confirmation per repository, and the KI-BREW result.
2. METHOD-READ: at the next re-read of `ki-work-package` and `ki-coordination`, set `method_read` to the harness short revision read.
3. Stay responsive; Kris's messages steer, and stop or abort only when Kris expressly says so, naming the work.

## Held

- LEDGER-FORM for apps-kris.me.uk, apps-dafacts.org, er-agentic-harness and apps-markhowarth.com: `--dry-run`-checked conform, one repository at a time on Kris's go, once ki.tools-burndown clears conform after tonight's release.
- SIZE-KIND write passes, after Kris confirms each repository's proposals.
- Registration and every write in another territory's repositories, until Kris's go, repository by repository.
- Rolling out KI-HARNESS-GOV-205 and KI-HARNESS-GOV-221, until the harness ships them (both still triage).
- Full repository re-audits, until KI-HARNESS-GOV-220 fixes COORD-1.
- Routing through ki-trades, until trades reopen (on hold, review due 2026-10-21).
