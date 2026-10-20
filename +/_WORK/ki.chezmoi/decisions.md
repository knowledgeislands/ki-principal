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

## Decision 150 (2026-10-20T00:48:00Z)

- Pointer: 093-PREFLIGHT a), taken under OVERNIGHT with confidence high (reviewed: the blind review pre093-blind chose a) independently): KB-DOTFILES-UE-093's read-only dependency preflight in the Emerge test is approved as Ready and built as a source-only run, because repairing today's checkout does not stop a future incomplete checkout failing without its setup remedy.

## Decision 151 (2026-10-20T00:55:00Z)

- Pointer: UE-076-STEPS, taken under OVERNIGHT with confidence high: a small follow-up run moves the non-task lines out of KB-DOTFILES-UE-076's `## Steps`, because the ITEM-3 failure from chezmoi `1999865` fails the repository gate for every run.

## Decision 152 (2026-10-20T00:55:00Z)

- Pointer: THEME-REGISTRY a), taken under OVERNIGHT with confidence high: the four `initiative` to `theme: rig` renames (KB-DOTFILES-UE-027, -082, -086, -087) land with the two registry legacy warnings added to the permitted baseline, because the warnings describe ki-principal's own registry, which the renames only expose; the registry migration stays with ki-principal.

## Decision 153 (2026-10-20T01:30:00Z)

- Pointer: Kris answered the RAT batch for [KB-DOTFILES-UE-027](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-027-honest-rationales-per-tool.md) "all as agreed unless below": a) confirms the proposed reasons for Actions, Alfred, ChatGPT (packaging watch), GarageBand, Hazel, OneDrive and Path Finder. RAT-DISPLAYLINK and RAT-OUTLOOK are read as a), the recommended option, despite the review's c); Kris can correct that reading.

## Decision 154 (2026-10-20T01:30:00Z)

- Pointer: RAT-SPARK b), Kris verbatim: "I keep this because I'd like to use it more but haven't tried it a lot recently." Read as the reason for `tool.spark`, Shadowlab's Spark utility, since Spark Desktop is already the default mail app; the worksheet's naming of Spark Mail is corrected.

## Decision 155 (2026-10-20T01:30:00Z)

- Pointer: DELIVERED-STATUS, Kris: "accept them". [KB-DOTFILES-UE-082 (pruned)](https://github.com/krisb/dotfiles/blob/7cb547a86133325168183bc9c5962fa9550671a5/docs/roadmap/KB-DOTFILES-UE-082-tolerate-missing-template-tools.md), [KB-DOTFILES-UE-088 (pruned)](https://github.com/krisb/dotfiles/blob/7cb547a86133325168183bc9c5962fa9550671a5/docs/roadmap/KB-DOTFILES-UE-088-ssh-alias-for-sol.md) and [KB-DOTFILES-UE-092 (pruned)](https://github.com/krisb/dotfiles/blob/7cb547a86133325168183bc9c5962fa9550671a5/docs/roadmap/KB-DOTFILES-UE-092-restore-local-skill-projection.md) are accepted and close through `ki-accept`.

## Decision 156 (2026-10-20T01:30:00Z)

- Pointer: [KB-DOTFILES-UE-077 (pruned)](https://github.com/krisb/dotfiles/blob/4fe2203cbc4046c697b543ec9e2c32a77f760ad1/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md): READY-077 a), the plan is Ready as written; CACHE-DISPOSAL, Kris: "done on both machines", the cache expiry step is complete on Terra and Sol; RIG-KEYCHAIN a), `security delete-generic-password -s ki-op-service-account-rig` joins Kris's attended step on both Macs, an absent entry counting as clean.

## Decision 157 (2026-10-20T01:30:00Z)

- Pointer: [KB-DOTFILES-UE-076](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-076-always-run-latest-source.md), Kris: "all as recommended": SOURCE-CHECK-HOME a), a step at the start of the daily `rig-update`; SOURCE-REFRESH b), the coordinator's and review's recommendation, fetch and report only, every pull attended; SOURCE-REFUSAL a), upgrade anyway and report findings.

## Decision 158 (2026-10-20T01:30:00Z)

- Pointer: VEGA-XDG a), as recommended: the agent-host Project adds four unset-only XDG defaults to the harness's `env.sh` in ki-techne-harness, and [KB-DOTFILES-UE-084 (pruned)](https://github.com/krisb/dotfiles/blob/3f7c9bd867a0b447756826e2a4dde9feebc85d12/docs/roadmap/KB-DOTFILES-UE-084-render-zshenv-on-vega.md) is cancelled with that resolution.

