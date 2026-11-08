# KI > Techne > Agora › rename-apps

**🤖 → 👤 Handoff to supervisor · Run report at 21:47 GMT · last mark 00:04 GMT**

---

## New and noteworthy

The apps now carry their new names throughout apps-agora.local. The menu-bar app is **Agora Beacon** (`Agora Beacon.app`). The desktop viewer is **Agora Atlas** (`Agora Atlas.app`). The iPhone app now shows as **Agora Lantern**. The tray reads Open Atlas…, Settings…, Check for Updates…, Quit Atlas and Quit Agora Completely.

The next `bun run self:install` on each Mac installs the two renamed apps. It then retires `Agora Portal.app` and the old `Agora.app`, each by its program path: it removes the bundle, unloads the old launch agent `info.knowledgeislands.agora`, removes that agent's plist and deletes the old apps' login items, printing one line for each app. Nothing was installed, packaged or relaunched in this run.

The bundle identifiers changed too, as the task asked. The Beacon is now `info.knowledgeislands.agora.beacon` and the Atlas `info.knowledgeislands.agora.atlas`, so the Beacon also gets a new launch agent. macOS may ask once more to approve it under Login Items. The config path, the state paths, the `call/` paths and the door socket did not change.

## Done

- `969b721` feat(apps): the code rename. This covers the product names, bundle names and identifiers in both electron-builder configs, the launch agent, the window title, the tray menu, tooltips and log lines, and the iPhone display name. The installer now retires the old apps through `retireOld` in `src/install.ts`, which is pure and tested. Check passed; 493 tests passed.
- `564688f` docs: the new names in the README, `AGENTS.md`, `docs/spec/`, `docs/design/` (architecture diagrams included), the example configuration and the changelog. Moved heading anchors were fixed. Check and tests passed; pushed.
- Check for Updates still works across the rename. It compares the installed build with `origin/main` in the source checkout, and the one install command it offers is the installer that does the rename.

## In Progress

Nothing. Left alone on purpose:

- The dated walkthrough (`docs/walkthrough/`) and the roadmap records still say Portal, because they are records of that time.
- The iPhone Xcode project and target are still named `AgoraBeacon`, and its bundle id is still `uk.me.kris.agora-beacon`, so the copy on the phone updates rather than installs a second app. Only the display name changed.
- In chezmoi, only household work records mention the old names. No configuration there needs changing.

## Queries

**Q1 - The word "beacon" on the Atlas's map**

**Context:** The Atlas's map already uses "beacon" in its own sense: the lit island portal on a summit when an island is taking part. Its key says "A lit beacon on a tile's summit", and the CSS has a `.beacon` class. That is now close to the Beacon app's name.

**Query:** Should the map's lit island portal get a different word?

**Options:**

a) (recommended, confidence medium - the two senses sit side by side on one screen, and the map's sense is the less settled one) Call it "the lit portal" or "the summit light" in the key and code, so "Beacon" names only the app.

b) Keep both: lowercase "beacon" for the summit light and capital "Beacon" for the app.

**Q2 - The login items the installer cannot see**

**Context:** The installer removes old login items through System Events, which may ask once for permission. Items the old apps registered through macOS's newer login-item service are not visible to it. Once the old bundle is deleted those items start nothing, but they can stay listed in System Settings > General > Login Items.

**Query:** Is a stale, inert listing there acceptable?

**Options:**

a) (recommended, confidence medium - the bundle is gone, so the listing does nothing) Accept it and remove it by hand if it shows.

b) Have the installer reset those registrations, which resets every app's login items and is too broad.

🧵 ki.prj.agora
