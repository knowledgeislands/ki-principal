---
id: ki.knowledge-acquisition
state: on-hold
hold:
  reason: more-expected
  release: explicit programme restart within the active Project cap after local trial reconciliation
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-18T17:59:40Z
method_read: null
---

# ki.knowledge-acquisition state

## Now

- On hold, more expected, since 04:30 BST on 18 October; marked at 18:59 BST on 18 October.
- Owner-selected tracking of the acquisition design and practical intake trials continues here; it does not activate a fifth Project above the cap.
- Nothing is running; no historical background run has been restarted.
- Run reports sit in `~/.local/state/ki/agents/knowledge-acquisition/`; any later authorised launch uses this folder, never the retired thread or checkpoint paths.

## Next steps

1. Review the delivered capture consolidation [KB-ACQUIRE-011 (pruned)](https://github.com/krisb/acquire/blob/e370006a8a5f5d79346146998030fb94ad30aa58/docs/roadmap/KB-ACQUIRE-011-consolidate-capture-contracts.md), left Awaiting review, with Kris. Continue the open discussions in `queries.md` without reopening completed source imports.
2. Before changes, read [the working design note](design/intake-and-clearance.md) and [the current canonical intake state](https://github.com/krisb/acquire/blob/main/intake/README.md); two receipt scopes remain pending there. Acquire starts at `CAPTURE.md` and the selected local guide. Keep intake receipts and source capture evidence separate from capability tracking.
3. Use the agreed `captures/<territory>/<source-or-ingress>/` and `context/<territory>/` layout; the local follow-through updates callers and routing wording. Keep mirrored Git/source-store item locators; dispatch, holding and routing-card trials remain their existing work, not a condition for simple capture.
4. Discuss what technical state must survive (STATE-PLACEMENT): Granola import/reconcile/mark reads its handling ledger; the ChatGPT checkpoint/converter and migration files are retained batch/provenance proof; `.acquire/` is not inherently required as a directory. Agree the minimal surviving-proof model and destination before tooling or state relocation.
5. Agree the intake tie-up rule (RECEIPT-RETENTION). No extra queue or receipt deletion is implemented.
6. Recheck the Observatory, dispatch-pilot and chezmoi/trades dependencies before broader work resumes. MS3 remains dropped.

## Held

- The broader acquisition programme beyond bounded intake and local trials: until an explicit programme restart within the active Project cap after local trial reconciliation.
- Relocating `.acquire/` (KB-ACQUIRE-002): until tools-ki supports an independent state root and the surviving-proof model is agreed.
