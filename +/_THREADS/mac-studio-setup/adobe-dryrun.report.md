# [Rig](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Initiatives/rig.md) › [Mac Studio bootstrap](/Users/krisbrown/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup/mac-studio-setup.md) › adobe-dryrun

**Run report at 23:50 BST · last mark 21:32 BST**

---

## Done

- **The dry run is safe to turn into the real run.** Every path the real run would remove or change belongs to Adobe. Nothing in it touches your documents, photos, fonts, licences, another vendor's files, shared frameworks or macOS system paths. The run on sol at 23:46 exited cleanly, with no errors and nothing skipped, and it found the same things as the 15 October dry runs.
- **What the real run would remove**, all of it Adobe's:
  - Lightroom Classic 15.6 and Photoshop 2023, 2024, 2025 and 2026, through Adobe's own HDBox uninstaller with your preferences kept. Then the 8 add-ons those apps pulled in (Camera Raw, colour profiles, CAI, the Substance viewer), and then Creative Cloud through its own uninstaller.
  - After that, whatever Adobe's tools leave behind: 2 launch daemons, 4 system launch agents, 2 of your own launch agents and the installer helper, each one unloaded first. Then the 7 Creative Cloud folders and the 5 app folders in `/Applications`.
- **Checked on sol, read-only:**
  - The app folders hold only Adobe's own files. All of them belong to root and were installed on the same day as the app. Nothing in them is yours, and there are no third-party Photoshop plug-ins.
  - There is no `~/Creative Cloud Files` folder, so no synced files can be lost.
  - No Adobe Fonts are activated. The fonts folder holds only a transfer database.
  - Each launchd label the script would unload matches the label inside its plist. Your `com.adobe.ccxprocess` agent points at an Adobe folder that no longer exists. It is stale but still Adobe's, and removing it is correct.
- **Kept for ADOBE-DATA, untouched:**
  - `/Library/Application Support/Adobe` (7.0 GB) and `~/Library/Application Support/Adobe` (6.2 GB).
  - The Camera Raw cache (19 GB) and the other caches.
  - Your Photoshop and Lightroom preferences.
  - The catalogue `~/Pictures/Lightroom/Lightroom Catalog.lrcat`.
- **Sudo:** the dry run needed none. The real run needs it for every change, because everything it removes sits in `/Applications`, `/Library` or the system launchd domain. The script refuses `--apply` without sudo.
- **Secrets:** the log holds no licence key, serial, token or password. It does hold sol's hardware UUID in some file names, which is not a secret.
- **One script bug, fixed and committed as `5ffea19`** (local only, not pushed). The final "What is left" check read the whole `launchctl print` output. That output includes launchd's list of disabled services, and launchd keeps entries in that list after a plist is gone. So even a clean removal would still have shown `loaded (system): com.adobe.AdobeDesktopService` and several `loaded (user)` lines. The check now reads only the services that are actually loaded. It also now spots the Genuine Software Integrity daemon, whose label is `Adobe_Genuine_Software_Integrity_Service` and was missed before.
- **Checks on the fix:** shellcheck passes. A dry run of a copy in a temporary folder exited 0, changed nothing, and gave the same output as your 23:46 log apart from the corrected loaded lines. That copy and its log are in `$TMPDIR` (`tmp.y8IaianIVH`), which macOS clears by itself, and I did not delete them.
- **The log:** I did not commit it. Git already ignores it through the `*.log` rule at `.gitignore` line 15, so the folder needs no new `.gitignore` line. Keep it until the real run has been reviewed (ADOBE-LOG).

## In Progress

Nothing is running from this run. The real removal is for you to run at sol's screen.

Outstanding - no action requested now:

- ADOBE-DATA from the adobe-sweep report stays open until the real run has reported what is left.
- ADOBE-SCRIPT-TERRA and ADOBE-RUN-TERRA from the adobe-script report are unchanged. `5ffea19` will reach terra with the same push.
- `+/_THREADS/chezmoi/decisions.md` has uncommitted changes from another session. I did not touch it.

## Queries

### ADOBE-RUN - Run the real removal at sol

