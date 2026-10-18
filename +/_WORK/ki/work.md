---
id: ki
level: territory
title: 'KI > SoP'
theme: null
worker: agent
supervisor: owner
state: on-hold
hold:
  reason: paused
  release: after the work migration lands
since: 2026-10-18T03:30:38Z
received: null
beat: null
mark: 2026-10-15T15:14:39Z
created_at: 2026-10-06T21:07:00Z
---

# ki

## Next steps

- **Status:** rest, wrapped up for ways of working's updates (WRAP-UP, 2026-10-18 02:19 BST). Running: nothing. 2026-10-18: obs-fold folded Command centre into the Observatory Project; dispatch-handover routed Personal's Acquire > Dispatch handover to knowledge acquisition; first-steps acted on ways of working's READY. Kris has resumed the Observatory and tools burndown; knowledge acquisition's resume line was given and is recommended next. No open queries; Kris dropped MS3-SPLIT (MS3-DROPPED, decisions log).
- **Resume:** `Resume Master: state-of-play under current ki-pmo and ki-delegation since 2026-10-15T15:14:39Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.`
- **Next steps, in order:**
  0. PILOT-SEED at a session with the terra checkout (decisions log, 18 October).
  1. Once ways of working's updates land, re-bootstrap on them. Then confirm knowledge acquisition has restarted; then the two Rig threads in parallel, then Host network (fifth, HOST-NETWORK-THREAD).
  2. On Kris's return: REBASE-OWNER and MGIT-017-CLASH (bug-census report); check whether SEAT-PUSH, LABEL-FORM and PROJECT-OVERLAP (seat-change and tools-project reports) were answered before 17 October, and delete those reports if so.
  3. THREADS-ORPHANS remainder: desk-kit reports (frontmatter now fixed) belong to Rig: mac-studio-setup (setup-note) and KI > mics / webcams (cam-check, webcam-compare).
  4. STASH-DROP at a session with the terra checkout.
  5. At the next mark, THREAD-TIDY the thread folder.
  - Rule from Kris, 2026-10-15 22:50 BST: the thread dispatches changes to coordination threads and does not ask whether to. GO-AHEAD, 2026-10-17: "you've got permission to get on with anything."
- **Live threads (2026-10-16):** KI > SoP; KI > Fnd > tools burndown; KI > Model > ways of working; KI > Model > knowledge acquisition; KI > Rig > mac studio setup; KI > mics / webcams; Acquire > intake (sol); Chezmoi > misc (sol), carrying Rig: chezmoi.

**Messages from Master: state-of-play** - the receiving thread acts on each line, then removes it.

- 2026-10-16 · THREADS-ORPHANS · KI Model: ways-of-working, on Kris's MSG-ORPHANS of 16 October (option a)): the empty `+/_THREADS/mac-studio-bootstrap/` is removed. Still to do: `+/_THREADS/desk-kit/` has no checkpoint; its untracked reports (`setup-note.report.md`, headed Rig › Mac Studio setup, and `cam-check` and `webcam-compare`, apparently KI > mics / webcams) need their owning thread found and THREADS-CLEAR passed on; Rig: chezmoi gets its THREADS-CLEAR line when its session rests.

1. Follow the pick-up block's next steps in order.
2. Commit this thread's checkpoint, thread folder and `decisions.md` through a private index by explicit path at each mark, pull with rebase and push fast-forward when the stack is only this thread's.
3. Work the dated queue; keep the burn-down moving through the Project threads, then offer the ki release and the specification review.
4. Later: Paperclip rebuild after the ways-of-working model settles; rebuild vega.

## Messages

- MIGRATED - this file was `+/_CHECKPOINTS/_state-of-play.md` until the work migration of 2026-10-18. At your next mark, cut it to next steps, Messages and the tags of parked queries, each linked to its report; move anything else to its durable home, then remove this line.

## Parked

Stored 2026-10-15 for the move to sol:

