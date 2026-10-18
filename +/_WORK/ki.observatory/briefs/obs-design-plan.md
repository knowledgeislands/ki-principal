# obs-design-plan - plan the ki-design handoff in the Observatory roadmap

Work: ki.observatory (KI > Model > Observatory), work file and decisions log in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/`.

Authority: Kris, 18 October (DESIGN-APPLY in the decisions log): follow `-/observatory-handoff/INSTRUCTION.md` in knowledgeislands/ki-design (main): apply the design system to the Observatory as it is today, without losing any tab, route or capability, then converge on the restructure step by step with Kris. Plan the steps in the Observatory's own roadmap first; **build nothing** - Kris sees the plan before any build starts. PUSH-ALL also governs: lose nothing, choose between nothing; NO-MERMAID: draw no Mermaid.

Read: the instruction and everything it lists, from `origin/main` of the local clone `/Users/krisbrown/workspaces/knowledge-islands/ki-design` (fetch; do not change that checkout's branch or files); the current app, its specs, PDR-KI-OBSERVA-002 and its roadmap in `/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local`; the in-flight KI-OBSERVA-BRG-002 and the live-artifact design `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/design/live-artifacts.md` (the handoff's Extensions switchboard overlaps it).

Do, in apps-observatory.local only, through `ki-next` and `ki-plan`:

1. Map the handoff's four steps (tokens and glyphs; shell polish without regrouping; per-tab upgrades in place; converge) onto KI-OBSERVA-* records, one shippable record per step or per independent per-tab upgrade, with dependencies, acceptance criteria that keep every tab, route, `?view=` address and capability working, and the existing contrast, density and width tests passing unchanged.
2. Shape step 1 to Ready if it can be; leave the rest as Next or triage drafts. Step 4 records each say Kris approves each consolidation first.
3. Record where the board conflicts with what the app already does well (the app wins) as a list for the design thread; do not open issues in ki-design.
4. Carry the handoff's §11 open questions as queries, not decisions.

Never commit screenshots or real estate data. Commit by explicit path; push fast-forward only when your commits alone are stacked, otherwise name the stacked commits. No service restart.

Report to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/obs-design-plan.report.md` in owner-report shape: the plan as a short ordered list of records with their links and one line each, the app-wins list, and Queries (each with Context, Query, lettered Options, recommended first with confidence), including the §11 questions.
