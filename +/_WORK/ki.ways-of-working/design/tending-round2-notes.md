---
note_type: streams/design
title: Tending round two practice notes from Valle Armonia
status: draft - October 2026
purpose: Feed the second Valle Armonia Tending round's practice notes into the Tending note
author: Written with Claude
work: ki.ways-of-working
run: va
agent: tending-collate
written_at: 2026-10-24
---

# Tending round two practice notes

Valle Armonia ran its second [Tending](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.ways-of-working/design/tending.md) round on 24 October over four repositories: apps-vallearmonia.com (website), va-agentic-harness (harness), apps-markhowarth.com (Mark) and va-principal with the territory and PMO track (principal). A decisions tidy-up ran alongside and left no notes. Each note below names the runs it came from, merged where two runs said the same thing.

## Useful

- Package lines that were already decided turned twelve warnings into one mechanical commit (website).
- Checking each package line or record against its Git history and testing whether its subject still exists found three done or already-held lines and one done-but-open record (principal, website).
- A grep across the whole territory for a repository's previous names found stale paths, including an out-of-date guide tree and a Known Lands entry that the repository's own audit cannot see (website, Mark).
- A link resolver run over every Markdown file found a link to a pruned record in another repository (website).
- Comparing a Project's records with its outcome confirmed coverage, and grepping member front matter against the registry was quick (Mark, principal).
- Reading the standard's own sections, such as `ki-repo-harness` source layout and root orientation, found gaps the audit does not catch (harness).
- Checking the installed harness's Git state, not just the commit, explained why a fixed warning was still reported (harness).

## Noise

- PMO levels 1 and 2 on a repository with no packages or records, and most level 3 lenses on a one-skill harness (harness, Mark).
- One disposition repeated many times: CLEAN-3 lists nine branches one record covers, and STREAM-14 repeats one area disposition fourteen times (website, principal).
- CLEAN-4 fires on the run's own local commits and counts other sessions' commits (website, principal).
- The previous-names check also hits names kept on purpose, for history or for Workers (principal).

## Missing

- Whether a member repository's run may carry out a decided line held in another package; the website run did, following the RELABEL-MARK precedent (website).
- A check that a record's body still agrees with later decisions in its Project note, as with a packaging record that still contradicted a 24 October decision (website).
- A check that a package line's subject closed after the line was written (principal).
- A check for an opt-in whose model has been retired, such as the Paperclip coordination skill after its record was cancelled (principal).
- A level 1 step confirming that an upstream fix is in the installed payload: a symlinked harness follows whichever branch its checkout is on, not `main` (harness).
- A rule on whether a dependency described in a triage record's prose also goes in `blocked_by` (Mark).

## Could become mechanical

- A guide's file tree naming paths that do not exist (website).
- Documentation that contradicts an opt-out in `.ki.toml`, such as `auto_memory = "disabled"` (website).
- A repository's previous names still appearing in other members' and the Capital's tracked files, with an allow-list for deliberate mentions (Mark, principal).
- A package line that names a record now done, or asks for a field every named record already carries (principal).
- The installed harness not being at its pinned or `main` revision (harness).
- A harness orientation that leaves out the audit and conform commands, and a shelf README that contradicts the standard on MCP source (harness).
- An audit baseline that shows only the verdict because the default output hides passes and judgement items (Mark).

## Time

About 6 to 12 minutes per repository: website 12, Mark 7, harness 6 and principal 6.
