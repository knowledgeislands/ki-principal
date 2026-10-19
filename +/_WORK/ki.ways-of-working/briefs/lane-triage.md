# lane-triage

Work: ki.ways-of-working (`+/_WORK/ki.ways-of-working/` in ki-principal). Authorised by Kris's words routed from State of play: TRIAGE-ALL (19 October, "I need them all triaging ... anything which is High confidence recommended. Let's move it into now and get it done"), roadmap-census-2 (20 October, "Can you go through any items which are triaged in knowledge islands and get them progressed?" and "things that are on hold, we need to re-validate everything") and BURN-WAVE-1 (one `ki-accept` pass, cancel, merge and idea list as a single query). Kris said "read messages" at 00:23 BST.

## Lane

ki-agentic-harness (14 triage records), ki-principal `Streams/Roadmap/` (2), ki-specifications (1). Work in worktrees for every repository edit; never edit the main harness checkout.

## Task

1. Under `ki-next`, triage every unadopted triage record in the lane: a recommended disposition and its confidence (high, medium, low) with one line of reason each.
2. First KI-HARNESS-GOV-219 and KI-HARNESS-GOV-224, which keep KI-OBSERVA-BRG-004 and KI-OBSERVA-VIS-042 on hold: if high confidence, adopt into Now and deliver each through `ki-plan` and `ki-implement` to Awaiting review.
3. Adopt every other high-confidence recommendation into Now (commit the adoption); do not deliver beyond GOV-219 and GOV-224 in this run; list them in order for delivery runs.
4. KI-HARNESS-GOV-215: run the COORD-12 check across the estate (met in ki-principal); if met everywhere, release it to Next.
5. Re-validate every On hold record in the lane: still blocked, by what, or ready to release.
6. One `ki-accept` read pass over Awaiting review records in the lane: recommend accept, cancel or merge for each. Accept nothing.
7. KB-DOTFILES-UE-096 waits on KI-TOOL-KI-CLI-145, not KI-HARNESS-GOV-199 Phase 3: append one line saying so to `+/_WORK/ki.chezmoi/messages.md` in ki-principal, asking ki.chezmoi to agree and update the record.

## Rules

- CAPTURE-GATE: create no new records; ideas go to the Project note as a list in your report.
- HOOK-GUARD: never run `ki repo conform` without `--dry-run`.
- Medium or low dispositions, and every cancellation, merge or deletion, come back as queries, one per repository lane, never applied.
- Commit by explicit path; pull with rebase; push fast-forward only when your own commits alone are stacked, otherwise name the others once in Done. Never `--no-verify` or force-push.
- Stay out of ki-design and apps-knowledgeislands.info. British English, ASCII hyphens.

## Report

Owner-report shape: Done, In Progress, Queries (one per lane, Context, Query, lettered Options, confidence on each), then the delivery order for the adopted Now records.
