---
note_type: streams/design
status: merged report - October 2026
work: ki.prj.ways-of-working
run: ki-prj-ways-of-working
agent: landscape-merge
updated: 2026-10-30T03:00:00Z
author: Written with Claude
---

# Where Knowledge Islands sits among the tools: merged report

**Brief:** [landscape.md](landscape.md), with [the explainer](landscape-explainer.md) · **Reviews:** [landscape-review-claude.md](landscape-review-claude.md) (Claude Opus 5.5, Claude Code), [landscape-review-codex.md](landscape-review-codex.md) (Codex) · **Owning work:** `ki.prj.ways-of-working` · **Date:** 2026-10-30

**Status:** merged report under `ki-work-design`, awaiting Kris's decisions on ORCH-NAME, ORCA-REACH, AGENT-HOME, WAKE-SESSION, WAKE-DURABLE, WAKE-HOST and WORKTREE-OPTOUT in [queries](../queries.md). Nothing here is a standard; no standard, skill, record, hook, configuration or Orca state has changed.

## Contents

- [Summary](#summary)
- [Evidence added at merge](#evidence-added-at-merge)
- [Corrections to the design](#corrections-to-the-design)
- [Claims](#claims)
- [Differences left open](#differences-left-open)
- [Bearing on the queries](#bearing-on-the-queries)
- [Homing table](#homing-table)

## Summary

Both reviews accept the design's core: the work model and its authority stay with Knowledge Islands, dispatch is a replaceable mechanism behind a small contract, `ki agent` stays as the floor, and the names `ki-coordination`, `ki-delegation`, `ki-delegation-orca`, `ki-delegation-paperclip` and `ki agent` hold. Of the 30 claims, 6 are agreed by both reviewers as written, 17 are agreed with additions or qualifications, and 7 drew a Differ from at least one reviewer. Every Differ is resolved below against the evidence except two placements that are Kris's to choose: where the durable wake may run (WAKE-HOST), and whether Orca may run on `vega` inside owner-opened sessions (ORCA-REACH).

The material corrections, each raised by both reviewers unless marked:

1. **The durable wake is not deferred.** Kris chose the headless coordinator pass under WAKE-SUBSTRATE on 26 October 2026 ("lift the deferral in order"), the contract is written in `ki-coordination`'s Headless passes section, and the launchd job went to `ki.prj.chezmoi` and `ki.prj.mac-studio-setup` as messages. Only doorbells and extra liveness fields stay deferred. The design's claims 18, 20 and 28 and homing row 27 are stale.
2. **That decision meets the Techne Programme Focus on host, not on method.** The focus, set on 20 October, allows agents on `vega` and sol "only in sessions the binding owner opens, with no unattended or scheduled agents". A launchd pass is a scheduled agent. The later work-level decision does not amend a governance policy, so the pass may not run on sol or `vega` until the focus is changed through the Enactment Process; terra is outside the focus. Where it runs is a separate decision (Claude's review; Codex's review says installation and host permission are separate).
3. **The complement is narrower than claimed.** GitHub Issues, Linear and a Paperclip server are durable and cross-host. What no tool offers is the statement of the work in the repository's own Git, beside the content and readable without the tool, carrying the owner's decisions in the owner's own words, the queries, and acceptance kept apart from completion.
4. **`ki-batch` stays separate.** It is roadmap authority over a frozen set of Ready records, with a window and a completion target; folding it into a delegation footer would lose its review and closure evidence. The contract's footers cite it instead.
5. **The worktree baseline has more open prerequisites than two**, and it should take effect when the integrate command ships, with today's short-package pilot rule standing until then.
6. **The contract is a vocabulary, not yet an executable contract.** It lacks a capacity verb (`queue`), recovery after an uncertain outcome (`recover`), event identity and acknowledgement, and a rule for report availability across hosts.
7. **The package invariant needs a boundary.** "Workers never write the package" means the five package files; runs routinely write `design/` notes and reports in the work folder under their briefs, and under the worktree baseline those writes reach the coordinator only once integrated, so integrate precedes receive.

## Evidence added at merge

Checked on sol on 30 October 2026, read-only:

- The [Techne Programme Focus](<../../../../Admin/Governance/Policies/Techne Programme Focus.md>) names two hosts, `vega` and sol, and does not mention terra; its Sessions bound reads "Agents run on either host only in sessions the binding owner opens, with no unattended or scheduled agents". The policy was last changed in substance on 20 October, before WAKE-SUBSTRATE.
- This package's [decisions log](../decisions.md): the 26 October read-back of WAKE-SUBSTRATE a), "lift the deferral in order: write the headless coordinator-pass contract ... into `ki-coordination`, then send the launchd shell-check job as a line to ki.chezmoi and ki.mac-studio-setup"; ROLES-ORCHESTRATOR and ROLES-EITHER of 29 October.
- `ki-coordination`'s standard, Headless passes: the contract is written and "installs nothing"; whether the job has shipped is not established by the standard, nor by this report.
- `ki agent wait --help` (0.14.1): `--next` "marking it seen", `--interval` only, no timeout option. A bound has to come from the waiter around it, and an event marked seen by a waiter that then dies is not re-delivered.
- `ki work --help`: "read the work model". Moving write commands under it changes its stated contract.
- tools-ki `src/core/agent/worktrees.ts`: `--worktree` runs `git worktree add ... HEAD` from the supplied checkout, so the base is whatever that checkout has committed, not necessarily `main`.
- [Vendor landscape](landscape-vendors.md) carries about 90 vendor URLs; the design note itself cites none beside its claims.

Neither reviewer, nor this merge, made a network call: every vendor-documentation claim (Orca's beta and LAN-only marking, `orca-ide` on Linux, Cursor's merge-back and webhook, Delta, Oz, Hermes, herdr, Paperclip) remains as the design's research recorded it, unverified locally.

## Corrections to the design

Beyond the summary's seven, to carry into the design and explainer when they are revised:

- **The register is a plane, not the last layer.** Committed local state is not the register until it is pushed; draw the register beside every layer rather than at the bottom of a chain (Codex, claim 3).
- **Package homes.** Project packages live at the Capital, but a regular or ad hoc package may have an approved home elsewhere; `start` resolves the work's declared home (Codex, claim 16; explainer).
- **Isolation limits.** A worktree isolates tracked files and the index, not source stores, credentials, providers or other shared external state; the contract keeps its scope and ownership checks (Codex).
- **Remote report paths.** A report written on a worker host is not readable on the coordinator's host by default; an adapter that places workers remotely must prove report transfer and keep local integration distinct from publishing (Codex).
- **Measurements.** Description characters, file bytes, discovery entries and effective loaded tokens are different measures; the 26,337-byte output style is a file size, not a verified largest share of effective context. Line counts naming `ki agent` are 41 to 42 in `ki-coordination` and 30 to 31 in `ki-delegation` depending on the counting scope (both reviewers).
- **`ki-work-roadmap` in KB repositories.** It owns the record model the Streams adapter uses, so its presence beside `ki-repo-kb-streams` is not redundancy; homing row 24 is withdrawn (Codex).
- **Vocabulary drift.** The output style is still `ki-coordinator` for a role Kris now calls the orchestrator. One line in the [Work Process](<../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note should say that the orchestrator role is exercised under `ki-coordination` (Claude, claim 8).

## Claims

Marks: **A** Agree, **D** Differ, **+** Add. Claude is [landscape-review-claude](landscape-review-claude.md), Codex is [landscape-review-codex](landscape-review-codex.md).

| # | Claim, short | Claude | Codex | Merged position |
| --- | --- | --- | --- | --- |
| 1 | Tools span layers; bind to layers, never products | A | A | Agreed |
| 2 | Surface layer: editor and terminal, Obsidian as reader | A | A | Agreed |
| 3 | Register distinct from method, under every layer | A | + | Agreed, with Codex's refinement: the register is a supporting plane beside every layer, and a local commit is not in it until pushed |
| 4 | No tool offers durable cross-host work, owner authority in the owner's words, or acceptance apart from completion | D | D | **Resolved: narrowed.** Issues, Linear and a Paperclip server are durable and cross-host. The complement is the statement in the repository's own Git beside the content, readable without the tool, with owner decisions in the owner's words, queries and separate acceptance; vendor evidence on recorded approvals is incomplete, so the claim is about the whole contract, not each leg |
| 5 | KI should not build live views, multiplexing or remote placement | A + | A | Agreed, with additions: freeze, not remove; `ki agent watch` and `status --worktrees` stay as the floor's only views on `vega`, with enough status and recovery to honour the contract |
| 6 | `decide`, `reconcile`, `home`, `prompts` are work-model commands staying in KI | A + | + | **Agreed with correction:** they stay in KI but are not one kind. `decide` and `reconcile` write the decisions log; `home` binds a run to its work home and belongs with the run; `prompts` prints openers. `ki work` is read-only by its own help, so the split is designed command by command before any moves. Carried to AGENT-HOME |
| 7 | ROLES-ORCHESTRATOR means dispatch should not be `ki-orchestration` | A | + | Agreed on the conclusion, with Codex's qualification: the decision assigns a role, it does not reserve the word; the reason to avoid `ki-orchestration` for dispatch is ambiguity, not prohibition |
| 8 | `ki-coordination` keeps its name | A, reason differs | A | **Agreed, reason corrected:** the keep rests on cost mid-rollout (output style, 216,988-byte standard, every live package). The role word, if anything, favours renaming `ki-coordination` itself; that view stays as ORCH-NAME c) |
| 9 | Contract stays `ki-delegation`; adapters `-orca`, `-paperclip`; none for `ki agent` | A | A | Agreed |
| 10 | `ki agent` keeps its name under KI-AGENTS-NAME | A | + | Agreed; KI-AGENTS-NAME keeps the name but says nothing about moving commands under `ki work`, which is AGENT-HOME's matter |
| 11 | Twelve verbs | + | + | **Agreed as a starting vocabulary, with additions:** `queue` (submit, cap, cancel before start) and `recover` (uncertain control outcome); a shell-callable `status` for the headless-pass trigger; and, before adapters are built, event identity, delivery acknowledgement, outcome-unknown recovery and report-availability rules |
| 12 | Only Cursor provides `integrate` natively; it stays in `ki-git` with a `ki` command | A | D | **Resolved: restated.** Neither Orca 1.4.244 nor `ki agent` 0.14.1 exposes an integration step, checked locally; Cursor's merge-back is vendor documentation, unverified, and a native merge is not KI's verified serial integration in any case. `integrate` stays in `ki-git` with a `ki` command any launcher can call |
| 13 | Every writing run gets a worktree; read-only may opt out; trivial may not | + | + | **Agreed on the boundary, with timing:** package-folder writes count as writes and integrate precedes receive; the baseline takes effect when the integrate command and the open prerequisites land; until then checkout-isolation's pilot rule (short package runs on primary `main`, pathspec commits, landed check) and the existing short-package and roadmap-ledger exceptions stand, to be reconciled explicitly at rollout. Carried to WORKTREE-OPTOUT |
| 14 | Coordinators stay on primary `main` | A | A | Agreed (MAIN-NOT-WORKTREES) |
| 15 | Registry resolution and integrate are the two open prerequisites | D | D | **Resolved: widened.** Open: registry resolution of a linked worktree; an integrate command; the pathspec commit helper and landed check, ranked Now by checkout-isolation; a worktree base taken from committed `main` rather than the supplied checkout's `HEAD` (verified in `worktrees.ts`); and package anchoring to the primary checkout. Skills and dependencies for `ki agent` are claimed by its help and code but untested; for Orca, unverified |
| 16 | `start` takes a work id and job, resolves the target; the coordinator chooses | + | + | Agreed, with additions: a job touching two repositories becomes two units or names several targets; the record's repository may differ from the package's home; `start` resolves the work's declared home rather than assuming the Capital |
| 17 | Orca runs headless, across hosts, with Codex; server mode beta | A + | + | Agreed on capability as advertised by local help (`serve --supervise`, `worker-start --on`, `--agent codex`); the beta and LAN-only marking and `orca-ide` are vendor documentation, unverified locally; no remote run has been tested. Orca also drives more runtimes than `ki agent` |
| 18 | Orca on `vega`, a Techné dispatch agent and a durable wake each need Enactment | D | D | **Resolved in part, two placements left open.** A Techné dispatch agent: holds, "the execution fabric" is an idea. A scheduled headless pass on sol or `vega`: barred by the Sessions bound until an Enactment change. A durable wake as method: already authorised under WAKE-SUBSTRATE, so not an Enactment matter. Orca on `vega` inside owner-opened sessions: the focus's words do not bar it, and an always-on supervised `orca serve` accepting remote workers is closer to the execution fabric; open, under ORCA-REACH |
| 19 | `ki agent` stays in tools-ki as the floor, frozen against Orca duplicates | A | + | Agreed, with Codex's refinement: not a blanket freeze; no new features that duplicate Orca, while contract correctness, isolation and recovery work continue |
| 20 | One `wait` verb is the wake; durable wake stays deferred | D | D | **Resolved: split.** The session wake as one bounded `wait`, one armed at a time, holds, with additions: the bound comes from the waiter because `wait --next` has none; wake and acknowledgement are proved per runtime, since a Codex coordinator has no background-task re-invocation and an event marked seen can be lost. The durable wake is the headless pass under WAKE-SUBSTRATE, not deferred; its host is open. Carried to WAKE-SESSION, WAKE-DURABLE and WAKE-HOST |
| 21 | Orca skills conflict with `ki-delegation` and `ki-git`; load only where chosen | A | + | Agreed, narrowed: the conflict is in the broad discovery triggers; in substance "never substitute a non-Orca subagent tool" applies inside an Orca Run, and `orca-cli`'s preference applies "when Orca state is involved". Scoped loading still holds |
| 22 | Slim `ki-coordination`: contract verbs, split standard | A + | A | Agreed; counts as noted under Measurements; the headless-pass trigger also names `ki agent status`, so the contract needs a shell-callable status verb |
| 23 | Slim the Paperclip skill to an adapter and unload it | A | + | Agreed, with Codex's safeguard: keep company jurisdiction, repository authority, remote-delivery and roadmap-ledger rules, and check which declarations depend on it before unloading |
| 24 | `ki-batch`'s envelope becomes a contract footer | D | D | **Resolved: reversed.** `ki-batch` stays separate as roadmap authority over Ready records; the contract's footers cite it |
| 25 | `ki-tokenomics` cannot see most standing load; extend to user level | A | + | Agreed, refined: the portable policy already names user and runtime surfaces; extend the runtime adapters' consent-bounded evidence to them, keeping user-level files private |
| 26 | `ki-git` the single home of commit, push and worktree rules | A | + | Agreed, with Codex's refinement: footers, owner grants and package lifecycle keep their own authority requirements and cite `ki-git`; rendered instructions that must stay in place are not deleted |
| 27 | Skills, MCP and hooks bind thinly per runtime | A | A | Agreed; required hooks still need per-platform verification |
| 28 | Scheduled and unattended runs out of scope until taken up | D | D | **Resolved: stale.** Kris took up the headless pass under WAKE-SUBSTRATE, and the method already defines unattended windows and headless passes. The open question is host placement, not scope |
| 29 | Runtime memory a retrieval aid; durable memory in Git | A | A | Agreed |
| 30 | Second brief belongs to `ki.prj.orca-evaluation`, waits on decisions and prerequisites | A + | + | Agreed, prerequisites split by mode: an attended first pilot waits on the Orca opt-in decision, the adapter design note and the worktree gaps for the repositories it touches; an away grant and WAKE-HOST matter only for unattended stretches; naming need not block an attended pilot |

## Differences left open

1. **Where the durable wake runs.** The headless pass is chosen; its host is not. Claude's review recommends terra first at medium confidence, because terra is outside the focus, while noting that a terra pass sees only terra's runs under the host-local `ki agent status`. Codex's review keeps the rollout but treats host permission as a separate decision without naming a host. The alternatives are an Enactment change to the focus admitting the pass on sol, where most coordination and Orca now run, or no host until a work needs one. Kris decides under WAKE-HOST.
2. **Orca on `vega` inside owner-opened sessions.** Both reviewers say the focus's words do not bar it; the design treated it as needing Enactment. The merged recommendation keeps `ki agent` alone on `vega` as a deployment choice, with any Orca use there needing its own decision and remote-delivery proof. Kris decides under ORCA-REACH.

No other Differ is left open.

## Bearing on the queries

| Query | Design's recommendation | Claude | Codex | Merged |
| --- | --- | --- | --- | --- |
| ORCH-NAME | Keep all names; move four commands under `ki work` | a), medium | a), medium | a), names unchanged; the command move goes to AGENT-HOME; reason is rollout cost; high, reviewed |
| ORCA-REACH | Attended Macs, opt-in; `ki agent` only on `vega` | a), high | a), high, with the `vega` limit a deployment choice | a), qualified as Codex's; high |
| AGENT-HOME | Stay in tools-ki, frozen; split under `ki work`; Techné as Idea | a), medium (split destination) | a), high (design the split first) | a), with the split designed command by command and no blanket freeze; high |
| WAKE | One `wait` verb; durable wake deferred | Session a), high; durable not deferred, terra first, medium | Amend a): bounded wait proved per runtime; keep the headless-pass rollout, host permission separate; high | Split: WAKE-SESSION high; WAKE-DURABLE high; WAKE-HOST medium |
| WORKTREE-OPTOUT | Read-only only; no trivial exception | Read-only high; no trivial opt-out once integrate ships, medium | a), high, reconcile exceptions before rollout | a), with the baseline taking effect when integrate ships; high |

