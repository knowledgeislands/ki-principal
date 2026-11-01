# [Model](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/kis/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › blind-rename-name

**🤖 → 👤 Handoff to supervisor · Run report at 23:31 GMT · last mark 13:55 GMT**

---

## Done

Blind review complete: recommend Yes, confidence high — one stable thread name avoids a rename after every normal launch and matches the identifier shown in reports.

Exact source checks passed for the standard's differing launch and rename forms and the opener printer's absence of a launch command.

No commits or repository changes; only the authorised report and status files were written. Prohibited queries, decisions and reports were not read.

## In Progress

Nothing is running. The supervisor retains the naming decision and any follow-on delivery.

## Findings

### START-NAME-EVIDENCE - Evidence and missed risks

**Goal:** Independently assess whether the opener should start with the thread name requested in this brief on 31 October 2026.

**Scope:** Local coordination standard, tools-ki opener construction and printing code, and existing opener tests; package and note metadata only for report identity and mark.

**As of:** 31 October 2026, 23:31 GMT.

Verified directly: [Opening work](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:936) specifies the label-and-id launch name and the thread-id rename form; [the footer rule](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:435) uses the same thread-id form. The standard records the dated owner quote; I did not inspect its original conversation independently.

The brief's implementation premise is unverified and differs from this checkout: [opener construction](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/core/work/prompts.ts:40) builds bootstrap text, and [the printer](/Users/krisbrown/kis/knowledge-islands/tools-ki/src/commands/agent/index.ts:342) prints that text without a Claude launch command. This is a source inspection, not a live runtime test; another installed version may differ.

Changing only the opener sentence would leave [Work naming](/Users/krisbrown/kis/knowledge-islands/ki-agentic-harness/skills/change-management/ki-coordination/references/standards-coordination.md:178) assigning the label-and-id work name to native sessions. Qualify that rule too. The shorter session name also loses the display label and any machine suffix; keep that information in the opener and report heading. The work id remains authoritative.

## Queries

### START-NAME - Use the same name from launch

**Context:** Launch and rename currently have different prescribed names. The label remains available in the opener and report heading, while the stable work id identifies the package. The checked CLI does not yet print the launch command described by the standard.

**Query:** Should the opener's starting session name also use the thread-id form?

**Options:**

a) (recommended, confidence high - one stable identifier avoids an immediate manual rename and makes the session match its reports) Yes: use the same thread-id name at launch, qualify the native-session naming rule, and ask tools-ki to provide a matching launch command after checking its delivery baseline.

b) No: retain the label-and-id starting name and use the thread-id form only for renaming.

### 🤖 → 👤 Handoff to supervisor · since 23:31 GMT

👤 1 with you

- [with you] START-NAME · supervisor · since 23:31 GMT

🧵 ki.prj.ways-of-working
