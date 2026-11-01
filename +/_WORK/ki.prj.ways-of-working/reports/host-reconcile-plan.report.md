# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › host-reconcile-plan

**🤖 → 👤 Handoff to supervisor · Run report at 13:15 GMT · last mark 13:05 GMT**

---

## Done

- Wrote the one-page [host-reconcile plan](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/host-reconcile/plan.md) for Kris, committed alone as `4ec55e13`; the repository audit and Markdown check passed on commit.
- In short: each Mac's Rig host thread keeps a no-model shell loop running every 15 minutes (sol at :00, :15, :30 and :45, terra seven minutes later). Each pass fetches everything, stops if nothing changed, and otherwise fast-forwards clean checkouts and pushes this Mac's own commits, fast-forward only and never forced. It wakes the thread only for a divergence, a dirty checkout in the way of a pull, or a failure. The same loop watches the thread's `messages.md`.
- Primary and secondary, read from the seats: sol leads Knowledge Islands, Personal, Legal, Valle Armonia, Sacred Inquiry, TechMedix and Equal Remedy; terra leads Humans Not Robots. The primary tells Kris when something stays stuck. Neither Mac can overwrite the other. The seven-minute offset means each Mac's next pass is the other's pull-back, at most eight minutes later. Rig drafts the map and Kris approves it.
- The plan records that the Observatory only watches, lists the three things needed first (the `mgit` push guard, one supervised run per Mac, keeping each Mac awake), and keeps vega out.
- Drafted three rollout lines inside the plan, not sent: one each for `personal.reg.rig-sol` and `personal.reg.rig-terra`, asking for a plan rather than an install, and one for `ki.prj.tools-burndown` marking MGIT-PUSH-GUARD as a blocking prerequisite.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The three rollout lines are waiting for the coordinator to send them once Kris is happy with the plan.
- Observatory's open SYNC-DIRECTION query, in [its queries](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.observatory/queries.md), asks how the pass should run, and Kris's mechanism answer (a loop inside the host thread) covers it. That query belongs to Observatory, so this run did not touch it.
- This plan answers Kris's HOST-RECONCILE points. The four older HOST-* queries in [queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/queries.md) can now be closed, and that is the coordinator's job.
- The plan reads the pull-back as each Mac's next offset pass and adds no separate step. If Kris wants something quicker than eight minutes, the offsets can be tuned.

## Queries

### VEGA-SYNC - Leave vega out of host reconcile

**Context:** Kris asked for reconciliation "on each of the machines". Vega is the third machine: the cloud agent host in the Techne account. It has no Rig thread, no seat and no place in the primary and secondary map. Under the [Techne Programme Focus](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Policies/Techne%20Programme%20Focus.md), its agents run only in sessions Kris opens, with no scheduled agents, and push only when Kris asks.

**Query:** Should vega stay out of host reconcile for now?

**Options:**

a) (recommended, confidence high - the policy and the missing seat both point this way, and nothing is lost) Leave vega out for now. Its sessions push their own work when Kris asks, as they do today. Revisit if vega ever holds long-lived checkouts of its own.

b) Add vega as a third host with its own Rig thread and time slot. That needs a change to the Techne Programme Focus first.
