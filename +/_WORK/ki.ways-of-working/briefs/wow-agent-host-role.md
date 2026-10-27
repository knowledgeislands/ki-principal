---
work: ki.ways-of-working
run: ways-of-working
agent: wow-agent-host-role
written_at: 2026-10-27T04:10:58.960920+00:00
---

# Task: deliver the already-approved agent-host role extraction as a verified partial unit

Exact repository: /Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness. Exact record: docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md. Authority: its merged OPS-025 section records Kris's approval of the independent role/profile extraction on 14 October; current SUCCESSIVE-WAVES and CONFIDENT-UNATTENDED in principal/+/_WORK/ki.ways-of-working/decisions.md explicitly permit bringing clear deferred work forward and doing useful confident parts. LOCAL-SYMLINKS removes release ceremony, not real prerequisites. Read Techne Programme Focus before work. No remote host operation is authorised.

Use the specific WAVE finding in /Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-next-wave.report.md, not another estate survey. The bounded outcome is ONLY moving the existing byte-identical rig.toml and observe-only rig-pins.sh from recipes/agent-host/ to roles/agent-host/, preserving file mode and one source, then rewiring current consumers without breaking staged or checkout invocation. Keep host-instructions.md recipe-owned and preserve staged payload basenames. The rest of OPS-018 remains undelivered: do not switch the tool installation mechanism, decide minimum versions, firewall declarations, clone/pin policy, install packages, change host/provider contracts or roll anything out.

Candidate paths to verify/freeze before edits:

- docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md
- recipes/agent-host/rig.toml -> roles/agent-host/rig.toml
- recipes/agent-host/rig-pins.sh -> roles/agent-host/rig-pins.sh
- recipes/agent-host/recipe.toml
- operations/aws/agent-host/setup.sh
- operations/aws/agent-host/status.sh
- operations/aws/agent-host/host/converge.sh
- tooling/checks/agent-host-workspace.sh
- docs/guides/operator/agent-host.md

Read applicable AGENTS.md, ki-git, ki-next, ki-plan and outcome/partial delivery rules. Legitimately select the existing deferred record and write an exact bounded phase plan under current outcome authority before implementing; check reference closure and any required directory convention then freeze its allowed paths. Do not invent public semantics or expand paths after freezing. Do not create replacement/new records. If the full parent cannot honestly be Ready because its other phases remain unsettled, do not manufacture Ready/Done status: the owner's explicit instruction to deliver confident parts permits this separately-approved, fully planned and verified phase while the parent stays honestly unfinished. Document that bounded partial authority and remaining scope in the existing record. Use a normal outcome batch only if its readiness semantics can be represented honestly; no fake authorisation hash or completion claim to get past tooling.

Implement the complete independently useful extraction. Extend only the existing offline fixtures meaningfully for both invocation modes and unchanged payload/mode. One sufficient aggregate check is bash tooling/checks/agent-host-workspace.sh; first inspect that it substitutes remote/tools/host operations locally. Never directly invoke setup.sh, status.sh or converge.sh against a real host. No AWS, SSH, provider, network/security, credential, MCP-binding or daemon mutation; no new software, release/tag/package publication, deployment or live observation. Use one sufficient verification pass and compulsory hooks, not standalone full tests followed by the same tests inside audit. Actual mandatory failures stop affected work without bypass. No tests mirroring the move mechanically when existing fixture coverage proves behaviour.

Use declared primary/worktree policy and short Git write window; preserve unrelated paths and contested staging. Commit only the complete verified phase and its honest evidence; inspect git show --name-status after hooks. Integrate/retire only your own worktree through the declared verified local fast-forward rule. Git fetch/reconciliation is allowed only from this repository's origin. No push is authorised for this new code unit: preserve verified local commits and report exact repository, sol.local and branch as the pending handoff. No acceptance or pruning. Do not edit principal packages/queues; its steward receives outcomes. Report useful delivery, actual checks and remaining parent scope concisely.

Do not use background subagents. Never end session while waiting.

**Report** to `/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-agent-host-role.report.md`, in the run's state folder and nowhere else, as an owner report: the ki-coordination report heading of the work you report to with `› <run name>` added, `# [<Theme>](<local theme page>) › [<Project>](<local Project note>) › <run name>`, the bold `**🤖 → 👤 Handoff to supervisor · Run report at <local time> · last mark <local time>**` line, adding `· blocked` after the state where you send back with a blocking query, and one `---`, then `## Done`, `## In Progress` and `## Queries`, each query carrying **Context**, **Query** and lettered **Options** as separate paragraphs with a blank line between them, each option its own paragraph, `a) (recommended, confidence <level> - <reason>)` first, no bullets and no reply block; where the brief asks for findings, add `## Findings` between `## In Progress` and `## Queries`, each finding a `### <TAG> - <title>` heading opening with its **Goal**, **Scope** and **As of** lines before any table, and write it also to the finding file the brief names; then, for coordinating work, the glyph banner the ki-coordination [Banner](../../../change-management/ki-coordination/references/standards-coordination.md#banner) section prints, its `###` state heading, counts line and `- [state] what · holder · since` list, closing with one thread line, `🧵 Coordination thread · <label> (<id>)` for Project work or `🧵 State of play thread · <label> (<id>)` for territory work, using the work you report to, and no send or resume line; a run report to a conversational session or ad hoc work has no mark in its form line and no banner. The report's first non-blank line is its `#` heading, after front matter if the report has any. Run tools quietly under the ki-coordination [quiet-tools rule](../../../change-management/ki-coordination/references/standards-coordination.md#quiet-tools): run Git with `-q`, never paste gate, audit or Git output, and report each outcome in one line. Owner reports, run reports and banners omit routine push state and other sessions' stacked commits; if your own unit could not be published because its push failed, Done names the affected unit and reason. A hold report keeps nothing about pushes beyond a failure.

Temporary output goes in <temporary>/, outside every repository; never remove it yourself, ki agent close empties and removes it, so home what must survive first. Write nothing into `+/_WORK/ki.ways-of-working/` beyond your report.

Do not use background subagents. Never end your session while waiting.
