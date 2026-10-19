# Brief: sol-preflight

Work: KI > Rig > chezmoi in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal`. Authority: Kris, 19 October 22:16 BST, SOL-FIREWALL a): "a quick read-only check of Sol's firewall, and then apply with me on Sol, and then check that screen sharing works from Terra." This run is the read-only check plus preparing the attended apply. You change nothing: no `sudo`, no `chezmoi apply`, no `rig apply` other than `--dry-run`, no commits.

Context: the Terra rehearsal passed at 22:06 BST, and firewall-record (which you wait for) has committed the `core` firewall declaration in the chezmoi source. Reports are in `/Users/krisbrown/.local/state/ki/agents/chezmoi/`: `firewall-record`, `firewall-rehearse-v2.md`, `firewall-freeze` and `firewall-seq-review`. pf is currently disabled on Sol, so the first apply turns pf on for the first time.

Do, on Sol, without root:

1. Read `/etc/pf.conf`, `/etc/pf.anchors/` and any pf-related LaunchDaemons. Compare them with stock macOS 27, and name anything that is not Apple's default. Say what enabling pf will activate beyond the new anchor, and whether that can affect SSH (22), Tailscale or Screen Sharing.
2. Run `rig doctor` and read every finding. Run `chezmoi diff --no-pager --use-builtin-diff` for the changed `~/.config/rig` targets only; do not run a full `chezmoi diff` (the LOCALS-DIFF warning). Run `rig apply --dry-run` for the firewall target, and report exactly what it will write and run.
3. Write `/Users/krisbrown/.local/state/ki/agents/chezmoi/sol-apply.md`: the attended sequence for Kris at Sol. It covers:
   - the `chezmoi apply` of the named targets, after Kris has reviewed the diff;
   - `rig apply --sudo` for the firewall target only;
   - a check block that refuses unless it is on Sol (hardware UUID `BFDD9EED-C084-5B5C-BECB-070FF0D05916`) and uses literal labels, with no shell variables between blocks;
   - a fresh-SSH check from Terra to Sol, and Screen Sharing from Terra over the tailnet;
   - an undo block.

   Follow the guard style of `firewall-rehearse-v2.md`. Each block says what Kris should see.

Stop and report if step 1 finds anything that enabling pf could turn on unexpectedly. Report under the owner report, with the work's report heading and `› sol-preflight`, including the diff for Kris to review.
