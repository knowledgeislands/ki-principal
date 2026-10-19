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

### KNIP-HUSKY - Let Knip read the committed hooks directly

since 2026-10-19 · from wave1.report.md in the run state folder · reviewed by qreview5 (Codex, high), amended

**Context:** Once Husky goes, Knip stops seeing Commitlint, lint-staged and syncpack and fails them as unused. The pilot and tonight's estate runs add ignores by hand. The review proved locally that Knip's Husky plugin can be pointed at `.githooks` directly, which passes without any ignores and keeps the detection honest.

**Query:** Should conform and new-repository scaffolding configure Knip to read `.githooks` directly, replacing the hand-added ignores?

**Options:**

a) (recommended, confidence high - reviewed: direct discovery passed locally without the three ignores) A tools-ki follow-up configures Knip's Husky plugin for the committed hooks in conversion and scaffolding, cleans up already-converted repositories, and the harness Knip guidance names it.

b) Have conform add the dependency ignores automatically, as a documented exception.

c) Leave the hand fixes; later audits catch the gap.

## Parked

### ASK-B - Coarse acquisition kind in the public export

since 2026-10-19 · from rigsite-config.report.md in the run state folder · parked: ASK-B a), under HIGH-CONFIDENCE on 19 October; release: the rig.midnight.ninja side asks

**Context:** Ask B has no go-ahead. If it goes ahead, a `kind` or `form` field derived as application or command-line would get past the site's forbidden-field check. Platform variants complicate it, because one tool can install differently on macOS and Linux. It would widen the public export (RIG-PUB-002).

**Query:** Keep Ask B parked?

**Options:**

a) (recommended, confidence high - there is no go-ahead, and it widens the public boundary) Keep it parked and raise it only when Kit asks.

b) Capture it at triage now, marked as waiting for Kit's go-ahead.
