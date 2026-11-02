# Brief: handover of ki.prj.mac-studio-setup to the household works

## Authority

Kris's word on 1 November (HANDOVER-HOUSEHOLD, ASSISTANT-NOW, FOCUS-ASSISTANT and the quick answers in ki-principal `+/_WORK/ki.prj.ways-of-working/decisions.md`): Mac Studio setup hands over to the household works (household-sol and household-terra, moving into the chezmoi source). This package must write a short handover note (what is open, what is owed, who takes each), send it as a message line to personal.reg.rig-terra (becoming personal.reg.household-terra), then go on hold pending close-out. Kris asked on 2 November whether this work had been wrapped up or moved.

## Do

1. Take stock, read-only, of every item in `+/_WORK/ki.prj.mac-studio-setup/`: each Open and Parked query in `discussions.md`, each Now, Next-step and Held line in `state.md`, each retained Rig line in `messages.md` (not the REFRESH or HANDOVER lines), and the files in `setup/`. Check each against current evidence: tools-rig roadmap and `_IDEAS.md` and git log (`~/kis/knowledge-islands/tools-rig`), chezmoi (`~/.local/share/chezmoi`, PERSONAL-DOTFILES-UE-086), ki-principal's other packages (notably ki.sop.main `discussions.md`, which already judges RIG-TRIAGE, SOL-SOURCES, SOL-HNR-HARNESS, SOL-KI-CONFIG-DRIFT and FW-LIVE obsolete, OLD-ORPHANS and ADOBE-SCRIPT-HOME), personal-principal's personal.reg.rig-terra / household packages, and read-only live sol state (`rig status`, `rig doctor`, OneDrive folders, `ki doctor`). Fetch allowed. No `rig apply`, no `sudo`, no machine changes.
2. Write `+/_WORK/ki.prj.mac-studio-setup/setup/handover.md`: a table of every item with verdict (`settled` by what, `superseded`, `partly`, `live`, `unknown`) and, for every item not settled, who takes it: household-sol, household-terra, the tools-rig owner, ki.prj.chezmoi, ki.sop.main, or Kris. Link records and files by absolute path. Plain English, British English, ASCII hyphens only.
3. Append one message line to the receiving work's `messages.md` in personal-principal (`~/kis/personal/personal-principal/+/_WORK/`: personal.reg.household-terra if it exists, otherwise personal.reg.rig-terra): `- IMPORTANT · <date> · HANDOVER-MAC-STUDIO · KI > Rig > Mac Studio setup (ki.prj.mac-studio-setup): ...` summarising what it now owns and linking the handover note by a pinned GitHub link to the ki-principal commit. If household-sol is a separate work that receives items, give it its own line too.
4. Commit each repository by explicit path only (handover note and brief in ki-principal; the messages line in personal-principal), Conventional Commits, `docs(work): ...`; pull fast-forward only and push fast-forward only; stop on divergence and report. Never stash, rebase, reset, force or use `--no-verify`. Do not touch any other file, and do not edit this package's `state.md`, `discussions.md`, `messages.md` or `decisions.md`; the coordinator puts it on hold.

## Report

Plain English: what was handed to whom, which items are already settled and can be closed, anything only Kris can answer (as queries with Context, Query and lettered Options, recommended first with confidence), and the commits.
