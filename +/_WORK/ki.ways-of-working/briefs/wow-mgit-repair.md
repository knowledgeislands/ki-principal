# mgit repair: write by default, drop --apply

Kris, 24 October 2026: "I really don't think that `mgit repair` needs `--apply`. The other command line tools that can do a repair don't need a --apply ... do get rid of the --apply."

Work in a worktree of `/Users/krisbrown/workspaces/knowledge-islands/tools-mgit` off current `origin/main`.

- Make `mgit repair` perform the recognised config repair and clone missing repositories by default.
- Add `--dry-run`/`-n` to preview, behaving exactly as `mgit register --dry-run` does (same wording style, writes nothing).
- Remove `--apply` entirely: no alias, no hidden option. An unknown `--apply` should fail like any unknown option.
- Keep every existing guard: never replace an existing repository path, never clone `../` members, validate the config repair before writing.
- Update help text, README, user guides, `docs/specs/` requirements and their `_Verify:_` tests, completions, and the changelog's unreleased section. Search the tools-mgit repository, the KI harness (`/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`), tools-rig and chezmoi (`/Users/krisbrown/.local/share/chezmoi`) for `mgit repair --apply` callers and list them in the report. Change callers only inside tools-mgit; for other repositories, report the exact lines to change.

Run the repository's full checks and normal hooks. Commit on the worktree branch, then fast-forward `main` in the primary checkout only if it is clean and has no rebase or merge in progress, and push `main` fast-forward. Never force, never `--no-verify`. No tag or release: both machines run local checkouts.

Smallest change that does the job; no new mechanisms.

## Report

The run report the launcher names, first line `VERDICT: <done|blocked> · confidence <high|medium|low> - <one line>`; then the commit, whether pushed, checks run, and the external callers found with file and line.
