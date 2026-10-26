# wow-review-answer-vector - blind review of one Observatory design query

You are an independent reviewer. Verify the Context's claims directly in the Observatory at /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local (its specs, contract, roadmap records including KI-OBSERVA-BRG-004, and the feedback-send path), tools-ki at /Users/krisbrown/workspaces/knowledge-islands/tools-ki and the `ki-work-package` standard in /Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness. Pick the option you would recommend, confidence high, medium or low, one-line reason, and note any claim you found false. Do not read any queries.md, decisions.md, *.report.md or design/observatory-review.md file. Read-only: change nothing, commit nothing.

Report under ## Done one ### section: pick, confidence, reason, verified or refuted claims. Then ## In Progress (Nothing) and ## Queries (None).

## ANSWER-VECTOR - whether the first slice writes the answer line itself or waits for a `ki work answer` command

**Context:** The proposal's first slice has the Observatory compose the `messages.md` line and commit it through its own declared file effect, the path `feedback-send` already implements and tests, so the slice needs no tools-ki change. The Observatory's contract prefers consuming stable `ki` commands over duplicating work semantics, and a `ki work answer <id> <TAG> --option a --note "..."` command would make the line's shape one tool's and give the Observatory an argument vector instead. Waiting for it adds a tools-ki unit and a pin before anything can be answered in the Observatory; building the file effect first means a later swap to the command.

**Query:** Should the first slice write the line through the Observatory's own file effect, with the `ki work answer` command as a later record, rather than wait for the command?

**Options (unranked):**

- Wait for tools-ki to provide `ki work answer`, and have the Observatory's first slice declare it as its vector from the start.
- Build the first slice on the existing file effect; capture `ki work answer` and `ki work queries` for tools-ki as a later message and the Observatory's KI-OBSERVA-INT-005.
