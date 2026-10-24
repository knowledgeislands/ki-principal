# Rig apply hold › hold-blind

**🤖 → 👤 Handoff to supervisor · Run report at 19:12 BST**

---

## Done

- Verified terra's active executable resolves to this clean checkout, HEAD `87fa261`, reporting 0.8.0; local tags stop at v0.7.0. The version string alone does not establish a released installation.
- Traced two distinct cask defects: `ebd6e32` addressed healthy self-updated/foreign-source applications being treated as missing; `671c864` corrected the later missing-tap metadata regression. The [original application record (pruned)](https://github.com/knowledgeislands/tools-rig/blob/ea7c3b6/docs/roadmap/RIG-CORE-043-self-updating-applications.md) documents the OneDrive refusal and foreign-source failures.
- Confirmed `671c864` is already contained in both v0.6.3 and v0.7.0, as well as terra's HEAD; waiting specifically for a v0.8.0 tag adds no cask fix.
- Found a contemporary link between the October 14 incident and executable selection: [KI-TOOL-RIG-CLI-026 (pruned)](https://github.com/knowledgeislands/tools-rig/blob/74140e530fe61ebecb9a687038d76cf3244439b3/docs/roadmap/KI-TOOL-RIG-CLI-026-per-tool-development-mode-switch.md) records an older Homebrew executable masking a broken checkout link while the fix was on main. The [release guide](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/guides/developer/releasing.md:18) explicitly supports checkout use. Checkout mutability remains a risk; an immutable-release requirement is not established by these records.
- Found no later open cask-specific record. Later operation-lock/history gaps were addressed by `55ee447`, `59e13f2` and `cacce0c`; current open apply-related defects include [TOML dynamic handlers](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-069-dynamic-type-handler-fallback.md:25) and [firewall evaluation](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md:35).
- Reviewed apply help and repository evidence only; no apply, network call, prohibited report/work-folder read, repository edit or commit. Tests were not rerun; today's successful targeted apply is supplied context, not independently reproduced evidence.

## In Progress

Nothing is running.

Outstanding - no action requested now: sol's executable/build remains unverified. The permitted sources do not establish the original hold's complete rationale, so its release wording must not be treated as automatically satisfied.

## Queries

### HOLD-LIFT - Replace the blanket hold with a bounded exception?

**Context:** Terra contains both identified cask corrections and later apply safeguards. Checkout execution is supported, but its contents can change without a new version string. Sol is unverified. The pending TOML assignment has a recorded unresolved failure; tagging the present candidate would not resolve it. No equivalent open Dock defect was found.

**Query:** Should Kris explicitly replace the both-Mac hold with permission for reviewed targeted applies?

**Options:**

a) (recommended, confidence medium - terra's fixes are verified, but sol and the original release-only intent remain unverified) Lift for terra's reviewed targeted applies, including Dock and shell-handler targets subject to normal preflight and effective-handler verification; leave TOML and firewall work held. Lift for sol only after checking its active executable against terra's reviewed build, including later safeguards. Recheck checkout identity before each carry.

b) Keep the hold until v0.8.0 is tagged and installed if immutable release installation was the intended condition; retain the separate TOML restriction until its defect is fixed.

c) Lift on both Macs now, accepting that sol's installed code has not been checked.
