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

## Decision 187 (2026-10-20T22:40:00Z)

- Pointer: Kris (23:40 BST), SPARK-REMOVE a), "make sure that we can get it removed properly": Shadowlab Spark is removed from sol (chezmoi `955faf5`, Decisions struck at the 01:41 mark); terra follows the spark-retire handoff with Kris at the machine.
- Pointer: Kris (23:40 BST) on trust: the declaration must be complete so no client ever needs to ask for a folder; an app asking or adding one is a defect. Carried in tools-ki `9252669a` and chezmoi `13458343`; no Decision Record yet (homeless: TRUST-COMPLETE).

## Decision 196 (2026-10-22T00:02:00Z)

- Pointer: Kris (01:02 BST), TOWER-CUTOVER, "I'm here": Kris is at terra for the Tower Assistant cutover. Read back as: run tower-cutover does the scriptable install under the Tower Assistant guide and stops at the Accessibility grant with the exact clicks for Kris; removing Tower Save Nudge.app and the after `rig doctor` follow in a second run once access is granted. No `chezmoi apply` without Kris's review of the diff.

## Decision 197 (2026-10-22T00:20:00Z)

- Pointer: Kris (01:20 BST) on Tower Assistant: show it in the Dock as well as the menu bar, with a setting to leave the Dock; give it an icon; install it in `/Applications`; redesign it through Claude Design; dispatch all of it to the Tower thread. Read back as: TOWER-APP-SHELL sent to kb.regular.site-tower (personal-principal `ff0877f`, pushed); ki.chezmoi keeps the cutover on terra and, when the install path changes, the Rig artefact and `~/bin/scheduled/rig-tower-save-nudge` paths.

## Decision 198 (2026-10-22T00:25:00Z)

- Pointer: Kris (01:25 BST): find and delete the old Tower Save Nudge app and its remnants on terra (he trashed the bundle himself), and ask the Tower thread for an in-app permissions setup panel. Read back as: run nudge-remove deletes only the old bundle's remnants, leaves Tower Assistant and the `tower-save-nudge` job names alone, and runs `rig doctor` after; TOWER-APP-PERMS sent to kb.regular.site-tower (personal-principal `47364af`, pushed).

## Decision 199 (2026-10-22T00:45:00Z)

- Pointer: Kris (01:45 BST): "<https://github.com/stablyai/orca> I want to evaluate this. Can you add it to the rig and install it so we can see what it looks like?" Read back as: run orca-install vets Orca, declares it in Rig as an evaluation tool, commits the source and stops at the `chezmoi diff` gate with a scoped apply and install for Kris to approve; no general `rig apply` while RIG-CASKS holds.

## Decision 200 (2026-10-22T00:56:00Z)

- Pointer: Kris (01:56 BST), STARSHIP-REVIEW: "For Starship, can we just try it in one of the windows?" Read back as: run starship-trial builds a disposable, SHA-256-verified Starship kit under `~/.local/state/ki/trials/starship/` that Kris sources in one window, with no install, Rig intent, shell startup or chezmoi change, and a teardown script. STARSHIP-REVIEW stays open until he has tried it.

## Decision 201 (2026-10-22T00:59:00Z)

- Pointer: Kris (01:59 BST), OLD-CERT: "I agree with the recommendation, which is to get rid of it. If you can delete it now, you can do that ... we don't need it anymore." Read back as: OLD-CERT a), run cert-delete removes the "Tower Save Nudge Local Signing" identity (SHA-1 2D369DA384B64CC4B8169B22D3FFA1C150836A38) and its trust setting from terra's login keychain with no backup; where a step needs Kris's password, it hands the exact commands back.
- Pointer: Kris (01:59 BST), TOWER-STEPS: Tower Assistant's Screen & System Audio Recording grant, alongside Accessibility, "has been added ... by hand". Read back as: the grants are done; run tower-finish verifies them.
- Pointer: messages.md TOWER-APP-PATH (kb.regular.site-tower, apps-tower.midnight.ninja `85ab55a`): Tower Assistant now installs to `/Applications`, releasing the hold under the 22 October Tower Assistant decision. Read back as: run tower-finish moves the Rig `tool.tower-assistant` artefact and `~/bin/scheduled/rig-tower-save-nudge` to `/Applications` with the `~/Applications` fallback, declares Tower Assistant in `dock.workstation` as Kris pinned it, and stops at the `chezmoi diff` gate.

