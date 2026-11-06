"""Agora Atlas page 8.2 Guilds, reworked: Kris's review of 8.1, drawn in the 0.3 shell (atlas_page).

A scrolling bar of guild shields with All guilds frozen first; the pack's summary-filter bar (tallies by ki-kind and
ki-applicability, chips, Filter, words, Group); a two-level tree table, each guild a row that folds, its skills beneath,
with the columns of SKILL.md front matter; and a chosen skill in the right tray, with tabs for SKILL.md, references/,
scripts/ and assets/. No bottom pane.

The skills are the 65 under ki-agentic-harness/skills/<guild>/<skill>/SKILL.md as read on 6 November 2026: their names,
ki-kind, ki-applicability, ki-depends-on, argument-hint, ki-supported-runtimes, the first clause of each description and
how many files each of references/, scripts/ and assets/ holds. Guild colours and monograms are 8.1's (work.GUILDS_KI).

Registered from plan.py (PAGE, ARTBOARDS, COMPONENTS, extra_shots) and board.py (COMPONENT_TITLES); see
guilds2.REGISTER.md. Its own styles are in guilds2.css, linked after app.css.
"""
import os
from html import escape

from mocks import R, head, aglyph, tray_frame, atlas_page
import work as W

CSS_LINK = '<link rel="stylesheet" href="../build/guilds2.css">'
CTX_KI = dict(territory='Knowledge Islands')
NOW = W.NOW

