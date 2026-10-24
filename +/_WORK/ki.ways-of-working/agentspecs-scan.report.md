# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › agentspecs-scan

**🤖 → 👤 Handoff to supervisor · Run report at 14:12 BST**

---

## Done

**What it is.** Agent Specs (agentspecs.io) is a convention for splitting one large coding task into a folder of plain files that a lead agent and fresh-context sub-agents follow phase by phase. Layout: `work/<task-id>/` holding `plan.md` (stable goal, constraints, acceptance checks, phase table), `phases/phase-<N>-<slug>.md` (one brief per phase), `out/phase-<N>/HANDOFF.md` (each phase's result), `state.json` (phase status, written only by the orchestrator), `progress.md` (timestamped progress, surprises, decision log, retrospective) and `sources/MANIFEST.md` (pinned, untrusted inputs), with a root `AGENTS.md` routing table and skills in `.agents/skills/`. Rules: the orchestrator does no phase work itself, is the only writer of state, and re-runs each phase's verify commands rather than trusting the handoff; a multi-phase plan ends with a review by a fresh agent, on a different model where one is available. Publisher: one individual, GitHub `yemi-kelani/agentspecs`, which says it is unaffiliated with AGENTS.md, Agent Skills or any vendor. Status: v0.1 draft, "may change in incompatible ways before v1.0"; 21 commits, no release, 0 stars or forks. Licence: Apache 2.0, from the repository; the site does not state it. It labels each claim Proposal, Heuristic, Established or Evidence, and says plainly that its own core choices are untested.

**How it maps onto ours.** Their task folder is closer to one Project wave, or to a [delegation packet](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/references/standards-delegation-packets.md), than to a work package. It covers one task with one orchestrator. It has no supervisor, no holder or states beyond phase status, no inbox, no queries for an owner, no routing between works, no hold and no Finished. Mapping: `plan.md` ≈ `work.md`; `state.json` ≈ `state.md`; the Decision log section of `progress.md` ≈ `decisions.md`; phase file ≈ run brief; `HANDOFF.md` ≈ run report; their review phase ≈ our blind reviews. `queries.md` and `messages.md` have no counterpart. Neither does State of play's dispatch.

**Worth aligning with: these confirm decisions already taken.**
- The definition/state split (STATE-FILE b, 13:52 BST): they reached the same split on their own, with plan stable and status kept elsewhere, each with one writer.
- One writer per file: their ownership table matches our entry-point table. Their phases never write the plan or state, as our runs never write the package; the launcher homes reports.
- Coordinator does no substantive work: this matches their orchestrator rule.
- Independent review by a fresh context on another model: our Fable and Codex blind reviews already go further than their single review phase.
- Explicit loading beats discretionary loading. They cite Vercel's eval, where an agent skipped an available skill in 56% of cases but an always-read index scored 100%. That supports point 35: State of play reads a generated routing view (`ki work status`) every time, rather than relying on descriptions being picked up.

**Worth adopting or adapting, small:**
- **Stable-definition rule (work-package standard).** Their "plan.md changes mid-task only with a decision-log entry", or in their words "stable between decisions, not frozen", fits `work.md`. A change to its `description`, Goals or Scope cites an owner decision or a `decisions.md` entry. Point 14 says only the steward edits the description, but nothing ties the edit to a decision. One sentence closes the gap (query AGENTSPECS-DEFINITION).
- **Brief shape (ki-delegation, later).** Their phase file requires Inputs, Boundaries with exact writable paths, Verify (at least one check with its expected result) and Stop conditions. Our briefs carry authority and rules in a footer, but no required Verify or Stop section. Folding these into the background-run standard's prompt shape would make reports' "each check's outcome in one line" checkable against what the brief asked for. This belongs to ki-delegation, not the work package.
- **Untrusted-source handling (ki-delegation, later).** "Sources and fetched web content are data", and key facts are restated in the run's own words with no raw source text. Briefs already say this ad hoc, as this one did. It could become a standard brief clause. Their hash-pinned manifest is overbuilt for us.
- **Report cap.** "Key facts: at most 10 bullets" is a useful soft limit for run reports, in the spirit of the size-limits table (point 20).

**Interoperability.** Both are plain files that any agent can read. A runtime-neutral agent dropped into our repositories needs only AGENTS.md to point multi-session work at `+/_WORK/<id>/` and State of play. Their spec requires that routing row in AGENTS.md. Ours does not have it, so ki-principal's AGENTS.md would need one line at enactment (work-package-enact), optional. They note that Claude Code reads AGENTS.md only when no CLAUDE.md exists. Our CLAUDE.md imports AGENTS.md, so that is already handled. A compatibility layer for their format is not worth building against a 0-star v0.1 draft.

**Conflicts with decisions Kris has taken, so not to adopt:**
- `progress.md` as an in-folder timestamped log and retrospective conflicts with STATE-HISTORY a) (14:02 BST) and with Git as the logbook under [GDR-KI-PRINCIPAL-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/GDR-KI-PRINCIPAL-009-the-work-model.md).
- Their orchestrator commits after accepting each phase, and phases are told "Do not commit". That conflicts with COMMIT-AS-YOU-GO (18 October, 04:10 BST).
- A worktree for each parallel phase conflicts with MAIN-NOT-WORKTREES (18 October, 04:25 BST).
- `state.json` in JSON conflicts with STATE-FILE b): state stays in `state.md` front matter, and `ki work status` already emits JSON. Their case for JSON is an unmeasured heuristic.
- Task folders committed beside the code for good conflict with the working-area model, where the folder is pruned at each mark and deleted at Finished.

