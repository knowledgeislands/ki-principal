# review-burndown (blind review)

Independent review: you have not seen anyone's recommendation; give your own for each. Do not read any `discussions.md`, `decisions.md` or `*.report.md` in a `+/_WORK/` folder.

## WATCH-AGORA - Whether `ki work watch` is still wanted now Agora rings a doorbell

This is also written into [discussions](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.tools-burndown/discussions.md). It is medium confidence, so it needs one blind review before it goes to Kris.

**Context:** On 1 November Kris decided INBOX-VERB: a read-only command, `ki work watch <work id>`, that waits quietly and wakes a thread when a message lands or a run finishes (the WATCH-VERB line). On 3 November Agora began waking threads itself through a doorbell file (AGORA-DOORBELL), and State of play's own wake now uses it. The method intake of 3 November thought the command was probably no longer needed, but that question never reached Kris.

**Query:** Should tools-ki still build `ki work watch`?

**Options (unranked):**

- Build it anyway, as a fallback for runtimes or hosts without Agora.

- Drop WATCH-VERB as no longer needed now Agora's doorbell exists, keeping its design for reference.

For each: your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
