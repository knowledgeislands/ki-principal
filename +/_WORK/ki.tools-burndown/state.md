---
id: ki.tools-burndown
state: with-worker
since: 2026-10-19T18:00:08Z
received: 2026-10-19T18:00:08Z
beat: null
method_read: 2026-10-19T18:00:08Z
---

# ki.tools-burndown state

## Now

- Received from Kris at 18:58 BST on 19 October and marked; `ki-work-package` re-read and the description, Goals and Scope confirmed, Scope now carrying HOOKS-STANDARD.
- Running in run `tools-burndown`: link155 finished: reciprocal link in `0720a05`, AUDIT-ITEM-5 cleared; AUDIT-ITEM-158 sent to wpreader's inbox, its own record KI-TOOL-KI-CLI-158 to conform before it finishes, the tag then on the last green commit; qreview2 (blind review of MGIT-GO and KI-RELEASE-GO, lowered to medium because publishing rests on run reports); pin finished: harness `bda6e4a0` pinned in `c55a6c42`, gate green bar AUDIT-ITEM-5; qreview finished: eight agreed and lifted to high, SITE-CONFIG-DATA and ROLLOUT-AUTHORITY disagree, both shown; mgitdep finished: KI-TOOL-MGIT-CLI-029 captured; tag goes on `9a3564d` (MGIT-TAG-TARGET a)); mgitrel finished: KI-TOOL-MGIT-CLI-023 Awaiting review, `v0.18.0` prepared locally as `9a3564d`; cli155 finished: KI-TOOL-KI-CLI-155 Awaiting review, KI-TOOL-KI-CLI-157 (validator parity) at triage, `v0.11.5` prepared locally; wpreader, chained after cli155 in tools-ki (`ki work status` reads both package shapes); burndown finished: KI-TOOL-KI-CLI-146 pruned in tools-ki (31 to 30 records), BURNDOWN-ACCEPT and TRIAGE-PROPOSAL received; PRUNE-FOOTER a) taken as the coordinator's own fix: prune work launches with `--rules prune`. mgitrel, chained after burndown in tools-mgit (KI-TOOL-MGIT-CLI-023 acceptance and the mgit release, built locally). hooksstd finished: [hooks-standard](design/hooks-standard.md), five queries received.
- With Kris: fourteen open queries, reviewed, in `queries.md`, MGIT-GO, KI-RELEASE-GO and the five hooks queries first; the rig.midnight.ninja reply in [rig-site-reply](design/rig-site-reply.md) to pass on.
- Messages taken: FIRST-STEP done; HOOKS-STANDARD to hooksstd; KI-PATCH-RELEASE to cli155 plus KI-RELEASE-GO; FIELDS-FOLLOW-UP and CLI-FIELDS to cli155; WORK-PACKAGE-READER to wpreader; BURNDOWN-PUSH (19:25 BST) to burndown; MGIT-RELEASE (19:42 BST) to mgitrel, chained after burndown, plus MGIT-GO; REFRESH (19:17 BST): QUERY-REVIEW re-read, every open medium-confidence query to the qreview blind run, then a fresh Summary with the reviewed recommendations.

## Next steps

1. Receive each run's report from `~/.local/state/ki/agents/tools-burndown/<name>.report.md`; copy its queries into `queries.md`.
2. On KI-RELEASE-GO a) and a green cli155, cut the `ki` patch with the harness pin at or after harness-link-fix, and send the tag to ki.ways-of-working's `messages.md`.
3. KI-TOOL-MGIT-CLI-028 sits Awaiting review; no `mgit` release without Kris.
4. Not this work's: KI-TOOL-KI-CLI-154; LGL-PRINCIPAL-OPS-018 (legal-principal).

## Held

- RIG-SITE-001-POINTER: drop the bootstrap-guide pointer, until Kris accepts KB-MIDNIGHT-RIG-SITE-001.
- KI-TOOL-KI-CLI-139's "Decision 55" citations, until the decisions move settles (DECISION-55-CITATIONS).
