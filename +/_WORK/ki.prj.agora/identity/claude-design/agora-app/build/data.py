"""Illustrative data for the Agora app mock-ups, 6 November 2026.

ki.prj.agora's and ki.sop.main's focus areas and query ids come from their work packages on sol; the rest are
placeholders until the live roster supplies them.
"""

NOW = '04:20'

# Each agent: work id, title, Mac, territory, focus areas (primary first), listening, last answer, queries.
AGENTS = [
    dict(id='ki.prj.agora', title='KI › Techne › Agora', mac='sol', terr='ki',
         focus=['send', 'jobs', 'voice', 'identity', '_emerging'], listen='call', at='04:12', waits=10,
         first='AGORA-COUNT-PLACE, MARK-WORDS', short='agora'),
    dict(id='ki.sop.main', title='KI › SoP', mac='sol', terr='ki',
         focus=['themes', 'acceptance', 'chain', '_emerging'], listen='call', at='04:05', waits=18,
         first='CHEZMOI-HANDOVER, STOA-PROJECT', short='ki sop'),
    dict(id='personal.reg.inbox-sol', title='The assistant on sol', mac='sol', terr='personal',
         focus=['method', 'kiv', 'coordination'], listen='call', at='04:10', waits=3, first='Q21, Q37, Q38',
         short='inbox'),
    dict(id='personal.reg.household-sol', title='The household on sol', mac='sol', terr='personal',
         focus=['rig', 'install', 'settings'], listen='poll', at='04:01', waits=0, first='', short='household'),
    dict(id='personal.reg.watchman-sol', title='The watchman on sol', mac='sol', terr='personal',
         focus=['portal'], listen='call', at='04:10', waits=0, first='', short='watchman'),
    dict(id='personal.reg.inbox-terra', title='The assistant on terra', mac='terra', terr='personal',
         focus=['method', 'records'], listen='call', at='04:08', waits=1, first='FOOTER-OWNER', short='inbox'),
    dict(id='personal.reg.household-terra', title='The household on terra', mac='terra', terr='personal',
         focus=['rig', 'install'], listen='call', at='04:06', waits=0, first='', short='household'),
    dict(id='personal.reg.watchman-terra', title='The watchman on terra', mac='terra', terr='personal',
         focus=['portal'], listen='call', at='04:09', waits=0, first='', short='watchman'),
    dict(id='hnr.sop.main', title='HNR › SoP', mac='terra', terr='hnr', focus=['routing', 'acceptance'],
         listen='silent', at='02:10', waits=2, first='SITE-DOMAIN, P2MS3-DATES', short='hnr sop'),
    dict(id='hnr.prj.5g-emerge-phase3', title='HNR › 5G-EMERGE › Phase 3', mac='terra', terr='hnr',
         focus=['delivery', 'reporting'], listen='open', at='03:30', waits=0, first='', short='phase 3'),
    dict(id='hnr.prj.5g-emerge-p2ms3', title='HNR › 5G-EMERGE › P2MS3', mac='terra', terr='hnr',
         focus=['delivery'], listen='call', at='03:58', waits=0, first='', short='p2ms3'),
    dict(id='hnr.prj.site-robots', title='HNR › Site › Robots', mac='terra', terr='hnr', focus=['site', 'content'],
         listen='silent', at='02:10', waits=0, first='', short='robots'),
]

LISTEN_WORDS = {
    'call': ("Agora's call", 'answered {at}', 'stone'),
    'poll': ('Polling, 2 min', 'answered {at}', 'stone'),
    'open': ('On open', 'read {at}', 'hollow'),
    'silent': ('Silent', '2 calls unanswered since {at}', 'slashed'),
}

# ki.prj.agora's open queries, from its discussions.md (6 November 2026), with the focus each sits under.
AGORA_QUERIES = [
    ('AGORA-COUNT-PLACE', 'Where the group count goes when the identity design lands', 'identity', '2026-11-03', 'a'),
    ('AGORA-START', 'What follows the mark broadcast', 'send', '2026-11-03', 'a'),
    ('CONFIG-OWNER', "Who owns Agora's settings file", '_emerging', '2026-11-04', 'a'),
    ('ORCA-WATCH', 'Watch the Orca chat-send work for you', 'send', '2026-11-05', 'a'),
    ('WAKE-NOTE', "The wake architecture note, and Legal's request", 'send', '2026-11-06', 'a'),
    ('MARK-WORDS', 'Whether a mark carries your own words', 'send', '2026-11-06', 'a'),
    ('SCHED-FIRST', 'Which jobs move to Agora first', 'jobs', '2026-11-06', 'b'),
    ('SCHED-REPORT', 'How a failure or missed run reaches you', 'jobs', '2026-11-06', 'a'),
    ('SCHED-PAUSED', 'How a paused job is declared', 'jobs', '2026-11-06', 'a'),
    ('SCHED-ONE-RIG', 'Jobs that must run on exactly one Mac', 'jobs', '2026-11-06', 'a'),
]

SOP_QUERIES = [
    ('CHEZMOI-HANDOVER', 'Fold the chezmoi Project into the household works now', 'themes', '2026-11-04', 'a'),
    ('STOA-PROJECT', 'Open a Stoa Project in Knowledge Islands', 'themes', '2026-11-05', 'a'),
    ('RIG-LANE', 'Who carries Rig tooling once Mac Studio setup closes', 'themes', '2026-11-05', 'b'),
]

# What has been said in the last hour: time, from, to, kind, layer, words, heard.
SAID = [
    ('04:19', 'Kris', 'everyone', 'broadcast', 'talk', 'Away until 08:00: work within your existing authority', '11 of 12 heard'),
    ('04:17', 'ki.prj.agora', 'personal.reg.inbox-sol', 'message', 'durable', 'DESIGN-PACK sent to the information architect', 'heard 04:17'),
    ('04:12', 'Agora on sol', 'hnr.sop.main', 'call', 'talk', 'hnr-principal on terra is diverged: settle it', 'silent'),
    ('04:08', 'personal.reg.inbox-terra', 'ki.prj.agora', 'message', 'durable', 'MARK-ROLLOUT: terra has the new Agora', 'heard 04:09'),
    ('04:05', 'Kris', 'everyone', 'ping', 'talk', 'Ping', '8 answered, 2 silent'),
    ('04:01', 'Claude Design', 'ki.prj.agora', 'message', 'durable', 'DESIGN-2: the calmer tray menu is ready to look at', 'heard 04:02'),
    ('03:58', 'Claude Design', 'ki.prj.agora', 'message', 'durable', 'DESIGN-1: three architecture diagrams are ready', 'heard 03:59'),
    ('03:55', 'ki.prj.agora', 'Claude Design', 'message', 'durable', 'MSG-0aff84b9 PING: a round-trip test', 'answered 04:01'),
    ('03:50', 'Agora on sol', 'every agent', 'health', 'talk', 'Re-arm your listener (75 %)', '10 of 12 heard'),
    ('03:41', 'Agora on terra', 'Agora on sol', 'pushed', 'talk', 'krisb/inbox at 1a2b3c4', 'fetched 03:41'),
]

CHECKOUTS = [
    ('knowledgeislands/apps-agora.local', 'level', 'level'),
    ('knowledgeislands/ki-principal', 'level', 'behind 1, fast-forwarding'),
    ('knowledgeislands/ki-design', 'level', 'level'),
    ('hnr/hnr-principal', 'level', 'diverged: ahead 1, behind 2'),
    ('krisb/inbox', 'ahead 1, push it', 'level'),
    ('krisb/assistant', 'level', 'level'),
]