## Decision 202 (2026-10-22T01:06:00Z)

- Pointer: Kris (02:06 BST), STARSHIP-REVIEW: "The starship trial was okay ... Are you really trying the latest and greatest of it? ... you've all sort of tried to keep on a single line, whereas some of the examples I saw went on to line underneath. Maybe there's more you could do." Read back as: run starship-variants confirms the kit runs the latest Starship release and adds several richer trial variants, including two-line prompts modelled on the official presets, each selectable in one window; still no install, Rig intent, startup or chezmoi change. STARSHIP-REVIEW stays open.
- Pointer: Kris (02:10 BST): "with what you know about what I do, I think you can design a [Starship] prompt which meets my needs. And ... it'd be good to switch between them in the same window and try them all out." Read back as: starship-variants adds a bespoke `kris` variant fitted to his work and makes it the default, alongside the others, all switchable in one window.
- Pointer: Kris (02:10 BST), ORCA-INSTALL: "just give me what you want me to type ... to install Orca and I'll do it now." Read back as: Kris runs the Homebrew install himself; the Rig file is applied later with the tower-finish change in one reviewed step. Kris also interrupted the steer to starship-variants; it was not sent.

## Decision 203 (2026-10-22T06:47:00Z)

- Pointer: Kris (07:47 BST): "can you remove GitUp, and can we add something to expand rig to include removal of items too. Also rig might want to consider other related settings it checks for such as notifications for tools". Read back as: run gitup-remove retires GitUp under the ki-self application lifecycle (Rig declaration in the chezmoi source, uninstall on terra, scoped diff for Kris; sol when Kris is there); RIG-REMOVAL and RIG-NOTIFICATIONS are portable tools-rig behaviour, routed to ki.mac-studio-setup as messages.
- Pointer: Kris (07:48 BST): "I have a number of terminal apps, iTerm2, warp, ghostty - we should decide which are needed". Read back as: run terminal-review surveys them read-only and brings a keep or retire recommendation as a decision; nothing is removed until Kris chooses.
- Pointer: Kris (07:49 BST): "remove motion app too". Read back as: run motion-remove retires the Motion app the way gitup-remove retires GitUp, chained after it because both edit Rig declarations in the chezmoi source.
- Pointer: Kris (07:50 BST): "I try to standardize all of the notifications as well, so we can always check and make sure that they're turned on for things again on a per app basis. It should be some of the configuration of what Rig expects with the app, so you can therefore at least audit against it. And likewise, we do need the capability to be able to delete things." Read back as: added to RIG-NOTIFICATIONS and RIG-REMOVAL in ki.mac-studio-setup; once tools-rig supports it, ki.chezmoi declares Kris's per-app notification values in the Rig catalogue here.
- Pointer: Kris (07:57 BST): "warp doesn't support prompt changes that way". Read back as: the Starship trial (sourcing a variant into a running window) does not work in Warp; trial it in Ghostty or Terminal. Recorded against TERMINALS: it weakens b) and the Starship case for Warp; TERMINALS stays open.
- Pointer: Kris (07:58 BST), trying the Starship variants in Ghostty (rainbow shown): "looks great in ghostty". Read back as: Starship with Nerd Font glyphs works in Ghostty with no font install; evidence for STARSHIP-REVIEW a) and TERMINALS a), neither yet answered.

## Decision 204 (2026-10-22T07:00:00Z)

- Pointer: Kris (08:00 BST), STARSHIP-REVIEW: "my feeling is that we go ahead with using Starship for the prompt handling ... a default one that we bake in with our approach ... by default, it's a simple one, but also, if you do the variant, it changes it for your machine, but it only makes it variant for that machine or for that terminal session, and ... some command line stuff which allows you to change between the different prompts ... We also need to add this to the tools list in the docs that we have within dot files." Read back as: STARSHIP-REVIEW answered beyond a): accept KB-DOTFILES-UE-104 and adopt Starship now. Run starship-adopt declares it in Rig, ships the variants through chezmoi with a simple default, a guarded Zsh fragment, and a `starship-variant` command that switches per session or persists per machine (unmanaged machine-local choice), keeps Warp working, adds Starship to the dotfiles tools docs, retires the trial kit, and stops at the diff gate.

