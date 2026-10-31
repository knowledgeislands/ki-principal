# Brief: top-level-cause (ki.prj.ways-of-working) - read-only diagnosis

Kris, 1 November 2026: "Under the work packages, directly, we're only meant to have five files ... we've still got reports being created at the same level as those five files. Can we understand why that is? And can we get those prioritized so that they're into the rules and skills and such, so that we stop making this happen?"

Observed: `ki agent launch` refuses a brief that names its own report path and says "an agent reports only to ~/.local/state/ki/agents/<run>/<name>.report.md, and the launcher homes it in <work folder>"; tonight's reports then appeared as `+/_WORK/ki.prj.ways-of-working/<name>.report.md` at the top level, untracked. Across the territories, packages hold top-level `*.report.md` files (for example `+/_WORK/ki.sop.main/*.report.md` in ki-principal).

Find out, citing file and line:

1. Exactly which code homes reports (and anything else) at a work folder's top level: `tools-ki` (`/Users/krisbrown/kis/knowledge-islands/tools-ki`, look at `ki agent` launch, wait, report homing, `ki agent home`), and any harness hook or script.
2. What the `ki-work-package` and `ki-coordination` standards and `ki-delegation` say a work folder may hold (the closed list) and where reports, briefs and design go; whether they contradict each other or the tool; and whether the `ki-work-package` audit rubric flags top-level extras as FAIL or only WARN, and why it did not stop this.
3. Whether `.gitignore` rules (e.g. `reports/` ignored at any depth) push reports to the top level.
4. A count, per repository under `/Users/krisbrown/kis/*/`, of work folders with files other than the five package files at their top level.
5. The open LAYOUT-SHAPE question (`+/_WORK/ki.prj.ways-of-working/design/package-layout/design.md`) proposes three layouts; say which minimal fix works under the current kind-first folders (`briefs/`, `design/`, `reports/`) without pre-empting it.

Propose the smallest change set that stops it, split by owner: the harness skills (this work owns `ki-work-package`, `ki-coordination`, `ki-delegation`), tools-ki (owned by ki.prj.tools-burndown, reached by a `messages.md` line), and a one-off sweep. Change nothing; commit nothing. Report as your run packet directs, with any decision Kris must make as a query in Context/Query/Options form.
