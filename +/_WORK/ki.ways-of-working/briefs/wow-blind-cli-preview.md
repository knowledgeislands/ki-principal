# Blind review - CLI-PREVIEW

Read-only. Change no file. Do not read any work package, decisions log, queries file or run report; read only the standards and tool sources below.

## Context

Kris, 24 October 2026, on `mgit repair`: "I really don't think that `mgit repair` needs `--apply`. The other command line tools that can do a repair don't need a --apply ... do get rid of the --apply." That change is being made now in tools-mgit (repair writes by default, `--dry-run`/`-n` previews).

Two harness standards bear on it:
- `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-cli-conventions.md` (around lines 42-55) defines `-n`, `--dry-run` as "Report what would change without changing anything."
- `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/repo-structure/ki-repo-tools/references/standards-tool-repositories.md` (around line 152) says `repair`'s "default is a non-mutating preview, and writing requires an explicit option such as `--apply` or a reviewed proposal output."

A survey of `ki`, `mgit`, `rig`, tools-techne, tools-git-almanac and the harness scripts found preview defaults and flags differ widely: some commands write by default with `--dry-run`, some lack `-n`, some preview by default and need `--apply`/`--write`/`--fix`, some use `--check` for verification. The owner has asked that nothing be over-engineered.

## Query

How far should the preview-and-write convention go now?

Options, in no order:
- Change only the repair rule in the tool-repository standard so `repair` writes by default with `--dry-run`/`-n`, matching the owner's mgit decision; leave other commands as they are.
- Adopt one convention for all owned writers (write by default; `--dry-run` and `-n` preview; `--check` only for non-zero-exit verification; no `--apply`/`--write`/`--fix` as routine gates; named exceptions for deletion, uninstall and review-file flows), update both standards now, and roll it out to each tool through its owning work over time.
- Change nothing in the standards; treat mgit as a one-off.

Check the standards and a sample of tool sources yourself. Consider safety: where would writing by default be risky?

## Report

The run report the launcher names, first line `VERDICT: <repair-only|convention|nothing> · confidence <high|medium|low> - <one line>`; then reasoning in under 15 lines and any exception the chosen option must keep.
