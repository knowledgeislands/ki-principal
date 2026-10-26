# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › core063

**🤖 → 👤 Handoff to supervisor · Run report at 23:44 BST · last mark 23:36 BST**

---

## Done

- [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) adopted to Now and planned to Ready under Kris's RIG-ORDER a) decision of 23:27 BST, then delivered; its status is now Awaiting review, not self-accepted.
- Commit `41adda2` docs(roadmap): plan [KI-TOOL-RIG-CORE-063 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/735a8e8560f951afeaa0194df52c5dffa26a3797/docs/roadmap/KI-TOOL-RIG-CORE-063-fatal-bats-assertions.md) to Ready.
- Commit `7665767` test: make bare Bats assertions fatal under Bash 3.2 - the 64 bare assertions across the nine suites now end `|| false`, and the flaky firewall global-flush check matches only pfctl's own `-d` or `-X` argument, so a temporary path containing `-X` no longer trips it.
- Making the assertions fatal exposed no latent fault and no Rig defect, so no follow-up record is needed.
- SHELL-FATAL audit: clear (was nine warnings). Full Bats suite: 582 of 582 pass. Shellcheck, syntax, assembly check, benchmark, native-provider smoke, manual lint and diff check: pass. Whole-repository audit: no failures.
- Both commits are local only in tools-rig on `main`; nothing pushed, applied live or touched elsewhere.

## In Progress

Nothing is running. Pending handoff: tools-rig `main` on sol holds the two unpushed commits above.

Outstanding - no action requested now:

- The roadmap audit still warns that four other records, including [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md), lack a `size` field; [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md)'s planning can add its own.

## Queries

No outstanding queries
