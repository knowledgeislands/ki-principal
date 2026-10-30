<!-- rumdl-disable MD041 -->

### ORCA-CLOSE-OUT

**Context:** Orca's guide counts supervised work as done only when each settled worker has been reused, explicitly retained or released, and KI's coordination and delegation guidance says nothing about it; two succeeded trial workers of `ki.prj.orca-evaluation` on sol are still waiting for that decision. Release closes only the worker's own terminal after archiving its output, keeps the Task and Dispatch records, and does not delete conversation history; deleting history is a separate GUI-only AI Vault action that cannot be undone. Section 3 already has `ki agent close` release ki-launched workers once Part B lands, which covers only runs `ki agent` starts.

**Query:** Should the five-step close-out rule above go into the `ki-coordination` standard now, as a message to the harness, rather than waiting for Part B?

**Options:**

1. Wait for the ORCA-SUBAGENT-PILOT and Part B, and fold the rule into `ki agent close` only, leaving hand-started workers to the work that started them.
2. Send the rule to the harness now and also make AI Vault session deletion part of close-out, with Kris's go per session, to declutter the history list.
3. Yes: send the rule to the harness now as a message, covering receive, mark, hold and Finished, with history deletion kept out of close-out; `ki agent close` takes over ki-launched workers when Part B lands.

### ORCA-PLACEMENT

**Context:** If the pilot shows nesting, Part B can start workers with Orca's own launch (`worker-start --agent`, which uses Kris's Orca agent-launch settings and cannot pass `--add-dir`), or create an Orca terminal running today's exact `claude`/`codex` command and hand it to `worker-start --terminal`, which keeps today's autonomy flags but is the low-level route Orca reserves for argv it cannot express. The first is simpler and closer to how Orca's own sub-agents start; the second preserves today's run contract exactly. Which one works depends on the pilot's permission and directory findings.

**Query:** Should Part B use Orca's own agent launch, or adopt a terminal running today's command?

**Options:**

1. The terminal route from the start, `terminal create --command` plus `worker-start --terminal`.
2. Orca's own launch, `worker-start --agent`, switching to the terminal route only if the pilot shows prompts or blocked writes.

### ORCA-QUEUE

**Context:** Orca does not start a task when its dependencies finish, so ki's dispatcher must still start a queued run when its `--wait-for` gate opens. The dispatcher keeps the coordinator's environment and can start the run as an Orca worker while the coordinator's chat is live; after the chat ends, Orca will most likely not accept it as the caller, and the run would start detached as today. The alternative is to keep every queued run detached so that queued and immediate runs behave the same.

**Query:** When a queued run's gate opens, should the dispatcher try the Orca path first and fall back to a detached launch?

**Options:**

1. Queued runs stay detached; only immediate launches use the Orca path.
2. Orca first while the parent chat is live, detached otherwise, with the placement and reason in the receipt.
