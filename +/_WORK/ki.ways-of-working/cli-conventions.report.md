# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › cli-conventions

**🤖 → 👤 Handoff to supervisor · Run report at 18:58 BST · last mark 18:12 BST**

---

## Done

- **Guidance written.** `ki-repo-tools` now has a command-line conventions reference, as you corrected at 18:08 BST, so no KI-TOOLS-SKILL query is raised. It covers:
  - POSIX option syntax and GNU long options, with `--` and `-`.
  - The common flag letters: `-h`, `--version`/`-V`, `-v`, `-q`, `-n`, `-f`, `-y`, `-r`/`-R`, `-0`, `--json` and `--color`.
  - The `-H`, `-L` and `-P` symbolic-link options.
  - Standard output and standard error, exit statuses, `NO_COLOR` and terminal behaviour, prompts and signals.
  - The XDG directories for configuration, state and cache.
  - Steps for choosing a new option.
- **Where it is linked.** SKILL.md, the tool-repository standard, the audit judgement pass and the scaffold steps all link to it.
- **Sources.** Seven sources are cited: the POSIX utility conventions, POSIX `find`, the GNU coding standards, the Bash exit statuses, clig.dev, `NO_COLOR` and XDG. The symbolic-link survey from the mgit-learn run was reused.
- **Limitation.** Each source is cited from its published text but was not re-fetched, because this run had no network grant. The next refresh of the skill's sources re-reads them.
- **Record.** [KI-HARNESS-GOV-218 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/a44fed7cd4d02aedf2d6c030e5caf30ed4e7fdcd/docs/roadmap/KI-HARNESS-GOV-218-cli-conventions.md) is now Awaiting review. No existing record fitted. Net records: ki-agentic-harness +1, ki-principal 0, tools repositories 0.
- **Commits.** ki-agentic-harness `78b04030` reserved the record number. `58307975` added the guidance and the record. Both are pushed. The other sessions' `fda24ea2` and `578c0840` were already on origin, so none went with mine.
- **Checks.**
  - `bun run test`: pass, 1255 tests.
  - `bunx tsc --noEmit`: pass.
  - Rubric: in sync.
  - `ki-skills` and `ki-authoring` audits: pass.
  - Commit gate: pass.
  - `ki-work-roadmap` audit: passes the new record. It fails on two records outside this run: [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md), whose review section is out of order, and another session's [KI-HARNESS-GOV-219 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/f9da11ced73eaab512d5df6a4ef6d21f574ce89d/docs/roadmap/KI-HARNESS-GOV-219-feedback-work-folder-kind.md).
- **What the three tools already do well.** I read their help, ran `--help`, `--version` and a few invalid commands, and searched their code; no tool code was changed. All three:
  - exit 0 for success, 1 for an operational failure and 2 for a syntax error;
  - have `-h`/`--help` and `-V`/`--version`;
  - write errors to standard error;
  - keep their files in the XDG directories.

  mgit's `-P`/`-L` already match the Unix meaning.
- **Departures in tools-mgit:**
  - `-f` means `--filter`. Unix tools use `-f` for force or file.
  - It does not accept `--jobs=2` or `-j2`, and does not accept grouped flags such as `-vW`.
  - `--dry-run` has no `-n`, and `worktree remove --force` has no `-f`.
- **Departures in tools-rig:**
  - It does not accept `--format=json`; only `--format json` works.
  - Machine output uses `--format text|json` rather than `--json`, which mgit uses.
  - `--dry-run` has no `-n`.
  - I found no `--` end-of-options handling in its option code. I searched for it but did not test it.
- **Departures in tools-ki:**
  - `ki --version` prints only `0.11.2`. GNU and the house standard both expect `ki 0.11.2`.
  - `repo audit` and `repo conform` write their progress display to standard output, not standard error.
  - Machine output uses `--format <text|json>`.
  - `-f` means `--filter`, as in mgit.
  - `--dry-run` has no `-n`.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- [KI-HARNESS-GOV-218 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/a44fed7cd4d02aedf2d6c030e5caf30ed4e7fdcd/docs/roadmap/KI-HARNESS-GOV-218-cli-conventions.md) awaits acceptance.
- [KI-HARNESS-GOV-210 (pruned)](https://github.com/knowledgeislands/ki-agentic-harness/blob/218b8e3df7c67412382c34960cf4edfc3c7a9152/docs/roadmap/KI-HARNESS-GOV-210-work-model-write-in.md) fails the roadmap audit because its review section is out of order. It predates this run and was left alone.

## Queries

### CLI-DEPARTURES - where the tools' departures go

**Context:** The three tools depart from the new guidance in the small ways listed under Done. None of them breaks anything today. The fewest-records rule favours adding them to records that already exist. Tools burndown already covers the tools repositories.

**Query:** Should the departures go to Tools burndown, to be added to each tool's existing records, or stay in this report only?

**Options:**

a) (recommended, confidence medium - keeps tool work with its owner and adds no record where one fits) Send Tools burndown one Messages line listing the departures for each tool, to be added to each tool's existing records and fixed at its next change.

b) Leave them in this report only, and fix them when each option is next touched.

### CLI-F-FILTER - `-f` for filter in ki and mgit

**Context:** Across Unix tools, `-f` means force or file. ki and mgit both use `-f, --filter` for the same thing, a basename prefix. Neither has a force flag at the top level. mgit's `worktree remove --force` has no short form for this reason. As written, the guidance allows only force or file for `-f`.

**Query:** Should `-f, --filter` stay as a recorded house exception, or move to another letter in both tools?

**Options:**

a) (recommended, confidence medium - it is the same in both tools, is already in use, and blocks no force flag today) Keep `-f, --filter` in both tools, and name it in the guidance as the one house exception.

b) Move filter to another letter in both tools so that `-f` is free for force. This breaks a flag already in use, and its help, completions and manuals change with it.
