# bootout-review brief

You are a blind reviewer for the work `ki.mac-studio-setup` in Knowledge Islands Principal, under the QUERY-REVIEW rule of the `ki-coordination` standard. Form your own view of the query below: the course you would recommend, your confidence (`high`, `medium` or `low`) with a one-line reason, and the evidence you checked. Read anything in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig` and run read-only Git commands only. Never run `launchctl`, `rig`, `sudo` or `ki repo conform`. Edit, commit, push or delete nothing beyond writing your report.

## BOOTOUT-GUARD - Guard every bootout site against an empty label

**Context:** `launchctl bootout system/` with an empty label shut terra down at 21:07 on 19 October, during a hand-run rehearsal. In tools-rig, `rig_firewall_retire` and `rig_firewall_load_state` (`src/rig/29-firewall.bash`) run `bootout "system/$locator"` without checking the locator themselves. They rely on `rig_firewall_locator_valid` having run earlier, at validation and at retirement preflight, and `rig_prepare_retire_invocation` always runs that preflight today. `rig_launchd_unload` (`src/rig/20-orchestration.bash`) has the same shape in the `gui/<uid>` domain, and its callers check the label first. Check these claims yourself.

**Query:** Should a defence-in-depth guard be added at each bootout site?

**Options:**

- Capture a Triage record in tools-rig for a local refusal of an empty or invalid label at each bootout site, with a fixture test each.
- Capture nothing, since the current guards hold.
- Fold the guard into KI-TOOL-RIG-CORE-047 (`docs/roadmap/KI-TOOL-RIG-CORE-047-tailnet-only-listener-firewall.md`) when it is next planned.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/bootout-review.report.md`, starting with a `# bootout-review report` heading, using British English and ASCII hyphens only. Do not commit it.
