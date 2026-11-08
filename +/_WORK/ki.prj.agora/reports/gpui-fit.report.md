# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › gpui-fit

**🤖 → 👤 Handoff to supervisor · Run report at 22:57 GMT · last mark 01:44 GMT**

---

## Done

**Short answer: no. Keep Electron.** GPUI (the Rust framework Zed is built on) is very good at drawing fast windows. But Agora is mostly a menu-bar app, and the things it needs from the operating system are a menu-bar icon with a native menu, notifications, start-at-login and single-instance. As far as I know, GPUI offers none of these. A GPUI Agora would get all of them from other Rust libraries and would use GPUI only for its two small windows, while Agora's 4,900 lines of TypeScript and their 3,000 lines of tests would have to be rewritten in Rust. If Agora's memory use ever matters, a thin native macOS menu-bar shell (a small Swift app) around the existing TypeScript logic is the cheaper move.

No code, record or repository file was changed, and nothing was committed. Agora's needs (the first column below) were checked against its source and README. **The GPUI column was not checked online:** the brief allowed reading web pages, but the run's Rules ban any network call and say the Rules win, so I made no web or GitHub reads. No GPUI source is on this Mac (no Cargo cache or Zed checkout; Zed.app 1.26.2 is installed only as an app). The GPUI and crate facts below therefore come from my own knowledge, which runs to about June 2026, and are marked *recalled*. Query Q1 asks whether to check them.

### What Agora uses today

Electron touches only `src/main.ts` (482 lines). The boundary rules keep every other file free of Electron, so the logic would move to a new shell untouched.

