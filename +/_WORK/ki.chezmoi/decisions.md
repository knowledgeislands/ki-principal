# Decisions

## Decision 27 (2026-10-09)

- Pointer: Kris, 9 October, "do all four gated records", KB-DOTFILES-UE-062 first. UE-062 is done and UE-065 cancelled; [KB-DOTFILES-UE-071](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-071-audit-macos-privacy-permissions.md) and [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md) carry the rest, held with the privacy and rationale audits in `state.md`.

## Decision 58 (2026-10-14)

- Pointer: burn-down standing focus, Kris on 14 October through State of play: burn the roadmap down, create no new feature records, capture only blockers, defects or items Kris asks for. Held in the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

## Decision 65 (2026-10-14)

- Pointer: RIG-CASKS, Kris on 14 October: hold `rig apply` on both Macs until a fixed release is installed. Carried as the both-Mac Rig apply hold in `state.md` until Kris lifts it.

## Decision 85 (2026-10-18T09:18:10Z)

- Pointer: HARNESS-PATHS, Kris on 18 October: migrate each host's KI harness paths to host-local state under [KI-TOOL-KI-CLI-143 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/a22214ee581b73a1f395da88f9a118ad89814bb9/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md); remove `[locals]` from the chezmoi source only after both hosts pass, and apply only on Kris's explicit approval. Sol's run is the next entry; the open part is SOURCE-LOCALS-LIVE in `queries.md`.

## Decision 97 (2026-10-19T13:29:12Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- Complete KI harness-path migration on Sol under the existing HARNESS-PATHS approval.

Terra is migrated and verified on KI v0.11.4. Both paths and active harnesses are unchanged; doctor is healthy. Its only diagnostic warning is the expected ignored legacy [locals] table.

Check Sol’s KI version, record doctor/diag and existing paths, then run ki bootstrap. Verify identical paths in host-local locals.toml, unchanged configuration and active harnesses, and healthy diagnostics. Check development switches using isolated test state.

Stop on unexpected differences. Once Sol passes, prepare removal of [locals] from the shared chezmoi source, show Kris the diff, and wait for explicit apply approval. Commit by explicit path; never push.

## Decision 101 (2026-10-19T18:56:48Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- It can do anything that's high confidence.

Read back as option a) of all five open queries: SOURCE-LOCALS-LIVE (removal intentional, no `[locals]` apply remains), MGIT-APPLY, TRIAGE-CUT, RIG-LIVE-DELIVER and CARRY-DIRECTIONS.

## Decision 104 (2026-10-19T19:53:54Z)

- Pointer: TOML-HANDLER, 19 October: Terra carried without the TOML target; the `.toml` drift finding is accepted on both Macs until tools-rig's `macos-handlers` falls back for dynamic types (sent to ki.mac-studio-setup).

## Decision 106 (2026-10-19T20:02:14Z)

- Pointer: PAPERCLIP-PLIST, 19 October: Terra's disabled `uk.me.kris.rig.paperclip.plist` stays until the Paperclip rebuild is designed.

## Decision 114 (2026-10-19T21:13:36Z)

- Pointer: SOL-FIREWALL a), Kris on 19 October: read-only pre-flight, then an attended `chezmoi apply` of the named targets on Kris's reviewed diff and `rig apply --sudo` of the firewall target at Sol, then Screen Sharing from Terra; LAN refusal left unchecked.

## Decision 116 (2026-10-19T21:26:30Z)

- Pointer: Kris on 19 October: NordVPN is used on Terra, not Sol; whether Sol keeps it is a later Rig lifecycle question.

## Decision 117 (2026-10-19T21:27:50Z)

- Pointer: Kris on 19 October: after Sol's apply, a read-only Terra check with NordVPN connected decides whether the fix lies in Rig (KI-TOOL-RIG-CORE-047) or a NordVPN setting; carried as next step 3 in `state.md`.

## Decision 118 (2026-10-19T21:44:22Z)