# ---------------------------------------------------------------- the real skills
# guild | name | ki-kind | ki-applicability | ki-depends-on | argument-hint | runtimes | references/scripts/assets | description
SKILLS_TSV = '''
keystone|ki-bootstrap|process|invocation-only||help | refresh||3/0/0|Explain first-time KI activation through the `ki` CLI: user bootstrap, verified harness selection, skills, and repository governance
keystone|ki-repo|governance|baseline|ki-authoring,ki-git|audit | conform <repo> | educate <repo> | help | refresh | review [scope] | review close <REV-NNN>||7/4/0|Audit or conform the universal KI repository contract declared by .ki.toml
keystone|ki-skills|governance|detected||audit <skill-or-repo> | conform <skill> | educate <description> | extract <repo> | help | optimise <skill> | refresh | review <skill-or-repo>||9/3/0|Create, audit, review, extract, or optimise Agent Skills
governance|ki-agentic-radar|governance|declaration-only||audit | conform | educate | help | refresh||4/2/0|Maintain an evidence-backed radar for agentic protocols, interfaces, organisations, architectures, research, and vendor terms
governance|ki-authoring|governance|baseline||audit <path> | conform <path> | educate <target> | help | refresh||9/2/0|Govern KI Markdown, TOML, README composition, industry white papers, and durable knowledge placement
governance|ki-decision-records|governance|detected||audit [dir] | conform [dir] | consolidate [dir] | educate [dir] | help | new <scope> "<title>" | refresh||9/2/0|Create or audit typed KI Decision Records for durable rationale and authority
governance|ki-delegation|governance|declaration-only||audit <repo> | conform <repo> | educate <work-item> | help | refresh||4/3/7|Govern agent delegation: routine detached background runs and durable packets for approved high-risk handoffs
governance|ki-diagrams|governance|declaration-only||audit [dir] | conform [dir] | help | educate [dir] | refresh||8/7/2|Create, audit or refresh a repository's living Archify diagrams: committed sources and SVGs, the manifest, privacy
governance|ki-engineering|governance|detected||audit <repo> | conform <repo> | help | educate <repo> | refresh||4/2/0|Audit or conform KI TypeScript/Bun engineering: modularity, reuse, boundary testing, package scripts, tsconfig, Biome
governance|ki-git|governance|declaration-only||audit <repo> | conform <repo> | help | educate <repo> | refresh||3/3/0|Govern KI Git commits and shared-tree safety: Conventional Commits, touched-path tracking, explicit staging
governance|ki-guides|governance|detected||audit [dir] | conform [dir] | help | educate [dir] | refresh||7/2/0|Create or audit repository-local guides for the practical how of using, operating, contributing to, or maintaining a system
governance|ki-model-radar|governance|declaration-only||audit | conform | educate | help | refresh||4/2/0|Maintain an evidence-backed radar for models and model-agent routes
governance|ki-specs|governance|detected||audit [dir] | conform [dir] | help | educate [dir] | new <area> "<title>" | refresh||8/2/0|Create or audit repository Specifications: accepted behaviour and quality requirements with conformance state
governance|ki-trade|process|invocation-only|ki-trades|prepare <receiver> | observe <TRD> | submit <TRD> | abandon <TRD> | receive <TRD> | release <TRD> | list | show <TRD> | help||1/0/0|Operate one repository's side of a declared cross-repository trade
governance|ki-trades|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/0|Govern directional work and knowledge trades between KI repositories: routes, records, authority, receipt
governance|ki-work-package|governance|detected||audit <repo> | conform <repo> | educate <repo> | help | refresh | remove <id> | resume <id> | update <id>||3/2/0|Own the work package of one piece of work, its five files in its work folder +/_WORK/<id>/
change-management|ki-accept|process|invocation-only||accept <work> | prune <work-record-or-glob>... | help||2/4/0|Close a reviewed local work record as done, cancel an open record, or prune eligible terminal records
change-management|ki-batch|process|invocation-only||batch <work>... | batch outcome <outcome> | run <batch-authorisation> | help||5/6/0|Prepare and run one bounded authority envelope over an exact set of Ready work records in one repository
change-management|ki-coordination|governance|declaration-only|ki-delegation,ki-work-package|audit <repo> | conform <repo> | drain | educate <repo> | help | hold | mark | receive | refresh | resume | send | summary||3/4/0|Govern coordinating work under the Knowledge Islands work model: the responsive coordinator and its turn budget
change-management|ki-implement|process|invocation-only||implement <work-item> | help||2/2/0|Deliver one approved Ready local work record from immutable baseline through verification and Awaiting review
change-management|ki-next|process|invocation-only||next [--review] | defer <item> <horizon> | help||1/2/0|Capture substantive prospective work as unadopted triage records, or select, adopt, promote, defer, hold and release
change-management|ki-plan|process|invocation-only||plan <work>... | help||1/2/0|Shape selected Now or Next draft work in the local roadmap or KB Streams adapter until it is Ready
change-management|ki-recap|process|invocation-only|ki-authoring|checkpoint <work id> | help | recap [--runtime detect|claude|codex] [--transcript <session-file>]||2/4/0|Recap the live session by summarising changes, decisions, touched files, unfinished work, and durable learning routes
change-management|ki-work|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||4/2/0|Select and audit a repository's KI forward-work adapter and shared lifecycle vocabulary
change-management|ki-work-design|process|invocation-only||start <subject> | resume <id> | help||2/0/4|Shape a new Project, theme or cross-cutting model before any work record exists
change-management|ki-work-github-issues|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/0|Define GitHub Issues configuration, lifecycle mapping, hierarchy, dependencies, review and closure as a KI work adapter
change-management|ki-work-linear|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/0|Define Linear configuration, lifecycle mapping, hierarchy, dependencies, review and closure as a KI work adapter
change-management|ki-work-recurring|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/2|Govern recurring-work identity, cadence, due-run reservation, and successful-run evidence
change-management|ki-work-roadmap|governance|declaration-only||audit <repo> | conform <repo> | help | educate <repo> | refresh||4/2/0|Govern flat local work items, roadmap horizons, lifecycle detail, dependencies and root orientation
repo-structure|ki-repo-dotfiles-chezmoi|governance|declaration-only|ki-authoring|audit <repo> | conform <repo> | help | educate <repo> | refresh||3/2/0|Audit or conform KI chezmoi source repositories: source-versus-target editing, app-mutated configuration
repo-structure|ki-repo-harness|governance|declaration-only|ki-skills,ki-subagents,ki-decision-records,ki-work-roadmap|audit [path] | conform [path] | educate <name> | help | refresh||4/3/1|Audit or design a KI-compatible harness that publishes skills, subagents, evals, and hooks as a verified installed payload
repo-structure|ki-repo-homebrew-tap|governance|detected||audit <repo> | conform <repo> | educate <repo> | help | refresh||7/2/1|Audit or scaffold a KI Homebrew tap and its Formula/*.rb distribution surface
repo-structure|ki-repo-kb|governance|detected|ki-repo-kb-activities,ki-repo-kb-live-artifacts,ki-repo-kb-streams|audit | conform | digest | extract | help | improve | educate | query <question> | refresh | save | update <note>||18/3/2|Create, query, update, distil, or audit a KI knowledge base using Calendar, Pillars, Resources, Streams
repo-structure|ki-repo-kb-activities|governance|declaration-only||audit | conform | help | educate | new <name> | refresh||8/2/0|Create, audit, and maintain Activity notes recording automation, scheduling, and agentic work
repo-structure|ki-repo-kb-live-artifacts|governance|declaration-only||audit | conform | help | educate | new <name> | refresh||8/2/0|Create, audit, and maintain KI Live Artifact pairs: a Markdown source and rendered HTML view
repo-structure|ki-repo-kb-principal|governance|declaration-only|ki-repo-kb,ki-decision-records|audit | conform | educate | help | refresh||3/2/1|Audit or conform a designated principal KI knowledge base's governance overlay
repo-structure|ki-repo-kb-streams|governance|detected||audit | conform | help | educate | refresh||8/2/0|Govern the KI knowledge-base Streams container and flat Roadmap records
repo-structure|ki-repo-mcp|governance|detected|ki-engineering|audit <repo> | conform <repo> | educate <repo> | help | refresh||12/2/2|Audit or scaffold KI MCP server code for source-release readiness, workspace-MCP layout, tool naming
repo-structure|ki-repo-project|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/1|Explain the baseline and composable structures for a non-Knowledge-Base KI Project repository
repo-structure|ki-repo-specifications|governance|detected||audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/1|Audit or scaffold the KI Specifications repository container: proposals, specifications, schemas, templates
repo-structure|ki-repo-tools|governance|detected||audit <repo> | conform <repo> | help | educate <repo> | refresh||11/2/2|Audit or scaffold a KI tools-* repository containing one CLI, installer, releases, changelog, CI and help
repo-structure|ki-repo-website|governance|detected||audit <repo> | conform <repo> | help | educate <repo> | refresh||7/2/1|Govern the generator-neutral KI website seam: source root, reproducible dist/, and the ki:site scripts
repo-structure|ki-repo-website-app|governance|detected|ki-repo-website|audit <repo> | conform <repo> | help | educate <repo> | refresh||7/2/0|Govern the KI interactive website implementation: one client-side React application bundled by Vite
repo-structure|ki-repo-website-cloudflare|governance|detected|ki-repo-website|audit <repo> | conform <repo> | educate <repo> | help | refresh||8/2/0|Govern Cloudflare Workers Static Assets hosting, not Pages, for either KI website implementation
repo-structure|ki-repo-website-content|governance|detected|ki-repo-website|audit <repo> | conform <repo> | help | educate <repo> | refresh||8/2/0|Govern KI content sites built with Eleventy 3, Markdown or data, Nunjucks, Tailwind 4 tokens
agentic-systems|ki-agent-coordination-paperclip|governance|declaration-only||audit <repo> | help | conform | educate | refresh||2/2/0|Deprecated alias of ki-delegation-paperclip, kept only so a repository still declaring it resolves
agentic-systems|ki-delegation-paperclip|governance|declaration-only|ki-git|audit <arrangement> | conform <arrangement> | educate <arrangement> | help | refresh||6/2/2|Govern Paperclip as the KI delegation adapter: company and repository boundaries
agentic-systems|ki-subagents|governance|detected||audit | conform | educate | refresh | help||3/2/0|Define or assess runtime-neutral KI subagent roles: identity, delegation purpose, instructions, lane, hand-offs
agentic-systems|ki-subagents-chatgpt|governance|detected|ki-subagents|audit | conform | educate | refresh | help|chatgpt-codex|3/2/0|Audit or write Codex TOML projections of approved portable KI subagent roles
agentic-systems|ki-subagents-claude|governance|detected|ki-subagents|audit <agent-or-dir> | conform <agent> | help | educate <description> | refresh|claude-code|4/2/0|Audit or write Claude Code Markdown/YAML projections of approved portable KI subagent roles
environment|ki-binding|governance|declaration-only||audit [project] | conform [project] | help | educate [project] | refresh||3/2/0|Govern the portable KI MCP inventory in XDG mcp-servers.yaml: schema, client targeting, and mcporter drift
environment|ki-binding-chatgpt|governance|declaration-only|ki-binding|audit [project] | conform [project] | help | educate [project] | refresh|chatgpt-codex|3/4/0|Audit or safely render KI-targeted MCP servers into Codex native [mcp_servers]
environment|ki-binding-chezmoi|governance|declaration-only|ki-binding,ki-repo-dotfiles-chezmoi|audit <target> | conform <target> | help | educate <target> | refresh||3/2/0|Audit or conform the chezmoi rendering path from canonical KI mcp-servers.yaml through chezmoi apply
environment|ki-binding-claude|governance|declaration-only|ki-binding|audit [project] | conform [project] | help | educate [project] | refresh|claude-code|3/2/0|Audit or safely conform Claude-native MCP configuration across Claude Code, Claude Desktop and claude.ai
environment|ki-housekeeping-chatgpt|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh|chatgpt-codex|7/4/0|Audit ChatGPT opaque local-store evidence and Codex local memory or repository-scoped sessions
environment|ki-housekeeping-claude|governance|declaration-only||audit | conform | help | educate | refresh|claude-code|7/2/0|Audit Claude Desktop, Cowork, Claude Code and VSCode state: memory, storage hygiene, plugins, caches and backups
environment|ki-tokenomics|governance|declaration-only||audit | conform | help | educate | refresh||8/2/0|Govern portable agent-context budgets, standing-surface attribution, and model-purpose policy
environment|ki-tokenomics-chatgpt|governance|declaration-only|ki-tokenomics|audit | conform | educate | refresh | help|chatgpt-codex|7/4/0|Audit non-secret Codex repository evidence for portable tokenomics
environment|ki-tokenomics-claude|governance|declaration-only|ki-tokenomics|audit | conform | educate | refresh | help|claude-code|7/2/0|Audit non-secret Claude Code repository evidence for portable tokenomics
acquire|ki-acquire|governance|declaration-only||audit <repo> | conform <repo> | educate <repo> | help | refresh||4/2/0|Govern source-independent knowledge capture and curation: supplied scope, honest coverage, faithful preservation
acquire|ki-acquire-chatgpt|governance|declaration-only|ki-acquire|audit <repo> | conform <repo> | educate <repo> | help | refresh|chatgpt-codex|3/2/0|Govern ChatGPT conversation capture: honest digest or full-thread coverage, routing from project evidence
acquire|ki-acquire-granola|governance|declaration-only|ki-acquire|audit <repo> | conform <repo> | educate <repo> | help | refresh||3/2/0|Acquire Granola meetings through read-only MCP calls: complete date windows, folder routing, transcripts
acquire|ki-pulse|process|invocation-only||capture <url-or-source> [reason] | help | scan <interest-or-query> [sources] | triage [current-signals]||1/0/0|Capture a submitted link or scan bounded public sources, then triage current signals
design|ki-design-inspiration|process|invocation-only||help | inspire <website-or-component> | refresh||1/0/0|Find website design inspiration in curated galleries and turn selected examples into practical directions
design|ki-design-system|governance|declaration-only||audit [dir] | conform [dir] | help | educate [dir] | refresh||9/5/1|Create, audit or refresh how a repository keeps its user-interface design: the token source, the guide, the checks
'''


