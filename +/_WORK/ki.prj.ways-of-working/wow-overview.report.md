# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-overview

**🤖 → 👤 Handoff to supervisor · Run report at 01:16 GMT · last mark 01:07 GMT**

---

## Done

- Wrote [overview](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/overview.md), committed alone as `8c4c1f99` in ki-principal, not pushed. It has four sections: the enhancements by theme; packages against records, with options A to C and three named queries; all 17 message lines with what happens to each; and the roadmap in this area. It reflects the read-backs in `f6ec8db3` and `0de07de8` and the unattended brief in `f7a2f0da`.
- Checks: every absolute link in the note resolves on disk; no en or em dashes; the commit hook's audit of the one path passed with no failures or warnings. The repository-wide audit still has one failure and seven warnings that were there before and are outside this path.
- Finding: none of the `ways-of-working` records can move tonight without Kris. [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) and [KI-PRINCIPAL-MOD-009](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md) need acceptance. [KI-HARNESS-GOV-204](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md) waits on Kris's evidence review, which fell due on 24 October. [KI-TOOL-KI-CLI-145](/Users/krisbrown/workspaces/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-145-thread-session-bindings-role.md) waits on THREAD-RENAME, and [KI-TOOL-KI-CLI-160](https://github.com/knowledgeislands/tools-ki/blob/cf186ecf39791689145530f3be73341a4717a8dc/docs/roadmap/KI-TOOL-KI-CLI-160-work-status-routing-view.md) on WORK-STATUS-FORM. Four things can still move unattended under decided answers: the coordination-standard run (COMMIT-CADENCE a), SUMMARY-WINDOW a) and the COORD2-RUBRIC label fix), the CENTRAL-TICK idea line, the WORK-PROCESS-NOTE fold and the unattended brief's reviews.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The grant's end time: it was read back at 01:07 GMT as 08:00 GMT. Kris said "until 9 a.m." at 01:31 BST, before British Summer Time ended, and 9 a.m. on the wall clock is now 09:00 GMT. Stopping at 08:00 GMT is an hour early, which is the safe side. Draft WINDOW-CLOCK in the [unattended-work brief](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unattended-work.md) covers future windows.
- In [messages.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md), the DIAGRAM-PRIVATE-CITATIONS line still links KB-MIDNIGHT-TOWER-SITE-019, and that file no longer exists. The record is now [PERSONAL-TOWER-SITE-019](/Users/krisbrown/workspaces/personal/apps-tower.midnight.ninja/docs/roadmap/PERSONAL-TOWER-SITE-019-redraw-mermaid-in-archify.md). Repointing the link is a one-line fix in the coordinator's own package.
- The [design index](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/design.md) does not list the overview yet. The brief allowed only this one note, so I left the index alone.
- Message lines that can be removed: WAKE-SUBSTRATE now, as it is carried. SUMMARY-SINCE-MARK and SUMMARY-OUTSTANDING once SUMMARY-WINDOW lands. DIAGRAM-PRIVATE-CITATIONS and CF-PRODUCTION-BRANCH go back to State of play to find an owner.

## Queries

### PACKAGE-HOME - every Project package lives in its Capital

**Context:** No standard says where a Project package lives. Records live in their owning repositories and find their Project through `project` and the Capital's registry. In practice every Project package in KI (16), HNR (25) and Valle Armonia (3) is already in its Capital. Moving a package beside its records (option B) would split the Capital's view, and a Project's records span several repositories. Putting records inside the package (option C) would overturn repository ownership of records and HANDOFF-AS-MESSAGE. The note's section 2 sets out all three options.

**Query:** Should the work-package standard say that every Project package lives in its territory's Capital, with records staying in their owning repositories and joined only by `project`?

**Options:**
a) (recommended, confidence high - it writes down what all three territories already do, needs no migration and adds no machinery) State it in the work-package standard: Project packages live in the Capital, records stay with their owners, and the State of play stewards packageless Projects until one needs its own package.
b) Let a Project package live in the repository that holds most of its records.

### MEMBER-PACKAGE - a member repository's own regular work

**Context:** [personal.regular.acquire-intake](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/personal.regular.acquire-intake/work.md) is a package held in the member repository `personal/acquire`, not in the Capital. The rubric bars only territory work outside a Capital, so this is allowed but undeclared anywhere. It is the only such case found. This query has not had a blind review.

**Query:** May a member repository hold a package for its own regular work, provided its `work.md` declares it as such?

**Options:**
a) (recommended, confidence medium - one case only, and regular work naturally sits with the code it runs against, but the pattern is unproven) Allow it for regular work only, declared in `work.md`; Project and territory work stay in the Capital.
b) Move every package into the Capital, including regular work.

### RECORD-RESOLVES - check that a record's `project` resolves

**Context:** Nothing checks that a record's `project` names a registered Project. Tending already lists this as a mechanical-check candidate, because VA-WEBSITE-SANC-011 names a Project that does not resolve. Separately, some records name no Project at all, such as [KI-HARNESS-GOV-202](https://github.com/knowledgeislands/ki-agentic-harness/blob/083735f4cb450adb6639b60f04b11f0cbdaddb67/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md), so no package steers them.

**Query:** Should a mechanical check flag a record whose `project` does not resolve, run as a tending check at the State of play rather than in each repository's rubric?

**Options:**
a) (recommended, confidence high - one check over data the Capital already holds, already proposed in tending, and in keeping with the over-engineering steer) Make it a tending check at the State of play, reporting unresolved and missing `project` values as findings.
b) Add it to the work-roadmap rubric so that each repository checks its own records.

### 🤖 → 👤 Handoff to supervisor · since 01:16 GMT

👤 3 with you

- [with you] PACKAGE-HOME · owner · since 01:16
- [with you] MEMBER-PACKAGE · owner · since 01:16
- [with you] RECORD-RESOLVES · owner · since 01:16
- [committed] overview note

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
