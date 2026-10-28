# Ways of working window plan - 25 October 2026

## Authority and window

This is wow-roadmap-2's plan under [the work's scope](../work.md) and [Kris's logged answers](../decisions.md): WINDOW-CLOCK at 01:38 GMT, PROGRESS-SCOPE and CONFLICT-RUN under REVIEWED-BLOC at 01:43 and 01:45 GMT, and the overnight ways-of-working focus. The current run brief authorises this plan, commits and fast-forward publication. The window ends at 09:00 GMT (2026-10-25T09:00:00Z); no new step starts after 08:45 GMT (2026-10-25T08:45:00Z).

Only already-adopted, authorised Now or Next drafts may be planned to Ready. Eligible Ready records may be delivered to awaiting review in frozen, repository-local ki-batch waves. Adoption, discretionary promotion, release from Hold, acceptance and pruning remain with Kris. No unattended field is added while UNATTENDED-FIELD remains open. Suitability below applies only to this window.

No release, force-push, verification bypass, provider or settings change, environment or credential change, external messaging, or standard or configuration change beyond Kris's logged decisions is authorised. Tools-ki is excluded tonight. Only the Git network calls expressly authorised by the brief are permitted. A connection-critical unit needs a tested restore path before admission.

## Entry and order

The dependency statuses for wow-harness-coord-2, wow-harness-model-2 and wow-skillset-fixes-2 all ended in DONE before this scan. Both primary repositories were pulled with fast-forward-only before inspection. The harness entry revision was `6f3497c53ab260cc67c091340b488d24e41a7845`; the principal revision at the completed scan was `b684b1e1b01497be490167be764a770ff854a827`. Each matched its origin/main tracking ref at inspection. Other sessions' package changes and reports are outside this run's touched paths.

1. Commit this plan in ki-principal, under the run's explicit write authority. This is a small documentation unit with no roadmap lifecycle change.
2. Recheck the complete flat roadmap inventory and owner queue before admitting any work. The selected adapters are `kb-streams` for ki-principal and `roadmap` for the harness, as declared in their tracked configuration.
3. For any admitted Now or Next draft, use ki-plan and its adapter gates before readiness. Freeze each complete eligible repository-local wave under ki-batch, citing this grant, before delivery; use `completion_target: awaiting-review` and expiry no later than 09:00 GMT. Honour dependencies and the owner queue cap. Do not create an empty authorisation.
4. If the recheck confirms the inventory below, start no wave and return the completed scan. A held item, an owner render check or an unrelated draft is not a substitute for eligible work.

After each commit, inspect its actual changed paths, pull fast-forward-only, fetch and publish only this run's commits where the brief permits. Do not publish another session's unpublished commits. A non-fast-forward pull permits rebasing only this run's unpublished commits in its own worktree under CONFLICT-RUN; uncertain ownership, another session's content or a judgement call stops the run for a query. Never stash, revert or commit another session's files.

## In-scope inventory and window suitability

- [KI-PRINCIPAL-MOD-009 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-MOD-009-amend-adr-001-staging-wording.md): `awaiting-review`, `now`. Included by the work's acquisition-method and canonical wording boundary, although it has no Project field. Delivery and its review packet already exist. Further progress is attended owner review and acceptance; reopening or accepting it is outside this grant. No draft planning or new delivery is eligible.
- [KI-PRINCIPAL-OPS-014 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/da027e6d/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md): `project: ways-of-working`, `awaiting-review`, `now`. Delivery already exists. The remaining four-client render checks were expressly assigned to Kris by RENDER-CHECK. Suitability fails the no-owner-judgement condition; preserve the review packet and leave the checks and acceptance with Kris.
- [KI-HARNESS-GOV-204](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-204-pretooluse-quietening-hook.md): `project: ways-of-working`, `draft`, `hold`. It is adopted but awaits Kris's review of a week's evidence, due 24 October. The elapsed review date does not release the hold. Suitability fails the no-owner-judgement and unblocked conditions: whether a hook is needed and its safe behaviour remain undecided. Do not plan, release or implement it.
- [KI-HARNESS-GOV-189 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bedbb4d9/docs/roadmap/KI-HARNESS-GOV-189-move-thread-between-hosts.md): `done`, no horizon. Its repository-level-check behaviour is within coordination scope despite `project: mac-studio-setup`. Terminal evidence only; no unattended delivery remains and pruning is excluded.
- [KI-HARNESS-GOV-209 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/bedbb4d9/docs/roadmap/KI-HARNESS-GOV-209-acquired-inbound-area.md): `done`, no horizon. Included conservatively as receiving-island method adjacent to the principal staging wording. Terminal evidence only; no unattended delivery remains and pruning is excluded.

For this window the complete eligible planning set and complete eligible Ready delivery set are both empty in each repository. There are no dependency-ordered waves to freeze. This is a completed eligibility assessment, not permission to expand scope.

## Other scanned records

The recursive Markdown scan found two principal work records and ten harness work records, excluding index and issues notes. All principal work records are accounted for above. The remaining harness records are excluded as follows:

- [KI-HARNESS-GOV-202](https://github.com/knowledgeislands/ki-agentic-harness/blob/083735f4cb450adb6639b60f04b11f0cbdaddb67/docs/roadmap/KI-HARNESS-GOV-202-skill-area-stable-stats-badge.md): Next draft for diagram stats and skill-area presentation; outside this work's method, coordination and work-record boundary. Its separate adoption does not extend tonight's grant.
- [KI-HARNESS-GOV-227](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-227-repository-storage-declarations.md): Next draft owned by Observatory, expressly outside this Project's scope.
- [KI-HARNESS-GOV-228](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-228-home-work-spec.md), [KI-HARNESS-GOV-229](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-229-home-acquire-spec.md) and [KI-HARNESS-GOV-230](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-GOV-230-knowledge-package-skill.md): unadopted triage owned by portable-specifications, expressly outside scope. None may be adopted or planned here.
- [KI-HARNESS-OPS-009](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-OPS-009-complete-ai-session-acquisition.md): Next draft for ChatGPT acquisition coverage and browser feasibility, not the work-process or coordination model. Outside scope and no browser or remote trial is authorised tonight.
- [KI-HARNESS-REV-012](../../../../../ki-agentic-harness/docs/ideas/KI-HARNESS-REV-012-thoughtworks-radar-input.md): unadopted triage for radar input, outside scope.

## Capacity and verification

At inspection the Project had eight existing open query headings and two records awaiting acceptance, counting the unclassified principal method record conservatively. The owner queue cap is eight queries and eight records awaiting acceptance. The queue is at the query cap, not over it; this run adds no query or review record and does not use the cap as authority to resolve an existing question.

Base ki-work selection audits passed in both repositories. The harness ki-work-roadmap audit passed. The principal ki-repo-kb-streams audit had zero failures and four existing STREAM-10 warnings for other Projects: mac-studio-setup, paperclip-capture-and-rebuild, secrets-hygiene and timelines. No planning is attempted through that warning gate and no unrelated repair is authorised.

Verify the plan's links, exact record status and horizon predicates, unchanged roadmap bytes, whitespace and the mandatory commit hooks. Recheck the inventory after the plan commit. This documentation-only scan needs no new implementation tests. Return the existing owner-review and hold constraints in the run report; leave canonical records unchanged.
