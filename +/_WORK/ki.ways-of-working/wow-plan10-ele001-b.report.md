VERDICT: NOT READY · confidence high · At 447dbce2, three things need fixing: a mixed matrix result can't be classified, the completed-outcome handoff to Awaiting review has no named owner, and one site fact is wrong.

Required changes, each with its exact edit to `docs/roadmap/KI-DESIGN-ELE-001-lit-ssr-spike.md`:

1. **Whether a VM result counts towards the outcome is never stated (Verify, Decision procedure, line 120; Step 7, line 52).** The plan runs plugin worker and plugin VM under both runtimes. The Decision procedure classifies only "direct and plugin" cells and never says what a VM pass or failure means for the outcome. Example: Bun direct fails with a diagnosed runtime cause, the Bun plugin worker fails with a diagnosed toolchain cause, and the Bun plugin VM run renders and passes both verifiers. Read as a passing Bun plugin path, that is **go**. Read as a diagnostic only, it is **conditional go** or **no-go**. A worker can't tell which, and the supervisor can't check the call.
   - Add this after the first sentence of the Decision procedure: "Each plugin cell is the `mode: 'worker'` run only. The VM runs are diagnostics: run both verifiers against any VM output that renders, and record the VM outcome and diagnosis beside the matching plugin cell. A VM pass never counts as a passing plugin path, and a VM failure never changes the class of a cell."
   - In Step 7, replace "also diagnose `mode: 'vm'` with `--experimental-vm-modules`, recording the distinction" with "also run `mode: 'vm'` with `--experimental-vm-modules` as a diagnostic only, which never decides a matrix cell under the Decision procedure, recording the distinction".

2. **No one is named to finish a completed outcome (Step 10, line 55; Boundary, line 36; Delegation, line 149).** Step 10 tells the worker to "complete the supervisor's independent review and protected-path checks before the normal cleanup". The worker can't do that, because the supervisor's review starts only after the worker's run returns. Nothing then names:
   - who runs the normal cleanup after that review;
   - who records "independent reproduction and cleanup result" in the Review packet, which Files touched gives to the implementing worker;
   - who commits that final evidence;
   - who completes the Review packet's six subsections required at awaiting-review (Files touched defines only Delivered and Verification);
   - who moves the record to Awaiting review.

   As written, a completed run either stalls In progress with no owner or reaches Awaiting review before its required evidence exists. See the Query below for who should finish the run.
   - Replace the last sentence of Step 10 with: "For a completed outcome, commit the evidence and the permitted edits, keep the fixture, return the run with the record In progress, and do not accept this record or change production. After the supervisor's independent review and reproduction under Delegation, the worker resumes under the same grant. It runs the protected-path checks and the normal cleanup, records the reproduction and cleanup result in Verification, and completes the Review packet's six subsections under `ki-implement`. It then commits and moves the record to Awaiting review."
   - In Delegation, replace "Cleanup confirmation completes the final review round." with "The resumed worker performs the cleanup under Step 10. The supervisor's confirmation of it at Awaiting review completes the final review round."
   - In Files touched, after "owned and maintained by the implementing worker", add: "Before Awaiting review it is completed as the six-part Review packet that `ki-implement` requires: Delivered, Change Summary, Verification, Outstanding concerns, Post-change review and Mini recap. On blocked, the worker commits the evidence recorded so far."

3. **A site repository fact is wrong, and an owned scratch path is assigned only to the worktree arrangement (Verify, line 116; Files touched, line 61).** In `apps-knowledgeislands.info`, `apps/site/tsconfig.tsbuildinfo` is untracked: `.gitignore` ignores it with its `*.tsbuildinfo` rule. It is not "tracked". The site TypeScript gate writes `.turbo/ssr-spike-site.tsbuildinfo` in either arrangement; nothing copies it. Yet Files touched lists it as "copied under Verify" and as owned only under the worktree arrangement. So in the primary-checkout arrangement, that gate writes a path that is neither owned nor cleaned up.
   - In Verify, replace "preserving the tracked `apps/site/tsconfig.tsbuildinfo`" with "leaving the checkout's ignored default `apps/site/tsconfig.tsbuildinfo` untouched".
   - In Files touched, replace "the four installed dependency directories and `.turbo/ssr-spike-site.tsbuildinfo` copied under Verify are also owned" with "the four installed dependency directories copied under Verify are also owned". Then add: "In either arrangement, `.turbo/ssr-spike-site.tsbuildinfo`, written by the site TypeScript gate, is an owned, untracked scratch path, removed at normal cleanup."

# [Model](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md>) › [Ways of working](</Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md>) › wow-plan10-ele001-b

**🤖 → 👤 Handoff to supervisor · Run report at 10:18 BST**

---

## Done

Each check's outcome at 447dbce2:

- **Ready preflight:** the `ki-work` audit and the `ki-work-roadmap` adapter audit both passed offline, with no failure or warning.
- **Completeness:** Goal, Boundary, Steps, Verify, Delegation and Documentation impact are complete and checkable, except for the handoff after a completed outcome (change 2).
- **Step order:** Steps run in an order that Dependencies and Verify allow. The browser setup check and any repin come before the matrix, and the gate preparation comes before baseline gates.
- **Outcomes:** go, conditional go, no-go and blocked are each reachable and consistently classified, except for the VM case (change 1). Blocked is fully directed; completed outcomes are not (change 2).
- **Evidence note:** defined as the record's `## Review` packet, with its owner and contents. It lacks the full six-part shape needed at Awaiting review (change 2).
- **Site gates:** runnable offline as written. Every named local tool is present, network verifiers run only with `--network`, no command uses `bunx` or installs anything, and dependency links in the copied trees are relative.
- **Settlement boundary:** no Step settles a Proposed or unapproved decision. Go keeps Lit and the route proposed, and every direction change goes through Queries for approval.
- **GDR-KI-DESIGN-012 amendment:** the scope meets `ki-decision-records` and the record's own Verify. It covers the BODY-11 links, the forward-work line in Consequences, the `date` handling and the title-filename alignment.
- **Guide scope:** meets `ki-guides`. It opens with what the reader can do, is self-contained, names records in prose, and the plan adds the index entry.
- **Repository facts and pins:** all check out except the tsbuildinfo claim (change 3). Checked: Bun 1.4.2, Node 24.22.0, Eleventy 3.1.6, the elements package (lit 3.3.1 and its exports), the site scripts and tsconfig, the uninstalled Lit Labs packages, local commit hooks only, and the registry pin metadata as cited.
- **Browser setup:** the design fits the local Chrome 155 against `playwright-core` 1.64.1 (Chromium 156), with one bounded repin and no download.
- **Disclosure:** while looking up the heading format, I saw the first lines of another reviewer's report. My findings had already been formed and are unaffected.

## In Progress

Nothing.

## Queries

**Context:** Change 2 needs a named actor to clean up after the supervisor's independent review and reproduction, record that result, complete the six-part Review packet, and move the record to Awaiting review.

**Query:** Who should finish a completed run after the supervisor's review?

**Options:**

a) (recommended, confidence high - the worker already owns the evidence note and the fixture grant, so the Review packet keeps one author) The original worker resumes under the same grant, as in the edit above.

b) The supervisor does the cleanup and records it, and a short `ki-implement` run completes the packet and the move.

c) A separately authorised cleanup-and-close run, named in the successor brief.
