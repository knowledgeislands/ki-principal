# ahp-spec (ki.sop.main)

Goal: Kris, 6 Nov: "add <https://microsoft.github.io/agent-host-protocol/> into the list of other specs such as MCP, WebMCP, A2A etc". An explicit owner instruction for one bounded change, so no Enactment record is needed; cite these words in the commit body.

1. Find where Knowledge Islands lists outside protocol specifications such as MCP, WebMCP and A2A: search ki-principal first (`Resources/`, then `Pillars/`), and also ki-specifications and ki-agentic-harness if the list lives there. If there are several lists, add it to each that lists outside agent protocols; if none, report that and stop.
2. Fetch the page (read-only) to learn what the Agent Host Protocol is, who publishes it, its status and version.
3. Add an entry in exactly the shape of its neighbours (same fields, ordering, link style, British English, ASCII hyphens only). If the list's entries have their own notes in `Resources/`, create one for it in the same shape, with its index note updated.
4. Run the repository's checks (`ki repo audit`, rumdl). Commit by explicit path, lower-case Conventional Commits subject; pull with `git -c pull.autostash=false -c rebase.autoStash=false pull --ff-only`; push fast-forward only; never stash, reset, force or --no-verify. Post nothing outside Kris's repositories.

Report: run report naming each file changed.
