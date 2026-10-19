import { patterns } from './assets/design.ts'
import type { Instrument } from './instrument.ts'
import { VOICE } from './voice.ts'

/**
 * The Known Lands chart: every territory in scope drawn as an archipelago with its declared
 * Capital, and the repositories in no territory as one more.
 *
 * This is the minimal chart VIS-030-MINIMAL put in place while Kris designs the real one, so it is
 * kept to two parts the designs can replace without rework. The chart is an image the backend
 * draws with the vendored renderer and serves under the SVG policy, so the page trusts none of
 * its markup. Beside it, the islands are listed as text, each linking to its row in the
 * Repositories view, which is what a reader of the image and a reader of the page can both follow.
 *
 * Nothing is placed, raised, or written: the layout is the renderer's own, and the chart
 * contributes no signal to the Beacon.
 */

const STYLE = `
#known-lands { overflow: auto; padding: 0 var(--gutter) var(--space-5); }
#known-lands #known-lands-state { margin: var(--space-5) 0; font-size: var(--text-sm); color: var(--muted); }
#known-lands #known-lands-state.warn { color: var(--warn); }
#known-lands #known-lands-chart { display: block; max-width: 100%; height: auto; margin-bottom: var(--space-5); }
#known-lands section { margin: 0 0 var(--space-5); }
#known-lands h3 { margin: 0; font-size: var(--text-sm); }
#known-lands p { margin: 0; font-size: var(--text-xs); color: var(--muted); }
#known-lands p.warn { color: var(--warn); }
#known-lands ul { margin: var(--space-1) 0 0; padding: 0; list-style: none; display: flex; flex-wrap: wrap;
  gap: 0 var(--space-5); font-family: var(--font-identifier); font-size: var(--text-xs); }
${patterns('#known-lands')}
`

const MARKUP = `<p id="known-lands-state">not yet observed</p>
<img id="known-lands-chart" alt="" hidden>
<div id="known-lands-islands"></div>`

