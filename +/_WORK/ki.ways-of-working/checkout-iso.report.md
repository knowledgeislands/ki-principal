# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › checkout-iso

**🤖 → 👤 Handoff to supervisor · Run report at 02:36 BST · last mark 02:01 BST**

---

## Done

- Wrote [checkout-isolation.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/checkout-isolation.md), committed in ki-principal as `1d0a523e` by explicit path. The pre-commit and commit-msg hooks passed and the landed check passed. Not pushed: ki-principal is 10 commits ahead, and some of them are other sessions'.
- Incident map: the retros report 12 collisions plus 5 unpushed-stack incidents. Causes: shared index 4, `index.lock` 6, audits reading the live working tree 3, a work-ownership overlap 1. Some had more than one cause, and none came from a ref lock on `HEAD`. b) would have prevented 9 of the 12, and take-stock's a) 4. Neither would have prevented the stack.
- Measured b) on scratch worktrees of ki-principal and ki-agentic-harness, then removed both. Each took under 0.25 s to create, and their checkouts were 38 MB and 21 MB. The island pre-commit passed in 1.4 s and the harness pre-commit in 2.4 s. The harness suite gave the same result as on `main`: 1,302 pass and the 4 known hook tests fail. Neither main checkout was touched.
- What b) needs before it works: `node_modules` in each worktree (an APFS clone takes 1.5 s). The project skill links and the `ki` registry entry are missing in a worktree, which gives 8 extra audit failures. `ki agent launch` needs `--repo` set to the primary checkout. The disk is 94% full.
- A per-session index (`GIT_INDEX_FILE`) failed the test. With the real hooks it silently reverted committed changes twice, and every hook passed both times. A pathspec commit (`git add -- <paths>`, then `git commit -- <paths>`) swept nothing and left the shared index consistent, and a three-command check confirms the commit landed.
- Limits: the lint-staged stash cause in ki.timelines' incident is not verified. `bun install` in a worktree was not measured, because it could need the network. The scratch logs left in the run's temporary folder hold nothing that needs keeping.

## In Progress

Nothing is running.

Outstanding - no action requested now

- The worktree commits I made for the tests are unreachable objects in ki-principal's `.git` and will go at the next garbage collection.

## Queries

### CHECKOUT-ISOLATION - Stop sessions colliding in shared checkouts

**Context:** Most collisions come from sessions sharing one index and lock in a checkout. Separate worktrees remove those causes, and they are cheap: under a second to create and about 2 seconds of hooks. Take-stock's per-session index turned out unsafe: in testing it silently reverted committed changes twice, with every hook passing. A pathspec commit plus a check that the commit landed does what the per-session index was meant to do, without that risk. Putting coordinators in worktrees would reverse Kris's MAIN-NOT-WORKTREES ruling from 18 October ("you should be able to just work on the main"). It would also stop routed messages, state changes and Obsidian from showing until each merge. Neither course fixes the unpushed stack, which is a push-policy matter.

**Query:** Should sessions be kept apart with a staged mix, with worktrees everywhere, or with no technical change?

**Options:**

a) (recommended, confidence medium - the mechanisms were measured directly, but merge cadence in a knowledge base and the pilot's real collision rate are untested) A staged mix. Now: a `ki` commit helper using the pathspec form and the landed check, and a `ki-git` rule against plain commits and private indexes in shared checkouts. Also now: worktrees with serial local merging for every writing run in code repositories, and audits that judge a run read committed state. Then a one-week pilot of worktrees for long, multi-file knowledge-base runs, with coordinators and short runs staying on `main`. Extend to b) if lock waits in ki-principal continue.

b) The blind review's course: every coordinator session and writing run in every repository gets its own worktree, with serial, verified merging into `main`. This needs `ki` to support worktrees (registry, skill links, `--worktree`, an integrate step) before it starts, and it reverses MAIN-NOT-WORKTREES.

c) One owning session per checkout per night, and no technical change.
