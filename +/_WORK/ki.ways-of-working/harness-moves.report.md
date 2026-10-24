# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › harness-moves

**🤖 → 👤 Handoff to supervisor · Run report at 03:43 BST · last mark 03:08 BST**

---

## Done

- HARNESS-TRIAGE applied in harness `50c9cced`: [KI-HARNESS-GOV-196](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-196-scratch-output-in-temp.md) and [KI-HARNESS-GOV-226](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-226-banner-rendered-glyphs.md) to Now; [KI-HARNESS-GOV-189](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md), [KI-HARNESS-GOV-225](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-225-hook-content-claims.md) and [KI-HARNESS-GOV-227](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-227-repository-storage-declarations.md) to Next; [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md) adopted and held until 24 October (review date set), not triage; [KI-HARNESS-GOV-222](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-222-timeline-and-calendar-skill.md) stays in triage with `project: timelines`. Nothing was "Later", so nothing went to Future. Now and Next records need full execution sections to pass the roadmap audit, so I added them to the five, as drafts, not Ready.
- KI-HARNESS-GOV-222 handoff: one `messages.md` line sent to the [ki.timelines](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.timelines/work.md) work (ki-principal `20e696d2`, committed locally, not pushed: ki-principal has 40 other sessions' commits waiting to push).
- [KI-HARNESS-GOV-202](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md) stays in triage. What it is: the ten skill-area diagrams show a "SRC" badge on each skill, and this would swap it for useful numbers such as rubric rule count, code size and reference count. Why it might matter: the badge would then tell a reader something about each skill, but it is cosmetic and nothing waits on it.
- PLANNED-READY applied in harness `d45a6179`: answers recorded and [KI-HARNESS-GOV-200](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-200-thread-folder-closed-list.md), [KI-HARNESS-GOV-205](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-205-static-light-diagram-export.md), [KI-HARNESS-GOV-214](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-214-working-area-marks.md), [KI-HARNESS-GOV-215](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-215-pmo-12-to-fail.md), [KI-HARNESS-GOV-220](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-220-coord-1-undeclared-warn-level.md) and [KI-HARNESS-GOV-221](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-221-ki-diagrams-mermaid-fence-warning.md) are Ready. For GOV-200 the temp home is the launcher's `$TMPDIR/ki-agents/<run>/<name>/` (Kris's HARNESS-TRIAGE a), via GOV-196), and the closed-list check lands as FAIL after the Capitals census, as WORK-FOLDER-CHECKS a) set; GOV-205 stays size `l`, not split, because a split would create a new record.
- [KI-HARNESS-GOV-223](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-223-island-maturity-declaration.md) not Ready: two of its three answers are recorded, but the decline rule has no tolerance value, and `ki repo audit` keeps no history, so a warning's age can't be read. See MATURITY-DECLINE.
- GFM-HOSTING-RULES, read-only: classic branch protection is off on every repository. Three repositories have an active ruleset on the default branch, and each lets the repository admin role bypass it always, so you can already push `main` from local; GitHub only reports the bypass:
  - ki-agentic-harness ("main", 9 October): PR with 0 approvals, check `build`, no deletion, no force-push.
  - homebrew-tap ("Protect main", 5 October): squash-only PR with 0 approvals, checks `KI governance` and `Homebrew formula gates`, no deletion, no force-push.
  - apps-knowledgeislands.info ("main: require build and pull requests", 5 October): PR with 0 approvals, check `build`.
  - The other 17 public repositories have nothing. The private repositories apps-observatory.local and mcp-acquire-whatsapp can't have rules on the current plan. paperclip has no `main` (its default is `ki/stable`, unprotected). Organisation-level rulesets need the `admin:org` scope I lack, but the per-branch rules read would have shown any that apply. Nothing changed.
- Checks: `bun run test` passed (1327); `bunx tsc --noEmit` passed; `ki repo audit --skill ki-work-roadmap` 0 FAIL (7 existing size warnings); pre-commit hooks passed. Harness `main` and the primary checkout fast-forwarded to `d45a6179` and pushed via the admin bypass. Worktree removed, branch deleted.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- KI-HARNESS-GOV-196 and KI-HARNESS-GOV-200 edit the same temp-home sentence and `run-prompt.md`. Both records say to deliver them one after the other.
- KI-HARNESS-GOV-225's boundary may still widen when NO-GATE comes back off park.

## Queries

### MATURITY-DECLINE - How the island-maturity record reads "decline"

**Context:** KI-HARNESS-GOV-223 adds a declared maturity level (founding, growing, settled, thriving) to each repository's `.ki.toml`. "Ruin" and "decline" are worked out from audit health, not declared. The recommendation you took gives "ruin" as failing checks or an audit that can't run, which works. It gives "decline" as warnings left open longer than a tolerance, but no tolerance was ever set. `ki repo audit` also keeps no history, so nothing knows how old a warning is. The record stays a draft until this is settled. The `ki` reader in tools-ki that shows the signal waits on this record.

**Query:** How should "decline" be read, so the record can go Ready?

**Options:**
a) (recommended, confidence medium - it works with what the audit gives today, but it flags any warning, however new) Decline means the latest audit has open warnings and no failures. No age and no tolerance; mark the record Ready.
b) Keep the age rule with a 30-day tolerance, and give the tools-ki reader the job of keeping audit history to measure it.

### 🤖 → 👤 Handoff to supervisor · since 03:44 BST

👤 1 with you

- [with you] MATURITY-DECLINE · owner · since 03:44 BST
- [committed] harness `d45a6179`, pushed
- [unpushed] ki-principal `20e696d2`, stacked with other sessions' commits
