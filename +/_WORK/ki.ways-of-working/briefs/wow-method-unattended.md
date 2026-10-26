# wow-method-unattended

## Goal

Fold METHOD-UNATTENDED into the coordination method in the KI Agentic Harness, `/Users/krisbrown/workspaces/knowledge-islands/ki-agentic-harness`.

## Context

Routed from HNR > SoP (hnr), from hnr.sop.sites on 25 October 08:18 GMT. Kris's words: "If you ask me for input as well in an unattended period, you should only really ask it for a couple of minutes. And if I don't respond, then you should not take any action from it. That's also something they should learn about."

Proposed rule: in an unattended window a coordinator asks in plain text, never a blocking question prompt, waits about two minutes, and with no answer acts on nothing from it, parks the query and carries on.

## Scope

- In: the unattended-window rules in `skills/change-management/ki-coordination` (the coordinating-work standard and its output-style source) and `skills/delegation/ki-delegation` where it states unattended limits; regenerate the rendered surfaces with `ki dev skill generate ki-coordination --write` (and ki-delegation if it has one); update the sources review; run the skill tests and `ki repo audit` for the touched skills.
- Keep the rule short, in Kris's words with the date, beside the existing unattended-window text. Use blank-line-separated paragraphs (the FORM-VS-RUMDL form wow-hooks-form has just landed).
- Out: tools-ki, chezmoi, Claude settings, any other repository. If the CLI needs a change, say so in the report; do not make it.

## Authority

Commit by explicit path with a Conventional Commit, push fast-forward only, never force or `--no-verify`; stop on divergence. Another session may be committing in the harness: pull with rebase first and leave its files alone.

## Report

Owner report: Done, In Progress, Queries (Context, Query, Options, recommended first with confidence). Name the harness commit.