- Pointer: Kris on 19 October, 22:40 BST: prepare Sol for the age-encrypted SSH key delivery verified on Terra. The work covers steps 1 to 5 and waits for Kris's explicit apply approval. Keep the passphrase, Keychain behaviour and OneDrive backup, and do not push. That preparation is done, and the apply is SSH-APPLY in `queries.md`.

## Decision 119 (2026-10-19T21:48:17Z)

- Pointer: Kris on 19 October, 22:47 BST, "go ahead with recommendations". SSH-APPLY a): apply `~/.ssh/config` and `~/.ssh/kris@kris.me.uk` on Sol with scripts excluded, then run the verification ([sol-ssh-key](/Users/krisbrown/.local/state/ki/agents/chezmoi/sol-ssh-key.report.md)).

## Decision 120 (2026-10-19T21:48:17Z)

- Pointer: Kris on 19 October, 22:47 BST, the same answer. SOL-APPLY a): run the whole [sol-apply](/Users/krisbrown/.local/state/ki/agents/chezmoi/sol-apply.md) sequence at Sol's console with the undo rehearsal included and NordVPN off. This includes the S1 `chezmoi apply` of `55-ports.toml`.

## Decision 121 (2026-10-19T22:05:15Z)

- Pointer: SOL-APPLY a) carried out with Kris at Sol's console, 22:50–23:06 BST. All blocks passed. The S3 gate check was corrected from "anchor listed" to "anchor holds entries" within the same authority. Evidence goes to KI-TOOL-RIG-CORE-047 through sol-firewall-record.

## Decision 122 (2026-10-19T22:11:19Z)

- Pointer: Kris on 19 October, 23:13 BST, "go with the recommendations": GUIDE-REMOTE. Update the Remote access section now, using the blind review's qualified wording and the NordVPN caveat ([guide-remote-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/guide-remote-review.report.md)).

## Decision 123 (2026-10-19T22:11:19Z)

- Pointer: Kris on 19 October, 23:13 BST, the same answer: TERRA-NORDVPN a). Open a Rig follow-up record for detecting the bypass ([terra-nordvpn](/Users/krisbrown/.local/state/ki/agents/chezmoi/terra-nordvpn.report.md)). It is given ahead of its blind review, which is still running, so the record run waits for the review and stops if the review disagrees.

## Decision 124 (2026-10-19T22:13:47Z)

- Pointer: FW-DECLARE, Kris on 15 October: "The Rig: chezmoi thread commits the firewall declaration as conf.d/private_45-firewall.toml with profiles = [\"laptop\"], and does not apply chezmoi on sol until sol's Rig is 0.6.0 or later; then give me the terra steps." Delivered as `[firewall.screen-sharing-tailnet]` in `private_55-ports.toml` (chezmoi `dd2a062`) and applied on Sol under SOL-APPLY. Held in the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

## Decision 125 (2026-10-19T22:13:47Z)

- Pointer: FW-DECLARE-NOW, Kris on 16 October: "Rig: chezmoi commits the FW-DECLARE firewall declaration (dot_config/rig/conf.d/private_45-firewall.toml, profiles = [\"laptop\"]) as its first step; no chezmoi apply on sol until sol's Rig is 0.6.0 or later; then give me the terra steps for KI-TOOL-RIG-CORE-047." Covered by RIG-LIVE-DELIVER ([mark-tidy-1019](/Users/krisbrown/.local/state/ki/agents/chezmoi/mark-tidy-1019.report.md)); held in the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

## Decision 126 (2026-10-19T22:13:47Z)

- Pointer: SSH-SPARE-KEY, Kris on 16 October: "Both Macs are always within physical reach, so the console is the restore path: no spare key is needed, and Rig: chezmoi notes the console fallback in the chezmoi macOS workstation guide before key-only SSH applies on terra." The console note is not yet in `docs/guides/user/macos-workstation.md`; its delivery is authorised as SSH-CONSOLE under CARRY-DIRECTIONS a) ([mark-tidy-1019](/Users/krisbrown/.local/state/ki/agents/chezmoi/mark-tidy-1019.report.md)). Held in the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

