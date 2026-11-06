# Registering 8.2 Guilds, reworked

`build/guilds2.py` and `build/guilds2.css` hold the whole page. Nothing else in the pack was edited. The lines below register it. They were tested in a copy of the pack: `python3 build/plan.py && node build/shoot.js build/plan.json shots && python3 build/board.py` gave 57 mock-ups, 30 components and 16 pages, and every 8.2 PNG was under 360 KB. Against the pack's current `mocks.py` (shell 0.4, bar 0.5), the 8.2 mocks draw in the new shell without clipping.

## build/plan.py

1. After `import work as W ...`:

```python
import guilds2 as G2  # noqa: E402  (8.2 Guilds, reworked)
```

2. After the `COMPONENTS = [...]` list, before `def tray_page(key):`:

```python
# 8.2 Guilds, reworked (build/guilds2.py) supersedes 8.1 after Kris's review.
PAGES[[p['id'] for p in PAGES].index('8.1')]['title'] = 'Guilds (superseded by 8.2)'
for _ab in ARTBOARDS:
    if _ab['page'] == '8.1':
        _ab.pop('preferred', None)
        _ab['dropped'] = 'superseded by 8.2 Guilds, reworked'
PAGES.append(G2.PAGE)
ARTBOARDS += G2.ARTBOARDS
COMPONENTS += G2.COMPONENTS
```

If 8.1 has to keep its ★ on the board, leave out the two lines inside the `for` loop. The 8.1 artboards still get the "Dropped" badge.

3. In `main()`, before `components = [...]`:

```python
    shots += G2.extra_shots(MOCKS)  # 8.2a in light
```

## build/board.py

After the `COMPONENT_TITLES = [...]` list:

```python
# 8.2 Guilds, reworked (build/guilds2.py)
COMPONENT_TITLES += [dict(id='8.2.1', title='Shield bar'), dict(id='8.2.2', title='Tree row, guild and skill'),
                     dict(id='8.2.3', title='Skill in the right tray')]
```

## IA.md (for the shell's owner)

- The page table: `| 8.2 | Guilds, reworked | this round (8.2a ★); supersedes 8.1 |`. The table now says "Guilds, revised", and Kris's review calls the page "Guilds, reworked". Use one name in both places.
- The 8.1 row: `| 8.1 | Guilds | superseded by 8.2 |`.
- The shell rule "Bottom pane without the tray" uses a skill as its example. On 8.2 a skill opens in the **right tray**, with tabs for SKILL.md, references/, scripts/ and assets/. Guilds no longer uses the bottom pane. The rule can stand with "a long document" as its example instead.

## index.md rows

In the keeper table:

```text
| [agora-app/8.2.html](agora-app/8.2.html), `build/guilds2.py`, `build/guilds2.css` | 2026-11-06 | Agora Atlas Guilds, reworked: the scrolling shield bar with All guilds frozen, the summary-filter bar, the guild and skill tree table, a skill in the right tray; supersedes 8.1 | Kris's review of 8.1 | keeper |
```

In "Agora app design pack: every artboard", after the 8.1 rows. Mark the 8.1 rows "dropped, superseded by 8.2 Guilds, reworked".

```text
| [8.2a](agora-app/8.2.html#8.2a) | Guilds, reworked | Shields over a tree table: ki-delegation in the tray | preferred | [shot](agora-app/shots/8.2a.png) |
| [8.2a, in light](agora-app/8.2.html#8.2a-light) | Guilds, reworked | 8.2a in light, for comparison | state | [shot](agora-app/shots/8.2a-light.png) |
| [8.2b](agora-app/8.2.html#8.2b) | Guilds, reworked | The shields as a list beside a flat table | alternative | [shot](agora-app/shots/8.2b.png) |
| [8.2c](agora-app/8.2.html#8.2c) | Guilds, reworked | 8.2a with the Governance shield chosen: the tray shut, every column whole | state | [shot](agora-app/shots/8.2c.png) |
| [8.2d](agora-app/8.2.html#8.2d) | Guilds, reworked | 8.2a with the bar scrolled to its end: All guilds frozen, Acquire chosen | state | [shot](agora-app/shots/8.2d.png) |
| [8.2e](agora-app/8.2.html#8.2e) | Guilds, reworked | 8.2a with the references/ tab open in the tray | state | [shot](agora-app/shots/8.2e.png) |
| [8.2.1](agora-app/8.2.html#8.2.1) | Guilds, reworked, components | Shield bar: at rest, more to the right; a shield chosen; scrolled, All guilds frozen; a shield | component | [shots](agora-app/shots/components/) |
| [8.2.2](agora-app/8.2.html#8.2.2) | Guilds, reworked, components | Tree row, guild and skill: a guild open; a guild folded; a skill chosen; a skill plain; a skill bound to a runtime; a long guild, Show 6 more | component | [shots](agora-app/shots/components/) |
| [8.2.3](agora-app/8.2.html#8.2.3) | Guilds, reworked, components | Skill in the right tray: SKILL.md; a folder tab, references/ | component | [shots](agora-app/shots/components/) |
```

## README.md

In the page table:

```text
| [8.2](8.2.html) | Guilds, reworked (supersedes 8.1) | 8.2a Shields over a tree table ★ (8.2c a shield chosen, 8.2d the bar scrolled, 8.2e a folder tab), 8.2b The shields as a list; 8.2a in light; components 8.2.1 to 8.2.3 |
```

Change the 8.1 row's part to "Guilds (superseded by 8.2)". Replace the "Guilds are badges across" choice with:

- **Guilds are shields over a tree table** (8.2a ★), after Kris's review of 8.1, which it supersedes. The guild shields sit in one bar that scrolls sideways. **All guilds** is frozen first, so the way back never scrolls away. A fade covers each side that hides shields, and the bar's right end holds two chevrons and how many shields lie before and after. A shield keeps its guild and adds a Guild chip. Under the bar is the same summary-filter bar as Roadmap and Jobs. It tallies the skills by `ki-kind` (governance 54, process 11) and by `ki-applicability` (baseline 2, detected 19, declaration-only 33, invocation-only 11), in captioned groups. The table is a two-level tree: each guild a row that folds, with its count, about line and mix of kinds and applicabilities, and its skills beneath on a branch line. The columns come from the SKILL.md front matter: name (monospace), description (its first clause), `ki-kind`, `ki-applicability`, `ki-depends-on` (the first, then +N), `argument-hint` (monospace) and runtimes (`ki-supported-runtimes`, or "any"). With the tray open, argument-hint and Runtimes step out and the last header reads +2. A long guild shows its first seven skills and "Show N more". A chosen skill opens in the **right tray**, with tabs for SKILL.md (front matter as keys and values, then the body drawn), references/, scripts/ and assets/ (each a file list with sizes, and the chosen file drawn). Guilds has no bottom pane, no gold and no brass, since nothing there waits on Kris. The alternative, **the shields as a list** (8.2b), shows all nine choices without scrolling. It costs 200 points of table, two columns hidden, and the guild as a place. The data is the 65 real skills in `ki-agentic-harness/skills/<guild>/<skill>/SKILL.md`, read on 6 November.
