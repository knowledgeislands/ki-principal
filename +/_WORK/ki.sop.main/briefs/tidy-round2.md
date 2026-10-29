# tidy-round2: act on the TIDY lines in State of play's tended works

Authority: ki-principal only, under Kris's BASELINE-CLEAN of 28 October ("optimize those work packages down ... really nice clean baselines") and the AWAY-WINDOW grant of 29 October. Commit per package by explicit path (`docs(work): <id> tidy`), push fast-forward only; never force, `--no-verify`, stash, rebase or reset; stop on divergence. Never answer, decide or drop a query; never release a hold; never send outside ki-principal. Delete only what `ki-work-package` tidy rules clearly allow; keep anything in doubt.

Works: ki.prj.agent-host, ki.prj.baseline-rollout, ki.prj.chezmoi, ki.prj.estate-factorisation, ki.prj.mac-studio-setup, ki.prj.paperclip-capture-and-rebuild, ki.prj.portable-specifications, ki.prj.timelines, ki.prj.tools-burndown, ki.prj.website and ki.reg.main, all under `+/_WORK/`. Skip ki.prj.observatory and ki.prj.ways-of-working entirely, and skip any package with uncommitted changes you did not make.

For each work, take its `messages.md` TIDY line from State of play (sent in d77efdf9): make the mechanical fixes the `ki-work-package` rubric flags (front matter shape, headings, line form, stale ids, homed reports and received briefs), log one disposition line in its `decisions.md` and remove the TIDY line in the same commit. Fixes needing judgement or an owner become one line in that work's `state.md` Outstanding, not a query. Then re-run the package check across `+/_WORK/` and give before and after failure counts per work.

Finally delete by explicit path `+/_WORK/ki.sop.main/resolve-close.report.md` and this brief, and commit `docs(work): ki.sop.main receive resolve-close`.

Report to `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/tidy-round2.report.md`, under 500 words, owner-report form. Plain British English, no em-dashes.
