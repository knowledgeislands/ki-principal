# Host reconciliation: what was proposed and decided

**Owning work:** `ki.prj.ways-of-working` · **Authority:** HOST-RECONCILE, Kris, 31 October 2026, in [decisions.md](../../decisions.md) · **Run:** `host-reconcile-find`, read-only, on sol

## HOST-RECONCILE - A long-lived per-host thread keeping every repository level

**Goal:** Establish what has been proposed and decided about a long-lived thread on each machine that keeps every repository fetched, synced and level across sol, terra and vega.

**Scope:** This package's decisions, queries and host-sync design notes; the Rig works `personal.reg.rig-sol` and `personal.reg.rig-terra`; `ki.prj.mac-studio-setup`, `ki.prj.chezmoi`, `ki.prj.observatory` and `ki.prj.tools-burndown` queues; [ADR-KI-PRINCIPAL-007](../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md); chezmoi `seats.yaml`; `tools-rig`, `tools-mgit` and Observatory docs. No other host was inspected.

**As of:** 31 October 2026, 13:06 GMT, Principal `cec884b4`, read on sol.

## 1. What Kris proposed

| When | Words | Where recorded |
| --- | --- | --- |
| 25 Oct, 01:04 GMT | MGIT-PUSH-GUARD, adopted after blind review: "sync pushes only with --push" | [ki.prj.tools-burndown messages](../../../ki.prj.tools-burndown/messages.md) |
| 28 Oct, 13:50 GMT | HOST-SYNC: "the sync process should always be run from this equivalent thread on both Terra and Sol ... each of them gets an offset ... we probably want to do a resync as well in short order after it"; primaries "on the hour", secondaries "five minutes later"; "the primary then needs to be able to read the secondary updates" | [live design note](../host-sync-and-reply-trades.md) |
| 28 Oct, 13:50 GMT | HOST-RESPONSIBILITY: the per-host map is "more to do with dot files", but "it would be good [if the] observatory knows or would expect something like this" | [ki.prj.observatory messages](../../../ki.prj.observatory/messages.md) |
| 28 Oct, 17:40 GMT | SYNC-EVENING, to terra: "check every 15 minutes ... make sure that everything is pushed" | [Terra sync brief](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/briefs/sync.md>) |
| 28 Oct, 20:58 GMT | SOL-SYNC, to sol: "can you run a regular 15 minute git sync and resolve any issues", "handle any drift in dotfiles too" | [Sol decisions](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/decisions.md>) |
| 28 Oct, 22:55 GMT | OBSERVATORY-SYNC: "given the fact that the observatory is running, why doesn't the observatory just do it?" | [ki.prj.observatory messages](../../../ki.prj.observatory/messages.md) |
| 28 Oct | MGIT-SYNC-ADOPT and MGIT-SYNC-JOB: the dotfiles sync should use `mgit sync`, and its regular run "could be one of the things" in a single host-based runner | [ki.prj.chezmoi messages](../../../ki.prj.chezmoi/messages.md) |
| 29 Oct, 16:40 GMT | SYNC-NOW: "`mgit sync` everything under `~/workspaces`, and then do the same here until its all settled" | [Terra decisions](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/decisions.md>) |
| 30 Oct, 01:20 GMT | Pick up HOST-SYNC early, keeping commits level across sol and terra | [decisions.md](../../decisions.md) |
| 31 Oct | HOST-RECONCILE: "some kind of long-lived thread which is doing this reconciliation on each of the machines ... I had proposed that it was done basically as part of the regular work under the rig-host ... potentially something to do with observatory" | [decisions.md](../../decisions.md) |

## 2. What was decided, and where