def _parse(tsv):
    out = []
    for line in tsv.strip().splitlines():
        # The argument-hint holds '|' itself, so split from both ends.
        guild, name, kind, appl, deps, rest = line.split('|', 5)
        rest, desc = rest.rsplit('|', 1)
        rest, files = rest.rsplit('|', 1)
        hint, runtimes = rest.rsplit('|', 1)
        r, s, a = (int(x) for x in files.split('/'))
        out.append(dict(guild=guild, name=name, kind=kind, appl=appl, deps=[d for d in deps.split(',') if d],
                        hint=hint.strip(), runtimes=runtimes, refs=r, scripts=s, assets=a, desc=desc))
    return out


SKILLS = _parse(SKILLS_TSV)
GUILDS = [dict(id=g[0], title=g[1], mono=g[2], hue=g[3], about=g[4]) for g in W.GUILDS_KI]
GBYID = {g['id']: g for g in GUILDS}
for _g in GUILDS:
    _g['skills'] = sorted((s for s in SKILLS if s['guild'] == _g['id']), key=lambda s: s['name'])
assert len(SKILLS) == 65 and all(_g['skills'] for _g in GUILDS)

KINDS = [('governance', 'Governance'), ('process', 'Process')]
APPLS = [('baseline', 'Baseline'), ('detected', 'Detected'), ('declaration-only', 'Declaration-only'), ('invocation-only', 'Invocation-only')]


