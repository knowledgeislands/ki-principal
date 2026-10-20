# key-blind

Work: ki.chezmoi (KI > Rig > chezmoi). Repository: /Users/krisbrown/.local/share/chezmoi, on Sol. Read-only blind review of two queries.

Read docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md (planned in commit 563afe9) and docs/guides/user/setup-mac-rig.md.

AGE-DOC. Context: the setup guide restores the "Dotfiles chezmoi age recovery identity" document from the Personal vault by hand; no render reads it, and only Kris can confirm where it lives now. Query: should the setup guide keep naming the Personal vault? Options: a) keep it, as the plan does; b) Kris names its current vault and source steps update the guide to match; c) move it into the Automation vault.

RIG-KEYCHAIN. Context: the retired Rig service account's token was kept in the login Keychain under `ki-op-service-account-rig` on 12 October; the token is revoked and no source names it. Query: should Kris's attended step on each Mac also delete that Keychain entry if present? Options: a) yes, add `security delete-generic-password -s ki-op-service-account-rig` to the attended step and say so in the record before Ready; b) no, leave it outside this record.

For each query pick one option and give your confidence (high, medium or low) with a one-line reason. Read-only: edit nothing, commit nothing; run no `op` or `security` command.

Report: heading `# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › key-blind`, Done, In Progress and Queries.
