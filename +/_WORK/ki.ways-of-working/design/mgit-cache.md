---
note_type: streams/design
updated: 2026-10-25T09:40:00Z
author: Written with Claude
---

# mgit result cache

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-25 · **Subject repository:** knowledgeislands/tools-mgit, read only

Design note for MGIT-CACHE. Kris raised the idea at 08:21 GMT on 25 October as one for in due course, and at 08:22 asked that the analysis weigh ways that need no cache at all. The read-backs are in the [decisions log](../decisions.md). This note states the problem, carries Kris's proposal verbatim, grounds the design in how mgit works today, sets out the real alternatives, merges one independent review, and ends with a recommendation and the queries Kris must answer. It changes nothing in `tools-mgit`; anything to build goes there as a message once Kris decides. It graduates when Kris has answered its queries and the accepted shape is captured as a `tools-mgit` work record, and is deleted in the same change.

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

Across a set of seventeen to sixty checkouts, a sweep such as `mgit st` is followed, often within a minute, by an action on the few checkouts the sweep singled out: `mgit push` for the ones ahead, `mgit add`/`mgit ci` for the dirty ones, `mgit stash` before a rebase. mgit runs the second command in every checkout, although the first command has just established that most of them need nothing. The cost is time, mostly network round trips for level repositories, and noise where the no-op output is not yet learned. Where the follow-up is not a harmless no-op on a clean checkout, such as `commit`, `stash`, `checkout -- .` or `reset`, running it everywhere is also a wider blast radius than the operator meant.

The information to narrow the second run already exists at the end of the first: mgit's own quiet classification names exactly the checkouts that differed from normal. Today there is no way to hand that set back to mgit. `--json` lets a script read it out; nothing lets a script, or Kris, feed a set in.

## Owner's proposal

Kris, 2026-10-25, voice, as the brief carries it:

> when you do git commands often, especially on large sets, there's almost a wish to ... use some kind of cache mode ... if I could do an git st followed by an git push, realistically speaking, I just got the latest status ... mgit --to-cache st && mgit --from-cache push ... say there was 17 repos and only 3 of them had non-standard status responses, they would be added to the cache list as the candidates, and then effectively the from cache on the second request is filtering the push to just those repositories ... the cache should not last more than 5 minutes ... if the cache [has] expired ... you can still do [mgit st] and it works as standard ... if you've got an idea around how that could work or be improved on it, you could do a bit of a design mode on that.

And at 08:22 GMT, steering this design:

> is [there] a way we can do an alias around it or something, or is there a command or something that changes [the] cache's behaviour, so git's behaviour ... You should certainly consider that, without [needing] to use the cache mode, as well as part of the analysis.

## Established facts

All paths are in `tools-mgit` at `746a6cc`, version 0.18.0.

