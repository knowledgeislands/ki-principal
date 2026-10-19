# Options for blind review - KI-TOOL-MGIT-CLI-030 sync closing summary

## SYNC-CATEGORIES - Outcome categories

**Context:** Today sync prints one line for each checkout that changed or has a problem, but it adds none of them up. The record needs a fixed set of outcomes that every repository falls into.

**Query:** Which outcomes should the tally count, and where does each kind of skip fall?

**Options:** a) Use five outcomes: in sync, pulled, pushed, skipped and failed. Skipped covers local changes, detached HEAD, no upstream, diverged, failed fetch, bare repositories and your own `-i` refusals. Failed covers only `status failed`, `cannot compare`, `pull failed` and `push failed`. b) Add a sixth outcome, "need attention", as `overview` has. It would take diverged, dirty, detached and no-upstream checkouts, and leave skipped for bare repositories and your refusals. c) Count a failed fetch as failed, not skipped.

### SYNC-TALLY - Tally shape

**Context:** Ordinary dispatch ends with `mgit: N repositories: ...` and always prints zero counts. A checkout can never both pull and push, because a branch that is both ahead and behind has diverged and is skipped.

**Query:** What should the closing tally line look like?

**Options:** a) `mgit sync: 57 repositories: 55 in sync, 0 pulled, 1 pushed, 1 skipped, 0 failed`. It keeps the `mgit sync:` prefix that sync's other lines use, prints zero counts, and counts each repository once. b) The same line, but leave out the zero counts. c) Use dispatch's bare `mgit:` prefix.

### SYNC-SKIPDETAIL - Where skipped detail goes

**Context:** With 50 or more repositories, a skip line printed early in the run scrolls off the screen long before the end. That is how the five unpushed commits went unnoticed.

**Query:** Where should the run name each skipped or failed repository and its reason?

**Options:** a) Keep the per-repository lines as they are. After the tally, add one indented line for each skipped or failed repository, such as `ki-agentic-harness: local changes, 5 ahead`. b) List them on the tally line itself, as dispatch lists its failures. c) Leave them only in the per-repository lines, with the counts added there.

### SYNC-HELD - Which held commits to count

**Context:** A dirty checkout's branch is still fetched, so up-to-date ahead and behind counts are available for it. A checkout whose fetch failed can only be compared with the copy of the upstream from its last successful fetch. A detached HEAD, or a branch with no upstream, has nothing to compare with.

**Query:** Which unpushed and unpulled commits should the skipped detail report?

**Options:** a) Count the checked-out branch only, as `mgit st` does. Give a dirty checkout its up-to-date ahead and behind counts. Give a failed fetch its counts against the last-fetched upstream, marked `stale`. Give detached heads and branches without an upstream no counts. b) The same as a), but give a failed fetch no counts. c) Also count other local branches that are ahead of their upstreams.

### SYNC-STREAMS - Standard streams

**Context:** Today every sync line goes to standard output. The `ki-repo-tools` command-line conventions put warnings and progress on standard error. [KI-TOOL-MGIT-CLI-029](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/roadmap/KI-TOOL-MGIT-CLI-029-cli-convention-departures.md) owns departures from those conventions across the commands.

**Query:** Should this record move sync's warning lines to standard error?

**Options:** a) Leave the streams as they are, and record the departure on KI-TOOL-MGIT-CLI-029. b) Do it here: move the skip, warning and progress lines to standard error, and keep the tally and the per-repository result lines on standard output.

### SYNC-EXIT - Exit status

**Context:** Today every skip except your own `-i` refusal makes sync exit with `1`, and so does any bare repository. Answering `q`, or input ending, under `-i` exits `1` with no closing lines at all.

**Query:** Should the exit status change, and what should a quit under `-i` print?

**Options:** a) Keep the exit status exactly as it is, with no extra explanation on the tally line, since the skipped and failed counts already show why. When you quit under `-i`, print the tally and detail for the repositories reached so far. b) Keep the exit status, and keep quitting silent, as now. c) Exit `1` only for failed checkouts, and treat skips as success.

### SYNC-JSON - Machine output

**Context:** Dispatch and `overview` both give `--json` a `summary` object; sync has no `--json`. No consumer has asked for one, and the record is already size m.

**Query:** Should sync gain `--json` in this record?

**Options:** a) Defer it to a new triage record. b) Add it here, with a `summary` object that matches dispatch and `overview`, and one result for each repository.

### SYNC-VERBOSE - Verbose mode

**Context:** Today bare repositories are counted only without `-v`. With `-v`, each one gets its own line instead.

**Query:** Should the tally depend on `-v`?

**Options:** a) Print the same tally with and without `-v`, with bare repositories always counted as skipped. `-v` then adds only progress lines. b) Keep today's split, and count bare repositories in the tally only without `-v`.

### SYNC-CLEANFETCH - Clean-branch wording

**Context:** MGIT-WS-018, the manual and the running-commands guide say sync fetches every _clean_ tracking branch. The code fetches every tracking branch, which is why a dirty checkout's behind count is up to date.

**Query:** Should the documents change to match the code, or the code to match the documents?

**Options:** a) Correct the specification, manual and guide to say that every tracking branch is fetched. b) Narrow the fetch to clean branches, which loses the up-to-date behind counts for dirty checkouts.
