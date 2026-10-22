# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rig-live

**🤖 → 👤 Handoff to supervisor · Run report at 08:33 BST · last mark 08:07 BST**

---

## Done

- Both Macs report `rig 0.7.0+dev`. On each one, `rig` is the tools-rig checkout at `424727c` linked in `~/.local/bin`, not the packaged `v0.7.0` release. Both run macOS 27.0.1. I reached `terra` over the tailnet by SSH.
- Live read-only evidence is now in the verification section of both records, committed in tools-rig as `22d4ed9` and pushed fast-forward to `origin/main`. Neither record is accepted. Checks: `ki repo audit` passes with no failures (only warnings already present: HOOK-1, SHELL-FATAL and the `.rumdl.toml` OWN-1 drift), and `git diff --check` is clean. I did not run Bats, ShellCheck or the benchmark, because only the two records changed.
- [KI-TOOL-RIG-CORE-042](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-042-profile-filtered-dock-items.md): your Dock declaration hasn't changed yet. It is still laptop-only with no tool links, and [KB-DOTFILES-UE-091](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-091-shared-dock-tool-links.md) is still a draft. So `sol` shows the Dock as not selected and doctor says nothing about it. On `terra` the real laptop Dock is `present`.
  - I tested the shared layout against a throwaway copy of the configuration. On `sol`, show, status, doctor and the dry-run all agree: 34 of 38 items are included, Zed sits between Claude and Visual Studio Code, and Delta, RendApp, The Tower and ChatGPT are left out. Every included app's path exists on `sol`. The Dock itself was unchanged on both Macs.
  - One finding for your personal configuration: the catalogue entry for ChatGPT (`chatgpt-current`) belongs to no profile. If KB-DOTFILES-UE-091 links it to the Dock item, ChatGPT drops off both Docks, `terra`'s included.
- [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md): neither Mac's configuration declares a firewall.
  - `terra` already has the Rig anchor and its startup daemon, installed on 14 October at 08:49. Rig has no receipt for them, so it would not retire them. They match the current renderer byte for byte, and the daemon has reloaded cleanly since the 15 October restart.
  - That live anchor uses the range rule, so the residual `100.64.0.0/10` risk applies to `terra` today: on a carrier-grade NAT or hotspot network, a neighbour holding an address in that range can reach port 5900. A forged tailnet source can also deliver one-way UDP over the LAN.
  - `sol` has no restriction. Rig correctly reports it `missing (exposed-beyond-tailnet)`. SSH from `sol` to `terra` over the tailnet works.
- No apply, sudo, firewall or Dock change, and no other remote call. Net record count in tools-rig: 0 new.

## In Progress

- Nothing. Each record's live criteria now need a live change or a privileged read, so I stopped there as the brief directs.

## Queries

### RIG-DOCK-LIVE - KI-TOOL-RIG-CORE-042 acceptance

**Context:** Every criterion that a fixture or read-only check can reach is evidenced, and every included app is checked on `sol`. But the acceptance check on `sol` needs three things that haven't happened yet: the KB-DOTFILES-UE-091 declaration delivered (with ChatGPT left unlinked), a real `rig apply` of the Dock, and afterwards `present` on both Macs.

**Query:** Should KI-TOOL-RIG-CORE-042 stay at Awaiting review until KB-DOTFILES-UE-091 lands and you approve the live Dock apply on `sol`, rather than be accepted now?

**Options:** a) (recommended, confidence high - the apply and post-apply checks are the record's own acceptance criteria, and none can be proved read-only) hold acceptance; deliver KB-DOTFILES-UE-091 first without linking ChatGPT, then run an attended `rig apply --target dock:workstation` on `sol` and the checks on both Macs. b) accept now on the fixture and read-only evidence, and track the live check as a follow-up. c) return it to in-progress.

### RIG-FIREWALL-LIVE - KI-TOOL-RIG-CORE-047 acceptance

**Context:** Observation, rendering and the read-only boundary are proved live on both Macs, and the residual `100.64.0.0/10` risk is stated in the record and is live on `terra` today. Still unproved, because each needs `sudo`, a restart or a live change: the loaded kernel rules, `vnc://` over the tailnet, refusal on the LAN, the NordVPN check on `sol`, and any `apply --sudo`. The `terra` anchor also has no declaration or receipt behind it.

**Query:** Should KI-TOOL-RIG-CORE-047 stay at Awaiting review until an attended session at the machine, with the documented no-Rig rollback ready, runs those live checks?

**Options:** a) (recommended, confidence high - the remaining criteria need a privileged, connection-critical session, and terra's unreceipted anchor should be adopted by a declaration first) hold acceptance; add the personal declaration through chezmoi, run `rig apply --sudo` attended on `terra` and then `sol`, and do the live checks. b) accept now and carry the live checks to a follow-up record. c) remove `terra`'s unreceipted anchor and start live acceptance afresh.
