"""Builds the design pack's pages from plan.json and the measured regions: one HTML page per part, an index page,
index.md and board.json. Run after plan.py and shoot.js.
"""
import re
import json
import os
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')
STAMP = '2026-11-06'
SOURCE = 'mock-ups from build/plan.py; not yet built'

ZONE_OF = {'N': 'navigation', 'T': 'tray', 'P': 'page'}

CSS = '''
:root { --paper:#f5efe0; --ink:#1a2030; --muted:#4a5568; --accent:#1b3a5c; --teal:#317070; --warn:#8a5a12; --rule:#d4c9b4;
  --boundary:#9a8358; --surface:#eef1f5; --gold:#c8963c; --wash-warn:#f1e8d3;
  --zone-navigation:#317070; --zone-tray:#1b3a5c; --zone-page:#8a5a12; }
* { box-sizing:border-box; }
body { margin:0; background:var(--paper); color:var(--ink); font:14px/1.5 -apple-system, BlinkMacSystemFont, Inter, "Segoe UI", sans-serif; }
.wrap { max-width:1560px; margin:0 auto; padding:24px 32px 64px; }
nav.crumbs { font-size:13px; color:var(--muted); margin-bottom:8px; }
nav.crumbs a { color:var(--accent); }
h1 { font-size:24px; margin:0 0 6px; font-weight:600; }
h2 { font-size:18px; margin:32px 0 10px; font-weight:600; }
.note { max-width:900px; }
.stamp { color:var(--muted); font-size:12px; }
.fields { max-width:900px; margin:10px 0 0; padding-left:18px; }
.fields li { margin:2px 0; }
.toggle { display:inline-flex; gap:6px; align-items:center; font-size:13px; color:var(--muted); margin-top:14px; }
figure.ab { margin:28px 0 0; }
figure.ab > header { display:flex; align-items:baseline; gap:12px; flex-wrap:wrap; margin-bottom:8px; }
figure.ab h3 { font-size:16px; margin:0; font-weight:600; }
.pref { display:inline-block; background:var(--gold); color:var(--ink); font-weight:600; font-size:12px; padding:2px 8px; border-radius:10px; }
figure.ab.preferred .frame { outline:3px solid var(--gold); outline-offset:4px; }
.tradeoff { display:grid; grid-template-columns:repeat(3, minmax(0, 1fr)); gap:16px; max-width:1440px; margin:0 0 10px; font-size:13px; }
.tradeoff div { border-top:2px solid var(--rule); padding-top:6px; }
.tradeoff .why { border-top-color:var(--gold); }
.tradeoff b { display:block; font-size:12px; color:var(--muted); }
.frame { position:relative; display:inline-block; max-width:100%; border:1px solid var(--rule); background:#0f2440; }
.frame img { display:block; max-width:100%; height:auto; }
.ov { position:absolute; border:1.5px dashed; border-radius:3px; }
.ov .badge { position:absolute; top:-1px; right:-1px; transform:translateY(-100%); font-size:11px; font-weight:600; color:var(--paper);
  padding:1px 6px; border-radius:3px 3px 0 0; white-space:nowrap; }
.ov.whole .badge { top:auto; bottom:-1px; transform:translateY(100%); border-radius:0 0 3px 3px; }
.ov.navigation { border-color:var(--zone-navigation); } .ov.navigation .badge { background:var(--zone-navigation); }
.ov.tray { border-color:var(--zone-tray); } .ov.tray .badge { background:var(--zone-tray); }
.ov.page { border-color:var(--zone-page); } .ov.page .badge { background:var(--zone-page); }
body.plain .ov { display:none; }
.legend { font-size:12px; color:var(--muted); margin-top:6px; }
.comps { display:grid; grid-template-columns:repeat(auto-fill, minmax(320px, 1fr)); gap:20px; }
.comp h4 { margin:0 0 6px; font-size:14px; }
.comp .states { display:flex; gap:12px; flex-wrap:wrap; align-items:flex-start; }
.comp figure { margin:0; }
.comp figcaption { font-size:12px; color:var(--muted); margin-top:4px; }
.comp img { display:block; border:1px solid var(--rule); max-width:300px; }
table.idx { border-collapse:collapse; width:100%; max-width:1200px; }
table.idx th, table.idx td { text-align:left; padding:6px 10px; border-bottom:1px solid var(--rule); vertical-align:top; }
table.idx th { font-size:12px; color:var(--muted); }
a { color:var(--accent); }
'''


