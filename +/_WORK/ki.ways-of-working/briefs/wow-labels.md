# wow-labels - T-shirt size display and label-then-id work naming

## Goal

Land two decided conventions in the KI Agentic Harness in one run. Kris agreed both on 2026-10-25 at 08:00 GMT ("With WORK-LABEL" / "With SIZE-LABEL").

1. **SIZE-LABEL.** Kris, 24 October: "I wonder if there's a way of showing T-shirt S, M, etc. next to it. And probably put it in a capital letter, almost like it's a label on a t-shirt." In `ki-work-roadmap`'s Priority and size section, add one paragraph: reports and messages display a size as 👕 plus the capital letter (👕 S, 👕 M, 👕 L, 👕 XL). Field values stay `s`, `m`, `l`, `xl`, and there is no XS.
2. **WORK-LABEL.** Kris, 25 October, on "Personal > Tower (personal.regular.tower)": "I like this label, the way that you put the work package in brackets after it at the end. Can we adopt that as a standard?" In `ki-coordination`'s Work naming, make `<label> (<id>)` the work name used wherever a session names a piece of work: replies, reports, message sender labels, hand-offs and openers. In `ki-work-package`'s message line form, add the id after the sender label, for example `KI > Model > Ways of working (ki.ways-of-working):`. Accept the old form through the tolerance window.

## Do

- Work in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`, in a clean temporary clone of `origin/main` or the primary checkout if it is clean. Edit the standards, update any rubric criteria and examples the change touches, and regenerate the generated surfaces (`ki dev skill generate ki-coordination --write` and any others the changes reach).
- Run the harness's tests and audits, including the banner test, until they pass. Commit by explicit path as Conventional Commits ending with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`, pull with rebase and push fast-forward only.
- After pushing, append one REFRESH line naming the new harness revision and the two changes to `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md`. State of play forwards it to live works. Commit and push that by explicit path.

## Do not

Change any other standard, release or tag anything, change GitHub settings, force-push, use `--no-verify`, or touch another session's uncommitted files.

## Report

The owner report: Done with commits and checks, In Progress, and Queries, each with Context, Query and Options, the recommended option first with its confidence and reason.
