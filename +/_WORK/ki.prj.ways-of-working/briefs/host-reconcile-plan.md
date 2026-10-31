# Brief: host-reconcile-plan

Work: ki.prj.ways-of-working. Authority: HOST-RECONCILE answers, Kris, 31 October 2026, at the end of `decisions.md`. Read them, `design/host-reconcile/findings.md`, `design/host-sync/report.md` and `design/inbox-wake/design.md`.

Write `design/host-reconcile/plan.md`: one page, plain English, for Kris. Cover:

1. **What runs, where.** Each Mac's Rig host thread is a long-lived chat thread. It keeps a cheap shell loop that does no model work. Every 15 minutes, offset per host (propose starting offsets: sol on :00/:15/:30/:45, terra seven minutes later), it fetches every repository and checks cheaply whether anything changed, locally or on GitHub. If nothing changed, it stops there. Otherwise it fast-forwards clean checkouts and pushes the commits that are local only, for both primary and secondary areas, fast-forward only and never forced. It wakes the thread's model only for something needing judgement: a divergence, a dirty checkout or a failure. The same loop also watches the thread's `messages.md`.
2. **Primary and secondary.** Say what that means in practice: which Mac leads for which territory's repositories, how the two avoid stepping on each other, and the pull-back shortly after the other Mac's pass. Rig drafts the map from the seats, and Kris approves it.
3. **The Observatory:** it watches and reports, and does no syncing.
4. **What must exist first:** the `mgit` push guard (tools-burndown, held), each Mac's first supervised run, and keeping each Mac awake.
5. **Vega:** where it stands.

Then draft, without sending, one rollout line each for `personal.reg.rig-sol` and `personal.reg.rig-terra` (in `/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/`), and one for `ki.prj.tools-burndown` about the push guard. End with at most one decision in the QUERY-TURNS shape, if anything is still open.

Commit the plan alone by explicit path and push fast-forward only. Report in plain English.
