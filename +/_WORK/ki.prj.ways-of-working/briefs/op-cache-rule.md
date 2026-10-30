# Brief: op-cache-rule

Work: ki.prj.ways-of-working. Received message OP-CACHE (30 October 2026, from hnr.sop.main): Kris: "agents should be using cached_op", not repeated `op` calls. The cached reader is chezmoi's `~/bin/chezmoi/op_cache "op://<vault>/<item>/<field>"`, one prompt per item per day, managed by `chezmoi_op`. Carry the rule into the delegation guidance and brief templates.

1. Verify the reader exists and how it is invoked: read `~/.local/share/chezmoi` sources for `op_cache` and `chezmoi_op` (do not run them and read no secret values).
2. Find where `ki-delegation` (in `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness/skills/`) sets brief templates, authority footers or credential guidance, and where `ki agent` renders footers (tools-ki). Draft the exact rule text and where it goes.
3. Find the KI Agentic Harness's receiving work package under `+/_WORK/*/work.md` in ki-principal (routing description), and add one line to its `messages.md` in the `ki-work-package` Messages line shape, naming OP-CACHE, Kris's words, the date, and the drafted text location. If tools-ki renders the footer, add a line to ki.prj.tools-burndown's `messages.md` too.
4. Write the drafted rule into `design/op-cache-rule.md` in this package.

Change no skill or tool. Commit each file alone by explicit path; push fast-forward only. British English, ASCII hyphens only.
