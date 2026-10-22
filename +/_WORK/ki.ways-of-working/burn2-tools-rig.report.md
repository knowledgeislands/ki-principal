# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › burn2-tools-rig

**🤖 → 👤 Handoff to supervisor · Run report at 07:26 BST · last mark 05:20 BST**

---

## Done

- [KI-TOOL-RIG-CORE-053](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-053-macos-menu-bar-declarations.md) - before: draft, Next; after: awaiting review, Now, with a complete review packet. Commit `c55f2e9`, fast-forwarded into `main` and pushed to `origin`. Rig can now declare a macOS menu bar layout and report unreadable, unplaced, visibility and order drift; apply skips it as observe-only and never writes a preference. The gate queries were taken under the coordinator decision of 06:53 BST, and the record asks the reviewer to confirm the first observe-only resource shape.
- Gate: all 611 tests, shellcheck, `bash -n`, assembly check, benchmark, native smoke probes, manual lint and `git diff --check` pass. The commit hook ran the whole suite and its staged audit passed.
- Task 2, SHELL-HOOK - left unchanged: commit `e651edb` (the ki.chezmoi hooks rollout, 20 October 00:39 BST) touched `.githooks/` within the last day. The whole-tree audit on `main` still fails SHELL-HOOK because `.githooks/pre-commit` runs Bats.
- One follow-up line added to the [ways-of-working messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md): in a linked worktree the audit fails RUNTIMES-2 because the ignored runtime activation directories exist only in the primary checkout. The line is uncommitted in `ki-principal`.
- The worktree `burn2-tools-rig` and branch `run/burn2-tools-rig` are retired; `tools-rig` `main` is level with `origin`.
- Containment note: during test development one run reached the real `/usr/bin/defaults read` for two domains on `sol`. Those were reads only and nothing was written; the test now uses the isolation stub.

## In Progress

Nothing is in progress. The remaining open records were assessed and none can move without Kris:

- [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) - unchanged, draft, Now: step 1 is Kris's attended handler probe on `sol`, a live change no run may make.
- [KI-TOOL-RIG-CORE-067](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-067-package-managers-as-catalogue-tools.md) - unchanged, draft, Next: already planned; Ready waits on PLAN067-EDGES, -OPTIN, -MATRIX, -ADR and -READY, which are owner decisions.
- [KI-TOOL-RIG-CORE-048](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md) - unchanged, draft, Soon: promotion needs owner decisions on field names, public-key declaration and archive layout.
- [KI-TOOL-RIG-CORE-064](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-064-unmanaged-configuration-scan.md) - unchanged, triage: adoption is an owner choice, and a blind review of its rejection is pending under the mac-studio-setup CANCEL-MERGE decision.
- [KI-TOOL-RIG-CORE-056](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-056-menu-bar-order-persistence.md) - unchanged, draft, Future: an investigation whose experiments need a throwaway app or scratch account, and whose merge into KI-TOOL-RIG-CORE-053 awaits the same blind review.

## Queries

**SHELL-HOOK in tools-rig**

**Context:** The whole-tree `ki repo audit` on `tools-rig` `main` fails SHELL-HOOK because `.githooks/pre-commit` runs the full Bats suite. This run left it alone because the ki.chezmoi hooks rollout changed `.githooks/` within the last day.

**Query:** Should a later run move Bats out of the commit hook now that the rollout has settled?

**Options:** a) Yes: a run tomorrow moves Bats to CI and the documented gate, once no other session has touched `.githooks/` for a day. b) Keep Bats in the hook and accept the SHELL-HOOK failure as a known exception. c) Route it to the ki.chezmoi hooks work to fold into its rollout.

**KI-TOOL-RIG-CORE-053 review shape**

**Context:** The menu bar layout is Rig's first observe-only setup resource. Apply records it as skipped `observe-only` without failing, and ADR-KI-TOOL-RIG-006 gained one paragraph naming observation-only layouts.

**Query:** Is the observe-only shape acceptable at review, or should apply treat a drifted menu bar differently?

**Options:** a) Accept the shape as delivered: skipped, with a Command-drag reminder and no failure. b) Have apply report drift as a non-failing warning. c) Return it for a different contract.

### 🤖 → 👤 Handoff to supervisor · since 06:57 BST

✅ 1 delivered · ⏸ 5 waiting on Kris

- [committed] KI-TOOL-RIG-CORE-053 at awaiting review, pushed
- [blocked] SHELL-HOOK left because of `e651edb` · work/ki.ways-of-working · since 06:57 BST
- [blocked] KI-TOOL-RIG-CORE-069, -067, -048, -064 and -056 need owner decisions or attended checks · owner · since 07:25 BST
- [unpushed] Follow-up line in ki-principal messages.md, uncommitted
