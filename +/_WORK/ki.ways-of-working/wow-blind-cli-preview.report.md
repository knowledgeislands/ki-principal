VERDICT: convention · confidence medium - Standardise public writers gradually while retaining destructive and review safeguards.

# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-blind-cli-preview

**🤖 → 👤 Handoff to supervisor · Run report at 01:20 BST · last mark not supplied**

---

## Done

Recommend the convention for public, owned mutating commands: act by default, preview with `--dry-run`/`-n`, reserve `--check` for verification that fails on findings, and remove routine write gates through each tool’s owning work over time.

Update both standards now: the repair-specific preview requirement appears in [the tool standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md:153) and [the CLI guidance](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md:55); changing only one leaves conflicting guidance, while changing neither contradicts the owner’s repair decision.

The sample supports a shared direction: [mgit repair](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit:2258), [ki repo repair](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/repo/repair.ts:36) and [ki repo conform](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/repo/conform.ts:64) act by default; [ki repair](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/commands/manage/repair.ts:61) and [Almanac repair](/Users/krisbrown/workspaces/knowledge-islands/tools-git-almanac/src/cli/run.ts:174) retain routine preview gates.

The owner’s statement directly settles mgit, not every shipped interface; confidence is medium for the wider policy. Adopt the small rule now, then reconcile compatibility, help and behaviour deliberately in owning work without a fleet-wide flag migration.

Keep named exceptions for destructive user-data deletion, uninstall and reviewed-proposal flows: [Rig remove](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/00-runtime.bash:176) requires explicit consent, while [Rig repair](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/35-adoption.bash:126) produces a separately reviewed file. Removing known disposable managed links is not a blanket reason to exempt every repair.

Preserve explicit targets, privilege grants, data-loss checks and live-operation authority. Writing by default is risky for [firewall/service changes](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/src/rig/29-firewall.bash:546) and [remote host removal](/Users/krisbrown/workspaces/knowledge-islands/tools-techne/src/cli.ts:823); connection-critical work still needs its tested restore path, and destructive gates remain exceptions.

A preview must prevent local and provider mutations, not merely suppress the final write; read-only diagnostics remain read-only. Scope the convention to public CLI actions, leaving private lifecycle hooks such as [plan stamping](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/hooks/plan-stamp.sh:1) and passed-through third-party flags outside the retrofit.

Checks: both standards and source samples across all six named areas inspected; static review only, with no executable tests or remote calls. Repository edits and commits: none.

## In Progress

Nothing is running.

Reporting limitation: the parent’s last-mark time was not supplied; it remains unspecified because work packages and other reports were excluded from this blind review.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 01:20 BST

🎯 1 handoff · 🤖 0 running · ⛔ 0 blocked

- [handoff] CLI-PREVIEW recommendation and safety exceptions · supervisor · since 01:20 BST

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
