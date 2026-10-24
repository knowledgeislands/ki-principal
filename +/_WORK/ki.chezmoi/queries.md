# ki.chezmoi queries

## Open

### FIREWALL-ROUTE - Choose the route for the attended firewall practice

**Context:** Two routes re-apply terra's Screen Sharing firewall (tailnet only). Both have passed a final blind review as ready for an attended practice at terra's screen; neither changes SSH or Tailscale. v5 practises its undo, then applies the rules itself and undoes them automatically after ten minutes unless you confirm from sol; it leaves nothing behind. Minimal practises a short undo, then you run `rig apply --sudo` yourself; any undo is by hand, and it leaves one extra firewall reference that the undo does not release (harmless to connections). Both need the practice and the sol checks to pass before the real change; seven stages each, with two Terminal windows on terra. Full sequences: ~/.local/state/ki/agents/chezmoi/firewall-fix-3.report.md. **Query:** Which route do you want for the practice? **Options:** a) (recommended, confidence medium, blind review - automatic undo and nothing left behind; the live practice is still to come) v5: a run first fixes three "IPv5" wording slips in its prompts, then you get the exact commands. b) minimal: you accept manual undo and the leftover reference; you get its exact commands. c) leave the firewall as it is for now.

### RADAR-SCOPE - Show radar stage apart from which machines run a tool

**Context:** You said a tool on Trial need not be on a given Mac, and the Rig website should show that. Pi is now Trial with no machine selected. Both runs agree the radar stage (ring) and machine selection should be independent: a ring change never alters what a Mac installs, and the website shows the ring beside the machines that select the tool, never "running" or "installed". A public tool selected by no Mac reads "Trial · no published machine selected". They differ on whether a trial's phase (planned, active, paused) is recorded and published. Publication risk found in review: Rig's public export carries each tool's full rationale text, and Pi's and Orca's hold dated private notes, so that prose must be cleaned before either is ever made public. Pi and Orca stay private under the current policy either way. **Query:** How far should the radar design go? **Options:** a) (recommended, confidence medium, blind review - your "started and stopped for now" is a phase worth recording, but publishing it adds upkeep and disclosure for little gain) separate ring and selection; record trial phase privately in the catalogue; publish only ring and declared machines. b) the same separation and website display, with no recorded phase; whether a trial is paused stays in the work records. c) the same, and also publish the trial phase on the website (the first run's high-confidence choice). d) defer both and leave the website unchanged.

## Parked

None (Kris unparked everything, 24 October).
