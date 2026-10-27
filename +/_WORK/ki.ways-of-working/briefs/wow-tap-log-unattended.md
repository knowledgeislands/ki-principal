---
work: ki.ways-of-working
run: ways-of-working
agent: wow-tap-log-unattended
written_at: 2026-10-27T03:09:56.533655+00:00
---

# Task: deliver the already approved SUMMARY-VISIBLE logging improvement

Kris approved SUMMARY-VISIBLE a on 26 October, as recorded in +/_WORK/ki.ways-of-working/decisions.md and the existing wow-tap-log.queued.md task. That scope reads: "in homebrew-tap, the Notify job also prints \"Dispatched <tool> <version> to <consumer>\" to its log as well as the job summary; point tools-ki's release guide step 6 at the log line. No behaviour change. Verify with a dry or replayed run that the line appears in gh run view --log." Kris's current CONFIDENT-UNATTENDED instruction lifts the launch pause and authorises useful confident partial deliveries with no repeated build/deployment checks. This task is that same approved unit, re-dispatched on Codex instead of using the nearly exhausted Claude account.

Exact permitted repository content paths:

- /Users/krisbrown/workspaces/knowledge-islands/homebrew-tap/.github/workflows/ci.yml
- /Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/guides/developer/releasing.md

Do not create/change a release, tag, deployed service or dispatch a workflow merely to verify a log line. Do not change notify routing, workflow triggers, tool versions, release payload shape or any other workflow behaviour. Current ci.yml line writes the Dispatched message only into GITHUB_STEP_SUMMARY. Make the smallest change that also emits the same exact line on stdout, preserving summary output; update the approved release-guide step to explain where that line can be read. Inspect exact source before editing. Keep this a logging/documentation change.

The launcher holds this run until wow-quick-wins, wow-extra-writes-2 and wow-unattended-plan finish, preventing overlap in Git write windows. Do not stop any worker or launch subagents. Read relevant repository AGENTS.md and ki-git standard; tools-ki requires an isolated worktree for edits and reviewed local fast-forward self-integration under its declared rules. Existing authority to push from the original wow-tap-log brief covers this approved unit, subject to inspecting every unpublished ancestor and stopping for unexpected code, divergence, contested staging or deployment risk. If the actual authority does not cover some publication, keep verified commits local and give a precise sol.local / repository / branch handoff.

Use one focused local replay/simulation proving the notification line reaches both stdout and the summary sink, and one syntax/guide check appropriate to the changed paths; no new test suite, whole application build, repeated audits or live workflow run. Required repository hooks cannot be bypassed. A real gh run view observation is optional and read-only; if no existing run contains the new code, state that evidence is not yet observed and deliver the verified local part without pretending otherwise.

Commit only the two intended paths in their owning repositories, inspect git show --name-status after each hook-backed commit, and integrate your own worktree via the authorised local fast-forward procedure. Do not accept/prune roadmap records or edit the coordinator's package. No loss of unrelated files or pending work is allowed. Report result, exact evidence and any publication/verification limitation concisely.

Do not use background subagents. Never end session while waiting.

**Report** to `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-tap-log-unattended.report.md`, in the run's state folder and nowhere else, as an owner report: the ki-coordination report heading of the work you report to with `› <run name>` added, `# [<Theme>](<local theme page>) › [<Project>](<local Project note>) › <run name>`, the bold `**🤖 → 👤 Handoff to supervisor · Run report at <local time> · last mark <local time>**` line, adding `· blocked` after the state where you send back with a blocking query, and one `---`, then `## Done`, `## In Progress` and `## Queries`, each query carrying **Context**, **Query** and lettered **Options** as separate paragraphs with a blank line between them, each option its own paragraph, `a) (recommended, confidence <level> - <reason>)` first, no bullets and no reply block; where the brief asks for findings, add `## Findings` between `## In Progress` and `## Queries`, each finding a `### <TAG> - <title>` heading opening with its **Goal**, **Scope** and **As of** lines before any table, and write it also to the finding file the brief names; then, for coordinating work, the glyph banner the ki-coordination [Banner](../../../change-management/ki-coordination/references/standards-coordination.md#banner) section prints, its `###` state heading, counts line and `- [state] what · holder · since` list, closing with one thread line, `🧵 Coordination thread · <label> (<id>)` for Project work or `🧵 State of play thread · <label> (<id>)` for territory work, using the work you report to, and no send or resume line; a run report to a conversational session or ad hoc work has no mark in its form line and no banner. The report's first non-blank line is its `#` heading, after front matter if the report has any. Run tools quietly under the ki-coordination [quiet-tools rule](../../../change-management/ki-coordination/references/standards-coordination.md#quiet-tools): run Git with `-q`, never paste gate, audit or Git output, and report each outcome in one line. Owner reports, run reports and banners omit routine push state and other sessions' stacked commits; if your own unit could not be published because its push failed, Done names the affected unit and reason. A hold report keeps nothing about pushes beyond a failure.

Temporary output goes in <temporary>/, outside every repository; never remove it yourself, ki agent close empties and removes it, so home what must survive first. Write nothing into `+/_WORK/ki.ways-of-working/` beyond your report.

Do not use background subagents. Never end your session while waiting.
