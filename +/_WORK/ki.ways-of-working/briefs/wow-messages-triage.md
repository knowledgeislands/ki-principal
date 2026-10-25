# wow-messages-triage - turn the queued messages into owner queries

## Goal

`+/_WORK/ki.ways-of-working/messages.md` in Knowledge Islands Principal holds nine routed requests (UNATTENDED-AND-DUE-DATES, DIAGRAM-PRIVATE-CITATIONS, SOP-PROJECT-CARE, SINGLE-THREAD, WAKE-SUBSTRATE, UNWRITTEN-RULES, SIZE-LABEL, WORK-LABEL, PERM-PROMPTS). Each asks for a change to a shared standard, which the coordinator may not make in tonight's unattended window. Draft, for each, the decision Kris must make so it can be put to him on his return at 08:00 GMT.

## Scope

- Read each line in full and the evidence it links. Read the current standard it would change in the KI Agentic Harness (`/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/`: `ki-coordination`, `ki-work-package`, `ki-delegation`, `ki-work-roadmap`, `ki-diagrams` or as the line names), so that each Context says what the standard does today.
- Write `+/_WORK/ki.ways-of-working/design/messages-triage.md`: one `###` query per line, headed `<TAG> - <plain-language title>`, the tag being the line's own tag, carrying exactly **Context:** (enough to decide without reading anything else, quoting Kris's words from the line), **Query:** (one sentence) and **Options:** with lettered lines, `a) (recommended, confidence <high|medium|low> - <one-line reason>) <course>` first and real alternatives beneath. Where Kris has already decided the substance (SIZE-LABEL under VA-HIGH a, WORK-LABEL as he asked it), the query is only whether to land it now, and as which run.
- Split a line into several queries where one decision would bundle unlike choices (UNWRITTEN-RULES asks for one query per rule). Keep every query short enough to answer by letter.
- Never write the standard itself, `queries.md`, `messages.md`, `decisions.md` or `state.md`.

## Constraints

- British English, ASCII hyphens only, under `ki-authoring`.
- Commit the one new note by explicit path and push fast-forward; never force or use `--no-verify`. Another run is editing `design/review-pack.md` alongside you: never touch it.

## Report

Done: the note, its commit and the count of queries with their confidences. Queries: only a genuine ambiguity in a message.
