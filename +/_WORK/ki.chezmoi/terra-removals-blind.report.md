# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Themes/rig.md) › [chezmoi](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/chezmoi.md) › terra-removals-blind

**🤖 → 👤 Handoff to supervisor · Run report at 12:00 BST · last mark not inspected (blind-review boundary)**

---

## Done

- Completed the independent read-only review on terra; no application, catalogue, roadmap, credential, scheduler or environment configuration changed; no commits or remote calls.
- Read repository guidance, the [application lifecycle](/Users/krisbrown/.local/share/chezmoi/.agents/skills/ki-self/references/application-lifecycle.md:11), the Rig source catalogue and relevant rendered entries, and [KB-DOTFILES-UE-086](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md); excluded work-package and other agents’ reports remained unread.
- Inventory checks: all requested removal candidates are installed, including Mercury Weather, which is present both as `/Applications/Mercury.app` and App Store ID 1621800675; B7 must remain unticked.
- Usage checks: Spotlight last-used dates and use counts are unavailable for every candidate; absence of a running process does not establish historical non-use.
- Process and startup checks: no candidate foreground app, Spark daemon, BlueStacks emulator or Wrangler process was found; Adobe Finder extensions are running, and its Content Manager background record reports last use at 10:48 BST today, which is background activity rather than proof of creative-app use.
- Startup checks: BlueStacks has a loaded but idle system cleanup watcher; Adobe has loaded but idle installer, CCXProcess and CCLibrary jobs plus active Finder extensions; no matching startup registration was found for the App Store candidates or Shadowlab Spark, although Spark contains an embedded login helper.
- Homebrew dependency check: `brew uses --installed cloudflare-wrangler` returned no dependents; Homebrew Wrangler 4.148.0 is redundant with the declared npm Wrangler 4.151.3, whose mise-managed executable wins the current command path.
- Report check: owner-report structure verified; Markdown lint passes with the repository configuration (the initial unconfigured check used incompatible defaults).
- Final read-only checks: repository clean, no Git lock files, and the assigned temporary directory empty; implementation tests and Rig health gates were not run because this review changes nothing and makes no machine-health claim.

### Item recommendations

- **Shadowlab Spark launcher — medium confidence: remove in the attended pass after preserving any launcher settings.** Identity is `com.xenonium.Spark` 3.3.2, distinct from retained Spark Desktop. Source and rendered catalogues select only Spark Desktop; no explicit launcher retirement entry was found, so the brief’s retirement date was not independently corroborated. No launcher process, active daemon or matching startup record was found. The bundle contains `Spark Daemon.app` and a “Stop Spark Daemon” action. Stop/disable that helper first if enabled, quit Spark, then remove its `spark-app` Homebrew cask without a data-wiping option; keep `readdle-spark` and Spark Desktop. The installed cask recipe is only an empty JSON object, so an uninstall that cannot resolve its recipe must stop for a supported receipt-aware method. No Spark library/preferences were found in the inspected standard locations; that is not proof none exist. Do not erase unknown launcher data or licence material.
- **Clockology, B6a — medium confidence: remove attended; the decision is recorded and no current use was observed.** App Store ID 1456386228 is installed, with no matching running/startup item; its inspected container is small and Documents empty. Use the roadmap’s `sudo mas uninstall` method for that ID, preserving its container and any external watch-face files. Historical last use, watch synchronisation and purchase/reactivation status were not established.
- **Prime Video, B6a — high confidence to hold until the media decision: substantial local content exists.** App Store ID 545519333 is installed, with no matching running/startup item. Its container occupies about 17 GiB and includes roughly 18.4 GB of media fragments; do not describe it as unused or disposable. Kris must confirm offline content is expendable or preserve the container first, with no promise that copied DRM downloads remain playable. Then use the roadmap’s attended `sudo mas uninstall` method, without container cleanup. This review did not inspect titles or account credentials.
- **Nitro, B6a — medium confidence: remove attended while preserving photo work.** App Store ID 1591292532 is installed, with no matching running/startup item; its inspected container is small and Documents empty. Use the roadmap’s `sudo mas uninstall` method for that ID; retain its container, photo libraries and external edits/exports. Empty Documents does not rule out edits in Photos or other storage, and licence/reactivation state was not verified.
- **BlueStacks and its multi-instance manager, B6b — high confidence to hold until an explicit backup/discard decision: the supported removal deletes a real instance.** The shared data tree occupies 3.3 GiB and includes `Engine/Tiramisu64/data.qcow2`, last modified 15 September 2026; no emulator process is running. The bundled [uninstaller](/Applications/BlueStacks.app/Contents/Resources/uninstaller.sh:91) removes both apps and their shared instance data, and also deletes shared NowGG sign-in credentials when BlueAI is absent. Its loaded cleanup daemon watches both app bundles, so moving both to the Bin is also capable of triggering destructive cleanup. Keep both apps in place until Kris backs up the entire shared data tree or expressly discards its instances and account state. Then use BlueStacks’ own Uninstall menu, which invokes the installed uninstaller with administrator approval; verify removal of both apps, watcher and helper. Do not experiment with its cleanup executable or use a blanket manual deletion.
- **Homebrew cloudflare-wrangler, B6d — high confidence: ready for removal during the attended pass because no installed formula depends on it and the selected npm executable is present.** Last historical CLI use is unknown, but it is not the current default and no running process was found. Recheck dependents immediately before the native Homebrew uninstall; preserve npm Wrangler, repository configuration, local Wrangler state and credentials. Leave `node` and its dependencies untouched and do not run autoremove. Technical readiness does not override the roadmap’s attendance requirement.
- **Adobe Creative Cloud, terra part of C7i — medium confidence: use the installed vendor uninstaller after an attended account/data check.** No Photoshop or Lightroom installation was found in the inspected Applications trees, but Creative Cloud, Core Sync and related components remain, with active Finder integrations. The installed uninstaller is [Creative Cloud Uninstaller.app](</Applications/Utilities/Adobe Creative Cloud/Utils/Creative Cloud Uninstaller.app>), also linked from `/Applications/Adobe Creative Cloud/Uninstall Adobe Creative Cloud`. Kris must first check the Creative Cloud screen for installed products, signed-in identity and pending sync/library work; sign-in and subscription/licence status cannot be safely inferred from background services and were not read from credential stores. Remove creative apps first if unexpectedly present, Creative Cloud last, through that uninstaller. Retain user assets and avoid a broad Adobe cleaner. The historical at-screen run report linked by C7i was not fetched under the no-network and blind-review restrictions; stop if vendor prompts or dependencies are unclear.
- **Mercury Weather, B7 — high confidence: it still needs an attended uninstall, not a completion tick.** App Store ID 1621800675 and bundle `com.tripleglazedstudios.Weather` 3.7.2 are installed; no matching running/startup item was found and last use is unknown. Follow B7’s native App Store removal, preserving preferences; tick only after both `mas list` and the application path confirm absence. App removal is not subscription cancellation.

