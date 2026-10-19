# ki.knowledge-acquisition queries

## Open

### STATE-PLACEMENT - What technical acquisition state must survive, and where

since 2026-10-18 · from [intake-and-clearance](design/intake-and-clearance.md#the-acquire-state-directory) and [acquire-capability-review](design/acquire-capability-review.md#remove-acquire-through-the-existing-state-work)

**Context:** Acquire's `.acquire/` directory holds 26 retained files: the Granola ledger (source and account identity, versions, capture locators, handled-source suppression), the ChatGPT conversion checkpoint and converter (retained batch and provenance proof) and migration manifests. The hidden directory is an implementation choice; its retained state and proof are necessary. KB-ACQUIRE-002 already selects `+/_ACQUIRE/{granola,chatgpt,migration}/`, but tools-ki still selects `.acquire/granola/` whenever `capture_root` is set and the Granola skill admits no independent state root, so moving the directory alone would break discovery of retained state. All current `.acquire/` bytes are unchanged; no move or reset has been performed.

**Query:** What is the minimal surviving-proof model for technical acquisition state, and where does it live, before any tooling or state relocation?

**Options:**

a) (recommended; the only option recorded) Preserve current state until importer/configuration support and a verified relocation plan exist.

### RECEIPT-RETENTION - How intake requests are tied up and their receipts retained

since 2026-10-18 · from [intake-and-clearance](design/intake-and-clearance.md#intake-retention-and-pruning)

**Context:** The current contract retains closed receipts: closing a request removes it from pending discovery but does not delete its receipt. There is no implemented or agreed receipt-pruning operation, and a work-folder tidy does not apply to the separate intake receipt store. The proposed tie-up rule closes a request only after its bounded scope has verified capture outputs or an explicit zero-output disposition, retaining one compact request-to-capture/handling link and any sole supplied bytes. Any later deletion of a whole receipt needs an explicit surviving-proof contract first; a receipt's age alone supplies no deletion authority.

**Query:** What intake tie-up and receipt-retention rule does Kris agree?

**Options:**

a) (recommended; the only option recorded) Retain compact identity and handling proof; prune redundant commentary only under an agreed preservation boundary.

### PROTOTYPE-DISPOSITION - What happens to the offline binary-bridge prototype

since 2026-10-19 · from [acquire-capability-review](design/acquire-capability-review.md#scripts)

**Context:** The five `scripts/binary-probe/` files in Acquire are an offline MCP/attachment engineering prototype and its tests. They are not used by routine capture, their real transport and identity binding is unimplemented, and they stay attached to the binary-bridge review (KB-ACQUIRE-003) until their engineering home or disposition is decided. No prototype files were changed in the approved consolidation.

**Query:** Should the prototype leave Acquire's live tree, and on what terms?

**Options:**

a) (recommended; the only option recorded) Remove it from the live tree with Git/review recovery after explicit owner disposition.

## Parked

- PUBLISH-STACK - This session has not pushed. Acquire and Harness changes are local on `main`; Principal also holds peer commits: `0c67f927` ki.ways-of-working next steps, work package delivery; `51d681ca` ki.ways-of-working owner answers, work package and queue priority; `3d12ecc5` ki.ways-of-working work-package note, state file restored; `82db4e67` reconcile completed coverage and remaining handoffs; `e10889b0` ki.ways-of-working receive, state file restored; `3fd3e041` ki.ways-of-working owner answer, state file; `1fc93b73` ki.ways-of-working send to owner, revised work package queries; `db12ad33` ki.ways-of-working work-package note, owner answers revised; `a9b75552` ki.ways-of-working mark, work package answers. Kris decides publication; do not push peer work.

### OBSERVATORY-FIRST - Whether acquisition work waits on the Observatory

since 2026-10-17 · from the decisions log, 22:35 BST on 17 October · parked: a carried-forward dependency; release: its current owner checked · (looks resolved; the worker judges)

**Context:** Kris raised OBSERVATORY-FIRST because knowledge acquisition should be managed through the Observatory, and answered it at 22:40 BST on 17 October: message state-of-play to prioritise getting the Observatory running and pass on the stock-take's overview as the acquisition requirements. [The design note](design/intake-and-clearance.md#next-bounded-decisions) carries it forward for reconciliation with its current owner before any pilot resumes.

**Query:** Does acquisition work still wait on the Observatory's first step?

**Options:**

a) (recommended; the only option recorded) Check its current owner before scheduling acquisition work around it.

### PILOT-SEED - The seed material the dispatch pilot waits on

since 2026-10-17 · from the work file's Parked section (PILOT-SEED / PILOT-GO) · parked: a carried-forward dispatch-pilot dependency; release: reconciled with its current owner before any pilot resumes

**Context:** PILOT-SEED was the request to state-of-play, sent through its inbox at 21:35 UTC on 17 October, to copy section 4 of the foundations-coherence report into its thread folder; PILOT-GO launches once that copy exists. [The design note](design/intake-and-clearance.md#next-bounded-decisions) carries it forward for reconciliation with its current owner; MS3 work was dropped and is not resumed.

**Query:** Does the seed and pilot direction still stand before a trial?

**Options:**

a) (recommended; the only option recorded) Reconcile the existing seed and pilot direction before a trial.

### PILOT-GO - Building the Known World seed pack

since 2026-10-17 · from the decisions log, 22:30 BST on 17 October · parked: a carried-forward dispatch-pilot dependency; release: PILOT-SEED reconciled · (looks resolved; the worker judges)

**Context:** Kris answered PILOT-GO at 22:30 BST on 17 October: build and stage the Known World seed pack on Sonnet, publishing nothing yet, once state-of-play has copied section 4 of the foundations-coherence report into its thread folder (PILOT-SEED). Known World is the inception loop's first pilot. [The design note](design/intake-and-clearance.md#next-bounded-decisions) carries it forward with PILOT-SEED.

**Query:** Does the answered pilot direction still stand before a trial?

**Options:**

a) (recommended; the only option recorded) Reconcile the existing seed and pilot direction before a trial.

### EXISTING-DEPENDENCIES - The chezmoi/trades review and the territory-key question

since 2026-10-18 · from [intake-and-clearance](design/intake-and-clearance.md#next-bounded-decisions) · parked: release: their existing owners' reviews

**Context:** The separate chezmoi/trades review on 21 October remains with its existing owner, and the earlier dispatch-envelope question stays there. The historical ChatGPT territory-key naming question must be compared with current kebab-case configuration and the routing-card work (KB-ACQUIRE-008) before any rename.

**Query:** Do these dependencies stay with their existing owners?

**Options:**

a) (recommended; the only option recorded) Keep their existing owners; do not infer a rename or restart.

### STOCK-TAKE-HOME - Homing the retained stocktake before it is pruned

since 2026-10-18 · from [intake-and-clearance](design/intake-and-clearance.md#retained-stocktake) · parked: release: its provider overview and holding analysis homed

**Context:** The native audit lists [the retained stocktake](stock-take.report.md) as a tidy candidate because its owner questions are answered, but the work-folder contract requires its outcome to have a durable home before deletion. Its provider overview and holding analysis have not yet been reconciled into their durable owners. Its historical counts, holding suggestions and outstanding queries are not current operating instructions.

**Query:** Is the stocktake kept until its provider overview and holding analysis are homed?

**Options:**

a) (recommended; the only option recorded) Retain it through that check rather than delete on the audit listing alone.
