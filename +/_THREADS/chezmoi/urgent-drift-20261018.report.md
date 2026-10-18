# [Rig](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/rig.md>) › [chezmoi](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md>) › urgent-drift-20261018

**Run report at 02:38 BST · last mark 15:59 BST (15 October 2026)**

---

## Done

Applied only `.claude/communication.md`, `.claude/delegation.md` and `.codex/AGENTS.md` under the existing CHEZMOI-APPLY instruction and the owner's urgent timing override. Exact source comparison against `d1a6e6d` passed for all three; live rendered-byte equality and scoped status passed after apply. Scripts were excluded and external refresh disabled. The other cited commits `673b999` and `d81a80c` contain roadmap reservation/capture, with no additional target changes.

Inspected the exact source, history and non-secret scoped diff for all seven targets. Retained the [owner review](</Users/krisbrown/.local/state/ki/agents/chezmoi/urgent-drift-20261018.review.md>) and [exact diff](</Users/krisbrown/.local/state/ki/agents/chezmoi/urgent-drift-20261018.scoped-review.diff>) locally while review is pending. No global diff or secret rendering was used.

Verified Sol's live Rig default is studio, inheriting core, while HNR email route triage belongs only to laptop: it is not selected on Sol. Its native launchd label is not loaded and its plist is absent. Copying its executable alone neither runs it nor schedules it; later explicit execution could mutate mailbox routing/read state, update HNR notes, create explicit-path commits and record reports/notifications. No email-send tool is granted by the wrapper. The full effects and exact proposed commands are in the retained review.

Read every doctor finding: exit 1, two findings - UTM MAS source mismatch and Headroom port ownership conflict. Both remain untouched because installation and Headroom changes are outside this authority. This is not a passing health gate; no Rig declaration was applied and no after-apply result is claimed.

Source Git remains clean and level with the existing origin/main tracking ref; no source edit, source commit or source publication was needed. Live drift reduced from seven targets to the four listed below. No source Git locks remain. Existing SSH evidence, held source work, checkpoint and other-session decisions-log edits were preserved. Wrap-ways had reached DONE before this report was written.

Report Markdown and whitespace checks pass. The local review also passes Markdown checks under the chezmoi configuration; its first check used the state folder's default line limit and was rerun with the repository's intended configuration.

Roadmap inspection found a pre-existing duplicate identifier between [Gmail routing](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-configure-gmail-routing-paths.md>) and [thread identity registration](</Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-096-thread-identity-hook-registration.md>); it was not changed. Source implementation gates were not run because no source changes or commits were made.

## In Progress

Waiting for owner review of `.config/rig/conf.d/50-services.toml`, `bin/scheduled/rig-hnr-email-route-triage`, `workspaces/personal/.mgit.toml` and `workspaces/personal/dotfiles`. No scheduler, service, credential, firewall, SSH or Headroom change is in progress. The wrapper has not been executed and Rig apply remains held.

Outstanding - no action requested now: the wider source restart remains parked under its existing prerequisites; this urgent drift exception grants no feature work or resumed source delivery.

## Queries

### DRIFT-APPLY - Review the four remaining targets

**Context:** The approved guidance is already applied and verified. The [review artifact](</Users/krisbrown/.local/state/ki/agents/chezmoi/urgent-drift-20261018.review.md>) contains the exact diff, every functional effect and proposed apply/verification commands for the four remaining targets. They add a laptop-only HNR job declaration, copy its executable and register/link the existing dotfiles repository in the personal workspace. The job is not selected or loaded on Sol; copying the files does not execute it. Repository AGENTS.md requires reviewed explicit approval, and no existing approval demonstrably covers these four changes.

**Query:** Approve the four-target apply and read-only verification in the artifact?

**Options:**

a) (recommended, confidence high - the scoped diff and Sol's non-selection were verified directly) Apply only the four reviewed targets with scripts excluded and external refresh disabled, then verify exact target/source equality, executable/link state, absent launchd job and before/after doctor findings; do not execute the wrapper or run Rig apply.

b) Leave the four targets pending and retain the review artifact.

```text
DRIFT-APPLY
Apply only the four reviewed targets with scripts excluded and external refresh disabled, then verify exact target/source equality, executable/link state, absent launchd job and before/after doctor findings; do not execute the wrapper or run Rig apply.
```

```text
╭─ run report · 2026-10-18T01:38:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █  █ █▀▀▀ █  █   · worker awaiting review │
│  █▀▀▄ █  █ ▀▀▀█ ▀█▀    · guidance applied      │
│  █▄▄▀ ▀▄▄▀ ▄▄▄█  █     · four targets pending  │
│                                                  │
╰──────────────────────────────────────────────────╯
- [waiting] DRIFT-APPLY owner review; worker remains active
- [done] three approved guidance targets applied and verified
- [held] Rig apply and all wider source delivery
- [preserved] previous SSH evidence and other-session work
```
