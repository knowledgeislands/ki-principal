# ki queries

## Open

None.

## Parked

- PRE-REBASE-REF - fold-harness left a local safety branch `fold-harness/pre-rebase-main` (old harness main 57226cdea) on terra only; main is pushed and level. Recommended a) (high, destructive, not yet blind-reviewed): delete it with `git branch -D`; b) keep it as a recovery reference. Not blocking the move.
- CLI006-READY - set [KI-TOOL-TECHNE-CLI-006 (pruned)](https://github.com/knowledgeislands/tools-techne/blob/ffcaf0c099f1d3019247ff97466754b8a7312166/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) to Ready: replanned at tools-techne `31c7b7d`, audits pass. Recommended a) (medium): Kris reviews the plan, then a ki-plan run sets it to Ready.
- CLI006-CONFIRM - how `techne host rebuild` and `withdraw` meet `destroy.sh`'s `CONFIRM_DESTROY_AGENT_HOST`: a stale export could confirm a destroy on a clean host. Recommended a) (medium, review disagrees): pass-through scoped to the one command; the reviewer prefers b) at high, a Harness-declared confirmation with fresh interactive consent.
- PROJECT-CLOSE - retire [Estate factorisation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/estate-factorisation.md), whose whole-estate Outcome was never met. Recommended a) (high, reviewed): retire it, keep OAI-1 as delivered, write FND-3 to EVAL-2 as ideas, route OBS-ACTIVATION to Observatory and GOVERNANCE residuals to State of play, and settle HOST-WRITES, ALIAS-OWNERS and RIG-REFS first.
- From va-consolidate (24 October), input for RESTART-ON-SOL, to be consolidated with the queues on Sol. Medium-confidence ones not yet blind-reviewed; full blocks in [design/va-consolidation.md](design/va-consolidation.md):
  - SUMMARY-WINDOW - Done counts from the mark; In Progress and Outstanding carry only this work's own items. Recommended a) (medium): yes, a hand-off is reported once and not carried; for ki.ways-of-working.
  - COORD-MOVES - add `hold`, `drain`, `resume`, `send` and `receive` commands. Recommended a) (medium): `drain` finishes running work and launches nothing new, staying With worker; `hold` drains and holds.
  - SOP-CASCADE - running a territory from one thread, thread metadata and host awareness, against the "executes nothing" and "no host" rules. Recommended a) (medium): ki.ways-of-working shapes it with `ki-work-design` first, then enacts it.
  - TENDING-FOLD - fold in round 2 and add the AGENTS.md and CLAUDE.md overlap checks at levels 3 and 4. Recommended a) (high): one design-note edit.
  - SIZE-LABEL - show sizes as 👕 plus a capital letter, with no XS. Recommended a) (high): a display convention in `ki-work-roadmap`.
  - PRODUCT-RECORDS - capture harness records for Always Use HTTPS and the `node_modules` rule (FILES-6). Recommended a) (high): one bounded capture run.
  - HARNESS-ORIENTATION - harness root orientation in `AGENTS.md`. Recommended a) (medium): a message to ki.baseline-rollout.
  - SANCTUARY-STAGE5 - Knowledge Islands takes stage 5. Recommended a) (medium): agree now, and set its Project and repository at the stage 4 handover.
- From skills-assessment (24 October), input for RESTART-ON-SOL. The matrix, gaps and proposed baseline are in [skills-assessment.report.md](skills-assessment.report.md). Medium-confidence queries are not yet blind-reviewed:
  - BASELINE - adopt one Capital baseline: the skills, configuration, structure and the `AGENTS.md`/`CLAUDE.md` split, recorded in `ki-repo-kb-principal`. Recommended a) (medium).
  - HARNESS-LINK - list each territory harness in its Capital's `[repo].harnesses`. Recommended a) (medium).
  - GRANOLA - declare `ki-acquire-granola` where it is used and retire the local commands in hnr and legal. Recommended a) (medium).
  - LEGAL-GUIDANCE - move legal's mandates from `CLAUDE.md` into `AGENTS.md` and promote its disciplines into skills. Recommended a) (medium).
  - HNR-GUIDANCE - rewrite hnr's `AGENTS.md` and its stale Headroom block. Recommended a) (high).
  - THEME-REGISTRY - tmx, si and legal follow their own records; er is asked to capture one. Recommended a) (high).