# ---------------------------------------------------------------- marks: shape carries the meaning, the word always beside it
def g2mark(kind):
    p = {
        # ki-kind
        'governance': '<rect x="2.2" y="2.2" width="7.6" height="7.6" rx="1" fill="currentColor"/>',
        'process': '<path d="M3 2 L10 6 L3 10 Z" fill="currentColor"/>',
        # ki-applicability
        'baseline': '<circle cx="6" cy="6" r="4" fill="currentColor"/>',
        'detected': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M6 2.2 A3.8 3.8 0 0 1 6 9.8 Z" fill="currentColor"/>',
        'declaration-only': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.4"/>',
        'invocation-only': '<circle cx="6" cy="6" r="3.8" fill="none" stroke="currentColor" stroke-width="1.3" stroke-dasharray="2 1.6"/>',
        'all': '<path d="M2 3.5h8M2 6h8M2 8.5h8" stroke="currentColor" stroke-width="1.3"/>',
    }[kind]
    return f'<svg class="sm g2m g2m-{kind}" viewBox="0 0 12 12" aria-hidden="true">{p}</svg>'


def g2shield(mono, hue, size=30, all_=False):
    """A guild's shield: its monogram on its own colour (identity only, never a meaning). All guilds is an outline."""
    path = 'M20 3 L35 9 V21 C35 30.5 28.6 37.2 20 41 C11.4 37.2 5 30.5 5 21 V9 Z'
    text = f'<text x="20" y="26" text-anchor="middle">{escape(mono)}</text>' if size >= 22 else ''
    cls = 'g2sh all' if all_ else 'g2sh'
    style = '' if all_ else f' style="--h:{hue}"'
    return f'<svg class="{cls}" viewBox="0 0 40 44" width="{size}" height="{round(size * 1.1)}"{style} aria-hidden="true"><path d="{path}"/>{text}</svg>'


# ---------------------------------------------------------------- 8.2.1 the shield bar
def shield_tile(g, on=False):
    return (f'<span class="g2tile{" on" if on else ""}" data-g2guild="{g["id"]}" title="{escape(g["about"])}">'
            f'{g2shield(g["mono"], g["hue"])}<span class="g2-tx"><span class="g2-nm">{escape(g["title"])}</span>'
            f'<span class="g2-ct">{len(g["skills"])} skills</span></span></span>')


def shield_bar(chosen=None, scroll=0, more_right=0, more_left=0, code='P2'):
    """All guilds frozen at the left; the guild shields scroll beneath a fade; the cue at the right end says how many shields
    lie out of view on each side. scroll is how far the track has moved (points)."""
    all_tile = (f'<span class="g2tile g2all{" on" if chosen is None else ""}" data-g2guild="all">{g2shield("65", 0, all_=True)}'
                f'<span class="g2-tx"><span class="g2-nm">All guilds</span><span class="g2-ct">{len(SKILLS)} skills</span></span></span>')
    tiles = ''.join(shield_tile(g, on=(g['id'] == chosen)) for g in GUILDS)
    fades = ('<span class="g2fade l"></span>' if scroll else '') + ('<span class="g2fade g2-r"></span>' if more_right else '')
    track = f'<div class="g2track" style="transform:translateX(-{scroll}px)">{tiles}</div>'
    words = ' · '.join(w for w in (f'{more_left} before' if more_left else '', f'{more_right} more' if more_right else '') if w)
    cue = (f'<div class="g2end"><span class="g2cues"><span class="g2cue{"" if more_left else " off"}" title="Scroll back">{aglyph("chev", "g2chev l")}</span>'
           f'<span class="g2cue{"" if more_right else " off"}" title="Scroll for more guilds">{aglyph("chev", "g2chev g2-r")}</span></span>'
           f'<span class="g2more">{words}</span></div>')
    return (f'<section class="g2bar{" scrolled" if scroll else ""}{" atend" if scroll and not more_right else ""}" {R(code, "Guild shields")}>'
            f'<div class="g2frozen">{all_tile}</div><div class="g2view">{track}{fades}</div>{cue}</section>')


# ---------------------------------------------------------------- the summary-filter bar (7.1.1 in Guilds' shape)
def _tally(key, n, words, on=False):
    cls = 'tally' + (' on' if on else '') + (' zero' if n == 0 else '')
    return (f'<span class="{cls}" data-tally="{key}" title="{escape(words)}: keep only these; ⌘-click to add">'
            f'<span class="v">{g2mark(key)}<b>{n}</b></span><span class="k">{escape(words)}</span></span>')


def _field(words):
    return f'<span class="g2field mono">{words}</span>'


def counts(skills):
    c = {k: 0 for k, _ in KINDS + APPLS}
    for s in skills:
        c[s['kind']] += 1
        c[s['appl']] += 1
    return c


