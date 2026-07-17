# MMALS G2 claim-manifest governance

Status: internal research governance artifact for v0.2-internal.

This layer makes the paper's evidence maturity taxonomy machine-readable. It is not evidence that any G2 claim has passed. It prevents an unqualified claim from silently changing status while Guillaume switches between research subjects.

## Contents

- `governance/schema/claim-manifest.schema.json`: JSON Schema 2020-12.
- `governance/manifests/g2-v0.2-internal.manifest.json`: frozen example/current-state manifest.
- `scripts/validate_manifest.py`: schema and cross-registry checks.
- `.github/workflows/validate-manifest.yml`: automatic validation on pushes and pull requests.

## Enforced rules

1. G2-candidate claims require an explicit falsification test.
2. Candidate and deferred claims cannot be marked externally publication-eligible.
3. A running phase cannot use an unfrozen gate threshold.
4. Phase dependencies must be complete before execution.
5. Consumed splits must have been produced by completed phases.
6. Estimators selected for elegance alone fail validation.
7. Established or G1-qualified claims cannot depend on gates that have not passed.

## Reviewer-derived contamination rule

Estimator selection in P3 may use only the development split. It must not inspect the calibration or qualification splits. R3's FARgate and GateRegret thresholds must be frozen before P5 consumes qualification evidence. The manifest intentionally records these numeric thresholds as unfrozen until they are preregistered.

## Local validation

```bash
python3 scripts/validate_manifest.py \
  --schema governance/schema/claim-manifest.schema.json \
  governance/manifests/g2-v0.2-internal.manifest.json
```

## Interpretation

A passing CI result means the evidence registry is internally consistent. It does not mean the scientific gates have passed. Most R1-R9 statuses remain pending by design.

## Provenance-seal semantics

The three commit fields in the frozen v0.2 manifest identify the immutable
**content snapshot commit** immediately preceding the provenance-seal commit:

`7bd82e88f1b4bd7bdc2f966d3ea6985877bd1bca`

A Git commit cannot contain its own hash without a self-reference paradox.
The archive therefore uses a two-commit seal:

1. the content snapshot commit fixes the complete research tree;
2. the provenance-seal commit replaces the three placeholders with the
   content snapshot hash and changes nothing else of scientific substance.

The final archive records the provenance-seal HEAD separately in
`FREEZE_SEAL.txt` and includes a Git bundle containing both commits.
