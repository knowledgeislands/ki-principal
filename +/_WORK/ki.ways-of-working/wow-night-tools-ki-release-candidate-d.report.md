# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-night-tools-ki-release-candidate-d

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 05:11 BST · last mark 01:40 BST**

---

## Done

Prepared a bounded incomplete dossier. There is no ready release candidate. Stopped at the first proved release blocker: [package.json](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/package.json:4) still declares `0.12.0`, and the existing lightweight `v0.12.0` tag identifies the earlier released source. No repository file, index, branch, worktree, tag, remote, credential or environment was changed. No command contacting a remote was run. No commits were made by this run; there is no own-commit push or integration handoff.

### Frozen identity and release need

Repository: `/Users/krisbrown/workspaces/knowledge-islands/tools-ki`, machine `sol.local`, branch `main`.

Proposed exact version: `v0.13.0`, a recommendation for the accumulated capability and pre-1.0 breaking changes, not an approved or prepared release marker. Its availability is established only against local tags; remote availability was not queried. This proposal does not make the source eligible for that tag.

Previous released tag: `v0.12.0`; tag object type `commit` (lightweight); peeled SHA `056ef85f825edf4a4de7d79bb1d8c025e752af03`. The accepted record retains factual publication and clean-install evidence for that release; it is historical proof, not proof of a new release.

Observed source SHA: `566679b2cb7648a0746d745aa29a297cd1b3eaf2`. This is the immutable main snapshot examined, not a future prepared SHA and not a ready candidate. Complete proposed inclusion range: `056ef85f825edf4a4de7d79bb1d8c025e752af03..566679b2cb7648a0746d745aa29a297cd1b3eaf2`, 60 commits. The working tree and index were clean at inspection. The [frozen source and complete per-commit changed-path inventory](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-tools-ki-release-candidate-d.work/frozen-source-and-range.json) retains every full commit ID, parent, subject and actual changed path, plus hashes of the version, pin, workflow and release-guide sources. Release authority for the earlier included changes is explicitly unestablished, rather than inferred from their presence on main.

A concrete release need exists beyond accepting the CI repair: a released executable carrying agent `--allow` would enable removal of GRANT-INTERIM once that release is installed. The range contains `a14a328d532ffc61e1bf5af76ffef0184f191b5a`, adding that capability. Accumulated changes also include Git message checking, territory membership reporting, hook convergence, acquisition changes, worktree ownership and completion fixes. Whether the entire range is approved to ship remains a separate missing pre-tag review.

### Named-record acceptance

[KI-TOOL-KI-CLI-156](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-156-ci-runs-local-gate.md:128) is retained as `done`. Implementation `fcbaf5105eee4b6804a6e251781e454f2ff868d9`, review packet `a859371c6701f9c58b2930ceefdbb524019dd20e`, and independent acceptance `566679b2cb7648a0746d745aa29a297cd1b3eaf2` are included. The [actual acceptance report](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-cli-156-accept-d.report.md) records the independent review and closure under the named overnight grant. This run inspected the record and report after their completed outcome; the historical dependency name was not treated as current waiting authority.

That acceptance covers the CI pin repair and its guard, not the preceding 57 commits. Their complete substantive review, per-record acceptance mapping, and review authority have not been established by this run. The range inventory is evidence of inclusion only. No claim that all accepted work, or only accepted work, is included is made.

### Available and missing proof

Source identity and clean checkout: PASS, frozen local main above; no touched repository paths.

Acceptance dependency: PASS, named record retained done with independent acceptance on local main.

Version/tag alignment: BLOCKED, source still reports package version `0.12.0`, already released as `v0.12.0`; proposed `v0.13.0` has no matching committed version preparation.