def g2_bar(skills, chosen=None, on=None, find='', group='Guild', code='P3'):
    """Tallies in three captioned groups (skills, ki-kind, ki-applicability), then the pack's chip row."""
    c = counts(skills)
    def grp(field, tallies):
        return f'<div class="g2tg"><span class="g2field mono">{field}</span><div class="g2tr">{"".join(tallies)}</div></div>'
    groups = (grp('skills', [_tally('all', len(skills), 'All skills', on=on is None)])
              + grp('ki-kind', [_tally(k, c[k], w, on=(on == k)) for k, w in KINDS])
              + grp('ki-applicability', [_tally(k, c[k], w, on=(on == k)) for k, w in APPLS]))
    chips = [W.ctx_chip('Territory', 'Knowledge Islands')]
    if chosen:
        chips.append(W.chosen_chip('Guild', GBYID[chosen]['title']).replace('data-chip="chosen"', 'data-chip="chosen" data-g2chip="guild"'))
    chips.append(W.filter_button())
    bar = W.sf_bar([], chips, W.find_box(find, 'Words in a name or description'), W.group_seg(['Guild', 'ki-kind', 'None'], group), code=code)
    return bar.replace('<div class="sf-tallies"></div>', f'<div class="g2tallies">{groups}</div>', 1)


# ---------------------------------------------------------------- 8.2.2 tree rows
def _cols(wide):
    if wide:
        return ('<colgroup><col class="c-name"><col class="c-desc"><col class="c-kind"><col class="c-appl"><col class="c-dep">'
                '<col class="c-hint"><col class="c-rt"></colgroup>'
                '<thead><tr><th>Name</th><th>Description</th><th>ki-kind</th><th>ki-applicability</th><th>ki-depends-on</th>'
                '<th>argument-hint</th><th>Runtimes</th></tr></thead>')
    # With the tray open, argument-hint and Runtimes give way (the tray shows both); the last header says so.
    return ('<colgroup><col class="c-name"><col class="c-desc"><col class="c-kind"><col class="c-appl"><col class="c-dep">'
            '<col class="c-mc"></colgroup>'
            '<thead><tr><th>Name</th><th>Description</th><th>ki-kind</th><th>ki-applicability</th><th>ki-depends-on</th>'
            '<th class="g2-mc" title="argument-hint and Runtimes: hidden while the tray is open">+2</th></tr></thead>')


def guild_row(g, open_=True, wide=True):
    n = len(g['skills'])
    c = counts(g['skills'])
    kinds = ' '.join(f'<span class="g2-gc" title="{c[k]} {k}">{g2mark(k)}{c[k]}</span>' for k, _ in KINDS if c[k])
    appls = ' '.join(f'<span class="g2-gc" title="{c[k]} {k}">{g2mark(k)}{c[k]}</span>' for k, _ in APPLS if c[k])
    rest = '<td></td><td></td><td></td>' if wide else '<td></td><td class="g2-mc"></td>'
    return (f'<tr class="g2g{" open" if open_ else " shut"}" data-g2row="{g["id"]}"><td class="g2-gname">'
            f'{aglyph("chev", "g2fold")}{g2shield(g["mono"], g["hue"], 20)}<b>{escape(g["title"])}</b>'
            f'<span class="g2-gn">{n}</span></td><td class="g2-gabout muted" title="{escape(g["about"])}">{escape(g["about"])}</td>'
            f'<td class="nowrap">{kinds}</td><td class="nowrap">{appls}</td>{rest}</tr>')


def _deps(deps):
    if not deps:
        return '<span class="muted">—</span>'
    first = f'<span class="mono">{deps[0]}</span>'
    return first + (f' <span class="muted g2-plus" title="{escape(", ".join(deps[1:]))}">+{len(deps) - 1}</span>' if len(deps) > 1 else '')


def skill_row(s, selected=None, last=False, wide=True):
    rt = f'<span class="mono">{s["runtimes"]}</span>' if s['runtimes'] else '<span class="muted">any</span>'
    kind = dict(KINDS)[s['kind']].lower()
    appl = dict(APPLS)[s['appl']].lower()
    dep = ' deprecated' if s['desc'].startswith('Deprecated') else ''
    return (f'<tr class="g2s{" sel" if s["name"] == selected else ""}{" last" if last else ""}{dep}" data-g2skill="{s["name"]}">'
            f'<td class="g2-sname"><span class="g2-branch"></span><span class="mono">{s["name"]}</span></td>'
            f'<td class="g2-desc" title="{escape(s["desc"])}">{escape(s["desc"])}</td>'
            f'<td class="nowrap">{g2mark(s["kind"])} {kind}</td><td class="nowrap">{g2mark(s["appl"])} {appl}</td>'
            f'<td class="g2-dep nowrap">{_deps(s["deps"])}</td>'
            + (f'<td class="g2-hint mono" title="{escape(s["hint"])}">{escape(s["hint"])}</td><td class="nowrap">{rt}</td></tr>' if wide else '<td class="g2-mc"></td></tr>'))


def more_row(g, n, wide=True):
    return f'<tr class="g2more-row"><td colspan="{7 if wide else 6}"><span class="g2-branch"></span>Show {n} more {escape(g["title"].lower())} skills</td></tr>'


