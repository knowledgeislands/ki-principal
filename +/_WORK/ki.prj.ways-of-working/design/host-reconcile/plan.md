---
note_type: streams/design
status: draft - October 2026
work: ki.prj.ways-of-working
run: ki-prj-ways-of-working
agent: host-reconcile-plan
written_at: 2026-10-31
author: Written with Claude
---

# Host reconcile: the plan in plain English

**Owning work:** `ki.prj.ways-of-working` · **Authority:** HOST-RECONCILE answers, Kris, 31 October 2026, 13:14 GMT, in [decisions.md](../../decisions.md) · **Builds on:** [findings](findings.md), the [merged host-sync report](../host-sync/report.md) and the [inbox wake design](../inbox-wake/design.md). This note changes nothing on either Mac; the Rig threads plan and install.

## 1. What runs, where

Each Mac has one Rig host thread, a chat thread Kris opens and leaves open: `personal.reg.rig-sol` on sol and `personal.reg.rig-terra` on terra. Inside it runs a small shell loop that uses no model time.

- **Every 15 minutes**, offset so the two Macs never run together: sol at :00, :15, :30 and :45, terra seven minutes later at :07, :22, :37 and :52. The offsets are a starting point, tuned once the first runs show how long a pass takes.
- **Each pass** fetches every repository and compares what it sees, locally and on GitHub, with the last pass. If nothing has changed, the pass stops there.
- **If something changed**, it fast-forwards every clean checkout that is behind and pushes every commit that exists only on this Mac, in both its primary and secondary areas. Fast-forward only, never forced, never merging, rebasing or stashing.
- **It wakes the model only for judgement:** two Macs' commits that have diverged, a dirty checkout in the way of a pull, or a failure. Everything else it does silently.
- **The same loop watches the thread's own `messages.md`**, as every coordinating thread now does, so a new line wakes the thread within minutes.

The loop lives and dies with the open thread. It is not a scheduled agent: if the thread closes, nothing syncs until it is reopened, and the next pass catches up with no backlog.

## 2. Primary and secondary

Rig drafts the map from the seats in chezmoi's `seats.yaml`, and Kris approves it. Read straight from the seats, with territories seated on both Macs going to the hub:

| Mac | Primary for | Secondary for |
| --- | --- | --- |
| sol (hub, Mac Studio) | Knowledge Islands, Personal, Legal, Valle Armonia, Sacred Inquiry, TechMedix, Equal Remedy | Humans Not Robots |
| terra (home, laptop) | Humans Not Robots | everything sol leads |

The chezmoi source repository is a named extra; Rig proposes which Mac leads it.

In practice:

- **The primary** is where that territory's work normally happens. Its Rig thread answers for the territory being level on GitHub and is the one that tells Kris when something has stayed stuck for two hours.
- **The secondary** keeps its copy current and pushes only commits it made itself.
- **They cannot overwrite each other.** Neither ever forces; if GitHub refuses a push because the other Mac got there first, the pass simply picks up the other Mac's work next time. A divergence is sorted out on the Mac that holds the unpublished commits, because only that Mac can, through a bounded resolve run.
- **The pull-back** comes free from the offsets: whatever terra pushes at :07 is on sol by :15, and whatever sol pushes at :00 is on terra by :07. Each Mac's next pass is the other's pull-back, never more than eight minutes later.

## 3. The Observatory

The Observatory watches and reports: which repositories are level, behind or ahead on each Mac against the approved map, and when each Mac last passed. It does no syncing. An ad hoc "sync now" through it is a later idea, not part of this plan.

## 4. What must exist first

1. **The `mgit` push guard** (MGIT-PUSH-GUARD, waiting in [ki.prj.tools-burndown](../../../ki.prj.tools-burndown/messages.md)): `mgit sync` pushes only when given `--push`, and a repository can veto pushing. Today it pushes by default with no veto, so no loop runs unattended on it.
2. **Each Mac's first supervised run:** one pass of the exact command over the approved map with Kris watching, testing that a dirty checkout is left alone and a divergence is reported, and timing the pass so it fits well inside the seven-minute gap.
3. **Keeping each Mac awake** while its host thread is open, as UNATTENDED-AWAKE asks. Rig chooses how. When terra sleeps or its lid closes, its passes are skipped and the next one catches up.

The earlier interim syncs (sol's SOL-SYNC, terra's SYNC-EVENING and its HNR sync) are retired once this runs.

## 5. Vega

