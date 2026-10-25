# Tower Assistant: Claude Design handoff prompt

Given to Kris at 01:20 BST on 22 October 2026 for Claude Design, and sent to personal.regular.site-tower with TOWER-APP-SHELL and TOWER-APP-PERMS.

```text
Design a cohesive visual identity and interface for "Tower Assistant", a small native macOS (SwiftUI, macOS 14+) companion app for the idle mobile game The Tower, which runs on the same Mac. It keeps the game's save fresh by nudging it on a schedule, records game screenshots and learning history for later review, and gives a floating toolbar of user-defined actions for the game.

Surfaces to design:
1. App icon: a macOS-style icon (1024px master, legible at 16-32px), plus a monochrome template glyph for the menu bar.
2. Menu-bar menu: status line (last save refresh, next scheduled run), Nudge Now, Snooze 5 minutes, Show The Tower, Show toolbar, Review history…, Settings…, Start at Login, Quit.
3. Floating Assistant toolbar: a compact always-on-top palette of action buttons with horizontal or vertical layout, a profile picker, and a clear active/idle state.
4. Settings window: General (show in Dock toggle, Start at Login, keep toolbar on top, in-app check reminders), Save refresh (enable, interval, Choose window…/Forget window), Profiles & actions editor (profiles: New, Duplicate, Rename, Remove; actions list with Add, Remove, Move up/down, label, screenshot toggle), and Data (JSON export…, Metadata export…, Offline HTML…, Import archive/recovery…, Emergency recovery export…, Retry unsaved recovery).
5. History review window: a browsable list of recorded captures with thumbnails, filters and Delete selected history….
6. Permissions panel: one row per grant the app uses (Accessibility for save refresh, Screen Recording for screenshots and learning images, Files & Folders for The Tower's save), each with a short purpose, a live status (Allowed, Not allowed, Not checked, Unavailable) and a button that shows the macOS prompt or opens that grant's System Settings pane; reachable from the menu, the app menu and a Dock click while a grant is missing.

Constraints: follow macOS Human Interface Guidelines and native controls (no web look); support light and dark mode; keep it calm and utilitarian, with a light nod to The Tower's sci-fi tower-defence look in the icon and accent colour only; destructive and recovery actions grouped away from everyday ones. Deliver annotated mockups for each surface, an icon set, the accent colour and type choices, and a short handoff note a SwiftUI developer can implement from.
```

Kris added TOWER-APP-PERMS afterwards: a permissions setup panel listing each grant (Accessibility, Screen Recording, Files & Folders for The Tower) with its status and a button that prompts or opens the right System Settings pane. Add it to the prompt as surface 6 if Claude Design has not yet run. Added as surface 6 on 22 October 2026, before Claude Design had run; personal.regular.site-tower built the interim panel as KB-MIDNIGHT-TOWER-APP-007.
