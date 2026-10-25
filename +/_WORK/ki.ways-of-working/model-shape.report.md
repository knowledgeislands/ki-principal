# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-model-shape

**🤖 → 👤 Handoff to supervisor · Run report at 01:42 BST · last mark 02:10 BST**

---

## Done

- I wrote the design brief [model-shape](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/model-shape.md) in the `ki-work-design` brief shape and committed it as 730a893d. It covers:
  - the five units (State of play, Project package, thread, run and record), each with its boundary and hand-offs;
  - the State of play cascade into Project packages;
  - how records flow through their `project` field;
  - upward relationship metadata;
  - the split between seat and requirement for hosts;
  - committing, pulling and pushing when many sessions write one package;
  - sixteen conflicts with the [Work Process](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Pillars/Philosophy/Model/Processes/Work Process/Work Process.md>) note and the `ki-coordination`, `ki-work-package` and `ki-work-roadmap` standards, each with its proposed change and its Enactment route;
  - seventeen numbered claims and a rollout sketch, with Valle Armonia as the pilot.
- No standard, Pillars note or package file was changed.
- The markdown lint passed after I fixed two blank lines inside blockquotes. The repository audit hook passed.
- I skipped `git pull --rebase` before committing. The tree held another session's uncommitted `design/repository-metadata.md`, so a rebase would have had to stash it. The run's footer also forbids remote calls. Both commits are local and unpushed.
- I found one inconsistency inside the current standard: `ki-work-package` prohibits any host in a package, yet allows a `(<host>)` label suffix. The brief resolves this by narrowing the prohibition to the seat.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- `ki-work-design` requires two independent reviews of the brief, on different models or runtimes, before a merged report and any decisions. None has been launched.
- None of the queries below has had a blind review. Each is medium or low confidence, so the coordinator should send each one to blind review before it reaches Kris.
- I left `design/repository-metadata.md` uncommitted and did not touch it, because it belongs to another session.

## Queries

### CASCADE-STEWARD - How a State of play knows whether a Project has its own thread

**Context:** Kris said the State of play should look after every Project package "unless, of course, I've got their own coordination thread, which it should know about somehow". Today nothing committed says whether any thread is working a package. `beat` gives only the time of the last heartbeat. The machine-local thread binding has not shipped, and it would be visible only on its own host.

**Query:** Where should a package record which work currently stewards it?

**Options:** a) (recommended, confidence medium - it is visible across hosts and reuses the holder vocabulary, but it is a new field that every steward must keep current) Add `steward: self | work/<sop id>` to `state.md`. It is set when a Project thread opens and reset at hold or close. The machine-local binding is local evidence only. b) Rely on the machine-local thread binding alone. Nothing is committed, but a thread on another host is invisible. c) Infer it from `beat` freshness, with no new field. This is fragile when a thread is idle but open.

### PARENT-UP - How every package says which State of play it answers to

**Context:** Kris asked that "we need to add to the metadata of the threads, what it's related to". Today only a secondary State of play carries `parent`, and its `covers` list points down, against the standard's "Links point upward". A Project package names its `project` and `theme`, but not its State of play.

**Query:** Should every package below the main carry `parent`, and what happens to `covers`?

**Options:** a) (recommended, confidence medium - it keeps all links pointing up and a package read alone says what it relates to, but it changes the closed field set and its tooling) Put `parent` on every package below the main. `ki work status` derives coverage, and `covers` is retired after a tolerance window. b) Put `parent` on every package and keep `covers`, with a rubric check that the two agree. c) Leave it as is: `parent` and `covers` on secondaries only.

### HOST-TARGET - How work aimed at a particular machine is written

**Context:** Kris asked that coordinators "use a hostname to understand who they're running on ... if there's things targeted to particular machines or categories of machines". The standards say a package names no host, and that a hold never says which host the work resumes on. The same standard allows a `(<host>)` label suffix, and `ki.chezmoi` already prefixes lines with `terra:` and `sol:` informally. The brief separates the seat, where a thread runs, which is never committed, from a requirement, which is a fact about the work.

**Query:** Should a host or machine-category requirement be allowed on message lines, briefs and records?

**Options:** a) (recommended, confidence medium - it keeps the protection against stale seats and gives Kris's targeting a sanctioned form, but category names need an inventory that Rig owns) Prohibit only the seat. Allow an optional `@<host or category>` on message lines, briefs and records, beside the label suffix. A coordinator establishes `hostname -s` at bootstrap and re-anchoring, and acts only on lines for its host or untagged lines. b) Allow no host anywhere in a package. Host-bound work is kept in machine-local or Rig configuration only, and the label suffix is removed.

### PACKAGE-PUSH - Who may push a shared work folder

**Context:** Kris said at 01:30 BST that work-folder changes sit "not regularly getting updates, pushes, and pulls". Under the rule Kris set on 14 October, a session pushes only when its own commits alone are stacked. On a shared checkout, another session's commits are nearly always stacked, so nobody pushes. COMMIT-CADENCE already fixes commit-at-write and pull-at-wake, and wow-coord-standard is drafting that standard change. This query is the push half and should be answered together with it.

**Query:** May any session push a fast-forward stack made only of `+/_WORK/` commits, whoever made them?

**Options:** a) (recommended, confidence medium - work-folder commits are package state, not product, and this removes the stall, but it relaxes a rule Kris set) Yes. After its pull and the repository's hooks, any session may push a fast-forward stack made only of `+/_WORK/` commits. Product commits keep the own-commits-only rule. b) No. Keep own-commits-only pushing and rely on the COMMIT-CADENCE commit and pull cadence alone.

### MESSAGES-MERGE - How concurrent writes to `messages.md` merge

**Context:** With one steward at a time, the only file many sessions write is `messages.md`: senders append lines and the steward removes them. On 25 October an unresolved merge on `+/_WORK/ki/messages.md` stopped another session. A union merge driver would resolve append-against-append without a stop, but it could resurrect a line the steward has just removed. One file per message ends conflicts, but it changes the closed list and every reader.

**Query:** Should `messages.md` get a merge mechanism, and which one?

**Options:** a) (recommended, confidence low - it is cheap and fixes the common case, but resurrecting a removed line is a real risk that only a test can bound) Add a `merge=union` driver for `+/_WORK/*/messages.md` through `.gitattributes`, adopted only after a test of remove plus concurrent append shows no resurrected line. b) Use one file per message, `messages/<date>-<tag>.md`. This changes the closed list, the tooling and every reader. c) Leave it as is: resolve conflicts by hand.

### CASCADE-REPORT - How one State of play thread reports on several packages

**Context:** When a State of play thread stewards several Project packages, Kris hears everything in one thread. The brief proposes that each Project's queries live in that Project's `queries.md` with their tags, and that Kris's answers are logged in that Project's `decisions.md`, even when they are asked and answered in the State of play thread.

**Query:** What form does the State of play's Summary take for cascaded packages?

**Options:** a) (recommended, confidence medium - one report keeps Kris's attention in one place, while state stays in the right package) One Summary under the territory heading and banner. Each item and query names its package, and acceptance bundles stay one per package. b) One owner report per package touched, each with its Project heading and banner.

### 🤖 → 👤 Handoff to supervisor · since 01:42 BST

👤 6 with you

- [with you] CASCADE-STEWARD · owner · since 01:42
- [with you] PARENT-UP · owner · since 01:42
- [with you] HOST-TARGET · owner · since 01:42
- [with you] PACKAGE-PUSH · owner · since 01:42
- [with you] MESSAGES-MERGE · owner · since 01:42
- [with you] CASCADE-REPORT · owner · since 01:42
- [committed] model-shape design brief

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
