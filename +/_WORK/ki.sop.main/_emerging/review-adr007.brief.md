# review-adr007 (blind review)

Independent review: you have not seen anyone's recommendation; give your own. Do not read any `discussions.md`, `decisions.md` or `*.report.md` in a `+/_WORK/` folder. You may read the record and the ki-decision-records skill in /Users/krisbrown/kis/knowledge-islands/ki-agentic-harness.

## ADR-007 - Update the acquisition decision record that still names `ki acquire`

**Context:** Harness decision record [ADR-KI-HARNESS-SKILLS-007](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/docs/decisions/ADR-KI-HARNESS-SKILLS-007-provider-neutral-ai-session-acquisition-and-adapter-pairing.md) still says two things that are no longer true. It says each acquisition skill advertises only the actions tools-ki has proven. It also says `ki acquire import --adapter <provider>` is what uses the session adapters and stages captures. Since 5 November tools-ki no longer has `ki acquire`. The assistant's `ki-muninn` runs acquisition, and the skills no longer carry the advertisement front matter. I left the record untouched, because changing a decision record is your decision to make, not a wording fix.

**Query:** Should the harness update ADR-KI-HARNESS-SKILLS-007 to match the move to `ki-muninn`?

**Options (unranked):**

- Leave it as history. The skills and their sources already record the move.

- Replace it with a new decision record that sets out who owns executable importers now that they live outside tools-ki.

- Add a dated amendment to ADR-KI-HARNESS-SKILLS-007. It would record that execution moved to the assistant's `ki-muninn` under ATER-027 and that skills no longer advertise importer actions in front matter.

Give your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
