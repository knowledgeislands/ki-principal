# ki.tools-burndown queries

## Open

### CAPTURE-FOLLOWUPS

since 2026-10-20 01:58 · acceptki2 · with Kris **Context:** acceptki2 returned KI-TOOL-KI-CLI-152 and KI-TOOL-KI-CLI-167 to In progress: both pass their gates, but the acceptance rule needs an identifier for the work still owed (`ki work message`, `ki work prune`, Knip scaffolding), and CAPTURE-GATE bars runs from creating records. **Query:** May a run capture those three follow-up records in tools-ki and resubmit 152 and 167? **Options:** a) (recommended, confidence high - the only route to Done; the reviewer independently found the two housekeeping captures warranted) capture three linked records and resubmit both for acceptance; b) keep CAPTURE-GATE; both stay In progress.

### SRC-PLACEMENT

since 2026-10-20 · parked for Kris's return, medium after review **Context:** KI-TOOL-KI-CLI-139 mirrors EBU SharePoint documents into a store copy; ADR-KI-TOOL-KI-004 keeps acquisition inside `ki`. Run view (low): a new `ki acquire` adapter with a Harness skill. Reviewer view (medium): a separately specified source-maintenance command group in `ki`, because mirror refresh has different lifecycle and replacement semantics; share the SharePoint code beneath both. **Query:** Where should the SharePoint mirror command sit? **Options:** a) (recommended, confidence medium - reviewer view, which outranks the run's low) a source-maintenance command group with its own specification; b) a `ki acquire` adapter after broadening the acquisition contract.

### WORKTREE-GATE

since 2026-10-20 · parked for Kris's return, medium after review **Context:** `ki repo audit` blocks commits from linked worktrees because registration compares exact checkout paths, and a contract test keeps that rule. The reviewer proposed an option the run missed. **Query:** How should linked worktrees commit without weakening the gate? **Options:** a) (recommended, confidence medium - reviewer's missed option; fixes the failure and keeps evidence that checks ran) a linked worktree inherits its verified common repository's registration, with contract tests; b) narrow the registration diagnostic only; c) commit only from primary checkouts.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
