# ki queries

## Open

### CLI006-READY - Set the guarded host commands plan to Ready

- **Context:** [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) has been replanned against today's sources (tools-techne `31c7b7d`), and its audits pass. Structured status becomes authoritative. Stop runs under the operator profile, and rebuild and withdraw run under the administrator profile. It also fixes a wrong-profile bug and a missed `destroy.sh` confirmation guard. Ready waits for your review of the plan and for CLI006-CONFIRM.
- **Query:** Set KI-TOOL-TECHNE-CLI-006 to Ready?
- **Options:**
  - a) (recommended, confidence medium - the plan is grounded and passes its audits, but it is a plan review that is yours to make) Review it in the morning, then have a ki-plan run set it to Ready.
  - b) Set it to Ready now.
  - c) Keep it as draft at `next`.

### CLI006-CONFIRM - How rebuild and withdraw meet `destroy.sh`'s confirmation (in blind review: query-review-7)

- **Context:** `destroy.sh` needs `CONFIRM_DESTROY_AGENT_HOST` set to the stack name, but the recipe manifest does not declare it.
- **Query:** How should the CLI meet it?
- **Options:**
  - a) (medium) Pass it through from your environment.
  - b) The Harness declares it in `[operations]`.
  - c) The CLI prompts for it and sets it.
