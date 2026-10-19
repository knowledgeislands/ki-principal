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
