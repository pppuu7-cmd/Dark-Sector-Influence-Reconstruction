# Recovery note — DSIR publication architecture frozen

Date: 2026-09-06  
Scope: **DSIR only**.

The project-level publication architecture was frozen in:

- `docs/DSIR_PUBLICATION_ARCHITECTURE_2026-09-06.md`
- creation commit: `fce46eb74aad797285e2a3fd89d01e41633e76f0`
- file blob: `4661b4c9c796094a57e3e5f33e3fd8a25c186eb5`

## Frozen sequence

1. **DSIR-1 — Framework**
2. **DSIR-2 — Inverse reconstruction / mathematical machinery**
3. **DSIR-3 — Observational implementation + complete funnel**
4. **DSIR-4 — Existing-Model Funnel Matrix**
5. **DSIR-5 — DSIR-derived new dark-sector model**, conditional on the DSIR-4 outcome
6. **DSIR-6 — Independent predictions / external falsification tests**, conditional follow-on

## Critical separation

DSIR-4 and DSIR-5 are deliberately separate publications by default. Existing models must be evaluated through the same prospectively frozen DSIR funnel before a new DSIR-derived model is claimed to be required.

A future model must not be designed and then validated on exactly the same information. The architecture therefore reserves a logical split between `G_design` (allowed to inform construction) and `G_blind` (withheld/prospectively reserved validation gates or external observables). Once the model is frozen, a failure on `G_blind` cannot be rescued by silently altering the same model; any alteration creates a new version/hypothesis.

## Immediate consequence

Work on the DSIR-4 Model Funnel Matrix may begin in parallel with Article 3, but only already-authoritative gates may be evaluated. Unavailable gates must remain `NOT_YET_TESTABLE`; no full DSIR PASS/FAIL may be claimed before all mandatory final funnel gates have admissible authority.

DSIR-5 work before DSIR-4 closure is limited to a constraint skeleton and anti-circularity design, not a final new-model claim.