## Decision 159 (2026-10-20T01:41:00Z)

- Pointer: ZED-WINDOW, Kris: "drop". No further Sol window; [KB-DOTFILES-UE-100](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-100-mcporter-daemon-child-leak.md)'s Sol findings are reviewed as they stand and a mitigation is decided after Terra's collection.

## Decision 160 (2026-10-20T01:41:00Z)

- Pointer: AGE-DOC, Kris: "this is correct but I think its the wrong vault". The age recovery document is right, but the setup guide's Personal vault is probably not where it lives. [KB-DOTFILES-UE-077 (pruned)](https://github.com/krisb/dotfiles/blob/4fe2203cbc4046c697b543ec9e2c32a77f760ad1/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md)'s guide fix waits on Kris naming the vault; its other fixes proceed.

## Decision 161 (2026-10-20T01:48:00Z)

- Pointer: AGE-DOC b), Kris: "I've moved it to `Persoal - Kris` with UUID `5lyahyqnrnep7lak65dikkdut4`". Read as the vault "Personal - Kris"; the age recovery document stays out of Automation, and [KB-DOTFILES-UE-077 (pruned)](https://github.com/krisb/dotfiles/blob/4fe2203cbc4046c697b543ec9e2c32a77f760ad1/docs/roadmap/KB-DOTFILES-UE-077-reorganise-1password-vaults-safely.md)'s setup guide names that vault. Runs rat-write, accept-delivered, build-077, fold-076 and cancel-084 are queued in sequence to process Decisions 153 to 161.

## Decision 162 (2026-10-20T02:14:00Z)

- Pointer: Kris (03:14 BST, spoken): take stock now, not as roadmap records. Read back as: (1) find every worktree or unmerged branch across the Knowledge Islands repositories and fold finished work into main (survey first, run wt-survey; folds only on the survey's evidence); (2) migrate ki-design off Husky to the committed `.githooks` gate now (run design-hooks); (3) standardise hooks to lint, format and commit-message gates only, no test suites, set once per repository shape and maintained by audit and conform; the model goes to Kris for a sanity check before any standard or hook changes (run hooks-model, note `design/git-hooks-model.md`).

## Decision 163 (2026-10-20T02:16:00Z)

- Pointer: Kris (03:16 BST): "We don't need to assess if Husky was the right call or not. I'm happy that it was now. We just need to focus on how we get them all aligned and how we roll this out." Committed `.githooks` is settled; hooks-model drops its mechanism assessment and covers alignment and rollout only (sent to the run's inbox).

## Decision 164 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). AUDIT-LINT a): "Yes, I agree with the recommendation." One focused `--staged` shape audit per hook, never the full audit.

## Decision 165 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). EMPTY-EXIT a): "I agree with the recommendation for empty exit." The early exit sits before the missing-tool refusal; HOOK-4 amended.

## Decision 166 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). HARNESS-LINES a): "should move to a manual gate and CI. Again, it's not a hook thing." The harness `tsc`, `ki-skills` audit and diagram-receipt check leave the hook.

## Decision 167 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). STRICTNESS a) for now: "it just needs to contain the recipe's required lines and a check for things that shouldn't be in there, and we can expand on that", with a stated concern that this does not support mechanical conform, and a possible extension point inside the hook. Read back as: provisional; the hooks model is revised to show how conform writes each shape's hook mechanically, and comes back to Kris.

## Decision 168 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). CHEZMOI-HOOK, none of the options: "it should be nothing for a dot files repo." The dotfiles shape has no hook; tooling does not stand in the way of a dotfiles repo applying itself. Read back as: chezmoi gets no `.githooks`, `ki-repo-dotfiles-chezmoi` GIT-2 is changed to require none, and the manual gate in AGENTS.md stays.

## Decision 169 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). OUT-OF-SCOPE a), as a standing rule: "If a repository does not have a .ki.toml file, it's outside of our standards, and therefore we leave it out. That's always the case."

## Decision 170 (2026-10-20T02:47:00Z)

- Pointer: Kris (03:47 BST, spoken; "Audit Lynn" read as AUDIT-LINT, "shame wire" as chezmoi). MAIN-PUSH: "I will do a push now." Kris pushes the three mains himself; no push rule given.

## Decision 171 (2026-10-20T03:36:00Z)

- Pointer: Kris (04:36 BST): "STRICTNESS-CONFORM - lets make it happen then, are we rolling it out?" Read back as: STRICTNESS-CONFORM d), the coordinator's recommendation: a canonical hook per shape, audited exact and written mechanically, with no extension point; tools-rig's `assemble-rig --check` becomes a `ki-repo-tools` criterion in the focused staged audit. Roll out now: run roll-standards (note section 6.1), then the repository hooks (6.2) and the tools-ki composer. MSG-UNIFY stays open; the rollout keeps the current message split.

## Decision 172 (2026-10-20T03:39:00Z)

- Pointer: Kris: "ah, interesting I guess, I'm fine with either then". Read back as: MSG-UNIFY b), the recommendation and the current `ki-git` standard: Commitlint where a package exists, `ki git check-message` only where none does. The rollout already uses it.

## Decision 173 (2026-10-20T03:47:00Z)

- Pointer: Kris (04:47 BST, spoken; "the big" read as Rig, "UV-082" as UE-082). RAT-UNCONFIRMED and RAT-READING: "I'll just go through and check them in [Rig] and come back with any comments. I can do that shortly." Both stay open with Kris; no action.

## Decision 174 (2026-10-20T03:47:00Z)

- Pointer: Kris (04:47 BST, spoken; "the big" read as Rig, "UV-082" as UE-082). RESOLUTION-084 a): "go with your recommendation." `rejected` stands.

