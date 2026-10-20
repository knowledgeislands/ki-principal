# sweep-review - blind review of roadmap dispositions

## Task

Review, independently, how each of the open roadmap records below should be disposed of. Read each record named, in its repository, and anything those records link to inside their own repository. Apart from this brief, do not read anything under `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/`, any `*.report.md` file, or any `queries.md`, `decisions.md` or `messages.md`; the review must stand on the records alone.

**Background.** Kris, the owner, wants every Knowledge Islands repository's open roadmap down to single figures. The rules in force: no new records may be created; a rollout or a handoff to other work is not a roadmap item, and is carried instead as one line in the receiving work's `messages.md`, so a record of that kind can be cancelled and replaced by such a line; only work the receiving repository genuinely owns and defers stays a record. A merge cancels one record as `merged` and moves its goal, steps and decisions into the target, which must still read as one deliverable. A cancel records a reason and leaves the idea in its Project note.

For each query, choose one option, give your confidence (high, medium or low) and one line of reason. Where you would choose none of them, say what you would do instead.

## Queries

### M1 - Temporary output and a work-area content rule

**Context:** [KI-HARNESS-GOV-196](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-196-scratch-output-in-temp.md) decides where temporary output goes; [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md) sets the content allowed in a work folder; [KI-HARNESS-GOV-214](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md) sets what may be written into the working areas. All three are in the ki-agentic-harness repository.

**Query:** How should these three records be held?

**Options:** merge 196 into 200 and keep 214; merge both 196 and 214 into 200; keep all three.

### M2 - Two coordination rubric levels

**Context:** [KI-HARNESS-GOV-215](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md) and [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md) each change the level of one `ki-coordination` rubric item.

**Query:** Should they be one record?

**Options:** merge 215 into 220; keep both.

### M3 - Two diagram skill changes

**Context:** [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md) and [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md) are both `ki-diagrams` changes.

**Query:** Should they be one record?

**Options:** merge 221 into 205; keep both.

### M4 - Two `.ki.toml` declarations

**Context:** [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md) and [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md) each add a `.ki.toml` declaration that the Observatory reads.

**Query:** Should they be one record?

**Options:** merge 227 into 223; keep both.

### M5 - Three steps of one specification plan

**Context:** [KI-HARNESS-GOV-228](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-228-home-work-spec.md), [KI-HARNESS-GOV-229](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-229-home-acquire-spec.md) and [KI-HARNESS-GOV-230](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-230-knowledge-package-skill.md) are consecutive steps of one plan.

**Query:** Should they be one record?

**Options:** merge 229 and 230 into 228; keep all three.

### M6 - Two work-status views

**Context:** [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) and [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md), in tools-ki, both add output to `ki work status`.

**Query:** Should they be one record?

**Options:** merge 160 into 149; keep both.

### M7 - Four Observatory consolidations

**Context:** [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) holds rules, a mapping and an order for a set of consolidations; [KI-OBSERVA-VIS-032](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-032-library-instrument.md), [KI-OBSERVA-VIS-034](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-034-streams-instrument.md), [KI-OBSERVA-VIS-038](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-038-machine-instrument.md) and [KI-OBSERVA-VIS-045](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) are consolidations of views. With no new records allowed, a merged consolidation could not later become its own record again.

**Query:** How should the four consolidation records be held?

**Options:** merge all four into APP-044 as numbered steps; keep all five; merge some and keep others (name which).

### M8 - Two routing-core tasks

**Context:** [KI-MCP-M365-TOOL-018](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-018-extract-the-routing-core.md) and [KI-MCP-M365-TOOL-020](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/KI-MCP-M365-TOOL-020-distribute-the-routing-core.md), in mcp-m365, are tasks in one email-routing design, planned in another territory's work.

**Query:** Should they be one record?

**Options:** merge 020 into 018; keep both.

### C1 - Coordinator update shape

**Context:** [KI-HARNESS-GOV-216](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-216-three-part-updates.md) changes the shape of a coordinator's progress updates in the `ki-coordination` standard. The work that owns ways of working in Knowledge Islands Principal also owns that standard's wording.