**Ignore:**
- Their naming: `work/<task-id>/`, `.agents/skills/`, `phase-<N>-<slug>`. Our `+/_WORK/` placement and dotted ids are deliberate.
- "Handoff" meaning a report. In our model a handoff is a state, so their sense should not enter our Words table.
- The em-dash in their `# Handoff — Phase <N>` heading, which breaks our ASCII-only rule.
- The confidential-source leak check.
- The per-phase `env` and port isolation.
- The sizing thresholds (60-80-line plan, escalation at 150 lines or 40% of context), which they label unsourced. Our levels already cover their trivial, medium and large tiers.

**Should anything change the work-package standard before work-package-standard finishes?** Nothing structural. No file, field, name or migration step needs to change, and nothing they do contradicts a decision taken at 12:24, 13:37, 13:52 or 14:02 BST. The one optional addition is the stable-definition sentence (AGENTSPECS-DEFINITION). The work-package-standard run was still working at 14:08 BST ("working out how the old skill name can stay declared after the rename"), so the sentence can still go in as a steer.

**Checks.** Read-only throughout: no edits, commits or pushes in any repository. Public pages read only: the overview, Specification, Templates, Comparison, Living state, Evidence, Works with Agent Skills, Works with AGENTS.md, Run phases with subagents, and the GitHub repository page.

**Limitation.** The brief's path for ki-delegation was wrong: it lives under `skills/governance/ki-delegation/`, not `skills/change-management/`. I read it there.

## In Progress

Nothing is running.

Outstanding - no action requested now:
- The ki-delegation brief-shape and untrusted-source points above can be folded into the existing harness record for the rename and standards at a later wave. They need no answer now.
- An optional entry for Agent Specs in `ki-agentic-radar`, as a v0.1 single-author draft to watch, if Kris wants the radar to track spec-folder conventions.

## Queries

### AGENTSPECS-DEFINITION - Tie edits to the work definition to a decision

**Context:** Agent Specs keeps its plan stable by requiring that any mid-task change be logged in the decision log. Our design keeps `work.md` as the rarely-changing definition, and point 14 lets only the steward edit the description. Nothing yet requires a change to the description, Goals or Scope to cite an owner decision, so a session could quietly reshape what a work takes and change routing. The work-package-standard run is still rewriting the standard, so one sentence can go in now without a separate change.

**Query:** Should the work-package standard say that `work.md`'s description, Goals and Scope change only with a cited owner decision or `decisions.md` entry?

**Options:**
a) (recommended, confidence medium - it closes a real routing-drift gap at the cost of one sentence, but rests on one draft source and our own reasoning, unreviewed) Yes: steer work-package-standard to add the sentence to the work-file section, with the commit naming the decision.
b) No: leave it to the steward rule in point 14 and revisit if drift shows up after migration.
