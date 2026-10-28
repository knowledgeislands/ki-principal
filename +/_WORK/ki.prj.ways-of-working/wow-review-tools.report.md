# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-review-tools

**🤖 → 👤 Handoff to supervisor · Run report at 23:12 GMT · last mark 01:07 GMT 25 October**

---

## Done

- Independent blind review completed; commits: none; repositories unchanged.
- Dependency and lockfile checks: the Context's claim that all required tools are pinned is false in all three local checkouts.
- Binary checks: hnr-principal lacks all five commands; legal-principal has rumdl and syncpack; apps-yorkphotosoc.org has lint-staged and commitlint.
- Canonical hook check: missing package-local commands cause refusal, confirming that installing the hook before resolving its prerequisites would block commits.
- Authority check: the software rule permits upgrades of installed tools and prohibits new installations; a lockfile is not an installation grant.
- Live GitHub checks: not performed under the no-remote-call rule; the reported settings failures remain unverified.
- Blindness check: no queries.md, decisions.md or report in the ways-of-working work folder was read; no installation, hook execution or remote call was made.

## In Progress

Nothing running. The follow-up convergence remains with the coordinator; this review authorises no changes.

## Queries

### MISSING-TOOLS - Populate the missing hook tools?

**Context**

The next ki release already requires a second convergence, and hnr-principal was reported to have another session working in it. More importantly, the proposed frozen install does not match the local dependency state as of 23:12 GMT on 26 October 2026: [hnr-principal's manifest](/Users/krisbrown/workspaces/humans-not-robots/hnr-principal/package.json:1) has no development dependencies and its root has no lockfile; [legal-principal](/Users/krisbrown/workspaces/legal/legal-principal/package.json:18) has package-lock.json, pinning rumdl and syncpack but lacking lint-staged, Biome and commitlint; [apps-yorkphotosoc.org](/Users/krisbrown/workspaces/techmedix/apps-yorkphotosoc.org/package.json:33) uses yarn.lock and declares Yarn, with lint-staged and commitlint but no Biome, rumdl or syncpack entries. None has a Bun lockfile. The Context's assertion that each repository already pins all the required tools, and that one frozen Bun install can therefore populate them without lockfile changes, is unsupported and materially wrong. I did not verify the reported concurrent session or live GitHub settings.

In my reading, installing a previously uninstalled tool falls **inside the prohibition** on installing new software, even when its version appears in a lockfile. A frozen lockfile constrains dependency resolution; it does not establish prior installation or owner permission. Restoring a demonstrably existing installation could be maintenance, but the brief supplies no such evidence, and the missing dependency declarations require more than restoration here. Deferral does not itself grant permission to install them later.

**Query**

Should a follow-up run populate node_modules from the lockfile in these three repositories and then converge their hooks?

**Options**

a) (recommended, confidence high - the proposed install cannot supply the undeclared tools, the software rule provides no exception, and another convergence is already planned) Leave them until the second convergence after the next ki release. Recheck dependency prerequisites then, wait for hnr-principal's other session to finish, and obtain an explicit owner decision before introducing missing tools. Resolve permitted GitHub settings prerequisites within that later run's authority.

b) Yes, run bun install --frozen-lockfile in all three now and converge their hooks. This requires a corrected dependency plan and explicit authority to introduce missing tools; the stated command alone is insufficient and overlaps hnr-principal's reported active session.

c) Yes, but only after hnr-principal's other session has finished, and as part of the second convergence. This improves timing but still pre-authorises an installation whose prerequisites and permission have not been established.

### 🤖 → 👤 Handoff to supervisor · since 23:12 GMT

🤖 0 running · 👤 1 with you · ⛔ 0 blocked

- [with you] MISSING-TOOLS recommendation · supervisor · since 23:12 GMT

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
