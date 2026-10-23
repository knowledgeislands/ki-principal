# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › handover-route

**🤖 → 👤 Handoff to supervisor · Run report at 08:13 BST · last mark 23:56 BST**

---

## Done

- I went through every open, held, next-step and pending item in [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) under Kris's words of 22 October (Decision 206): "feel free to push out those messages to those threads to hand the work over now." Four handover lines went to two works and are published. Each line quotes Decision 206. Only NORDVPN-HOLD is marked important, because it carries a hold.
- [ki.mac-studio-setup messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/messages.md) got NORDVPN-HOLD (important), FW-EXPOSURE and HANDLER-FAIL in ki-principal `30018774`. They do not repeat RIG-REMOVAL, RIG-NOTIFICATIONS, RIG-COMMENT-KIND, [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md)'s sol probe or UTM-SOL, which that work already holds.
- [ki.tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md) got HOOK-ROLLOUT in ki-principal `ee440eef`.
- Checks: the commit gate's `ki repo audit` passed on both commits with no failures. The rebase onto upstream was clean, and only these two commits were stacked when I pushed. ki.chezmoi's files are untouched.
- I checked, without fetching, that every tools-repository hook commit and harness commit that ki.chezmoi listed as unpushed is already on origin, and so is the Rig site's apps-rig.midnight.ninja `680a95f`. So none of them is still pending.
- One material risk is still open. Terra's Screen Sharing firewall reports `exposed-beyond-tailnet`. It is now with ki.mac-studio-setup, but that work is on hold until Kris says resume, and a message line does not wake held work.