## In Progress

Nothing is running. No removals or completion ticks were attempted.

Outstanding — no action requested now: the supervisor must merge this blind review with its own current work state; the mark, exact thread label and whole-project counts were deliberately not read from the excluded work package. The banner below covers this review’s one decision only.

For an approved attended pass, first read every `rig doctor` finding and inspect unmanaged inventory and the targeted Rig diff; do not apply unrelated pending configuration. Obtain explicit permission to run these removals ahead of the excluded B1–B5 sequence, because [the current plan requires order and attendance](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md:152). Preserve the data identified above, perform native removals one at a time, and verify application paths, App Store/Homebrew inventory, processes and startup jobs afterward. Run lifecycle Rig checks and the catalogue suite, explaining every remaining finding. Tick only completed individual steps; C7i remains open until both Macs are complete. Any source reconciliation and roadmap commit needs the repository’s full local gate. This is a recommendation, not implementation authority.

## Queries

### TERRA-REMOVALS — [When to perform the remaining removals](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/KB-DOTFILES-UE-086-finish-software-alignment.md)

**Context:** Removal decisions already exist, so a separate full software-alignment session is not technically needed. However, the recorded plan requires Kris for every uninstall, including Homebrew Wrangler, and orders B after the excluded toolchain switch. Mercury is still installed. BlueStacks has a live instance disk whose automatic cleanup deletes it, Prime Video has substantial local media, and Adobe’s sign-in/sync state needs an at-screen check. These conditions prevent an unconditional “remove everything now” recommendation.

**Query:** Should Kris approve one bounded attended removal pass now, explicitly allowing it before B1–B5 and settling preservation of BlueStacks instances and Prime Video downloads before their removal?

**Options:**

a) (recommended, confidence medium - existing decisions can be completed together, but local data and account checks must precede destructive steps) Run one attended ki-self pass now; remove each item only after its stated precondition is met, keep BlueStacks and Prime Video installed until their data decision is explicit, and hold Adobe if its account/sync check cannot be completed. Correct B7 only after a real removal. Leave node and the Python/uv switch outside the pass.

b) Leave all removals for a dedicated attended KB-DOTFILES-UE-086 session; retain the same data safeguards and keep B7 open meanwhile.

c) Explicitly amend the plan to permit an unattended Wrangler-only uninstall now and defer the attended apps. There is no B7 tick available now, and this split presently offers less benefit than one attended pass.

### 🤖 → 👤 Handoff to supervisor · since 12:00 BST

👤 1 with you · 🤖 0 running

- [with you] TERRA-REMOVALS · owner · since 12:00 BST

🧵 Coordination thread · chezmoi (ki.chezmoi)
