# estfix - finish the estate hook migration

Kris ordered the whole estate off Husky (decisions.md, 23:24 BST) and set TO-DONE. Read /Users/krisbrown/.local/state/ki/agents/tools-burndown/estmig-org.report.md and /Users/krisbrown/.local/state/ki/agents/tools-burndown/qreview9.report.md, then carry out, as recorded in /Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md at 00:21 BST:

1. YORK-YARN: in techmedix/apps-yorkphotosoc.org, remove Husky with Yarn (`yarn remove husky`, registry access allowed), then `ki repo conform`, keeping lint-staged and Commitlint and binding `prepare` in the same commit.
2. PKG-NO-HUSKY: in humans-not-robots/hnr-principal and legal/legal-principal, install a frame-first check-only Knowledge Base `.githooks/pre-commit` as va-principal has, add the `prepare` binding to both manifests, bind with conform. No commit-msg until KI-TOOL-KI-CLI-161.
3. NO-GATE: in equal-remedy/apps-dafacts.org, personal/apps-kris.me.uk and personal/acquire, install a frame-first pre-commit running `ki repo audit --skill ki-repo --staged` check-only, and bind it. Check it is practical for acquire's preserved captures; if not, report and skip acquire.

Verify each as estmig-org did (hooksPath, refusal with ki off PATH in a fresh worktree, the real commit passing through the hook, no HOOK finding). Revert conform's `.rumdl.toml` rewrite and any `rumdl --fix` reflow it makes. Commit by explicit path, never --no-verify or force-push; push each fast-forward only if the stacked commits are all yours; leave other sessions' files and commits alone and name them. Report one line per repository under Done, In Progress and Queries.
