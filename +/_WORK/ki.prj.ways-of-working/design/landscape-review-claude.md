---
note_type: streams/design
status: review - October 2026
work: ki.prj.ways-of-working
run: ki-prj-ways-of-working
agent: landscape-review-claude
written_at: 2026-10-30T02:20:00Z
author: Written with Claude
---

# Landscape: review by Claude Opus 5.5

**Reviewer:** Claude Code, Claude Opus 5.5. **Date:** 2026-10-30. **Read-only:** yes, apart from this note.

**Scope.** One of two independent reviews of [landscape](landscape.md) under `ki-work-design`, against [its brief](../briefs/landscape.md) and [the explainer](landscape-explainer.md). Not read: `queries.md`, any run report, the other reviewer's output.

**Evidence checked on sol, 30 October 2026, 02:00 to 02:20 GMT:** `ki --version`, `ki --help`, `ki agent --help` and the `launch`, `new`, `wait`, `close`, `status` and `work` subcommand help; `orca --help`, `orca serve --help`, `orca orchestration worker-start --help` and `check --help`; the [Techne Programme Focus](<../../../../Admin/Governance/Policies/Techne Programme Focus.md>); this package's [decisions log](../decisions.md) for ROLES-ORCHESTRATOR, KI-AGENTS-NAME and WAKE-SUBSTRATE; the `ki-coordination` standard's headless-pass section; [checkout-isolation](checkout-isolation.md) for MAIN-NOT-WORKTREES and the worktree gaps; the installed `SKILL.md` descriptions in Claude Code (user and ki-principal project links), the Orca `orchestration` and `orca-cli` skills, `ki-tokenomics`, and the harness tree for `ki-trade`. No vendor web pages were read: this run makes no network calls, so every vendor-documentation claim (Cursor merge-back, Orca server beta, Delta, Oz, Hermes, herdr, Paperclip) is unverified here and marked so.

## Summary

The note is accurate where it rests on local evidence: `ki agent`'s 17 subcommands, its `--worktree`, `--wait-for` and `wait --next`; Orca's `serve --supervise`, `worker-start --on`, the agent list including `codex`, and the absence of any merge command; the skill description sizes (each within two characters); the 217 KB standard and the 26,337-byte output style; the ROLES-ORCHESTRATOR and KI-AGENTS-NAME quotes; the Techne focus wording. Three corrections matter:

1. **WAKE-SUBSTRATE is mis-stated.** The note says a durable wake "stays deferred under WAKE-SUBSTRATE". The decisions log (under its entry headed 2026-10-25 02:56 GMT) and the `ki-coordination` standard's headless-pass section, which dates the choice 26 October, both record that Kris chose the headless coordinator pass as the durable wake and lifted the launchd deferral in order: contract first, then the job sent to Rig and chezmoi. Only doorbells and extra liveness fields stay deferred.
2. **That decision collides with the Techne focus on sol, not on terra.** The focus bars "unattended or scheduled agents" on `vega` and sol only. A launchd headless pass is a scheduled agent. Terra is outside the focus. The note's claims 18, 20 and 28 and homing row 27 ("already homed ... no new home") miss this; it needs a placement decision.
3. **Worker writes into the package folder are routine.** The invariant "workers never write the package" sits beside briefs, this one included, that have runs write `design/` notes and `reports/` in the package folder and push to `main`. Under the worktree baseline those writes are invisible to the coordinator until integrated. The contract should say the invariant covers the five package files, and that `integrate` precedes `receive`.

## Claims

