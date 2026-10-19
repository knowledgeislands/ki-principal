# ki.ways-of-working queries

## Open

### MGIT-RELEASE - When other machines get the -f change

since 2026-10-19 · from mgit-filter.report.md in the run state folder

**Context:** `main` now carries breaking changes since v0.17.0 (`-B/--bypass`, `learn` and dropping `-f`), but only this Mac runs the checkout; Terra and Sol keep v0.17.0, where `-f` still works.

**Query:** Should mgit be released now so every machine has the same flags, or wait until Kris finishes the hands-on check in KI-TOOL-MGIT-CLI-023?

**Options:**

a) (recommended, confidence medium - one release carries the hands-on fixes and avoids a second breaking bump) Wait for the KI-TOOL-MGIT-CLI-023 hands-on check, then release once under [Release mgit](/Users/krisbrown/workspaces/knowledge-islands/tools-mgit/docs/guides/developer/releasing.md).

b) Release v0.18.0 now from `main`, so the machines agree today.

### PUSH-ALL - Push the stacks that hold other sessions' commits

since 2026-10-19 15:17 BST · from migrate-pass, work-package-standard, no-alias-sweep and territories-package

**Context:** ki-principal is 34 commits ahead (six from ki.specifications, ki.knowledge-acquisition and ki.chezmoi); ki-agentic-harness 8 ahead (including the acquire consolidation, `8bc9d49d` and `88cce3e5`); personal/acquire 4 ahead (`cd439cd` and `c8af3d4` from another session). Until pushed, other machines do not see the migrated packages or the harness rename.

**Query:** May the coordinator push all three stacks fast-forward now?

**Options:**

a) (recommended, confidence medium - all are routine work-folder, roadmap or documentation commits from sessions Kris opened today, not reviewed line by line) Push all three now, pull with rebase first.

b) Kris looks over the other sessions' commits first, then pushes.

### DEPLOY-PUSH - Site repositories whose push deploys

since 2026-10-19 · from fields-rest

**Context:** 5g-emerge-phase2, 5g-emerge-demos and apps-tower.midnight.ninja each hold one field-migration commit (front matter only) unpushed, because a push to `main` deploys the site; another session's commit sits in each too.

**Query:** Push them, accepting a redeploy?

**Options:**

a) (recommended, confidence medium - front matter only, but a live deploy follows) Push all three; the sites redeploy with no visible change.

b) Leave them for the next deliberate site release.

### CITATIONS-DANGLE - Old-path citations outside the work areas

since 2026-10-19 · from territories-package

**Context:** Tracked notes still cite `+/_CHECKPOINTS/` or `+/_THREADS/` paths that no longer exist: hnr-principal 48, acquire 8, personal-principal 5, legal 4, tmx 2, er 1, va 1. Git keeps the targets.

**Query:** Rewrite them now or leave them to each territory?

**Options:**

a) (recommended, confidence medium - mechanical, but canonical notes fall under each island's Enactment Process) A line in each territory's `messages.md` naming the count and the rewrite, done at resume.

b) One mechanical rewrite run across the seven repositories now.

### CHEZMOI-MIGRATE - ki.chezmoi's folder is still single-file

since 2026-10-19 · from migrate-pass

**Context:** ki.chezmoi's `work.md` holds uncommitted changes from its run sol-locals-complete, so the pass skipped it.

**Query:** How does it reach the package shape?

**Options:**

a) (recommended, confidence high - keeps its coordinator's authority over its own folder) Once its coordinator commits that receive, a one-folder migrate run from this work.

b) Its coordinator migrates its own folder at that receive.

### MARK-READOPT - VA-MARK records left in triage

since 2026-10-19 · from fields-pilot-markhowarth

**Context:** The field pilot moved apps-markhowarth.com's records off the retired triage horizon to `status: triage`, which drops their adoption.

**Query:** Re-adopt them now or leave them in triage?

**Options:**

a) (recommended, confidence medium - adoption is cheap when work is picked up) Leave them in triage and adopt each when picked up.

b) Re-adopt them now with a kind and size each.

## Parked

### DESK-CAM - Which webcam to buy for sol

since 2026-10-15 · from [webcam-compare](webcam-compare.report.md) · parked: listed as outstanding and not this work's; release: Kris's purchase decision

**Context:** Kris wants one webcam with good built-in microphones for calls first and dictation second, using sol's own speaker. The best fit is the Insta360 Link 2C Pro at £199.00 (B0G3SSQMJQ): 1/1.3-inch sensor, two beamforming mics with a Focus mode, built-in shutter, plain UVC/UAC, and an optional app available as a Homebrew cask. The cheaper alternative with the strongest mic hardware is the OBSBOT Tiny 3 Lite at £169.00 (B0G63LXK6R). The UGREEN FineCam Pro at £57.78 (B0FX5QMB6K) is the budget option, with little audio evidence. All prices were seen on the product pages on 15 Oct 2026. Buying is Kris's decision.

**Query:** Which webcam does Kris want for sol?

**Options:**

a) (recommended) Insta360 Link 2C Pro, £199.00, amazon.co.uk/dp/B0G3SSQMJQ; add the `insta360-link-controller` Homebrew cask to sol's Rig configuration once it arrives

b) OBSBOT Tiny 3 Lite, £169.00, amazon.co.uk/dp/B0G63LXK6R; OBSBOT Center installed by hand

c) OBSBOT Tiny 3, £296.00, amazon.co.uk/dp/B0G636CXQM, for the best-reviewed webcam mics and the largest sensor

d) UGREEN FineCam Pro, £57.78, amazon.co.uk/dp/B0FX5QMB6K, the budget option with no app

- Parked 2026-10-09: a gradual move from Obsidian-style to GitHub-flavoured Markdown, starting with a front-matter field declaring a note's flavour.