| Capability | Electron today (verified in source) |
| --- | --- |
| Menu-bar item | `Tray` with a template image that follows light and dark mode, title text (count, `↑`) and a tooltip |
| Menu | Native `Menu` from a template, with submenus, rebuilt on every state change |
| No Dock icon | `app.dock.hide()` and `LSUIElement` in Info.plist |
| Single instance | `app.requestSingleInstanceLock()` |
| Notifications | `Notification` (title and body) |
| Start at login and relaunch | `app.setLoginItemSettings` with `agentService` (registers the bundled launch agent through macOS's SMAppService), falling back to a plain login item |
| Windows | One small form window (Broadcast… and Away text entry) built from inline HTML; About panel; `shell.openPath` for the log |
| Packaging | electron-builder: ad-hoc signed `.app` with an `.icns` icon and the launch-agent plist inside the bundle |
| Runtime for the logic | Node inside Electron: `child_process` for `git`, `tailscale`, `ki` and `orca`; `fs.watch` (FSEvents) to follow checkouts; `http` servers for peers on the Tailscale address and for the loopback read endpoint with server-sent events |
| On the roadmap | Settings screen (permissions check, territory tree, assignments view), still open on who owns the settings file; the send side for the KIV Electron app (KIV-SEND, which KIV-ELECTRON waits on) |

Measured now: the installed Agora.app is 252 MB on disk and its 3 processes use 254 MB of memory.

### GPUI against those needs

| Capability | GPUI (*recalled*, unverified) | Workaround in Rust (maturity, *recalled*) |
| --- | --- | --- |
| Menu-bar item | Missing: no public tray or status-item API | `tray-icon` (Tauri team; mature, used by Tauri v2) |
| Native menu on it | Partial: GPUI sets the app's main menu bar, but draws its own context menus | `muda` (Tauri team; mature) |
| No Dock icon | Not exposed; `LSUIElement` in Info.plist works for any app | Info.plist, or set the activation policy through `objc2-app-kit` (mature) |
| Single instance | Missing; Zed builds its own over a local socket | A lock file or socket, or a small crate (easy) |
| Notifications | Missing: in-app notices only | `mac-notification-sys` / `notify-rust` (fair), or `objc2` bindings to UserNotifications (needs a signed bundle) |
| Login item / launch agent | Missing | `smappservice-rs` (small, young) or `objc2` bindings to ServiceManagement |
| Windows | Strong: GPU-drawn, fast | No text box or tree view built in; the third-party `gpui-component` library supplies inputs, trees and tables (active, pre-1.0). Weak screen-reader accessibility is a known gap |
| Packaging and `.icns` | Missing: no bundler | `cargo-bundle` or `cargo-packager` (fair); signing stays `codesign` |
| Logic runtime | Its own async runtime, not Tokio | `std::process`, `notify` (FSEvents; mature), `hyper` / `axum` (mature), with a bridge to Tokio |
| Release status | On crates.io as a 0.x crate, released to follow Zed's needs, breaking changes expected, docs thin outside Zed | — |
| Platforms | macOS (Metal), Linux (X11 and Wayland), Windows | — |

### Weighing the move

- **Fit.** GPUI is made for a window-first editor; Agora is a menu bar first, with a window now and then. Every tray-side need would come from crates outside GPUI. Those are the same crates Tauri ships, so GPUI adds only the window drawing, and Agora's windows are small forms.
- **Rewrite cost.** Moving the logic to Rust means rewriting about 4,900 lines (presence, protocol, sync, watch, wake, review, view and the rest) and about 3,000 lines of Vitest tests, rebuilding the dependency-cruiser boundaries as Cargo crate boundaries, and splitting Agora from the TypeScript and Bun toolchain the rest of the estate uses. The only way to keep the logic in TypeScript under GPUI is to run it as a second process, which then makes GPUI a costly way to draw two forms.
- **Footprint.** This is the one real gain. A Rust or Swift menu-bar app usually takes tens of MB of memory and disk, against Electron's 250 MB (an estimate, not measured here). It matters only if a rig is short of memory.
- **Stability.** GPUI follows Zed's needs and has no stable promise for outside users. Electron 45 is stable, and the KIV app is Electron too, so the two share a toolchain.
- **Better-fitting alternatives:**
  - **Keep Electron.** Everything works today, and the shell is already confined to one file.
  - **Native Swift menu-bar shell.** Use `NSStatusItem`, `NSMenu`, UserNotifications and SMAppService, all first-party, with the TypeScript logic compiled to one binary by `bun build --compile` and run as a child process. This is the smallest and most native result, but macOS only. Agora already serves its state on loopback, so the shell could read it there. It would still need a control channel for Sync now, Broadcast and Quit; a pipe to the child process keeps the read endpoint read-only.
  - **Tauri v2.** Tray, menus, notifications, single-instance and autostart come as official plugins, and the window is built in HTML. It runs on all three platforms and is smaller than Electron. The TypeScript logic would run as a Bun sidecar, a helper program the app starts. Its autostart plugin uses a plain launch agent rather than SMAppService (*recalled*).

**Recommendation:** keep Electron (confidence medium-high). Agora's needs sit in the tray, notifications and login items, which GPUI does not cover, and the costly part of any move would be rewriting the logic, not the shell.

**What would change the answer:**

- Agora's memory use becoming a real cost: move to the Swift shell first.
- Agora needing Linux or Windows rigs without Electron: Tauri.
- The settings screen or a KIV/Agora window growing into a large, always-open, high-performance view, with a decision to move Agora to Rust: GPUI then becomes a candidate for that window.
- GPUI gaining stable tray, notification and login-item support.

## In Progress

Nothing.

## Queries

### Q1 - Check the GPUI facts online?

**Context:** The brief allowed reading gpui.rs, the Zed repository and docs.rs, but the run's Rules forbid any network call and say the Rules win. So the GPUI column rests on my own knowledge to about June 2026 and has not been checked against today's source.

**Query:** Should a short follow-up run check the GPUI column online?

**Options:**

a) (recommended, confidence medium - the answer rests mainly on Agora's own shape, which was checked, and GPUI adding a tray, notifications and login items in five months would be a large change) No check now; check only if a move away from Electron is considered.

b) Launch a short run whose Rules explicitly allow read-only web and `gh` reads of gpui.rs, `zed-industries/zed` (`crates/gpui`) and docs.rs, to verify the GPUI column with links and dates.

🧵 ki.prj.agora
