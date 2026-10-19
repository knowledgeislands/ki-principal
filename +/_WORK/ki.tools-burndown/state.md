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
- Running in run `tools-burndown`: cli155 (KI-TOOL-KI-CLI-155 with the FIELDS-FOLLOW-UP rules, VALIDATOR-PARITY captured after it, release prepared but not tagged); wpreader, chained after cli155 in tools-ki (`ki work status` reads both package shapes); burndown (BURNDOWN-PUSH: prune done records, acceptance batch, triage cancel-or-merge proposal). hooksstd finished: [hooks-standard](design/hooks-standard.md), five queries received.
- With Kris: eleven open queries in `queries.md`, KI-RELEASE-GO and the five hooks queries first; the rig.midnight.ninja reply in [rig-site-reply](design/rig-site-reply.md) to pass on.
- Messages taken: FIRST-STEP done; HOOKS-STANDARD to hooksstd; KI-PATCH-RELEASE to cli155 plus KI-RELEASE-GO; FIELDS-FOLLOW-UP and CLI-FIELDS to cli155; WORK-PACKAGE-READER to wpreader; BURNDOWN-PUSH (19:25 BST) to burndown.

## Next steps

1. Receive each run's report from `~/.local/state/ki/agents/tools-burndown/<name>.report.md`; copy its queries into `queries.md`.
2. On KI-RELEASE-GO a) and a green cli155, cut the `ki` patch with the harness pin at or after harness-link-fix, and send the tag to ki.ways-of-working's `messages.md`.
3. KI-TOOL-MGIT-CLI-028 sits Awaiting review; no `mgit` release without Kris.
4. Not this work's: KI-TOOL-KI-CLI-154; LGL-PRINCIPAL-OPS-018 (legal-principal).

## Held

- RIG-SITE-001-POINTER: drop the bootstrap-guide pointer, until Kris accepts KB-MIDNIGHT-RIG-SITE-001.
- KI-TOOL-KI-CLI-139's "Decision 55" citations, until the decisions move settles (DECISION-55-CITATIONS).
