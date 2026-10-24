# wow-summary-drift

## Goal

Kris, 24 October: "I still really need this thread to be giving me proper summaries, which you're not doing, I don't know why, can you investigate where that is?" Find why the ki.ways-of-working coordinator thread on sol does not give owner reports in the standard's shape, and propose the fix.

## Evidence

- This session's transcript: `/Users/krisbrown/.claude/projects/-Users-krisbrown-workspaces-knowledge-islands-ki-principal/ee47a74e-6bed-42d2-9690-3596814f0d47.jsonl` (session ee47a74e). Read the assistant replies from the re-bootstrap onwards.
- The standard: `skills/change-management/ki-coordination/references/standards-coordination.md` in ki-agentic-harness, its Reply forms, Owner report, Report forms and Banner sections; the harness `output-styles/ki-coordinator.md` and `hooks/coordinator-reminder.sh`; `scripts/banner.test.ts`.
- The output style actually loaded in this session is in the transcript's system prompt; compare it with the harness copy on disk and with what `~/.claude` installs (`ki agent` / skills install path), byte for byte where it matters.
- `state.md` `method_read: eff6163b` against harness `git log -1 --format=%h -- skills/change-management/ki-coordination skills/governance/ki-work-package` (111b853a on sol today): the refresh rule was not run at this re-bootstrap.
- Competing instructions in the session context: `~/.claude/communication.md` (quiet level), the headroom proxy's `<headroom_output_shaping>` block ("Skip preamble and postamble ... Never restate ... tool output"), and Kris's own "report in three lines".

## Do

- List each assistant reply that should have been an owner report or carried the banner under the standard, and say what it lacked: heading, form line, the three sections, full queries, banner, thread line.
- Name each cause with evidence, e.g. stale installed style or skill, the proxy shaping block, the quiet level, an ambiguous rule on "report in N lines", replies to owner messages that answer where the work stands without the banner, or the coordinator's own error.
- Propose the smallest fix for each: a standard or style wording change, an install or refresh step, a proxy or user-config change (chezmoi), or a coordinator habit. Any change to a standard or Kris's configuration is a query, not an edit.

## Do not

- Edit any standard, skill, style, hook, chezmoi file or package file other than your report; push; launch agents.

## Output

Write `+/_WORK/ki.ways-of-working/summary-drift.report.md` in ki-principal and commit it by explicit path with `docs(work): ki.ways-of-working summary drift report`, pulling with rebase first if ki-principal moved. Report in the owner-report shape with queries for each proposed change.
