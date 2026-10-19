# ki.tools-burndown queries

## Open

### SYNC-CATEGORIES - Outcome categories

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today sync prints one line for each checkout that changed or has a problem, but it adds none of them up. The record needs a fixed set of outcomes that every repository falls into. Reviewer adds: specify precedence for dirty checkouts whose fetch also failed, retaining both reasons.

**Query:** Which outcomes should the tally count, and where does each kind of skip fall?

**Options:**

a) (recommended, confidence medium - every checkout gets exactly one outcome, and "failed" means Git itself went wrong) Use five outcomes: in sync, pulled, pushed, skipped and failed. Skipped covers local changes, detached HEAD, no upstream, diverged, failed fetch, bare repositories and your own `-i` refusals. Failed covers only `status failed`, `cannot compare`, `pull failed` and `push failed`.

b) Add a sixth outcome, "need attention", as `overview` has. It would take diverged, dirty, detached and no-upstream checkouts, and leave skipped for bare repositories and your refusals.

c) (reviewer's view, confidence high - A fetch error belongs with operational failures within five exclusive outcomes) Count a failed fetch as failed, not skipped.

### SYNC-STREAMS - Standard streams

since 2026-10-19 · from mgitplan.report.md in the run state folder · reviewed by qreview6 (Codex, high)

**Context:** Today every sync line goes to standard output. The `ki-repo-tools` command-line conventions put warnings and progress on standard error. [KI-TOOL-MGIT-CLI-029](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-029-cli-convention-departures.md) owns departures from those conventions across the commands. Reviewer adds: include prompts and diagnostic detail on standard error; the proposed deferral record currently excludes new departures.

**Query:** Should this record move sync's warning lines to standard error?

**Options:**

a) (recommended, confidence medium - this keeps the record bounded, and lets one record settle streams for every command) Leave the streams as they are, and record the departure on KI-TOOL-MGIT-CLI-029.

b) (reviewer's view, confidence medium - Apply the existing stream convention while changing this output contract) Do it here: move the skip, warning and progress lines to standard error, and keep the tally and the per-repository result lines on standard output.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
