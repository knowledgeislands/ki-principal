---
note_type: streams/design
updated: 2026-10-26T21:50:00Z
author: Written with Claude
---

# Findings

**Status:** a nascent area of Ways of working, being pioneered on the Valle Armonia territory. Other territory threads, personal-principal first, are invited to run it on their own territory and add their findings under [Other territories](#other-territories). Nothing here is a standard yet; the shape is expected to change as runs report back.

**Owner:** Kris Brown · **Owning repository:** knowledgeislands/ki-principal · **Owning work:** `ki.ways-of-working` · **Date:** 2026-10-24 · **Pioneered by:** [VA > SoP](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/work.md), whose [decisions log](/Users/krisbrown/workspaces/valle-armonia/va-principal/+/_WORK/va/decisions.md) holds Kris's words of 24 October under FINDINGS-SECTION and PROPOSALS

A finding is something Kris asked a coordinator to find out. Today it arrives once, in one Summary, and then scrolls away. This proposal gives findings their own section in the owner report, has each one say what it was for, and keeps it in front of Kris until Kris is content with it.

## The problem

Kris asks coordinators for investigations: a table of a territory's repositories and how far they agree, or a walk through the working-area folders with a recommendation for each. Three things go wrong with what comes back.

- **It gets lost.** The output lands in one Summary among Done lines, and the next Summary moves on. Kris: the outputs "get lost sometimes with all the things that come backwards and forwards, and scrolling it up and down to find them is really tedious."
- **It cannot be reviewed away from the screen.** Kris often answers in speech, away from the desk, and can only answer what the latest report carries: "it's very difficult for me to give you feedback on them if I don't see them because sometimes I'm away from the screen."
- **It does not say what it was for.** Of one table Kris said it did not "state it before table ... it doesn't really say what the goal was". A table without its question has to be decoded before it can be judged.

## What exists today

The [owner report](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#owner-report) has three sections, `## Done`, `## In Progress` and `## Queries`, in that order, every time; a full summary adds `## Decided` before them, and a hold report uses `## Done`, `## Parked` and `## Left over`. There is no place for findings. An investigation's results go into Done, where a background run also puts its commit identifiers and check results, and its decisions go into Queries.

Nothing carries a finding forward. The Summary covers the window since the last message, and the recap the window since the mark, so a table given once is not given again. The run report that held it is deleted at the next tidy once its outcome is homed, and its queries are copied into `queries.md`; the table itself has no home in the package.

## What counts as a finding

A finding is the output of an investigation the owner asked for: a survey, a table, a comparison or an assessment, whose purpose is to inform a judgement Kris has still to make. It is distinct from Done, which records outcomes: something was changed, committed, decided or delivered. "va-principal's working areas were tidied" is Done; "here is each working-area folder, what it holds and what should happen to it" is a finding.

Only an owner request makes a finding. A run's own observations, a Tending pass's dispositions and a check's results stay in Done or become queries as they do today. Where Kris asks for findings in so many words, or asks "could you give me a table", that is a finding even if it turns out short.

## The Findings section

A Summary, recap or full summary carries `## Findings` whenever at least one finding is open, and leaves it out otherwise, so the three standing sections stay as they are for most reports. It sits after `## In Progress` and before `## Queries`:

1. `## Done`: what changed.
2. `## In Progress`: what is running and waiting.
3. `## Findings`: what Kris asked to know.
4. `## Queries`: what Kris must decide.

That order reads as the finding being the evidence and the queries the decisions it raises, so a query can point up to the finding rather than repeating its table. In a full summary, `## Decided` still comes first.

Each finding is a `###` heading with a stable tag, in the same vocabulary as Needs tags, so Kris can say "REPO-ALIGN is fine" in speech: `### <TAG> - <plain-language title>`. It then opens with its goal, in one short paragraph, before any table:

- **Goal:** the question asked, in Kris's words where they exist, who asked it and when, such as "Kris, 24 October 16:46 BST: which of the territory's repositories are consistent with each other, and what would bring them into alignment?"
- **Scope:** what was looked at and what was not, in one line, such as "the four Valle Armonia repositories, local checkouts and GitHub settings, read only".
- **As of:** when the facts were last checked, so a refreshed finding shows it is fresh.

Then comes the table or the short list, and beneath it any footnotes, marked `† ‡ § ¶ ‖`, and one line naming the queries it raised.

## Carrying findings until they are settled

A finding is carried in full, table and all, in every Summary, recap and full summary from the one that first gives it until it is settled. Kris asked for this: findings should have "its own section in the summary, and repeat the same tables until we're happy with things". The [Report forms](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#report-forms) rule that what is still open is restated in full each time already applies to queries; this extends it to findings. No report says "see the earlier table".

A finding is settled in one of two ways:

- **At a mark.** When Kris strikes a mark, each open finding is settled as part of the mark, unless Kris keeps it open.
- **When Kris says so.** "REPO-ALIGN is fine", "I'm happy with the folders" or the like settles that finding at once, and is read back in the decisions log like any answer.

Settling is not losing. At settlement the coordinator gives the finding one disposition, as Tending's focus rule does for its findings, and records it in the decisions log:

- **Homed in a record:** the finding is evidence for work, so its table goes into the work record that carries the work, or into the record's plan.
- **Homed in a design note:** the finding informs a design, so it goes into that note, as the repository-alignment table would go into a repository-consistency proposal.
- **Homed in the decisions log:** the finding settled a question, so the decision entry quotes the answer and links the finding's last revision.
- **Dropped:** it has served its purpose, every query it raised is answered and nothing more needs it. The log says so in one line, and Git history keeps the file.

## Carrying prompts

A prompt a coordinator drafts for Kris to hand on, to another thread, another territory or back to the coordinator itself, is carried the same way as a finding: in full, in every Summary, recap and full summary from the one that first gives it until a mark or until Kris has used it, and never by reference to an earlier reply. Kris, 24 October: "I talked about findings being included in the summaries, but also the prompts should be included in them in full. We shouldn't refer back to previous ones when we ask for a summary from a mark, for example."

A prompt is carried under `## Findings`, as one `###` heading with a stable tag, its goal line saying who it is for and what it asks of them, then the prompt itself in a fenced block Kris can copy whole. It is settled when Kris says it has been sent or used, or at a mark unless Kris keeps it open, and its disposition is recorded in the decisions log like a finding's; a prompt that has been sent is usually dropped, because the receiving thread now carries what it asked.

## Where a finding lives between Summaries

**Decided:** Kris settled the writer and the age on 26 October 2026, read back in the [decisions log](../decisions.md), taking the recommended option of each. Under INTERIM-FINDING-WRITER the `ki-work-package` standard's steward-only package writer stands and this note's proposal that a run writes `findings/<tag>.md` when its brief names it is declined: a run carries a finding in its run report, goal first, and the steward copies it into the file at receive, as it copies queries. Under INTERIM-FINDING-AGE an open finding has no age limit and no age warning, since it is settled by the owner-report Findings rule and not by time; an age may return once territory evidence shows one useful. Both rules are written into the standard's Entry points and Tidying sections in `ki-agentic-harness`.

A Summary is a message and is not saved, so a finding carried only in the coordinator's context is lost at the first compaction. It needs a home in the work package that survives both compaction and a fresh session.

The proposal is a new kind in the [closed list](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/governance/ki-work-package/references/standards-work-package.md#closed-list): `findings/<tag>.md`, one file per open finding, holding exactly the text the report carries, goal first. It is written by the run that does the investigation, the way a run writes to `design/` when its brief names a design note, or by the coordinator when it copies the finding out of a run report at receive, as it copies queries into `queries.md` today. It is kept until the finding is settled and homed, and deleted in the tidy that follows, by explicit path.

Two things would need to change to allow this:

- **The work package.** `ki-work-package` would add the `findings/` row to its closed list, with "kept until it is settled and homed at a mark or on the owner's word", give the run and the steward as its entry points, and add it to the tidying rules. The rubric's FOLDER family would then pass the files, and warn on one older than a set age on work that is not on hold.
- **The coordinator's read budget.** A coordinator reads only its five package files, one report and one short file in a turn. A Summary that must restate open findings in full needs to read them. The simplest change counts `findings/` as part of the package read at bootstrap, re-anchoring and Summary time, so one package read takes the five files and every open finding together. The alternative, one finding per turn as the "one short file", fails as soon as two findings are open, which is the case in the pilot.

A carried prompt lives the same way, as `findings/<tag>.md` holding exactly the text the report carries, goal first and the prompt beneath it, written by the run that drafts it or copied out of a run report by the coordinator at receive, and deleted by explicit path in the tidy after it is used or settled at a mark. Until then the run report that holds it is not deleted, because the prompt is not yet homed.

Placing findings in `queries.md` instead was considered and set aside: queries are decisions, findings are evidence, and a table under `## Open` would make the file hard to scan and its size hard to judge. Placing them in `design/` was also set aside: a design note lives until it graduates, and most findings are settled within a day.

## Refreshing a finding

A finding states facts as of a time. When the facts change while it is open, because a run has fixed part of what it found or Kris has answered a query it raised, the coordinator has the finding refreshed rather than carrying a stale table: the run that changes the facts updates the finding file, or the coordinator launches a short read-only run to do so. The finding's **As of** line moves, and a row that has been dealt with says so in its last column, such as "done, `a1b2c3d4`", rather than vanishing, so Kris can see what moved since the last report. A refresh never changes the goal; a new question is a new finding.

## Findings and queries

A finding raises queries; it does not replace them. Each decision it calls for is a query in `## Queries`, in the usual Context, Query and Options shape, and goes through query review in the usual way. The query's Context can refer to the finding by its tag, "see REPO-ALIGN above", because the finding is in the same report, which is the one exception to the rule against pointing elsewhere.

The two are settled separately. Answering every query a finding raised does not settle the finding, because Kris may still want it in view, and settling a finding does not answer its queries, which stay open in `queries.md` until answered. The finding's closing line names its queries, and each query's Context names its finding, so either can be traced to the other.

## Surfaces that would change

If this graduates, the changes are made once in the `ki-coordination` standard and rendered from its [Generated surfaces](/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md#generated-surfaces):

- **The owner report** in the `ki-coordination` standard gains the optional `## Findings` section between In Progress and Queries, the finding heading and goal shape, the carrying rule and the settlement dispositions. The Report forms table says that every form carries open findings in full.
- **The `ki-coordinator` output style**, rendered from the `output-style` source, gains one paragraph on the Findings section and its order, and the read-budget line counts `findings/` in the package read.
- **The run-prompt report rule**, rendered from the `run-report` source, and the four authority footers from `footer-report`, tell a run that was asked for findings to write each as a `## Findings` section, goal first, in its report and, where its brief names one, to the finding file.
- **The hook line**, from `hook-line`, is unchanged unless Kris wants the Findings section among its hard rules.
- **The work-package standard** and its rubric, as above; this is a `ki-work-package` change, not a generated surface.

## The Valle Armonia pilot

va adopted FINDINGS-SECTION for its own Summaries on 24 October, ahead of this proposal. Two findings and one set of prompts are open there now, and each shows a part of the shape.

### REPO-ALIGN - how far the territory's repositories agree

**Goal:** Kris, 24 October 16:46 BST: "Could you give me a table that looks at that the repos so we can see them in the different kind of groups of repositories that we have, and if they're consistent with each other, or they need improvements, such as no tags, etc. So, what the suggested changes would be to seek alignment?" **Scope:** the four Valle Armonia repositories, their GitHub topics, descriptions, homepages and visibility, and their `.ki.toml` declarations, read only. **As of:** 24 October, the repo-align run.

The repo-align run produced a good table: one row per repository grouped as principal knowledge base, agentic harness and website, with columns for topics, description, homepage, visibility, declared skills and suggested changes. It found that no repository has GitHub topics, that both website repositories carry keywords and a homepage in `package.json` that GitHub does not show, and that the two website repositories differ in their declared skills. It raised three queries: TAG-FORM, TAG-APPLY and TAG-ROUTE.

What it lacked was the goal. The report opened "Read-only survey finished" and went straight into the table, which is the gap Kris named. Under this proposal it would open with the Goal, Scope and As of lines above, and its closing line would name TAG-FORM, TAG-APPLY and TAG-ROUTE.

It is still open. Kris answered TAG-APPLY ("the right way to do it is not to make the changes right now") and TAG-ROUTE, and TAG-FORM is with a second-opinion run. Kris's PROPOSALS answer gives it a home: the table is the evidence for the repository-consistency proposal, which "extends into the package.json in those repositories that have one as much as it does into the GitHub values". So REPO-ALIGN would be carried in each va Summary until that design note exists, then homed in it and deleted from the package.

### FOLDERS - what should happen to each working-area folder

**Goal:** Kris, 24 October 16:10 BST: "We need to really work through those and decide what's left with those so we've got nice clean working areas", and "in the outbound working areas we have a hit digests folder. Is that something that we expect to have?" **Scope:** va-principal's `+/` and `-/`, checked against the working-areas standard and the declared skills, read only. **As of:** 24 October, the work-areas run; a refresh after areas-apply would move it.

The work-areas run gave each item a verdict: `+/_ACQUIRE/granola/` not expected, delete; `+/_ACQUIRED/`, `+/_BATCHES/` and `-/_DIGESTS/` expected by declared skills, keep; `Granola Harvest Triage.md` and `community-presence-handover.md` loose notes, to be homed and removed. It gave them as a list of paragraphs, with the reasoning inside each; a table of folder, expected or not, why, and recommendation would have been quicker to read away from the screen. It raised ACQUIRE-FOLDER, GRANOLA-TRIAGE, PRESENCE-HANDOVER and WEBSITE-LINES.

This finding shows refreshing and settlement. As Kris answered each query and areas-apply and kn4-deliver carried them out, each row would move to "done" with its commit. Kris then settled it in so many words: "it's good now that the underscore acquire slash granola is gone. And I think I agree with the acquired batches and digests because, like you say, they're effectively mandated by those skills if they're enabled." Under this proposal that is the settlement: the log entry records it, the finding is dropped because its outcome is wholly in the decisions log and the commits, and the file goes at the next tidy. Two points the run could not settle, the two Kit Acquire captures not yet delivered and whether the meetings are marked in Granola, leave with it as Outstanding for the Knowledge intake Project, not as part of the finding.

### PROMPTS - the prompts Kris is to hand on

**Goal:** Kris, 24 October, under PROPOSALS: "give me the prompt to send to both of you", so that va and personal-principal adopt the proposals as interim policy, with a simple one-liner for whichever Knowledge Islands thread takes each proposal; and under PROMPT-TENDING, add "the third one, which effectively is the Tending as well". **Scope:** the prompts drafted by the metadata-proposal run and amended for Tending. **As of:** 24 October, after PROMPT-TENDING.

PROMPTS carries three prompts. The shared adoption prompt, for the va and personal-principal threads, names this note, [Repository metadata](repository-metadata.md) and [Tending](tending.md), asks each thread to adopt all three as interim policy on its own territory, and asks for feedback under each note's Other territories section. The two one-liners, one for Ways of working and one for KI > SoP, each hand a Knowledge Islands thread the proposal it is to take up.

This finding shows the carrying rule for prompts. The prompts sat in the metadata-proposal run's report, which va keeps until Kris uses them, and the first Summary gave them in full. Under PROMPTS-IN-FULL each later va Summary and recap gives all three again, whole and copyable, rather than pointing back to that Summary, until Kris sends them or strikes a mark; then they are dropped with a line in the decisions log, and the run report goes at the next tidy.

## Where it came from

Kris, 24 October 2026, read back in the va decisions log under FINDINGS-SECTION: "if I ask you for some findings ... I could ask you if you could do an investigation or create me some findings on something, and then that needs to be in its own section in the summary, and repeat the same tables until we're happy with things". The same entry records why: the outputs "get lost sometimes with all the things that come backwards and forwards, and scrolling it up and down to find them is really tedious. Also, it's very difficult for me to give you feedback on them if I don't see them because sometimes I'm away from the screen", and of one table, it did not "state it before table ... it doesn't really say what the goal was". The FINDINGS-SECTION line in this package's [messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/messages.md) carries it here.

Under PROPOSALS the same day, Kris asked for this note: "In the same way that we put a proposal together around tending, I suggest that we put a proposal together around these two aspects", findings being the first and repository consistency the second, each a design note here beside [Tending](tending.md), pioneered by va, and adopted by va and personal-principal as interim policy.

## Other territories

Later runs add a `### <Territory> run, <date>` section here, a few short lines on which findings were asked for, whether the goal-first shape and the carrying rule helped, where the finding files lived, and how each was settled.

### Valle Armonia interim pass, 2026-10-24

One quick territory pass applied the interim policy. Goal first made its tending table readable on its own, and REPO-ALIGN, FOLDERS and PROMPTS carried cleanly. Two points were unclear, with short answers:

- **Whether a dispositions table the brief asked for, rather than Kris, is a finding:** no. It is Done, under [What counts as a finding](#what-counts-as-a-finding): only an owner request makes a finding.
- **Whether a run writes `findings/<tag>.md` when its brief names no file:** no. A run writes the file only when its brief names it, as with a design note; otherwise it puts the finding in its run report and the coordinator copies it at receive, under [Where a finding lives between Summaries](#where-a-finding-lives-between-summaries).

### Personal run, 2026-10-24

Personal asked for one finding, REPO-META, the repository metadata survey of its nine members.

- **Fitted:** REPO-META was carried as one finding with its per-repository table, and its decisions went to Kris as separate queries, as [Findings and queries](#findings-and-queries) intends.
- **Did not fit:** REPO-META is held as `findings/REPO-META.md` in Personal's package, which the `ki-work-package` closed list does not yet allow, so it stands on this proposal until that change lands; the survey run left it uncommitted for the coordinator, since its brief barred it from the package.
- **Missing, with a short answer:** how a run hands a finding to a package it may not edit. Through its run report: the run writes the finding there, goal first, and that package's coordinator copies it into `findings/<tag>.md` at receive and commits it, as it copies queries today.
- **Differed from Valle Armonia:** Valle Armonia's pilot findings were tables held in this note; Personal's was the first held as a package file.
