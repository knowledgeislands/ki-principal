# review-board-capture (blind review)

Independent review: you have not seen anyone's recommendation; give your own. Read nothing in any `+/_WORK/` folder.

Context: The ki-agentic-harness skill `ki-design-system` (`skills/design/ki-design-system/`) now has an annotated design board method with a shared in-page region collector, region codes and overlays (`scripts/annotate-board.ts`). Each site still writes its own browser steps: screenshots, switching components through states, publishing to its canvas. The harness already drives a system Chrome without Playwright inside `ki-diagrams`, private to that skill; sharing it means publishing a shared module touching a second skill. One site has a board so far.

Query: Should `ki-design-system` get its own plan-driven capture step now, or only once a second site adopts the board?

Options (unranked): add a capture step now, sharing the ki-diagrams Chrome driver; wait for a second site, then add capture by sharing the driver.

Answer with your choice, confidence (high/medium/low) and a two-line reason. Read-only; no commits.
