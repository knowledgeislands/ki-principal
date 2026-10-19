# acceptgit2 - independent accept pass, mcp-git-audit and tools-git-almanac

Kris set TO-DONE on 20 October (/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/decisions.md): take every record to Done, with an independent accept pass. burnrig's report is /Users/krisbrown/.local/state/ki/agents/tools-burndown/burnrig.report.md.

In mcp-git-audit, take KI-MCP-GIT-FND-006 from Awaiting review to Done under `ki-accept`: verify it yourself against its Verify section and acceptance criteria (run the gate and the checks it names), not from the report. If it passes, accept and prune it as ki-work-roadmap says, pinning any absolute links first. If it fails, send it back to In progress with the failure written in the record. Then, in mcp-git-audit and tools-git-almanac, push main fast-forward if every stacked commit is this work's (burnrig's `6d843bd` and `36a30ec`, and yours); otherwise leave it and name the others. Commit by explicit path; never --no-verify or force-push; leave other sessions' files alone. Report under Done, In Progress and Queries.

Authority (coordinator, 00:25 BST, answering acceptgit's ACCEPT-AUTHORITY a)): this run may accept and prune KI-MCP-GIT-FND-006 after its independent checks pass, and may push burnrig's `6d843bd` and `36a30ec` with its own commits; both are this work's, under TO-DONE.
