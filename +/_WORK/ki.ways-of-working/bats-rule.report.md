# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › bats-rule

**🤖 → 🧑 Handoff to supervisor · Run report at 09:48 BST · last mark 22:34 BST**

---

## Done

- The `ki-repo-tools` standard, skill summary and sources now carry the TEST-FATAL rule: every `[[ ]]` or `!` assertion in a shell tool's Bats suite ends `|| false`, because under macOS Bash 3.2 a failing one in the middle of a test does not fail it. tools-mgit `00ef0de` is cited as the evidence.
- The checker now has a new WARN criterion, `SHELL-FATAL`. It reports each `tests/*.bats` suite that has such an assertion without `|| false`, giving the count and the first line numbers. It is line-based: it joins continuation lines, skips comments, and leaves `&&`/`||` control-flow lines alone.
- The generated rubric is current. The one other surface it touched is a pinned criterion count in `ki-skills`' remediation-inventory test, which rose by one. That is recorded as an approved deviation in the review packet.
- [KI-HARNESS-GOV-211](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-211-bats-fatal-assertions.md) was captured under ki-next, planned to Ready under ki-plan, and delivered to Awaiting review under ki-implement. Its review packet is complete, its reviewer is still pending, and nothing was accepted.
- There are four harness commits: `e6b72541` (ledger reservation), `1d7c2895` (capture), `a7b3d17a` (plan) and `4190c555` (delivery). Each went through the pre-commit gate, and all four were pushed fast-forward to origin `main`. There were no other sessions' commits beneath them.
- Checks:
  - `bun run test`: pass, 1248 tests.
  - `bunx tsc --noEmit`: pass.
  - `ki repo audit --skill ki-authoring` and `--skill ki-work-roadmap`: pass.
  - `ki repo audit --skill ki-skills`: no failures. Its three warnings are date-driven refresh-cadence findings in other skills' `sources.md`, not part of this change.
- Run against tools-mgit, `tests/mgit.bats` (the suite `00ef0de` fixed) passes `SHELL-FATAL`.
- I searched the workspaces and the chezmoi source read-only. Only two repositories have Bats suites, and these would get the warning (every sampled line is a genuine bare `!` or `[[` assertion):
  - tools-mgit: `tests/territory-producer.bats` (6 lines) and `tests/territory-protocol.bats` (1 line).
  - tools-rig, 9 suites with 64 lines in all:
    - `tests/rig.bats` (17)
    - `tests/rig-app-clis.bats` (17)
    - `tests/rig-application-updates.bats` (8)
    - `tests/rig-default-applications.bats` (7)
    - `tests/rig-software-removal.bats` (7)
    - `tests/rig-skills.bats` (4)
    - `tests/rig-macos.bats` (2)
    - `tests/rig-homebrew-authority.bats` (1)
    - `tests/rig-human-config.bats` (1)
- This report was written only to this path, not to `+/_WORK/ki.ways-of-working/bats-rule.report.md` in ki-principal. The progress protocol says its report path overrides any other the brief names, so nothing was committed in ki-principal.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [KI-HARNESS-GOV-211](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-211-bats-fatal-assertions.md) needs an independent review, then acceptance under ki-accept.
- No release was made. Other repositories' audits show `SHELL-FATAL` only through a `ki` that loads this harness revision.

## Queries

### BATS-CLEANUP - How to route the clean-up of the 11 warning suites

**Context:** The rule landed for every Bats suite, but tools-mgit's two smaller suites and nine of tools-rig's suites still carry 71 non-fatal assertions between them. As in `00ef0de`, making those assertions fatal may expose latent test faults that each repository's owner then has to fix. This run edited neither repository.

**Query:** Should each repository get a triage record so the clean-up is tracked, or should it be left to happen ad hoc?

**Options:**
a) (recommended, confidence medium - a record keeps the warnings from being lost, and capture needs no adoption authority) Capture one triage record in tools-mgit and one in tools-rig, each listing its warning suites and citing `00ef0de`.
b) Leave the warnings in the audit output, and let each owner clean up when they next touch the suites.

### 🤖 → 🧑 Handoff to supervisor · since 09:48 BST

🧑 2 with you

- [with you] BATS-CLEANUP · owner · since 09:48
- [with you] KI-HARNESS-GOV-211 review and acceptance · owner · since 09:48
- [committed] ki-agentic-harness, pushed
