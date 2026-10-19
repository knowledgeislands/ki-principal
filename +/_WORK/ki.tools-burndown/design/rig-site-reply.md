# Reply to the rig.midnight.ninja design handoff

Draft reply for RIG-SITE-CONFIG, under SITE-CONFIG-PREMISE a) (Kris, 19 October 2026), drawn from the [Rig site configuration design note](rig-site-config.md). Kris passes it on; nothing here has been sent.

```text
Thanks for the handoff on showing per-host configuration (Ask A) and the optional acquisition kind (Ask B). Here is where things stand from the Rig side.

1. With today's data the "own config" cell would read the same on terra and sol

We checked what is actually declared. Every tool's "own config" answer would currently be identical on both Macs: anything configured is either common to both machines, or concerns a tool that is only on the laptop anyway, so the tool column already shows the difference. The idea that the two Macs differ mainly through configuration does not hold for what is declared today. It may change once Kris declares genuinely host-specific configuration, but there is no date for that.

So the decision is yours: ship the cell now, knowing both columns will match for the time being, or hold it until there is a real difference to show.

2. The shape Rig is likely to provide (provisional, not yet agreed or built)

- Rig would own the meaning of "configured", rather than the site working it out.
- Each piece of configuration could name the tool it is about, as a "tool" link.
- In the per-profile JSON from `rig show`, every tool entry would carry a "configured_by" list: the configuration items that configure it in that profile, empty when none.
- The site would reduce that list to a yes or no per tool and host, and publish only the yes or no, as you proposed. The public export would not change.

Please treat field names and details as provisional until a Rig record is captured and delivered.

3. A published schema for Rig's JSON output (wanted, not yet decided)

Kris wants Rig to publish a schema for its JSON output, so you can see what data is where without reading Rig's code. Today only the text form of `rig show` is specified, and the JSON the site already reads has no written contract. Whether and how this happens is not decided yet; we will tell you when it is.

4. Ask B stays parked

We are not widening the public export with an acquisition kind for now. If you want it, ask, and we will pick it up then.

5. Two things to be aware of

- Placeholder rationales: many tools still carry a stock "retain the explicit package choice" rationale. This is fixed in Kris's own Rig configuration data, not in Rig or the site, and that work is on hold for Kris's decisions, with a review date of 7 November. The site already recognises these placeholders, so nothing is needed from you.
- vega has no public view: vega's Rig configuration has no public view, so it cannot feed the site the way the Macs do. That is fixed in the agent-host setup that configures vega, as part of moving its tools onto Rig, which is on hold. Until then the hand-written vega entry on the site stays as it is.
```
