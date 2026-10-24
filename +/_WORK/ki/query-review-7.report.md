# [Knowledge Islands](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Charter.md) › State of play › query-review-7

**🤖 → 👤 Handoff to supervisor · Run report at 00:52 BST · last mark 23:46 BST**

---

## Done

Reviewed [KI-TOOL-TECHNE-CLI-006](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md); exact-content comparison passed against the replan at `31c7b7d`.

Parsed the [recipe manifest](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/recipes/agent-host/recipe.toml:47): both operations resolve to destroy, and the confirmation variable is undeclared.

Checked [destroy's confirmation gate](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/operations/aws/agent-host/destroy.sh:57), its [risk and identity guards](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/operations/aws/agent-host/destroy.sh:96), the [operator guide](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/guides/operator/agent-host.md:443) and [ADR-KI-PRINCIPAL-006](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-006-techne-implementation-ownership.md:36); the recommendation below follows those local sources.

No repository writes, commits, remote calls or live commands were made; only the required run status and report were written. Verification was static; no destructive script was executed.

## In Progress

Nothing is running. This review makes no implementation change or adoption decision.

## Queries

### [CLI006-CONFIRM](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/docs/roadmap/KI-TOOL-TECHNE-CLI-006-guarded-host-commands.md) - Declare destructive confirmation before CLI delivery

**Context:** The manifest declares the operations and their script, but gives the CLI no confirmation contract. The script independently requires the stack-name environment value before any AWS call. Missing or wrong confirmation therefore fails closed today. The ADR assigns the interface to the manifest and the declared binding-to-environment contract; the operator guide documents direct script use, but is not machine-readable operation metadata. Generic environment inheritance is not itself a CLI hard-coded dependency, so A can preserve the existing script guard. It nevertheless leaves the CLI workflow dependent on an undeclared prerequisite. More significantly, an exported value can survive previous operations and satisfy the guard again without fresh consent. For a clean host, the script proceeds without a typed prompt; its typed discard prompt is only for unknown or unreadable work. Clean workspace status establishes work safety, not consent to delete infrastructure or credentials.

**Query:** Should rebuild and withdraw wait for a Harness-declared confirmation contract rather than adopt environment pass-through as the finished CLI interface?

**Options:**

a) (recommended, confidence high - the sources confirm both the interface gap and the absence of a fresh prompt for clean destruction) Choose B. Have the Harness declare operation confirmation semantics, including the environment key, the expected value derived from the selected binding and the requirement for fresh interactive consent. Agree and validate the corresponding manifest schema in the CLI. Prompt with the resolved target and the named operation, distinguishing rebuild's retained credentials from withdrawal's deletion, then pass the matching value only to that invocation. Reject absent, unsupported or malformed confirmation metadata before execution; ambient values must not substitute for that prompt. Rebuild and withdraw wait for this contract; independent status and stop work can proceed. Keep all script-owned workspace, override, account and same-host guards. Merely declaring an ordinary parameter with a default equal to the stack name would auto-confirm destruction and misses B's central safety requirement.

b) Choose A as a consciously limited compatibility route. It avoids CLI hard-coding and still refuses when the variable is absent or wrong, but guide referral does not resolve the undeclared interface or ensure fresh consent. Prefer command-scoped operator assignment over a persistent export. This remains a weaker finished interface, and interactive-terminal presence alone does not supply confirmation.

c) Choose C only after changing the declared ownership boundary. A fresh stack-name prompt improves consent, but setting the undeclared Harness variable couples the CLI to an implementation detail and can drift across independently released versions. Do not adopt it under the current ADR. Neither this prompt nor B's prompt replaces the script's distinct discard confirmations or the binding owner's authority for a live operation.

### 🤖 → 👤 Handoff to supervisor · since 00:52 BST

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] CLI006-CONFIRM review recommendation · supervisor · since 00:52 BST
