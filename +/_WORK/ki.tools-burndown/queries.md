# ki.tools-burndown queries

## Open

### HOOK-GUARD - Confine the conversion to the waves until release

since 2026-10-19 · from hcreview.report.md in the run state folder

**Context:** The installed `ki` runs straight from the tools-ki checkout, so the unreleased hooks conversion is already live. Any session that runs `ki repo conform` without `--dry-run` on a KI repository with Husky now converts it - rewriting hooks, `package.json` and `bun.lock`, deleting `.husky/` and changing the binding - outside the waves Kris grants. An IMPORTANT warning went to State of play at 23:20 BST.

**Query:** Should conform convert hooks only when explicitly asked, until the release?

**Options:**

a) (recommended, confidence high - the review verified the exposure directly, and a switch confines conversion to granted waves) A short tools-ki run, after wave1 finishes its tools-ki step, adds an opt-in switch so conform converts hooks only when asked; the waves pass it, and whether the release keeps it is decided at the release.

b) Rely on the State of play warning until the release.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
