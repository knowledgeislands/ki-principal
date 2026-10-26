# Blind review: an orphaned work folder

You are an independent reviewer. Read the evidence yourself in `/Users/krisbrown/workspaces/knowledge-islands/ki-principal` (Git history, `+/_WORK/ki.specifications/`, `+/_WORK/ki.portable-specifications/`, and `/Users/krisbrown/.local/state/ki/agents/specifications/`). Do not read `+/_WORK/ki.ways-of-working/queries.md`, `decisions.md` or any report under `+/_WORK/ki.ways-of-working/`. Change nothing.

## Context

`+/_WORK/ki.specifications/` was opened on 19 October 2026 as the Project work package for KI Specifications (`cd388627`). The same day the Project was renamed and its tracked files moved as pure renames to `+/_WORK/ki.portable-specifications/` (`a90aea3b`), which has been on hold since 20 October. 25 `*.report.md` files were left at the old path; they were untracked run reports swept into Git by a `chore: baseline` commit `e78fff63` on 24 October. They are said to be byte-identical copies of the run reports still held in `/Users/krisbrown/.local/state/ki/agents/specifications/`. The renamed package holds no reports.

## Query

Who owns the orphan folder, and how should it be repaired? Possible courses, unranked:

- Owner ki.portable-specifications, deleting the folder now in a bounded run, relying on the run directory as the surviving copy.
- Leave the folder untouched until the Project resumes, sending nothing.
- Owner ki.portable-specifications: send a line to its messages.md naming the 25 reports; when it resumes it checks each against its decisions log, then deletes the folder by explicit path.

## Report

Verify the byte-identity claim yourself. Give your recommended course with confidence (high, medium, low) and a one-line reason, and any course you would add.
