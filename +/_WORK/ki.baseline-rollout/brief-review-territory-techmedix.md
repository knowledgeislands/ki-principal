# Brief - review-territory-techmedix

Blind query review for KI > Foundations > Baseline rollout (`ki.baseline-rollout`), under the `ki-coordination` standard's Query review section. You are reviewing one query before it reaches Kris. Check what you can directly by reading; write nothing in any repository and make no network call beyond read-only Git or GitHub metadata.

## The query

### TERRITORY-TECHMEDIX - Techmedix audit stops on an archived, unregistered member

**Context:** `ki territory audit -t techmedix` exits 2 because the Capital declares `techmedix/apps-childhealthyorkshire.co.uk`, which Known Lands calls archived read-only, and that repository has no local clone or registration. So the whole territory gets no audit at all. HNR's Known Lands states the territory principle that "Local unavailability does not remove an inventoried island", and this failure goes against it.

**Query:** How should the Techmedix audit be unblocked?

**Options:**

- Hand a record to tools-ki asking territory audit and show to report an unregistered declared member as a finding and carry on, rather than failing. Leave the declaration as it is.
- Clone the archived repository locally and register it, which needs a network fetch and a registration run.
- Take it out of `territory_members` in tmx-principal through its Enactment Process, keeping it in Known Lands as archived.

## Report

Return a run report in the `ki-coordination` run-report form with one query, TERRITORY-TECHMEDIX, carrying your own recommended option first as `a) (recommended, confidence <high|medium|low> - <one-line reason>)`, the other options beneath, and under Done one line per thing you verified directly.

Authority: read-only across all repositories; no commits, no pushes, no registration, no writes outside the run's state folder; never run `ki repo conform`.
