# Acquire capability assessment

**In progress; marked at 2026-10-18T17:59:40Z.** The owner asked for an assessment of the whole Acquire capability and outstanding items, aiming for a much cleaner structure. This note preserves the first inventory and questions before a pause; it is not the completed assessment or an approved cleanup plan.

## Scope and evidence baseline

Acquire baseline: `cedee9445bf0421caae0b8f954c50deab7f4f674`. The existing [intake/clearance synthesis](intake-and-clearance.md) carries the completed trial and preservation boundaries. This review covers the capability, outstanding work, its retained technical state and receipt contracts, both legacy working areas, and the routing/context and Git/OneDrive split.

Observed file inventory:

- `captures/`: 3273 files, 396,136,674 bytes.
- `intake/`: 16 files, 81,457 bytes.
- `.acquire/`: 26 files, 2,416,992 bytes.
- `+/_CHECKPOINTS/`: 2 files, 4,790 bytes.
- `+/_THREADS/`: 39 files, 514,036 bytes.
- `context/`: 9 files, 10,667 bytes.

At the mark there are fifteen canonical intake receipts: thirteen closed, one blocked and one received/routing-pending. The README is additional. No receipt, capture, provider state, original attachment or historical proof has been deleted or relocated in this assessment.

## Initial findings to investigate

- The structural clutter is real. Acquire still carries an old conversational checkpoint and a large thread-report tree while this work is now tracked in the existing KI work folder. The old tree also contains prototype scripts and tests: copying it wholesale into `+/_WORK/` would violate that folder's closed list. Classify useful doctrine, live obligations, retained proof and obsolete run material before removing the old paths.
- `.acquire/` and `intake/` overlap in identifiers, hashes and processing outcomes, but their current responsibilities differ. Provider checkpoints and ledgers govern incremental acquisition, source versions and handled-source suppression; request receipts govern what the owner submitted and whether that bounded request was preserved. Some proof is repeated in receipts, capture READMEs and manifests. The assessment should choose the authoritative home of each fact, not merely merge two directories with different readers.
- The current Granola importer still selects `.acquire/granola/` when `capture_root` is set. Safe reset-retention support has landed, but independent state placement has not. Separate evidence retirement from physical state relocation; a cosmetic move cannot be the first cleanup step.
- `intake/` retains closed receipts under the current contract. Decide the minimum surviving proof and whether redundant progress prose can be compacted. Where a receipt holds the only supplied text, that source evidence must survive. Closing a request does not authorise deleting the receipt or its capture.
- The shared context remains ChatGPT-shaped despite the agreed provider-independent direction. Its migration must preserve bootstrap consumers while keeping territory Capitals authoritative.
- Holding, routing, dispatch, seed/return and capture-mark work are at different delivery stages. Some operating paths are already working in manual trials, while forward records still describe unimplemented broader capability. Distinguish verified behaviour, awaiting-review delivery and prospective work; avoid carrying all of them as one undifferentiated backlog.

## Outstanding records to reconcile

- [KB-ACQUIRE-002: Migrate Granola state](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-002-migrate-granola-state.md) - `draft`; substantive review pending.
- [KB-ACQUIRE-003: Investigate binary bridge](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-003-investigate-binary-bridge.md) - `awaiting-review`; substantive review pending.
- [KB-ACQUIRE-004: Granola screenshots and markers](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-004-granola-acquired-workflow.md) - `awaiting-review`; substantive review pending.
- [KB-ACQUIRE-005: Seed-and-return loop](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-005-seed-and-return-loop.md) - `triage`; substantive review pending.
- [KB-ACQUIRE-006: Image and video holding](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-006-image-video-holding-area.md) - `triage`; substantive review pending.
- [KB-ACQUIRE-007: Dispatch push and return](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-007-dispatch-packet-push-and-return.md) - `triage`; substantive review pending.
- [KB-ACQUIRE-008: Routing knowledge cards](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-008-routing-knowledge-cards.md) - `triage`; substantive review pending.
- [KB-ACQUIRE-009: Chat capture marks](https://github.com/krisb/acquire/blob/main/docs/roadmap/KB-ACQUIRE-009-chat-capture-marks.md) - `awaiting-review`; substantive review pending.

These are observed record states, not acceptance or cancellation recommendations. The assessment still needs the full bounded contents, dependency owners and current implementation evidence before making those recommendations. Keep the existing allocation ledger and do not create duplicate cleanup records during assessment.

## Cleanup decision to prepare

Produce one minimal target structure and a per-area action list: keep, compact, move, retire to Git history, or change tooling first. Name the authoritative item identity, receipt/handling proof, technical checkpoint, active work record and external-asset locator. Show which legacy files have a durable home, which obligations remain open, the exact migration/rollback and byte-preservation checks, and the smallest staged execution plan for owner agreement.

The owner requested a mark before that assessment was complete. Resume by reconciling fresh Git and receipt state, then finish the evidence pass and bring back the assessment. Customs, clearance area, `items/`, a new receipt layout and state-root changes remain design questions; no rename or automatic pruning policy is enacted here.
