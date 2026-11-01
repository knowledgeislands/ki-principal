# Brief: file the Orca question-card bug

Work: ki.prj.orca-evaluation. Authority: Kris, 31 October 2026, "Yes, via the Orca evaluation work", to raise this one bug with Orca. Nothing else may be sent.

1. Find Orca's public bug route (check `orca --help`, the app's Help or About links, and the product's public GitHub repository with `gh`). Search it for an existing report of the same problem; if one exists, add nothing and report its link.
2. Otherwise file one short bug report, plain and factual: In Orca 1.4.245 on macOS, the native chat question card (Claude Code's AskUserQuestion card) drops line breaks in the question title and option descriptions and renders them as one bold run of words, flattening headings, bullets and paragraphs; Claude Code in a terminal and Zed keep them. Suggest keeping line breaks, for example `white-space: pre-wrap` on the title and descriptions, or rendering them as Markdown. Evidence: the question-prompt design at /Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/question-prompt/design.md (read it to confirm the component; do not quote private paths or names in the report). Do not include any personal details, emails or repository names.
3. If there is no route you can file through without a login prompt or a choice only Kris can make, stop and say so in the report with the draft text ready.

Write only ~/.local/state/ki/agents/ki-prj-orca-evaluation/file-card-bug.report.md with the link or the draft, then call worker_done. No edits, commits or other sends.