Harness alignment: INCOMPLETE, [src/core/storage/registry.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/registry.ts:25) still pins Harness `f4d6c521ef4859dc8965579bc39a5575004e3ac5`, digest `004d7fa408e63036558879ef101207b7f71b6567b3a35383da4a570d0e6e07f9`. Local Harness main was `7378f88a323454339ae61bab6bd1bdb03104a8eb`. The release guide requires a separate bootstrap-pin commit when the Harness has moved; no new revision/digest preparation was authorised or performed here. A selected revision and verified archive digest remain required, not inferred from the current Harness main name.

`bun run test`: NOT RUN in this unit, stopped at the version blocker; predecessor success is not a gate on this frozen SHA.

`bunx tsc --noEmit`: NOT RUN in this unit, same stop boundary.

`bunx biome check`: NOT RUN in this unit, same stop boundary.

`ki repo audit --repo .`: NOT RUN in this unit, same stop boundary. The offline audit-home README, including Capital, territory and Project registries, was read; no audit activation was attempted. Predecessor CI-1 and MATURITY-1 warnings are historical only, not a fresh audit result.

`bun run test:coverage`: NOT RUN in this unit; the proposed range includes behaviour changes and requires exact-candidate coverage.

Manual lint, rendered manual, command inventory, help/completion/guide/CHANGELOG parity: NOT VERIFIED for this release range. CLI-156 alone changes no grammar; that does not exempt preceding grammar changes. No generated source was rewritten.

Installer and archive version alignment: NOT VERIFIED on a prepared candidate. The installer accepts an exact positional version and the release guide names three archives containing the executable and manual; no compiled archive or disposable installation was exercised in this stopped unit. The source marker currently prevents alignment with `v0.13.0`.

