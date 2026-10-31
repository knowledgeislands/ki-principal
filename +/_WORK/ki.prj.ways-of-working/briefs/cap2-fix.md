# Brief: cap2-fix

Work: ki.prj.ways-of-working; window AWAY-31-OCT. The full ki-agentic-harness audit fails one check, CAP-2: the generated skill catalogue in `skills/README.md` is stale. Two runs found this tonight, and it predates their changes.

Regenerate the catalogue with the harness's own documented generator. Find it in `package.json` scripts or `ki dev`; do not hand-edit. Change nothing else. Run the full audit and the tests; both must pass.

Work in your own worktree, fast-forward `main`, commit by explicit path and push fast-forward only. If the generator would change anything beyond the catalogue, stop and report instead. Report in plain English.