def tree(open_=('governance',), only=None, selected=None, limit=None, wide=True, code='P4', label='Guilds and their skills'):
    rows = []
    for g in GUILDS:
        if only and g['id'] not in only:
            continue
        o = g['id'] in open_
        sk = g['skills']
        lim = limit if (limit and o) else len(sk)
        rows.append(guild_row(g, o, wide))
        if o:
            show = sk[:lim]
            rows += [skill_row(s, selected, last=(i == len(show) - 1 and lim >= len(sk)), wide=wide) for i, s in enumerate(show)]
            if lim < len(sk):
                rows.append(more_row(g, len(sk) - lim, wide))
    return (f'<section class="panel tablepanel g2tree" {R(code, label)}><table class="records g2t{"" if wide else " narrow"}">{_cols(wide)}'
            f'<tbody>{"".join(rows)}</tbody></table></section>')


# ---------------------------------------------------------------- 8.2.3 the skill in the right tray
TRAY_FILES = {
    'references/': [('rubric.md', '10 KB'), ('sources.md', '38 KB'), ('standards-background-runs.md', '60 KB'),
                    ('standards-delegation-packets.md', '4.5 KB')],
    'scripts/': [('inbox-boundary.test.ts', '2.9 KB'), ('rubric/', '3 items'), ('shared/', '1 item')],
    'assets/': [('grant-fetch.md', '1 KB'), ('grant-machine.md', '2.2 KB'), ('rules-none.md', '5.9 KB'), ('rules-prune.md', '6.4 KB'),
                ('rules-push.md', '6.1 KB'), ('rules-release.md', '6.7 KB'), ('run-prompt.md', '3.8 KB')],
}


def skill_tray(name='ki-delegation', tab='SKILL.md'):
    s = next(x for x in SKILLS if x['name'] == name)
    g = GBYID[s['guild']]
    tabs = [('SKILL.md', None), ('references/', s['refs']), ('scripts/', s['scripts']), ('assets/', s['assets'])]
    strip = ''.join(f'<span class="g2tt{" on" if t == tab else ""}{" none" if n == 0 else ""}">{t}{f"<span class=g2-n>{n}</span>" if n is not None else ""}</span>'
                    for t, n in tabs)
    strip = f'<div class="g2ttabs" {R("T2", "Tabs")}>{strip}</div>'
    if tab == 'SKILL.md':
        fm = [('name', f'<span class="mono">{s["name"]}</span>'),
              ('ki-kind', f'{g2mark(s["kind"])} {s["kind"]}'), ('ki-applicability', f'{g2mark(s["appl"])} {s["appl"]}'),
              ('ki-depends-on', '<span class="mono">[]</span>' if not s['deps'] else f'<span class="mono">{", ".join(s["deps"])}</span>'),
              ('ki-shared-dependencies', '<span class="mono">ki-skills:rubric</span>'),
              ('argument-hint', f'<span class="mono g2-wrap">{escape(s["hint"])}</span>'),
              ('ki-supported-runtimes', '<span class="muted">not set: any</span>' if not s['runtimes'] else f'<span class="mono">[{s["runtimes"]}]</span>')]
        kv = ''.join(f'<tr><td class="mono">{k}</td><td>{v}</td></tr>' for k, v in fm)
        body = (f'<div class="g2fm" {R("T3", "Front matter")}><table class="kv"><tbody>{kv}</tbody></table>'
                f'<p class="g2desc">Govern agent delegation: routine detached background runs (run packet, prompt shape, authority footers, decisions log, '
                f'coordination, run queue, monitoring) and durable packets for approved high-risk handoffs.</p></div>'
                f'<div class="g2md" {R("T4", "SKILL.md, drawn")}><div class="g2mdh">SKILL.md · 77 lines</div>'
                f'<h4>Knowledge Islands delegation standard</h4>'
                f'<p><span class="mono">ki-delegation</span> owns two runtime-neutral contracts for delegating Knowledge Islands work to agents:</p>'
                f'<ul><li><b>Background runs</b>: routine delegation to background agents: detachment, the run packet, prompt shape, authority tiers.</li>'
                f'<li><b>Delegation packets</b>: the durable, reviewable brief for an approved high-risk handoff.</li></ul>'
                f'<h5>Operating modes</h5><p>Carries the universal AUDIT · CONFORM · EDUCATE · REFRESH modes.</p>'
                f'<p class="g2-toc mono">Mode AUDIT · Mode CONFORM · Mode EDUCATE · Mode REFRESH · Mode HELP · Notes</p></div>')
    else:
        files = TRAY_FILES[tab]
        pick = 'standards-background-runs.md' if tab == 'references/' else files[0][0]
        lis = ''.join(f'<tr class="{"sel" if f == pick else ""}"><td class="mono">{f}</td><td class="muted nowrap g2-r">{sz}</td></tr>' for f, sz in files)
        body = (f'<div {R("T3", "Files")}><table class="g2files"><tbody>{lis}</tbody></table></div>'
                f'<div class="g2md" {R("T4", "The chosen file, drawn")}><div class="g2mdh g2-file mono">{tab}{pick} · 60 KB</div>'
                f'<h4>Background-run standard</h4><h5>Scope</h5>'
                f'<p>A background run is routine delegation of substantive work to one or more background agents. Anyone running Knowledge Islands work '
                f'through an agent uses this contract, whatever the runtime.</p>'
                f'<p>A <b>background agent</b> is a worker launched detached through <span class="mono">ki agent</span> under this contract. An '
                f'<b>in-session subagent</b> runs inside the launching session’s turn and is not a background agent.</p>'
                f'<p class="g2-toc mono">Detachment · Coordinating work · Run packet · Prompt shape · Authority tiers · Decisions log · Run queue · Monitoring · Reporting</p></div>')
    fade = '<div class="g2tfade">Scroll for more</div>' if tab == 'SKILL.md' else ''
    inner = f'{strip}<div class="g2tscroll">{body}{fade}</div>'
    kind = f'Skill · {g["title"]} · ki-agentic-harness'
    acts = [('', 'Open in a tab'), ('', 'Copy its path'), ('', 'Show in Roadmap')]
    return tray_frame(kind, f'<span class="id g2tid">{name}</span>', inner, actions=acts).replace('class="at-tray"', 'class="at-tray g2tray"', 1)


