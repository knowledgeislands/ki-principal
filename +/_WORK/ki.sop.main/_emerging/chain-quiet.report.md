# [KI > SoP](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.sop.main/work.md) › State of play › chain-quiet

**🤖 → 👤 Handoff to supervisor · Run report at 04:14 GMT · last mark 00:03 GMT**

---

## Done

- **Quiet chain output (CHAIN-QUIET a)), commit `0d21c2c`, published to tools-mgit `main`.** `mgit chain` now leaves out every repository where all steps succeeded and nothing was printed, the way ordinary mgit commands do. The closing line counts them, as in `3 completed (3 quiet), 0 stopped, 0 failed to start`. `-v` and `--json` still show every repository; the JSON also gains a quiet flag on each repository and a quiet count in its summary. The usage text, manual, README, running-commands guide, MGIT-WS-028 and changelog say so.
- **A checkout that cannot be entered (CHAIN-START-ENTER a)).** It already counted as "failed to start", so the behaviour is unchanged. A new test now proves it by moving a repository away mid-run.
- **[KI-TOOL-MGIT-CLI-032](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md) updated.** Its Discussion records both decisions, and the outstanding concern about every repository being shown is removed. The way a first step that runs and fails is counted is left as built, because CHAIN-START-FIRST is still open with you. The record stays Awaiting review.
- **Checks:** shellcheck, `bash -n`, mandoc lint, `git diff --check`, rumdl and `ki repo audit` all pass with no failures. The full Bats suite passes 153 of 154, including all ten chain tests. The one failure is a territory test that fails the same way on the unchanged previous commit. It comes from the installed ki 0.14.1 (CI pins v0.13.0), not from this change; see TERRITORY-TEST.

### Review prep: KI-TOOL-MGIT-CLI-032, chain Git commands

**What it does.** `mgit chain fetch --prune --then pull --ff-only --then push` runs those Git commands in order in each repository. A repository stops at its first failing step, so a repository whose pull failed is never pushed, while the others carry on. Repositories run in parallel. Only the ones that failed or printed something are shown, then one line says how many completed, stopped part-way or failed to start, and names each one that did not finish. A sequence you use often can be saved once, with `git config --global mgit.chain.tidy 'fetch --prune --then pull --ff-only'`, and then run as `mgit chain tidy` or just `mgit tidy`. A saved name never replaces one of mgit's own commands, and `-B` skips it.

**Evidence.** All seven steps in the record are ticked, and I found each in the code. Ten chain tests in disposable repositories cover: Git options passing through untouched; stop-at-first-failure with other repositories continuing; parallel and one-at-a-time runs; JSON; saved recipes with quoting; precedence and the `-B` bypass; usage errors; quiet repositories being hidden; and a repository that cannot be entered. In a scratch run of three clean repositories, `mgit chain fetch -q --then status --short` printed only `3 completed (3 quiet), 0 stopped, 0 failed to start`.

**Still open.** CHAIN-START-FIRST, whether a first step that runs and fails counts as "stopped" or "failed to start", still gates acceptance. A recipe saved only inside one repository is not seen when you run mgit from the workspace root, because recipes are read like Git aliases from where you run mgit.

**Try it yourself.** From your workspace root:

- Run `mgit chain fetch --then status --short`. Only repositories with local changes should appear above the tally.
- Run the same with `-v` and see every repository stream.
- Save `git config --global mgit.chain.tidy 'fetch --prune --then pull --ff-only'`, run `mgit tidy`, then run `mgit -B tidy` and see it go to Git instead.
- Run `mgit chain status --then` and get a usage error before anything runs.

### Review prep: KI-TOOL-MGIT-CLI-033, guard sync pushes

**What it does.** `mgit sync` now only fetches and fast-forwards. A branch with local commits that are not on the remote is not pushed. Instead it is named `ahead N, not pushed (pass --push)`, both as the run goes and in the closing list. `mgit sync --push` publishes such a branch. Setting `git config mgit.syncPush false` in a repository stops sync from ever pushing it, even with `--push` or `-i`, and a value Git cannot read as true or false blocks the push too.

**Evidence.** All four steps in the record are ticked. Two new tests and several adjusted ones cover: no push by default; pushing with `--push`; the veto beating `--push` and `-i --push` for false, true, unset and invalid values; `-i` alone never offering a push; and linked worktrees sharing their repository's veto. In a scratch run against a local bare remote:

- Plain `mgit sync` left the remote unchanged and said `ahead 1, not pushed (pass --push)`.
- With `mgit.syncPush false`, `mgit sync --push` still did not push and named the veto.
- With the veto removed, `mgit sync --push` pushed the commit.
- An unpushed branch alone left sync's exit status at 0.

**Worth knowing.** Because an unpushed branch does not fail the run, a script has to read the closing list to notice unpublished commits. A global `mgit.syncPush false` in your own Git configuration blocks pushes for every repository. That works, but it is a side effect rather than a designed feature.

**Try it yourself.** In a repository with one local commit ahead of its remote:

- Run `mgit sync` and see "not pushed (pass --push)".
- Run `git config mgit.syncPush false`, then `mgit sync --push`, and see it refuse.
- Run `git config --unset mgit.syncPush`, then `mgit sync --push -i`, and get asked before the push.

## In Progress

Nothing is running. Neither record has been accepted; both await your review. CHAIN-START-FIRST stays open with you and gates KI-TOOL-MGIT-CLI-032.

## Queries

### CHAIN-ENTER-LABEL - How a checkout that cannot be entered is shown

**Context:** Under CHAIN-START-ENTER a), a repository mgit cannot enter counts as "failed to start", as built. In the normal output, though, its first step is shown as `1 failed (exit 1)`, as if Git had run it, with the "could not enter" error printed above. In the JSON output the same step is correctly shown as not run. The tally entry reads `(step 1, exit 1)`. This affects [KI-TOOL-MGIT-CLI-032](/Users/krisbrown/kis/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-032-chain-command.md).

**Query:** Should a repository that cannot be entered show all its steps as "not run", with the tally saying it could not be entered, instead of a failed first step?

**Options:**

a) (recommended, confidence medium - the text output would match the JSON and say what really happened; it is a small change but not one the decision asked for, so I left it) Yes, as a small follow-up before acceptance.

b) Leave it as built; the error line above the steps already explains it.

### TERRITORY-TEST - One territory test fails with the installed ki

**Context:** The full test suite has one failure: `real producer blocks selected missing roots and missing member registrations before dispatch`, in `tests/territory-producer.bats`. It fails the same way on the commit before this work. It only runs when the installed `ki` 0.14.1 is used as the territory producer. CI pins ki v0.13.0, so mgit and the newer ki seem to disagree on how missing repositories are reported. Neither record touches this area.

**Query:** Should this be looked into as separate tools-mgit work?

**Options:**

a) (recommended, confidence high - it is real breakage against the ki you run, and it is outside both records under review) Yes: capture it as a new tools-mgit item to bring mgit and its territory tests in line with ki 0.14.

b) Leave it until CI's ki pin is next raised.

### 🤖 → 👤 Handoff to supervisor · at 04:14 GMT

🤖 0 running · 👤 2 with you

- [with you] CHAIN-ENTER-LABEL · owner · since 04:14
- [with you] TERRITORY-TEST · owner · since 04:14

🧵 ki.sop.main
