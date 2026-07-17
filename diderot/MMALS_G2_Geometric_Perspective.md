# Diderot Entry — MMALS G2 Geometric Perspective

**Status:** Internal research snapshot v0.2 - not for external publication  
**Date:** 2026-07-17  
**Parent entries:** Geometry-MMALS G1; MMALS-TPUT; MMALS Chronicle; MMALS-CAL  
**Primary trigger paper:** Perez-Dattari et al., *Let the Dynamics Flow: Stable Flow Matching Dynamical Systems* (arXiv:2606.03834v2).

## Core proposition

MMALS G2 studies whether inferred contexts, routes, host functions, memory states, audit distributions, and calibration states can be represented by coupled geometric objects whose distances, tangent directions, transport maps, and admissible regions improve continual-system decisions under matched budgets.

G2 does **not** claim that learning trajectories are physical trajectories. It imports one disciplined engineering pattern from SFMDS: expressive learned dynamics can be restricted to an admissible solution set, either softly through penalties or hard by architectural projection.

## Concept graph

- **Continual learning** supplies stability–plasticity and sequential evaluation.
- **Chronicle** supplies typed history, immutable reconstructive evidence, and compiled functional memory.
- **Context inference** supplies `q(c|x,m)` without requiring task identity at runtime.
- **RC2O / TPUT** makes routes first-class, goal- and budget-conditioned objects.
- **Geometry G1** qualifies whether internal order is predictive, causal, and operational.
- **Geometry G2** controls adaptation using validated geometric objects and admissible transitions.
- **MMALS-CAL** gates action under uncertainty, but does not constitute a complete safety proof.

## Multi-space model

1. Observation space `X`
2. Context manifold `M_C`
3. Route space `M_R`
4. Functional quotient space `M_F`
5. Audit-distribution space `M_A`
6. Calibration space `M_cal`

The key warning is:

`G_function != G_geometry != G_calibration`

A single universal context manifold is not assumed.

## Chronicle relation

Chronicle is a typed historical graph, not a replay buffer. It separates:

- `M_R`: reconstructive evidence memory;
- `M_S`: compiled macro-routes with validity envelopes.

Geometric lifecycle operations include reuse, transport, merge, repurpose, retirement, and capacity allocation. Every operation must preserve provenance and expose irreversible loss.

## SFMDS transfer

SFMDS learns expressive multimodal dynamics while restricting velocities to admissible sets derived from positive invariance and Lyapunov conditions.

MMALS translation:

- robot velocity → route/lifecycle adaptation direction;
- admissible velocity set → admissible adaptation cone;
- soft stability loss → retention/risk/cost/audit penalty;
- hard projection → structural rejection or projection of an unsafe update;
- latent Lyapunov function → candidate distance to an acceptable operational set.

## Candidate G2 diagnostics

- counterfactual route regret;
- route–function alignment drift;
- calibration inflation after misrouting;
- context-specific versus robust multi-context CAL;
- representation versus plasticity saturation;
- audit blind directions through the kernel of the observation map.

## Immediate experiment

Do not add a manifold architecture. Freeze the current host bank and evaluate every admissible host per sample. Record selected-host loss, best-host loss, route regret, context confidence, calibration set size, coverage, inflation, and intervention outcomes.

## Falsification

Reject a G2 mechanism when:

- it improves visual organization but not function;
- it reduces drift by blocking new learning;
- it performs no better than Euclidean or shuffled-geometry controls;
- calibration compensates by becoming excessively conservative;
- the geometric object is unstable across seeds or reparameterizations;
- hard projection removes useful adaptation without safety benefit.

## Twelve-year-old explanation

MMALS is like a school with specialist teams and a coordinator. Chronicle is the history book. Geometry is several maps: who understands similar things, who is safe for a problem, and which shortcuts can be reused. The SFMDS paper teaches that a robot may invent many movements while a safety fence blocks dangerous directions. G2 asks whether learning steps can have a similar evidence-based fence.


## Meta-calibration addition

The admissibility layer consumes uncertain estimators. G2 therefore distinguishes the true admissible set `A*` from the estimated set `A_hat_(1-alpha)`. Every gate input must expose an uncertainty object and calibration contract. Gate outcomes are `admissible`, `inadmissible`, or `indeterminate`; insufficient evidence is never silently converted into permission.

Key qualification metrics are false admissibility, gate regret, boundary bias, bootstrap route-decision instability, and drift response. A nominal hard gate is demoted to a soft advisory or abstention rule when these tests fail.

## Private publication note

This entry freezes the current research state. The external specification should be rebuilt after G2-0 instrumentation, route-function estimator qualification, CAL-compatible failure-injection studies, and meta-calibration gates. Detailed phases P0-P9 and release gates R0-R9 are recorded in `docs/PRIVATE_PUBLICATION_AND_GATE_PLAN.md`.
