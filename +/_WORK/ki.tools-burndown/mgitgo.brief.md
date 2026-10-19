# mgitgo - accept and release mgit v0.18.0

Work: ki.tools-burndown (/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown). Authority: Kris, 19 October, BURNDOWN-ACCEPT a) and MGIT-GO a) in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md.

1. In /Users/krisbrown/workspaces/knowledge-islands/tools-mgit, accept KI-TOOL-MGIT-CLI-028 and then KI-TOOL-MGIT-CLI-023 under ki-accept.
2. Publish v0.18.0 on 9a3564d (MGIT-TAG-TARGET): tag it, push main and the tag fast-forward only, create the GitHub release, verify the installer, and let the Homebrew tap open its formula pull request, following the repository's release guide and /Users/krisbrown/.local/state/ki/agents/tools-burndown/mgitrel.report.md.
3. Append one line to /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/messages.md: mgit v0.18.0 is released; CONSUMER-MIGRATE can proceed. Commit that file alone by explicit path in ki-principal and push fast-forward. Never --no-verify, never force-push. Report the outcome and any query as your footer says.
