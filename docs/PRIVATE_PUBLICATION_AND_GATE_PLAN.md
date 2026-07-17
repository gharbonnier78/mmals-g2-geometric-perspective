# Private publication recommendation and CAL-compatible gate plan

**Status:** Guillaume-only internal archive  
**Version:** v0.2-internal, 17 July 2026  
**External publication:** Not approved

This document mirrors the private chapter of the LaTeX paper and exists for rapid context recovery.

## Recommendation

Keep the current repository as an internal research snapshot. The eventual external specification should be rebuilt from verified evidence, not by expanding the present conditional formalism.

The strongest future contribution is the empirical separation of:

1. retained host competence;
2. autonomous context inference;
3. route misallocation;
4. host-functional drift;
5. calibration compensation or inflation;
6. uncertainty of the gate estimators themselves.

Geometry becomes a publishable mechanism only when it predicts or improves these phenomena beyond simpler alternatives under matched cost.

## Action plan

- **P0 - Freeze and provenance:** tag, hash, source manifest, evidence-status labels.
- **P1 - G2-0 instrumentation:** exhaustive host audit, route regret, functional probes, CAL diagnostics.
- **P2 - Estimator qualification:** uncertainty bands and nested calibration for retention, risk, cost, and audit-visibility estimators.
- **P3 - Route-function study:** compare intervention, Jacobian, and counterfactual estimators.
- **P4 - CAL-compatible verification:** global, oracle-context, inferred-context, and robust multi-context CAL under injected routing and host failures.
- **P5 - Meta-calibration:** false admissibility, gate regret, boundary bias, bootstrap decision instability, drift.
- **P6 - Soft constraints:** matched-budget comparison against non-geometric controls and CL baselines.
- **P7 - Hard projection:** only after calibrated estimators and demonstrated soft benefit.
- **P8 - Cross-benchmark replication:** SplitCIFAR, CORe50, and an engineering stream.
- **P9 - External specification:** validated core first; candidate and deferred mathematics visibly separated.

## Mandatory release gates

| Gate | Requirement | Current status |
|---|---|---|
| R0 | Clean reproducible build and immutable artifacts | Partial |
| R1 | Diagnostics recover injected failures | Pending |
| R2 | Gate estimators meet calibration contract | Pending |
| R3 | False admissibility and gate regret below frozen limits | Pending |
| R4 | Failure modes separable | Pending |
| R5 | Operational gain at matched budget | Pending |
| R6 | Indeterminate and fallback behaviour validated | Pending |
| R7 | Cross-stream and cross-seed robustness | Pending |
| R8 | Chronicle and claim-manifest completeness | Partial |
| R9 | CL, calibration, geometry, and systems reviews closed | Pending |

A failed gate changes the claim level. It does not justify silently weakening the test.
