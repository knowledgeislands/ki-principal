---
work: ki.ways-of-working
run: ways-of-working
agent: wow-fix-rig-hook
written_at: 2026-10-27T04:20:59.264296+00:00
---

# Task: implement the qualified wow-fix-rig-hook repair

## RIG-SHELL-HOOK - Remove the obsolete audit-only hook scaffolding

**Goal:** Keep Rig's commit hook limited to its accepted staged checks.

**Scope:** tools-rig's existing pre-commit hook only.

**As of:** 27 October 2026, 04:14 GMT; current local files, inspected without executing the hook.

**Disposition:** High-confidence small conformity repair. The record's suggestion that the rubric merely misreads a function is incomplete: the hook actually calls the audit twice on failure and invokes that function. The current contract explicitly excludes audits from commit time.

**Evidence:** [The current hook](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/.githooks/pre-commit:33) retains the audit function and invocation. [SHELL-HOOK](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/.agents/skills/ki-repo-tools/references/rubric.md:127) and [Commit gate](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/.agents/skills/ki-repo-tools/references/standards-tool-repositories.md:114) exclude it. [The rubric implementation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/.agents/skills/ki-repo-tools/scripts/rubric/items/shell.ts:162) explicitly rejects both the function name and audit calls. [The implementation record](https://github.com/knowledgeislands/tools-rig/blob/4f006e3505c4e14c247b8f4a8b129ed8551547a4/docs/roadmap/KI-TOOL-RIG-CORE-073-native-tool-absolute-path-fallback.md#L105) supplies the original finding.

**Owning record:** No separate repair record identified in the scoped evidence. [KI-TOOL-RIG-CORE-073](https://github.com/knowledgeislands/tools-rig/blob/4f006e3505c4e14c247b8f4a8b129ed8551547a4/docs/roadmap/KI-TOOL-RIG-CORE-073-native-tool-absolute-path-fallback.md) owns the native-tool path fallback and supplies evidence only; do not reopen or expand it to own this repair.

**Exact allowed path for a subsequent unit:** `/Users/krisbrown/workspaces/knowledge-islands/tools-rig/.githooks/pre-commit` only.

**Proposed minimal change:** Delete the audit-only root assignment at line 4, remove the now-unused KI executable prerequisite from line 7, and delete the audit-only tail beginning at line 33. Preserve the missing-tool refusal, empty-index exit, Markdown, shell and manual checks, and executable mode. This is a deletion of obsolete scaffolding, not a wholesale hook replacement.

**Authority:** The same recorded COMMIT-VS-CI decision and declared SHELL-HOOK contract already settle this behaviour; SUCCESSIVE-WAVES/CONFIDENT-UNATTENDED permits qualification for bounded local delivery. The later instruction that earlier hook commits stand does not grant general replacement authority; this proposal preserves their staged checks. Implementation remains outside this read-only unit.

**One sufficient targeted verification:** Read-only byte equality between the edited hook and [the declared no-package canonical asset](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/.agents/skills/ki-repo-tools/assets/githooks/no-package/pre-commit). The exact three-part deletion above already passed this comparison in memory. A delivery unit would compare its actual edited file once, preserving its mode; no hook execution, provider probe, suite or release cycle is needed to establish canonical hook content.

Implement ONLY this frozen single-file conformity repair. The exact accepted COMMIT-VS-CI contract and current SUCCESSIVE-WAVES/CONFIDENT-UNATTENDED authority are identified above; the owner now also explicitly authorises high-confidence acceptance/pruning, but this unit performs neither lifecycle action. No new roadmap record, feature, policy, broad hook replacement, dependency or lockfile change. Earlier hook commits remain historical; make the minimal newly verified repair.

Read applicable AGENTS.md and ki-git. Use tools-ki's mandatory isolated worktree, and a safe declared worktree/primary policy for Rig; inspect initial main, cached origin/main, index/dirt and active writers before mutation. Freeze the one allowed path from the qualified finding. For tools-ki remove only the two rewriting flags, preserving every other parsed package value, globs and command order. For Rig remove only the audit scaffolding, leaving existing staged checks intact and preserving executable mode; exact final bytes must equal the already-declared canonical no-package hook. Do not run the old hook directly.

One sufficient targeted verification is the exact JSON transformation predicate or canonical hook byte/mode equality stated above. Do not run coverage, full suites, broad audits, builds, provider tests, releases or deployment. Required commit hooks still run once, without bypass; do not execute them again manually. Finish every intended edit before any formatting write pass. Stage only the single owned file, use a Conventional Commit, inspect actual git show --name-status after hooks, self-integrate a verified own worktree only by the standard fast-forward rule and retire it safely.

Fetch/reconcile only this repo's origin for freshness. Publication is permitted only if the existing exact COMMIT-VS-CI/convergence task grant actually covers this repair and every unpublished ancestor, or another explicit recorded grant covers it; inspect the source rather than inferring code/runtime push authority from general autonomy or a generic footer. If no grant covers it, preserve the verified local main commit and report exact repository, sol.local and branch; never force, deploy or publish a package. Stop on divergence, contested staging, unknown extra scope or genuine required-check failure, preserving all unrelated work.

Do not edit principal package/queues. Report repair, exact focused evidence and any pending publication concisely so the coordinator can let acceptance proceed against the repaired baseline. No acceptance/pruning in this unit. Do not use background subagents. Never end session while waiting.

**Report** to `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-fix-rig-hook.report.md`, in the run's state folder and nowhere else, as an owner report: the ki-coordination report heading of the work you report to with `› <run name>` added, `# [<Theme>](<local theme page>) › [<Project>](<local Project note>) › <run name>`, the bold `**🤖 → 👤 Handoff to supervisor · Run report at <local time> · last mark <local time>**` line, adding `· blocked` after the state where you send back with a blocking query, and one `---`, then `## Done`, `## In Progress` and `## Queries`, each query carrying **Context**, **Query** and lettered **Options** as separate paragraphs with a blank line between them, each option its own paragraph, `a) (recommended, confidence <level> - <reason>)` first, no bullets and no reply block; where the brief asks for findings, add `## Findings` between `## In Progress` and `## Queries`, each finding a `### <TAG> - <title>` heading opening with its **Goal**, **Scope** and **As of** lines before any table, and write it also to the finding file the brief names; then, for coordinating work, the glyph banner the ki-coordination [Banner](../../../change-management/ki-coordination/references/standards-coordination.md#banner) section prints, its `###` state heading, counts line and `- [state] what · holder · since` list, closing with one thread line, `🧵 Coordination thread · <label> (<id>)` for Project work or `🧵 State of play thread · <label> (<id>)` for territory work, using the work you report to, and no send or resume line; a run report to a conversational session or ad hoc work has no mark in its form line and no banner. The report's first non-blank line is its `#` heading, after front matter if the report has any. Run tools quietly under the ki-coordination [quiet-tools rule](../../../change-management/ki-coordination/references/standards-coordination.md#quiet-tools): run Git with `-q`, never paste gate, audit or Git output, and report each outcome in one line. Owner reports, run reports and banners omit routine push state and other sessions' stacked commits; if your own unit could not be published because its push failed, Done names the affected unit and reason. A hold report keeps nothing about pushes beyond a failure.

Temporary output goes in <temporary>/, outside every repository; never remove it yourself, ki agent close empties and removes it, so home what must survive first. Write nothing into `+/_WORK/ki.ways-of-working/` beyond your report.

Do not use background subagents. Never end your session while waiting.
