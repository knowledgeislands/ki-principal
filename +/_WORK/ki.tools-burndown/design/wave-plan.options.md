# WAVE-PLAN options, for blind review

## WAVE-PLAN - first rollout grant

**Context:** Under ROLLOUT-AUTHORITY a), each wave runs under one owner grant. The run commits each repository's conversion locally by explicit path, and Kris pushes. A conversion means: write both `.githooks` hooks with the Husky content inlined, change `prepare`, remove `husky` and `.husky/`, rebind the clone, then prove that a commit refuses in a fresh worktree with no install and passes after an install. The note proposes five waves:

1. Pilot: ki-principal, tools-ki and va-principal.
2. Knowledge Islands Bun repositories: ki-agentic-harness, ki-design, ki-techne-harness, tools-techne, tools-git-almanac, apps-knowledgeislands.info, apps-observatory.local and the eight `mcp-*` repositories.
3. Other Bun repositories: HNR, `5g-emerge-*`, personal and Valle Armonia apps, and apps-yorkphotosoc.org.
4. Package-less repositories, pre-commit only.
5. `commit-msg` for the package-less repositories once KI-TOOL-KI-CLI-161 ships, then the estate sweep on Terra and Sol, then the FAIL step.

Converting before the standard changes would make `PKG-5` and `SCR-11` fail in the converted repositories. That is why the harness change comes first, and it is held behind the other harness session.

**Query:** Do you grant wave 1, the pilot in ki-principal, tools-ki and va-principal, to run once the harness standard change has landed?

**Options:**

a) Grant wave 1 now, to run after the harness standard and the tools-ki conform changes land. Later waves come back to you one at a time.

b) Grant wave 1 to run now, by hand from the template, ahead of the standard. This accepts WARN or FAIL findings on `PKG-5` and `SCR-11` in the three repositories until the harness change lands.

c) Hold all waves until KI-TOOL-KI-CLI-161 ships, so that each repository converts once with both hooks complete.
