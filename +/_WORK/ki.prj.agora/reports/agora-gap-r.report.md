# KI > Techne > Agora › agora-gap

**🤖 → 👤 Handoff to supervisor · Run report at 03:53 GMT · last mark 00:04 GMT**

---

## New and noteworthy

The central gap is durable shared messaging and roster state behind the MCP. The existing Beacon, Atlas and Lantern do not yet implement that store. The MCP checkout progressed from scaffolding to uncommitted source and a store contract during this run; no committed or tested delivery was observed. The design includes that late evidence.

AGORA-STORE answers the MCP draft's Q1, Q2 and Q10 and supersedes its JSON/month-folder layout, batching and archive-tree model. Filename processing order must be separated from Git change discovery so late offline messages are not skipped.

Atlas still looks up the literal island key `ki-portal`, and the chezmoi source still has an old mgit binding. These need owner-scoped corrections. Model portals, working bundle ids and the generic `[phone]` key need no blanket rename.

The late-pass contract exposes four acceptance gaps: offline acceptance before a successful fetch, missing one-shot send/ack/reply/wait commands for the cloud pilot, caller retry identity, and harvest that can hide an acknowledged but unanswered question. Its whole-store read scope also differs from the earlier draft and needs an explicit trust decision. These are design/integration findings from uncommitted work, not a delivery review or a claim that its checks failed.

## Done

Completed [agora-gap.design.md](<agora-gap.design.md>): the five-part picture and modes, capability gap table, thirteen naming assessments, six phased delivery gates and thirteen proposed decisions.

Read the interrupted run's session-limit log; no earlier design/report artifact or earlier delivery by this run was identified in the local evidence inspected.

Checked local code, specifications, coordinator/doer mailboxes, method guidance, store/MCP work in progress and selected cross-owner references; no repository changes, commits, fetches, remote calls, messages or agent launches made.

Design validation: all five requested sections and thirteen query blocks present; absolute local links resolve; table rows stay within 140 characters; rumdl check passed. Application tests were not run because this was a read-only design task.

## In Progress

Nothing is running in this gap run. The design is ready for supervisor review; implementation and cross-owner adoption have not started under this run.

Outstanding - no action requested now: agora-store owns the separate version 1 delivery. Reconcile its actual STORE.md, tools and test evidence before planning the Beacon binding. GitHub freshness, terra's installed state and cloud wait/wake behaviour were not verified: the brief forbids remote calls. The app checkout was changing under other runs, so evidence is a local source-reading window, not a frozen or installed-build audit.

## Queries

These thirteen proposals include the draft’s still-open Q3–Q9, plus Q11/Q12 and four target/integration choices. Q1, Q2 and Q10 are settled and are not asked again. Recommendations that require independent query review remain unreviewed: this brief forbids agent launches and is a design run. The supervisor should route that review before final presentation to Kris; no review or approval is implied here.

### Q3 - What reading a message records

**Context:** The draft says inbox/wait create read receipts, with a choice about persisting them. The current MCP scaffold instead says reads have no side effects and unread means not yet acknowledged or answered. Durable ack and answer records provide recovery, but they do not prove that someone merely looked at a message.

**Query:** Should version 1 retain only durable acknowledgements and answers, or also record reading separately?

**Options:**

a) (recommended, confidence medium - explicit acknowledgements survive retries and avoid making a viewer's read change workflow state) Keep reads side-effect-free in version 1; persist ack and answer messages, label the queue as unacknowledged/open where appropriate, and reserve read telemetry for a later explicit capability.

b) Record durable read receipts in Git, distinguishing read, acknowledged and answered, and make receipt-writing an explicit documented effect of the relevant tools.

c) Keep read telemetry only in a live queue and label it as unavailable or unknown after restart or across offline rigs.

### Q4 - Message kinds and default reply obligations

**Context:** The six target kinds are brief, question, answer, art, ack and info. The draft makes brief and question need a reply by default. This catches missed questions but can leave a completed brief open unless art delivery or a closing answer is defined carefully.

**Query:** Should both briefs and questions require a reply by default?

**Options:**

a) (recommended, confidence medium - explicit closure makes an unanswered instruction visible while allowing informational exceptions) Keep the six kinds; default brief and question to needs_reply, permit an explicit override, and require a linked closing answer when a deliverable alone does not satisfy the brief.

