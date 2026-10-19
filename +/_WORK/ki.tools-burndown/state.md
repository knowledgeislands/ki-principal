---
id: ki.tools-burndown
state: with-worker
since: 2026-10-19T18:00:08Z
received: 2026-10-19T18:00:08Z
beat: null
method_read: 9c17df3c
---

# ki.tools-burndown state

## Now

- kirel finished 21:47 BST: full gate green at `395060ae` with loopback allowed (qreview3's timeouts were environmental); `ki` v0.11.5 tagged, release workflow succeeded and published; ki.ways-of-working told in `fe2dda30`.
- githooks and ghreview finished: GIT-HOOKS reviewed, high, drop Husky for committed `.githooks`; in `queries.md`.
- 21:34 BST answers taken (decisions.md): launching kirel (ki v0.11.5), mgitgo (accept -028/-023, mgit v0.18.0), rigcap after mgitgo (tools-rig and chezmoi records), githooks then ghreview (GIT-HOOKS). Next tools-ki run after kirel: note BIOME-CI-STANDARD a) on KI-TOOL-KI-CLI-156.
- Received from Kris at 18:58 BST on 19 October and marked; `ki-work-package` re-read and the description, Goals and Scope confirmed, Scope now carrying HOOKS-STANDARD.
- qreview3 finished 21:32 BST: KI-RELEASE-GO review disagrees (gate not confirmed green, loopback denied in its sandbox), ROUTING-VIEW review prefers capture now; both in `queries.md`.
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
