# review-rename-eda (blind review)

Independent review: you have not seen anyone's recommendation; give your own for each. Do not read any `discussions.md`, `decisions.md`, `*.report.md` or `*.design.md` in a `+/_WORK/` folder.

## RENAME-FENCE - Records under a renamed work now carry over

**Context:** A test added on 28 Oct (`7f91270b`, KI-TOOL-KI-CLI-174) deliberately left a run's control record refused after its work was renamed, and needed a separate new run to continue. Your 1 Nov request, via hnr.sop.5ge, asked for renamed work ids to be followed. I replaced that test: a record made on this machine whose old home is gone now moves to the renamed work, and its earlier attempts stay valid under the former id.

**Query:** Is carrying the record over, rather than refusing it, what you want?

**Options (unranked):**

- No. Keep refusing, with only the single repair command offered.

- Yes. Keep the new behaviour.

## EDA-HOME - Where the Exchange Dynamics Analysis method should live

**Context:** Kris wants a reusable way to analyse a conversation once and present it several ways: as an infographic, a report or an interactive view. It has four parts: the method, a data format (a JSON schema), a visual layout and step-by-step instructions for an agent. The existing skills `archify` and `dataviz` only draw. Neither is owned by Knowledge Islands, and `archify` comes from an outside author, so extending either would mean keeping our own copy of someone else's code. A skill in the KI Agentic Harness can be used from any repository and can include the data format, a checking script and an example. A note in Pillars can only be read inside this island. The harness has no group of skills for analysis yet; the closest group is `acquire`, which already handles turning sources into structured knowledge.

**Query:** Where should the method live?

**Options (unranked):**

- Extend `archify` or `dataviz` to carry the method.

- A Pillars note in ki-principal only, with no skill. Agents in other repositories could not use it directly, and every change would need the Enactment Process.

- The same skill, but in a new `analysis` group of skills, in case more analysis methods follow.

- A new harness skill, `ki-exchange-dynamics`, in the `acquire` group of ki-agentic-harness. It would hold the method, data format, visual layout, agent steps and the invented example, and it would use archify and dataviz to draw. Ki-principal would get an optional short note in Emerging Concepts that points to the skill.

For RENAME-FENCE you may read tools-ki branch `launcher-paths` (`8384a731`) and `7f91270b` read-only. For each: your choice, confidence and a two-line reason. Read-only; no commits. Write it as your run report.