b) Default only questions to needs_reply, requiring a sender to opt each brief into a reply obligation.

### Q5 - Who may send a brief

**Context:** Addressability is not authority. The current coordination method requires routed work to receive and dispose of a request within its own authority. A transport allow-list could block legitimate cross-package routing, while an unrestricted sender must not acquire execution rights.

**Query:** Should the MCP enforce coordination routes, or leave authority judgement with the recipient?

**Options:**

a) (recommended, confidence high - the existing method already assigns authority judgement to the recipient and a stable sender identity permits audit) Allow an identified package to send a brief to a known recipient; enforce identity and message access, and leave execution authority and disposition to the recipient's rules.

b) Encode allowed coordination routes in the MCP and refuse briefs outside those routes, with a separately owned policy and update process.

### Q6 - Where a mark's Summary appears

**Context:** Today's Summary belongs in the agent's owner-facing conversation. The draft proposes that the mark can receive an answer so Atlas can show a complete picture. A transport acknowledgement must not imply that the Summary was delivered or that its work was accepted.

**Query:** Should a completed mark also receive a store answer?

**Options:**

a) (recommended, confidence medium - the conversation remains the owner's surface while the store can distinguish acknowledgement from completed reporting) Keep the full Summary in its normal conversation and send a linked answer identifying that Summary after it exists; Atlas shows that completion and pointer.

b) Keep the Summary solely in the conversation and store only the mark acknowledgement, leaving Atlas unable to prove reporting completion.

c) Store the full Summary as the mark's answer as well, accepting duplicate retained content and defining which copy governs.

### Q7 - Claude Design's route for the pilot

**Context:** The existing bridge already reaches the local mailbox, but a blocking MCP command has not been measured here. Public remote mounting, authentication support and between-turn waking remain unverified. A cloud server would add a new operational dependency.

**Query:** Which route should the initial Claude Design pilot use?

**Options:**

a) (recommended, confidence medium - it uses the existing route and can be measured without exposing a new endpoint) Verify the one-shot MCP command through the bridge first, with bounded waits below the bridge limit and explicit timeout/cancellation tests.

b) First investigate a directly mounted authenticated remote MCP, and require a separate connection/security design before exposing it.

c) Defer the cloud doer until a cloud-hosted Agora service is designed and operated.

### Q8 - The listening word for MCP wait

**Context:** `agora-call` currently describes a file/terminal notification route. `wait` holds a live turn and does not wake a closed one. Treating them as the same listening mechanism would hide materially different guarantees.

**Query:** Should the worker register name MCP wait separately?

**Options:**

a) (recommended, confidence high - the listener name should distinguish an active tool wait from a between-turn notification) Add `agora-mcp` for a worker actively listening with wait, preserve `agora-call` for the call route, and have the method owner define how both capabilities are represented.

b) Keep `agora-call` as the umbrella value and add a separate field explaining whether the current listener is a file wait, terminal wake or MCP wait.

### Q9 - Join and leave at MCP mounts

**Context:** Version 1 is commissioned with eight tools and does not necessarily implement join/leave. Today's roster is derived from package files; the target roster is durable and package-owned. Automatically treating any mount as listening could leave false live entries after abrupt exit.

**Query:** Should every MCP mount have to join, or should Beacon remain the initial roster publisher?

**Options:**

a) (recommended, confidence medium - it keeps version 1 bounded and avoids two competing writers before the pilot establishes mount lifetimes) Keep explicit join/leave optional initially; Beacon publishes the package declaration, mounts bind a verified identity, and an active wait reports only its observed listening lifetime. Revisit mandatory mount registration after the pilot.

b) Require an idempotent join at mount startup, lease its live status and mark leave on clean shutdown; specify expiry and single-writer reconciliation before delivery.

### Q11 - Checkpoints across durable and live routes

**Context:** A Git commit records discovery/publication, while filenames define processing order. A future live queue can expose an id before its Git commit arrives. A commit reference from unpublished offline history may also cease to be a usable ancestor after reconciliation.

**Query:** Should agents receive one opaque combined checkpoint or manage a checkpoint for each route?

**Options:**

a) (recommended, confidence medium - one gateway can deduplicate routes without exposing their implementation to every agent) Give version 1 a store-scoped Git checkpoint, with explicit pending-publication status; extend it opaquely for live delivery later, retaining stable ids and a defined recovery scan when a reference is unknown.

