# obs-review-6: blind review of MERMAID-HANDLER

Read-only review. Change no file in any repository.

Repository: /Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local. Read [KI-OBSERVA-APP-046](</Users/krisbrown/workspaces/knowledge-islands/apps-observatory.local/docs/roadmap/KI-OBSERVA-APP-046-browser-smoke-check-red.md>) (its Outstanding concerns), the Mermaid rendering and sanitising path, the drawing frame's content policy and the smoke check's hostile-label step, then answer independently.

**Context:** A hostile Mermaid label's `onerror` stays in the drawing frame just long enough for the frame's content policy to refuse it, although no drawn element keeps it. The smoke check now counts that refusal as containment. **Query:** Should Mermaid's sanitising be made to strip the handler before the policy has to refuse it? **Options:** a) Accept as is and leave it as a review note. b) Capture a triage record to harden the label sanitising.

Report as an owner report with heading `# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Observatory](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/observatory.md) › obs-review-6`, the bold form line, `---`, Done, In Progress, Queries. Under Done give the option you recommend, a confidence of high, medium or low with a one-line reason, and any factual claim above the code contradicts. British English, ASCII hyphens only.
