# G2 Engineering Architecture

## Components

1. Context Inferer
2. Route Generator
3. Named Energy Evaluator
4. Admissibility Projector
5. Host Executor
6. MMALS-CAL Service
7. Chronicle Reconstructive Store
8. Chronicle Compiled Memory Registry
9. Counterfactual Auditor
10. Lifecycle Manager

## Deterministic boundaries

- schema validation;
- route and evidence versioning;
- hard policy constraints;
- provenance and claim manifest;
- replay and reconstruction;
- irreversible-action approval.

## Learned boundaries

- context posterior;
- host capability estimate;
- route utility;
- drift and saturation estimate;
- conformity score;
- optional transport map.

## Core event

```json
{
  "input_ref": "...",
  "latent_ref": "...",
  "context_distribution": {},
  "candidate_routes": [],
  "energy_terms": {},
  "constraint_residuals": {},
  "calibration_state": {},
  "selected_route": {},
  "output_ref": "...",
  "cost": {},
  "versions": {},
  "lifecycle_actions": []
}
```