- **Quiet is a first-class result.** `dispatch_captured` ([bin/mgit:3880](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L3880)) sorts every checkout into quiet, with output, or failed. Quiet means exit 0 and either no output at all or output matching a learned template. The closing line counts the three. "Non-standard status responses" in Kris's words is precisely the union of with-output and failed.
- **`--json` already exports the set.** The same function prints, per checkout, `label`, `path`, `exit`, `quiet`, `stdout` and `stderr`, plus a summary. A script can obtain the candidate paths today with `mgit --json st`; it needs `jq` or equivalent, which is outside mgit's Bash-and-Git dependency rule ([AGENTS.md](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/AGENTS.md)).
- **Nothing imports a set.** Selection is a workspace manifest or directory discovery, optionally replaced by one exclusive territory selector (`--territory`, `--estate`, `--principals`), then narrowed by repeatable `--filter PREFIX` on the directory basename ([bin/mgit:4099](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L4099)). `--repo` is a usage error outside `register add/rm` ([bin/mgit:4145](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L4145)). There is no explicit-path selector for ordinary commands.
- **Zero matches stop dispatch.** The README states that selected missing roots, zero matches and incomplete producer output stop dispatch; selector conflicts are usage errors that run nothing. The tool's habit is to refuse rather than widen.
- **`sync` is the command-aware form of "push what is ahead".** `sync_command` ([bin/mgit:2973](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L2973)) fetches every tracked branch in parallel, then per checkout compares `HEAD...@{upstream}` with `rev-list --left-right --count`, fast-forwards only-behind, pushes only-ahead, and skips dirty, diverged, detached and upstream-less branches with a reason. It has no push-only or pull-only switch and no way to skip the fetch.
- **`overview` reads ahead and behind locally.** It uses `status --porcelain=2 --branch` and `for-each-ref` with no fetch; counts are as fresh as the last fetch ([bin/mgit:3186](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L3186)).
- **Learned templates are the only persistent state.** They live in `${XDG_CONFIG_HOME:-~/.config}/mgit/templates/`, one plain-text file per expanded command ([bin/mgit:3629](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/bin/mgit#L3629)). mgit uses no `XDG_STATE_HOME`, `XDG_CACHE_HOME` or `XDG_RUNTIME_DIR` today. On this machine `st`, `status`, `status --short --branch` and `branch` are learned; `push` is not, so a level `mgit push` prints `Everything up-to-date` in every checkout.
- **`-v` and `--json` bypass classification.** Verbose streams one checkout at a time with no quiet decision; `--json` reports `quiet` but hides nothing. `-R/--raw` commands never use templates.
- **Git aliases are expanded before template lookup**, so `st` and `status -sb` share one identity ([KI-TOOL-MGIT-CLI-031](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-031-learn-command-shapes.md) documents the mechanism and its limits).
- **Runtime rules.** Bash 3.2 and Git only; mutating behaviour is verified in disposable repositories with isolated configuration; the roadmap ledger `CLI` is reserved through 031 and is advanced in its own commit before a record is written ([docs/roadmap/_ISSUES.md](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/_ISSUES.md)).
- **Git has no setting that makes `push` skip locally.** `git push` with nothing to send still contacts the remote and prints `Everything up-to-date`; `push.default`, `remote.pushDefault` and the like choose where to push, not whether. A local "is anything ahead" test is `git rev-list --count @{upstream}..HEAD`, which `sync` already uses in its two-sided form.

## What the cache would and would not buy

Take the headline case, `mgit st` then `mgit push`, over a set where three checkouts are not level.

- **Which checkouts get pushed is the same with or without the cache.** `status -sb` prints `[ahead N]` for any branch ahead of its upstream, so every ahead checkout is in the candidate set, and `git push` in a level checkout pushes nothing. The cache changes the number of no-op pushes, not the set of real ones.
- **What it saves is network time and noise.** Each no-op push is one remote round trip. With eight jobs, a fifty-checkout set costs tens of seconds; with the three candidates it costs one. The noise it saves is already removable another way: `mgit learn push` over a level set records `Everything up-to-date` and makes those checkouts quiet.
- **What it protects is the follow-ups that are not no-ops.** `commit -am` exits 1 with "nothing to commit" in a clean checkout and counts as failed; `stash` prints "No local changes to save"; `checkout -- .` and `reset --hard` act on whatever is there. For these, narrowing to the checkouts the sweep named is a scope control, not an optimisation, and it is where the idea earns its place.
- **What it cannot do is make the sweep fresh.** A checkout that changed between the two commands, by another session committing or a fetch landing, is either a missed candidate or a candidate that no longer needs anything. The five-minute bound limits this but does not remove it. For `push` both failure modes are harmless. For a destructive follow-up they are not, which is why expiry must stop rather than widen.

## Alternatives

Six routes, of which the first three need no cache. Kris asked that these be weighed first.

### A. `mgit sync`, as shipped and with a push-only switch

`mgit sync` already does the headline case properly: it decides from a fresh fetch which checkouts are only ahead and pushes exactly those, leaving dirty and diverged ones named. For "status then push" it is the right tool today, with two gaps: it also pulls, and it fetches every checkout first, which costs the same round trips the cache was meant to save. A `sync --push-only` (and its twin `--pull-only`) and a `sync --no-fetch` that compares against the last fetched upstream, as `overview` does, would close both gaps without state. This route covers push and pull only; it says nothing about `commit`, `stash` or `checkout`.

### B. A raw per-checkout guard, with no change to mgit

mgit can already run a local check and act only where it passes, in one `-R` command:

```sh
mgit -R sh -c 'n=$(git rev-list --count @{upstream}..HEAD 2>/dev/null) && [ "$n" != 0 ] && git push || true'
```

Level checkouts print nothing and are quiet; checkouts without an upstream are skipped by the failed `rev-list`; ahead checkouts push. A shell alias such as `mpush` makes it one word. This is Kris's "alias around it": it exists today, costs no network for level checkouts, and is exactly as safe as `git push`. Its limits are that it is one guard per intent, each hand-written, that the guard and the action are coupled in a quoted shell string, and that `-R` runs bypass templates, so any output is shown. It is a good answer for push and a poor general mechanism.

### C. Teach `mgit push` to skip locally

Add a command-aware rule inside mgit: before `push`, test ahead-of-upstream and skip when zero. This contradicts the principle adopted with `learn` that mgit has no built-in idea of what a Git command's normal state is, and it is wrong for the many push forms that do not push the current branch: `push --tags`, `push origin feature`, `push -u`, `push --delete`, `push --force-with-lease` after a rebase that left the branch behind. `sync` is the sanctioned place for push-specific knowledge. Not recommended.

### D. Kris's proposal: `--to-cache` and `--from-cache`, one slot, five minutes

A run with `--to-cache` records its non-quiet checkouts; a later run with `--from-cache` selects only those. One implicit slot, written at the end of a captured run, expiring five minutes after it was written. Plain commands are unaffected. This is general across commands, two flags, and reads naturally with `&&`. Its open questions are what happens on expiry, how the slot is keyed so a different workspace or selector does not inherit a foreign set, whether failed checkouts count as candidates, and how two concurrent sessions share one slot. The design section below answers them.

### E. Named result sets

Generalise D to `--to-cache NAME` and `--from-cache NAME`, listed and forgotten like templates. Names carry intent (`dirty`, `ahead`, `release`), several can coexist, and agents in parallel sessions do not collide. The cost is surface: listing, forgetting, naming rules, and the question of whether a named set should expire at all. Sensible as an extension of D once D has proved itself, not as the first cut.

### F. Explicit path list in, from a file or stdin

Add a selector that takes checkout paths, `--repos-from FILE` or `--repos-from -`, NUL- or newline-separated, exclusive with the territory selectors and narrowed by `--filter` as usual. With `--json` already exporting paths, this closes the import gap statelessly and composes with any tool. Agents prefer it: no hidden state, the set is visible in the transcript, and two sessions cannot interfere. For Kris at a prompt it needs a pipeline or `jq`, so it does not replace D; it is the primitive D can be sugar over, with `--to-cache` meaning "write the non-quiet paths to the slot file" and `--from-cache` meaning "`--repos-from` the slot file, if fresh".

### Weighing them

| Route | Needs state | Covers | Stale risk | Change to mgit |
| --- | --- | --- | --- | --- |
| A sync, push-only, no-fetch | none | push, pull | none, fresh fetch; last-fetch with `--no-fetch` | small, inside `sync` |
| B raw guard alias | none | push, anything with a local test | none | none; a dotfiles alias |
| C push skips locally | none | push only | none | small but against principle |
| D to/from cache | one slot file | any command | bounded by TTL | moderate: two flags, slot file, expiry |
| E named sets | files | any command | per set | D plus list, forget, naming |
| F paths from file or stdin | none | any command | caller's | small: one selector |

## Design of the cache, if built

Routes D and F are designed together, F as the primitive and D as the two-flag convenience. Every point here is a proposal for Kris and the reviewer to agree with or differ from.

1. **Candidates are the non-quiet checkouts.** `--to-cache` records every checkout the run classified as with output or failed, in selection order, by canonical checkout path. Quiet checkouts, by template or by silence, are left out. A run with no templates for its command therefore caches the whole set, which is correct and visibly so.
2. **Failed checkouts are included.** A sweep that failed in a checkout has not shown it is normal. Including it means the follow-up fails there too, which is loud and harmless for a read or a push and is the right default for a scope control. Kris may prefer the opposite; it is a query.
3. **Written only from a captured run.** `--to-cache` requires the default captured mode. With `-v` there is no classification, so `--to-cache -v` is a usage error. With `--json` it is allowed, since the classification exists; with `--learn` it is allowed and records the classification made with the templates that existed before the learn. With `-R/--raw` it is allowed and records every checkout with output, since raw runs have no templates.
4. **One slot file under the cache home.** `${XDG_CACHE_HOME:-~/.cache}/mgit/last-set`, plain text, in the style of a template: comment lines, then `written: <epoch seconds>`, `command: <printed command>`, `selection: <key>`, `count: <n of m>`, then one `path: <canonical path>` line per candidate. Written atomically by rename. Nothing else is stored, so a stale or foreign file can cause nothing worse than an error.
5. **Selection key.** The key is the canonical selection root plus the ordered filters: the workspace manifest path or the discovery root for ordinary selection, or `territory:<handle>`, `estate` or `principals` for a KI selector, then `filter:<prefix>` lines. `--from-cache` refuses, with a one-line error naming both keys, when the current selection would not have produced the cached run; `--filter` on the reading side is allowed as a further narrowing. This stops a `--from-cache push` in one workspace acting on paths cached from another.
6. **Expiry is five minutes, fixed, and stops the run.** `--from-cache` with a slot older than 300 seconds, or no slot at all, is a usage error: `mgit: cache from 'st' is 7m12s old (limit 5m); re-run with --to-cache`, exit 1, nothing dispatched. It never falls back to the full set, in keeping with mgit's rule that zero matches and selector conflicts stop dispatch. Plain `mgit push` remains one word away for the full set. Kris's words allow the other reading, so it is a query.
7. **Age is always shown.** A `--from-cache` run prints one line before its results, `mgit: 3 of 17 repositories from 'st' 42s ago`, so the operator sees how old the set is and what produced it. `mgit --from-cache` with no command lists the cached checkouts, as `mgit` alone lists the selection, so the set can be inspected before acting.
8. **Invalidation by content is deferred.** Recording `HEAD` and the index mtime per candidate at write time can detect that a candidate changed since, but cannot detect a quiet checkout becoming non-quiet, which is the dangerous direction, without re-running the sweep. The TTL already bounds both; a later refinement could warn when a candidate's `HEAD` moved. Not in the first cut.
9. **`--to-cache` and `--from-cache` compose.** `mgit --from-cache --to-cache ci -am "wip"` narrows to the cached set, runs, and rewrites the slot with the checkouts that were non-quiet under `ci`, so a chain `st` → `ci` → `push` narrows at each step. Each write replaces the slot.
10. **Concurrency.** Two sessions in the same cache home share the slot; the selection key stops cross-workspace mistakes but not two sessions in one workspace. The first cut accepts this, since an agent should use route F or a named set; if it bites, E adds names.
11. **`--repos-from` is the primitive.** `--repos-from FILE|-` reads newline- or NUL-separated checkout paths, resolves each to a selected checkout or stops with an error naming the first path outside the selection, and is exclusive with `--territory`, `--estate` and `--principals`. `--from-cache` is implemented as `--repos-from <slot>` with the freshness and key checks in front. The two flags and the selector are documented together.
12. **Completion and help.** The three options join `mgit help`, the manual, Bash and Zsh completion, and the user guide's "Run commands" page; a short "Status then act" example sits beside `sync` so the reader picks `sync` for push and pull and the cache for the rest.
13. **Verification.** Bats fixtures in disposable repositories: a sweep over three checkouts with one dirty writes one path; `--from-cache` runs only there; a foreign key, a missing slot and a backdated `written:` each stop with the named error; `--to-cache -v` is a usage error; `--repos-from -` with a path outside the selection stops; chained narrowing replaces the slot.

## Agents and Kris

Kris at a prompt wants the two-word form: `mgit --to-cache st && mgit --from-cache push`, or the sync route for push and pull. Agents under the harness mostly run mgit in captured or `--json` mode and keep their reasoning in the transcript; for them hidden state between steps is a liability, since a parallel run can overwrite the slot and a reader of the transcript cannot see what the set was. Agents should prefer `--json` plus `--repos-from -`, or where a set must survive several steps, a file they own in temporary output. The coordinator standard's quiet-tools rule is unaffected: a `--from-cache` run's age line is one more line of ordinary output. Where agents sweep an estate for the owner, `mgit sync` and `mgit overview --json` remain the tools of record, as today.

## Review

One independent review was taken on a different runtime, Codex, read-only, with the draft and `tools-mgit` as its only inputs. Its marks and this note's settlements follow.

_(filled after review)_

## Recommendation

_(filled after review)_

## Queries

_(filled after review)_
