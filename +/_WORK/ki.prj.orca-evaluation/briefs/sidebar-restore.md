# Brief: sidebar-restore (ki.prj.orca-evaluation)

You are a background agent for ki.prj.orca-evaluation ("KI > Techne > Orca evaluation"). Read-only investigation; change nothing and commit nothing.

Kris, 30 October 2026: "I've removed some things from the sidebar. It's really easy to quickly remove them by saying hide from sidebar on the item. This would be, for example, Orca Mobile and Tasks. And in fact automations, but I do want to keep that one off the side anyway. What I don't have is anything which is obvious how to add them back on again."

Goal: find how to bring hidden items (Orca Mobile, Tasks) back into the Orca desktop app's sidebar, keeping Automations hidden.

Look, without editing anything: Orca's settings and menus as documented (docs, changelog, release notes), `orca --help` and any CLI or settings command, the app bundle's resources for the "Hide from sidebar" string and its counterpart (for example a "Show in sidebar", "Customise sidebar" or settings toggle, or a sidebar right-click menu), and Orca's local state under ~/Library/Application Support/orca/ to find where the hidden list is stored (read only).

Report: the simplest way back in the UI if one exists; otherwise one exact command Kris could paste to restore Mobile and Tasks only, stating whether Orca must be quit first, with the evidence; and whether this is worth a feature request to Orca (an obvious "show hidden items" control). British English, ASCII hyphens only.
