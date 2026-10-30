# intake-review - blind review of one owner decision

Work: ki.prj.mac-studio-setup (KI > Rig > Mac Studio setup). You are an independent reviewer. Do not read `queries.md`, `decisions.md`, `state.md` or any `*.report.md` in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.mac-studio-setup/`. You may read that package's `messages.md` (the nine Rig capability lines), the tools-rig repository (`/Users/krisbrown/workspaces/knowledge-islands/tools-rig`: `docs/roadmap/`, `docs/roadmap/_IDEAS.md`, `docs/ideas/`, `docs/specs/`, `docs/guides/`, code, Git history) and the chezmoi source (`/Users/krisbrown/.local/share/chezmoi`). Verify claims directly.

## Context

Nine capability lines for Rig (eleven bullets) wait in the package's `messages.md`: RIG-APP-FOOTPRINT (IMPORTANT), RIG-NOTIFICATIONS (two), RIG-MACHINE-MANAGEMENT, RIG-CLI-CONSISTENCY, RIG-COMMENT-KIND, WAKE-SUBSTRATE, RIG-TUI, RIG-SSH-CHECK, RIG-REMINDER-DOCTOR. Kris set BURN-DOWN on 14 October ("burn the roadmap down; no new feature records"), refined on 19 October by CAPTURE-GATE: capture only blockers, defects seen failing, or items Kris asked for; ideas go to `_IDEAS.md`. RIG-TUI, RIG-SSH-CHECK, RIG-COMMENT-KIND and the footprint group (RIG-APP-FOOTPRINT, RIG-NOTIFICATIONS, RIG-MACHINE-MANAGEMENT) carry Kris's own explicit asks; RIG-CLI-CONSISTENCY reports defects seen on sol under Rig 0.8.0. The footprint group's natural owner, the KI-TOOL-RIG-CORE-072 idea (application configuration touch points), was moved to ideas on 27 October when Kris bulk-approved a sweep's "defer to Later" bucket and asked for fewer things in the queue; that sweep did not have the footprint lines in front of it. It is claimed that `scheduled-job` already renders launchd calendar jobs (WAKE-SUBSTRATE's Rig share) and that chezmoi already registers the coordinator hook on every machine (RIG-REMINDER-DOCTOR).

## Query

What should happen to the nine lines? Candidate courses, in no order:

- Strict BURN-DOWN: capture only RIG-TUI and RIG-SSH-CHECK as unadopted triage records; RIG-COMMENT-KIND and RIG-CLI-CONSISTENCY as `_IDEAS.md` bullets; footprint group folded into the KI-TOOL-RIG-CORE-072 idea; WAKE-SUBSTRATE and RIG-REMINDER-DOCTOR returned to their senders.
- Bring KI-TOOL-RIG-CORE-072 back from ideas as a triage record carrying the whole footprint group, plus triage records for RIG-TUI, RIG-SSH-CHECK, RIG-COMMENT-KIND and the CLI defects; the same two returns.
- Four triage captures (RIG-TUI with an in-Rig full-screen idea folded in, RIG-SSH-CHECK, RIG-COMMENT-KIND, one CLI-defects record); footprint group held in the KI-TOOL-RIG-CORE-072 idea until Kris brings 072 back; the same two returns.

Choose one (or a better course), give your confidence (high, medium or low) with a one-line reason, and note any claim above you found false.

## Bounds

Read-only. Write nothing except your report. No system change, no commit, no push.

## Report

Write your report to `/Users/krisbrown/.local/state/ki/agents/ki-prj-mac-studio-setup/intake-review.report.md`; the launcher homes it in the work package.
