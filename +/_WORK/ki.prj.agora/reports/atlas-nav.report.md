# KI > Techne > [Agora](/Users/krisbrown/kis/knowledge-islands/ki-principal/+/_WORK/ki.prj.agora/work.md) › atlas-nav

**🤖 → 👤 Handoff to supervisor · Run report at 23:14 GMT · last mark 00:04 GMT**

---

## New and noteworthy

- **Home now shows who holds what.** It lists the live work packages across sol and terra in three groups: leaders first, then managers, then doers. Two seats not created follow, and clicking a row opens it in the right tray.
- **Agora is a warden, not "Agora's keeper".** While this run was going, Kris approved the guild's ROLES-TIDY, and ki.prj.agora's `state.md` now records `role: warden`. The table follows that change: it has no Agora's keeper role, and a record that still says "Agora's keeper" is read as the old name for Warden and marked †.
- **Short eyebrows for the folded sidebar:** AGO (Agora), WRK (Work), GLD (Guilds), OBS (Observatory), KIV (KIV), NXT (Coming) and SYS (System: Accounts, Settings and Updates).
- **The installed Beacon does not yet send roles.** It was built before this change, so for now the Atlas reads each package's role and tier from `state.md` on this Mac. The Beacon will share roles between the rigs once it is rebuilt and reinstalled, which is outside this run.

## Done

- `f175801` on `main`, pushed: the self-check passed and all 524 tests passed. The screenshots looked right in light and dark, both expanded and folded, and the capture output was removed.
- **Known Lands:** the map has moved from Home into Work under its new name. Its icon is a chart folded in three, with a mark on it. A named slot (`ART`, key `lands`) is ready for the illustrator's art. Every "Show on Home" is now "Show on Known Lands".
- **Sidebar:**
  - Every place now sits under a section with an eyebrow, and Guilds and the foot have eyebrows too.
  - The eyebrows are smaller than before.
  - When the sidebar is folded, each section shows its three-letter eyebrow in place of the old divider line.
- **Home's roles table** has the columns Role (with its glyph), Tier, Package, Rig, Focus areas and State.
  - **Focus areas:** each id is in bold with its ⭐ or ⏰ marks and its line, cut to one line, with the full line on hover.
  - **State:** a glyph and words, such as 🤖 Working, 👤 With you, 👤 Waits on you or 🤖 Waiting for a worker.
  - **Where role and tier come from:** the package's `state.md` front matter first, either its own `role:` and `tier:` or the first worker's in the older `workers:` block. Otherwise the table uses a stand-in role catalogue, written from the settled role catalogue brief and the guild's decisions since. Failing both, it shows "—".
  - **Footnotes:** † means the record disagrees with the catalogue, such as "enablers" or "assistant". ‡ means no role is recorded, so the catalogue's role is shown. § means the record names a role the catalogue does not have. Each footnote is listed once below the table, naming every package it applies to.
  - **Seats not created:** Quartermaster `ki.reg.tools` and Librarian `ki.reg.library` show as "not created", with State 👤 Yours to approve.
  - **Territory:** the table follows the window's territory setting.
- **Tests:** pure tests with fixtures cover reading the seat from `state.md`, the catalogue lookups, role and tier precedence, every footnote case, the state words, the table's order and the headline. Messages from peers on an older Beacon, which send no roles, still read correctly.
- **Docs:** the view API page and its example now include the new roster fields, and the app's design note describes Home, Known Lands and the sidebar.

## In Progress

- Nothing from this run. The table will look tidier as each package records its role. The inbox packages still say "assistant" and "enablers", and five packages record no role yet. That clean-up belongs to the guild's ROLE-FIX work, not to Agora.

## Queries

### LIBRARY-ROW - Should Home list the library as a seat not created?

**Context:** Kris asked Home to list the catalogue's roles that have no package yet, such as the quartermaster's `ki.reg.tools`. The settled role catalogue brief also names one library, `ki.reg.library`, but whether to open it is still an open guild query (LIBRARY-OPEN). Home shows it now as Librarian `ki.reg.library`, not created, 👤 Yours to approve.

**Query:** Should the library stay on Home as a seat waiting for your approval?

**Options:**

a) (recommended, confidence medium - the brief names the seat and opening it is your decision, which is what the row says) Keep it until LIBRARY-OPEN is answered.

b) Drop it until the guild opens the library, so Home shows only the quartermaster.

🧵 ki.prj.agora
