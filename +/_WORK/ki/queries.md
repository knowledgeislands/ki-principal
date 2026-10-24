# ki queries

## Open

### HARNESS-OAUTH - Two versions of the ki-binding OAuth change block the harness

**Context:** ki-agentic-harness main is 8 commits ahead of origin and 1 behind. Local fceb8dc2e and origin's 76f7e7d3d make substantially the same OAuth change to ki-binding in different code; a rebase conflicts in five files, so level-for-sol aborted and left main untouched. Origin's version has stricter BIND-2 wording and negative tests; the local one adds YAML and multi-client coverage and documents that an absent marker stays absent. The 8 local commits include the SOP-SECONDARY merge. Until settled, Sol's clone of the harness lacks those 8 commits.

**Query:** How should the two OAuth changes be reconciled so harness main can be pushed?

**Options:**

a) (recommended, confidence high - reviewed: the behaviour already agrees, so a small reconciliation keeps both sets of coverage) A bounded run keeps origin's 76f7e7d3d as the base, folds in only fceb8dc2e's extra documentation and tests, replays the other local commits, checks the result against today's main, runs the full harness tests, type check and hooks, then pushes fast-forward. b) Drop fceb8dc2e and replay the other 7 commits, losing its extra coverage. c) Kris resolves the conflict by hand on terra.

### TOOLS-KI-BRANCH - tools-ki's secondary States of play work is not on main

**Context:** tools-ki is checked out on `sop-secondary`, 2 commits ahead of main and on origin but unmerged: the secondary States of play support with `ki agent prompts`, and an inbox hand-in. Main is its ancestor, so it is a clean fast-forward. The harness already carries the matching contract. A fresh clone on Sol would lack the command.

**Query:** Should tools-ki main take this before Sol starts?

**Options:**

a) (recommended, confidence high - reviewed: a clean fast-forward that supplies the CLI side of a contract the harness already has) A bounded run runs tools-ki's tests, coverage gate, type check and hooks, fast-forwards main, pushes and returns the checkout to main; the inbox hand-in stays for normal triage. b) Leave it on the branch for Sol to fetch explicitly.

### WHITEPAPER-BRANCH - An unmerged white-paper guidance branch in a run worktree

**Context:** A worktree from the fourth-white-paper run holds `docs/whitepaper-authoring-learning`, one commit (26e46c185) of white-paper guidance, criteria and tests, built on an old harness revision. The reviewer found a local origin reference to it, so it is probably already on origin. Merging it needs its own reconciliation (its criteria count is stale).

**Query:** What should happen to it before the move?

**Options:**

a) (recommended, confidence high - reviewed: preserving it avoids loss without adding unrelated work to the move) Within the harness run, confirm origin holds 26e46c185 and push the unchanged branch only if not; leave the worktree; integration later from Sol. b) Reconcile and merge it into main as part of the harness run. c) Leave it on terra only.

## Parked

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
