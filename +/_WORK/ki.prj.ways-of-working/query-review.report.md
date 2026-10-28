# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › query-review

**🤖 → 👤 Handoff to supervisor · Run report at 19:18 BST · last mark 18:56 BST**

---

## Done

- The QUERY-REVIEW rule is in the [ki-coordination standard](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#query-review). It sits in a new Query review section under Owner report, quotes Kris's words from QUERY-REVIEW (2026-10-19 08:22 BST) and QUERY-REVIEW-STANDARD ("agreed, please go ahead"), and the query shape now points to it.
- The rule marks an agreed query with a reason that begins `reviewed` and a disputed one with a reason that begins `review disagrees`. Both forms still pass the existing COORD-11 confidence check. Agreement never lifts a destructive course resting on claims not verified directly to `high`, because the confidence rule already forbids it.
- The output style carries the rule as one clause in its Queries item, regenerated with `ki dev skill generate ki-coordination --write`.
- **Limitation:** the hook line is unchanged. Any useful clause pushes it past its 1,400-character test limit (see HOOK-REVIEW-CLAUSE).
- The `ki-delegation` run-report and footer-report sources are unchanged: the standard has the coordinator review a run report's queries when it receives the report, and a background agent does not launch the review itself.
- New judgment rubric item COORD-13 checks the review. The remediation-inventory counts went up by one to match. The standard's review history has a twenty-ninth entry.
- Harness commit `b04d0e72` is pushed fast-forward to origin/main. Tests and TypeScript pass, and the ki-skills audit passes. The ki-coordination audit shows only an existing COORD-3 warning about one folder in `+/_WORK_REVIEW/`.
- The REFRESH line is at the top of all nine `messages.md` queues, timed 19:17 BST and naming `b04d0e72`. In the queues of [ki.specifications](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.specifications/messages.md) and [ki.chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.chezmoi/messages.md), the line replaced the `None.` empty-queue marker.
- ki-principal commit `b13bb7da` is local and not pushed. Two other sessions' commits sit beneath it: `11f917dc` (ki.ways-of-working REFRESH-RESUMMARY) and `77bfc4f0` (ki.tools-burndown receive burndown).
- acquire commit `8a47423` is local and not pushed. Another session's commit `77d4979` (kb.regular.acquire-intake resume, send to owner) sits beneath it.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Pushing ki-principal (`11f917dc`, `77bfc4f0`, `b13bb7da`) and acquire (`77d4979`, `8a47423`) waits on the owner, because both repositories hold other sessions' commits.

## Queries

### HOOK-REVIEW-CLAUSE - whether the coordinator hook line should carry the query review

**Context:** QUERY-REVIEW-STANDARD named the hook line among the surfaces to regenerate, but the hook test limits it to under 1,400 characters. It is already about 1,370, and a clause naming which queries go to review needs about 90 more. The standard and the output style both carry the rule, and the hook's fourth hard rule already points coordinators at the owner-report shape that includes it. **Query:** Should the hook line stay without a query-review clause, or should its length limit be raised so it can carry one? **Options:** a) (recommended, confidence medium - the rule reaches every coordinator through the output style and standard; whether the hook matters is a judgment) leave the hook line as it is b) raise the hook test's limit to about 1,500 characters and add "every medium- or low-confidence or destructive query blind-reviewed once before it reaches the owner" to the fourth hard rule

### 🤖 → 👤 Handoff to supervisor · since 19:18 BST

👤 2 with you

- [with you] HOOK-REVIEW-CLAUSE · owner · since 19:18
- [with you] push ki-principal and acquire with other sessions' commits stacked · owner · since 19:18
- [committed] harness `b04d0e72`, pushed
- [unpushed] ki-principal `b13bb7da`, acquire `8a47423`