Vega is the cloud agent host, the EC2 instance in the Techne account. It has no Rig thread, no seat and no place in the map. Under the [Techne Programme Focus](<../../../../../Admin/Governance/Policies/Techne Programme Focus.md>) its agents run only in sessions Kris opens, with no scheduled agents, and push only when Kris asks. It stays out of this plan.

## Rollout lines, drafted and not sent

For `personal.reg.rig-sol` (`personal-principal/+/_WORK/personal.reg.rig-sol/messages.md`):

> - 2026-10-31 · HOST-RECONCILE · KI > Model > Ways of working (ki.prj.ways-of-working): Kris on 31 October (HOST-RECONCILE answers): this host thread becomes sol's long-lived reconcile thread. Please plan, not install: a no-model shell loop inside the open thread, every 15 minutes at :00/:15/:30/:45, that fetches every repository, stops if nothing changed, else fast-forwards clean checkouts and pushes local-only commits in primary and secondary areas, fast-forward only, never forced, waking the thread only for divergence, a dirty checkout blocking a pull, or failure; the same loop watches this work's `messages.md`. Draft the primary/secondary map from `seats.yaml` (sol primary for the territories it seats, terra's HNR secondary) for Kris's approval, choose how sol stays awake while the thread is open, and plan one supervised run with Kris after `ki.prj.tools-burndown` ships MGIT-PUSH-GUARD. SOL-SYNC and the open HOST-SYNC interim query are superseded once it runs. Stop word: "stop the wake". Plan: [plan.md](https://github.com/knowledgeislands/ki-principal/blob/main/+/_WORK/ki.prj.ways-of-working/design/host-reconcile/plan.md).

For `personal.reg.rig-terra` (`personal-principal/+/_WORK/personal.reg.rig-terra/messages.md`):

> - 2026-10-31 · HOST-RECONCILE · KI > Model > Ways of working (ki.prj.ways-of-working): Kris on 31 October (HOST-RECONCILE answers): this host thread becomes terra's long-lived reconcile thread. Please plan, not install: a no-model shell loop inside the open thread, every 15 minutes at :07/:22/:37/:52, seven minutes after sol, that fetches every repository, stops if nothing changed, else fast-forwards clean checkouts and pushes local-only commits in primary and secondary areas, fast-forward only, never forced, waking the thread only for divergence, a dirty checkout blocking a pull, or failure; the same loop watches this work's `messages.md`. Terra is primary for Humans Not Robots and secondary for the rest, per the map sol's Rig thread drafts from `seats.yaml` for Kris's approval. Choose how terra stays awake while the thread is open (missed passes on sleep are skipped, no replay), and plan one supervised run with Kris after MGIT-PUSH-GUARD ships. SYNC-EVENING, the HNR sync and SYNC-NOW are superseded once it runs. Stop word: "stop the wake". Plan: [plan.md](https://github.com/knowledgeislands/ki-principal/blob/main/+/_WORK/ki.prj.ways-of-working/design/host-reconcile/plan.md).

For `ki.prj.tools-burndown` (`ki-principal/+/_WORK/ki.prj.tools-burndown/messages.md`):

> - 2026-10-31 · HOST-RECONCILE · KI > Model > Ways of working (ki.prj.ways-of-working): MGIT-PUSH-GUARD (adopted 25 October) is now a blocking prerequisite: Kris on 31 October set each Mac's Rig host thread to run `mgit sync --push` every 15 minutes, and no loop starts until `mgit sync` pushes only with `--push` and honours the per-repository `mgit.syncPush false` veto. Please say when it ships; SYNC-RECIPE can follow. Plan: [plan.md](https://github.com/knowledgeislands/ki-principal/blob/main/+/_WORK/ki.prj.ways-of-working/design/host-reconcile/plan.md).

## Decision still open

Query 1 of 1

## VEGA-SYNC: Leave vega out of host reconcile

**Where things stand**

- Kris asked for reconciliation "on each of the machines"; vega is the third.
- Vega is a cloud host with no Rig thread, no seat and no place in the map.
- The Techne Programme Focus allows it no scheduled agents and no push unless Kris asks.

**The options**

1. **Leave vega out for now** _(recommended, high confidence)_: its sessions push their own work when Kris asks, as today; revisit if vega ever holds long-lived checkouts of its own. _Why:_ the policy and the missing seat both point this way, and nothing is lost.
2. **Add vega as a third host** with its own Rig thread and offset, which needs a change to the Techne Programme Focus first.

Reply with 1 or 2, or your own words.