Exact-candidate CI: PENDING. The saved factual [CI run](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-tools-ki-release-candidate-d.work/ci-run.raw.json) and [build job](/Users/krisbrown/.local/state/ki/agents/ways-of-working/wow-night-tools-ki-release-candidate-d.work/ci-jobs.raw.json) identify head `a859371c6701f9c58b2930ceefdbb524019dd20e`, not `566679b2cb7648a0746d745aa29a297cd1b3eaf2`. Workflow [CI run 39540918234](https://github.com/knowledgeislands/tools-ki/actions/runs/39540918234) succeeded, created `2026-10-21T03:52:05Z`, updated `2026-10-21T03:53:47Z`; [build job 119028204835](https://github.com/knowledgeislands/tools-ki/actions/runs/39540918234/job/119028204835) succeeded from `2026-10-21T03:52:07Z` to `2026-10-21T03:53:46Z`. These are prior-head results only. No already available exact-main result was supplied by the accepted run, and no GitHub query was made. A later prepared SHA will require its own matching evidence.

Public-channel reachability, repository immutability setting and peer advisory snapshot: NOT freshly verified; this unit has no remote-read grant for these checks. Historical release success is not current configuration proof. Any missing required pre-tag setting/reachability evidence must return through a separately authorised read, without credential or environment inspection.

### Breaking changes and preparation files

The range includes breaking acquisition commit `26c754f3` (`feat(acquire)!: drop Granola ledger and dedupe on Acquired membership`). Migration and compatibility notes for this and the remaining product changes require substantive review. No statement that there are no migrations is justified.

Known remaining preparation paths are [package.json](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/package.json:4) for the exact unused version and [src/core/storage/registry.ts](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/src/core/storage/registry.ts:25) for the selected immutable Harness revision and verified digest. [CHANGELOG.md](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/CHANGELOG.md), [man/ki.1](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/man/ki.1), [man/ki.commands.json](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/man/ki.commands.json), help, completions and affected user guides require range-wide parity review; this run has not established that any of those require an edit. [install.sh](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/install.sh) takes the version argument, so no independent hard-coded installer version bump is inferred. This unit authorises none of these edits.

### Concrete publication calls, written only

The local [release workflow](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/.github/workflows/release.yml:4) has `workflow_dispatch.inputs.version`. Its validation rejects a dispatch from a non-default branch, fetches the requested exact tag, rejects a package-version mismatch and requires the tagged commit to be an ancestor of the default branch. This matches the supplied `--ref main` contract when main remains the default branch. No live default-branch or environment setting was inspected.

The following is a frozen, deliberately guarded illustration of the requested lightweight-tag, non-force tag-push and workflow calls, with the proposed exact tag and the only observed SHA. It was never executed. The first check fails on today's source, so these calls do not constitute a ready publication instruction. After authorised preparation, the coordinator must replace this dossier with the actual new committed SHA and rerun every pre-tag proof; never remove the guard to tag this snapshot.

```sh
test "$(git show 566679b2cb7648a0746d745aa29a297cd1b3eaf2:package.json | node -p 'JSON.parse(require("node:fs").readFileSync(0, "utf8")).version')" = '0.13.0' &&
git tag v0.13.0 566679b2cb7648a0746d745aa29a297cd1b3eaf2 &&
git push origin v0.13.0 &&
gh workflow run release.yml --repo knowledgeislands/tools-ki --ref main -f version=v0.13.0
```

The workflow, rather than a separate `gh release create` instruction, owns archive builds, signing, asset verification and publication. No tag, push, dispatch, signing or publication command was executed.

<details>
<summary>Complete frozen commit range, oldest first</summary>

- `b32a5e5a6f752c5686bbf3e27ff4b77d16b3a968` - docs(roadmap): plan [KI-TOOL-KI-CLI-161](https://github.com/knowledgeislands/tools-ki/blob/b32a5e5a6f752c5686bbf3e27ff4b77d16b3a968/docs/roadmap/KI-TOOL-KI-CLI-161-git-check-message.md) to Ready
- `1baef5254633672e3e83ec4dfed048754b87723c` - docs(roadmap): reduce [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-125-ki-release-contract.md)'s hold to an ARM host being needed
- `17097fa899e78acdcf60364098a4fbfd3204115f` - feat(git): add ki git check-message
- `0ae33c9287ac88993b90592e0a81f5cce440a561` - fix(repo): follow a symlinked --repo to its real location
- `c5168f3e11ec48d1937fa50ce0be8918e48d6327` - docs(roadmap): plan [KI-TOOL-KI-CLI-154](https://github.com/knowledgeislands/tools-ki/blob/c5168f3e11ec48d1937fa50ce0be8918e48d6327/docs/roadmap/KI-TOOL-KI-CLI-154-territory-tolerates-unregistered-members.md) to Ready
- `be5c6ddf5cd9a347ccc0d2fdbb996ddd3e75bd6b` - feat(territory): report unregistered members in show and audit
- `f0cc4012a8932538cc29bae4824c00ce20b48672` - docs(roadmap): adopt and plan [KI-TOOL-KI-CLI-164](https://github.com/knowledgeislands/tools-ki/blob/f0cc4012a8932538cc29bae4824c00ce20b48672/docs/roadmap/KI-TOOL-KI-CLI-164-estate-hook-binding-sweep.md) to Ready
- `7a70dea383956ac56b5e4e201ef9257850ceefb0` - fix(roadmap): record [KI-TOOL-KI-CLI-154](https://github.com/knowledgeislands/tools-ki/blob/7a70dea383956ac56b5e4e201ef9257850ceefb0/docs/roadmap/KI-TOOL-KI-CLI-154-territory-tolerates-unregistered-members.md) baseline as a full commit id
- `4cd8e0d0ea3ee586408aac4c6bc4902637ab34dc` - feat(estate): bind registered checkouts to tracked hooks with converge --hooks
- `23808b9877ca778278e3e1d0722d1514320a7fff` - docs(roadmap): record GRANOLA-CHECKPOINT on [KI-TOOL-KI-CLI-166](https://github.com/knowledgeislands/tools-ki/blob/23808b9877ca778278e3e1d0722d1514320a7fff/docs/roadmap/KI-TOOL-KI-CLI-166-granola-acquired-folder-alone.md)
- `708a3b3266eaed05cda82a355c13ab03d0fc1640` - docs(roadmap): adopt and plan [KI-TOOL-KI-CLI-152](https://github.com/knowledgeislands/tools-ki/blob/708a3b3266eaed05cda82a355c13ab03d0fc1640/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md) to Ready
- `22ee06099877d70ac0c52d982f70252dad6e3be5` - fix(agent): read every decisions-log entry and write unnumbered decisions
- `d85ca18c45bf50bd69b084c231d7288f86d71b2b` - docs(roadmap): adopt [KI-TOOL-KI-CLI-165](https://github.com/knowledgeislands/tools-ki/blob/d85ca18c45bf50bd69b084c231d7288f86d71b2b/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md) at Soon
- `ce905bee422605f2f7c7c4c2d94819582f0c56b8` - docs(roadmap): shape [KI-TOOL-KI-CLI-165](https://github.com/knowledgeislands/tools-ki/blob/ce905bee422605f2f7c7c4c2d94819582f0c56b8/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md) as a Soon draft
- `86298d3fe62ad03552cfee14d52fd613fc4a779a` - docs(roadmap): size four open work records
- `19c100671bed3eba1e2cc8cf9ff17973c9e48883` - docs(roadmap): accept four records and return two failed reviews
- `3457c0ad9b86acafcbc13362d971d00bbd927a2b` - docs(roadmap): pin tools-ki references before pruning
- `2ad0f74a34dfcdb7e87afc9fb2037b3c7cbf2935` - chore(roadmap): prune 4 done work records
- `26c754f3a387559a80b7f465cb453982b2865ade` - feat(acquire)!: drop the Granola ledger and dedupe on Acquired membership
- `ee40f26565fd3852a067164dab564e0f4745d23c` - docs(roadmap): repoint [KI-TOOL-KI-CLI-139](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-139-ebu-sources-sync.md) to the Humans Not Robots Phase 3 Project
- `a1fdecb4114eb6e6316ba0ad7722cb431681f10b` - docs(roadmap): cancel [KI-TOOL-KI-CLI-151](https://github.com/knowledgeislands/tools-ki/blob/a1fdecb4114eb6e6316ba0ad7722cb431681f10b/docs/roadmap/KI-TOOL-KI-CLI-151-cli-conventions-departures.md) as a standing message
- `949cd36a6ac5b0d9b04be5982fa9cd840eddf60e` - docs(roadmap): return [KI-TOOL-KI-CLI-167](https://github.com/knowledgeislands/tools-ki/blob/949cd36a6ac5b0d9b04be5982fa9cd840eddf60e/docs/roadmap/KI-TOOL-KI-CLI-167-knip-reads-committed-hooks.md) to awaiting review
- `f2fdf22721ded0a9871bc93ece957332885d9a17` - feat(repo): conform canonical shape hooks
- `75427fa2d0cb769cc3c81ffe19edcfb5d8ced28c` - fix(repo): refuse unsafe hook migration targets
- `a14a328d532ffc61e1bf5af76ffef0184f191b5a` - feat(agent): append --allow grant sections after the footer
- `907a627ef407513ef560fce4b1f7ba103d60d7e5` - docs(roadmap): return [KI-TOOL-KI-CLI-152](https://github.com/knowledgeislands/tools-ki/blob/907a627ef407513ef560fce4b1f7ba103d60d7e5/docs/roadmap/KI-TOOL-KI-CLI-152-work-folder-housekeeping-commands.md) to awaiting review
- `0c107a9fa1edfd0e6cd789ed5392984a3778f222` - docs(roadmap): record two failed acceptance reviews
- `bc563d56bd0bee4b628fcb65bb68703fa2a1b046` - docs(roadmap): accept two independently verified records
- `0a200642019589fd5593c9d8f6267c6cf2d2ce37` - docs(roadmap): return [KI-TOOL-KI-CLI-134](https://github.com/knowledgeislands/tools-ki/blob/0a200642019589fd5593c9d8f6267c6cf2d2ce37/docs/roadmap/KI-TOOL-KI-CLI-134-launch-footer-follows-brief.md) and [KI-TOOL-KI-CLI-165](https://github.com/knowledgeislands/tools-ki/blob/0a200642019589fd5593c9d8f6267c6cf2d2ce37/docs/roadmap/KI-TOOL-KI-CLI-165-hook-composition-claims-host.md) to awaiting review
- `a37f31515e17a6fb626eab796aada5a9ad497e20` - chore(roadmap): prune 1 done work record
- `fde00e978a4c9b0e697252bac3e0979f09d85e8c` - docs(roadmap): accept hook host and retain footer owner review
- `39f1a91d015efedcc8e362b5cd625eb44d941fe1` - chore(roadmap): prune 3 done work records
- `b4f8a100c0c4675d11a9b8ce7baaddee4afaafa3` - docs(roadmap): plan [KI-TOOL-KI-CLI-159](https://github.com/knowledgeislands/tools-ki/blob/b4f8a100c0c4675d11a9b8ce7baaddee4afaafa3/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md) to Ready
- `5aebeb9d093c29fe975ac5eb1408e915a0ef2a91` - feat(territory): report island maturity and audit health
- `a073f97b65f894fec0e8c30ec064749d6da3fb35` - docs(roadmap): accept [KI-TOOL-KI-CLI-159](https://github.com/knowledgeislands/tools-ki/blob/a073f97b65f894fec0e8c30ec064749d6da3fb35/docs/roadmap/KI-TOOL-KI-CLI-159-island-maturity-and-health.md)
- `93f87721d45c71f843204e77a6a000e596d27c46` - docs(roadmap): repoint [KI-TOOL-KI-CLI-160](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) to the pinned work-package design
- `c7dac1321dc4f50b0626b51f62833c78dfdd7ee3` - docs(roadmap): repoint links to pruned records for ki.ways-of-working
- `a0cadb9f1ad9b1ee513b41d837f83834e6301fa5` - chore(roadmap): prune 1 done work record
- `f4811dd9310b48d8809d9143ca8864fc7b4be5e2` - docs(roadmap): accept CLI-134 and record agreed check and view homes
- `6c865c85a17b1889bfc742ac1c1948c8d2a23775` - chore(roadmap): prune 1 done work record
- `9252669a3f56d9b025921041ae6544a525139b2e` - fix(vscode): preserve trust independently of workspaces
- `a2e3460db4efdc4065d6cb9e0bcd88d57a9adc49` - chore(hooks): adopt canonical tools commit gates
- `80060dcc9aa823e740b8e82e17901d2479ec3c25` - chore(authoring): restore the canonical rumdl configuration
- `35e3bf5497db66d991caf20d544a9e5380ab4913` - chore(hooks): invoke staged formatters directly
- `d6f650d46751056f97834ff351ab819f2930456a` - docs(roadmap): correct EBU sources sync project reference
- `f928a73a327715f679facf663b22f79540679125` - fix(acquire): reject retired adapter actions
- `755bd21b9cfbd71959b73be57f543493dc4a19f2` - fix(work): keep resolution targets in their repository
- `5889f847c8893100550cf83f505c411f341f6569` - fix(repo): inherit verified linked-worktree ownership
- `869fed5d185c332653f7fdd85ee4a7301e3a6f2f` - docs(contributing): keep tools-ki main on committed code
- `ec57890e6a0811bd9268e6d0d6b1b7413728a769` - test(work): verify resolution and worktree failure boundaries
- `ca246ff8a94676bfb3f0619505f90409148d8870` - feat(agent): align worktree launch and estate visibility
- `fcc8876a4ac974d7d8c0aa41e5d14ec2021302ff` - test(boundaries): retain complete graph output in audit snapshots
- `4a02b008a9adafe9909916489b8926b34cd24937` - test(repo): reject copied Git administration pointers
- `6bb9334fc830797a25e106cfe5dfe58f9d713e5e` - fix(completion): complete worktree repository paths
- `f95bc710d3b518c6b664a49e2bcd5d00cfe1eda5` - test(work): assert absent cross-repository replacement targets
- `d5eac480f6b44a7fe0bb1ca1d2b7340decbefcab` - test(agent): retry transient sandbox cleanup failures
- `d6e8f369fac456de387298cae060058471970705` - docs(roadmap): ready offline CLI-140 evidence plan
- `fcbaf5105eee4b6804a6e251781e454f2ff868d9` - fix(ci): audit with a compatible released KI
- `a859371c6701f9c58b2930ceefdbb524019dd20e` - docs(roadmap): submit CLI-156 for review
- `566679b2cb7648a0746d745aa29a297cd1b3eaf2` - docs(roadmap): accept CLI-156 independent review

</details>

## In Progress

Nothing is running. Candidate preparation is returned to the ki.ways-of-working coordinator, not waiting in this session. No linked worktree was needed for read-only inspection; no development or verification was performed in the primary checkout. No repository changes or unpublished commits from this run need transferring from sol.local.

Outstanding - no action requested now: future release proof must remain separate from the pre-tag dossier. After all pre-tag conditions pass, Kris alone creates and pushes the exact lightweight tag and dispatches the release workflow. That later run must prove signed archives, downloaded-asset verification, immutable publication and clean Linux installation, followed by exact released version and manual installation checks. An unrun workflow or future tag CI is not current proof.

Outstanding - no action requested now: publication can trigger the enrolled Homebrew tap dispatch, formula pull request, checks and automatic merge; the tap then owns enrolled website notification. A sent event is not completed downstream delivery. Retain the exact immutable installer URL and pinned invocation for the eventual released tag, and confirm the website overview route `https://knowledgeislands.info/projects/ki/`. No tap, website or receiver pin action was performed. No credential or App configuration was inspected.

Outstanding - no action requested now: after actual publication, route the local post-release `+dev` version-marker follow-up through its owning approved workflow; no `+dev` marker or future commit is created here. Explicitly retain GRANT-INTERIM until a tagged release carrying `--allow` is installed. Neither acceptance nor this dossier retires it.

## Queries

### CANDIDATE-PREP - Prepare an eligible version and return exact proof

**Context**: Main `566679b2cb7648a0746d745aa29a297cd1b3eaf2` includes the independently accepted CI repair but still declares the already-tagged `0.12.0`. The frozen range contains 60 commits, including earlier product and breaking changes whose release review authority has not been established here. The Harness pin has not advanced with local Harness development. Saved CI succeeds only at the earlier review-packet head. Required gates were not run after the first blocker, as the brief requires stopping rather than repairing product/version/pin sources.

**Query**: Coordinator to arrange a separately authorised preparation pass, confirm the intended version and entire included range, then return a newly frozen candidate with all missing pre-tag proof. This report does not ask Kris to tag or publish now.

**Options**

a) (recommended, confidence high - the current version cannot match a new exact release tag and the supplied CI head is different) Confirm `v0.13.0` or explicitly select another unused semantic version; authorise the version and immutable Harness-pin/digest preparation in their owning lane; establish acceptance/review authority and migration notes for every included product change; verify public-surface and installer/manual alignment; run the full isolated definition-of-done and behaviour coverage gates with installed dependencies; obtain separately authorised exact-new-head CI and any required read-only setting proof; then issue a replacement dossier with real resolved tag/SHA calls for Kris.

b) Hold the release candidate, retain the accepted CI repair and GRANT-INTERIM, and return once a concrete approved release scope and preparation authority exist. No tag, publication, new record or source edit follows from this option.

### 🤖 → 👤 Handoff to supervisor · since 05:11 BST

👤 1 with you · ⛔ 1 blocked

- [with you] CANDIDATE-PREP - eligible version, range authority and exact proof · ki.ways-of-working coordinator · since 05:11 BST
- [blocked] Named tools-ki release candidate incomplete · ki.ways-of-working coordinator · since 05:12 BST
