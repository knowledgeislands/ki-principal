# ki queries

## Open

### CLI006-READY - Set the guarded host commands plan to Ready

- **Context:** [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) has been replanned against today's sources (tools-techne `31c7b7d`), and its audits pass. Structured status becomes authoritative. Stop runs under the operator profile, and rebuild and withdraw run under the administrator profile. It also fixes a wrong-profile bug and a missed `destroy.sh` confirmation guard. Ready waits for your review of the plan and for CLI006-CONFIRM.
- **Query:** Set KI-TOOL-TECHNE-CLI-006 to Ready?
- **Options:**
  - a) (recommended, confidence medium - the plan is grounded and passes its audits, but it is a plan review that is yours to make) Review it in the morning, then have a ki-plan run set it to Ready.
  - b) Set it to Ready now.
  - c) Keep it as draft at `next`.

### CLI006-CONFIRM - How rebuild and withdraw meet `destroy.sh`'s confirmation

- **Context:** `destroy.sh` needs `CONFIRM_DESTROY_AGENT_HOST` set to the stack name, and the recipe manifest does not declare it. The script fails closed today. The review found that on a clean host the script destroys with no typed prompt, so an exported variable left over from an earlier run could confirm a destroy without fresh consent.
- **Query:** How should `techne host rebuild` and `withdraw` meet the confirmation?
- **Options:**
  - a) (recommended, confidence medium - review disagrees: the planner prefers pass-through, which works today with no Harness change; the reviewer prefers b) at high, because pass-through gives no fresh consent and leaves the interface undeclared) Pass it through from your environment, preferably scoped to the one command rather than exported.
  - b) The Harness declares the confirmation in its manifest, including fresh interactive consent. The CLI prompts with the target and operation and passes the value only to that run. Rebuild and withdraw wait for this; status and stop go ahead.
  - c) The CLI prompts and sets the undeclared variable itself, which needs a change to ADR-KI-PRINCIPAL-006's boundary.

### PROJECT-CLOSE - Retire the Estate factorisation Project, keeping its unmet phases as ideas

- **Context:** [Estate factorisation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/estate-factorisation.md) has been on hold since 15 October, waiting for your close-out review. Its first two pieces of work are done, the groundwork records and OAI-1, and most parked items have finished or have live owners. Its whole-estate Outcome was never achieved, and phases FND-3 to EVAL-2 were never captured as records. Closing retires that Outcome by your choice; it does not certify it.
- **Query:** Retire the Project, keeping its phases as ideas?
- **Options:**
  - a) (recommended, confidence high - reviewed: both runs agree the duplicate coordination should end, but the reviewer says retiring an unmet Outcome is yours to choose, so it was not acted on overnight) Retire it.
    - Keep OAI-1 as delivered, and write the remaining phases as `Idea:` lines with their gates.
    - Route OBS-ACTIVATION's remaining health checks to Observatory (the local service is confirmed running) and the GOVERNANCE residual checks to State of play.
    - Settle HOST-WRITES, ALIAS-OWNERS and RIG-REFS explicitly before the finish and the prune.
  - b) Keep the Project, and capture FND-5 after re-grounding it against today's work model.
  - c) Leave it on hold, unchanged.
