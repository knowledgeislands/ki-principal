# query-review-7

Blind review of one query. Read-only: make no writes and no commits. Read `tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md` (replanned at `31c7b7d`), the ki-techne-harness recipe manifest and `destroy.sh`, its operator guide, and `ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-006*`.

**CLI006-CONFIRM.** `destroy.sh` refuses to run unless `CONFIRM_DESTROY_AGENT_HOST` equals the stack name. The recipe manifest does not declare this variable, and ADR-KI-PRINCIPAL-006 makes the manifest the only contract between the CLI and the Harness. How should `techne host rebuild` and `techne host withdraw` meet this confirmation?

- A: pass it through from the operator's environment, never set it in the CLI, and point the CLI docs to the Harness operator guide.
- B: have the Harness declare the confirmation in its `[operations]` table so the CLI can prompt for it; rebuild and withdraw wait for that change.
- C: have the CLI prompt for the stack name and set the variable itself, which hard-codes an undeclared Harness variable.

Give your own recommendation, with its confidence (high, medium or low), your reasons, and any safety risk an option misses.

Report to the path your run packet names, as an owner report: Done, In Progress, Queries.
