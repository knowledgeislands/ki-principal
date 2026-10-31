# Orca preferences declaration and checker (ORCA-PREFS)

Written by run `w-U13` on Saturday 31 October 2026, during the unattended window AWAY-31-OCT, for unit U13 of [the window plan](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.ways-of-working/design/window-31-oct/plan.md). Design only: nothing is built, rendered or applied, and nothing writes to Orca.

## The ask

ORCA-PREFS, sent here by personal.reg.rig-terra on 31 October at Kris's request (line 18 of this package's [messages](../messages.md)), carries Kris's ORCA-CONFIG-SCOPE answer, a) amended, logged in [personal.reg.rig-terra's decisions](/Users/krisbrown/workspaces/personal/personal-principal/+/_WORK/personal.reg.rig-terra/decisions.md) at 01:20 GMT:

> not write to that database, but if we can read from it ... reconcile it by reading on both and looking for differences and then flagging that up. It's actually completely okay for each host to have its own Orca config ... some variations between that, we want to keep and some that we want to make sure are consistent ... we still put it in the dot files somewhere.

Two things are wanted: a dotfiles declaration of Orca preferences split into shared and per-host values, and a read-only checker that flags differences on terra and sol.

## Inputs

- The terra survey, personal-principal `+/_WORK/personal.reg.rig-terra/orca-config.report.md` at `c71ac2b1` (finding ORCA-CONFIG), Orca 1.4.245. It found the settings in a live SQLite profile database mixed with machine state and credential-related fields, no supported settings export or settings CLI, and recommended a small reviewed allowlist with the database left unmanaged.
- A read-only, copy-free inspection of sol's profile on 31 October at about 03:20 GMT, Orca 1.4.244. It opened `~/Library/Application Support/orca/profiles/local-default/profile-state.db` through SQLite's `immutable=1` read-only URI, which takes no locks and never touches the `-wal` or `-shm` sidecars, and read only table definitions, document names and revisions, and the top-level key names and JSON types of the `settings` and `ui` documents. No value was read, nothing was copied, and terra was not contacted.
- [PERSONAL-DOTFILES-UE-107](/Users/krisbrown/.local/share/chezmoi/docs/roadmap/PERSONAL-DOTFILES-UE-107-decide-orca-adoption.md), Decide Orca adoption, still a draft, which holds the open permission, trust and per-pane questions.
- ORCA-SETTINGS-READ in [ki.prj.orca-evaluation's messages](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/+/_WORK/ki.prj.orca-evaluation/messages.md), which asks Orca for a supported read-only settings export.
- The chezmoi [runtime-mutated configuration guide](/Users/krisbrown/.local/share/chezmoi/docs/guides/agents/config-patterns.md), which keys per-machine data by `rigProfile` (`laptop` is terra, `studio` is sol) rather than hostname, and [`.chezmoidata/codexbar.yaml`](/Users/krisbrown/.local/share/chezmoi/.chezmoidata/codexbar.yaml), an existing preference declaration for an app-owned file.
- RIG-OWNS-CONFIG (line 9 of this package's messages): Rig declares application configuration intent, and dotfiles are one way of delivering it.

## What sol's profile shows

The database has four tables. `profile_state_documents` holds one JSON document per domain (`domain`, `payload`, `domain_version`, `revision`, `updated_at`, `content_hash`); the others hold profile metadata and automation runs. Sol has 35 domains. Only two carry preferences:

| Domain | Top-level keys | What it mixes |
| --- | ---: | --- |
| `settings` | 230 (terra: 235) | Preferences, account and pairing state, environment values, provider cookies and keys, migration flags |
| `ui` | 110 | Status-bar and sidebar preferences with live window, pane, tour and repository state |

The other 33 domains (`projects`, `repos`, `workspaceSession`, `sshTargets`, `worktreeMeta` and so on) are machine state and stay out of scope entirely.

The two Macs run different builds (1.4.244 and 1.4.245), and the key counts differ by five. The checker therefore has to treat a missing key as "absent on this build", not as a difference.

Freshness matters for the read path. On sol the main database file was last written at 16:06 GMT on 30 October, while its write-ahead log was current to 03:08 GMT on 31 October. A read that ignores the log sees the settings as they were at Orca's last checkpoint, which can be many hours old while Orca is running.

## Recommendations

### R1 - Declare in `.chezmoidata/orca.yaml`, rendering nothing into Orca

**Recommended, confidence high** - it follows the existing CodexBar declaration and keeps Kris's rule that nothing writes Orca's database.

The declaration is data only. No chezmoi target writes to Orca's profile, and the survey's Pattern A writer stays deferred until Orca offers a supported patch interface. The only consumer is the checker.

### R2 - Key per-host values by Rig profile, not hostname

**Recommended, confidence high** - the repository already does this for the Rig profile and the territory seats, because macOS renames hosts.

`hosts.laptop` is terra and `hosts.studio` is sol. A future third Mac gets its profile's entry.

### R3 - Four classes, and everything undeclared stays unread

**Recommended, confidence high for the structure** - it gives Kris's "some variations ... we want to keep and some that we want to make sure are consistent" a place each, and keeps secret-bearing fields out by construction. The values themselves are Kris's.

| Class | Meaning | What the checker reports |
| --- | --- | --- |
| `shared` | One value every host must hold | DRIFT when a host's value differs from it |
| `hosts.<profile>` | A value each host is expected to hold, which may differ between hosts | DRIFT when a host differs from its own declared value |
| `watched` | Read and shown, never judged | The value, for comparison and classification |
| `never` | Paths the checker must not read | Nothing; declaring one in another class fails validation |

The checker reads only paths named in `shared`, `hosts` and `watched`. Any key in no class is unmanaged and is not read at all. The `never` list is a guard on the declaration, so a later edit cannot quietly start reading a cookie.

Paths are leaf paths into one document, such as `settings.terminalFontSize`, `settings.notifications.<leaf>` or `ui.statusBarItems`, with arrays compared whole. **Confidence medium** on leaf granularity for nested objects such as `notifications`, `telemetry` and `voice`: their inner keys were not read on sol, so the builder confirms the leaves from Orca's code before declaring them.

### R4 - Start every candidate in `watched`, then let Kris promote

**Recommended, confidence high** - the survey warns that a value's presence "does not establish that Kris deliberately selected every value", and this classifies without guessing.

The first build declares the candidates below as `watched` and nothing as `shared` or per-host. One attended run on each Mac prints the watched values side by side with the declaration. Kris then promotes each to `shared`, to `hosts`, or drops it. That run is the "reading on both and looking for differences" step, done once for classification and then continuously for drift.

Candidates, drawn from the survey's allowlist and sol's key names:

- **Likely shared:** `theme`, `appFontFamily`, `editorFontFamily`, `terminalFontFamily`, `terminalFontSize`, `terminalFontWeight`, `terminalFontWeightBold`, `terminalLineHeight`, `terminalLigatures`, `terminalThemeDark`, `terminalThemeLight`, `terminalUseSeparateLightTheme`, `terminalCursorStyle`, `terminalCursorBlink`, `terminalScrollbackRows`, `terminalMacOptionAsAlt`, `terminalShortcutPolicy`, `terminalColorOverrides`, `terminalCustomThemes`, `uiLanguage`, `leftSidebarAppearanceMode`, `editorWordWrap`, `editorMinimapEnabled`, `editorAutoSave`, `diffDefaultView`, `diffWordWrap`, `diffShowWhitespace`, `agentStatusHooksEnabled`, `defaultTuiAgent`, `disabledTuiAgents`, `claudeAgentTeamsMode`, `branchPrefix`, `branchPrefixCustom`, `autoRenameBranchFromWork`, `skipDeleteWorktreeConfirm`, `confirmClosePinnedTab`, `nestWorkspaces`, `nestedWorkerMaxDepth`, `orchestrationHeartbeatsEnabled`, `orchestrationHeartbeatIntervalMinutes`, the `experimental*` choice flags, `notifications`, and from `ui`: `statusBarVisible`, `statusBarItems`, `statusBarUsageMode`, `usagePercentageDisplay`, `groupBy`, `sortBy`, `agentsGroupBy`.
- **Likely per host:** `workspaceDir`, `keepComputerAwakeWhileAgentsRun` (sol is the always-on hub seat), `minimizeToTrayOnClose`, `showMenuBarIcon`, `terminalGpuAcceleration`, `terminalDefaultShell`, `openInApplications` (the Rig profiles install different apps), `agentHibernationIdleMs`, `experimentalAgentHibernation`, `experimentalMobile`, `showMobileButton`, `mobileEmulatorEnabled`, and from `ui`: `uiZoomLevel`, `editorFontZoomLevel`.
- **Watched until PERSONAL-DOTFILES-UE-107 settles them, then promoted or left watched:** `agentPermissionDefault`, `agentPermissionOverrides`, `agentWorkspaceTrustEnabled`, `nativeChatPermissionMode`, `telemetry`, `agentSkillSharingEnabled`, `artifactSharingEnabled`, `browserClientHostedRemoteEnabled`.

`disabledTuiAgents` is where the survey's retired-Hermes change would land; watching it shows whether that separately reviewed change has been made on each Mac.

### R5 - A `never` list from sol's key names

**Recommended, confidence high** - every entry is account, credential, pairing, environment, path-history or live-state material.

- **`settings`:** `activeClaudeManagedAccountId`, `activeCodexManagedAccountId`, `activeCodexManagedAccountIdsByRuntime`, `claudeManagedAccounts`, `codexManagedAccounts`, `activeRuntimeEnvironmentId`, `agentDefaultEnv`, `agentDefaultArgs`, `agentCmdOverrides`, `nativeChatShellEnvironmentVariables`, `httpProxyUrl`, `httpProxyBypassRules`, `opencodeSessionCookie`, `opencodeWorkspaceId`, `minimaxEndpoint`, `minimaxGroupId`, `minimaxUsageModels`, `zcodePlanSite`, `mobilePairingConnectionMode`, `mobilePairingCustomAddress`, `mobilePairingCustomAddresses`, `machineName`, `workspaceDirHistory`, `floatingTerminalTrustedCwds`, `githubProjects`, `pluginConsents`, `devPluginPaths`, `prBotAuthorOverrides`, `defaultLinearTeamSelection`, `defaultRepoSelection`, `androidSdkPath`, `mobileEmulatorDefaultDeviceUdid`.
- **`ui`:** `trustedOrcaHooks`, `windowBounds`, `lastActiveRepoId`, `lastActiveWorktreeId`, every `*ByPaneKey` and `*ByWorktree` key, `filterRepoIds`, `agentsFilterRepoIds`, `manualRepoOrder`, `collapsedGroups`, `taskResumeState`, `featureInteractions`, `contextualToursSeenIds`, `featureTipsSeenIds`, `setupScriptPromptDismissedRepoIds`, `workspaceHostOrder`, `visibleWorkspaceHostIds`, `agentsVisibleHostIds`, `automationHostFilter`, `browserKagiSessionLink`, `lastUpdateCheckAt`.
- **By rule, in both documents:** migration and one-time flags, meaning keys starting `_` or containing `Migrated`, `Defaulted`, `DefaultAdded`, `NoticeSeen`, `NoticeDismissed`, `Dismissed` or `starNag`.

Every other document domain is out of scope as a whole.

### R6 - Compare each host with the declaration, not host with host

**Recommended, confidence high** - no host reads the other, so it needs no SSH, no new channel and no copy of one Mac's values on the other, and a terra-against-sol difference on any declared path still shows, because both are measured against the same Git-held declaration.

A direct pairing, such as a later `--peer <host>` that runs the checker on the other Mac over SSH and merges the two reports, is possible but adds a connection dependency. **Confidence low** that it is needed once R4's classification is done; leave it out of the first build.

### R7 - Read path: a supported interface first, the immutable read until then

**Recommended, confidence medium** - the immutable read cannot write or lock, but it can be hours stale while Orca runs, and it depends on Orca's private schema.

In order of preference:

1. **A supported Orca read or export interface**, once ORCA-SETTINGS-READ yields one. The checker switches to it and drops the database read.
2. **Until then, SQLite's `immutable=1` read-only URI on the main database file**, selecting only declared paths with `json_extract` on the `settings` and `ui` rows: never the whole payload, never another domain, never a copy, never the sidecars. Each report states its "as of", the document's `updated_at` and the main file's modification time, and says when Orca is running that recent changes may not show until it next checkpoints, typically when it quits. An error is retried once and then reported as unreadable, never worked around.

Rejected:

- `mode=ro` without `immutable`: it honours the write-ahead log, but SQLite may open the live `-shm` sidecar for writing and take locks beside the running app.
- `mode=ro&readonly_shm=1`: it reads the log through a read-only sidecar, but rests on SQLite's Unix internals and can refuse to open while Orca's sidecar is mid-recovery. **Confidence low** that it is safe enough to rely on unattended.
- Copying the database and its log to a temporary folder: fresh, but it copies the cookie and key fields R5 keeps unread.
- Orca's private `settings:get` channel or other Electron calls: not a versioned contract, as the survey says.

### R8 - One checker script, rendered from the declaration

**Recommended, confidence medium** - it matches the existing `bin/executable_rig-bringup-check.tmpl` pattern and needs no chezmoi call at run time, but the builder should confirm the repository's preferred script language.

- **Where:** `bin/executable_orca-prefs-check.tmpl`, rendering to `~/bin/orca-prefs-check` with the declaration embedded as JSON (`toJson .orca`) and the host's class taken from `.rigProfile`. A declaration edit reaches the checker at the next attended `chezmoi apply`, and `chezmoi diff` shows it until then.
- **Tools:** macOS's `/usr/bin/sqlite3` and its JSON functions, with `jq` only if the comparison needs it.
- **Output:** a header naming the host's profile, Orca's version from `/Applications/Orca.app/Contents/Info.plist`, and the "as of"; then one line per declared path: class, path, declared value, host value and result (`ok`, `DRIFT`, `absent on this build`, or `watched`), followed by a one-line summary. `--json` gives the same for a later Rig doctor check.
- **Exit codes:** 0 when clean, 1 on drift, 2 when Orca or its profile is absent or unreadable, 3 when the declaration is invalid (a `never` path declared elsewhere, or an unknown class).
- **Never:** write, copy, open a sidecar, read an undeclared path, or print a value outside the declared paths.
- **Tests:** in `tests/` beside the existing template tests, against a fixture database the test builds in its temporary folder and never the live profile. They prove the URI carries `immutable=1`, that no query selects a whole payload, that a declared `never` path fails validation, and each exit code.
- **Guide:** a new `docs/guides/tools/orca.md` covering the declaration, the classes, the read path and its staleness, and the attended classification run.

Wiring into `rig doctor`, as RIG-OWNS-CONFIG suggests, is a later step for the Rig side. **Confidence low** on its timing, since it depends on how Rig and chezmoi divide configuration.

## Illustration

The shape only. No value here is decided, and the first build declares candidates under `watched` as R4 says.

```yaml
# Orca preference intent. Data only: nothing writes Orca's profile database.
# Read by ~/bin/orca-prefs-check; see docs/guides/tools/orca.md.
orca:
  shared:
    settings: {}
    ui: {}
  hosts:
    laptop:   # terra
      settings: {}
      ui: {}
    studio:   # sol
      settings: {}
      ui: {}
  watched:
    settings: [theme, appFontFamily, terminalFontFamily, terminalFontSize, agentPermissionDefault]
    ui: [statusBarItems, statusBarUsageMode, usagePercentageDisplay]
  never:
    settings: [opencodeSessionCookie, claudeManagedAccounts, agentDefaultEnv, httpProxyUrl]
    ui: [trustedOrcaHooks, windowBounds]
```

After Kris promotes, an entry such as `terminalFontSize` moves from `watched` into `shared.settings` with its value, or into each `hosts.<profile>.settings` with that host's value.

## Ownership and next steps

- **ki.prj.chezmoi** owns the declaration, the checker, its tests and guide, and the record that builds them. A build waits for Kris to adopt this design; capturing an unadopted record in the chezmoi roadmap adopts nothing.
- **personal.reg.rig-terra and personal.regular.rig-sol** each run the attended classification read and, later, any reviewed apply.
- **ki.prj.orca-evaluation** owns ORCA-SETTINGS-READ. When a supported interface lands, R7 switches to it.
- **PERSONAL-DOTFILES-UE-107** owns the permission, trust and telemetry values until it settles them.
- Nothing here changes Orca, the database, the hooks coexistence binding or the Rig declaration.
