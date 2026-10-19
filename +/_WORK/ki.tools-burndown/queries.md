# ki.tools-burndown queries

## Open

### MGIT-026-SIZE - Size the older mgit record

since 2026-10-19 · from trimga.report.md in the run state folder

**Context:** KI-TOOL-MGIT-CLI-026 was adopted earlier with no `size`, so the roadmap audit warns.

**Query:** Should it get `size: m`?

**Options:**

a) (recommended, confidence high - it spans several commits and a planned step list) Set `size: m` at its planning.

b) Leave it until it becomes Ready.

### MGIT-030-NEXT - Promote the mgit sync summary record

since 2026-10-19 · from trimga.report.md in the run state folder · reviewed by qreview4 (Codex, high): disagreement

**Context:** KI-TOOL-MGIT-CLI-030 is high priority at Soon with nine open output-design choices; its record says four must be settled before promotion. Next allows a draft whose plan is still forming, and `ki-plan` takes only Now or Next drafts.

**Query:** Should it be selected for planning now?

**Options:**

a) (recommended, confidence medium - reviewer's view, with which the coordinator now agrees: `ki-plan` cannot run on a Soon record) Promote it to Next as a draft through `ki-next` now, replacing its promotion condition, then settle the nine choices with Kris through `ki-plan`.

b) Settle the four promotion choices with Kris as Soon shaping first, then promote and plan.

c) Leave it at Soon until the burndown reaches it.

### KNIP-HUSKY - Teach conform the Knip side of the conversion

since 2026-10-19 · from wave1.report.md in the run state folder · blind review qreview5 running

**Context:** Knip saw Commitlint and lint-staged through its Husky plugin; once Husky goes it reports them unused, failing Knip. wave1 added them to `ignoreDependencies` by hand, and the estate runs were told at 23:32 BST to do the same so the migration is not held up.

**Query:** Should `ki repo conform`'s conversion add those Knip ignores itself, for repositories converted later and for new ones?

**Options:**

a) (recommended, confidence medium - it keeps future conversions mechanical, at the cost of one more tools-ki change) Extend the KI-TOOL-KI-CLI-163 conversion in a follow-up release, and have the harness's Knip guidance name it.

b) Leave conform as it is; the estate runs fix it by hand tonight and later conversions rely on the audit.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
