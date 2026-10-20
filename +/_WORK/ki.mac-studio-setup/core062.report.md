# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [Mac Studio setup](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup.md) › core062

**🤖 → 👤 Handoff to supervisor · Run report at 00:55 BST · last mark 23:36 BST**

---

## Done

- [KI-TOOL-RIG-CORE-062](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/KI-TOOL-RIG-CORE-062-own-address-firewall-destination.md) records Q-062-SCOPE a) and Q-062-ABSENT a) under Queries. Its Verify now says any live rollout is attended at the screen and carries KI-TOOL-RIG-CORE-047's tested SSH rollback and restore path. It moved to Ready in `9dce712`.
- Delivered and moved to Awaiting review in `dae10f2`, local on `main`, not pushed, not self-accepted. The `macos-pf` anchor now lets tailnet sources reach a port only at the Mac's own tailnet IPv4 and IPv6 addresses. Rig finds both addresses by pairing them on the one interface that carries Tailscale's ULA. It refuses when discovery is ambiguous, reports `tailnet-address-undiscoverable` and installs or rewrites nothing, and reports `tailnet-address-stale` when an address changes. The dry run and `show` print the addresses. The tests use an isolated `ifconfig` fixture, and the isolation helper now refuses `ifconfig`.
- Updated RIG-ORCH-023, RIG-STATE-045, ADR-KI-TOOL-RIG-009, the operational-resources guide, the manual and the changelog. They state the remaining on-link targeted case for TCP and UDP, use "tailnet-only" wording that promises no authenticated Tailscale ingress, and keep the advice to turn the listener off on untrusted shared networks. Added a pointer in KI-TOOL-RIG-CORE-047's Range correction. RIG-CONF-030 and the help text do not describe the match, so they are unchanged.
- Full test suite: 593 of 593 passed, and passed again with a planted `XDG_STATE_HOME` that stayed empty. Firewall tests: 13 of 13 passed. Shell gate: clean. `git diff --check`: clean. `ki repo audit --repo .`: no failures; its warnings come from earlier changes. No `SHELL-FATAL`. The pre-commit hook passed.
- A read-only `show` on `sol`, using a throwaway catalogue and stubbed `launchctl`, `sudo` and `pfctl`, names `100.90.130.74` and `fd7a:115c:a1e0::b636:824c`. Nothing was escalated or written. No live machine change was made.

## In Progress

- Nothing from this run. Another session committed `e651edb` (githooks) during the run and has an uncommitted edit to `docs/roadmap/KI-TOOL-RIG-CORE-048-signed-release-install-kind.md`. Both were left alone.
- Once this version of Rig is in use on `sol` and `terra`, their existing range-rule anchors will show `drifted (anchor-changed)` until an attended `rig apply --sudo`. That apply is a connection-critical rollout that needs Kris's separate approval.

## Queries

**Q-062-TERRA**

**Context:** The record's Verify asks for a read-only `ifconfig` on `terra`, which runs Homebrew `tailscaled`, to confirm the same discovery shape before any live apply. This run made no remote calls, so that check has not been done.

**Query:** How should the `terra` check be run before the attended rollout?

**Options:** a) (recommended, confidence high - it is read-only and is the only unconfirmed assumption) Run `rig show firewall:ID` or `/sbin/ifconfig` on `terra` at the start of the attended rollout session, before any `apply --sudo`. b) Launch a separate run with SSH read authority to check it beforehand. c) Accept the record on `sol`'s evidence alone.

### 🤖 → 👤 Handoff to supervisor · since 00:55 BST

👤 1 with you

- [with you] Q-062-TERRA · owner · since 00:55
- [committed] tools-rig main, unpushed
