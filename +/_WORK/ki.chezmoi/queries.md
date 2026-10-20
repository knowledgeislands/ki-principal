# ki.chezmoi queries

## Open

### [AGE-DOC - The age recovery document's vault](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md)

**Context:** Kris asked what this asks: in short, which 1Password vault holds your age recovery document now? The setup guide restores the "Dotfiles chezmoi age recovery identity" document from the Personal vault by hand. No render reads it, and only you can confirm where it lives now.

**Query:** Kris confirmed the document but thinks Personal is the wrong vault (Decision 160). Which vault holds it now? `op item get "Dotfiles chezmoi age recovery identity" --format json | jq -r .vault.name` shows it without revealing the contents.

**Options:**

a) (the planning run's recommendation, confidence medium) Keep Personal, as the plan does.

b) (the blind review's recommendation, confidence high - only you can confirm the location) You name its current vault and the source steps update the guide to match, keeping Personal if you confirm it.

c) Move it into Automation; both advise against, since every agent holding the token could then read the age identity.