# ---------------------------------------------------------------- the pages
def _head(summary):
    return head('P1', 'Guilds', summary)


def page_a(open_=('governance',), selected='ki-delegation', limit=None):
    """8.2a: All guilds; the tree with Governance open and ki-delegation chosen."""
    return (_head(f'8 guilds · 65 skills in Knowledge Islands · from ki-agentic-harness · read {NOW}')
            + shield_bar(None, more_right=5) + g2_bar(SKILLS) + tree(open_, selected=selected, limit=limit, wide=False))


def page_chosen():
    """8.2c: the Governance shield chosen as a filter; the tray shut, so every column shows."""
    g = GBYID['governance']
    return (_head(f'13 of 65 skills · Governance · from ki-agentic-harness · read {NOW}')
            + shield_bar('governance', more_right=3) + g2_bar(g['skills'], chosen='governance') + tree(('governance',), only=('governance',)))


def page_scrolled():
    """8.2d: the bar scrolled to its end, All guilds frozen; Acquire, the seventh shield, chosen."""
    return (_head(f'4 of 65 skills · Acquire · from ki-agentic-harness · read {NOW}')
            + shield_bar('acquire', scroll=520, more_left=2) + g2_bar(GBYID['acquire']['skills'], chosen='acquire')
            + tree(open_=('acquire',), only=('acquire',)))


# 8.2b, the alternative: the shields as a vertical list beside a flat table of the chosen guild's skills.
def shield_list(chosen='governance', code='P2'):
    items = [f'<li class="g2li{" on" if chosen is None else ""}" data-g2guild="all">{g2shield("65", 0, 22, all_=True)}<span class="g2-nm">All guilds</span><span class="g2-ct">65</span></li>']
    items += [f'<li class="g2li{" on" if g["id"] == chosen else ""}" data-g2guild="{g["id"]}">{g2shield(g["mono"], g["hue"], 22)}'
              f'<span class="g2-nm">{escape(g["title"])}</span><span class="g2-ct">{len(g["skills"])}</span></li>' for g in GUILDS]
    return f'<nav class="g2list" {R(code, "Guilds, a list")}><ul>{"".join(items)}</ul></nav>'


def page_b():
    g = GBYID['governance']
    rows = ''.join(
        f'<tr class="g2s{" sel" if s["name"] == "ki-delegation" else ""}"><td class="mono nowrap">{s["name"]}</td>'
        f'<td class="g2-desc" title="{escape(s["desc"])}">{escape(s["desc"])}</td>'
        f'<td class="nowrap">{g2mark(s["kind"])} {s["kind"]}</td><td class="nowrap">{g2mark(s["appl"])} {s["appl"]}</td>'
        f'<td class="g2-dep nowrap">{_deps(s["deps"])}</td></tr>' for s in g['skills'])
    table = (f'<section class="panel tablepanel g2flat" {R("P4", "Governance skills, flat")}><table class="records g2t">'
             f'<colgroup><col class="c-name"><col class="c-desc"><col class="c-kind"><col class="c-appl"><col class="c-dep"></colgroup>'
             f'<thead><tr><th>Name</th><th>Description</th><th>ki-kind</th><th>ki-applicability</th><th>ki-depends-on</th></tr></thead>'
             f'<tbody>{rows}</tbody></table><p class="g2hidden muted">argument-hint and Runtimes are hidden at this width; Filter › Columns shows them.</p></section>')
    right = f'<div class="g2bcol">{g2_bar(g["skills"], chosen="governance")}{table}</div>'
    return (_head(f'13 of 65 skills · Governance · read {NOW}')
            + f'<div class="g2split">{shield_list()}{right}</div>')


def _window(content, tray=None, theme='night'):
    html = atlas_page('guilds', content, tray=tray, context=CTX_KI, theme=theme)
    return html.replace('</head>', CSS_LINK + '</head>', 1)


def ab_a(theme='night'):
    return _window(page_a(limit=7), tray=skill_tray(), theme=theme)


def ab_b():
    return _window(page_b(), tray=skill_tray())


def ab_c():
    return _window(page_chosen())


def ab_d():
    return _window(page_scrolled())


def ab_e():
    return _window(page_a(limit=7), tray=skill_tray(tab='references/'))