| # | Mark | Reason | Evidence checked |
| --- | --- | --- | --- |
| 1 | Agree | Orca is surface and orchestrator, Hermes runtime and orchestrator; binding to a layer is the only stable seam | `orca --help` (worktrees, terminals, orchestration, automations in one tool) |
| 2 | Agree | Ghostty, herdr and Orca panes are where runs are watched; Obsidian reads the primary checkout | Note's evidence table; checkout-isolation line 116 (Obsidian reads the live primary checkout) |
| 3 | Agree | The method travels with the harness, the record with each repository's remote; they fail and move differently | Harness installed under `~/.local/share/ki/harnesses`; packages under `+/_WORK/` in Git |
| 4 | Differ | Overstated on the first leg: GitHub Issues, Linear and a Paperclip server are durable and cross-host, and `ki-work` already adapts to the first two. What no tool offers is the statement in the repository's own Git, beside the content, readable without the tool, with queries and owner decisions attached. The other two legs hold | `ki-work` description; note's own overlap ledger row 2 |
| 5 | Agree | Add: freeze, not remove - `ki agent watch` and `status --worktrees` already exist and are the floor's only views on `vega` | `ki agent --help` |
| 6 | Agree | Add: `home` is the run-to-package seam rather than pure work model (it records a run's work folder), and `ki work` is described as "read work model"; moving `decide` and `reconcile` there changes its read-only contract, so either widen `ki work`'s description or give writes their own group | `ki agent --help`; `ki work --help` |
| 7 | Agree | Quote verified: "the thread agent is effectively the orchestrator of the state machine" | Decisions log, ROLES-ORCHESTRATOR, 2026-10-29 |
| 8 | Agree | Differ on the reason: the role word supports Kris's floated rename of `ki-coordination` to `ki-orchestration` rather than ruling it out; the sound reason to keep it is cost mid-rollout (output style, 217 KB standard, every live package). The output style is still "ki-coordinator" for a role now called orchestrator; that drift wants one line in the Work Process note | ROLES-ORCHESTRATOR; `wc -c` on the standard (216,988 bytes) |
| 9 | Agree | "Delegation" names what the orchestrator does to workers and collides with neither the role word nor Orca's `orchestration` skill | Orca skill name; `ki agent` describes itself as "under the ki-delegation run contract" |
| 10 | Agree | Quote verified: "Keep "agents"; ways of working logs the decision in its decisions log and nothing is renamed" | Decisions log, 2026-10-25 01:56 entry |
| 11 | Add | The twelve verbs omit capacity: `ki agent queue`, `dispatch` and `dequeue` implement "about three running, the rest queued", which the coordinator style requires; add `queue` (submit, cap, cancel before start). `recover` (uncertain control effect) is worth naming too | `ki agent --help`; coordinator output style |
| 12 | Agree | No merge in Orca 1.4.244 or `ki agent` 0.14.1. Cursor's merge-back is vendor documentation, unverified here | `orca --help` grep for merge: none; `ki agent --help` |
| 13 | Add | Agree on read-only opt-out and coordinators. Add: runs that write into the package folder (design notes, reports) need integrate before receive, or the coordinator reads a stale tree; and until an integrate command exists every trivial run means a manual merge, so "no trivial opt-out" should take effect when integrate ships, with checkout-isolation's pilot rule (short package runs on primary `main`, pathspec commits) until then | checkout-isolation steps 1 and 4; this brief, which has the run write in the package |
| 14 | Agree | MAIN-NOT-WORKTREES verified: "you should be able to just work on the main" (18 October) | checkout-isolation line 116 |
| 15 | Differ | Three prerequisites are open, not two: checkout-isolation ranks the pathspec commit helper and landed check as "Now", and coordinators plus opted-out runs keep sharing the primary checkout. Skills and dependencies for `ki agent` are closed by its help text only, not by a test | `ki agent launch --help` (`--worktree`: "installed dependencies and project skills"); `ki registry --help` has no worktree option; checkout-isolation step 1 |
| 16 | Add | Agree; add that a job touching two repositories either becomes two units or `start` takes several targets, and the record id's repository may differ from the package's Capital | Note's own Starting work section |
| 17 | Agree | `serve` with `--supervise` for launchd or systemd, `worker-start --on <saved-environment>`, `--agent codex` all present. "Beta", the LAN-only note and `orca-ide` on Linux are not in the local help: vendor-only, unverified here. Add: Orca drives more runtimes than `ki agent` (Cursor, opencode and others) | `orca serve --help`; `orca orchestration worker-start --help` |
| 18 | Differ | Right for a Techné dispatch agent ("the execution fabric" is an idea) and for any scheduled pass on sol or `vega`. Orca on `vega` used only in owner-opened sessions is arguably agent-host workspace setup, which the focus allows; an always-on supervised `orca serve` accepting remote workers is closer to the execution fabric. Kris decides which; the note should not presume full Enactment for the session-only form | Techne focus, Focus and Operating bounds sections |
| 19 | Agree | The only launcher allowed on `vega` today; OF-KI-AGENT's freeze is ORCA-FIT's open choice | orca-fit.md, OF-KI-AGENT |
| 20 | Differ | The session wake as one `wait` verb holds. "Durable wake stays deferred" does not: WAKE-SUBSTRATE chose the headless pass on 26 October and lifted the launchd deferral in order. Add: the "background task re-invokes the session" path is Claude Code's; a Codex coordinator has no such re-invocation, so its wait is only as good as its next turn | Decisions log 2026-10-25 02:56 entry; `standards-coordination.md` line 1035 |
| 21 | Agree | The conflict is in the triggers ("coordinator loops", "decomposing work across agents", "handoff"). In substance the rules are narrower than the note says: "never substitute a non-Orca subagent tool" applies inside an Orca Run, and `orca-cli` prefers itself over raw worktrees only "when Orca state is involved" | `~/.agents/skills/orchestration/SKILL.md` lines 22 to 28; `orca-cli` description |
| 22 | Agree | 42 lines name `ki agent` in `ki-coordination` (note: 41) and 30 in `ki-delegation` (note: 31), in the installed and checkout copies alike; immaterial. Add: the headless-pass trigger also names `ki agent status`, so the contract needs a status verb a shell job can call | grep over both copies; standard line 1037 |
| 23 | Agree | 344-character description loaded in ki-principal while Paperclip is not running | ki-principal `.claude/skills` |
| 24 | Differ | `ki-batch` is roadmap authority over Ready records for `ki-implement`, usable with or without background runs; folding it into the dispatch contract couples roadmap lifecycle to the launcher. Keep it separate and have the contract's footers cite it | `ki-batch` description |
| 25 | Agree | `ki-tokenomics-claude` audits "repository evidence"; the output style and user skills sit outside it. Extending it must respect that user-level files are private | Skill descriptions; `ls ~/.claude/output-styles` |
| 26 | Agree | One home with citations is the method's own rule for duplicated text | Note's skills matrix |
| 27 | Agree | `ki-binding` with per-runtime adapters is already this shape | Skill descriptions |
| 28 | Differ | Stale: Kris took up one scheduled thing, the headless pass, under WAKE-SUBSTRATE. The focus forbids it on sol and `vega`, not on terra. The open question is placement, not scope | Techne focus Sessions bound; WAKE-SUBSTRATE |
| 29 | Agree | Matches the user's `memory-scope.md` rule | `~/.claude/memory-scope.md` |
| 30 | Agree | Orca evaluation is the natural owner. Add a prerequisite: the WAKE placement decision above, since a roadmap pass over hours needs either Kris present or a sanctioned wake | Note's What the second brief needs |

Not checked: the explainer's prose against the note beyond the naming and wake lines, which repeat claims 9 and 20 and inherit the same correction.

## Recommendations on the open questions

**ORCA-REACH: option a), high confidence.** Orca on attended Macs only, by logged package opt-in; `ki agent` alone on `vega`. Locally verified: the headless server and remote placement exist, nothing is paired, and the focus bars unattended agents on both Techné hosts. Revisit after the server mode leaves beta, through the route claim 18 describes.