- **Placement of the Rig works.** Both Rig works' `work.md` already include "keeping [the host's] checkouts level with their remotes" in scope. This is the "regular work under the rig-host" Kris refers to; it is standing scope, not a schedule.
- **Seats.** [ADR-KI-PRINCIPAL-007](../../../../../Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md) (15 October): one seat and one standby per territory, Git the source of truth. Chezmoi `.chezmoidata/seats.yaml` binds terra (home) and sol (hub). It names no sync primary or secondary, and vega is not in it.
- **HOST-SYNC-DESIGN** (29 October): take HOST-SYNC up under `ki-work-design` and send the rollout as one line each to `personal.reg.rig-terra` and `personal.reg.rig-sol`.
- **HOST-REVIEW a)** (30 October): produced the [merged host-sync report](../host-sync/report.md). Its settled points: a chezmoi-carried per-territory map; one `mgit sync`-based recipe, fast-forward only, never forced; **each host's Rig thread owns its pass and resolves what it leaves**; Observatory observes and never gates execution; no host takes over another's work; one attended run per host before any recurrence. It adopts nothing itself.
- **Not yet decided.** Four queries stay open in [queries.md](../../queries.md): HOST-CADENCE, HOST-COVERAGE, HOST-SECONDARY-PUBLISH and HOST-READBACK, each recommending a), none taken under ACCEPT-BY-CRITERIA on 31 October. The older HOST-SYNC query sits in the same file. Observatory's SYNC-DIRECTION (which executor: a direct per-host Rig activity against attended passes) is open in [its queries](../../../ki.prj.observatory/queries.md). Sol's HOST-SYNC query (restart its 15-minute sync until the rollout lands) is open in [its queries](</Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-sol/queries.md>). MGIT-PUSH-GUARD and SYNC-RECIPE wait in the `ki.prj.tools-burndown` queue.

## 3. What exists today on each host

| Host | Sync running | What there is |
| --- | --- | --- |
| sol | None | No sync launch agent. SOL-SYNC ran every 15 minutes until 16:20 GMT on 29 October; its script and repository list remain in `~/.local/state/ki/agents/chezmoi/git-sync/`. An attended `mgit sync` on 30 October left sol level. `personal.reg.rig-sol` is the Rig thread. |
| terra | None reported | The half-hourly HNR `mgit sync` stopped at 13:52 GMT on 28 October; SYNC-EVENING ended at midnight; SYNC-NOW never ran. Terra's state carries SYNC-NOW and "take any HOST-SYNC outcome" as next steps. Not inspected from here. |
| vega | None | The Techne agent host, built by `ki.prj.agent-host`. It has no Rig work, no seat and no place in any sync design. |

The tools: `mgit sync` exists and still pushes ahead-only branches by default (no `--push` guard in `tools-mgit`, last commit `0a995a8`, 28 October, adding `mgit chain`). `tools-rig` has scheduled-job machinery but no sync job, and its docs do not mention sync. Observatory's docs do not cover sync coverage.

## 4. The gaps

1. **The four HOST-* decisions are unanswered**, so the rollout lines to the Rig queues have not gone.
2. **The push guard is not built.** MGIT-PUSH-GUARD, adopted 25 October, is undelivered, and the merged report makes a certified publish and pull-only `mgit sync` a prerequisite for any unattended pass.
3. **No primary/secondary map exists.** `seats.yaml` is the nearest; HOST-COVERAGE decides whether it seeds the map.
4. **Nothing runs.** Both hosts' interim syncs stopped on 28 and 29 October, and levelling now happens only when asked.
5. **Vega is outside everything:** no Rig work, no seat, no sync role. Kris named it in this brief; nothing yet says it should join.
6. **"Long-lived thread" is not yet a defined thing.** The merged report makes the Rig thread the owner and resolver but leaves how the pass runs (scheduled job or thread pass) to Observatory's SYNC-DIRECTION.

## 5. Recommended way forward

Recommended, confidence high: what Kris said on 31 October matches the design already merged, so no new design is needed. Kris answers the four open HOST-* queries and Observatory's SYNC-DIRECTION, taking a) in each. Then the HOST-SYNC rollout goes as one line each to `personal.reg.rig-sol` and `personal.reg.rig-terra`, naming each Rig thread as the long-lived owner of its host's levelling, with Observatory as observer. One message to `ki.prj.tools-burndown` asks for MGIT-PUSH-GUARD as the prerequisite. Vega stays out until Kris says it joins.

The confidence is high because Kris's HOST-RECONCILE words ("regular work under the rig-host", "potentially ... observatory") line up with the merged report's settled ownership and with SYNC-DIRECTION a). Until the rollout lands, the interim is Sol's open HOST-SYNC query and Terra's SYNC-NOW, both with their Rig owners.
