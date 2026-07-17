# Magazine Update — The Map Is Not the Territory, but It Can Become a Guardrail

## MMALS enters Geometry G2

The first geometry phase of MMALS asked a deliberately uncomfortable question: are the elegant route plots and host clusters real scientific structure, or are they only attractive pictures? Geometry G1 therefore required more than visualization. A route geometry had to predict held-out contexts, survive shuffled null models, support targeted interventions, and improve a concrete objective under matched cost.

G2 starts only after that discipline. Its question is no longer simply, “Is there geometry?” It is:

> Can validated geometry constrain how the system learns, remembers, routes, and acts?

### Chronicle: history as an engineering object

Chronicle is often described as MMALS memory, but that word is too weak. Chronicle is the system's historical substrate. One layer keeps reconstructive evidence: inputs, inferred contexts, candidate routes, decisions, costs, calibration state, failures, model versions, and causal interventions. A second layer compiles repeated evidence into reusable macro-routes, each carrying a validity envelope.

That distinction matters. Evidence history must remain immutable. A compiled shortcut may be replaced or retired. The system can reinterpret old evidence under a new calibration model, but it must never rewrite what happened.

### The decisive external paper

Perez-Dattari and colleagues' 2026 paper, *Let the Dynamics Flow: Stable Flow Matching Dynamical Systems*, offers an engineering pattern that fits the next MMALS step. Their robot policies are expressive and multimodal, yet the generated velocities are constrained to remain inside admissible sets. They implement both soft constraints, which penalize unsafe directions, and hard constraints, which project the learned field back into the allowed region. They also extend the method to Lie groups, respecting the non-Euclidean geometry of orientation.

MMALS should not copy the robot model. It should copy the discipline:

> Do not learn any adaptation and check safety afterwards. Define which adaptation directions are admissible, then learn inside that space.

### Several maps, not one

G2 rejects the temptation to draw one universal context manifold. The system needs at least three relations:

1. Which contexts look geometrically close?
2. Which hosts are functionally substitutable?
3. Which contexts share valid calibration evidence?

These relations may disagree. Two contexts can be near in representation space but require different safety thresholds. Two hosts can be far in parameter space but implement the same function. A route can stay smooth while the host behind it changes function.

### The first G2 experiment

The next experiment is intentionally simple. Freeze the host bank. For each input, evaluate every admissible host and compare the selected host with the best available host. The difference is route regret. Record route confidence, host-function alignment, conformal set size, coverage, and calibration inflation.

This separates four failures:

- old function was forgotten;
- context was inferred incorrectly;
- the right host existed but the router missed it;
- calibration hid the defect by becoming conservative.

### Engineering promise

The long-term G2 architecture is an assurance layer around adaptation. A learned model may propose a route or update. Named constraints check retention, risk, cost, auditability, and evidence quality. A soft mode adds penalties. A hard mode rejects or projects the action. Chronicle records the proposal, the rejection or projection, the final action, and the evidence supporting it.

The goal is not a beautiful mathematical story. The goal is a continual learner whose evolution can be inspected, replayed, challenged, and bounded.

### Explained to a twelve-year-old

Imagine a school with several expert teams. The coordinator keeps a history book of which team solved each problem. Geometry is a set of maps showing which teams are similar and where each team is safe to use. The new paper describes a robot that can invent many movements but cannot move outside a safety fence. MMALS G2 asks whether learning itself can have a similar fence, so the system can keep learning without erasing important skills or taking unsafe shortcuts.


## What the internal review changed

A safety-looking gate can be dangerous when the estimates feeding it are wrong. The revised G2 snapshot therefore adds a second layer of uncertainty: not only must the prediction be calibrated, but the gate's estimates of retention, risk, cost, and audit visibility must also be qualified. The system may now answer `indeterminate` rather than pretending an estimated boundary is a known safety fence.

The update also makes the maturity of each geometric idea visible. The multi-space model is a G2 candidate; Lyapunov, Lie, Grassmann, Koopman, Euler-Poincare, and SFMDS transfers remain deferred hypotheses. The archive preserves them for research continuity without presenting them as committed architecture.

This magazine entry remains part of a private GitHub archive. A future public article should be written only after the failure modes and calibration gates have been tested experimentally.