## Decision 175 (2026-10-20T03:47:00Z)

- Pointer: Kris (04:47 BST, spoken; "the big" read as Rig, "UV-082" as UE-082). RAT-SPARK-VOICE, neither option: "I think it can just say alternative email client as it's reasoning... nothing contentious." Spark's rationale becomes "Alternative email client." (run b2-chezmoi).

## Decision 176 (2026-10-20T03:47:00Z)

- Pointer: Kris (04:47 BST, spoken; "the big" read as Rig, "UV-082" as UE-082). 077-REVIEW-PATH a): "I've run that command on both machines." The Keychain step is ticked and KB-DOTFILES-UE-077 moves to Awaiting review (run b2-chezmoi).

## Decision 177 (2026-10-20T03:47:00Z)

- Pointer: Kris (04:47 BST, spoken; "the big" read as Rig, "UV-082" as UE-082). PLAN-076 c): "Plan-076 is fine." Pending review is deferred to one follow-up triage record and KB-DOTFILES-UE-076 moves to Ready (run b2-chezmoi).

## Decision 178 (2026-10-20T03:47:00Z)

- Pointer: Kris (04:47 BST, spoken; "the big" read as Rig, "UV-082" as UE-082). UE-082-FOLLOWUPS a): "whatever you think, honestly, I'm not sure." One triage record for a persistent absent-command finding; path stability dropped (run b2-chezmoi).

## Decision 179 (2026-10-20T03:55:00Z)

- Pointer: Kris (04:55 BST, spoken; "the big" read as Rig). On the Rig site's tool table: drop "why it is here" wording; each tool shows what it is for, factually ("Zoom: video meetings where Zoom is the required platform"; ack: what ack is, not its Homebrew package); a reason is not required, and any particular comment goes as subtext underneath, like "needs uv"; show each tool's kind (command line or application, "seems to have been lost") and install vector. "I don't think we should indicate ... install vector ... app type" is read as "I do think", from the surrounding sentences; flagged to Kris. "Just go at this and try and improve it, and then I'll come back and have another look." Supersedes RAT-UNCONFIRMED and RAT-READING. Runs rig-purpose (chezmoi declarations) and purpose-render (apps-rig.midnight.ninja).

## Decision 180 (2026-10-20T03:55:00Z)

- Pointer: Kris (04:55 BST): "a lot of items in the roadmap ... most of them done. Can we get them approved if not?" Read back as: prepare the chezmoi roadmap for one approval pass (run accept-prep, read-only), then bring an acceptance batch and a clear-out batch.

## Decision 181 (2026-10-20T04:02:00Z)

