# Brief: accept-by-criteria

Work: ki.prj.ways-of-working. Read "Owner answers during AWAY-31-OCT" (ACCEPT-BY-CRITERIA) at the end of `decisions.md`, and every query under `## Open` in `queries.md`.

For each query, test the four criteria strictly and in plain English:

1. high confidence;
2. every reviewer named in the Context agreed, so any design review or blind review that preferred another option fails it;
3. not contentious;
4. easily undone, so anything that changes published history, deletes material, renames widely or changes security posture irreversibly fails it.

When in doubt, fail it.

For each query that passes, append to `decisions.md` one line: the tag, "a) taken under ACCEPT-BY-CRITERIA", the option's text in short, and the one-line reason it passes. Then move the query from `## Open` to `## Answered` as a one-line pointer.

For each query that fails, leave it open and add one plain-English line to its Context saying which test it failed.

Do not act on any accepted option. Write `design/window-31-oct/accepted.md` listing every accepted query in execution order: its owner work, the repository, what doing it means, its size, and what it waits on. Prefer small units done one at a time.

Commit `decisions.md`, `queries.md` and that file by explicit path, subject `docs(work): ki.prj.ways-of-working accept by criteria`, and push fast-forward only.
