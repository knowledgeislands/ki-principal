# ki.chezmoi queries

## Open

### [ZED-WINDOW - A second mcporter window on Sol with a Zed start](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md)

**Context:** Kris asked whether this item is needed. [KB-DOTFILES-UE-100](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md) Sol's 30-minute read-only window saw no growth: 155 transports, 112 processes, about 5.2 GiB. All growth came in the daemon's first hour as 14 sets of 8 servers, seven of them 2 to 3 seconds after a Claude Code session launched from Zed; 32 sessions started outside Zed added none. That is a correlation, and the window cannot set a safe limit. The stage is Awaiting review (chezmoi `f6a36e5`).

**Query:** Will you start a Zed Claude session yourself partway through one more 30-minute window on Sol?

**Options:**

a) (recommended, confidence high - reviewed, an ordinary attended Zed start tests the strongest correlation within a bounded window) Authorise one more attended 30-minute Sol window, with you starting a Zed Claude session partway through.

b) Review the Sol findings as they stand, and decide on a mitigation after Terra.

c) Leave the evidence stage here.

### [AGE-DOC - The age recovery document's vault](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md)

**Context:** Kris asked what this asks: in short, which 1Password vault holds your age recovery document now? The setup guide restores the "Dotfiles chezmoi age recovery identity" document from the Personal vault by hand. No render reads it, and only you can confirm where it lives now.

**Query:** Should the setup guide keep naming the Personal vault?

**Options:**

a) (the planning run's recommendation, confidence medium) Keep Personal, as the plan does.

b) (the blind review's recommendation, confidence high - only you can confirm the location) You name its current vault and the source steps update the guide to match, keeping Personal if you confirm it.

c) Move it into Automation; both advise against, since every agent holding the token could then read the age identity.
