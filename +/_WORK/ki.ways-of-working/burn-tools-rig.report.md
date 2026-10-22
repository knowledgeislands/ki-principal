# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › burn-tools-rig

**🤖 → 👤 Handoff to supervisor · Run report at 06:10 BST · last mark 05:20 BST**

---

## Done

- **Waited and pulled.** I waited for apply-sweep to write `DONE` (05:53 BST), then pulled tools-rig fast-forward. The sweep had already accepted and pruned KI-TOOL-RIG-CLI-027, KI-TOOL-RIG-CORE-065 and KI-TOOL-RIG-CORE-066, and cancelled KI-TOOL-RIG-CLI-026, KI-TOOL-RIG-CORE-057 and KI-TOOL-RIG-DIST-011. None of those is touched here.
- **[KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md): draft, Next → draft, Next, planned.** Commit `d92167b`. I grounded it with read-only `defaults read` checks on `sol` and wrote nothing to the machine. On macOS 27, visibility is stored in `NSStatusItem VisibleCC` and order in `NSStatusItem Preferred Position`, both in the user domain, so the record's proposed current-host scope is no longer needed. Login items cannot be read without an Automation-consent prompt, which timed out here. The record now has Current state, Steps, Files touched, Verify, Documentation impact, `size: l`, and three queries that hold it at draft. Gates: the commit hook (Bats 602 of 602, roadmap audit) passed and `git diff --check` is clean. Pushed.
- **[KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md): draft, Next → draft, Next, planned.** Commit `5908727`. I grounded it on the fixed deferral matrix, the missing-manager finding that repeats for every dependent tool, and doctor's manager list, which appears only when the configuration fails to load. The plan has nine steps: an optional `provides` field, manager edges derived from each binding, one finding per missing manager, a doctor managers block (G2), and an opt-in missing-provider check (G4). Five queries hold it at draft. Gates: the commit hook (Bats 602 of 602, roadmap audit) passed and `git diff --check` is clean. Pushed.
- **Push.** I fast-forwarded `run/burn-tools-rig` into local `main`, removed the worktree and branch, and pushed `main` fast-forward. Only tonight's two commits were ahead of origin. tools-rig is level with origin.
- **Follow-up (CAPTURE-GATE).** I added one line, RIG-PRECOMMIT-BATS, to [ki.tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md) in ki-principal `3374348b`. On tools-rig's primary checkout, `ki repo audit` fails SHELL-HOOK because `.githooks/pre-commit` runs the full Bats suite, which takes several minutes on every commit. This failure was there before tonight. **Not pushed:** ki-principal `main` has about ten other sessions' commits stacked ahead of origin, so I stopped pushing that repository.

## In Progress

Nothing is running. The records below were left alone, with the reason for each:

- **[KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md): awaiting review, unchanged.** Both review packets are complete. They are waiting for independent review and acceptance, and for Kris's attended firewall rollout on both Macs.
- **[KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md): draft, Now, unchanged.** Its gate is Kris's attended NordVPN check at `terra`'s console, which writes pf and is connection-critical. Its PLAN068 queries are still open.
- **[KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md): draft, Now, unchanged.** Step 1 is a live handler probe that Kris runs at `sol`'s screen. Only that probe can choose the native setter.
- **[KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md): draft, Soon, unchanged.** It needs promotion first. Its shaping lists open decisions: field names, how a public key is declared, version comparison, archive layout, and which tool verifies Ed25519 without adding a runtime dependency. These belong with the Techne vega work.
- **[KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md): draft, Future, unchanged.** The record itself says it needs re-scoping before it can be acted on.
- **[KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md): triage, unchanged.** The sweep narrowed it today. It is still in triage, which is not adopted, so it cannot be planned.
- **Stale, superseded or duplicate:** none found among the open records.

## Queries

**KI-TOOL-RIG-CORE-053 model and Ready**

**Context:** The menu-bar plan departs from the record's own design in two places, both based on read-only evidence from `sol`. It drops the current-host scope and leaves out login-item checks. The record asked for your check of its units before planning.

**Query:** Should PLAN053-MODEL and PLAN053-LOGIN be taken as recommended and the plan approved to Ready (PLAN053-READY)?

**Options:** a) (recommended, confidence medium - the evidence for both departures is strong, but this is the first observe-only setup resource and you asked to check its model) take PLAN053-MODEL a) and PLAN053-LOGIN a), then approve Ready. b) take the two model answers but keep the record in draft. c) keep the current-host scope and confirm the integer encoding first, which needs each module toggled with you present.

**KI-TOOL-RIG-CORE-067 design answers**

**Context:** The managers plan needs four design answers before Ready. Should derived edges sit beside hand-written ones (PLAN067-EDGES)? Should the missing-provider check apply only once a catalogue uses `provides` (PLAN067-OPTIN)? Should the fixed deferral matrix stay as a fallback (PLAN067-MATRIX)? Should a new ADR-KI-TOOL-RIG-011 be written (PLAN067-ADR)?

**Query:** Should the four answers be taken as the record recommends, and the plan approved to Ready (PLAN067-READY)?

**Options:** a) (recommended, confidence medium - EDGES, OPTIN and ADR are high confidence, but MATRIX is medium because it keeps two routes for a while) take every recommended a) and approve Ready. b) take the answers but keep the record in draft. c) remove the matrix now (PLAN067-MATRIX b)), which requires `provides` before any deferral.

**ki-principal push**

**Context:** My messages line (`3374348b`) is committed locally on ki-principal, behind about ten other sessions' unpushed commits.

**Query:** Who pushes ki-principal?

**Options:** a) (recommended, confidence high - the stacking rule leaves this to the owning coordinator) the ways-of-working coordinator pushes it with its own commits. b) leave it until Kris reviews the stack.
