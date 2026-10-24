# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-app044-fix

**🤖 → 👤 Handoff to supervisor · Run report at 01:17 BST**

---

## Done

[KI-OBSERVA-APP-044](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-044-instrument-restructure-decision.md) corrected against the code in commit `4d967aa` (local, not pushed); status, priority and decisions are unchanged and RESTRUCTURE stays open with Kris.

- Renderer: `renderPage` corrected to `renderShell` in Current state; it was the only wrong name.
- Redirect table: Current state now records that only `renderShell` calls `resolveInstrument`, that the shell reads raw ids including on history navigation, and that the CLI rejects any id resolution changes. A new step and the Files touched entry require explicit adaptation of each consumer: alias canonicalisation in the shell, unknown-id rejection kept in the CLI, and old addresses, filters, report parameters and Beacon destinations verified as each consolidation lands. The Redirect option a) wording now matches.
- Waiting for you: the step, the Discussion section and Order a)'s reason no longer say the rename waits on DESIGN-WORK. They now say the Review queue derives its handoff rows from Work's with-you view and links into Work, so only moving or retiring Work waits on it. Order a)'s recommendation stays, and its reason now reads as a preference.
- Shaping: promotion condition left as it stands.
- Checks: roadmap audit FAIL=0 (WARN=0 on this record, WARN=3 elsewhere in the repository); rumdl clean; the commit hook passed.

## In Progress

Nothing.

## Queries

None.
