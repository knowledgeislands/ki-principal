# ki.tools-burndown queries

## Open

### SCR5-CONFORM - Keep the safer install-script repair

since 2026-10-19 · from hookstd.report.md in the run state folder

**Context:** The hooks design said the SCR-5 conform step should rewrite Husky's `prepare` install script to point Git at `.githooks` in every repository. In a repository that doesn't yet have committed `.githooks/pre-commit` and `commit-msg`, that would silently switch the commit gate off. hookstd made conform keep the Husky form until the committed hooks exist. The audit warns on SCR-5 the whole time, so the gap stays visible.

**Query:** Should SCR-5 conform keep the Husky install script until the committed hooks exist?

**Options:**

a) (recommended, confidence high - it only defers a change the audit already reports, and never unbinds the gate) Keep the behaviour as committed, and note the refinement in the hooks design.

b) Rewrite unconditionally, as the design states, and rely on the waves converting the hooks before conform runs.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