**Query:** Should this stay a harness record or become a message to that work?

**Options:** convert to a `messages.md` line to the ways-of-working work; keep as a record.

### C2 - Banner glyph wording

**Context:** [KI-HARNESS-GOV-226](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-226-banner-rendered-glyphs.md) changes the wording of the banner's glyphs in the coordination standard, a change the same ways-of-working work owns.

**Query:** Should this stay a harness record or become a message to that work?

**Options:** convert to a `messages.md` line to the ways-of-working work; keep as a record.

### C3 - Timeline and calendar skill

**Context:** [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) proposes a timeline and calendar capability. The owner has handed it to a timelines Project in Knowledge Islands Principal; where it would be built (the harness, tools-ki or a shared package) is undecided.

**Query:** Should the harness keep a record for it?

**Options:** convert to a `messages.md` line to the timelines work and cancel the record; keep the record with its project set to that work.

### C4 - CLI convention departures

**Context:** [KI-TOOL-KI-CLI-151](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-151-cli-conventions-departures.md) lists places where `ki` departs from its CLI conventions. The owner has decided each departure is fixed at the next change to the command concerned.

**Query:** Should this stay a record?

**Options:** convert to a standing `messages.md` line to the tools-burndown work; keep as a record.

### C5 - Unmanaged configuration scan

**Context:** [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md), in tools-rig, proposes scanning for configuration that chezmoi does not manage; the owner described it as "a fairly regular thing". Knowledge Islands Principal records recurring obligations as Activity notes.

**Query:** Should this stay a Rig record?

**Options:** convert to a `messages.md` line to the chezmoi work, to become an Activity; keep as a Rig record.

### C6 - Stale Rig link on one machine

**Context:** [KI-TOOL-RIG-DIST-011](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-DIST-011-stale-terra-rig-link.md) fixes a stale Rig link on one machine, `vega`.

**Query:** Should this stay a Rig record?

**Options:** convert to a `messages.md` line to the agent-host work; keep as a Rig record.

### X1 - Local resolution targets

**Context:** [KI-HARNESS-GOV-170](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-170-keep-resolution-targets-local.md), opened 9 October, would keep record resolution targets local to their repository. Records now link other repositories' records by absolute path.

**Query:** What should happen to it?

**Options:** cancel as superseded; keep.

### X2 - Moving a thread between hosts

**Context:** [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md), opened 14 October, would move a coordinating thread from one host to another. Work packages now live in Git with their briefs; the run queue is local to a machine.

**Query:** What should happen to it?

**Options:** cancel as superseded; keep.

### X3 - Skill-area stats badge

**Context:** [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md), opened 16 October, adds a statistics badge to skill areas. The owner has asked for it to be re-explained.

**Query:** What should happen to it?

**Options:** cancel as won't do for now; keep in triage.

### X4 - Release contract

**Context:** [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md), opened 13 October and on hold, defines a release contract; its hold names a condition in the record.

**Query:** What should happen to it?

**Options:** cancel as won't do for now; keep on hold.

### X5 - Menu-bar order persistence

**Context:** [KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md), opened 14 October with a Future horizon, investigates keeping menu-bar order; it relates to [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md).

**Query:** What should happen to it?

**Options:** cancel as won't do for now; merge into CORE-053; keep.

### X6 - GitHub Desktop repository list

**Context:** [KI-TOOL-RIG-CORE-057](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md), opened 14 October and in triage, would have Rig manage GitHub Desktop's repository list.

**Query:** What should happen to it?

**Options:** cancel as won't do; keep.

## Limits

- Read only. Change, stage or commit nothing; create no record. No remote call of any kind.
- Apart from this brief, do not read `+/_WORK/`, any report, `queries.md`, `decisions.md` or `messages.md`.
- British English, ASCII hyphens, they/them.

## Report

One line per query: `<tag>: <chosen option> (confidence <level>) - <reason>`. Then any record you think was misread, one line each. Nothing else.
