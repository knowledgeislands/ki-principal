# [Model](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/model.md) › [Ways of working](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/ways-of-working.md) › landscape-review-claude

**🤖 → 👤 Handoff to supervisor · Run report at 02:13 GMT · last mark 01:39 GMT**

---

## Done

- Reviewed all 30 numbered claims in [landscape](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/landscape.md) against the `ki agent` and Orca command help, the Techne Programme Focus, the decisions it quotes, checkout-isolation and the installed skills: 21 Agree, 6 Differ (4, 15, 18, 20, 24, 28) and 3 Add (11, 13, 16), with further additions noted against several Agrees. Vendor-documentation claims are unverified here, since the run made no network calls.
- Material corrections: WAKE-SUBSTRATE is not deferred. Kris chose the headless pass as the durable wake on 26 October and lifted the launchd deferral. That pass is a scheduled agent, which the Techne focus forbids on sol and `vega` but not on terra. Separately, worker writes into the package folder need integrate before receive under the worktree baseline.
- Recommendations: ORCA-REACH a) high; AGENT-HOME a) medium, because `ki work` is read-only by its own description; WAKE a) high for the session wake, with the durable wake's placement split off (terra first, medium); WORKTREE-OPTOUT read-only opt-out high, no trivial opt-out once an integrate command exists, medium; naming kept as the note proposes, medium, on cost rather than on the role word.
- Wrote [landscape-review-claude](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/landscape-review-claude.md), committed alone as `29d78639`. Repository audit hook passed and the commit landed with only that path.

## In Progress

Nothing is running.

Outstanding - no action requested now: the explainer was checked only on its naming and wake lines, which carry the same correction as claims 9 and 20.

## Queries

### WAKE-PLACE - Where the decided headless pass may run

**Context:** Under WAKE-SUBSTRATE, Kris chose a launchd-started headless coordinator pass as the durable wake, contract first and then the job sent to Rig and chezmoi. The Techne Programme Focus allows agents on sol and `vega` "only in sessions the binding owner opens, with no unattended or scheduled agents", and changes only through the Enactment Process. Terra is not covered by the focus. The landscape note treats the durable wake as deferred and so does not raise this conflict.

**Query:** Where should the headless pass run first?

**Options:**

a) (recommended, confidence medium - allowed today with no rule change, but a terra-only pass sees only terra's checkouts while most coordination runs on sol) Run it on terra first, under the focus as written, and leave sol until any Enactment change.

b) Amend the Techne focus through the Enactment Process to allow a bounded, shell-triggered pass on sol, then run it there.

c) Hold the pass on every host until Orca's position is settled.

### WORK-WRITES - Where the split-off `ki agent` write commands go

**Context:** The note moves `decide`, `reconcile`, `home` and `prompts` out of `ki agent` and under `ki work`. `ki work --help` describes the group as "read work model", and `decide` and `reconcile` write the decisions log. `home` records which work folder a run belongs to, so it sits on the seam between the run and the package.

**Query:** Should the split widen `ki work` to cover writes, or give the write commands their own group?

**Options:**

a) (recommended, confidence medium - keeps one place for the work model at the cost of a broader description) Widen `ki work` to "read and record the work model", move `decide`, `reconcile` and `prompts` there, and keep `home` with the launcher.

b) Keep `ki work` read-only and add a separate group for the writes.

### 🤖 → 👤 Handoff to supervisor · since 02:13 GMT

👤 2 with you

- [with you] WAKE-PLACE · owner · since 02:13
- [with you] WORK-WRITES · owner · since 02:13
- [committed] landscape-review-claude

🧵 ki.prj.ways-of-working
