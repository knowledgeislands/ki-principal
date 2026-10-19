# Brief: firewall-review

Blind review of one query for KI > Rig > chezmoi, under the `ki-coordination` Query review rule. Check the claims directly where you can, read-only, then return your own recommended option, a confidence and a one-line reason. Change nothing; make no remote or `sudo` call.

Evidence: `/Users/krisbrown/.local/state/ki/agents/chezmoi/rig-dock.report.md`; the tools-rig [rollback guide](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/user/operational-resources.md); the ki-engineering connection-critical rule in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-engineering/references/standards-engineering.md`; KI-TOOL-RIG-CORE-047 in tools-rig `docs/roadmap/`.

## RIG-FIREWALL-REHEARSE

**Context:** A firewall declaration must not be written until the restore has been rehearsed. Sol has no Rig firewall anchor or daemon, and this session has no `sudo`. Terra has a live, unreceipted anchor (`/etc/pf.anchors/uk.me.kris.rig.firewall.screen-sharing` and its LaunchDaemon, loaded since 15 October). The guide's restore is `sudo launchctl bootout system/LOCATOR` then `sudo pfctl -a com.apple/LOCATOR -F all`, reversed by `sudo launchctl bootstrap system /Library/LaunchDaemons/LOCATOR.plist`. The declaration would adopt Terra's anchor and cover every Mac in `core`: tailnet-only Screen Sharing, `tcp:5900` and `udp:5900`.

**Query:** Where should the restore be rehearsed before the declaration is written?

**Options:** a) In an attended session from Sol, run the restore on Terra over SSH, confirm SSH still connects and the rules are gone, re-bootstrap, record evidence; then a run writes the declaration for an attended `rig apply --sudo` on Terra then Sol. b) In an attended session on Sol, apply the declaration with `--sudo` and rehearse the restore there at once. c) Leave the firewall to CORE-047's live acceptance and write no declaration now.

## Report

Owner report with heading `# KI > Rig > chezmoi › firewall-review` and, under `## Done`, `RIG-FIREWALL-REHEARSE: <option>) confidence <level> - <reason>`, plus any claim in the Context you found false.
