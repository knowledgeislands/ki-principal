# review-adobe: blind review of one question

Authority: read only. Change, commit and send nothing. Do not read any `queries.md`, `decisions.md` or `*.report.md` file anywhere. You may read `work.md`, `state.md`, `messages.md`, roadmap records and Git logs in `/Users/krisbrown/workspaces/knowledge-islands/` (notably `tools-rig`) and the chezmoi source at `/Users/krisbrown/.local/share/chezmoi`.

Context: work package `ki-principal/+/_WORK/ki.prj.mac-studio-setup/` holds `design/adobe-remove.sh`, a script that removes Adobe Creative Cloud leftovers from a Mac and only acts with `--apply` (dry run otherwise). Work folders have a closed list of allowed files, and a script breaks it, so the package cannot pass its check while the script sits there. No other repository holds the script. The rest of the Adobe clean-up (about 7.5 GB of data, and a restart) is parked with the owner. Rig (`tools-rig`) is the workstation tool and has a declared direction towards managing app removal on machines (ideas around machine management and app footprint), which it has not yet acknowledged for this case. chezmoi manages the owner's personal dotfiles and maintenance scripts.

Question: where should the script go?

Options (unranked):

- Route it to tools-rig as removal evidence for Creative Cloud, and delete it from the package once tools-rig holds it.
- Move it into the chezmoi source as a personal maintenance script.
- Delete it and leave the Adobe clean-up to an at-screen session, relying on Git history for the script.

Choose the option you recommend, with confidence (high, medium, low), a one-line reason and the evidence you checked. Report to `/Users/krisbrown/.local/state/ki/agents/ki-sop-main/review-adobe.report.md`. Plain British English, no em-dashes.
