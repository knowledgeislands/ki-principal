# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › wow-standards

**🤖 → 👤 Handoff to supervisor · Run report at 03:07 BST · last mark 02:01 BST**

---

## Done

- Harness `609ee238`, feat(ki-coordination): COORD-9 now counts the roadmap records awaiting acceptance for each piece of Project work's Project, across the Capital and the checkouts beside it that name the same Capital, and warns over eight. A test covers it. A smoke run against Knowledge Islands Principal flags Observatory at 10 (and Ways of working's 16 open queries, as before).
- Harness `071567a1`, docs(skills): the take-stock rules are now in the standards, each quoting Kris's words and date:
  - `ki-coordination`: SMALL-FIXES, squared with the first hard rule as bookkeeping in the coordinator's own package; CLAIM-CHECK; masked BLIND-REVIEW; the OWNER-QUEUE cap, with a `📥 <n> to accept` count on the banner; OOS-WAKE as standard text, with the watcher left to its tooling.
  - `ki-delegation`: the brief side of CLAIM-CHECK, CLASS-FIX, BLIND-REVIEW and CAPTURE-GATE; the GREEN-MAIN green baseline; the waiter's OOS-WAKE line.
  - `ki-git`: GREEN-MAIN, so harness edits are made off the shared primary checkout.
  - `ki-next`, `ki-work-roadmap` (one consistency line): CAPTURE-GATE and the 14 October burn-down focus.
  - HOMELESS-STANDING: PRFLOW now lives in the harness AGENTS.md and RIG-REL-PATCH in release readiness. PIN was already carried by `ki-engineering`.
  - The output style was regenerated.
- Generated surfaces: `ki dev skill generate --write` writes only into the primary checkout, so I rendered them in the worktree with the skill's own generator module. Only the output style changed. I edited rubric.md's COORD-9 lines to match the new item text.
- `bun run test`: 1327 passed, 0 failed. `bunx tsc --noEmit`: clean.
- Focused audits: `ki-coordination`, `ki-delegation`, `ki-git` and `ki-skills` pass. `ki-work-roadmap` keeps the same 11 warnings as `main`. `ki-next` and `ki-repo-tools` are not declared in the harness, so they cannot be audited there.
- Integration: the primary harness checkout was fast-forwarded to `071567a1`, and both commits (mine only) were pushed fast-forward to `origin/main`. The worktree and the `wow-standards` branch are removed, and the temp folder is empty.
- REFRESH: one important line each went to 13 live works in Knowledge Islands Principal (`75ac5f28`) and to State of play in er (`1300234`), hnr (`b86e4a2`), lgl (`8d35236d`), kb (`b1c80902`), si (`ea760f3`), tmx (`32421c1`) and va (`9307b37`). Each line names the changed rules and links the standards at `071567a1`; the capital lines also ask State of play to pass it on. The set is refresh-banner's, with four changes:
  - added: ki.agent-host, ki.estate-factorisation, ki.paperclip-capture-and-rebuild and ki.portable-specifications, which are now live;
  - dropped: ki.regular.registry-removal, which no longer exists;
  - skipped: ki.specifications, whose folder is now empty.
- Reply to [kb.regular.acquire-intake messages](/Users/krisbrown/workspaces/personal/acquire/+/_WORK/kb.regular.acquire-intake/messages.md): SMALL-FIXES adopted, now in `ki-coordination` Coordinator responsiveness (acquire `e5cb23b`).
- Unpushed: the message commits above are local only. The brief authorised only the harness push, and other sessions' commits sit beneath mine in ki-principal and lgl.

## In Progress

Nothing is running.

Outstanding - no action requested now:

- The OOS-WAKE watcher and the `ki agent new` masked review scaffold belong to ki.tools-burndown. The standard says out-of-session runs wait for the owner's send line until the watcher ships.
- H9 (accept runs may capture), the CAPTURE-ORIGIN field and CHECKOUT-ISOLATION are still undecided, so none of them is in the standards.

## Queries

No outstanding queries

### 🤖 → 👤 Handoff to supervisor · since 03:07 BST

🤖 0 running · 👤 0 with you

- [committed] harness standards and audit, pushed
- [unpushed] REFRESH and reply lines in ki-principal, er, hnr, lgl, kb, si, tmx, va and acquire
