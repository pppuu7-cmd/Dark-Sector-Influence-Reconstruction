# DSIR-4 angular-authority binding contract v0.1

Status: prospectively frozen support contract. Scope: DSIR only.

## Purpose

Define the machine-checkable boundary between an admitted `G_DOMAIN_MAPPING` hypothesis and the later `G_ANGULAR_AUTHORITY` funnel gate. This contract does not compute model predictions and cannot itself create model authority.

## Preconditions

A hypothesis may enter this interface only if:
1. its exact mapping artifact has admitted `G_DOMAIN_MAPPING` authority;
2. its hypothesis identity and parameter point are frozen;
3. the certified domain is exactly `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, linear regime, with no quasi-static or sub-horizon shortcut;
4. all six common residual components are explicitly mapped or structurally zero under the frozen residual convention.

## Required angular authority inventory

`G_ANGULAR_AUTHORITY` may be scored only from repository-admitted angular authorities. Workflow success, candidate outputs, staged preregistrations, or partial checkpoints are insufficient.

For the current four-source basis S0..S3 the complete symmetric WW authority set is:
`S0_S0, S0_S1, S0_S2, S0_S3, S1_S1, S1_S2, S1_S3, S2_S2, S2_S3, S3_S3`.

Every required pair must be bound to:
- exact authority-admission experiment token;
- admitted run/job and head SHA;
- exact source ordering / same-object semantics where applicable;
- canonical `EE<-EE` `<f8 [39,12288]` identity;
- DES NSIDE=4096, ell `0..12287`, 39 bands;
- exact file-backed/provenance/checkpoint contract required by its frozen admission.

Missing authority is `NOT_YET_TESTABLE`, never PASS and never FAIL. A scientific FAIL in a mandatory angular authority propagates as FAIL only when the corresponding hypothesis prediction contract requires that authority. Infrastructure/resource failures remain distinct and do not become scientific FAIL.

## No-shortcut rule

Forbidden: candidate-only evidence, workflow-success-only evidence, effective ell/z/k, fiducial-P replacement, interpolation or averaging used to manufacture a missing authority, tolerance rescue, or substituting a different source pair because it is numerically close.

## Gate status

This contract currently creates no `G_ANGULAR_AUTHORITY` scientific authority. Until all hypothesis-required admitted angular authorities are bound prospectively, the gate remains `NOT_YET_TESTABLE`.

## Downstream

Only an admitted `G_ANGULAR_AUTHORITY` may feed `G_ORDERED_JOIN`. Neither this contract nor its static audit may dispatch self-hosted science.