b) Return separate Git and live checkpoints and require each client to retain both and deduplicate messages.

### Q12 - A package seated on two rigs

**Context:** The old draft's receipt filenames could collide across two seats. The target's immutable ack/answer messages avoid that physical receipt-path collision, but status still needs to say whether one seat or both must respond. The roster now has one path per work id, not one per rig.

**Query:** Should package-level acknowledgement be enough when two rigs have seats for the same work?

**Options:**

a) (recommended, confidence medium - the recipient is a work package and one accountable active owner avoids duplicate obligations during the pilot) Treat receipt and reply obligations as package-level, retaining each event's rig provenance; use one active roster writer per package and require an explicit handoff before another rig writes it.

b) Require per-seat receipts and represent several seats inside the package's roster file, with explicit rules for which seat owns each obligation and for concurrent updates.

### GAP-ORDER - Filename order and important messages

**Context:** AGORA-STORE specifies filename processing order. The coordination standard currently takes important mailbox lines first, then ordinary lines from the top. Late offline publication can also introduce a filename earlier than one already processed. Neither commit order nor a last-filename cursor resolves both issues.

**Query:** Should the store retain strict filename processing order and treat importance as an alert rather than reordering?

**Options:**

a) (recommended, confidence high - this preserves deterministic processing and a change-based scan prevents older offline messages being skipped) Keep filename order for each discovered batch, surface importance as an alert, and require the method owner to state any urgent handling exception explicitly; use stable ids plus change checkpoints for late arrivals.

b) Have the method owner define an explicit priority-order exception and amend the processing contract to describe when priority may override filename order.

### GAP-HARVEST - Keep unanswered obligations active

**Context:** The new in-progress store contract permits harvest when a reply-requesting message is acknowledged or answered. The draft's workflow semantics distinguish receipt from an answer. An acknowledged question could therefore disappear from the active tree while its sender still needs the answer, although history retains it.

**Query:** Must a message requesting an answer remain in the active queue until answered or explicitly closed by its sender?

**Options:**

a) (recommended, confidence high - acknowledgement proves receipt but does not satisfy the outstanding answer obligation) Keep needs_reply obligations active after ack; permit harvest only after an answer or explicit sender closure, with the complete thread and audit provenance preserved.

b) Permit ack-only harvest, but require every inbox/open-obligation query to reconstruct unresolved answer obligations from history so pruning cannot hide them.

### GAP-ACCESS - Who can read messages through a mount

**Context:** The earlier MCP draft limits a mount to its own messages and threads, while the new uncommitted contract explicitly trusts the whole store to one person and permits cross-package inbox and audit reads. The target explicitly makes the roster queryable by anyone; it does not settle message-read scope. A remote cloud mount makes this difference material.

**Query:** Should version 1 retain whole-store reading only within the person's trusted local environment, with broader remote mounts gated on a separate access design?

**Options:**

a) (recommended, confidence medium - this states the actual trust boundary honestly while keeping the pilot usable without a new public service) Permit whole-store reads for explicitly trusted local or existing-bridge mounts, disclose that scope, and require a separate least-privilege design before granting a wider remote/cloud mount access.

b) Require per-work-id message-read filtering before the pilot, retaining universal roster queries and owner-only full audit.

### GAP-PLAN - Approve the next bounded delivery gates

**Context:** MCP/store version 1 is in progress. Beacon integration, a three-party pilot, viewer reads and method-wide mailbox migration are distinct changes with different owners. The design identifies them without opening records or granting implementation authority.

**Query:** After version 1 is received, should the coordinator prepare and bring back the Beacon binding and pilot as the next bounded plan?

**Options:**

a) (recommended, confidence high - these two gates prove durability and real reply handling before requiring other packages to migrate) Agree the phase order, receive version 1, and have the coordinator prepare the Phase 1 and Phase 2 records and owner agreements; later phases remain gated on their tests and method-owner agreement.

b) Hold after receiving version 1 and revise this design before planning Beacon integration or the pilot.

### 🤖 → 👤 Handoff to supervisor · at 03:54 GMT

🤖 0 running · 👤 1 design for review · 13 proposed decisions

- [with you] Gap design and decision proposals · supervisor · since 03:54 GMT

🧵 ki.prj.agora