## Decision 127 (2026-10-19T22:13:47Z)

- Pointer: SEAT-RECORD host binding, Kris on 15 October: "... A message to Rig: chezmoi asks it to bind home to terra and hub to sol in host data." Delivered in chezmoi `856c8f1` under CARRY-DIRECTIONS a). Held in the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

## Decision 128 (2026-10-19T22:13:47Z)

- Pointer: TOML-OPENER, Kris on 17 October: ".toml files are currently opening up in [Warp], and I don't want that. I'd rather they opened up in [Zed] ... I think it must have some kind of default opener on it." Delivered in chezmoi `faa4d3a`; applying it waits on TOML-HANDLER. Held in the [State of play decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/decisions.md).

## Decision 129 (2026-10-19T22:17:07Z)

- Pointer: Kris on 19 October, 23:13 BST, "go with the recommendations", which Kris confirmed at 23:17 covered the six parked queries too. FIRST-STEP-GATES is closed as resolved. IWORK: Keynote, Numbers and Pages stay catalogue-only and the A8 step is completed. STYLE-LINK: a read-only dead-link check runs after apply, with no harness pull. DIR-PRUNE: a managed-set state file, so only entries that left the declaration are pruned. REST-HOLD: rechecked against the delivered Dock work. GUIDE-REMOTE was already delivered (chezmoi `43d45d3`).

## Decision 130 (2026-10-19T22:19:39Z)

- Pointer: REST-HOLD a), taken under Kris's standing authority for high-confidence work ("It can do anything that's high confidence"). The hold is narrowed to UE-090 gap 1 together with UE-087. The other open UE-090 gaps go to `ki-plan` (run ue090-plan, after parked-three). CORE-042's acceptance goes to Kris, with the Dock evidence from both Macs ([rest-hold-check](/Users/krisbrown/.local/state/ki/agents/chezmoi/rest-hold-check.report.md)).

## Decision 131 (2026-10-19T22:27:44Z)

- Pointer: ACCEPT-047 a), taken under Kris's standing authority for high-confidence work ("It can do anything that's high confidence"). KI-TOOL-RIG-CORE-047 stays awaiting-review: the record still lists the NordVPN on/off checks and `rig apply --sudo` on Terra as outstanding, so acceptance waits for them ([accept-047](/Users/krisbrown/.local/state/ki/agents/chezmoi/accept-047.report.md)). Narrowing the scope instead (option b) is left to Kris.

## Decision 132 (2026-10-19T22:28:29Z)

- Pointer: MCPORTER-RESTART, Kris on 19 October, 23:30 BST: "McPorter restart: you can just do it if you need to." Sol's daemon is restarted with the existing `mcporter_restart` (run mcporter-restart).

## Decision 133 (2026-10-19T22:29:49Z)

- Pointer: STYLE-WHEN a), taken under Kris's standing authority for high-confidence work. The dead output-style link warns at render time (`warnf`, chezmoi `7ac9047`), on every apply, diff and status, rather than in a `run_after_` script that would keep `chezmoi status` permanently dirty ([parked-three](/Users/krisbrown/.local/state/ki/agents/chezmoi/parked-three.report.md)).

## Decision 134 (2026-10-19T22:32:44Z)

- Pointer: CLAUDE-APPLY a), Kris on 19 October, 23:33 BST: "yes". An agent shows the targeted diff of `~/.claude/settings.json` and `~/.claude/output-styles/ki-coordinator.md`, applies only those two if it is empty, and verifies (run claude-apply).

## Decision 135 (2026-10-19T22:37:01Z)

- Pointer: BRINGUP-CHECK a), taken under Kris's standing authority for high-confidence work after the blind review agreed with high confidence. One read-only `rig-bringup-check` for KB-DOTFILES-UE-090 gaps 2, 7 and 8, with the review's safeguards; gap 9 handed to KB-DOTFILES-UE-076 ([ue090-plan](/Users/krisbrown/.local/state/ki/agents/chezmoi/ue090-plan.report.md), [bringup-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/bringup-review.report.md)). Run bringup-fold records it.

