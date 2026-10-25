# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-labels

**🤖 → 👤 Handoff to supervisor · Run report at 08:09 GMT · last mark 01:07 GMT**

---

## Done

- SIZE-LABEL landed in `ki-work-roadmap` Priority and size: reports and messages show a size as 👕 S, 👕 M, 👕 L or 👕 XL, field values stay `s`, `m`, `l`, `xl`, no XS, with Kris's 24 October words and the 25 October adoption cited. Harness commit `fa9c6739`, `docs(ki-work-roadmap): display size as a T-shirt label`.
- WORK-LABEL landed in `ki-coordination` Work naming as the **work name**, `<label> (<id>)`, used wherever a session names a piece of work: replies, reports, message sender labels, handoffs, the native session name, the opener's `Label:` line, the rename line and the thread line; the three opener templates and the territory routing example now carry the id, the SKILL.md summary names the work name, and the label alone stays readable through the tolerance window. Harness commit `0404754a`, `docs(ki-coordination): adopt label-then-id work name`.
- `ki-work-package` Messages lines now read `- <date> · <TAG> · <sender label> (<sender id>): ...`, with the example `KI > Model > Ways of working (ki.ways-of-working):`, the tolerance sentence for label-only senders, the checker's failure message updated and a new test proving both forms pass. The checker's regex already accepted both, so no behaviour changed.
- Checks: `bun run test` 1468 pass, 0 fail; `bunx tsc --noEmit` clean; Biome clean on the two TypeScript files; rumdl clean on the four Markdown files; `ki dev skill generate ki-coordination` reports all seven surfaces in sync, so no generated surface needed rewriting; `ki dev skill rubric` in sync for `ki-coordination`, `ki-work-package` and `ki-work-roadmap`; `ki repo audit --skill ki-skills` FAIL=0; the pre-commit harness audit passed on each commit.
- Published: harness `main` fast-forwarded to `0404754a` on `origin`, no divergence. The REFRESH line naming `0404754a`, WORK-LABEL and SIZE-LABEL went into `/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki/messages.md` as an important line below the two existing important lines, the position the standard gives a REFRESH line rather than the end, committed as `docs(work): ki message from ki.ways-of-working` and pushed, principal `main` at `3aa56315`.
- Deviation from the brief's template: the co-author trailer names Claude Fable 5.1, the model that made the commits, as the commit-trailer rule requires, not the Opus 5.5 text the brief's Do line carried.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- Fleet finding, not in the contract under change: `ki repo audit --skill ki-skills` warns three times under LONG-3 that `ki-skills` `references/sources.md` has sources last reviewed in July 2026, past the quarterly refresh cadence.
- A secondary State of play's work name doubles the brackets by the rule as adopted, `KI > SoP (sites) (ki.sop.sites)`; the thread line already produced this form before this run, so nothing new was introduced.

## Queries

### OPENER-LABEL - Bring the printed opener's Label line level with the standard

**Context:** The `ki-coordination` standard's three opener templates now read `Label: <Territory> > <Theme> > <Project> (<territory>.<project>).` and the equivalents for territory and secondary work. `ki agent prompts`, which prints the filled openers, lives in `tools-ki` and still prints the label without the id; the standard accepts that older form through the tolerance window, and the `claude --name "<label> (<id>)"` launch command it prints already carries the id. Sending work to another repository needs Kris's permission unless already authorised.

**Query:** May State of play send `tools-ki` a message asking it to print the opener's `Label:` line as `<label> (<id>)`?

**Options:**

a) (recommended, confidence high - the standard and the printed opener should say the same thing, the change is one template line in `tools-ki`, and the tolerance window keeps everything working meanwhile) Send one line to the work that owns `tools-ki`, citing WORK-LABEL and harness `0404754a`. b) Leave the printed opener as it is and let the tolerance window carry the difference.

### 🤖 → 👤 Handoff to supervisor · since 08:09 GMT

👤 1 with you

- [with you] OPENER-LABEL · owner · since 08:09
- [committed] harness and principal

🧵 Coordination thread · KI > Model > Ways of working (ki.ways-of-working)
