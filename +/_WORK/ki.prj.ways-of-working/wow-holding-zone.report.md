# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-holding-zone

**🤖 → 👤 Handoff to supervisor · Run report at 02:50 GMT · last mark 01:07 GMT**

---

## Done

All 40 records in buckets B, E and F of the [roadmap sweep](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/roadmap-sweep.md), plus [KI-TOOL-KI-CLI-125](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/ideas/KI-TOOL-KI-CLI-125-ki-release-contract.md) and [KI-TECHNE-OPS-024](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/ideas/KI-TECHNE-OPS-024-weekly-pin-bump.md), are out of the roadmap and in the owning repository's ideas. Buckets C and D stay. No record could not be moved.

Where the ideas live, in every repository: the full text of each record is at `docs/ideas/<original filename>`, unchanged except for one plain-language line under the front matter saying what it is for, when it moved and what identifier it had; and `docs/roadmap/_IDEAS.md` holds one bullet per idea linking to its full text, as `ki-work-roadmap` and `ki-next` define the ideas list. A `_IDEAS/` subfolder inside `docs/roadmap/` fails the audit's roadmap rule, and the record loader and the Observatory's roadmap reader both skip `docs/ideas/`, so the moved records no longer count as roadmap work anywhere.

- apps-observatory.local: 5 moved, commit db0d4a7, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/_IDEAS.md) and `docs/ideas/`. The Observatory holding area sits in that file, under its own heading, quoting Kris's words of 27 October, naming the five moved records and holding the three Observatory improvement ideas from the sweep (queries read and answered in the Observatory, a burn-down trend, work status from a contract). Audit FAIL=0.
- ki-agentic-harness: 7 moved, commit 1e679cd1, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/_IDEAS.md) and `docs/ideas/`. Audit FAIL=0.
- tools-ki: 9 moved (the eight from the sweep plus CLI-125), commit 631deaf9, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/_IDEAS.md) and `docs/ideas/`. Work loader clean.
- tools-rig: 3 moved, commit 89b649a, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/_IDEAS.md) and `docs/ideas/`. The three renames were already staged when wow-quick-wins committed a3b7f57, so they travelled in that commit unchanged; 89b649a adds the plain-language lines and the ideas list. Audit FAIL=1, the pre-existing SHELL-HOOK finding, unrelated.
- ki-design: 3 moved, commit 4a0033f, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/_IDEAS.md) and `docs/ideas/`. [KI-DESIGN-ART-002](/Users/krisbrown/workspaces/knowledge-islands/ki-design/docs/roadmap/KI-DESIGN-ART-002-art-licensing.md), a bucket D record that stays, no longer names the moved tile set in its `blocks` list, because the audit's dependency rule fails on a link to a record that is no longer on the roadmap; its text says the dependency returns with the record. Audit FAIL=4, all pre-existing and unrelated (a decision file heading, lint-staged, a retired docs root, GitHub live state).
- mcp-m365: 9 moved, commit 110a2be, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/mcp-m365/docs/roadmap/_IDEAS.md) and `docs/ideas/`. Audit FAIL=1, pre-existing lint-staged finding.
- mcp-gsuite: 2 moved, commit e410311, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/mcp-gsuite/docs/roadmap/_IDEAS.md) and `docs/ideas/`. Audit FAIL=1, pre-existing lint-staged finding.
- tools-mgit: 1 moved, commit f1ce64d, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/_IDEAS.md) and `docs/ideas/`. Audit FAIL=1, the pre-existing SHELL-HOOK finding.
- ki-techne-harness: 1 moved (OPS-024), commit 3f26d8d, pushed. Ideas at [docs/roadmap/_IDEAS.md](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/_IDEAS.md) and `docs/ideas/`. [KI-TECHNE-OPS-018](/Users/krisbrown/workspaces/knowledge-islands/ki-techne-harness/docs/roadmap/KI-TECHNE-OPS-018-converge-tools-through-rig.md) stays on the roadmap at Later (`horizon: future`) with its hold block and Rig/ki release dependency removed and a short section saying why. Audit FAIL=1, pre-existing lint-staged finding.
- ki-principal: inbound links repointed in 16 work-package files, commit 796e1ad2, pushed. The repoints in `ki.observatory/messages.md` and `ki.ways-of-working/decisions.md` had already gone out in the coordinator's own commits.
- personal-principal: 1 link repointed, commit e6d7a128, pushed.
- hnr-principal: 4 links repointed in one record, commit 87a5c808, not pushed. The pull could not fast-forward: local main carries the coordinator's unpushed f4fb8653 and origin/main has since merged it from another machine (a82ae51a), so the checkout is one ahead and two behind. Stopped on divergence as instructed; nothing stashed, rebased or reset.

Checks: the markdown lint passes on every changed file in every repository that has it; tools-rig and tools-mgit have no local lint binary, so their files were linted with mcp-m365's copy. Every commit passed its pre-commit and commit-msg hooks; one ki-design commit attempt failed the body line-length rule and was redone with a wrapped body. Audits re-run after the edits show no dependency, roadmap-content or ideas-related failure anywhere.

Left alone on purpose: 42 historical `*.report.md` files, most of them untracked and other sessions', still carry old `docs/roadmap/` links; a harness test fixture (`ki-coordination/scripts/rubric/contexts/coordination.test.ts`) uses made-up roadmap paths; neither is a live link. Other sessions' uncommitted files in tools-rig, personal-principal and ki-principal were not staged. tools-rig's local main also carries wow-quick-wins' unpushed 5d2472f, left to that run.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- hnr-principal's commit 87a5c808 (four link repoints) waits for a fast-forward path: a bounded resolve run in its own worktree, or the coordinator pulling with rebase, would publish it.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 02:50 GMT

👤 1 with you · 🅿️ 0 parked

- [with you] wow-holding-zone report · supervisor · since 02:50 GMT
- [behind] hnr-principal: 2 commits, with 1 unpushed on top
- [committed] 12 commits across 12 repositories, 11 pushed

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
