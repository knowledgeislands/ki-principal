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

## Decision 102 (2026-10-19T19:10:57Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- You can take a mark since the last update that you gave me, so next time the summary gives me what I need to know.

Read back as: mark at 2026-10-19T19:10:00Z, the 20:10 BST update.

## Decision 103 (2026-10-19T19:43:22Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- go ahead with the 2 recommendsations.

Read back as option a) of APPLY-CARRY and of RIG-FIREWALL-REHEARSE, including pushing this work's chezmoi source commits so terra can pull.

## Decision 104 (2026-10-19T19:53:54Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- TOML-HANDLER, reviewed a) high, narrows Kris's APPLY-CARRY go-ahead of 20:30 BST: carry Terra without the TOML target, route the dynamic-type fallback to tools-rig through ki.mac-studio-setup, and accept the TOML drift finding on both Macs until it lands. No new owner authority taken.

## Decision 105 (2026-10-19T19:55:50Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- TERRA-PULL, from apply-terra, a) high, under Kris's standing "It can do anything that's high confidence": fast-forward Terra's chezmoi checkout from Sol over SSH and rerun apply-terra; no credential or sshd change.

## Decision 106 (2026-10-19T20:02:14Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- PAPERCLIP-PLIST, from apply-terra-2, a) high, under Kris's standing "It can do anything that's high confidence": leave Terra's disabled `uk.me.kris.rig.paperclip.plist` in place until the Paperclip rebuild is designed.

## Decision 107 (2026-10-19T20:04:44Z)

home: +/_WORK/ki.chezmoi/work.md class: operational

- RIG-FIREWALL-RUN are you walking me though it?

Read back as option a): Kris runs the Terra rehearsal from Sol now, walked through step by step; a follow-up run records the evidence and commits the `core` declaration, no push or apply.
