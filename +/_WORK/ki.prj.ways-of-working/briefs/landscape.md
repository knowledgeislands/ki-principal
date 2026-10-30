# Brief - landscape

Work: ki.prj.ways-of-working. Authority: Kris on 30 October 2026, agreeing the goals of a landscape study in a conversational thread: "Okay, yes." To be logged in decisions.md by this package's coordinator at launch. Skill: ki-work-design (design stage only). Successor to ORCA-FIT: it takes over that run's frame; ORCA-FIT is not relaunched.

## Goal

Kris wants Knowledge Islands to make him independent of any one editor, agent runtime or orchestrator, without becoming a lowest-common-denominator approach and without reinventing what the tools already do well. Map where every tool he uses or has evaluated sits, where Knowledge Islands complements them, where it duplicates them, and how the skills spread across all of it, then explain the picture plainly. In his words: "commission something which talks about or understands where all these tools sit together and how what I'm doing with Knowledge Islands is complementary to these so-called tools."

## Read

- Inputs that set the frame: design/orca-fit.md and design/orca-fit-explainer.md (ORCA-FIT, finished); +/_WORK/ki.prj.mac-studio-setup/plan069.report.md (first Orca trial); the digest quoted under Starting proposal.
- Work Process note: Pillars/Philosophy/Model/Processes/Work Process/Work Process.md; ki-coordination, ki-delegation, ki-agent-coordination-paperclip, ki-work-package, ki-work-roadmap, ki-binding and its runtime adapters, ki-tokenomics and its adapters; `ki --help`, `ki agent --help`, `orca --help` (read-only).
- Admin/Governance/Policies/Techne Programme Focus.md and Known Lands, for where Techné work may go.
- The island's own evaluations of tools: search Pillars, Resources, Streams, Calendar and +/_WORK across ki-principal, and the harness and tools repositories read-only, for Hermes Agent, herdr, OpenClaw, Paperclip, Warp, Cursor, Amp, opencode, Zed and anything else evaluated. List what you found and where.
- Current vendor documentation for each tool, including Zed's Delta product. Check versions installed on this host where they are; do not answer from memory, and say where you could not verify.
- The skills as installed (Claude Code and Codex skill lists, ki-agentic-harness and ki-techne-harness), with their sizes.

## Starting proposal (test it, do not assume it)

Four layers: editor (Zed), agent runtime (Claude Code, Codex), orchestrator (`ki agent`, Orca, Paperclip), durable method (Knowledge Islands). Skills cut across the layers as a matrix rather than sitting in one.

Three owners, from the digest of the first Orca trial: the work model (packages, seven states, queries, decisions in the owner's words, owner reports, authority, acceptance, roadmaps, handoffs as messages) stays with Knowledge Islands; agent dispatch (detached launch, queue, chaining, status, waiters, heartbeats) is not Knowledge Islands' remit and may move to a Techné agent; live orchestration (worktrees, task dependencies, live status, asks, gates) uses Orca where it fits, not assumed on headless hosts.

The handoff contract as the stable seam: a brief becomes a run or task with its ids in state.md; a done signal plus a report at a known path is the receive, its queries copied to queries.md and decisions to decisions.md; an owner decision is a query plus a blocking wait in the launcher, never a timed ask; workers never write the package; launcher chatter never goes into Git.

Naming as Kris and this thread left it: `ki-coordination` stays as the work-model skill (Kris floated renaming it `ki-orchestration`; the thread advised against, because coordinating is deciding work with Kris and orchestrating is driving agents - test this); the portable half of `ki-delegation` becomes `ki-orchestration`, with adapters `ki-orchestration-orca` and `ki-orchestration-paperclip` (from `ki-agent-coordination-paperclip`), and no `ki-orchestration-ki`. `ki agent` is the bare-bones default orchestrator for hosts without Orca or Paperclip, automation-friendly; Kris floated renaming it `ki orchestrate`. Whether it stays in the KI CLI or moves to a Techné agent with at most a thin KI shim is AGENT-HOME.

## Deliver, in design/

1. `landscape.md`, the design note, with numbered claims for at least two independent reviews:
   - Landscape: each tool placed in the layers, what it does natively today, its maturity, and its fit for Kris's hosts (sol, terra, a headless agent host).
   - Skills matrix: layers across, skills down; for each skill the layers it touches, its standing context cost, overlaps and conflicts with other skills, and a verdict - keep, merge, slim or retire.
   - Overlap ledger: for each Knowledge Islands capability (skills, `ki agent`, work packages, MCP binding, hooks, memory, wake and liveness), keep as method, bind thinly to a tool's native feature, or retire.
   - Orchestration family: the portable contract, `ki agent` as the floor, the Orca and Paperclip adapters, the `ki-coordination` lines that name `ki agent` directly, and a recommended name for each skill and the command.
   - Starting work at package level: today `ki agent` launches into a repository and Orca into a worktree; neither starts work "in this package, from its job list". State it as a requirement on the contract.
   - Answers, each with a recommended option: ORCA-REACH (does Orca run headless, across hosts, with Codex), AGENT-HOME, WAKE (how each launcher wakes the coordinator on done or blocked).
   - What the second brief needs: using Orca to work through the roadmap incrementally and get Knowledge Islands into a solid state. Name its inputs and prerequisites; do not design it.
2. `landscape-explainer.md`, for Kris: technical but free of AI jargon, built on Knowledge Islands' own imagery - islands, the Capital, Known Lands, ports, shipping routes for trades. A starting mapping to test, not force: repository as island; Principal as Capital; roadmap as the harbour works schedule; work package as a voyage's papers; agent runtime as ship and crew; orchestrator as port authority (`ki agent` a harbour master with a logbook, Orca a port with a control tower, Paperclip a shipping line); method as charter and charts; Git as the register; skills as seamanship manuals any crew carries aboard any ship. One layered diagram, the skills matrix as a picture, a one-table "who owns what". Under three pages.
3. Durability. Kris said the findings must be "durable, not just things that sit somewhere and never get picked up or learnt from". End landscape.md with a homing table: every finding, verdict and recommended change, its durable home (a decision record, a Pillars note through the Enactment Process, a skill change sent to the harness owning it as a messages.md line, a record the owning repository captures) and who must act. Propose the homes; create none.

Use British English and ASCII hyphens only. Change nothing outside this package's design/ folder; no standard, skill, record, hook, configuration or Orca state changes. Commit only your files by explicit path with `docs(work): ki.prj.ways-of-working landscape design`, pull --ff-only and push; normal hooks apply (hook-managed backups are fine; no manual stash, never bypass). Report to +/_WORK/ki.prj.ways-of-working/reports/landscape.report.md with Done, In Progress and Queries in ki-coordination owner-report query form. The coordinator may split the work into a landscape run and a skills-matrix run chained before the write-up, if one run would be too large.
