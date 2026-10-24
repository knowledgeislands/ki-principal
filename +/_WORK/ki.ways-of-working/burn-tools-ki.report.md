# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › burn-tools-ki

**🤖 → 👤 Handoff to supervisor · Run report at 06:11 BST · last mark 06:11 BST**

---

## Done

- [KI-TOOL-KI-CLI-134](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md): moved from in progress to awaiting review. `ki agent launch` and `ki agent queue` gained a repeatable `--allow fetch|machine` option, which appends the matching ki-delegation grant after the tier footer. The protocol line no longer mentions a reply block. Tests, manual, command inventory, README, user guide and CHANGELOG are updated, and the full review packet is in the record. Commit `a14a328d`. Coverage, tsc, biome, rumdl, knip, mandoc and the inventory check all pass. The repository audit fails only on ITEM-3 for KI-TOOL-KI-CLI-165, which is another session's record. Not pushed.
- [KI-TOOL-KI-CLI-152](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md): moved from complete-but-unreviewed to awaiting review. Its follow-up (`ki work message` and `ki work prune`) is now a messages line rather than a new record. Commit `907a627e`. Gates pass, with the same audit caveat. Not pushed.
- Follow-ups captured as lines in [ki.ways-of-working messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), commit `c15693e3` in ki-principal, not pushed:
  - CAPTURE-FOLLOWUPS: the `ki work message` and `ki work prune` commands from KI-TOOL-KI-CLI-152.
  - GRANT-INTERIM: remove the harness's interim grant sentence once a tools-ki release carries `--allow`.
- The worktree is removed, `run/burn-tools-ki` is deleted and the temporary folder is cleaned.

## In Progress

Nothing is running. These records were left, with the reason for each:

- [KI-TOOL-KI-CLI-165](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md) and [KI-TOOL-KI-CLI-167](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-167-knip-reads-committed-hooks.md) were already awaiting review, set by other sessions. 165's packet fails ITEM-3, and the composer-fix sessions are active on it, so I left it untouched.
- [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md) is on hold until 16 November, waiting for an ARM host.
- [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) is blocked on KI-HARNESS-GOV-199 Phase 1, which is in progress.
- [KI-TOOL-KI-CLI-159](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md) depends on KI-HARNESS-GOV-223, which is still a draft.
- [KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md) needs CI-run evidence for planning, and getting it takes a GitHub call this run could not make.
- [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md), [KI-TOOL-KI-CLI-140](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-140-git-hygiene-estate-audit.md), [KI-TOOL-KI-CLI-149](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-149-work-status-views-contract.md), [KI-TOOL-KI-CLI-157](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-157-validator-parity.md) and [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) each wait on a decision; see Queries.
- No record was stale, superseded or duplicated. Nothing was accepted or pruned.

## Queries

**1. Pushes held back**

**Context:** tools-ki main sits four commits above origin. Two of them are mine (`a14a328d`, `907a627e`). The other two belong to other sessions and are stacked beneath mine: `f2fdf227` from gpt-6.1-sol and `75427fa2` from GPT-6. ki-principal main sits 26 commits above origin, mostly other sessions' work, with my `c15693e3` on top.

**Query:** How should these be pushed?

**Options:** a) (recommended, confidence high - pushing mine would publish the other sessions' unreviewed work) Push each repository after the hook and ki.chezmoi sessions have landed or reviewed their commits. b) Push now, publishing everything stacked.

**2. Provisional choices in KI-TOOL-KI-CLI-134**

**Context:** I made three choices without a covering decision:
- The grant names are fixed as `fetch` and `machine`.
- The flag is spelt `--allow`.
- Grants are appended in the order given, after the footer.

All three are recorded in the record's Outstanding concerns.

**Query:** Do you confirm them during review?

**Options:** a) (recommended, confidence medium - they match the harness grant files) Confirm them as delivered. b) Change them during review.

**3. KI-TOOL-KI-CLI-139, the EBU SharePoint sync**

**Context:** The record needs three things this run could not supply. The first is a design choice between an acquire adapter and a new command group, which also brings a specification change. The second is the Chrome-cookie credentials. The third is ownership: the work belongs to the HNR Phase 3 Project.

**Query:** How should it be shaped?

**Options:** a) (recommended, confidence medium - it reuses the existing acquire pattern) Shape it as an acquire adapter in an attended planning session with the HNR Project. b) Shape it as a new command group.

**4. KI-TOOL-KI-CLI-140, the Git-hygiene estate audit**

**Context:** Its dependencies have landed. The CLEAN-1 to CLEAN-7 rubric items, however, live in the harness ki-git catalogue as judgment items.

**Query:** Where should the mechanical checks live?

**Options:** a) (recommended, confidence medium - the rubric already owns the criteria) Make them mechanical in the harness catalogue, and have tools-ki compose them with `mgit overview --json`. b) Implement them natively in tools-ki.

**5. KI-TOOL-KI-CLI-160 and KI-TOOL-KI-CLI-149, the work status views**

**Context:** 160's promotion condition is that State of play confirms the form it wants to read, and it has four open questions. 149 has open questions of its own: whether views carry full lines or keys, and whether v1 is retained.

**Query:** Should the work status records stay where they are until State of play confirms the form?

**Options:** a) (recommended, confidence medium - building first would pre-empt that decision) Have ki.tools-burndown ask State of play, then plan 160 as a `--view routing` option beside the text views. b) Plan both now on provisional choices.

**6. KI-TOOL-KI-CLI-157, validator parity**

**Context:** The work spans several repositories, and the home of the parity table has not been decided.

**Query:** Where should the parity table live?

**Options:** a) (recommended, confidence low - the specifications own the portable contracts) Keep it in ki-specifications. b) Keep it in tools-ki.

**7. KI-TOOL-KI-CLI-165 packet shape**

**Context:** Commit `f2fdf227` left 165's review packet failing ITEM-3, which makes the tools-ki audit fail.

**Query:** Who should fix the packet?

**Options:** a) (recommended, confidence high - the record is theirs) Leave it to the composer-fix session to fix before review. b) Have a later run fix it.
