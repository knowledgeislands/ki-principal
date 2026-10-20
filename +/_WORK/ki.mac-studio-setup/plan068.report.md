# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › plan068

**🤖 → 👤 Handoff to supervisor · Run report at 01:58 BST · last mark 23:36 BST on 19 October**

---

## Done

- [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) is fully shaped and committed locally on `main` as `fcf14da`. It stays in `draft`, because Ready needs Kris's explicit approval (PLAN068-READY below). It now has a source-grounded Current state, gated Steps, Files touched, Verify, Dependencies and Documentation impact, plus three planning queries.
- **Attended NordVPN check written** as ten numbered steps with expected output. It has three blocks: N (a read-only root inspection with an `EVALUATED`, `NOT EVALUATED` or `UNKNOWN` verdict), P (endpoint probes from `sol` that report `GREETING`, `TIMEOUT` or `REFUSED`) and R (the restore). It takes in every correction from the blind review. All three blocks and both root scripts pass `zsh -n`. None was run.
- **Restore path:** R reloads Apple's own `/etc/pf.conf` into root and reloads Rig's anchor with the command its LaunchDaemon already runs. It refuses while the NordVPN app is running or another VPN is connected. Step 4 rehearses R on `terra` before NordVPN connects, and the trial stops if that rehearsal fails. NordVPN's own disconnect and a console restart are the fallbacks. The restart is proven by KI-TOOL-RIG-CORE-047's restart evidence. The kill-switch phase is optional and needs Kris's separate go.
- **The planning found a new gap in the source.** If the unprivileged observation says a firewall is present, `rig apply --sudo` neither prompts nor rereads, not even the child's rules. RIG-ORCH-043 and the guide specify that behaviour, but ADR-KI-TOOL-RIG-009, the guide's other sentence and 047's Risks say apply checks the rules on every run. The plan covers this as PLAN068-VERIFY-GRANT.
- Checks: `git diff --check` passed. `ki repo audit --repo .` passed with 0 failures and no warning on this record; one Steps-shape failure was fixed before the commit. The commit hook ran the full Bats suite, and all of it passed. No pf read or write, sudo, `launchctl`, apply, push or remote call was made.

## In Progress

Nothing is running. Implementation waits for the gate: Kris's attended check, with steps 2 to 4 matching and the results pasted into the record, and answers to the queries below.

The temporary directory still holds the six draft and syntax-check files. Removing them needed a permission that was not granted. Their content is in the record, so `ki agent close` can clear them.

## Queries

### PLAN068-VERIFY-GRANT - Verify a present firewall under `apply --sudo`

**Context:** Today, if the unprivileged observation says a firewall is present, `apply --sudo` takes no grant and runs no privileged read. A Mac whose files look correct, while NordVPN has replaced root's ruleset, would therefore never reach the new root check.

**Query:** Should an explicit `apply --sudo` take the grant to verify a present `macos-pf` firewall?

**Options:**

a) (recommended, confidence high - without it the root check never runs where the bypass hides; plain `apply` stays promptless) Count a selected `macos-pf` firewall as work for an explicit `--sudo`, and update RIG-ORCH-043, the ADR and the guide.

b) Keep today's rule, and run the root check only after a repair.

### PLAN068-UNPRIV - What doctor reports without privilege

**Context:** The record's Goal says doctor reports unknown, not healthy, when it lacks privilege. Today a matching firewall is `present` with `kernel-rules-unverified`. An unprivileged `scutil` hint would be neither necessary nor sufficient: the kill switch can keep the replaced ruleset after a disconnect, and Tailscale itself appears as a connected service.

**Query:** Should the unprivileged observation change from `present` to `unknown`?

**Options:**

a) (recommended, confidence medium - `unknown` would make every firewall a permanent doctor finding and drown the signal) Keep `present` with `kernel-rules-unverified`, and state explicitly that this covers root reachability and never means the rules are evaluated.

b) Report `unknown` with `kernel-rules-unverified`, and accept a standing finding on every Mac with a firewall.

### PLAN068-READY - Approve the plan to Ready

**Context:** The detection plan holds whatever the check shows, unless step 5 contradicts the helper's template, and the gate catches that case. Re-assertion stays out of this record either way.

**Query:** Approve [KI-TOOL-RIG-CORE-068](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-068-replaced-pf-root-ruleset-bypass.md) to Ready, with implementation gated on the attended check?

**Options:**

a) (recommended, confidence medium - the plan is complete and its only live dependency is an explicit gate) Approve Ready. `ki-implement` starts only after the gate is met.

b) Keep it in draft until Kris has run the check.

### 🤖 → 👤 Handoff to supervisor · since 01:58 BST

👤 4 with you · 🅿️ 0 parked

- [with you] PLAN068-VERIFY-GRANT present-firewall verification · supervisor of ki.mac-studio-setup · since 01:58 BST
- [with you] PLAN068-UNPRIV unprivileged doctor view · supervisor of ki.mac-studio-setup · since 01:58 BST
- [with you] PLAN068-READY Ready approval · supervisor of ki.mac-studio-setup · since 01:58 BST
- [with you] Attended NordVPN check on `terra` · Kris · since 01:58 BST
