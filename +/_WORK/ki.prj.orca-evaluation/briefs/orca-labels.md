# Brief: orca-labels (ki.prj.orca-evaluation)

Read-only investigation for ki.prj.orca-evaluation ("KI > Techne > Orca evaluation"); change nothing, commit nothing, launch nothing.

Kris, 30 October 2026, with screenshots of Orca's ki-principal worktree card ("5 agents"): "sometimes the label is showing something else too, e.g. the one that should be orca-evaluation". The row for this coordinator session (a Claude Code chat started with `claude --name "KI > Techne > Orca evaluation (ki.prj.orca-evaluation)"` and renamed with /rename) at times shows "Monitoring background tas..." instead of "ki.prj.orca-evaluation - ...". Other rows show "ki.prj.mac-studio-setup...", "ki.sop.main - **Orca e...", "ki.prj.observatory - # [..." (apparently the start of the last reply).

Find out where Orca takes an agent row's label from and why it changes: the session name, the Claude Code session title, the latest prompt or reply, or a hook event (for example a background Bash task's description such as "Wait up to five minutes ..."). Evidence: Orca's shipped app code and settings, `orca worktree ps --json` (read only), its session stores under ~/Library/Application Support/orca/ (read from copies), and the Claude Code session title behaviour.

Report: the label's source and what makes it flip; whether a coordinator can keep a stable label (for example by how it names sessions or background tasks), whether an Orca setting does it, or whether it needs an Orca feature request; any decision for Kris as a query in owner-report shape (`### <TAG> - <title>`, Context, Query, Options with the recommended option first carrying its confidence and reason). British English, ASCII hyphens only.