## Decision 136 (2026-10-19T22:44:41Z)

- Pointer: READY-REST a), Kris on 19 October, 23:43 BST: "go ahead". Gap 1 is split out of KB-DOTFILES-UE-090 into its own record, held with KB-DOTFILES-UE-087, and the rest of UE-090 moves to Ready; KB-DOTFILES-UE-076 stays draft (run ready-rest).

## Decision 137 (2026-10-19T22:51:40Z)

- Pointer: READY-PREFLIGHT a), Kris on 19 October, 23:47 BST: "yes you can retry". One-run exception to the stop-on-warning preflight for the 20 existing roadmap migration warnings only; any new warning or failure still stops the run ([ready-rest-1](/Users/krisbrown/.local/state/ki/agents/chezmoi/ready-rest-1.report.md)).

## Decision 138 (2026-10-19T22:55:55Z)

- Pointer: READY-GATE a) and READY-DETAIL a), taken under Kris's standing authority for high-confidence work. The one-run exception also covers the three existing full-audit warnings (`.rumdl.toml` drift, the ADR-KB-DOTFILES-003 amendment heading, the absent `.githooks/pre-commit`); after the split, the gap-5 fallback and the size-l delivery rounds are shaped before Ready is reassessed ([ready-rest-2](/Users/krisbrown/.local/state/ki/agents/chezmoi/ready-rest-2.report.md)). Run ready-rest-3.

## Decision 139 (2026-10-19T22:55:55Z)

- Pointer: TRIAGE-ALL, Kris on 19 October via State of play: triage KB-DOTFILES-UE-098, UE-099 and UE-100 under `ki-next`, adopt and deliver high-confidence ones to Awaiting review, and bring medium, low, cancellation, merge or deletion ones as one lane query after one blind review. Run triage-lane, after ready-rest-3.

## Decision 140 (2026-10-19T23:09:17Z)

- Pointer: TRIAGE-ROOTS-GATE a), taken under Kris's standing authority for high-confidence work. The pending-apply `CLAUDEBIND-1` mismatch for KB-DOTFILES-UE-098's git-audit roots is excepted for its source-only commit; applying stays gated ([triage-lane](/Users/krisbrown/.local/state/ki/agents/chezmoi/triage-lane.report.md)). Run roots-commit. TRIAGE-SERVICE-SEQUENCE and TRIAGE-LEAK-DIAGNOSIS, both medium, go to blind review (run triage-review).

## Decision 141 (2026-10-19T23:14:56Z)

- Pointer: TRIAGE-LANE a), Kris on 20 October, 00:16 BST: "go ahead". KB-DOTFILES-UE-099 stays at triage until a released Rig supports service subject links (KI-TOOL-RIG-CORE-065), the Paperclip path fix coming forward only if Paperclip is re-enabled first. KB-DOTFILES-UE-100 is adopted for a bounded diagnostic stage, read-only on Sol and attended on Terra, with any mitigation a separate reviewed decision ([triage-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/triage-review.report.md)). Run triage-dispose.

## Decision 142 (2026-10-19T23:30:00Z)

- OVERNIGHT, Kris on 20 October, 00:30 BST: "I'm going to bed now. I want you to keep looking every 10 minutes to see if there's any new work for yourself in some way. And if there is, I want you to progress it. You can do anything on a high confidence level that you recommend. If you can get a good recommendation, you can move on to the next one, and as you do more and work, it might be that when you come back to ones that you couldn't get a good recommendation for, it might be more accurate." Taken as: check messages and runs at least every 10 minutes; launch and take every high-confidence recommendation; keep medium and low ones for Kris and revisit them as evidence grows. No push, no `chezmoi apply` and no attended step on Terra: those still need Kris. The RAT-* rationale batch stays with Kris: only Kris can confirm a personal reason. Runs ue100-sol and cmigrate.

## Decision 143 (2026-10-19T23:36:00Z)

