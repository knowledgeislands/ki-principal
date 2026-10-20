# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › rig-capture

**🤖 → 👤 Handoff to supervisor · Run report at 23:31 BST · last mark 19:01 BST**

---

## Done

**RIG-UNLOAD-LABEL: no record needed (confidence high).** `rig_launchd_unload` cannot receive an empty label, so I captured nothing for it. It has two callers, both in `src/rig/20-orchestration.bash`. `rig_launchd_apply_resource` and `rig_launchd_retire_resource` each call `rig_launchd_plist_path "$label" || return` before they unload. That function returns 2 unless `rig_launchd_label_valid` passes, and that check rejects `''` and any character outside `A-Za-z0-9._-`. Earlier, `rig_launchd_preflight_resource` and `rig_launchd_preflight_retirement` also reject an invalid label with `rig_fail`.

The function's domain is also not `system`. It is `gui/<uid>` unless `RIG_LAUNCHD_DOMAIN` is set, and an empty override falls back to the default. So even an empty label here would have given `gui/<uid>/`, not the `system/` that shut terra down.

The `rig launchd` actions in `src/rig/30-commands.bash` don't bootout at all. They also check the label first. The firewall's own `bootout "system/$locator"` calls in `src/rig/29-firewall.bash` are guarded by `rig_firewall_locator_valid`, but only at validation and at retirement preflight. `rig_firewall_retire` and `rig_firewall_load_state` don't check again themselves. See Queries.

**TOML-HANDLER: captured.** [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) asks for a dynamic-type fallback in `macos-handlers`, with matching observation, a named failure detail, fixture tests and a guide update. It cites the apply-carry and toml-review reports. Status `triage`, with no horizon, priority medium and size s. It is not adopted.

Commits in tools-rig, local only and not pushed: `ccd14ac` (reserves KI-TOOL-RIG-CORE-069 in the ledger) and `4f97d74` (captures the record). The tree was clean before and after.

Checks: `ki repo audit --repo .` passed with no failures. Its 22 warnings don't name the new record. `git diff --check` was clean. The shell gate doesn't apply to a docs-only change. I made no code edits and ran no `launchctl` or `rig apply`.

## In Progress

Nothing is running.

## Queries

**Context**

Rig's `system/` bootouts only stay safe because a check runs earlier. `rig_firewall_retire` and `rig_firewall_load_state` don't check the locator again. With an empty locator, `launchctl print system/` would succeed. The function would then report the service as loaded, and the bootout that follows would shut the machine down, the same failure terra had. Today `rig_prepare_retire_invocation` always runs the retirement preflight first, so this isn't a live defect. A future caller that skips the preflight would bring it back. `rig_launchd_unload` has the same shape in the user domain, but there the stakes are lower.

**Query**

Should I capture a defence-in-depth record that adds a local refusal of an empty or invalid label at every `bootout` site?

**Options**

a) (recommended, confidence medium - small and cheap, and it closes the one input that turns a service bootout into a machine shutdown, but nothing is broken today) Capture a Triage record in tools-rig for a guard at each `bootout` site, both `rig_launchd_unload` and the two firewall bootouts, with a fixture test for each. b) Capture nothing. The current guards are proven, and the hazard on 19 October came from the hand-run rehearsal, not from Rig. c) Fold the guard into [KI-TOOL-RIG-CORE-047](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md) when it is next planned, rather than giving it its own record.