export const KNOWN_LANDS_VIEWER = `
const REPORT = 'observatory/known-lands/v1'

const stateLine = document.getElementById('known-lands-state')
const chart = document.getElementById('known-lands-chart')
const lists = document.getElementById('known-lands-islands')

let report = null
let scope = null
let active = false
${VOICE}
const query = () => '?scope=' + encodeURIComponent(scope || 'estate')
const islandsOf = (body) => new Set(body.archipelagos.flatMap((archipelago) => archipelago.islands)).size
const unreadOf = (body) => body.archipelagos.filter((archipelago) => archipelago.reason !== null).length
const observed = () => paneObserved(report.observedAt, islandsOf(report), unreadOf(report))
const repositoryName = (identity) => identity.split('/').pop()

// Each island opens its own row in the Repositories view, as a real address a reader can also open
// in a new tab.
const islandAddress = (identity) => query() + '&view=repositories&filter.repository=' + encodeURIComponent(identity)

const capitalLine = (archipelago) => {
  if (archipelago.declaredCapital === null) return 'no Capital is declared for these'
  if (archipelago.capital === null) return 'Capital ' + archipelago.declaredCapital + ', not in this scope'
  return 'Capital ' + repositoryName(archipelago.capital)
}

const line = (text, warn) => {
  const added = document.createElement('p')
  added.textContent = text
  if (warn) added.className = 'warn'
  return added
}

const paintArchipelago = (archipelago, unread) => {
  const section = document.createElement('section')
  section.setAttribute('data-archipelago', archipelago.territory === null ? '' : archipelago.territory)
  const heading = document.createElement('h3')
  heading.textContent = archipelago.label
  section.append(heading)
  if (archipelago.reason !== null) {
    section.append(line('could not be read: ' + archipelago.reason, true))
    return section
  }
  section.append(line(capitalLine(archipelago), false))
  // Unread territories' repositories cannot be told apart from these, so they may be among them.
  if (archipelago.territory === null && unread)
    section.append(line('may include repositories of a territory that could not be read', false))
  const list = document.createElement('ul')
  for (const identity of archipelago.islands) {
    const item = document.createElement('li')
    const link = document.createElement('a')
    link.href = islandAddress(identity)
    link.textContent = identity
    link.title = 'open in the Repositories view'
    if (identity === archipelago.capital) item.setAttribute('data-capital', 'true')
    item.append(link)
    list.append(item)
  }
  section.append(list)
  return section
}

const paint = () => {
  const unread = unreadOf(report)
  const islands = islandsOf(report)
  stateLine.textContent = report.archipelagos.length
    ? 'the chart is the renderer\\u2019s fixed layout; every island is listed below it'
    : 'no repository in this scope to chart'
  stateLine.classList.toggle('warn', false)
  if (report.archipelagos.length) {
    chart.alt = 'Known Lands chart of ' + report.archipelagos.length + ' archipelagos; each is listed below it'
    chart.src = '/api/known-lands/svg' + query() + '&at=' + encodeURIComponent(report.observedAt)
    chart.hidden = false
  } else {
    chart.hidden = true
    chart.removeAttribute('src')
  }
  lists.replaceChildren(...report.archipelagos.map((archipelago) => paintArchipelago(archipelago, unread)))
  headline(report.archipelagos.length + ' archipelagos \\u00b7 ' + islands + ' repositories' +
    (unread ? ' \\u00b7 ' + unread + ' territor' + (unread === 1 ? 'y' : 'ies') + ' unread' : ''))
}

chart.addEventListener('error', () => {
  chart.hidden = true
  stateLine.textContent = 'the chart could not be drawn; every island is still listed below'
  stateLine.classList.toggle('warn', true)
})

// Each read is numbered, and only the latest asked is kept, so a slower answer for a scope no
// longer chosen is dropped when it lands.
let reading = 0

const load = async () => {
  const mine = ++reading
  speak('reading Known Lands in ' + (scope || 'estate') + '\\u2026')
  const done = window.__shell.loading('known-lands', Boolean(report))
  try {
    const answer = await fetch('/api/known-lands' + query(), { headers: { accept: 'application/json' } })
    const body = await answer.json()
    if (mine !== reading) return
    if (body.schema !== REPORT) throw new Error(body.reason || 'unrecognised Known Lands schema')
    report = body
    paint()
    observed()
  } catch (error) {
    if (mine !== reading) return
    stateLine.textContent = 'could not read Known Lands: ' + error.message
    stateLine.classList.toggle('warn', true)
    paneUnobserved('could not read Known Lands: ' + error.message)
  } finally {
    done()
  }
}

// A scope change returns this view to how it stood before its first read, so nothing of the
// previous scope is shown while the new one is read.
const forget = () => {
  reading += 1
  report = null
  stateLine.textContent = ''
  stateLine.classList.toggle('warn', false)
  chart.hidden = true
  chart.removeAttribute('src')
  lists.replaceChildren()
  if (active) headline('')
}

window.__instruments['known-lands'] = {
  selectScope: (chosen) => {
    if (!chosen || chosen === scope) return
    scope = chosen
    forget()
    if (active) load()
  },
  activate: () => { active = true; if (report) { paint(); observed() } else load() },
  deactivate: () => { active = false },
  refresh: () => load(),
  arrange: () => { if (report) paint() }
}
`

export const knownLandsInstrument: Instrument = {
  summary: {
    id: 'known-lands',
    title: 'known lands',
    summary: 'Each territory in scope as an archipelago around its Capital, and the repositories in no territory',
    subject: 'scope',
    availability: 'available',
    roadmap: 'KI-OBSERVA-VIS-030',
    dimensions: [],
    defaultGrouping: null
  },
  style: STYLE,
  narrow: [],
  markup: MARKUP,
  skeleton: 'graph',
  script: KNOWN_LANDS_VIEWER
}
