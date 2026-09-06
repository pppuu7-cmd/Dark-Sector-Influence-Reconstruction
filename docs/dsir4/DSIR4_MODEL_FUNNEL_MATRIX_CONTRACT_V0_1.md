# DSIR-4 Model Funnel Matrix contract v0.1

Frozen: 2026-09-06. Scope: DSIR only.

## Purpose

Define a machine-readable, non-circular comparison layer for existing cosmological model classes before any DSIR-derived new model is claimed necessary.

This contract is infrastructure only. It creates no model PASS/FAIL result.

## Scientific unit of evaluation

A model-class label is an inventory entry, not automatically a scientific hypothesis. Scientific evaluation should occur at a frozen `parameter_point_id` or a prospectively defined `equivalence_class_id` when multiple parameter points are observationally indistinguishable under the available DSIR gates.

Every evaluated hypothesis must bind:

- `model_class_id`;
- `hypothesis_id` (`parameter_point_id` or `equivalence_class_id`);
- mapping version/hash into the DSIR common residual/influence interface;
- certified `(z,k)` applicability domain;
- frozen prediction artifact identity/hash;
- per-gate observational authority provenance;
- exact gate status.

## Allowed scientific statuses

Exactly:

- `PASS`
- `FAIL`
- `OUTSIDE_DOMAIN`
- `NOT_YET_TESTABLE`
- `NUMERICALLY_UNRESOLVED`

No percentage PASS, score-to-PASS proxy, or free-text replacement is allowed.

## Mandatory funnel gates v0.1

1. `G_DOMAIN_MAPPING` — mapping into common DSIR interface plus certified domain.
2. `G_ANGULAR_AUTHORITY` — required angular observational authority set.
3. `G_ORDERED_JOIN` — frozen ordered observable join.
4. `G_RADIAL_SUPPORT` — radial multiplication / support construction.
5. `G_PHYSICAL_SUPPORT` — physical-support admissibility.
6. `G_COV_WHITENING` — covariance and whitening authority.
7. `G_NUISANCE_QUOTIENT` — nuisance quotient.
8. `G_RELATION_NULL` — relation/null structure.
9. `G_FINAL_MODEL` — final prospective model comparison gate.

A later version may refine gate granularity, but may not silently reinterpret an earlier result.

## Aggregation rule

For a frozen hypothesis:

1. `PASS` is permitted only when **every mandatory gate is PASS** and every gate has bound authority provenance.
2. If any mandatory gate is `FAIL`, overall status is `FAIL`.
3. `OUTSIDE_DOMAIN` is used when the frozen hypothesis cannot validly make the required prediction on the mandatory DSIR domain. It is not converted to PASS/FAIL by extrapolation.
4. `NUMERICALLY_UNRESOLVED` is allowed only under a prospectively frozen numerical ambiguity rule after prerequisites exist; it is not a tolerance rescue.
5. Otherwise, if one or more mandatory gates are unavailable, overall status is `NOT_YET_TESTABLE`.
6. `NOT_YET_TESTABLE` must never be counted as PASS, FAIL, fractional PASS, or evidence for/against a model.

## Current pre-DSIR-3-closure rule

Until the complete observational funnel is available, all inventory entries remain overall `NOT_YET_TESTABLE`. Individual infrastructure/mapping readiness may be tracked separately but has zero scientific PASS/FAIL weight.

## Anti-circularity

- Thresholds and status semantics are frozen independently of the desired outcome for any model.
- A future DSIR-derived model is excluded from this existing-model inventory until DSIR-4 establishes that construction of such a model is scientifically motivated.
- No post-hoc model modification may rescue a failed frozen hypothesis; the modified object receives a new hypothesis/version ID.
- Missing later gates remain missing; no proxy may replace them while preserving the same gate name.

## Initial model-class inventory target

The v0.1 inventory contains class-level placeholders for:

- LambdaCDM / GR baseline;
- wCDM;
- w0wa dark energy;
- canonical quintessence-like models;
- interacting dark-energy / interacting-dark-sector models;
- f(R)-type modified gravity;
- DGP-like models;
- Horndeski / EFT-like representative models;
- additional representative dark-matter/dark-sector classes when a sufficiently explicit DSIR mapping is frozen.

These are inventory targets only, not current scientific conclusions.
