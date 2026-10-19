# Brief: mark-tidy-1019

Work: KI > Rig > chezmoi (`+/_WORK/ki.chezmoi/` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`). Mark struck at 2026-10-19T18:02:56Z.

Authority: Kris's "do all the recommended items" (PRINCIPAL-CI-RED) and "do what you need to do to get that working" (AUDIT-TIDY), and the REPORT-SWEEP and PIN-DONE-LINKS lines, as recorded in `decisions.md` and `messages.md`.

Do, under `ki-work-package` Tidying the work folder and the `ki-coordination` decisions life cycle:

1. REPORT-SWEEP: for each report and brief that line lists, copy any open query not already in `queries.md` into it, home each outcome (work record, decisions log, `state.md` next steps or a commit), then delete the file by explicit path. Keep a report whose outcome has no durable home and say why.
2. PIN-DONE-LINKS and COORD-7: in any report you keep, link every bare record identifier to its local file, or pin a pruned one to its GitHub copy at the named revision.
3. Decisions life cycle on `decisions.md`: strike entries whose home now holds them, point the ones still governing live work, keep the rest; mark any standalone entry `homeless: <TAG>` in `state.md` next steps.
4. Run `ki repo audit --skill ki-coordination --repo .` and `ki repo audit --skill ki-work-package --repo .`; fix only findings in `+/_WORK/ki.chezmoi/`.

Edit only `+/_WORK/ki.chezmoi/`. Do not touch `state.md` front matter or `messages.md`. Commit by explicit path with subject `docs(work): ki.chezmoi mark tidy`. Do not push: other works' commits are stacked above origin.

Report under the owner report with the work's report heading and `› mark-tidy-1019`.