- Pointer: CMIGRATE-PIN a), taken under OVERNIGHT with confidence high after blind review: vega's Linux `tool.mgit` pin moves from v0.16.0 to v0.18.0 in source only, with the checksum confirmed from the tag and `rig doctor` before and after; vega rendering stays held ([cmigrate](/Users/krisbrown/.local/state/ki/agents/chezmoi/cmigrate.report.md), [cpin-blind](/Users/krisbrown/.local/state/ki/agents/chezmoi/cpin-blind.report.md)). Run cpin.

## Decision 144 (2026-10-19T23:48:00Z)

- Pointer: RIGDOC-DETAIL a), taken under OVERNIGHT with confidence high after blind review: the bring-up check keeps `rig doctor`'s exit codes, and structured JSON counts are looked at in KB-DOTFILES-UE-090 round 3, because doctor's JSON groups prose findings rather than typed counts ([ue090-r1](/Users/krisbrown/.local/state/ki/agents/chezmoi/ue090-r1.report.md), [r1-review](/Users/krisbrown/.local/state/ki/agents/chezmoi/r1-review.report.md)). Round 1's gate failed on two defects (runtime declaration coverage, unbounded zero timeout); run ue090-r1b fixes them before a re-review.

## Decision 145 (2026-10-19T23:50:00Z)

- Pointer: RIG-DRIFT a), taken under OVERNIGHT with confidence high after blind review: no overnight remediation of Sol's four `rig doctor` findings. When Kris is back: review and apply the TOML handler (Warp where Zed is declared); re-apply the firewall anchor's narrowed tailnet ranges (KI-TOOL-RIG-CORE-047's range correction) as a separate attended run with its tested restore path, minding KI-TOOL-RIG-CORE-068; review UTM's source by hand, as it has no App Store receipt ([cpin](/Users/krisbrown/.local/state/ki/agents/chezmoi/cpin.report.md), [rigdrift-blind](/Users/krisbrown/.local/state/ki/agents/chezmoi/rigdrift-blind.report.md)).

## Decision 146 (2026-10-20T00:00:00Z)

- Pointer: ENUM-FLAG a), taken under OVERNIGHT with confidence high: KB-DOTFILES-UE-090's gap-5 fallback enumerates with `chezmoi managed --path-style=all --format=json` and reads each entry's `absolute` field, because `--path-style=absolute` ignores `--format=json` on chezmoi 2.73.2 ([ue090-r2](/Users/krisbrown/.local/state/ki/agents/chezmoi/ue090-r2.report.md)). Round 2 goes to review run r2-review.

## Decision 147 (2026-10-20T00:06:00Z)

- Pointer: TERRA-STEP a), taken under OVERNIGHT with confidence high: KB-DOTFILES-UE-100's Terra collection Step is reworded as Kris's attended step and ticked, the full Terra scope kept under its Outstanding concerns, following KB-DOTFILES-UE-098's pattern ([ue100-sol](/Users/krisbrown/.local/state/ki/agents/chezmoi/ue100-sol.report.md)). Sol's diagnostic stage is Awaiting review (chezmoi `f6a36e5`). ZED-WINDOW, medium, goes to blind review run zed-blind.

## Decision 148 (2026-10-20T00:09:00Z)

- Pointer: RUN-REASON a), taken under OVERNIGHT with confidence high: the bring-up check's `ki-doctor` failure reason names `ki harness install <harness-id>` then `ki bootstrap`, as the guide does, because `ki bootstrap` takes no harness argument ([ue090-r3](/Users/krisbrown/.local/state/ki/agents/chezmoi/ue090-r3.report.md)). Run ue090-r3b, then round 3's review gate (r3-review).

## Decision 149 (2026-10-20T00:33:00Z)

- Pointer: REREVIEW-SCOPE a), taken under OVERNIGHT with confidence high: round 3 of KB-DOTFILES-UE-090 gets a focused read-only re-review of chezmoi `f3021f2` against r3-review3's guard defect, because the earlier reviews already passed the rest; on a pass the record moves to Awaiting review.
