# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-mgit-cache-design

**🤖 → 👤 Handoff to supervisor · Run report at 08:48 GMT · last mark 01:07 GMT**

---

## Done

- **Design note written and published.** [design/mgit-cache.md](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/mgit-cache.md) in ki-principal: problem, Kris's proposal verbatim with the 08:22 steer, eleven established facts cited to `tools-mgit` at `746a6cc`, what the cache buys and does not, six routes weighed (three needing no cache), a thirteen-point design for the cache if built, agents' use, the merged review, a recommendation and five queries. Commits `e79259be` and `b8c99f73` (one wording correction), pre-commit audit pass, fetch and fast-forward pull clean, pushed to origin fast-forward; checkout level with origin.
- **Independent review taken on Codex** (GPT-6, high reasoning, read-only sandbox, recommendation and queries withheld). It fact-checked every claim, agreed on nine design points, differed on seven, and added six; every difference is settled in the note's review table with its evidence, and the one unsettled difference, whether the two-flag cache ships first or after the stateless primitive, goes to Kris as MGIT-CACHE-SCOPE. The raw review stays in this run's temporary output, folded into the note; the brief limited commits to the note itself.
- **Material corrections from the review.** The draft's no-cache push guard masked push failures with a trailing `|| true`; corrected and re-tested read-only. "Zero matches stop dispatch" narrowed to selectors; "same checkouts pushed either way" qualified; timing figures marked as estimates since no remote call was made.
- **tools-mgit read only**, unchanged, no message sent. The only mgit runs were read-only `-R sh -c` sweeps with `echo` in place of `git push`.
- **Limitations.** The first Codex attempt hung on an open standard input for ten minutes before being killed and relaunched with input closed. The draft was swept into the coordinator's work-folder commit `e87d2375` before this run's own commit; nothing was lost and the final note supersedes it.

## In Progress

Nothing is running.

Outstanding - no action requested now: once Kris answers MGIT-CACHE-SCOPE, the accepted shape goes to `tools-mgit` as a `messages.md` line for it to capture under its own ledger (`CLI` reserved through 031), and the `mpush` alias, if accepted, to ki.chezmoi the same way; the note graduates and is deleted when that record exists.

## Queries

### MGIT-CACHE-SCOPE - what to build first

**Context:** Six routes were weighed. The Codex review and the note agree that `--repos-from` (an explicit path-list selector, route F) is the right primitive and that teaching `push` to skip locally (route C) is wrong. They differ on timing for your two-flag cache (route D): the reviewer would ship F and the `sync` direction switches first and defer D until isolation is specified; the note says the selection key, membership check, stop-on-expiry and an optional set name specify it, and that F alone gives you nothing at the prompt without `jq`.

**Query:** Which shape goes to `tools-mgit` as the first record?

**Options:**
a) (recommended, confidence medium - the reviewer disagrees on timing, agreeing on everything the first cut would contain) `--repos-from` and `--to-cache [NAME]`/`--from-cache [NAME]` together, one record; `sync --push-only` and `--pull-only` as a second record.
b) `--repos-from` and the `sync` switches first; the cache flags as a later record once the primitive has been used.
c) The cache flags alone as you proposed, one default slot, no `--repos-from` and no name.

### MGIT-CACHE-EXPIRY - what `--from-cache` does when the set is missing or older than five minutes

**Context:** Your words were that after expiry "you can still do mgit st and it works as standard", which is true of the plain command either way. The open point is the flagged command. mgit's habit is to stop on selector conflicts and KI zero matches rather than widen; a `--from-cache reset --hard` that silently ran everywhere would be the worst outcome of the feature. The reviewer agrees that missing or expired state must stop.

**Query:** When the set is missing or expired, does `--from-cache <command>` stop with an error, or run the full set with a warning?

**Options:**
a) (recommended, confidence high - reviewed; stopping is the only safe behaviour for a destructive follow-up and costs one re-run) Stop with a one-line error naming the set's age and the fix, exit 2, nothing dispatched; a fresh empty set runs nothing and exits 0.
b) Warn and run the full selection, as plain `mgit <command>` would.

### MGIT-CACHE-FAILED - whether a checkout whose sweep failed is a candidate

**Context:** A sweep can fail in a checkout, for example on an `index.lock`, a missing upstream or a broken worktree. The note includes such checkouts in the set, since they have not shown they are normal, and the follow-up would then run and most likely fail there too, loudly. The reviewer points out that a failed inspection does not prove the next command fails harmlessly, and that the sweep's own exit 1 already stops an `&&` chain, so you would only reach `--from-cache` by `;` or a second command.

**Query:** Are failed checkouts included in the cached set?

**Options:**
a) (recommended, confidence medium - the reviewer left it open; inclusion keeps the set a superset of what needs attention, and the sweep's exit status already warns you) Include them, and show the count of failed candidates in the age line.
b) Exclude them, so the set holds only checkouts that ran and printed something.
c) Make `--from-cache` refuse to run while the set records any failed checkout, until the sweep is repeated clean.

### MGIT-CACHE-TTL - whether five minutes is fixed

**Context:** You set "not more than 5 minutes". The note fixes 300 seconds from the sweep's start, with no option, so the behaviour is the same on every machine and in every script. A configurable limit would need a setting home mgit does not yet have beyond templates.

**Query:** Is the five-minute limit fixed, or configurable?

**Options:**
a) (recommended, confidence high - one constant, no new configuration surface, and your words set the bound) Fixed at five minutes from the sweep's start.
b) Configurable, with five minutes as the default, by an environment variable or a future `mgit` setting.

### MGIT-PUSH-ALIAS - adopting the no-cache push guard today

**Context:** Route B is a one-line `mgit -R sh -c '...'` guard that pushes only checkouts ahead of their upstream, costs no network for level ones, keeps push failures visible, and needs no change to mgit. Tested read-only on this machine. It would live in chezmoi as an alias such as `mpush`, handed to the ki.chezmoi work as a message.

**Query:** Do you want the alias now, independent of what `tools-mgit` builds?

**Options:**
a) (recommended, confidence high - zero cost, available today, and it remains useful after the cache ships) Yes: hand the alias to ki.chezmoi as a `messages.md` line, and learn `push` over a level set so a plain `mgit push` is quiet.
b) No: wait for the `tools-mgit` record.

### 🤖 → 👤 Handoff to supervisor · since 08:48 GMT

👤 5 with you

- [with you] MGIT-CACHE-SCOPE · owner · since 08:48 GMT
- [with you] MGIT-CACHE-EXPIRY · owner · since 08:48 GMT
- [with you] MGIT-CACHE-FAILED · owner · since 08:48 GMT
- [with you] MGIT-CACHE-TTL · owner · since 08:48 GMT
- [with you] MGIT-PUSH-ALIAS · owner · since 08:48 GMT
- [committed] design/mgit-cache.md

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
