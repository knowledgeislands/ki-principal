# ki.tools-burndown queries

## Open

No open queries.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.

- CAPTURE-FOLLOWUPS - KI-TOOL-KI-CLI-152 and 167 pass their gates but need follow-up record identifiers that CAPTURE-GATE bars runs from creating. Recommended a) (high): capture `ki work message`, `ki work prune` and Knip scaffolding records, then resubmit both.
- SRC-PLACEMENT - where KI-TOOL-KI-CLI-139's SharePoint mirror command sits. Recommended a) (medium, reviewer view): a separately specified source-maintenance command group in `ki`.
- WORKTREE-GATE - `ki repo audit` blocks commits from linked worktrees on exact path registration. Recommended a) (medium, reviewer view): a linked worktree inherits its verified common repository's registration, with contract tests.
