# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › unpark-draft

**🤖 → 👤 Handoff to supervisor · Run report at 02:58 BST · last mark 02:01 BST**

---

## Done

- Checked all five unparked queries against local state, with no network calls. None was wholly overtaken, but three were partly overtaken:
  - NO-GATE: the hooks were already installed in apps-dafacts.org, apps-kris.me.uk and acquire at 00:32 BST under ki.tools-burndown. The query is redrafted as the remaining question, which is where the gate's content owner is declared.
  - PKGLESS-GATE: folded into NO-GATE, so answering NO-GATE answers it.
  - PRINCIPAL-TRIAGE: the KI-PRINCIPAL-GOV-035 prune half is done ([KI-PRINCIPAL-GOV-035 (pruned)](https://github.com/knowledgeislands/ki-principal/blob/a54cd93183e931cd0f302cbf330384a7cbcf36eb/Streams/Roadmap/KI-PRINCIPAL-GOV-035-turn-the-techne-programme-hold-into-a-focus-rule.md), pruned in `e6d04024`). Both blockers on [KI-PRINCIPAL-OPS-014](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Roadmap/KI-PRINCIPAL-OPS-014-gfm-conversion.md) have landed, so the recommendation is now Now for the pilot only, not Next.
- [design/unparked-queries.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/unparked-queries.md) holds four live queries in owner-report shape: NO-GATE (with PKGLESS-GATE), GFM-HOSTING-RULES, HARNESS-TRIAGE and PRINCIPAL-TRIAGE. All four are at medium.
  - HARNESS-TRIAGE lists a disposition for each of the eight records. It names [KI-HARNESS-GOV-228](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-228-home-work-spec.md), [KI-HARNESS-GOV-229](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-229-home-acquire-spec.md) and [KI-HARNESS-GOV-230](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/docs/roadmap/KI-HARNESS-GOV-230-knowledge-package-skill.md) as newer triage records that ki.portable-specifications owns, so they are not in this query.
  - Correction: the GFM-HOSTING-RULES override key is `[skills.ki-repo.checks]`, not `[skills.ki-repo]` as the earlier draft said.
- [briefs/unpark-review.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/briefs/unpark-review.md) is the masked blind review brief: Context, Query and unranked options only, and the options are shuffled so the recommended one is not always first.
  - It covers GFM-HOSTING-RULES, HARNESS-TRIAGE and PRINCIPAL-TRIAGE, which had not been reviewed.
  - It also covers NO-GATE, which goes beyond the brief: qreview9 (NO-GATE) and qreview10 (PKGLESS-GATE) reviewed only the earlier question of whether to install the hooks, so the residual question is unreviewed. To keep NO-GATE at its earlier review instead, drop that section from the brief before launching.
- Commit `2a7b1f2c`, `docs(work): ki.ways-of-working draft unparked queries`, contains the two files only, staged by explicit path; the pre-commit gate passed, and it is not pushed.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The coordinator launches unpark-review under Codex, then puts the four queries to Kris with the review's view.
- ki-principal pins `ki` v0.11.5 while the converter is in v0.12.0. PRINCIPAL-TRIAGE a) moves the pin as its first step.

## Queries

No outstanding queries.

### 🤖 → 👤 Handoff to supervisor · since 02:58 BST

👤 1 with you

- [with you] launch unpark-review, then the four queries · supervisor · since 02:58
- [committed] `2a7b1f2c` design/unparked-queries.md and briefs/unpark-review.md
- [unpushed] ki-principal