- **HOLD-MODEL (Kris, 15 October; pass to KI Model: ways-of-working when it restarts):** rename drain to **hold**: a hold is a mark plus stopping all work, draining by not restarting anything, used for a move or for closing a thread for a period, and issuable across a whole territory. Every banner type (today REST, BUSY, DONE, plus the interim DRAINED frame) also updates a **pick-up block as the first thing in the checkpoint**: how the thread is resumed, its status (a hold sets status `hold`), and its next steps when back in use, with questions kept below. A mark shows in the banner and updates the pick-up block's mark heading. On a hold or reinstatement, the state-of-play thread says which threads should restart. A hold never says where (which host) the work comes back up; that is not part of the information. Kris's words are in `decisions.md`.
- **RESTART-SET (Kris, 15 October):** the pick-up state is the combination of the banner type and the thread type (conversational, coordination, or state-of-play as the coordination of coordinations), each with its own instructions; this thread works that out first on restart, before handing HOLD-MODEL to KI Model: ways-of-working. Threads to reinstate: Master: state-of-play, KI Model: ways-of-working, Rig: chezmoi and Acquire: acquire-intake, with Rig: mac-studio-bootstrap carrying on as it is. Rig: chezmoi and Acquire: acquire-intake sit outside this thread's territory and are included this time only. Every other thread stays held.
- **HOLD-VERBS (Kris, 15 October):** drain and resume are the activities and hold is the state: a thread drains to reach a hold and resumes to leave it. Pass this to KI Model: ways-of-working with HOLD-MODEL.
- **HOLD-BANNER (Kris, 15 October):** the drain report becomes a **hold report**: block letters HOLD, top border `hold report`, captions threads drained / queries parked / fully archived, closing with "To bring this thread back and continue the work, paste this:" and the resume line. Pass to KI Model: ways-of-working with HOLD-MODEL.
- **HOST-ROLES (Kris, 15 October):** the home role is terra, the laptop; the hub role is sol, the Mac Studio. This binds the roles in ADR-KI-PRINCIPAL-007's seats (as amended by Kris on 17 October: home: humans-not-robots; hub: valle-armonia, sacred-inquiry, techmedix, equal-remedy; both, tipped to the hub: knowledge-islands, personal, legal). Recorded in Host network, Known Lands, ADR-KI-PRINCIPAL-007 and Known World; SEAT-HOSTS with Rig: chezmoi. On restart: record the binding where the decision's Known Lands table can point to it, and hand the per-host seat binding to Rig: chezmoi.
- **SOL-FIRST-CHURN (Kris, 15 October; first work on restart on sol):** analyse thread and session-based digests and the churn they cause across repositories, and the older material left lying around. Kris raised this in another thread and possibly KI Model: ways-of-working, so find that first and fold it in. Rule from Kris: temporary files live under the `tmp` folder. Dispatch the analysis to a background run; no new feature records unless Kris asks.
- **SOL-MOVE (Kris, 15 October):** Kris moves working to sol next. Every thread in ki-principal and acquire drains, commits and pushes; Kris then makes a blank baseline commit across all repositories; tidy-ups follow on sol. Resume this thread on sol from this checkpoint; machine-local `~/.local/state/ki/agents/state-of-play/` does not travel, `decisions.md` in the thread folder does.
- **FW-TERRA-OFF (answered 15 October; Kris's words in `decisions.md`: no, Kris stayed in to get the firewalls and approach right that day):** turn off Screen Sharing and Remote Login on terra at the Mac until [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) is live there; sol unchanged (the fw-exposure report, now in Git history). Both currently listen on every network and accept passwords.
- **FW-SSH-KEYONLY (answered 15 October; Kris's words in `decisions.md`; the plan is drafted in the chezmoi macOS workstation guide):** a run drafts a key-only SSH rollout plan in the chezmoi macOS workstation guide's Remote access section (key inventory in both directions, held session, second-machine test, restore steps), which Kris carries out attended. Kris agrees SSH stays open as the deliberate way back in, made key-only; keys are not yet proven in both directions.
- **LIVE-MAN-SWITCH (idea, Kris, 15 October):** a reverse dead man's switch. Each host periodically pulls a control repository and re-applies its declared state, so a host that has lost inbound access heals itself once it has outbound connectivity; firewall and SSH changes must never break outbound traffic. Check [KI-TOOL-RIG-CORE-046](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-046-remote-access-and-continuity.md) as the likely home before any capture; no record yet. Gate the FW-SSH-KEYONLY and firewall rollouts on it as a design input.
- **Firewall steps:** waiting on Rig: chezmoi's FW-DECLARE commit; then Kris gets the terra steps.

Parked at the territory hold, 2026-10-15, each with its recommended option:

- **FW-DECLARE-NOW:** Rig: chezmoi drained without committing the FW-DECLARE firewall declaration (`dot_config/rig/conf.d/private_45-firewall.toml`, `profiles = ["laptop"]`); it is still absent from the chezmoi source. Recommended: Rig: chezmoi commits it as the first step on reinstatement, with no chezmoi apply on sol until its Rig is 0.6.0 or later, then Kris gets the terra steps.
- **SSH-SPARE-KEY:** add a second ed25519 key by hand to both Macs' `authorized_keys` before any chezmoi apply that turns SSH key-only; chezmoi on terra was 9 commits behind and its next apply turns key-only on. Recommended: yes, with its fingerprint recorded in the guide's key table ([ssh-keyonly report (deleted)](https://github.com/knowledgeislands/ki-principal/blob/2e9fd5d5f2d7831faf44d66e7cdae1f74397a158/+/_THREADS/state-of-play/ssh-keyonly.report.md)). The territory hold fast-forwarded terra's chezmoi source, so a plain `chezmoi apply` on terra now turns key-only on.
- **ESTATE-MAP-OBSERVATORY:** Kris asked whether the Estate Map is captured as critical for the Observatory; it is not (only trades-revamp mentions it). Recommended: add it as an idea in the [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) (formerly Command centre) Project's Notes.
- **STASH-DROP:** keep `stash@{0}` and `refs/rebase-repair/autostash-f091d468` in ki-principal on terra until Rig: mac-studio-bootstrap commits `+/_THREADS/mac-studio-bootstrap/chezmoi-fix.report.md`, then drop the stash entry and delete the ref. At the territory hold the stash list was already empty; the ref remains.

Waiting on Kris: FW-DECLARE-NOW, SSH-SPARE-KEY, ESTATE-MAP-OBSERVATORY and STASH-DROP, parked above.

Waiting on Rig:

- **Rig: chezmoi:** FW-DECLARE commit, then Kris runs terra steps for [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) (plan in the fw-rollout report, now in Git history).

With other threads, no Kris action now:

- **SYNC-GUARD:** answered; KI Model: ways-of-working folds "level before resume and at every mark" into KI-HARNESS-GOV-189.
- **CHANNEL-TELEMETRY:** answered; the findings are dispatched as ideas and now sit in the [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) (formerly Command centre), [Host network](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/host-network.md) and [AI observability](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ai-observability.md) Project notes.
- **CLI127-LINKS:** answered; outstanding note for [KI-TOOL-KI-CLI-127](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-127-agent-status-live-threads.md)'s next planning pass: point both of its KI-TOOL-KI-CLI-124 links at the pruned GitHub link, [KI-TOOL-KI-CLI-124 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/9c4c0c0/docs/roadmap/KI-TOOL-KI-CLI-124-agent-run-close.md), with no separate commit now.
- **GATE-REMAIN:** sent 2026-10-15; the remaining `ki repo audit` failures are their owners' to fix. Rig: mac-studio-bootstrap (RECORD-2, BOUNDARY-1) through its checkpoint message block and `~/.local/state/ki/agents/mac-studio-bootstrap/inbox.md`; Observatory: product (LIFECYCLE-1) through a new message block in its checkpoint. The two tools-burndown MD041 reports no longer exist, so no message went.

Settled on 15 October (foundations-apply; fw-route):

- **FOUNDATIONS-HOME:** the [Known World](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Emerging Concepts/Known World.md>) Emerging Concepts note, held by a widened Outcome in [Island model and Tending](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/island-model-and-tending.md), with each other Project's part in its Notes.
- **FOUNDATIONS-NOTE:** carried out with FOUNDATIONS-HOME in the same [Known World](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Emerging Concepts/Known World.md>) note.
- **SEAT-RECORD:** [ADR-KI-PRINCIPAL-007](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Decisions/ADR-KI-PRINCIPAL-007-territory-seats-on-hosts.md) and the Seat column in [Known Lands](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Admin/Governance/Known Lands.md>); SEAT-BIND sent to the [Rig: chezmoi checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) and its inbox.
- **PAPERCLIP-SEAT, PAPERCLIP-CHEZMOI, PAPERCLIP-BRANCHES:** Notes of [Paperclip capture and rebuild](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/paperclip-capture-and-rebuild.md); PAPERCLIP-OFF sent to the Rig: chezmoi checkpoint and its inbox.
- **INCEPTION-PILOT:** a message in the [knowledge-acquisition checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.knowledge-acquisition/work.md).
- **ROOTING-OWNER, TERRITORY-RULE:** the ROOTING-MODEL direction and the adopted territory rule at the top of the [ways-of-working checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md); ROOTING-OWNER's concept-note target also in the knowledge-acquisition checkpoint.
- **FW-DECLARE:** sent to the [Rig: chezmoi checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/work.md) and its inbox: commit `dot_config/rig/conf.d/private_45-firewall.toml` with `profiles = ["laptop"]`, no chezmoi apply on sol before Rig 0.6.0, then Kris runs the terra steps.
- **FW-ADR:** applied by the acceptance run on Kris's pass: it accepts [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) and marks both [ADR-KI-TOOL-RIG-009](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-009-system-domain-resources-under-an-attended-grant.md) and [ADR-KI-TOOL-RIG-010](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/decisions/ADR-KI-TOOL-RIG-010-linux-firewall-through-a-rig-owned-nftables-table.md) accepted.
- **AREAS-PATTERN:** adopted; sent to the [ways-of-working checkpoint](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/work.md) and its inbox, Ways of working holding the rule.
- **RIG-PROJECTS-LIST:** no change; the [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) Initiative note keeps no Projects list, the `initiative` field being the link.

Dated queue:

- 2026-10-16: review the [KI-PRINCIPAL-MOD-008](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-008-whole-philosophy-coherence-review.md) hold; release it if most of the roadmap is cleared, otherwise move the review on one week.
- 2026-10-21: the trades and Delta follow-up ([delta-evaluation](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/delta-evaluation.md)). HOLD-1 warnings begin 2026-10-22.
- About 2026-10-21: review the logged report-shape tweaks.
- 2026-11-12: review the holds [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) and [KB-DOTFILES-UE-084](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-084-render-zshenv-on-vega.md).
- 2026-11-16: vega and agent-host holds [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) and [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md); the burn-down cancelled and pruned [KI-HARNESS-GOV-179 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/731580841ce5/docs/roadmap/KI-HARNESS-GOV-179-diagram-html-commit-opt-in.md) and [KI-TOOL-RIG-CORE-049 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/06da52aec5de/docs/roadmap/KI-TOOL-RIG-CORE-049-shared-agentic-rig-role.md). The 2027-01-04 holds, [KI-SPEC-KIN-003 (pruned)](https://github.com/knowledgeislands/ki-specifications/blob/9d56444dddf0/docs/roadmap/KI-SPEC-KIN-003-portable-live-artifact-contract.md) and [KI-TOOL-RIG-CORE-046 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/06da52aec5de/docs/roadmap/KI-TOOL-RIG-CORE-046-remote-access-and-continuity.md), went the same way.

Master follow-ups (no Kris action): Cowork clean-up of old knowledge-base aliases in `~/workspaces/claude-desktop/` at Kris's next Cowork session; retired `kit-mcp-gmail` entries in legal-principal `.claude/settings.json` and chezmoi `.chezmoiignore`; Paperclip decision cards with the rebuild.

- Parked 2026-10-12: the Rig full-screen mode idea; other parked items are in `thread-history.md` section 5.
- Parked 2026-10-15: THREADS-CHECKINS: Kris's question on how threads are used and the excessive number of check-ins; Kris picks it up with this thread.
