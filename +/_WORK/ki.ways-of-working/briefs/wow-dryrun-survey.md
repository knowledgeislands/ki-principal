# Survey: how the KI command-line tools preview and write

Read-only. Change no file in any repository.

Kris, 24 October 2026: "can we look and see where we're using this dry run consistently?"

Survey every command that writes, repairs, migrates, installs, prunes or applies in: tools-ki (`ki`), tools-mgit (`mgit`), tools-rig (`rig`), tools-techne, tools-git-almanac, and the KI harness scripts (`ki-agentic-harness/scripts`, its `bun run` scripts), all under `/Users/krisbrown/workspaces/knowledge-islands/`. Read the help (`--help`) and source, not memory. Note that `mgit repair --apply` is being removed now, so record mgit as it will be: repair writes by default with `--dry-run`/`-n`.

For each command record: default behaviour (writes or previews), the preview flag (`--dry-run`, `-n`, `--check`, `--plan`, none), any opt-in write flag (`--apply`, `--write`, `--fix`, `--yes`), and whether short `-n` exists.

Also check whether Engineering Practice in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Engineering Practice/` or the harness command-line conventions already state a rule.

## Report

The run report the launcher names, first line `VERDICT: <consistent|inconsistent> · confidence <high|medium|low> - <one line>`. Then:

- a compact table, one row per command;
- the outliers, grouped;
- any existing written convention, quoted with its path;
- a proposed one-paragraph convention (the expected one: write by default, `--dry-run`/`-n` to preview, with `--check` only for a non-zero-exit verification mode), and the smallest list of changes to reach it, per repository. Flag any command where writing by default would be unsafe and say why.

Keep it short; no new mechanisms.
