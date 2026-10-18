# obs-mermaid - lift the Mermaid 12.1.0 hold in apps-observatory.local

Work: ki.observatory (KI > Model > Observatory), work file `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/work.md`.

Authority: Kris answered DEPS-HOLDS a) on 18 October in the ki.ways-of-working decisions log. The estate dependency run (`75af834`) held Mermaid at 12.1.0 in apps-observatory.local because 12.2.0 fails the third-party notices test, `THIRD-PARTY-NOTICES.md` recording 12.1.0.

Task, in `/Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local` only:

1. Find where the hold is declared (dependency manifest, lockfile, any update-tool pin or ignore) and lift it so Mermaid resolves to 12.2.0.
2. Refresh `THIRD-PARTY-NOTICES.md` for Mermaid 12.2.0 with the repository's own generator or script if one exists, by hand only if none does, and include any transitive licence changes the bump brings.
3. Run the repository's full gate (lint, typecheck, tests, build, the third-party notices test). Fix only what the bump itself breaks; anything larger stops the run and becomes a query.
4. Commit by explicit path under ki-git, one Conventional Commit. Push fast-forward only if your commit alone is stacked on origin; otherwise name the stacked commits and leave the push.
5. Do not restart the Observatory service; that stays interactive with Kris.

Report to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.observatory/obs-mermaid.report.md` in owner-report shape (Done, In Progress, Queries), naming the gate result, the commit, whether it was pushed, and that a service restart is pending.