**Context:** The dry run checks out, and the script now has the fix to its leftover check, so a fresh dry run comes first. In step 5 of the real run, a line reading `exit 3` (or a similar number) after a `launchctl bootout` line is expected. `com.adobe.ccxprocess` and `com.adobe.GC.Scheduler-1.0` are each listed twice, so the second unload finds nothing to unload. An `exit` line after an HDBox `Setup` or the `Creative Cloud Uninstaller` line is not expected.

**Query:** Will you run the removal at sol's screen with the steps below?

**Options:**

a) (recommended) yes. At sol:

1. Save your work, then quit Lightroom Classic and every Photoshop.
2. Open Terminal and type `cd ~/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup`
3. Type `./adobe-remove.sh`. This is a dry run. Check that no `Still open` section appears and that the last line reads `Dry run finished. Nothing was changed.`
4. Type `sudo ./adobe-remove.sh --apply` and give sol's password. It takes a few minutes. If a line says `Operation not permitted`, turn Terminal on in System Settings › Privacy & Security › App Management and type the same command again.
5. Check the end of the output. Under `What is left`, there should be no `/Applications/Adobe` line, no plist, no helper, no `loaded` line and no process, and the last line should read `Done with 0 step(s) that failed or fell back`.
6. Restart sol, open Terminal, and type `cd ~/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup && ./adobe-remove.sh`. Check that it lists `none` for apps and add-ons, no Creative Cloud folder, and nothing under `What is left` before the folder sizes.
7. Check that your data is there: type `ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat`. Only the `Lightroom Catalog.lrcat` line should appear.
8. Tell the thread "sol done". An agent will then read the `*.apply.log` and the newest `*.dry-run.log` beside the script.

b) run only steps 1 to 3 (the fresh dry run) and send its output before deciding

### ADOBE-LOG - What to do with the dry-run logs

**Context:** Git already ignores `adobe-remove.sol.20261017-234633.dry-run.log`, so it cannot be committed by mistake. It is the record of what sol had before the removal, and it is useful when the real run is compared against it.

**Query:** What should happen to the dry-run and apply logs beside the script?

**Options:**

a) (recommended) keep them where they are until the real run is reviewed. Then an agent moves them to `~/.local/state/ki/agents/mac-studio-setup/archive/`, as it did with the 15 October logs.

b) delete the dry-run log now

```text
ADOBE-RUN

a) At sol: quit Lightroom Classic and every Photoshop; cd ~/workspaces/knowledge-islands/ki-principal/Streams/Projects/mac-studio-setup; ./adobe-remove.sh (expect no "Still open" and "Dry run finished. Nothing was changed."); sudo ./adobe-remove.sh --apply (if "Operation not permitted", turn Terminal on under App Management and rerun; "exit N" after a launchctl bootout line is fine); expect nothing under "What is left" (no app, plist, helper, loaded line or process) and "Done with 0 step(s) that failed or fell back"; restart, rerun ./adobe-remove.sh and expect "none" and nothing left before the sizes; ls -d /Applications/Adobe* /Applications/Utilities/Adobe* ~/Pictures/Lightroom/*.lrcat shows only the catalogue; tell the thread "sol done" so an agent reads the apply log and newest dry-run log; delete no data (ADOBE-DATA stays open)

---

ADOBE-LOG

a) Keep the dry-run and apply logs beside the script until the real run is reviewed, then an agent moves them to ~/.local/state/ki/agents/mac-studio-setup/archive/
```

```text
╭─ run report · 2026-10-17T22:50:00Z ──────────────╮
│                                                  │
│  █▀▀▄ █▀▀▀ █▀▀▀ ▀▀█▀   · run done                │
│  █▀▀▄ █▀▀  ▀▀▀█   █    · 5ffea19 local           │
│  █  █ █▄▄▄ ▄▄▄█   █    · 2 queries               │
│                                                  │
╰──────────────────────────────────────────────────╯
```

- [at rest] adobe-dryrun finished; nothing running from this run
- [waiting] ADOBE-RUN
- [waiting] ADOBE-LOG
- [unpushed] ki-principal `main` on sol has `5ffea19` and this report's commit

```text
Resume Rig: mac-studio-bootstrap under current ki-pmo and ki-delegation since 2026-10-14T16:47Z: re-bootstrap, mark, fresh summary with carried-forward open points, take stock, restart authorised work, then banner.
```