def overlay(ab, shot, zones):
    size = shot['size']
    out = []
    for r in shot['regions']:
        zone = ZONE_OF[r['code'][0]]
        if zone not in zones or r['w'] < 12 or r['h'] < 8:
            continue
        whole = r['code'][1:] == '0'
        x, y, w, h = r['x'], r['y'], r['w'], r['h']
        style = (f'left:{100 * x / size["w"]:.3f}%;top:{100 * y / size["h"]:.3f}%;'
                 f'width:{100 * w / size["w"]:.3f}%;height:{100 * h / size["h"]:.3f}%')
        label = f'{r["code"]} · {r["label"]}'
        out.append(f'<div class="ov {zone}{" whole" if whole else ""}" style="{style}" data-region="{ab["id"]} {r["code"]}" '
                   f'title="{escape(ab["id"] + " " + label)}"><span class="badge">{escape(label)}</span></div>')
    return ''.join(out)


def coded(ab, shot, zones):
    return [dict(code=r['code'], label=r['label'], x=r['x'], y=r['y'], w=r['w'], h=r['h'])
            for r in shot['regions'] if ZONE_OF[r['code'][0]] in zones]


def page_html(pg, abs_, comps, regions, pages):
    i = [p['id'] for p in pages].index(pg['id'])
    prev = pages[i - 1] if i else None
    nxt = pages[i + 1] if i + 1 < len(pages) else None
    crumbs = (f'<a href="index.html">The pack</a>'
              + (f' · previous <a href="{prev["id"]}.html">{prev["id"]} {escape(prev["title"])}</a>' if prev else '')
              + (f' · next <a href="{nxt["id"]}.html">{nxt["id"]} {escape(nxt["title"])}</a>' if nxt else ''))
    fields = ''.join(f'<li>{escape(f)}</li>' for f in pg['fields'])
    figs = []
    for ab in abs_:
        shot = regions[ab['id']]
        pref = ab.get('preferred')
        trade = ''
        if 'gains' in ab:
            why = f'<div class="why"><b>Why this one</b>{escape(ab["why"])}</div>' if pref else '<div></div>'
            trade = (f'<div class="tradeoff">{why}<div><b>Gains</b>{escape(ab["gains"])}</div>'
                     f'<div><b>Costs</b>{escape(ab["costs"])}</div></div>')
        badge = '<span class="pref">Preferred</span>' if pref else ''
        figs.append(f'''<figure class="ab{" preferred" if pref else ""}" id="{ab["id"]}">
<header><h3>{ab["id"]} · {escape(ab["title"])}</h3>{badge}</header>{trade}
<div class="frame" style="width:{shot["size"]["w"]}px"><img src="shots/{ab["id"]}.png" alt="{escape(ab["id"] + " " + ab["title"])}" width="{shot["size"]["w"]}" height="{shot["size"]["h"]}">{overlay(ab, shot, ab["zones"])}</div>
</figure>''')
    comp_html = ''
    if comps:
        items = []
        for c in comps:
            states = ''.join(
                f'<figure><img src="shots/components/{c["id"]}-{re.sub(r"[^a-z0-9]+", "-", state, flags=re.I).lower()}.png" alt="{escape(c["title"] + ", " + state)}"><figcaption>{escape(state)}</figcaption></figure>'
                for state, _ in c['states'])
            items.append(f'<div class="comp" id="{c["id"]}"><h4>{c["id"]} · {escape(c["title"])}</h4><div class="states">{states}</div></div>')
        comp_html = f'<h2>Components</h2><div class="comps">{"".join(items)}</div>'
    if light := (pg['id'] == '1'):
        shot = regions['1a-light']
        figs.append(f'''<figure class="ab" id="1a-light"><header><h3>1a, in light</h3><span class="stamp">the same artboard; night is the reference rendering</span></header>
<div class="frame" style="width:{shot["size"]["w"]}px"><img src="shots/1a-light.png" alt="1a in light" width="{shot["size"]["w"]}" height="{shot["size"]["h"]}"></div></figure>''')
    zones = sorted({z for ab in abs_ for z in ab['zones']})
    zone_words = {'navigation': 'N, navigation (teal)', 'tray': 'T, the tray (blue)', 'page': 'P, page content (brass)'}
    return f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{pg["id"]} {escape(pg["title"])} · Agora app</title><style>{CSS}</style></head>