- Pointer: Kris (05:02 BST, spoken; "the big" read as Rig): "I don't think we need what is for and why it is here. We can just deal with it as a single description: the bold text can be what it is"; ack's description says what ack is about, and "there's nothing else to talk about really, it's just an obvious choice"; the table includes the kind (command line or GUI application) and how it is installed. Confirms the Decision 179 read-back of kind and install vector. Sent to runs rig-purpose and purpose-render. Kris did not recognise Shadowlab's Spark ("I think it must have been a mistake from recognizing Spark Desktop. Can you check the history there"): run spark-history.

## Decision 182 (2026-10-20T04:05:00Z)

- Pointer: Kris (05:05 BST): "Can you also fix in the chezmoi drift again?" Read back as: classify `chezmoi status` drift on sol, bring in-place target changes back into the source, and prepare the apply for Kris's review; no apply without his explicit request (run drift-fix).

## Decision 183 (2026-10-20T04:35:00Z)

- Pointer: route receipt from ki.ways-of-working apply-sweep (05:34 BST), CONFIG-UNDER-CONTROL under SWEEP-CONVERT a), quoting Kris (18 October): "I think we do need to have a fairly regular thing where we look to see if we should be bringing more configuration under control."
- Read back as: adopt a recurring read-only Activity in the chezmoi source scanning each Mac's unmanaged application and tool configuration, starting with `~/.config/mgit/`, reporting for Kris to choose; KI-TOOL-RIG-CORE-064 keeps Rig-managed configuration. Run config-control extends KB-DOTFILES-HK-001 or adds a template.

## Decision 186 (2026-10-20T22:39:00Z)

- Pointer: Kris (23:39 BST): "TRUST - remove all 102 and then we can keep an eye on it". TRUST c): revoke every undeclared Claude Desktop trust grant so it trusts exactly the 53 declared folders, keeping a rollback inventory; "keep an eye on it" read as one added step in the recurring unmanaged-configuration scan (KB-DOTFILES-HK-001) listing new undeclared grants (run trust-revoke).

## Decision 187 (2026-10-20T22:40:00Z)

- Pointer: Kris (23:40 BST, spoken; "mid site" read as Rig site, "Hannis" as harness, "fault of targets" as the four APPLY targets, already applied under Decision 185). "Yes" to checking the dropped folders (run resources-check). ROADMAP-BATCH a) (run roadmap-batch). RIG-SITE a): remove the rationale filter now (run site-filter); the `comment` field and exported kind and install route routed to ki.mac-studio-setup, which owns Rig. SPARK-REMOVE a), "make sure that we can get it removed properly" (run spark-retire). HARNESS-CI-TSC a) and HOOKS-FOLLOWUPS a) (run hooks-tools; GOV225-CLOSE already handled by ki.ways-of-working).
- Pointer: Kris (23:40 BST) on trust: the declaration must be complete so no client ever needs to ask for a folder; an app asking or adding one is a defect. Supports Decision 186.

## Decision 188 (2026-10-20T22:46:00Z)

- Pointer: Kris (23:46 BST) on the trusted-folder declaration: include all 8 folders under `~/workspaces/claude-desktop/Projects` ("Kit Legal" is gone in favour of "Legal"); hnr-backend, hnr-frontend and hnr-shared are needed, "in fact any git repo under `~/workspaces` is allowable, and we can consider the folders too, e.g. `~/workspaces/knowledge-islands`"; `~/.claude` "makes sense too". Asked what the five Resources folders are. Sent to run resources-check to shape the fix.

## Decision 189 (2026-10-20T22:49:00Z)

- Pointer: Kris (23:49 BST) on resources-check: "~/workspaces/valle-armonia/va-principal/Resources shouldn't be needed if ~/workspaces/valle-armonia/va-principal is in the list right?" Read as RESOURCE-GRANTS b): declare parent roots only, no Resources child grants (HNR's Resources is covered by hnr-shared). Decision 188 read as TRUST-SOURCE a) (trust intent independent of VS Code workspaces), HNR-REGISTRY b) ("any git repo under ~/workspaces is allowable": no KI adoption needed) and KIT-LEGAL a) (Legal replaces Kit Legal). Run trust-declare.

## Decision 190 (2026-10-20T23:12:00Z)

- Pointer: Kris (00:12 BST): the request to clear the `tools-*`, `mcp-*` and `apps-*` roadmaps overnight "was in the wrong window!!! ... stop please on the above". Withdrawn: run overnight-survey stopped, OVERNIGHT-STOP, OVERNIGHT-PUSH and OVERNIGHT-PUBLISH withdrawn; nothing was written by the survey.
