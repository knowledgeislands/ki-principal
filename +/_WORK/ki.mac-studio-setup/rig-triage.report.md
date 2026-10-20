# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › rig-triage

**🤖 → 👤 Handoff to supervisor · Run report at 00:20 BST · last mark 00:20 BST**

---

## Done

- Triaged all eight unadopted Triage records in tools-rig; dispositions are in the table below. Two were high-confidence Now, both tools burn-down, and both are delivered to Awaiting review. Neither is self-accepted.
- [KI-TOOL-RIG-CORE-066](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CORE-066-plan-managers-and-uv-prerequisite.mdCORE-066): a first `rig apply` now installs uv through a declared mise prerequisite before the uv tools that need it. G2, the doctor manager list, was not built because its premise does not match the code; it is in the query below. Commits `d0ea743` (plan to Ready) and `969ec58` (delivery). Gate: bats 584 of 584, audit no failures, shellcheck, assembly, benchmark, native-provider smoke, mandoc and diff check all pass.
- [KI-TOOL-RIG-CORE-065](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CORE-065-resource-subject-links.mdCORE-065): settings, services, scheduled jobs, firewalls and default applications can name the tool they configure with `tool = "ID"`. `rig show` JSON carries `configured_by` on every tool, the tool table gains a `CONFIGURED` column, `rig show TOOL` gains a "Configured by" line, and new specification clause RIG-QUERY-009 covers the JSON. Public export is unchanged. Commits `fd3634c` (plan to Ready) and `9eb01f3` (delivery). Gate: bats 590 of 590, after one exact-output expectation was updated for the new line, plus all the checks listed above.
- Nothing was applied live, pushed, accepted, pruned or created. [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) and [KI-TOOL-RIG-CLI-027](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CLI-027-command-line-convention-departures.mdCLI-027) were left alone.

## In Progress

Nothing is running. Pending handoff: tools-rig `main` on sol holds unpushed commits. By the last local view, without a fetch, it is 1 commit ahead of `origin/main`. The rig.midnight.ninja site will show configured tools only after the chezmoi repository adds `tool` to Kris's declarations.

Ideas for the coordinator, not captured as records: the developer guide could note that `bats --jobs` needs GNU parallel, which this Mac lacks; and a firewall or scheduled-job case could be added to the subject-link tests.

## Queries

**RIG-TRIAGE**

**Context:** Six triage dispositions are below high confidence, so I recorded them without applying them, as the brief requires. Separately, KI-TOOL-RIG-CORE-066's G2 asked doctor to list missing managers. Doctor already reports a missing manager per tool as unavailable whenever configuration loads, and its manager probe runs only when configuration fails to load, where there is no plan to compare against.

**Query:** Do you approve the dispositions in the table for KI-TOOL-RIG-CORE-053, KI-TOOL-RIG-CORE-057, KI-TOOL-RIG-CORE-064, KI-TOOL-RIG-CORE-067, KI-TOOL-RIG-CORE-068 and KI-TOOL-RIG-CORE-069, and where should G2 go?

**Options:**

a) (recommended, confidence medium - each needs a design or attended decision before delivery) Apply the table as written: 053 and 067 to Next; 057 and 064 to Future; 068 adopted to Next and planned, with implementation waiting for your attended NordVPN check; 069 adopted to Now but planned only after you confirm on a Mac which handler interface works. Fold 066's G2 into KI-TOOL-RIG-CORE-067, whose per-manager finding is the useful part.

b) Same as a), but keep G2 in KI-TOOL-RIG-CORE-066, re-scoped as a manager summary line on doctor's loaded-configuration path.

c) Hold all six in Triage for now, and leave G2 undelivered in KI-TOOL-RIG-CORE-066.

| Record | Disposition | Confidence | Reason | Done here |
|---|---|---|---|---|
| [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) | Adopt into Next | medium | You chose report-only, but it is large and not tools burn-down | Recorded only |
| [KI-TOOL-RIG-CORE-057 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e53/docs/roadmap/KI-TOOL-RIG-CORE-057-github-desktop-repository-list.md) | Future | medium | Open design questions: mgit manifest reading, confirming opens, hook or tool action | Recorded only |
| [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) | Future | low | Unclear whether it belongs in Rig, a ki-principal Activity or chezmoi checks | Recorded only |
| [KI-TOOL-RIG-CORE-065](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CORE-065-resource-subject-links.mdCORE-065) | Now | high | You chose its shape (SITE-CONFIG-SHAPE a); tools burn-down; the site waits on it | Delivered to Awaiting review, `fd3634c`, `9eb01f3` |
| [KI-TOOL-RIG-CORE-066](https://github.com/knowledgeislands/tools-rig/blob/4ca939fa230b3e9eb02d9a170491a544a51b3651/docs/roadmap/KI-TOOL-RIG-CORE-066-plan-managers-and-uv-prerequisite.mdCORE-066) | Now | high | Small corrective, tools burn-down | Delivered to Awaiting review, `d0ea743`, `969ec58`; G2 queried |
| [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) | Next | medium | Large model change that may need a Decision Record | Recorded only |
| [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) | Adopt into Next, plan only | medium | High priority and connection-critical, but implementation waits for your attended NordVPN check | Recorded only |
| [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) | Now, after your check | medium | Planning must confirm the handler interface on a real Mac, which changes sol's live handler configuration | Recorded only |
