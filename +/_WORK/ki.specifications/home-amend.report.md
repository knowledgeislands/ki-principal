# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Portable specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/portable-specifications.md) › home-amend

**🤖 → 👤 Handoff to supervisor · Run report at 01:17 BST · last mark 23:45 BST**

---

## Done

- [design/home-plan.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/home-plan.md) amended; it is the only file changed. Not committed, as the brief says. rumdl reports it clean and it has no en or em dashes.
- Provenance: a line saying home-amend amended the note to CATALOGUE-WRITE, HOMING-REVIEW and query-review-6.
- Gate and order: the gate is now SPEC-TEXT with HOMING-EDITS folded in, both pending Kris. A record must be at Ready before a run starts. 6a keeps the ENTRY-NAMES prerequisite firmly: it waits until that change has integrated into local `main`, so the profile's "if it has landed" wording is now definite.
- New section, Records, review and acceptance: three triage records captured under ki-next, with deduplication first. The ledger is re-read before identities are allocated, and GOV-227 is the current high mark, not a reservation. Capture authorises no delivery. Then Ready, delivery to Awaiting review with the six-part packet, and one blind Codex review per candidate on the exact commit and its combined result, with tests, type-check and focused audits. Then serialised integration and Kris's acceptance under ki-accept. This route replaces the plan's Steward gate for this coordinator route only; the Paperclip route's Steward review is left untouched.
- Homing transform: HOMING-EDITS is stated as part of SPEC-TEXT and pending Kris, with the fallback if Kris takes option b).
- New subsection for 6c, The bounded conform write: exactly one write-mode `ki-repo-harness` conform, as a scoped exception. The note records that HOOK-GUARD is superseded in ki.tools-burndown and ki.mac-studio-setup but still carried by ki.ways-of-working, ki.timelines and ki.baseline-rollout. The steps are: audit, dry-run, check the complete path set and diff against a four-path briefed set, write, check paths and hunks again, re-audit, export the SVGs separately, then re-audit again. Manifests, lockfiles and hook directories are excluded, and the generated output is regenerated if `main` moves under 6c.
- Verification: the gates run in each worktree and again on the combined result. The 6c `ki-repo-harness` audit now runs before and after the write and after the export.
- Running the three in parallel: the shared-tree approach is replaced with separate worktrees under `~/.local/state/ki/agents/<run>/worktrees/ki-agentic-harness`. Integration into local `main` is serialised inside `ki-git`'s write window, and the rules for a moved `main` are set out. The chain-instead option is removed because worktrees make it unnecessary.
- What needs Kris: SPEC-TEXT with HOMING-EDITS, and acceptance of each record. CATALOGUE-WRITE and HOMING-REVIEW are listed as already decided.
- One addition beyond the review: ki.tools-burndown has recorded conform rewriting `.rumdl.toml` and running a `rumdl --fix` reflow 20 times. So the step after the write checks hunks as well as paths, and the run stops if it sees either.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [design/plan.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.portable-specifications/design/plan.md) still says "Steward review" in its step 6a row (line 149) and its harness review latency risk (line 171). The home plan now replaces both for this route, but bringing plan.md into line is the coordinator's job; this brief limited writes to home-plan.md.
- `ki-work-package`'s description mentions `work.md`, so the ENTRY-NAMES harness run will change the generated catalogue. If that lands before 6c integrates, 6c must regenerate. The amended plan covers this.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 01:17 BST

👤 0 with you · 🅿️ 0 parked

- [uncommitted] design/home-plan.md