<body><div class="wrap">
<nav class="crumbs">{crumbs}</nav>
<h1>{pg["id"]} · {escape(pg["title"])}</h1>
<p class="note">{escape(pg["note"])}</p>
<p class="stamp">Refreshed {STAMP} · source: {SOURCE}</p>
<b>What it shows</b><ul class="fields">{fields}</ul>
<label class="toggle"><input type="checkbox" onclick="document.body.classList.toggle('plain', this.checked)"> Hide the region boxes</label>
<p class="legend">Region codes: {"; ".join(zone_words[z] for z in zones)}. Quote them as "{abs_[0]["id"]} {"P" if "page" in zones else "N" if "navigation" in zones else "T"}2".</p>
{"".join(figs)}
{comp_html}
</div></body></html>'''


def main():
    plan = json.load(open(os.path.join(HERE, 'plan.json'), encoding='utf-8'))
    regions = json.load(open(os.path.join(ROOT, 'shots', 'regions.json'), encoding='utf-8'))
    pages = plan['pages']
    board = dict(stamp=STAMP, source=SOURCE, pages=[])
    rows = []
    md_rows = []
    for pg in pages:
        abs_ = [ab for ab in plan['artboards'] if ab['page'] == pg['id']]
        comps = [c | dict(title=next(x['title'] for x in COMPONENT_TITLES if x['id'] == c['id'])) for c in plan['components'] if c['id'].startswith(pg['id'] + '.')]
        with open(os.path.join(ROOT, f'{pg["id"]}.html'), 'w', encoding='utf-8') as f:
            f.write(page_html(pg, abs_, comps, regions, pages))
        board['pages'].append(dict(id=pg['id'], title=pg['title'], artboards=[
            dict(id=ab['id'], title=ab['title'], image=f'shots/{ab["id"]}.png', size=regions[ab['id']]['size'],
                 preferred=bool(ab.get('preferred')), regions=coded(ab, regions[ab['id']], ab['zones'])) for ab in abs_],
            components=[dict(id=c['id'], title=c['title'], states=[s for s, _ in c['states']]) for c in comps]))
        alts = ', '.join(f'<a href="{pg["id"]}.html#{ab["id"]}">{ab["id"]}</a>{" ★" if ab.get("preferred") else ""} {escape(ab["title"])}' for ab in abs_)
        rows.append(f'<tr><td><a href="{pg["id"]}.html">{pg["id"]}</a></td><td>{escape(pg["title"])}</td><td>{alts}</td><td>{len(comps) or ""}</td></tr>')
        for ab in abs_:
            md_rows.append(f'| [{ab["id"]}]({pg["id"]}.html#{ab["id"]}) | {pg["title"]} | {ab["title"]} | {"preferred" if ab.get("preferred") else "alternative" if "gains" in ab else "state"} | [shot](shots/{ab["id"]}.png) |')
        for c in comps:
            md_rows.append(f'| [{c["id"]}]({pg["id"]}.html#{c["id"]}) | {pg["title"]}, components | {c["title"]}: {", ".join(s for s, _ in c["states"])} | component | [shots](shots/components/) |')
    with open(os.path.join(ROOT, 'board.json'), 'w', encoding='utf-8') as f:
        json.dump(board, f, indent=2, ensure_ascii=False)
    index = f'''<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agora app · design pack</title><style>{CSS}</style></head><body><div class="wrap">
<h1>Agora app · design pack</h1>
<p class="note">The rich Electron app beside the tray (DESIGN-PACK, Kris about 05:40 GMT). It first shows what is happening within each Agora and across them; later it takes in the KIV's inbox and the Observatory's insight. One page per part, in the app's own order: the shell and tray first, then home, then each view. Where a page has alternatives, they are lettered and the preferred one is outlined in brass with its reason.</p>
<p class="stamp">Refreshed {STAMP} · source: {SOURCE} · night is the reference rendering</p>
<table class="idx"><thead><tr><th>Page</th><th>Part</th><th>Artboards (★ preferred)</th><th>Components</th></tr></thead><tbody>{"".join(rows)}</tbody></table>
<p class="stamp">Read the <a href="README.md">README</a> for the choices and what is open.</p>
</div></body></html>'''
    with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index)
    with open(os.path.join(HERE, 'artboards.md.part'), 'w', encoding='utf-8') as f:
        f.write('| Artboard | Page | What | Kind | Image |\n| --- | --- | --- | --- | --- |\n' + '\n'.join(md_rows) + '\n')
    print(f'{len(pages)} pages')


COMPONENT_TITLES = [
    dict(id='0.1.1', title='Brand'), dict(id='0.1.2', title='Views'), dict(id='0.1.3', title='Speak to everyone'),
    dict(id='0.1.4', title='The portal'), dict(id='0.1.5', title='Tabs'), dict(id='0.2.1', title='Summary lines'), dict(id='0.2.2', title='Exception row'),
    dict(id='0.2.3', title='Speak to everyone'),
]

if __name__ == '__main__':
    main()
