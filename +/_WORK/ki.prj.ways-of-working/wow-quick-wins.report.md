# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-quick-wins

**🤖 → 👤 Handoff to supervisor · Run report at 03:57 GMT · last mark 02:07 BST 25 Oct**

---

## Done

- [KI-OBSERVA-BRG-004](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-BRG-004-turn-feedback-sending-on.md) delivered and awaiting review in apps-observatory.local, commit `d278f8a`, pushed; the running Observatory still serves the old build until it is restarted with `launchctl kickstart -k "gui/$(id -u)/uk.me.kris.rig.observatory"` and checked at `http://127.0.0.1:1675/`, which the run did not do.
- [KI-TOOL-RIG-CORE-073](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-073-native-tool-absolute-path-fallback.md) delivered and awaiting review in tools-rig, commit `a3b7f57`, pushed; full gate passed (648 bats, shellcheck, assemble, benchmark, smoke, mandoc, diff-check); `ki repo audit` keeps its one pre-existing SHELL-HOOK failure on the untouched pre-commit hook.
- [KI-TOOL-RIG-CORE-071](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-071-firewall-exposure-wording.md) delivered and awaiting review in tools-rig, commit `5d2472f`, pushed; same gate, same pre-existing audit finding.
- [KI-TOOL-RIG-CORE-070](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-070-handler-read-back-after-confirmation.md) delivered and awaiting review in tools-rig, commit `e882998`, pushed; same gate (648 bats), same pre-existing audit finding; the bound is 120 s attended, none unattended, overridable by `RIG_HANDLER_CONFIRMATION_TIMEOUT`.
- [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) delivered and awaiting review in tools-ki, commit `5428d384`, pushed; coverage gate passed at the 100% thresholds (97 files, 2151 tests), tsc, Biome, command inventory, mandoc, audit and diff-check passed, the worktree audit's three failures are none of this change's (the pre-existing lint-staged `--write`, a symlinked `node_modules` worktree artefact, and the worktree base behind `main`, cleared by rebasing); the record's Verification names the first rebase target `631deaf9`, and the commit was then rebased once more onto `183c4746` over three roadmap-only commits that touch none of its files; the coverage run takes about 27 minutes on this machine and the first attempt was killed at a 10-minute budget before being rerun.
- [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) skipped: the only route to a stable stats badge without changing the record's shape is a viewer change, which its Boundary excludes; see GOV202-ROUTE below. No change made in ki-agentic-harness.
- [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) skipped: a firewall change gated on Kris's attended NordVPN check and the unanswered PLAN068 queries, so it is connection-critical and not agent-doable tonight.
- [KI-TOOL-RIG-CORE-069](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md) skipped: its first step is Kris's attended native probe on `sol`, the only live change in its plan and the gate before delivery starts, and the setter route is settled only by that probe's result; nothing an agent can do tonight.
- tools-ki worktree `/private/var/folders/6b/b4c73j8s6w12g2k9_yl652_h0000gn/T/ki-agents/ways-of-working/wow-quick-wins/tools-ki-cli-160` on branch `wow-cli-160` is level with `main` and left in place for `git worktree remove`, since removal could wait on a permission prompt; its two `node_modules` symlinks into the primary checkout are the run's and are untracked.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The Observatory restart above, for Kris at the machine.
- Five records await Kris's acceptance: KI-OBSERVA-BRG-004, KI-TOOL-RIG-CORE-073, KI-TOOL-RIG-CORE-071, KI-TOOL-RIG-CORE-070 and KI-TOOL-KI-CLI-160; the run accepted nothing.
- KI-TOOL-RIG-CORE-070 leaves an attended `rig apply` on `sol` to Kris, since no live handler change was in scope.

## Queries

### GOV202-ROUTE - how the stable stats badge reaches the skill-area diagrams

**Context:** [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) wants each skill-area diagram component to carry a stable stats badge. The ten diagrams' components already carry a `sublabel` of the form "concern · trigger" and a `sources` list, and the viewer renders `sources` as the badge; replacing that badge means a viewer change, which the record's Boundary excludes, and the only no-viewer route is appending the stats to the `sublabel` text, which changes the shape the record describes. Neither reading is small enough to deliver under "keep each change as small as the record allows" without Kris choosing.

**Query:** Which route should KI-HARNESS-GOV-202 take?

**Options:**

a) (recommended, confidence medium - the generator change is small and keeps the Boundary, but it alters the sublabel shape the record and viewer currently assume) Append the stable stats to the existing `sublabel` text in the generator, keeping the `sources` badge as it is, and replan the record's Steps to say so.

b) Widen the Boundary to allow a viewer change so the badge itself shows the stats, and plan it as a larger record.
