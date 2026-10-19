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
- `ki-brew` received 00:01 BST: Homebrew `ki` upgraded 0.11.4 to 0.11.5; v0.12.0 (hooks migration) prepared in tools-ki but not yet tagged or in the tap.
- `raise-tmx` received 00:05 BST: [TMX-PRINCIPAL-KB-008](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-008-retitle-issuing-areas.md) and [TMX-PRINCIPAL-KB-009](/Users/krisbrown/workspaces/techmedix/tmx-principal/Streams/Roadmap/TMX-PRINCIPAL-KB-009-establish-theme-registry.md) captured and committed in tmx-principal, unpushed; TMX-AREA-TITLES and TMX-THEMES copied, awaiting one batched blind review with the other naming queries once all raise runs finish.
- `raise-hnr` received 00:09 BST: five triage records in hnr-principal and the three 5g-emerge repositories, committed, unpushed; report kept as `report-raise-hnr.md`; its queries await the batched blind review.
- `va-plan` received 00:10 BST: four drafts shaped, SITE-003 repaired from evidence and still awaiting review, roadmap audit fails 7 to 0; committed `f0087d7` in apps-vallearmonia.com, unpushed. SANC008-SPLIT and VA-READY await the batched blind review.
- Standing answer applied to new high-confidence queries: HNR-QUEUE routed to hnr-principal's `hnr` work package; SITE003-CONCERN to run `va-site003-concern`.
- Running in run `baseline-rollout`: `raise-capitals`, `sizekind-1`, `raise-va`; queued: `va-site003-concern` (after raise-capitals), `sizekind-2` (after raise-va). Records are captured as triage and committed locally, never pushed.
- HOOKS-MIGRATION: the estate moves from Husky to `.githooks` tonight; briefs keep off `package.json`, `bun.lock`, `.husky/`, `.githooks/` and non-dry-run conform.

## Next steps

1. Receive each run's report, copy its queries into `queries.md`, blind-review any medium or low one, and give Kris a Summary when all have finished: records raised per repository, the two size-and-kind proposal tables for confirmation per repository, and the KI-BREW result.
2. METHOD-READ: at the next re-read of `ki-work-package` and `ki-coordination`, set `method_read` to the harness short revision read.
3. Stay responsive; Kris's messages steer, and stop or abort only when Kris expressly says so, naming the work.

## Held

- KI-BREW rerun (`brief-ki-brew.md` kept): relaunch `ki-brew` with `--relaunch` once tools-ki tags v0.12.0 and the tap is bumped.
- LEDGER-FORM for apps-kris.me.uk, apps-dafacts.org, er-agentic-harness and apps-markhowarth.com: `--dry-run`-checked conform, one repository at a time on Kris's go, once ki.tools-burndown clears conform after tonight's release.
- SIZE-KIND write passes, after Kris confirms each repository's proposals.
- Registration and every write in another territory's repositories, until Kris's go, repository by repository.
- Rolling out KI-HARNESS-GOV-205 and KI-HARNESS-GOV-221, until the harness ships them (both still triage).
- Full repository re-audits, until KI-HARNESS-GOV-220 fixes COORD-1.
- Routing through ki-trades, until trades reopen (on hold, review due 2026-10-21).
