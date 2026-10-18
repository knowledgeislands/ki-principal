# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › release-ki

**🤖 → 🧑 Handoff to supervisor · Run report at 10:11 BST · last mark 10:06 BST**

---

## Done

- Accepted all ten records as done, citing TOOLS-SITTING a) from the [decisions log](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/decisions.md) ("owner answers, batch 5"): [KI-TOOL-KI-CLI-123](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-123-agent-run-events.md), [KI-TOOL-KI-CLI-130](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-130-skill-generated-surfaces.md), [KI-TOOL-KI-CLI-133](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-133-retired-reports-come-back.md), [KI-TOOL-KI-CLI-135](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-135-reused-agent-name-overwrites.md), [KI-TOOL-KI-CLI-137](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-137-agent-run-tmp-home.md), [KI-TOOL-KI-CLI-138](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-138-warn-unknown-record-fields.md), [KI-TOOL-KI-CLI-141](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-141-granola-screenshots-markers.md), [KI-TOOL-KI-CLI-142](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-142-preserve-harness-release-settings.md), [KI-TOOL-KI-CLI-143](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-143-separate-local-harness-paths.md) and [KI-TOOL-KI-CLI-144](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-144-older-runs-start-seen.md) (64b4bee8). Each record's independent review of 18 October said "ready for acceptance", and each review packet was complete. The Done notes on -142 and -143 say that the Terra and Sol live checks follow through the chezmoi handoff under HARNESS-PATHS-LIVE a).
- COMPOSE-REPLY-BLOCK is now in [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md): a Discussion note, Requirement 1, an open Step and Verify 5, all to remove "with the reply block" from the launch prompt (19a633c8). Nothing was built, and the record stays in progress.
- The harness pin moved from ebc05eb to 4cae8271, with its archive digest checked, in its own fix(bootstrap) commit (61c030be). This follows the release guide, as v0.11.0 did: the harness had moved 13 commits.
- v0.11.1 is released. Tag `v0.11.1` is on 857d53ca ("chore(release): prepare v0.11.1"). The release is published, immutable and signed, with three archives. All seven release-workflow jobs passed, including the clean Linux install and the Homebrew tap notice.
- It carries the ten accepted records above, plus the new harness pin.
- The Homebrew tap opened and merged its formula update itself ([homebrew-tap #43](https://github.com/knowledgeislands/homebrew-tap/pull/43), b42be8b1). The tap's post-merge CI passed, including its notice to release consumers.
- Installed on this Mac: `brew upgrade` moved Homebrew's ki from 0.11.0 to 0.11.1. `/opt/homebrew/bin/ki --version` prints `0.11.1`, and `ki doctor` passes 17 checks.
- Pushed main fast-forward: four commits, all mine, after a rebase pull. Origin had not moved, and no other session's commits were included.
- No npm or other public-registry publish was part of the process, so nothing needed asking.
- Checks:
  - Tests and coverage pass (1334 tests).
  - tsc, biome, knip and the manual lint pass.
  - `ki repo audit` has no failures and the same two warnings as before.
  - CI on main passed before tagging.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The Terra and Sol live checks for -142 and -143 run on both Macs under the chezmoi handoff (HARNESS-PATHS-LIVE). v0.11.1 is now installed here.
- On this Mac, `ki` on PATH resolves first to the local-development runner at `~/.local/bin/ki`, which runs from the checkout and also prints 0.11.1. Homebrew's copy comes later on PATH.
- The new harness pin carries harness work that is not yet accepted: [KI-HARNESS-GOV-211](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-211-bats-fatal-assertions.md) is awaiting review. [KI-HARNESS-GOV-175](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-175-delegation-run-events.md) and [KI-HARNESS-GOV-199](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-199-thread-identity-role-native-sessions.md) are in progress. The pin itself follows the release guide.
- The progress protocol makes this the only report path, so nothing was committed in ki-principal.

## Queries

None.
