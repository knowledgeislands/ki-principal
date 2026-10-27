---
note_type: streams/design
updated: 2026-10-26T21:50:00Z
author: Written with Claude
---

# mgit result cache

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-25 · **Subject repository:** knowledgeislands/tools-mgit, read only · **Review:** Codex, read only, merged below

Design note for MGIT-CACHE. Kris raised the idea at 08:21 GMT on 25 October as one for in due course, and at 08:22 asked that the analysis weigh ways that need no cache at all. The read-backs are in the [decisions log](../decisions.md). This note states the problem, carries Kris's proposal verbatim, grounds the design in how mgit works today, sets out the real alternatives, merges one independent review taken on Codex, and ends with a recommendation and the queries Kris must answer. It changes nothing in `tools-mgit`; anything to build goes there as a message once Kris decides. It graduates when Kris has answered its queries and the accepted shape is captured as a `tools-mgit` work record, and is deleted in the same change.

## Contents

- [Problem](#problem)
- [Owner's proposal](#owners-proposal)
- [Established facts](#established-facts)
- [What the cache would and would not buy](#what-the-cache-would-and-would-not-buy)
- [Alternatives](#alternatives)
- [Design of the cache, if built](#design-of-the-cache-if-built)
- [Agents and Kris](#agents-and-kris)
- [Review](#review)
- [Recommendation](#recommendation)
- [Queries](#queries)

## Problem

Across a set of seventeen to sixty checkouts, a sweep such as `mgit st` is followed, often within a minute, by an action on the few checkouts the sweep singled out: `mgit push` for the ones ahead, `mgit add`/`mgit ci` for the dirty ones, `mgit stash` before a rebase. mgit runs the second command in every checkout, although the first command has just shown that most of them printed nothing unusual. The cost is time, mostly network round trips for level repositories, and noise where the no-op output is not yet learned. Where the follow-up is not a harmless no-op on a clean checkout, such as `commit`, `stash`, `checkout -- .` or `reset`, running it everywhere is also a wider blast radius than the operator meant.

The information to narrow the second run already exists at the end of the first: mgit's own quiet classification names exactly the checkouts that differed from the learned normal. Today there is no way to hand that set back to mgit. `--json` lets a script read it out; nothing lets a script, or Kris, feed a set in.

## Owner's proposal

Kris, 2026-10-25, voice, as the brief carries it:

> when you do git commands often, especially on large sets, there's almost a wish to ... use some kind of cache mode ... if I could do an git st followed by an git push, realistically speaking, I just got the latest status ... mgit --to-cache st && mgit --from-cache push ... say there was 17 repos and only 3 of them had non-standard status responses, they would be added to the cache list as the candidates, and then effectively the from cache on the second request is filtering the push to just those repositories ... the cache should not last more than 5 minutes ... if the cache [has] expired ... you can still do [mgit st] and it works as standard ... if you've got an idea around how that could work or be improved on it, you could do a bit of a design mode on that.

And at 08:22 GMT, steering this design:

> is [there] a way we can do an alias around it or something, or is there a command or something that changes [the] cache's behaviour, so git's behaviour ... You should certainly consider that, without [needing] to use the cache mode, as well as part of the analysis.

## Established facts

All paths are in `tools-mgit` at `746a6cc`, version 0.18.0. Each fact was checked by the Codex review; its corrections are folded in.

- **Quiet is a first-class result.** `dispatch_captured` ([bin/mgit:3880](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L3880)) sorts every checkout into quiet, with output, or failed. Failure takes precedence; quiet means exit 0 and either no output at all or output matching a learned template. The closing line counts the three. "Non-standard status responses" in Kris's words is the union of with-output and failed. The review adds the qualification that this is a presentation classification: a checkout is non-quiet because its output did not match, not because mgit has established that it needs the next action.
- **`--json` already exports the set.** The same function prints, per checkout, `label`, canonicalised `path`, `exit`, `quiet`, `stdout` and `stderr`, plus a summary. A script can obtain the candidate paths today with `mgit --json st`; it needs `jq` or equivalent, which stays outside mgit's own Bash-and-Git dependency rule ([AGENTS.md](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/AGENTS.md)) but is fine in a caller's pipeline.
- **Nothing imports a set.** Selection is a workspace manifest or directory discovery, optionally replaced by one exclusive territory selector (`--territory`, `--estate`, `--principals`), then narrowed by repeatable `--filter PREFIX` on the directory basename ([bin/mgit:4099](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L4099)). Repository-owned symlink metadata and `--all-worktrees` also shape the final set. `--repo` is a usage error outside `register add/rm` ([bin/mgit:4145](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L4145)). There is no explicit-path selector for ordinary commands.
- **Selector conflicts and KI zero matches stop dispatch.** The README states that selected missing roots, zero matches and incomplete producer output stop dispatch for the KI selectors and filters, and selector conflicts are usage errors that run nothing. The review corrects the generalisation: an unfiltered empty discovery can reach captured dispatch with nothing to run, so "refuse rather than widen" is the tool's habit for selectors, not a universal empty-set rule.
- **`sync` is the command-aware form of "push what is ahead".** `sync_command` ([bin/mgit:2973](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L2973)) fetches every tracked branch in parallel, once per repository and remote, then per checkout compares `HEAD...@{upstream}` with `rev-list --left-right --count`, fast-forwards only-behind, pushes only-ahead, and skips dirty, diverged, detached and upstream-less branches with a reason. It has no push-only or pull-only switch and no way to skip the fetch, so it is not equivalent to a plain `push` sweep: it also pulls, and it will not push a dirty checkout that `git push` would.
- **`overview` reads ahead and behind locally.** It uses `status --porcelain=2 --branch` and `for-each-ref` with no fetch; counts describe the locally available tracking refs, as fresh as the last fetch ([bin/mgit:3186](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L3186)).
- **Learned templates are the only persistent state.** They live in `${XDG_CONFIG_HOME:-~/.config}/mgit/templates/`, one plain-text file per expanded command ([bin/mgit:3629](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L3629)). mgit uses no `XDG_STATE_HOME`, `XDG_CACHE_HOME` or `XDG_RUNTIME_DIR` today. On this machine `st`, `status`, `status --short --branch` and `branch` are learned; `push` is not, so a level `mgit push` prints `Everything up-to-date` in every checkout.
- **`-v` and `--json` bypass classification.** Verbose streams one checkout at a time with no quiet decision; `--json` reports `quiet` but hides nothing. `-R/--raw` commands never use templates.
- **Git aliases are expanded before template lookup**, so `st` and `status -sb` share one identity ([KI-TOOL-MGIT-CLI-031](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/ideas/KI-TOOL-MGIT-CLI-031-learn-command-shapes.md) documents the mechanism and its limits).
- **Runtime rules.** Bash 3.2 and Git only; mutating behaviour is verified in disposable repositories with isolated configuration; the roadmap ledger `CLI` is reserved through 031 and is advanced in its own commit before a record is written ([docs/roadmap/_ISSUES.md](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/_ISSUES.md)).
- **No Git setting known to this note makes `push` skip locally.** `git push` with nothing to send still contacts the remote and prints `Everything up-to-date`; `push.default` and `remote.pushDefault` choose where to push, not whether. A local "is anything ahead" test is `git rev-list --count @{upstream}..HEAD`, which `sync` uses in its two-sided form; an upstream count says nothing about a push that names a refspec, a tag or another destination.

## What the cache would and would not buy

Take the headline case, `mgit st` then `mgit push`, over a set where three checkouts are not level.

- **In the ordinary case the same checkouts get pushed with or without the cache.** `status -sb` prints `[ahead N]` for a branch ahead of its upstream, so an ahead checkout is in the candidate set, and `git push` in a level checkout pushes nothing. The review qualifies this: it holds when the learned `st` template is the plain level one, nothing moved between the two runs, and the push targets the compared upstream. Under those conditions the cache changes the number of no-op pushes, not the set of real ones.
- **What it saves is network time and noise.** Each no-op push is one remote exchange. With eight jobs a fifty-checkout set is expected to cost tens of seconds and the three candidates a few; these are estimates, not measurements, since this note made no remote calls. The noise it saves is already removable another way: `mgit learn push` over a level set records `Everything up-to-date` and makes those checkouts quiet.
- **What it protects is the follow-ups that are not no-ops.** `commit -am` exits 1 in a clean checkout and counts as failed; `stash` prints "No local changes to save"; `checkout -- .` and `reset --hard` act on whatever is there. For these, narrowing to the checkouts the sweep named is a scope control, not an optimisation, and it is where the idea earns its place. The review notes that a non-quiet sweep result does not prove the next command will fail harmlessly elsewhere; the narrowing is what makes the follow-up safe, not the no-op.
- **What it cannot do is make the sweep fresh.** A checkout that changed between the two commands, by another session committing or a fetch landing, is either a missed candidate or a candidate that no longer needs anything. The five-minute bound limits this but does not remove it; nor does a cached path freeze the branch or files acted on later. For `push` a missed candidate is harmless to the repository but not to the operator who believes everything is sent. For a destructive follow-up neither failure mode is harmless, which is why expiry must stop rather than widen.

## Alternatives

Six routes, of which the first three need no cache. Kris asked that these be weighed first.

### A. `mgit sync`, as shipped and with direction and fetch switches

`mgit sync` already does the headline case under its own policy: it decides from a fresh fetch which checkouts are only ahead and pushes exactly those, leaving dirty and diverged ones named. For "status then push" it is the right tool today, with two gaps: it also pulls, and it fetches every checkout first, which costs the round trips the cache was meant to save. A `sync --push-only` (and its twin `--pull-only`) and a `sync --no-fetch` that compares against the last fetched upstream, as `overview` does, would close both gaps without state. The review's reservation stands: `sync` is a synchronisation policy, it skips dirty checkouts that a plain `push` would push, and it says nothing about `commit`, `stash` or `checkout`.

### B. A raw per-checkout guard, with no change to mgit

mgit can already run a local check and act only where it passes, in one `-R` command. The review found the draft's first form masked push failures with a trailing `|| true`; the corrected form keeps a push failure visible:

```sh
mgit -R sh -c 'n=$(git rev-list --count @{upstream}..HEAD 2>/dev/null) || exit 0; [ "$n" = 0 ] && exit 0; exec git push'
```

Level checkouts and checkouts without an upstream exit 0 silently and are quiet; ahead checkouts push, and a failed push is counted as a failure. Tested read-only on this machine with `echo` in place of `git push` over ten checkouts: level checkouts quiet, and in an earlier run an ahead checkout named with its count. A shell alias such as `mpush` makes it one word, in chezmoi. This is Kris's "alias around it": it exists today, costs no network for level checkouts, and is exactly as safe as `git push` to the upstream. Its limits are one hand-written guard per intent, the guard and the action coupled in a quoted shell string, `-R` runs bypassing templates, and the upstream count not describing pushes with a refspec or tag. It is a good answer for push and a poor general mechanism.

### C. Teach `mgit push` to skip locally

Add a command-aware rule inside mgit: before `push`, test ahead-of-upstream and skip when zero. This contradicts the principle adopted with `learn` that mgit has no built-in idea of what a Git command's normal state is, and it is wrong for the many push forms that do not push the current branch: `push --tags`, `push origin feature`, `push -u`, `push --delete`, `push --force-with-lease` after a rebase that left the branch behind. `sync` is the sanctioned place for push-specific knowledge. Not recommended; the review agrees.

### D. Kris's proposal: `--to-cache` and `--from-cache`, one slot, five minutes

A run with `--to-cache` records its non-quiet checkouts; a later run with `--from-cache` selects only those. One implicit slot, written at the end of a captured run, expiring five minutes after the run began. Plain commands are unaffected. This is general across commands, two flags, and reads naturally with `&&`. Its open questions are what happens on expiry, how the slot is keyed so a different workspace or selector does not inherit a foreign set, whether failed checkouts count as candidates, and how two concurrent sessions share one slot. The design section below answers them; the review's position is that a shared implicit slot is not yet a reliable scope contract until the isolation and replay rules are specified.

### E. Named result sets

Generalise D to `--to-cache NAME` and `--from-cache NAME`, listed and forgotten like templates. Names carry intent (`dirty`, `ahead`, `release`), several can coexist, and agents or sessions in parallel do not collide. The cost is surface: listing, forgetting, naming rules, and whether a named set should expire at all. The review differs from the draft's "later" and says distinct names help from the moment D ships, since they are the isolation D lacks. This note takes that: an optional name on both flags is in the first cut, with a default slot for the two-word form; listing and forgetting can wait.

### F. Explicit path list in, from a file or stdin

Add a selector that takes checkout paths, `--repos-from FILE` or `--repos-from -`, NUL- or newline-separated, exclusive with the territory selectors and narrowed by `--filter` as usual. With `--json` already exporting paths, this closes the import gap statelessly and composes with any tool. Agents prefer it: no hidden state, the set is visible in the transcript, and two sessions cannot interfere. For Kris at a prompt it needs a pipeline or `jq`, so it does not replace D; it is the primitive D is sugar over, with `--to-cache` meaning "write the non-quiet paths to the slot file" and `--from-cache` meaning "`--repos-from` the slot file, if fresh and from this selection".

### Weighing them

| Route | Needs state | Covers | Stale risk | Change to mgit |
| --- | --- | --- | --- | --- |
| A sync, direction and fetch switches | none | push, pull under sync's policy | none with a fresh fetch; last fetch under `--no-fetch` | small, inside `sync` |
| B raw guard alias | none | push, anything with a local test | none | none; a dotfiles alias |
| C push skips locally | none | push to upstream only | none | small but against principle |
| D to/from cache, one slot | one slot file | any command | bounded by TTL; shared slot | moderate: two flags, slot file, expiry, key |
| E named sets | files | any command | bounded by TTL; isolated by name | D plus a name; list and forget later |
| F paths from file or stdin | none | any command | caller's | small: one selector |

## Design of the cache, if built

Routes F, D and the name from E are designed together, F as the primitive and D as the two-flag convenience. Each point records the review's mark and any change it caused.

1. **Candidates are the non-quiet checkouts.** `--to-cache` records every checkout the run classified as with output or failed, in selection order, by canonical checkout path. Quiet checkouts, by template or by silence, are left out. A run with no templates for its command therefore caches the whole set, which is correct and visibly so. The review differs on wording only: the set is "checkouts whose output did not match", and the documentation must say so rather than "checkouts that need the next command".
2. **Failed checkouts are included, by default.** A sweep that failed in a checkout has not shown it is normal. Including it means the follow-up runs there too, which is loud and, for a read or a push, harmless to the repository. The review would not call it harmless in general and asks the owner whether a failed inspection should stop the chain, be excluded, or be included. It is a query; note that the sweep's own exit 1 already stops Kris's `&&` chain when any checkout failed, which is a further reason the slot must be written whatever the exit status, so that `;` or a second command can still use it.
3. **Written only from a captured run.** `--to-cache` requires the default captured mode. With `-v` there is no classification, so `--to-cache -v` is a usage error. With `--json` it is allowed and the JSON document stays pure, the age and count lines going to standard error. With `--learn` it is allowed and records the classification made with the templates that existed before the learn. With `-R/--raw` it is allowed and records every checkout with output or failure, since raw runs have no templates. Agreed by the review.
4. **One slot file per name under the cache home.** `${XDG_CACHE_HOME:-~/.cache}/mgit/sets/<name>`, default name `last`, plain text, in the style of a template: a `mgit-set: 1` version line, then `started: <epoch seconds>`, `command: <printed command>`, `selection: <key>`, `count: <n of m>`, then one `path: <canonical path>` line per candidate, no other content. Written to a temporary file in the same directory and renamed into place, with user-only permissions. A reader validates the version line, every field and every path before dispatching anything, and never evaluates metadata. Changed after review: version line, start time rather than write time, strict validation, private permissions.
5. **Selection key and membership.** The key records the producer's selection: the workspace manifest path or discovery root, or `territory:<handle>`, `estate` or `principals`, plus its filters, worktree mode and symlink mode. `--from-cache` refuses, with one error line naming both, when the reader's root selector differs. It then resolves the current selection and checks that every cached path is a member of it today, stopping on the first that is not, so a manifest or registry change since the sweep is caught rather than replayed. Reader-side `--filter` narrows the cached set as an intersection; the producer's filters are kept as identity, not compared for equality. Changed after review, which showed a root key alone does not prove the same membership and that ordered-filter equality conflicts with reader narrowing.
6. **Expiry is five minutes from the sweep's start, fixed, and stops the run.** `--from-cache` with a set whose `started` is older than 300 seconds, or no set at all, stops: `mgit: set 'last' from 'st' is 7m12s old (limit 5m); re-run with --to-cache` on standard error, exit 2 as a usage error, nothing dispatched. A set that exists, is fresh and is empty runs nothing and says so, exit 0: an empty set is a valid result, never "all". It never falls back to the full set. Plain `mgit push` remains one word away. Kris's words allow the other reading, so the stop is a query. Changed after review: age measured from the run's start, since a slow sweep can take minutes; empty-but-valid distinguished from missing; usage-error exit status.
7. **Age is always shown.** A `--from-cache` run prints one line on standard error before its results, `mgit: 3 of 17 repositories from 'st' 42s ago`, so the operator sees how old the set is and what produced it, and JSON output stays pure. `mgit --from-cache` with no command lists the cached checkouts, as `mgit` alone lists the selection, so the set can be inspected before acting. Agreed by the review.
8. **Invalidation by content is deferred.** Recording `HEAD` and the index mtime per candidate at write time can detect that a candidate changed since, but cannot detect a quiet checkout becoming non-quiet, which is the dangerous direction, without re-running the sweep. The TTL bounds both without protecting against either; the documentation says so plainly. A later refinement could warn when a candidate's `HEAD` moved. Agreed by the review.
9. **`--to-cache` and `--from-cache` compose, as a filter.** `mgit --from-cache --to-cache ci -am "wip"` narrows to the cached set, runs, and rewrites the set with the checkouts that were non-quiet under `ci`. The review differs on what that means: the new set is "checkouts whose `ci` output did not match a template", which is a filtering operation, not a record of checkouts successfully committed. Chained narrowing is kept, documented in those words, and a `st` → `ci` → `push` chain is shown as an example of narrowing, not as a guaranteed pipeline.
10. **Concurrency by name.** Two sessions in one cache home share the default set `last`; the selection key stops cross-workspace mistakes but not two sessions in one workspace, and atomic rename prevents torn files, not replacement between two invocations. The review asks that each workflow be isolated before D ships. Taken: `--to-cache NAME` and `--from-cache NAME` are in the first cut, so an agent or a second terminal names its set; the default `last` serves the two-word form at Kris's prompt.
11. **`--repos-from` is the primitive.** `--repos-from FILE|-` reads newline-separated checkout paths, or NUL-separated with `--repos-from0`, reads the whole input before dispatching, deduplicates, resolves each path to a member of the current selection without following symlinks beyond what the selection already did or adding sibling worktrees, and stops with an error naming the first path outside the selection. It is exclusive with `--territory`, `--estate` and `--principals`. `--from-cache` is implemented as `--repos-from <set file>` with the version, freshness, key and membership checks in front. Changed after review: explicit framing, full-input validation, membership scope.
12. **Completion and help.** The options join `mgit help`, the manual, Bash and Zsh completion, and the user guide's "Run commands" page; a short "Status then act" example sits beside `sync` and states `sync`'s trade-offs accurately, so the reader picks `sync` for synchronisation and the set for the rest. Agreed by the review.
13. **Verification.** Bats fixtures in disposable repositories: a sweep over three checkouts with one dirty writes one path; `--from-cache` runs only there; a foreign key, a path no longer in the selection, a missing set and a backdated `started:` each stop with the named error; a fresh empty set runs nothing with exit 0; `--to-cache -v` is a usage error; `--repos-from -` with a path outside the selection stops before dispatch; chained narrowing replaces the set; a failed sweep still writes the set and exits 1; `--json --to-cache` emits a parseable document with the age line on standard error; two names coexist; an interrupted producer leaves the previous set intact. Extended after review.

## Agents and Kris

Kris at a prompt wants the two-word form: `mgit --to-cache st && mgit --from-cache push` for an arbitrary follow-up, `mgit sync` for synchronisation, and the `mpush` alias from route B for a quick push that costs nothing to adopt today. Agents under the harness mostly run mgit in captured or `--json` mode and keep their reasoning in the transcript; for them hidden state between steps is a liability, since a parallel run can overwrite a default set and a reader of the transcript cannot see what the set was. Agents should prefer `--json` plus `--repos-from -`, or a named set when a set must survive several steps in one session, naming it after the run. The coordinator standard's quiet-tools rule is unaffected: a `--from-cache` run's age line is one more line of ordinary standard error. Where agents sweep an estate for the owner, `mgit sync` and `mgit overview --json` remain the tools of record, as today.

## Review

One independent review was taken on Codex (GPT-6, high reasoning effort), read-only, with the draft and `tools-mgit` as its only inputs and the recommendation and queries withheld. Its own view: the request is to reuse an observed selection, not to establish which action is currently necessary; F should be the primitive, A suits synchronisation under its own policy, and D is convenient but a shared implicit slot with a five-minute lifetime is not a scope contract. Its recommendation was F first, A for those who want sync's policy, and D deferred until workflow isolation and replay validation are specified, at high confidence.

| Point | Codex | Settlement and evidence |
| --- | --- | --- |
| A | Differ | Taken as a qualification: `sync` pulls and skips dirty checkouts, so it is a policy, not a push sweep. Route A now says so. `bin/mgit:3081`, `3109`. |
| B | Differ | Taken: the draft's `\|\| true` masked push failures. The guard is corrected to exit 0 only when there is nothing to push. |
| C | Agree | Not recommended. |
| D | Differ | Taken in part: D ships only with the key, membership check, stop-on-expiry and a name (points 5, 6, 10). The reviewer would still defer D; this note recommends shipping it with those rules, see Recommendation. |
| E | Differ | Taken: an optional name is in the first cut as D's isolation; list and forget wait. |
| F | Agree | The primitive. |
| 1 | Differ | Taken as wording: "output did not match", not "needs the next command". |
| 2 | Differ | Open: failed checkouts in or out goes to Kris as MGIT-CACHE-FAILED. |
| 3 | Agree | Kept; JSON purity added. |
| 4 | Differ | Taken: version line, strict validation, private permissions; atomicity alone does not make a bad file harmless. |
| 5 | Differ | Taken: membership validated against today's selection; producer filters kept as identity; reader filters intersect. |
| 6 | Agree | Kept; exit 2 for the usage error, exit 1 reserved for command failures. |
| 7 | Agree | Kept; diagnostics on standard error. |
| 8 | Agree | Kept; the documentation states what the TTL does not protect. |
| 9 | Differ | Taken as wording: chaining is a filter, not a success record. |
| 10 | Differ | Taken: a name isolates each workflow from the first cut. |
| 11 | Agree | Kept; full-input validation, framing and membership scope spelled out. |
| 12 | Agree | Kept; accurate `sync` trade-offs. |
| 13 | Agree | Kept and extended with the reviewer's cases. |
| Add | - | A failed sweep exits 1 and stops an `&&` chain: noted under point 2; the set is written regardless. |
| Add | - | Empty-but-valid set is distinct from missing and never means all: point 6. |
| Add | - | Interrupted producers and write failures never publish a partial set; the previous set stays: points 4 and 13. |
| Add | - | Replay exact paths without widening through symlinks or sibling worktrees: point 11. |
| Add | - | Bound observation age from the sweep's start, not its write: point 6. |
| Add | - | Test JSON purity, quiet successes, concurrency and path cases: point 13. |

The one unsettled difference is whether D ships in the first cut or follows F and A. The reviewer's reason is that the next command's scope should not depend on a shared implicit slot. This note's reason for shipping D now is that Kris's stated use is the two-word form at a prompt, that F alone gives Kris nothing without `jq`, and that the key, membership check, stop-on-expiry and optional name answer the reviewer's concern within the same change. Both views are given to Kris under MGIT-CACHE-SCOPE.

## Recommendation

Build routes F and D together in `tools-mgit`, with the name from E, as one work record: `--repos-from` as the stateless primitive, `--to-cache [NAME]` and `--from-cache [NAME]` as the convenience over it, under the thirteen design points above. Add the `sync` direction switches, `--push-only` and `--pull-only`, as a second, independent record, and leave `--no-fetch` for later. Reject C. Adopt B today as an `mpush` alias in chezmoi, since it costs nothing and covers the push case until the record ships, and learn `push` over a level set so a plain `mgit push` is quiet. Nothing here is built until Kris decides; the accepted shape goes to `tools-mgit` as a `messages.md` line for it to capture under its own ledger, which reserves `CLI` through 031.

## Queries

### MGIT-CACHE-SCOPE - what to build first

**Context:** Six routes were weighed. The Codex review and this note agree that `--repos-from` (F) is the right primitive and that teaching `push` to skip (C) is wrong. They differ on timing for the two-flag cache (D): the reviewer would ship F and the `sync` switches first and defer D until isolation is specified; this note says the selection key, membership check, stop-on-expiry and an optional set name specify it, and that F alone gives you nothing at the prompt without `jq`.

**Query:** Which shape goes to `tools-mgit` as the first record?

**Options:** a) (recommended, confidence medium - the reviewer disagrees on timing, agreeing on everything the first cut would contain) F and D together with an optional name, one record; `sync --push-only` and `--pull-only` as a second record. b) F and the `sync` switches first; D as a later record once F has been used. c) D alone as you proposed, one default slot, no `--repos-from` and no name.

### MGIT-CACHE-EXPIRY - what `--from-cache` does when the set is missing or older than five minutes

**Context:** Your words were that after expiry "you can still do mgit st and it works as standard", which is true of the plain command either way. The open point is the flagged command. mgit's habit is to stop on selector conflicts and KI zero matches rather than widen; a `--from-cache reset --hard` that silently ran everywhere would be the worst outcome of the feature. The reviewer agrees that missing or expired state must stop.

**Query:** When the set is missing or expired, does `--from-cache <command>` stop with an error, or run the full set with a warning?

**Options:** a) (recommended, confidence high - reviewed; stopping is the only safe behaviour for a destructive follow-up and costs one re-run) Stop with a one-line error naming the set's age and the fix, exit 2, nothing dispatched; a fresh empty set runs nothing and exits 0. b) Warn and run the full selection, as plain `mgit <command>` would.

**Decided:** Kris took a) on 26 October 2026, read back in the [decisions log](../decisions.md): when the set is missing or expired, `--from-cache <command>` stops with a one-line error naming the set's age and the fix, exits 2 and dispatches nothing; a fresh empty set runs nothing and exits 0. Nothing is built until MGIT-CACHE-SCOPE is answered.

### MGIT-CACHE-FAILED - whether a checkout whose sweep failed is a candidate

**Context:** A sweep can fail in a checkout, for example on an `index.lock`, a missing upstream or a broken worktree. The draft includes such checkouts in the set, since they have not shown they are normal, and the follow-up would then run and most likely fail there too, loudly. The reviewer points out that a failed inspection does not prove the next command fails harmlessly, and that the sweep's own exit 1 already stops an `&&` chain, so you would only reach `--from-cache` by `;` or a second command.

**Query:** Are failed checkouts included in the cached set?

**Options:** a) (recommended, confidence medium - the reviewer left it open; inclusion keeps the set a superset of what needs attention, and the sweep's exit status already warns you) Include them, and show the count of failed candidates in the age line. b) Exclude them, so the set holds only checkouts that ran and printed something. c) Make `--from-cache` refuse to run while the set records any failed checkout, until the sweep is repeated clean.

### MGIT-CACHE-TTL - whether five minutes is fixed

**Context:** You set "not more than 5 minutes". The draft fixes 300 seconds from the sweep's start, with no option, so the behaviour is the same on every machine and in every script. A configurable limit would need a setting home mgit does not yet have beyond templates.

**Query:** Is the five-minute limit fixed, or configurable?

**Options:** a) (recommended, confidence high - one constant, no new configuration surface, and your words set the bound) Fixed at five minutes from the sweep's start. b) Configurable, with five minutes as the default, by an environment variable or a future `mgit` setting.

**Decided:** Kris took a) on 26 October 2026, read back in the [decisions log](../decisions.md): the limit is fixed at five minutes from the sweep's start, one constant with no setting. Nothing is built until MGIT-CACHE-SCOPE is answered.

### MGIT-PUSH-ALIAS - adopting the no-cache push guard today

**Context:** Route B is a one-line `mgit -R sh -c '...'` guard that pushes only checkouts ahead of their upstream, costs no network for level ones, keeps push failures visible, and needs no change to mgit. Tested read-only on this machine. It would live in chezmoi as an alias such as `mpush`, handed to the ki.chezmoi work as a message.

**Query:** Do you want the alias now, independent of what `tools-mgit` builds?

**Options:** a) (recommended, confidence high - zero cost, available today, and it remains useful after the cache ships) Yes: hand the alias to ki.chezmoi as a `messages.md` line, and learn `push` over a level set so a plain `mgit push` is quiet. b) No: wait for the `tools-mgit` record.

**Decided:** Kris took a) on 26 October 2026, read back in the [decisions log](../decisions.md): the route B guard goes to ki.chezmoi as an `mpush` alias, sent as a line in that work's `messages.md` the same day by run wow-harness-b; teaching `mgit push` to be quiet over a level set waits for the `tools-mgit` record under MGIT-CACHE-SCOPE.