**AGENT-HOME: option a), medium confidence.** `ki agent` stays in tools-ki as the floor, Techné dispatch kept as an `Idea:` line. Medium because of the split's destination: `ki work` is read-only by its own description, so `decide` and `reconcile` need either a widened `ki work` or their own command group; `home` belongs with the run, not the work.

**WAKE: option a), high confidence for the session wake; the durable wake needs a separate placement decision.** One bounded `wait` verb per launcher, one armed at a time. The durable wake is not deferred: WAKE-SUBSTRATE's headless pass stands, and it can run on terra under the focus as written, or on sol only after an Enactment change. Recommended for that split-off question: terra first, medium confidence, because sol is where Orca and most coordination now run and a terra-only pass watches only terra's packages.

**WORKTREE-OPTOUT: read-only runs may opt out, high confidence; trivial runs get no opt-out once `ki` has an integrate command, medium confidence.** Until then, checkout-isolation's pilot rule keeps short package runs on primary `main` with pathspec commits and the landed check. Package-folder writes count as writes.

**Naming: keep `ki-coordination` and `ki-delegation`, adapters `ki-delegation-orca` and `ki-delegation-paperclip`, no `ki agent` adapter, `ki agent` keeps its name; medium confidence.** The keep is on cost, not on the role word, which favours Kris's floated rename; the "coordinator" versus "orchestrator" drift should be settled in prose in the Work Process note rather than by renaming skills mid-rollout.

## Homing additions

| Finding | Proposed home | Who acts |
| --- | --- | --- |
| WAKE-SUBSTRATE's headless pass versus the Techne focus on sol | A query in this package, then either an Enactment change to the focus or a recorded terra placement | Kris decides |
| The package invariant covers the five files; integrate precedes receive | `ki-delegation` contract and `ki-coordination` receive rule | This package |
| A `queue` verb for capacity, and a shell-callable status verb | `ki-delegation` contract | This package |
| `ki work` read-only contract versus moved write commands | The tools-ki record for the split | `ki.prj.tools-burndown` |
