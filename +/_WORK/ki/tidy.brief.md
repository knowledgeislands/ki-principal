# tidy brief

Work: ki, State of play, KI > SoP. Host sol. Kris asked on 2026-10-25 for every work package related to State of play's current work to be tidied.

## Goal

1. **State of play's own package, `+/_WORK/ki/`:** tidy it under `ki-work-package`, "Tidying the work folder", and the `ki-coordination` mark rules.
   - Delete every report whose outcome is homed and whose queries are already in `queries.md`, and every brief whose report has been received.
   - Keep the five package files, live design notes such as `design/estate-factorisation-retirement.md` (ESTATE-CLOSE is open), and the `accept-review` brief and report, which belong to a run in flight.
   - Strike each decision that a durable home now wholly carries, and reduce to a one-line pointer each one that still governs live work. Keep every 2026-10-25 entry, since those govern live work.
   - Make sure `queries.md` lists exactly the open queries. ACCEPT-WEBSITE, ACCEPT-WOW, ACCEPT-OBSERVATORY and ACCEPT-RIG are now answered (see `decisions.md`), so record them as answered or in hand, not as open.
2. **Related packages:** run the `ki-work-package` rubric over the packages State of play has touched since the mark of 2026-10-24 20:29 BST: ki.ways-of-working, ki.baseline-rollout, ki.tools-burndown, ki.mac-studio-setup, ki.chezmoi, ki.observatory, ki.website, ki.agent-host and ki.knowledge-acquisition.
   - For ki.website, which State of play seeded overnight, fix any conformance gap yourself. It is State of play's creation, and it stays on hold.
   - For every other package, do not edit it. Append one `TIDY` line to its own `messages.md` naming each finding, as territory work does at its mark.
   - Leave `+/_WORK/ki.specifications/` untouched, since SPECS-FOLDER is open.

## Limits

- Another session has uncommitted changes in ki.ways-of-working, ki.chezmoi, ki.knowledge-acquisition, ki.baseline-rollout and `Admin/Governance/Known Lands.md`. Never touch, stage or revert them. If a `messages.md` you need is dirty from another session, skip it and say so.
- No Admin, Pillars or Resources changes, no record changes, and no deletion outside `+/_WORK/ki/` apart from the ki.website fixes.
- Commit by explicit path with `docs(work): ki tidy ...` subjects, pull with rebase, and push fast-forward only. Never force a push and never use `--no-verify`.

## Report

Write `+/_WORK/ki/tidy.report.md` in run-report form: Done, In Progress and Queries. List what was deleted, struck and messaged, and name each skipped file. Commit it and push.