| Item | Decision | Tag | Work package |
| --- | --- | --- | --- |
| TOWER-APPLY (scoped apply of `40-macos.toml` and the save-nudge wrapper) | Stays: a reviewed chezmoi apply | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| TOWER-PATH (Rig artefact and Dock path moved to `/Applications`) | Stays (Decision 197 keeps the Rig paths here); waits on TOWER-MOVE | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| TOWER-MOVE (attended move of Tower Assistant to `/Applications`) | Already with kb.regular.site-tower: its next step 2 runs the move under [KB-MIDNIGHT-TOWER-APP-006](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/KB-MIDNIGHT-TOWER-APP-006-dock-icon-and-applications.md). No line sent: personal-principal is outside this run's write authority | - | [kb.regular.site-tower](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.regular.site-tower/work.md) |
| Tower Assistant app itself (Dock, icon, permissions panel, redesign) | Already with kb.regular.site-tower (TOWER-APP-SHELL and TOWER-APP-PERMS, Decisions 197 and 198) | - | [kb.regular.site-tower](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.regular.site-tower/work.md) |
| Shadowlab Spark removal on terra | Stays: Rig declaration and machine lifecycle | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Attended steps and acceptance for [KB-DOTFILES-UE-090](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-090-close-rig-bring-up-gaps.md) and [KB-DOTFILES-UE-100](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md) | Stays: chezmoi records | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| TRUST-COMPLETE (Decision 187) | Stays. The declaration is chezmoi data, `.chezmoidata/trusted-folders*.yaml` (chezmoi `13458343`); tools-ki `9252669a` only keeps VS Code trust apart from workspaces. Its home is a chezmoi (KB-DOTFILES) Decision Record, so it no longer has to be marked homeless | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| TRUST-RETURNED (Claude Desktop rewriting trust grants) | Closed: Decisions 193 and 195. trust-reconcile set Desktop's list to the 76 declared folders, and trust-check saw no rewrite over 200 seconds. The `state.md` text is stale | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Orca evaluation (ORCA-INSTALL) | Stays | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Starship: starship-preview and starship-adopt ([KB-DOTFILES-UE-104](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-104-evaluate-starship-with-chezmoi-drift.md)) | Stays | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| terminal-retire (Ghostty primary, iTerm2 and Warp retired) | Stays | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Motion and GitUp removal on sol; apply-check (one combined Rig apply) | Stays | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Hold on the Rig apply for both Macs (RIG-CASKS, Decision 65) | Stays: Kris's hold over applying | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Hold on the attended NordVPN trial ([KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md)); [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md)'s terra NordVPN checks (Decision 131) | Handed to ki.mac-studio-setup, which owns tools-rig records and the listener firewall | NORDVPN-HOLD (important) | [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/work.md) |
| Terra firewall exposure (FIREWALL-EXPOSURE, FW-SCREENSHARE) and sol's anchor ranges (Decision 145) | Handed to ki.mac-studio-setup, for [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md)'s attended rollout | FW-EXPOSURE | [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/work.md) |
| The 19 October handler failure on terra, and the `.toml` drift (Decision 104) | Handed to ki.mac-studio-setup, for [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md). Applying the Zed opener (chezmoi `faa4d3a`) stays here | HANDLER-FAIL | [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/work.md) |
| Sol's `rig doctor` findings hold (handler, firewall anchor range, UTM source) | Handed: the handler is already RIG-069-PROBE there, the anchor range went in FW-EXPOSURE, and UTM-SOL is already there | FW-EXPOSURE | [ki.mac-studio-setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.mac-studio-setup/work.md) |
| Hooks rollout, the "unpushed" tools-repository hook commits and harness commits, and [KI-TOOL-KI-CLI-165 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/fde00e978a4c9b0e697252bac3e0979f09d85e8c/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md) | Handed to ki.tools-burndown (HOOKS-STANDARD). The commits are on origin, and KI-TOOL-KI-CLI-165 is accepted (Decision 194) and pruned | HOOK-ROLLOUT | [ki.tools-burndown](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/work.md) |
| Rig site (apps-rig.midnight.ninja `680a95f`) and Kris's "come back and have another look" (Decision 179) | Owned by kb.regular.personal-rig (becoming kb.regular.site-rig). `680a95f` is on origin. The Rig-side fields are already RIG-COMMENT-KIND with ki.mac-studio-setup. No line sent: personal-principal is outside this run's write authority | - | [kb.regular.personal-rig](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/kb.regular.personal-rig/work.md) |
| WhatsApp refresh | Stays: it is [KB-DOTFILES-UE-035](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-035-install-whatsapp-spool-refresh.md), a chezmoi record on hold | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Vega rendering | Already with ki.agent-host as VEGA-XDG (Decision 158). [KB-DOTFILES-UE-084 (pruned)](https://github.com/krisb/dotfiles/blob/3f7c9bd867a0b447756826e2a4dde9feebc85d12/docs/roadmap/KB-DOTFILES-UE-084-render-zshenv-on-vega.md) was cancelled, so the hold is stale | - | [ki.agent-host](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.agent-host/work.md) |
| Privacy audits ([KB-DOTFILES-UE-071](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-071-audit-macos-privacy-permissions.md), [KB-DOTFILES-UE-094](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-094-audit-sol-privacy-permissions.md)) and the rationale audit ([KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md)) | Stays: chezmoi records, held until Kris resumes them | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Declaring per-app notification values once Rig supports them (RIG-NOTIFICATIONS) | Stays: waits on ki.mac-studio-setup | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Terra's disabled Paperclip plist (PAPERCLIP-PLIST, Decision 106) | Stays: waits on the Paperclip rebuild design | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Not raised: CORE-SET-COMMENTS, SSH-MARKER, MOTION-APPLY | Stays: no action | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |
| Not raised: RAT-UNCONFIRMED, RAT-READING | Closed: superseded by Decisions 179 and 181 | - | [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) |

No item lacks an owner.

### Lines for the coordinator to remove from `state.md`

- Remove the whole `## Now` bullet that begins `- Rig site rationale filter removed (apps-rig.midnight.ninja \`680a95f\`, unpushed).`. Everything in it is done and already recorded, and its "unpushed" commits are all on origin.
- Remove the whole `## Now` bullet `- Hook rollout: stages 1 and 3 delivered; stage 2 reached every repository, the tools shape included. KI-TOOL-KI-CLI-165 passed re-review and is Awaiting review; run \`ki repo conform\` only with \`--dry-run\` until Kris accepts it.` It was handed over as HOOK-ROLLOUT.
- In the `## Now` bullet beginning `- drift-apply applied all eight drifted targets on sol`, change `but running Claude Desktop rewrote them back (TRUST-RETURNED, with Kris)` to `TRUST-RETURNED closed (Decisions 193, 195)`.
- In the `## Now` bullet beginning `- motion-remove done:`, remove the sentence `Terra firewall anchor exposure seen again (FW-SCREENSHARE, kept with FIREWALL-EXPOSURE, not raised).`
- In the `## Now` bullet beginning `- Accepted (Decision 194):`, remove `KI-TOOL-KI-CLI-165 was already accepted and pruned.`
- Change next step 1 to `1. On terra: TOWER-APPLY (scoped apply of \`40-macos.toml\` and the wrapper, \`rig doctor\` after); once kb.regular.site-tower's attended move to \`/Applications\` is done, a short follow-up moves the artefact and Dock path (TOWER-PATH a).`
- Change next step 4 to `4. TRUST-COMPLETE (Decision 187): record it as a chezmoi Decision Record.`
- Remove from `## Held`: `- Sol's \`rig doctor\` findings (handler, firewall anchor range, UTM source) - until Kris is at the machine.`
- Remove from `## Held`: `- The attended NordVPN trial - until a tested restore path exists (KI-TOOL-RIG-CORE-068).`
- Change in `## Held` `- WhatsApp refresh and vega rendering - until Kris takes them up.` to `- WhatsApp refresh (KB-DOTFILES-UE-035) - until Kris takes it up.`

### Lines for the coordinator to remove from `queries.md`

- Remove `- TOWER-MOVE (Needs: attendance, Kris): quit Tower Assistant, ...` (the whole line). kb.regular.site-tower owns the move.
- Change `- Not raised: CORE-SET-COMMENTS (stays in the worksheet); FIREWALL-EXPOSURE (transient, re-check 05:18 showed only \`anchor-changed\`); RAT-UNCONFIRMED, RAT-READING (superseded by Decisions 179 and 181).` to `- Not raised: CORE-SET-COMMENTS (stays in the worksheet).`

## In Progress

Nothing is running.

Outstanding - no action requested now:

- ki.mac-studio-setup and ki.tools-burndown are on hold until Kris says resume, so the four lines wait there unread. Terra's Screen Sharing exposure beyond the tailnet stays open until then.
- Two lines this run could not send, because personal-principal is outside its write authority. The coordinator may send them:
  - To kb.regular.site-tower: tell ki.chezmoi when the move to `/Applications` is done, because TOWER-PATH waits on it.
  - To kb.regular.personal-rig: Kris's site review under Decision 179.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 08:13 BST

📨 4 lines sent · 👤 0 with you

- [sent] NORDVPN-HOLD, FW-EXPOSURE, HANDLER-FAIL · ki.mac-studio-setup · since 08:12
- [sent] HOOK-ROLLOUT · ki.tools-burndown · since 08:12
- [committed] two works' message queues