## Decision 205 (2026-10-22T07:05:00Z)

- Pointer: Kris (08:05 BST), with a Ghostty screenshot of `zsh: command not found: starship-variant`: "sometimes it doesn't always work based on the background. What I think would be really good is to have some kind of option where I could ask it to show me what they all look like in the given directory ... without it actually being a prompt ... so it does the equivalent rendering." Read back as: the not-found is a fresh window without the kit sourced; run starship-preview adds a preview-all option to the trial kit now (each variant rendered in the current directory with `starship prompt`, labelled, no switch), and starship-adopt is steered to ship the same in the managed `starship-variant` and to check every variant's colours against Ghostty's background.
- TERMINALS: Kris (08:05 BST): "I definitely think I want to use Ghost Tty as the main one ... I'm happy to drop warp, and I'm happy to drop eye term too, actually." Read back as: a), with Warp retired now rather than after a week's trial. Run terminal-retire (after starship-adopt, same Rig files) makes Ghostty primary with a managed config and Dock item, retires iTerm2 (app, stale `.zshrc` line, leftovers) and Warp (Rig, Dock, skills runtime, `dot_warp/`) in the chezmoi source, uninstalls iTerm2 on terra, and stages Warp's uninstall as an attended step after Kris exports what he wants and deletes Warp's cloud data and signs out. Warp is not quit or uninstalled while sessions may run in it.

## Decision 206 (2026-10-22T07:06:00Z)

- Pointer: Kris (08:06 BST): "I've also asked for a bunch of things that might be better off dealt with through other coordination threads, so feel free to push out those messages to those threads to hand the work over now." Read back as: run handover-route finds every item in this work package whose owner is another work (another Project, territory or repository thread), hands each over as a message line in that work's `messages.md` quoting Kris's words, commits and pushes those lines, and reports the list; the coordinator then drops them from `state.md` and `queries.md` as handed over.

## Decision 207 (2026-10-22T07:07:00Z)

