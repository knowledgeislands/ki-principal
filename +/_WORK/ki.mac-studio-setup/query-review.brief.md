# query-review brief

You are a blind reviewer for the work `ki.mac-studio-setup` in Knowledge Islands Principal (`/Users/krisbrown/workspaces/knowledge-islands/ki-principal`), under the QUERY-REVIEW rule of the `ki-coordination` standard. For each query below, form your own view independently: choose the course you would recommend, give your confidence (`high`, `medium` or `low`) with a one-line reason, and say what evidence you checked. You see each query's context and options without the coordinator's recommendation, on purpose.

You may read anything in the repositories named below and run read-only Git commands (`git log`, `git show`, `git grep`, `git status`, `git fetch`). Do not edit, commit, push, delete or launch anything, apart from writing your report.

## SOL-FW-TEST - What this parked tag meant

**Context:** Kris parked a query tagged SOL-FW-TEST on 14 October. It was listed among the queries from the 14 October `old-trees` and `sol-build` run reports, but its text has been lost. Check `+/_WORK/ki.mac-studio-setup/` (all files and `design/`), `~/.local/state/ki/agents/mac-studio-setup/` and its `archive/`, `~/.local/state/ki/agents/mac-studio-bootstrap/`, and the Git history of ki-principal (`git log -S SOL-FW-TEST --all`), including the older `+/_CHECKPOINTS/` and thread files. Separately, the work holds a live firewall test on sol for KI-TOOL-RIG-CORE-047 (tailnet-only listener firewall, in `/Users/krisbrown/workspaces/knowledge-islands/tools-rig/docs/roadmap/`) until Kris is at sol's screen.

**Query:** Is SOL-FW-TEST the same thing as the held KI-TOOL-RIG-CORE-047 live firewall test on sol, or something else that is still open?

**Options:**

- Treat it as the held sol firewall test and delete the separate entry.
- Ask Kris to restate it from memory.
- If you find its text, say what it was and whether it is still open.

## PUSH-STACK - Push the stacked commits in ki-principal

**Context:** ki-principal's `main` is ahead of `origin/main`. Run `git -C /Users/krisbrown/workspaces/knowledge-islands/ki-principal fetch` and then `git log origin/main..main` to see the current stack. One commit is this work's own (`d7c4d4ef`, the ki.mac-studio-setup mark). The others belong to other coordinating sessions (ki.specifications, ki.observatory, ki.tools-burndown, ki.ways-of-working, and maybe more by now), some with agents still running. Kris's rule from 14 October: "each agent session commits its own work. And if there's a need or it has little confidence in the other commits that are stacked up with it, that's flagged to me, and I will then push if I'm happy with the push." Check whether the stacked commits look sound: touched paths, whether any is half-finished, and whether the pre-commit checks would pass.

**Query:** Should this session push the whole stack now, or leave the push to the sessions that own the other commits?

**Options:**

- Leave the push to the next owning session that pushes; this commit goes up with theirs.
- Push the whole stack now, fast-forward only.

## Report

Write `/Users/krisbrown/.local/state/ki/agents/mac-studio-setup/query-review.report.md`, starting with a `# query-review report` heading. Give one `##` section per tag with your recommended course, its confidence and reason, and the evidence you checked. Use British English and ASCII hyphens only. Do not commit it.
