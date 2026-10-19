# ki.tools-burndown queries

## Open

### ESTATE-PUSH - Push the converted repositories

since 2026-10-19 23:25 BST · from the coordinator · blind review qreview4 pending (raised to Kris before review)

**Context:** The migration commits locally in each repository. The rule so far is that runs commit and Kris pushes; local-only leaves other machines on Husky until pushed. The release run already pushes tools-ki.

**Query:** Should the migration runs push each repository after its conversion is verified?

**Options:**

a) (recommended, confidence medium - "make it happen" points to landing it, but pushing about 50 repositories is outward-facing and "push" was not said) Each run pushes fast-forward only after the verified commit, and never pushes a repository carrying another session's unpushed commits, listing those instead.

b) Commits stay local and Kris pushes with `mgit` when ready.

### MGIT-030-NEXT - Promote the mgit sync summary record

since 2026-10-19 · from trimga.report.md in the run state folder · blind review qreview4 pending

**Context:** KI-TOOL-MGIT-CLI-030 is now high priority at Soon, with nine open output-design choices, so its Next plan sections cannot honestly be written yet.

**Query:** Should it move to Next now, settling its design choices at planning?

**Options:**

a) (recommended, confidence medium - stranded unpushed commits are a real cost, and planning is where the output contract belongs) Settle the choices with Kris at planning under `ki-plan`, then promote it to Next.

b) Leave it at Soon until the burndown reaches it.

### MGIT-026-SIZE - Size the older mgit record

since 2026-10-19 · from trimga.report.md in the run state folder

**Context:** KI-TOOL-MGIT-CLI-026 was adopted earlier with no `size`, so the roadmap audit warns.

**Query:** Should it get `size: m`?

**Options:**

a) (recommended, confidence high - it spans several commits and a planned step list) Set `size: m` at its planning.

b) Leave it until it becomes Ready.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