- Pointer: Kris (08:07 BST), first impressions of Orca: "it's really pretty and really good. I think it could actually be a replacement for Z or potentially Z and Delta, or anything else for that matter. In particular, I like its status bar. It's even got things built in which make it so that its own footer wouldn't remove the need for codex bar as well." Read back as: "Z" is Zed; "Delta" is taken as the `git-delta` diff pager until Kris says otherwise; the footer remark is read as Orca's usage footer possibly replacing CodexBar. Run orca-eval maps Orca's capabilities against Zed, delta, CodexBar and the other tools in the Rig catalogue it overlaps, read-only, and brings ORCA-ADOPT with what Orca could retire. Not yet a decision to adopt or retire anything.
- Pointer: Kris (08:09 BST): "Ghosty does have these kind of tabs across the top, but I'm wondering if it has this kind of sidebar based approach as well because it's quite handy in order to see what ran last." Read back as: a requirement for the Warp replacement: a vertical, sidebar view of tabs showing what ran last. terminal-retire is steered to check whether Ghostty offers one (or a close equivalent) and to raise it as a gap rather than retire Warp silently without it; orca-eval to note whether Orca's sidebar covers it. The `kt <territory>` command in the coordinator's reply was an illustration, not an existing command.
- Coordinator (08:11 BST), receiving starship-preview: `starship-variant --all` is in the trial kit; `kris` and `kris-nerd` recoloured to theme-safe colours (foreground, blue, red, purple). Its two medium queries are not raised: both serve Kris's background complaint and stay inside running work. starship-adopt is steered to apply the same colour rule to the managed dev, two-line and one-line variants (official presets untouched); terminal-retire to set `minimum-contrast = 3` in the managed Ghostty config, noted in its diff for Kris's review.
- Coordinator (08:14 BST), receiving orca-eval: "Delta" in Kris's words resolves to Zed's Delta agent workspace (beta, `/usr/local/bin/delta`, 16 launches), not git-delta. Orca replaces Delta; partly covers CodexBar (footer only while open), GitHub Desktop and the Codex app; does not replace Zed (no language server) or Ghostty. Found: telemetry on despite the install plan, agent permission bypass on by default, Orca hooks in managed agent settings. ORCA-ADOPT is medium, so it goes to blind review (orca-adopt-blind) before Kris; the sidebar question went unanswered and is asked there.
- Pointer: Kris (08:14 BST): "What I really want to do as well is make sure that for every application we've got something that understands how it's configured. Whether that's a command line tool which tells you where its files are, but also for an application in terms of anything it does within the system settings, especially in macOS stuff. So, for example, things like notification, file access, all of that, really. Anything that's got with startup jobs. This is more than just installing apps. This is about managing your rig". Read back as: a Rig capability, per-application configuration knowledge (config file locations, macOS settings footprint: notifications, privacy and file-access grants, login items and launch jobs), declared and auditable; it widens RIG-NOTIFICATIONS and RIG-REMOVAL into RIG-APP-FOOTPRINT. Portable behaviour belongs to tools-rig, so it is handed to ki.mac-studio-setup through handover-route; ki.chezmoi declares Kris's per-app values once Rig supports them (Orca's hooks and telemetry, and Warp's leftovers, are the first live cases).
- Pointer: Kris (08:15 BST): "I think also in terms of the tools that we've got, we should probably have some kind of tech radar approach, which is trial, adopt, those kinds of things which indicates where we are with them." Read back as: every tool in the Rig catalogue carries a radar ring (for example Adopt, Trial, Assess, Hold or Retire) showing where it stands. Run radar-design (read-only) proposes where the ring lives (Rig schema in tools-rig, personal data in this repository, or both), how it maps onto existing tiers, profiles and rationales, a first placement of every tool, and how the Rig site shows it; it comes back as RADAR-DESIGN.
- Pointer: Kris (08:17 BST), with a screenshot of the rainbow variant drawing ? boxes for every glyph: "now I'm moving to using Ghost TTY, and in particular in Ghost TTY, I want to make sure that I'm using Starship. I also do want my default prompt that I had previously that works using the simple prompt capability in standard Z sessions. I also don't know, for example, if I can make the nerd fonts work, for example, in the Z terminal." Read back as: Ghostty uses Starship (starship-adopt); the previous prompt (the current oh-my-zsh one with the chezmoi ⚙ count) stays as a named choice, `starship-variant classic` (or off), and remains the prompt wherever Starship is not used; Nerd Font glyphs in Zed's terminal need a Nerd Font, because Zed lacks Ghostty's built-in symbols. Run zed-nerd-font (after terminal-retire, same Rig files) declares a Nerd Font through Rig and sets Zed's terminal font. Whether "Z" means zsh or Zed is asked in one line.
- Coordinator (08:19 BST), receiving starship-adopt: Starship adopted in source (four local commits): `~/.zsh/99_starship` (inert without the binary; old prompt under Warp), completion, seven variants under `~/.config/starship/variants/`, `[tool.starship]` in `16-homebrew.toml`; default `kris`; KB-DOTFILES-UE-104 accepted. It finished before reading the inbox steers: no `classic` choice and no `--all` preview. Run starship-classic adds them (and the colour rule if missing). STARSHIP-APPLY raised now; `classic` follows as a small second apply.
- Coordinator (08:19 BST), receiving orca-hooks-blind (Codex): the premise was half wrong. Claude's settings already preserve Orca's hooks (fragment binding); Codex's whole-file `hooks.json` template would strip Orca's nine registrations. Recommends a narrow Codex fragment-preservation change (Pattern C), holding only Codex's hooks target meanwhile (high, reviewed: refines apply-check's medium a). ORCA-HOOKS raised.
- Coordinator (08:21 BST), receiving orca-adopt-blind (Codex): agrees with a bounded laptop evaluation to 5 November after safety fixes (high, reviewed). Differs on the first retirement trial: orca-eval proposed Delta; the blind review proposes CodexBar only, because Delta's shared and cloud features may be in use. Both views shown in ORCA-ADOPT. Sidebar: Orca's Agents feed and experimental Agent Dashboard show each agent's state and last message; a Warp-style last-command list per terminal is not established. Safety today: agent default arguments bypass permission prompts (Codex also its sandbox), "Trust folder when Orca starts agent" is on, telemetry on.
- Coordinator (08:25 BST), receiving radar-design: the ring can only reach `rig doctor` and the site if tools-rig carries it (Rig rejects unknown keys; export fields are fixed; no second catalogue in front of Rig). RADAR-DESIGN raised at high: a) tools-rig owns vocabulary, review fields, doctor's `review-overdue` and the export field; chezmoi owns values; the site owns display. RADAR-PUBLIC (medium) goes to blind review (radar-public-blind, Codex) before Kris.
- Coordinator (08:27 BST), receiving starship-classic: `starship-variant classic` restores the previous `99_prompt` prompt (session, or `--machine classic` for the machine); `--all` previews classic and every variant; dev, two-line and one-line recoloured to the theme-safe rule (chezmoi `27d524a`, `20922de`, local). STARSHIP-APPLY needs no extra targets, so its option b) (wait for classic) falls away.
- Coordinator (08:28 BST), receiving radar-public-blind (Codex, high): agrees with radar-design's a) for the public site; RADAR-PUBLIC lifts to high (reviewed). Added safeguards: a public Hold tool must not name a private replacement (apply public relationship closure to replacements), say the site shows the public subset, and remove retired tools from every generated artefact.
- Coordinator (08:31 BST), receiving terminal-retire: Ghostty primary in source (managed `config.ghostty`, GitHub light/dark theme following macOS, built-in Nerd Font symbols, 30-second command notifications, Dock item, `.sh`/`.zsh` to Zed, guide); `territory <code>` zsh function replaces Warp's tab configs (Ghostty AppleScript, preview feature, asks Automation once); Warp retired in source; iTerm2 trashed on terra (undo folder `~/.Trash/terminal-retire-202610220807`). Candidate doctor 4 → 7, the three added (`.sh`/`.zsh` handlers, Dock order) clear at `rig apply`. Its report does not answer the sidebar requirement. WARP-RETIRE is medium and destructive, so warp-retire-blind (Codex) reviews it, including the sidebar gap and how its apply combines with RIG-APPLY and STARSHIP-APPLY.
- Coordinator (08:36 BST), receiving zed-nerd-font: "Z" taken as Zed (orca-eval confirmed). Zed has no built-in symbol font, so the symbols-only Nerd Font (`font-symbols-only-nerd-font`, cask, core) is declared in Rig and set as Zed's `terminal.font_fallbacks` (`Symbols Nerd Font Mono`), keeping the editor font (chezmoi `768c59a`, `45bd78d`); candidate doctor 7 → 8, the new one `missing` until installed. ZED-FONT-APPLY raised at high.
- Coordinator (08:38 BST), receiving warp-retire-blind (Codex): agrees Warp goes, but staged, still medium: prove Ghostty and `territory` first, preserve exports, check whether sol shares the Warp account before deleting cloud data, inspect the cask's zap scope before uninstalling. Ghostty 1.3.1 has no sidebar or per-tab last-command view (titles and prompt navigation only), so Warp's sidebar workflow has no replacement. It also found that the pending applies overlap: each Rig file applies whole, so RIG-APPLY, STARSHIP-APPLY, ZED-FONT-APPLY and WARP-RETIRE's predictions are stale. Run apply-plan builds one ordered, staged, verified plan (APPLY-PLAN) to replace them.
- Pointer: Kris (08:40 BST): "I'm thinking in Ghosty what we do is we have three tabs. The first tab is the active territory that we're working in, e.g. workspaces, knowledge islands. The second tab is workspaces in the home folder, so I can do any bulk updates. And the third one is the Cheyenne Wai home. That would be my standard setup." Read back as: Ghostty's standard set is three tabs: the active territory folder, `~/workspaces`, and the chezmoi source. Run ghostty-tabs adds a command for it on the `territory` function (territory code, else the last used, else `ki`), opens it at Ghostty start if Ghostty supports that cleanly, keeps `territory <code>` for one tab; apply-plan is steered to treat those targets as still moving.
- Coordinator (08:46 BST), receiving ghostty-tabs: `territory-set [code]` opens the standard set (territory tab reused, `ws` for `~/workspaces`, `dotfiles` for the chezmoi source), last code remembered in `~/.local/state/territory/last` (default `ki`); a once-per-launch pre-prompt hook opens it when Ghostty starts with one empty window (Ghostty has no clean config option); `territory <code>` unchanged (chezmoi `557af1d`). Only target `~/.zsh/60_territory`, folded into APPLY-PLAN.
- Coordinator (08:49 BST), receiving apply-plan: one staged terra plan replaces RIG-APPLY, STARSHIP-APPLY, ZED-FONT-APPLY and WARP-RETIRE's timing. Stage 1 (backup, `brew install starship` and the font, scoped apply of 12 targets including all four Rig files; doctor 6 → 6 with a different mix), stage 2 Kris's attended Warp retirement after Ghostty proves itself and sol's account is checked (zap trashes; leftovers listed), stage 3 `rig apply` of handlers and Dock when the both-Mac hold lifts. Removing Warp from Rig while it runs is safe (Rig never uninstalls an undeclared tool). Never a bare `chezmoi apply` (Orca hooks). APPLY-PLAN raised at high; sent to Kris.
- Pointer: Kris (22 October, via HNR > SoP, IMPORTANT · DRAIN): "take stock and drain to On hold, "hold, more expected". ... Kris will bring the work packages back up one by one, in order." Read back as: hold, more expected. No run was in flight; the six open queries are parked; the chezmoi source's 13 commits from this work's runs were pushed under the drain's instruction to push own work; the ki-principal work-folder commits stay unpushed because other sessions' commits are stacked among them.
- Pointer: Kris (after the DRAIN hold): "I know we drained, but there is a lot of drift on this machine, so can we work through that. Also, sometimes we have machine specifics, and this is `terra` so if there is anything for that we can look at it too. But don't try to do too much else." Read back as: lift the hold for terra drift and terra-specific items only. Run drift-survey (read-only) classifies every drifted target and `rig doctor` finding and lists terra-actionable items; APPLY-PLAN, ORCA-HOOKS and TOWER-PATH come back from Parked because they are drift; RADAR-DESIGN, RADAR-PUBLIC and ORCA-ADOPT stay parked.
- Coordinator (11:55 BST), receiving drift-survey: 37 drifted targets; 22 are APPLY-PLAN stage 1 (source ahead, no live edits), 11 are stage 2 (Warp), `~/.claude/settings.json` only reorders Orca's hook (harmless), `~/.codex/hooks.json` would lose Orca's hooks (ORCA-HOOKS), `~/.codex/config.toml` changed both sides and was not diffed (1Password-backed render, so Kris diffs it at the screen). `rig doctor`'s 6: GitUp pair clear at stage 1; Dock, `.toml` handler and its 19 October failure need `rig apply` (both-Mac hold stands, so the survey's "then `rig apply`" is not offered); firewall stays with ki.mac-studio-setup (FW-EXPOSURE). terra: Spark launcher and KB-DOTFILES-UE-086 B6a, B6b, B6d, C7i removals still pending, B7 only needs ticking; destructive, so terra-removals-blind (Codex) reviews TERRA-REMOVALS first. APPLY-PLAN stage 1 now also takes `~/.claude/settings.json`.
- Coordinator (12:02 BST), receiving terra-removals-blind (Codex, high): every item is still installed, Mercury Weather included, so B7 needs a real uninstall, not a tick. Holds before removal: Prime Video has about 17 GiB of offline media; BlueStacks' own uninstaller and cleanup watcher delete a 3.3 GiB instance and shared NowGG sign-in; Creative Cloud needs an at-screen check of products, sign-in and pending sync, then its own uninstaller. Ready in an attended pass: Spark launcher (stop daemon, `spark-app` cask without zap, keep Spark Desktop), Clockology, Nitro, Mercury (`sudo mas uninstall`), Homebrew `cloudflare-wrangler` (no dependents; npm Wrangler stays). Running B ahead of B1–B5 needs Kris's say-so. TERRA-REMOVALS raised at medium, reviewed; state to supervisor.
