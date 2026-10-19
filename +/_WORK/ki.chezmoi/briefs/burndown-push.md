# Brief: burndown-push

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`).

Authority: the BURNDOWN-PUSH line from KI > Model > Ways of working, 19:25 BST on 19 October: "Kris agreed a roadmap burndown push for the chezmoi source: prune every record that is done under `ki-work-roadmap`; bring every record awaiting review to Kris as one acceptance batch; and cancel or merge triage records, aiming for at least half, each with a one-line reason, for Kris to confirm before anything is cancelled. Report the net count before and after."

In `/Users/krisbrown/.local/share/chezmoi`, records under `docs/roadmap/` (`ki repo roadmap list`):

1. Count open records by status and horizon first.
2. Prune every Done record under `ki-work-roadmap` and `ki-accept` prune, with the done-before-prune commit boundary. This is authorised.
3. Awaiting review: list every record as one acceptance batch, each with one line on what was delivered and how it was verified. Do not accept any.
4. Triage: propose a cancel or merge for at least half, each with a one-line reason and its merge target. Do not cancel or merge any.
5. Count again and give the net count before and after; the count after the proposals counts them as pending.

Commit only the prune, by explicit path, and run the gate first: `ki repo audit --repo .`, `node --test tests/*.test.mjs`, `rumdl check .`. Do not push or apply.

Report under the owner report with the work's report heading and `› burndown-push`, with two queries: ACCEPT-BATCH and TRIAGE-CUT, each listing its records with links.
