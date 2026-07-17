#!/usr/bin/env python3
"""
CI gate for MMALS G2 claim manifests.

Checks, in order, any one of which fails the build:

  1. Schema conformance          (claim-manifest.schema.json)
  2. Gate-freeze-before-use      a phase may not be in-progress/complete
                                  while using a gate whose threshold is
                                  not frozen (Section 16.4 circularity risk)
  3. Phase ordering               a phase may not be in-progress/complete
                                  unless every phase it depends_on is complete
  4. Split provenance             a phase may not consume a split_id that
                                  no completed phase has produced
  5. Estimator selection honesty  selected_for_elegance_only must not be true
  6. Publication eligibility      g2-candidate / deferred claims must not be
                                  marked external_publication_eligible
                                  (belt-and-suspenders on top of the schema's
                                  own if/then, in case a manifest was hand-
                                  edited around it)
  7. Gate status vs. hard claims  a claim whose falsification_test depends on
                                  a gate cannot be 'g1-qualified' or higher
                                  while that gate's status is not 'passed'

Usage:
    python3 validate_manifest.py --schema claim-manifest.schema.json manifest1.json [manifest2.json ...]

Exit code 0 = all checks passed on all manifests.
Exit code 1 = at least one check failed. All failures are printed before exiting
              (the script does not stop at the first error) so CI logs show the
              full list to fix in one pass.
"""

import argparse
import json
import sys

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema is required. Install with: pip install jsonschema --break-system-packages", file=sys.stderr)
    sys.exit(2)


def load(path):
    with open(path) as f:
        return json.load(f)


def check_schema(instance, schema, errors):
    validator = jsonschema.Draft202012Validator(schema)
    for e in sorted(validator.iter_errors(instance), key=lambda e: list(e.path)):
        loc = "/".join(str(p) for p in e.path) or "(root)"
        errors.append(f"[SCHEMA] {loc}: {e.message}")


def check_gate_freeze_before_use(instance, errors):
    gates_by_id = {g["gate_id"]: g for g in instance.get("gates", [])}
    for phase in instance.get("phases", []):
        if phase.get("status") not in ("in-progress", "complete"):
            continue
        for gate_id in phase.get("uses_gates", []):
            gate = gates_by_id.get(gate_id)
            if gate is None:
                errors.append(f"[GATE-FREEZE] phase {phase['phase_id']} uses unknown gate {gate_id}")
                continue
            if not gate.get("threshold_frozen", False):
                errors.append(
                    f"[GATE-FREEZE] phase {phase['phase_id']} is '{phase['status']}' and uses gate "
                    f"{gate_id}, but {gate_id}.threshold_frozen is false. Freeze the threshold "
                    f"before this phase may run, or the gate's pass/fail is circular."
                )


def check_phase_ordering(instance, errors):
    phases_by_id = {p["phase_id"]: p for p in instance.get("phases", [])}
    for phase in instance.get("phases", []):
        if phase.get("status") not in ("in-progress", "complete"):
            continue
        for dep_id in phase.get("depends_on_phases", []):
            dep = phases_by_id.get(dep_id)
            if dep is None:
                errors.append(f"[PHASE-ORDER] phase {phase['phase_id']} depends on unknown phase {dep_id}")
                continue
            if dep.get("status") != "complete":
                errors.append(
                    f"[PHASE-ORDER] phase {phase['phase_id']} is '{phase['status']}' but its "
                    f"dependency {dep_id} is only '{dep.get('status')}', not 'complete'."
                )


def check_split_provenance(instance, errors):
    produced_by_complete = set()
    for phase in instance.get("phases", []):
        if phase.get("status") == "complete":
            produced_by_complete.update(phase.get("produces_split_ids", []))

    for phase in instance.get("phases", []):
        if phase.get("status") not in ("in-progress", "complete"):
            continue
        for split_id in phase.get("consumes_split_ids", []):
            if split_id not in produced_by_complete:
                errors.append(
                    f"[SPLIT-PROVENANCE] phase {phase['phase_id']} consumes split '{split_id}', "
                    f"which no completed phase has produced yet."
                )


def check_estimator_honesty(instance, errors):
    for est in instance.get("estimators", []):
        if est.get("selected_for_elegance_only") is True:
            errors.append(
                f"[ESTIMATOR-HONESTY] estimator {est['estimator_id']} is flagged "
                f"selected_for_elegance_only=true, which the research discipline forbids "
                f"(Section 5.1: 'select no estimator solely for elegance')."
            )


def check_publication_eligibility(instance, errors):
    for claim in instance.get("claims", []):
        if claim.get("status") in ("g2-candidate", "deferred") and claim.get("external_publication_eligible") is True:
            errors.append(
                f"[PUBLICATION-ELIGIBILITY] claim {claim['claim_id']} has status "
                f"'{claim['status']}' but external_publication_eligible=true. "
                f"Candidate and deferred claims must not be marked externally publishable."
            )


def check_claim_gate_consistency(instance, errors):
    gates_by_id = {g["gate_id"]: g for g in instance.get("gates", [])}
    for claim in instance.get("claims", []):
        if claim.get("status") not in ("g1-qualified", "established"):
            continue
        for gate_id in claim.get("depends_on_gates", []):
            gate = gates_by_id.get(gate_id)
            if gate is None:
                errors.append(f"[CLAIM-GATE] claim {claim['claim_id']} depends on unknown gate {gate_id}")
                continue
            if gate.get("status") != "passed":
                errors.append(
                    f"[CLAIM-GATE] claim {claim['claim_id']} is marked '{claim['status']}' but "
                    f"depends on gate {gate_id}, whose status is '{gate.get('status')}', not 'passed'. "
                    f"Downgrade the claim to 'g2-candidate' or pass the gate."
                )


def validate_file(path, schema):
    instance = load(path)
    errors = []
    check_schema(instance, schema, errors)
    # Cross-referential checks only make sense on a structurally valid document;
    # still run them, but errors will be prefixed distinctly from schema errors.
    check_gate_freeze_before_use(instance, errors)
    check_phase_ordering(instance, errors)
    check_split_provenance(instance, errors)
    check_estimator_honesty(instance, errors)
    check_publication_eligibility(instance, errors)
    check_claim_gate_consistency(instance, errors)
    return errors


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--schema", required=True)
    ap.add_argument("manifests", nargs="+")
    args = ap.parse_args()

    schema = load(args.schema)
    any_failed = False

    for path in args.manifests:
        errors = validate_file(path, schema)
        if errors:
            any_failed = True
            print(f"\nFAIL: {path}")
            for e in errors:
                print(f"  - {e}")
        else:
            print(f"PASS: {path}")

    if any_failed:
        print("\nCI GATE: FAILED")
        sys.exit(1)
    else:
        print("\nCI GATE: PASSED")
        sys.exit(0)


if __name__ == "__main__":
    main()