**Naming, decided:** the thread skill and output style keep their names, `ki-coordination` and `ki-coordinator`. This is ORCH-NAME-THREAD b), "Keep coordination", answered by Kris in the interactive prompt on 31 October 2026 ([decisions](../decisions.md#owner-answers-during-away-31-oct-0136-gmt-31-october-2026)); it settles claim 8 and the thread half of homing row 9. The dispatch contract, its adapters and the command remain open under ORCH-NAME-DISPATCH.

## Homing table

Updated from [the design's table](landscape.md#homing-table). Changed rows are marked **changed**, new rows **new**, a withdrawn row **withdrawn**. None of these homes is created by this run.

| # | Finding or change | Proposed home | Who acts |
| --- | --- | --- | --- |
| 1 | Five layers; tools placed by layers occupied; the register as a plane beside every layer (**changed**) | [Work Process](<../../../../Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note, a short section, through the Enactment Process | This package proposes; Kris approves |
| 2 | Knowledge Islands' complement, narrowed to the in-repository statement of work with owner decisions, queries and separate acceptance (**changed**) | Same Work Process section, and a governance decision record recording the stance | Kris decides; this package drafts |
| 3 | Tool placements and maturity, each volatile claim with its vendor URL and date from [Vendor landscape](landscape-vendors.md) (**changed**) | [Technology Radar](<../../../../Pillars/Engineering Practice/Technology/Technology Radar.md>) entries for Orca, herdr, Delta, Hermes, Ghostty, at its 31 October review, through the Enactment Process | Radar owner in Engineering Practice |
| 4 | Contract verbs, now with `queue`, `recover` and a shell-callable `status`; event identity, acknowledgement, outcome-unknown recovery and report availability; invariants with the five-file boundary and integrate before receive (**changed**) | `ki-delegation` standard rewrite | This package, which owns `ki-delegation` |
| 5 | `ki-coordination` launcher lines replaced by contract verbs; standard split; description shortened; receive rule says integrate precedes receive (**changed**) | `ki-coordination` change | This package |
| 6 | Orca adapter, including remote report-path availability and the narrowed trigger scope | New `ki-delegation-orca` skill in ki-agentic-harness, sent as a `messages.md` line to the harness's owning work; drafted with `ki.prj.orca-evaluation` | Harness owner; Orca evaluation package |
| 7 | Paperclip adapter renamed and slimmed, safeguards kept; dependants checked before unloading from ki-principal (**changed**) | Harness change as a `messages.md` line; project-skill declaration in ki-principal | Harness owner; ki-principal's repository owner |
| 8 | Orca skills loaded only where a package has chosen Orca | Rig or chezmoi skill-link configuration, as a line to `ki.prj.chezmoi` | `ki.prj.chezmoi` |
| 9 | Names: `ki-coordination`, `ki-delegation`, adapters, `ki agent` | A decision in this package's decisions log, then a decision record if adopted | Kris decides (ORCH-NAME) |
| 10 | Split of `decide`, `reconcile`, `home`, `prompts`, designed command by command; `ki work`'s read-only contract widened or a write group added; `home` stays with the run (**changed**) | tools-ki record captured by its owning work | `ki.prj.tools-burndown` |
| 11 | Render-only step and integrate command in `ki` | tools-ki records captured by its owning work | `ki.prj.tools-burndown` |
| 12 | Worktree prerequisites: registry resolution of linked worktrees; worktree base from committed `main`; package anchoring to the primary checkout; a tested skills-and-dependencies check (**changed**) | tools-ki records | `ki.prj.tools-burndown` |
| 13 | No new `ki agent` features that duplicate Orca; correctness, isolation and recovery continue (**changed**) | Decision in this package's log (OF-KI-AGENT, AGENT-HOME), message to `ki.prj.tools-burndown` | Kris decides; tools-burndown acts |
| 14 | Worktree baseline, opt-outs and merge model, effective when integrate ships; pilot rule and existing exceptions until then; isolation limits stated (**changed**) | `ki-git` change, plus a line in `ki-delegation`'s contract | Harness owner, by message |
| 15 | Orca repository setup links skills and dependencies | Orca evaluation trial step | `ki.prj.orca-evaluation` |
| 16 | Stale-worktree and disk-headroom doctor finding | tools-rig record captured by its owner | `ki.prj.mac-studio-setup` or `ki.prj.chezmoi` |
| 17 | Package-level `start`, resolving the work's declared home; multi-repository jobs (**changed**) | `ki-delegation` contract; tools-ki record for `ki agent`; Orca adapter for Orca | This package; tools-burndown; Orca evaluation |
| 18 | ORCA-REACH answer, including Orca on `vega` in owner-opened sessions (**changed**) | Decision in `ki.prj.orca-evaluation`'s log | Kris decides |
| 19 | AGENT-HOME answer; Techné dispatch as an Idea line | This package's decisions log; `Idea:` line on the Techne theme page through the Enactment Process | Kris decides |
| 20 | Session wake: the bounded `wait` verb, its bound supplied by the waiter, wake and acknowledgement proved per runtime (**changed**) | `ki-coordination` armed-check rule and `ki-delegation` contract | This package |
| 21 | `ki-batch` stays separate; the contract's footers cite it (**changed**, reversed) | `ki-delegation` contract line | This package |
| 22 | `ki-tokenomics` runtime adapters extended to user-level surfaces, consent-bounded; measures labelled separately (**changed**) | Harness change by message | Harness owner |
| 23 | Commit, push and worktree rules homed once in `ki-git`, others citing it and keeping their own authority requirements (**changed**) | Harness change by message | Harness owner |
| 24 | Whether KB repositories need `ki-work-roadmap` loaded (**withdrawn**: it owns the record model the Streams adapter uses) | None | None |
| 25 | `ki-trade` installed nowhere | Harness owner's review, by message | Harness owner |
| 26 | Delta trial decision still outstanding | [Delta evaluation](../../../../Streams/Projects/delta-evaluation.md) Project's Outcome | Kris decides |
| 27 | Durable wake is the headless pass under WAKE-SUBSTRATE, not deferred; its host to be chosen (**changed**, reversed from "no new home") | WAKE-DURABLE and WAKE-HOST in this package's queries, then either an Enactment change to the Techne Programme Focus or a recorded terra placement; the job's install stays with `ki.prj.chezmoi` and `ki.prj.mac-studio-setup` | Kris decides |
| 28 | Second brief's inputs and prerequisites, split into attended-pilot and unattended prerequisites (**changed**) | `ki.prj.orca-evaluation`'s `messages.md`, as a line | This package sends; Orca evaluation receives |
| 29 | One line saying the orchestrator role is exercised under `ki-coordination` (**new**) | Work Process note, through the Enactment Process | This package proposes; Kris approves |
| 30 | Design and explainer revised for these corrections: package homes, the narrowed complement, the register plane, the durable wake (**new**) | [landscape.md](landscape.md) and [landscape-explainer.md](landscape-explainer.md) | This package |
