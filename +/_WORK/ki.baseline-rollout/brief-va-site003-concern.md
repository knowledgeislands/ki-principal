# Brief - va-site003-concern

Capture one record for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), from run `va-plan`'s query, which Kris's standing answer covers (2026-10-19 23:59 BST: "Anything high confidence can be done.").

## The query as raised

### SITE003-CONCERN - Give the Sanctuary style gap its own record

**Context:** Under Outstanding concerns, [VA-WEBSITE-SITE-003](/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com/docs/roadmap/VA-WEBSITE-SITE-003-consolidate-the-design-system.md) notes that the Sanctuary's `.webc` styles are outside the SITE-RT-033 token guard. The roadmap standard says such a concern needs its own identifier before acceptance, because the concern disappears when the record is pruned. No record carries it today.

**Query:** Should a triage record be captured in apps-vallearmonia.com to extend the token guard to Sanctuary `.webc` styles before VA-WEBSITE-SITE-003 is accepted?

**Options:** a) (recommended, confidence high - capture is unadopted and reversible, and the standard requires an identifier before acceptance) Capture one triage record through `ki-next` and cite it in VA-WEBSITE-SITE-003's Outstanding concerns. b) Accept VA-WEBSITE-SITE-003 with the gap recorded as an accepted risk and no follow-on record.

## Task

In `/Users/krisbrown/workspaces/valle-armonia/apps-vallearmonia.com`, take option a): capture one unadopted triage record through `ki-next` for the Sanctuary style gap, reserving its number in the ledger as the roadmap standard requires, and cite it in VA-WEBSITE-SITE-003 without changing SITE-003's awaiting-review state. Follow the repository's AGENTS.md.

## Authority

Commit by explicit path under `ki-git`, Conventional Commits ending `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; never push. Never touch `package.json`, `bun.lock`, `.husky/` or `.githooks/`; never run `ki repo conform` without `--dry-run`; wait and retry on a Git lock; name other sessions' uncommitted files without touching them.

## Report

Return a run report in the `ki-coordination` run-report form: under Done the record captured and SITE-003's citation, linked by absolute path, with commits; any decision for Kris as a query with a recommended option and confidence.
