---
id: ki.prj.ways-of-working
state: on-hold
since: 2026-10-29T22:41:26Z
received: 2026-10-29T15:38:09Z
beat: null
mark: 2026-10-29T22:41:26Z
method_read: 07b9333a
hold:
  reason: moving to sol
  release: resume on sol
---

# ki.prj.ways-of-working state

## Now

- At rest for the move to sol under [STOP-FOR-MOVE-WOW](decisions.md#stop-for-move-wow---2026-10-29), encoded as on-hold until the state-machine rollout. Nothing of this work is running, queued for execution or scheduled; no wakes are held.
- The work state machine and its open choices remain in [work-state-machine.md](design/work-state-machine.md); all open queries are parked in [queries.md](queries.md).
- Reports are preserved in reports/; spent briefs are removed. The two retained briefs await relaunch after resume.
- PR inventory supplied by the orchestrator: knowledgeislands/ki-principal had no open PRs at 2026-10-29T22:33Z. No provider call made here.

## Next steps

1. On sol, fetch origin and check main is level with origin/main; pull fast-forward only if behind, and stop on divergence.
2. Re-bootstrap as ki.prj.ways-of-working under ki-coordination.
3. Restore parked queries to Open as appropriate; relaunch [wow-host-sync-design](briefs/wow-host-sync-design.md) and [wow-finish-line](briefs/wow-finish-line.md).
4. Settle the state-machine choices with the rollout, then route the state machine to ki-work-package, ki-coordination, the Work Process note and tools-ki. Continue FOLDER-MIGRATE per package; this package is already tidied and moved.
5. Continue HOST-SYNC rollout through the Rig queues, MOD-011 reconciliation from published sources and the private PUBLIC-REPORT-AUDIENCE review within their existing authority.

## Held

- Preserve original model candidates, Tools retained refs and publication recovery evidence; reconcile published sources without overwriting unresolved overlaps or replaying stale trees. The named wow-publication recovery ref is absent from this checkout.
- Host-sync and other unchosen designs retain their decision stages; no executor, schedule or automatic takeover is selected.
- HNR remains excluded; Observatory appearance belongs to its own work. No release, deployment, installation, credential/provider operation, confidential publication, force/reset/stash or hook bypass is authorised here.
