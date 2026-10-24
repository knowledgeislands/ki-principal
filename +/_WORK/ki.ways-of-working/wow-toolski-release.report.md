# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-toolski-release

**🤖 → 👤 Handoff to supervisor · Run report at 02:23 BST · last mark 02:12 BST**

---

## Done

Tagged and published [v0.13.0](https://github.com/knowledgeislands/tools-ki/releases/tag/v0.13.0) at exactly `65e062737e3efaa696c5d92aaf2f8fc8bf31d1e9`; remote tag target verified.

Pre-tag checks: PASS, pinned commit is an ancestor of freshly fetched origin/main; v0.13.0 was absent locally and remotely; candidate version and Harness archive pin match the [dossier](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-day-toolski-pin.report.md).

Exact-commit CI: PASS, [run 39612182761](https://github.com/knowledgeislands/tools-ki/actions/runs/39612182761) completed successfully on the pinned commit.

Immutability: PASS, live repository setting enabled before tagging; the [publication job](https://github.com/knowledgeislands/tools-ki/actions/runs/39705072920/job/119583886638) verified the published release is immutable.

Publication: PASS, [release run 39705072920](https://github.com/knowledgeislands/tools-ki/actions/runs/39705072920) completed successfully; all three target builds passed, signed manifest and archive verification passed, and all five expected assets are published.

Clean installation: PASS, [Linux proof](https://github.com/knowledgeislands/tools-ki/actions/runs/39705072920/job/119584004962) installed v0.13.0 and bootstrapped its pinned Harness successfully.

Downstream notification: PASS, [Homebrew tap dispatch](https://github.com/knowledgeislands/tools-ki/actions/runs/39705072920/job/119584004984) completed successfully.

Scope: only the exact tag was pushed; no branch was pushed, no repository commit was created, and the primary checkout's working tree was untouched.

Install the published version:

```sh
curl -fsSL https://raw.githubusercontent.com/knowledgeislands/tools-ki/v0.13.0/install.sh | bash -s -- v0.13.0
```

## In Progress

Nothing is running.

Outstanding - no action requested now: the Homebrew tap owns its formula update; its merge and package-manager installation were outside this run's authorised calls and were not checked. This run did not update the owner's installed executable.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 02:23 BST

👤 1 handoff

- [handoff] Published tools-ki v0.13.0 with verified installation proof · supervisor · since 02:23 BST
