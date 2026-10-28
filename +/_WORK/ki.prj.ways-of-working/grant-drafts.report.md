# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › grant-drafts

**🤖 → 🧑 Handoff to supervisor · Run report at 11:01 BST · last mark 10:53 BST**

---

## Done

- Drafted [grant-fetch.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/assets/grant-fetch.md) and [grant-machine.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-delegation/assets/grant-machine.md) in the ki-delegation assets folder, where [KI-HARNESS-GOV-201 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) says they live, in the shape approved on 16 October under FOOTER-GRANTS: each a harness-owned section, appended after the tier footer, that lifts only its matching ban.
- Each draft is marked unapproved twice: in a note above its section and in the first line of the section itself, so it would grant nothing even if appended by mistake. Nothing wires them in: the standard's tier table, the sources note, the rubric and the launcher do not name them, and `ki agent` has no `--allow` option yet.
- Added a Discussion note to [KI-HARNESS-GOV-201 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md) recording CLI134-GRANTS a) and where the drafts sit. The record stays in triage.
- Commit `0d0c3e8d` in ki-agentic-harness, pushed fast-forward to origin with only my commit above it. `bun run test` passed, `bunx tsc --noEmit` passed, focused audits for ki-delegation, ki-authoring and ki-work-roadmap passed, and the pre-commit gate passed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [KI-TOOL-KI-CLI-134 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/f4811dd9310b48d8809d9143ca8864fc7b4be5e2/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) stays in progress until the wording is approved and adopted.
- This report is written only to the state-folder path, because the launch protocol says that path governs any other the brief names. It is not in the work folder.

## Queries

### GRANT-WORDING - approve or amend the two grant texts

**Context:** These texts set how much authority a run gets under `ki agent --allow fetch` and `--allow machine`. Each one overrides one ban in the tier footer and leaves the rest standing. On the record's three planning questions, the drafts take these positions. First, `machine` points to the connection-critical rule and says it still applies, but does not repeat it, because every tier footer already carries it. Second, each grant is limited to what the brief names: the remotes for a fetch, defaulting to `origin`, and the specific changes for a machine grant. Third, `fetch` adds nothing under the `push` tier and does no harm there, while `machine` fits every tier. Two choices are yours to make: `machine` lets a named install download from its own package source, because an install cannot run without that, and credential changes stay banned under both grants. Approving the wording means a harness run then removes the draft lines, adds both grants to the standard beside the tier table, records them in the sources note and adds a rubric check, and [KI-TOOL-KI-CLI-134 (pruned)](https://github.com/knowledgeislands/tools-ki/blob/f4811dd9310b48d8809d9143ca8864fc7b4be5e2/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) becomes Ready.

The full draft of `grant-fetch.md`:

```markdown
# Authority grant: fetch

> **Draft, not approved.** This wording awaits Kris Brown's review under [KI-HARNESS-GOV-201](../../../../docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md). No launcher reads this file, the background-run standard does not list it, and it grants nothing until its wording is approved.

Once approved, `ki agent launch --allow fetch` appends this file from `## Grant: fetch` onwards, after the tier footer. See the [background-run standard](../references/standards-background-runs.md#authority-tiers).

## Grant: fetch

- **Draft, not approved: this grant is not in force, and the Rules above stand unchanged.**
- Fetching is authorised by the decision this task cites: you may run `git fetch`, and `git pull --rebase --no-autostash` or `git pull --ff-only`, from the remotes the task names, or from `origin` where it names none. This overrides only the Rules' ban on a Git fetch; every other line of the Rules stands.
- A fetch or pull may update remote-tracking branches and replay your own local commits; it never authorises a push, a force-push, a stash, a reset of shared `main`, or resolving a conflict in another session's work. If a pull refuses or conflicts, stop and report.
- Every other remote call stays banned: no push unless your tier or task grants one, and no GitHub API, cloud, network or messaging call. Under a tier that already allows `git fetch`, this grant adds nothing.
```

The full draft of `grant-machine.md`:

```markdown
# Authority grant: machine

> **Draft, not approved.** This wording awaits Kris Brown's review under [KI-HARNESS-GOV-201](../../../../docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md). No launcher reads this file, the background-run standard does not list it, and it grants nothing until its wording is approved.

Once approved, `ki agent launch --allow machine` appends this file from `## Grant: machine` onwards, after the tier footer. See the [background-run standard](../references/standards-background-runs.md#authority-tiers).

## Grant: machine

- **Draft, not approved: this grant is not in force, and the Rules above stand unchanged.**
- Machine changes are authorised by the decision this task cites: you may make the local environment and scheduler changes the task names, such as a package install or update, a configuration or dotfile edit, or loading, reloading or unloading a scheduled job, on this machine only and nothing beyond them. This overrides only the Rules' ban on an environment or scheduler change; every other line of the Rules stands.
- A named install or update may download what it needs from its package source. No other remote call is lifted, and a change on another machine is a remote call.
- Before each change, note how to undo it; after it, check that it took effect. Report each change with its outcome and its undo in one line.
- Credentials stay banned: make no credential change, and do not read or print secrets. A connection-critical change still needs the tested restore path the Rules require, under the standard's [connection-critical rule](../references/standards-background-runs.md#connection-critical-changes); without one, stop and report.
- If a change the task does not name proves necessary, or a named change needs a step the task does not name, stop and report rather than widen it.
```

**Query:** Do you approve both grant texts as drafted, or which amendment do you want?

**Options:**

a) (recommended, confidence medium - the drafts follow your 16 October shape and keep every other ban, but the wording of a grant is your call) Approve both as drafted, and a harness run adopts them under [KI-HARNESS-GOV-201 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-201-fetch-and-machine-grants.md).

b) Approve with `fetch` widened to also allow reading the public web pages the task names, such as an upstream source refresh, with no other network call.

c) Approve with `machine` narrowed so that a named install may not download anything, which means an install would need a separate network grant.

d) Amend the wording yourself, in speech, before anything is adopted.

### 🤖 → 🧑 Handoff to supervisor · since 11:01 BST

🧑 1 with you

- [with you] GRANT-WORDING · owner · since 11:01
- [committed] ki-agentic-harness, pushed
