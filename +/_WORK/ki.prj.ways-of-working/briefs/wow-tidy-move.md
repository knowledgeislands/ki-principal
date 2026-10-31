# Brief: wow-tidy-move (ki.prj.ways-of-working)

Repository: `/Users/krisbrown/kis/knowledge-islands/ki-principal`. Package: `+/_WORK/ki.prj.ways-of-working/`. The repositories moved wholesale on 31 October 2026 from `~/workspaces/<territory>/` to `~/kis/<territory>/`; `~/workspaces/knowledge-islands` no longer exists.

1. Repoint absolute links in this package's five files and `design/` from `/Users/krisbrown/workspaces/` to `/Users/krisbrown/kis/`, checking each new target exists; list any that do not and leave them.
2. Tidy the folder under `ki-work-package` "Tidying the work folder": many `*.report.md` files at the top level are untracked. For each report (tracked or not) and each brief in `briefs/` and `reports/`, delete it only if its outcome has a durable home (a record, `decisions.md`, the package or a commit) and its queries are already in `queries.md`; delete briefs whose report has been received. Do not delete `briefs/footer-rename.md` or `briefs/wow-tidy-move.md`. Leave any report whose outcome is not homed and list it. Review `design/` under the design-note guards; delete only graduated or recorded-superseded notes, keep anything in doubt.
3. `state.md` front matter says `with-worker`; keep it. Fix any other stale line in `state.md` you can prove stale.

Touch nothing outside this package. Commit by explicit path, `docs(work): ki.prj.ways-of-working tidy after move`, fetch and push `main` fast-forward only (never force, never `--no-verify`, never stash/rebase/reset; stop on divergence). Other sessions' untracked files elsewhere (for example `+/_WORK/ki.sop.main/*.report.md`) are not yours.

Report, as your run packet directs: what was deleted, kept and why, links repointed and broken, and any query in Context/Query/Options form.