# ---------------------------------------------------------------- what plan.py and board.py read
PAGE = dict(
    id='8.2', title='Guilds, reworked', zones=['page', 'tray'],
    note='Kris\'s review of 8.1, which this page supersedes. The guilds and their 65 skills, read from each skills/<guild>/<skill>/SKILL.md '
         'in ki-agentic-harness, with a chosen skill read in the right tray. Three changes from 8.1: the guild shields sit in one bar '
         'that scrolls sideways, with All guilds frozen first so the way back never scrolls away; the skills are a two-level tree table '
         'whose columns are the SKILL.md front matter itself, under the same summary-filter bar as Roadmap and Jobs; and a skill opens in '
         'the tray, not the bottom pane, so Guilds uses the bottom pane nowhere. It matters because the front matter is what a person '
         'compares across skills (what kind, when it applies, what it leans on, how it is called, which runtimes), and a table lets them '
         'see it for every skill at once, while the shields keep 8.1\'s sense of a guild as a place. Until the guildmaster\'s catalogue '
         '(ki.reg.guilds) names the guilds, each harness folder stands in. The territory is the context control\'s. There is no brass '
         'action and no gold: nothing on this page waits on Kris.',
    fields=['Shield bar (P2): All guilds, frozen, with all 65 skills; then each guild\'s shield (monogram on its own colour), name and count; '
            'it scrolls sideways under a fade on each side that hides shields, and the bar\'s right end holds two chevrons and how many shields lie '
            'before and after; choosing a shield keeps that guild and adds a Guild chip',
            'Summary-filter bar (P3): tallies All skills; ki-kind (Governance, Process); ki-applicability (Baseline, Detected, Declaration-only, '
            'Invocation-only), each counting what the other filters keep; chips (the context\'s territory first, then the chosen guild); one '
            'Filter menu (runtimes, depends on, has references/, scripts/ or assets/, columns); words in a name or description; Group by Guild, ki-kind or None',
            'Tree table (P4): a guild row (fold chevron, shield, name, count, its about line and its mix of kinds) and its skills beneath, '
            'indented on a branch line: name (monospace), description (first clause, one line), ki-kind and ki-applicability (each a mark '
            'and its word), ki-depends-on (the first, then +N), argument-hint (monospace, one line), runtimes (ki-supported-runtimes, or any); '
            'a long guild shows its first seven and "Show N more"; with the tray open, argument-hint and Runtimes step out and the last header reads +2',
            'Right tray (T1), a skill chosen: Skill · its guild · its harness, its name; tabs (T2) SKILL.md, references/, scripts/ and assets/, '
            'each with how many files, an empty folder greyed; SKILL.md shows the front matter (T3) as keys and values, then the body drawn (T4); '
            'a folder tab lists its files with sizes and draws the chosen one; Open in a tab (page 6), Copy its path, Show in Roadmap',
            'No bottom pane on this page'],
)

ARTBOARDS = [
    dict(id='8.2a', page='8.2', title='Shields over a tree table: ki-delegation in the tray', make=lambda: ab_a(), zones=['page', 'tray'], preferred=True,
         why='The shields keep a guild a place you can pick at a glance, and frozen All guilds is always one click away however far the bar has '
             'scrolled. The tree puts every skill\'s front matter in columns, so "which skills are runtime-bound" or "what leans on ki-acquire" '
             'is read down a column, and folded guilds keep all eight in one window. The tray reads a skill without leaving the table, which '
             'is the shell rule for one chosen thing.',
         gains='One summary-filter bar across Roadmap, Jobs and Guilds; the front matter compares across skills; guilds fold to a line; no bottom '
               'pane, so the table keeps its full height; the bar holds any number of guilds in one row.',
         costs='With the tray open the table is about 820 points, so argument-hint and Runtimes step out (the tray shows both, and "+2" '
               'says so) and descriptions are cut to one line; shields past the fourth are a scroll away; a skill\'s body is read at 360 '
               'points, narrower than 8.1\'s pane.'),
    dict(id='8.2b', page='8.2', title='The shields as a list beside a flat table', make=lambda: ab_b(), zones=['page', 'tray'],
         gains='All nine choices seen at once with full names and counts, no scrolling; the table is one guild\'s skills with no guild rows to read past.',
         costs='The list takes 200 points from the table, so with the tray open argument-hint and Runtimes are hidden; two navigation columns sit '
               'side by side with the sidebar; skills of several guilds are never in one view; the shields lose their weight as places.'),
    dict(id='8.2c', page='8.2', title='8.2a with the Governance shield chosen: the tray shut, every column whole', make=lambda: ab_c(), zones=['page']),
    dict(id='8.2d', page='8.2', title='8.2a with the bar scrolled to its end: All guilds frozen, Acquire chosen', make=lambda: ab_d(), zones=['page']),
    dict(id='8.2e', page='8.2', title='8.2a with the references/ tab open in the tray', make=lambda: ab_e(), zones=['page', 'tray']),
]

COMPONENTS = [
    dict(id='8.2.1', page='8.2', title='Shield bar', selector='.g2bar',
         states=[('at rest, more to the right', '8.2a'), ('a shield chosen', '8.2c'), ('scrolled, All guilds frozen', '8.2d'),
                 ('a shield', '8.2c', '[data-g2guild="governance"]')]),
    dict(id='8.2.2', page='8.2', title='Tree row, guild and skill', selector='tr[data-g2row="governance"]',
         states=[('a guild, open', '8.2a'), ('a guild, folded', '8.2a', 'tr[data-g2row="change-management"]'),
                 ('a skill, chosen', '8.2a', 'tr[data-g2skill="ki-delegation"]'), ('a skill, plain', '8.2a', 'tr[data-g2skill="ki-git"]'),
                 ('a skill, runtime-bound', '8.2d', 'tr[data-g2skill="ki-acquire-chatgpt"]'), ('a long guild, Show 6 more', '8.2a', 'tr.g2more-row')]),
    dict(id='8.2.3', page='8.2', title='Skill in the right tray', selector='[data-region="T1"]',
         states=[('SKILL.md', '8.2a'), ('a folder tab, references/', '8.2e')]),
]


def extra_shots(mocks_dir):
    """The hidden shots 8.2 needs beyond its artboards: 8.2a in light."""
    path = os.path.join(mocks_dir, '8.2a-light.html')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(ab_a(theme='light'))
    return [dict(shot='8.2a-light', html=os.path.abspath(path), width=1440, hidden=True)]
