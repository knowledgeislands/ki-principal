# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-workers-record

**🤖 → 👤 Handoff to supervisor · Run report at 23:20 BST · last mark 23:20 BST**

---

## Done

- New triage record [KI-OBSERVA-VIS-045 Workers instrument](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-045-workers-instrument.md) carries the Workers phase's whole scope, acceptance and considerations across from KI-OBSERVA-VIS-031. KI-OBSERVA-APP-044's decision and Kris's approval are named as prerequisites in its Discussion, with `blocked_by` left empty. It stays separate from KI-OBSERVA-VIS-044 and points to it.
- In [KI-OBSERVA-VIS-031](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-VIS-031-who-is-working.md), still done, each Workers phase description (Goal, Context, Boundary, Shaping, Current state, Dependencies and its Discussion section) is replaced by a link to KI-OBSERVA-VIS-045. The Done and Answers history is left as it was.
- Commits on `main`, not pushed: `e6699f7` reserves the number in the ledger; `24c4bd8` adds the record and the VIS-031 links.
- `ki repo audit`: no failures. Its 24 warnings were there before this change, and none of them names either record.
- Step 3:
  - KI-OBSERVA-VIS-023, KI-OBSERVA-VIS-024 and KI-OBSERVA-BRG-002 no longer exist. Commit `fa16595` removed them.
  - That commit removed these six records: KI-OBSERVA-APP-042, KI-OBSERVA-BCN-008, KI-OBSERVA-BRG-002, KI-OBSERVA-INT-004, KI-OBSERVA-VIS-023 and KI-OBSERVA-VIS-024.
  - Open records with relative links to removed records, which are now broken: KI-OBSERVA-BRG-004 (to BRG-002), KI-OBSERVA-VIS-029 (to VIS-023), KI-OBSERVA-VIS-033 (to VIS-024 and BRG-002) and KI-OBSERVA-VIS-041 (to INT-004).
  - The done KI-OBSERVA-VIS-031 also links to VIS-023 twice without a pin. Every link to APP-042 is already pinned. Nothing links to BCN-008.

## In Progress

Nothing.

## Queries

**Context:** Five links in open records, and two in KI-OBSERVA-VIS-031, still point to records that `fa16595` pruned, so they no longer resolve. This run was told only to report them.
**Query:** Should a follow-up pin them to `22ea8dc`, the last commit where those records still existed, the same way the KI-OBSERVA-APP-042 links are pinned?
**Options:** a) (recommended, confidence high - these are link-only fixes that follow the pinning already used for APP-042) pin all seven in one commit; b) pin only the five links in open records; c) leave them.

**Context:** In [KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md), line 36 still says Workers is a later phase in KI-OBSERVA-VIS-031. This run was not authorised to edit that record.
**Query:** Should that line now point to KI-OBSERVA-VIS-045?
**Options:** a) (recommended, confidence high - the mapping would otherwise send readers to a closed record) repoint it in the same commit as the link pins; b) leave it until KI-OBSERVA-APP-044 is next shaped.
