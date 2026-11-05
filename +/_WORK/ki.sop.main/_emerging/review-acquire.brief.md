# review-acquire (blind review)

Independent review: you have not seen anyone's recommendation; give your own. Do not read any `discussions.md`, `decisions.md` or `*.report.md` in a `+/_WORK/` folder. You may read the three skills in /Users/krisbrown/kis/knowledge-islands/ki-agentic-harness and munin in /Users/krisbrown/kis/personal/assistant/prototype/munin/.

## ACQUIRE-SKILLS - how the Harness acquire skills follow munin

**Context:** munin, the assistant's capture tool, now handles Granola acquisition. Once it handles ChatGPT too, `ki acquire` can be retired ([KI-TOOL-KI-CLI-176](/Users/krisbrown/kis/knowledge-islands/tools-ki/docs/roadmap/KI-TOOL-KI-CLI-176-git-style-extension-veneer.md)). Three Harness skills, `ki-acquire`, `ki-acquire-chatgpt` and `ki-acquire-granola`, govern the acquisition that `ki acquire` performs today.

**Query:** What should happen to those three skills as munin takes over?

**Options (unranked):**

- Move the skills into krisb/assistant so they live alongside munin. The guidance then belongs to the tool's owner, but it leaves the portable Harness for a personal repository.

- Point `ki-acquire-granola` at munin now and leave the ChatGPT skill on `ki acquire` until munin covers it. This is accurate sooner, but for a while the guidance is split across two tools.

- Keep all three until `ki acquire` retires. Then retire them together, each leaving a short pointer to munin's own documentation.

Give your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
