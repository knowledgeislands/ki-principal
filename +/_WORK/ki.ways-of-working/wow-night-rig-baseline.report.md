# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-night-rig-baseline

**🤖 → 👤 Handoff to supervisor · blocked · Run report at 02:31 BST · last mark 01:40 BST**

---

## Done

Confirmed the rule defect: FILES-10 rejects `[[skills.ki-repo-tools.assembled]]`, although ASSEMBLE-1 explicitly requires an array of artefact records. The inline-table alternative conflicts with ki-authoring's TOML rules.

Schema and layout proof: passed; the existing declaration is valid, and making both arrays multiline preserves its complete parsed meaning but leaves the subtable rejection.

Full audit: ran offline in a disposable worktree using a fresh copy of the specified audit home; PASS=15 WARN=5 FAIL=0, with FILES-10 still reporting all three findings as warnings because the isolated registry has no registered Capital. This does not establish a green territory baseline.

Assembly check: passed unchanged; tools-rig main remains clean at `f92d9a1cef403c80ddcc640c8672f3538e43fa26`, with no Rig edit or commit.

Concurrency check: chezmoi and hooks runs were at rest; tools-rig main had no uncommitted work.

Recorded one defect line in [tools-burndown messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.tools-burndown/messages.md); committed as `0f37a2ce` (`docs(work): report Rig assembly layout rule conflict`) in ki-principal, explicitly touching that path alone.

Message verification: Markdown and whitespace checks passed; commit hooks passed, and the committed-path inspection confirmed only the intended message file.

Pending handoff: ki-principal on `sol.local`, branch `main`, holds this unpushed message commit above other sessions' commits; no push was attempted. The next session on another machine must reconcile this checkout first.

## In Progress

Nothing running. Tools-rig's lane remains blocked until the harness reconciles FILES-10 with ASSEMBLE-1. No new record, live apply, provider change or publication occurred.

## Queries

### RIG-BASELINE - Reconcile the harness rule

**Context:** Multiline arrays remove two findings, but FILES-10 still rejects the array-of-tables shape that the assembly schema requires. Reshaping Rig alone cannot satisfy the complete governing TOML contract without changing its meaning or violating the inline-table rule.

**Query:** Route the FILES-10 defect to the harness owner, then rerun this baseline repair before restarting the Rig lane?

**Options:**

a) (recommended, confidence high - the schema and layout checks reproduce the contradiction) Reconcile FILES-10 with the assembly array-of-tables contract, then redispatch the Rig baseline check.

b) Keep the Rig lane held pending a wider configuration-contract decision.

### 🤖 → 👤 Handoff to supervisor · blocked · since 02:31 BST

🤖 0 running · ⛔ 1 blocked

- [blocked] RIG-BASELINE: FILES-10 conflicts with the assembly schema · ki.ways-of-working coordinator · since 02:31 BST
