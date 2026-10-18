# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › rumdl-upgrade

**🤖 → 🧑 Handoff to supervisor · Run report at 11:46 BST · last mark 11:06 BST**

---

## Done

- The house rumdl pin moved from `^0.2.78` to `^0.3.0` in the harness `package.json`, the lock (resolves 0.3.0) and the `ki-engineering` scaffold default and its source evidence. Committed as `4b81efba`. 0.3.0 broke no recorded defence, so the pin did not need to stay where it was.
- Every recorded reproduction ran on 0.2.78 and then on 0.3.0, comparing the output byte for byte. The `MD005`, `MD075` and `MD056` fixtures were the exact recorded ones from the authoring tests. The rest were neutral stand-ins.
  - `MD005` and `MD075` both pass with the rules switched on, on both versions.
  - `MD056`: the house no-fix guard holds, and 0.3.0 no longer truncates the row even without the guard.
  - The `MD060` placeholder-table defect and the `##]` heading-continuation defect still reproduce.
  - The empty-list-item case no longer misbehaves on 0.3.0.
  - `MD030` and the `MD013` pipe skip are unchanged.
  - `MD037` now reports without fixing.
- `--preflight` checks the whole batch before it writes anything. If any file in the batch can't be written, it writes nothing, where plain `--fix` writes the other files. 0.2.78 rejects the flag.
- Fixed point:
  - In the harness, a formatting pass changed one file: a work-review brief that already broke the house format. 0.2.78 flags it and fixes it the same way, so this is not an upgrade change. Committed as `021dddbf`; the harness is now clean across 539 files.
  - In ki-principal, a read-only pass on 0.3.0 gives the same six findings as 0.2.78. All six are in other sessions' uncommitted files: `+/_WORK/ki.chezmoi/decisions.md`, `+/_WORK/ki.ways-of-working/harness-upkeep.report.md` and `+/_WORK/ki.ways-of-working/work-folder-rename.report.md`. I changed nothing there and committed nothing.
- The `ki-authoring` watch items and source review now record all these results. Committed as `102061fb`.
- Full harness gate:
  - `bun run test` passed (1254 tests).
  - `bunx tsc --noEmit` passed.
  - The `ki-authoring` and `ki-skills` audits passed, as did the pre-commit hooks.
  - The `ki-engineering` audit failed once, on its check that the shared Git hooks are bound (`SCR-11`). That check reads `.husky/pre-commit`, which this run did not change, so the failure is not from this upgrade.
- Pushed all three commits to the harness `main` fast-forward. GitHub logged its usual bypass of the pull-request and status-check rule. No other session's commits were stacked beneath mine.
- Net open records: harness 0 and ki-principal 0. The results went into `ki-authoring`'s source list, which is where the watch items live.
- This report is at the run's state path only, as the progress protocol requires. That protocol overrides the brief, so I wrote and committed nothing in the ki-principal work folder.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- 29 other repositories still pin rumdl below 0.3.0 and need the same change:
  - **Knowledge Islands (16, all `^0.2.78`):** `apps-knowledgeislands.info`, `apps-observatory.local`, `ki-design`, `ki-principal`, `ki-techne-harness`, `mcp-acquire-whatsapp`, `mcp-git-audit`, `mcp-gsuite`, `mcp-housekeeping-chatgpt`, `mcp-housekeeping-claude`, `mcp-ki-kb-fs`, `mcp-ki-kb-notion-mirror`, `mcp-m365`, `tools-git-almanac`, `tools-ki` and `tools-techne`.
  - **Humans Not Robots (7):** `5g-emerge-apex`, `5g-emerge-demos`, `5g-emerge-phase2`, `5g-emerge-phase3`, `5g-emerge-testbed` and `infoschematics` pin `^0.2.78`; `hnr-agentic-harness` pins exactly `0.2.78`.
  - **Personal (3, `^0.2.78`):** `apps-midnight.ninja`, `apps-rig.midnight.ninja` and `apps-tower.midnight.ninja`.
  - **Valle Armonia (2, `^0.2.78`):** `apps-markhowarth.com` and `apps-vallearmonia.com`.
  - **Legal (1):** `legal-principal` pins `^0.2.64`.
- The `ki-engineering` hook-binding failure (`SCR-11`) in the harness is an existing finding for a later engineering pass.

## Queries

### RUMDL-ESTATE - Move the rest of the estate to rumdl 0.3.0, then tighten the house template

**Context:** The harness is on 0.3.0, but the 29 repositories listed above are not, and each needs its own install authority to move. Once they have all moved, three changes to the house template become possible:

- `MD005` and `MD075` now pass their exact recorded fixtures and raise no finding in the harness or ki-principal, so both rules could be switched back on.
- `--preflight` would make each formatting pass all-or-nothing.

Both changes alter the template every consumer adopts, and 0.2.78 rejects `--preflight`, so they must wait until the other repositories are on 0.3.0. Claude Design is changing the website repository right now, so it would wait until that work finishes.

**Query:** Should one follow-on run move every other pinning repository to `^0.3.0` and then make those template changes?

**Options:**

a) (recommended, confidence medium - the evidence is clean on both repositories measured, but 27 others are unmeasured and each would be checked for a fixed point as it moves) Authorise one run to move the 28 repositories other than the website to `^0.3.0`, each through its own gate. Once every one is on 0.3.0, switch `MD005` and `MD075` back on and add `--preflight` to the house formatting command in one `ki-authoring` and `ki-engineering` change. The website follows when Claude Design finishes.

b) Move the pins only, and leave the house template unchanged.

c) Leave the other repositories to move on their own next routine dependency update, with no template change.

### 🤖 → 🧑 Handoff to supervisor · since 11:46 BST

🧑 1 with you

- [with you] RUMDL-ESTATE · owner · since 11:46
- [committed] ki-agentic-harness, pushed
