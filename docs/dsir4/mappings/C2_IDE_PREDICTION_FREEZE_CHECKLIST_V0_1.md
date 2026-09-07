# DSIR-4 C2 IDE prediction freeze checklist v0.1

Date: 2026-09-07

Scope: `C2_IDE_LOCAL_TANGENT_CONE` only.

Status: **PRE-PREDICTION FREEZE CHECKLIST / +0/+0**. This file does not create `prediction_ready`, `G_DOMAIN_MAPPING=PASS`, or any scientific model verdict.

## Purpose

The six-component residual mapping for C2 is now mapping-ready in `C2_IDE_RESIDUAL_MAPPING_V0_1.md`. The next admissible DSIR-4 step is to freeze a deterministic C2 prediction artifact without changing the already frozen hypothesis after seeing downstream gates.

## Frozen authorities that must be inherited verbatim

- Common residual convention: `docs/dsir4/DSIR4_COMMON_RESIDUAL_CONVENTION_V0_1.md`.
- Mapping artifact contract: `docs/dsir4/DSIR4_MODEL_MAPPING_ARTIFACT_CONTRACT_V0_1.md`.
- C2 residual mapping: `docs/dsir4/mappings/C2_IDE_RESIDUAL_MAPPING_V0_1.md`.
- Hypothesis ID: `C2_IDE_LOCAL_TANGENT_CONE`.
- Solver lineage: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

## Mandatory prediction domain

The dedicated prediction artifact must cover exactly the common DSIR-4 v0.1 comparison domain where the C2 branch is valid:

- `0.295 <= z <= 2.33`;
- `0 < k <= 0.06664762008318016 Mpc^-1`;
- linear perturbation regime;
- no Newtonian-gauge C2 perturbation prediction is admitted from the pinned implementation;
- every emitted C2 point must satisfy `rho_idm > 0` and `rho_iv >= 0` throughout the required history.

A point violating the physical branch is `OUTSIDE_DOMAIN`, not observational `FAIL`.

## Parameter freeze requirements

Before numerical generation, the artifact must recover and bind the exact already-frozen legacy tangent definitions rather than reconstructing them from memory:

1. exact reference point `(alpha,beta)=(0,0)`;
2. exact finite left-sided alpha step(s) used by the admitted C2 tangent-cone hypothesis;
3. exact two-sided beta step(s) used by the admitted C2 tangent definition;
4. exact baseline cosmological parameters and precision settings;
5. exact redshift and k nodes used for the dedicated DSIR-4 prediction payload;
6. exact unit conversion between any solver `h/Mpc` output and the common `Mpc^-1` gate domain.

If any one of these cannot be recovered from immutable repository provenance, prediction generation must stop as `NOT_YET_TESTABLE`; no substitute step size, interpolation, or re-fit is permitted.

## Observable bridge requirements

The prediction payload must use the already frozen same-solver common response construction, not raw synchronous `delta_idm_iv`:

`Delta_m = delta_m + 3 (1+w_m) Hconf theta_m/k^2`

and the matched model/reference response

`r_Delta(k,z) = ln[P_Delta_model^S(k,z)/P_Delta_ref^S(k,z)]`.

The extraction must remain within the pinned solver lineage and matched settings. The synchronous source mapping is provenance for `X_munu`; it is not itself the cross-model observable coordinate.

## Deterministic payload manifest

The final C2 prediction artifact must contain, at minimum:

- `hypothesis_id`;
- solver repository and exact commit;
- mapping artifact path and SHA-256;
- parameter-point identifiers and exact alpha/beta values;
- baseline cosmology and numerical precision settings;
- branch-mask result for each emitted parameter point;
- output coordinates `(z,k)` with units;
- prediction columns required by the frozen DSIR response interface;
- deterministic serialization rule;
- SHA-256 of the complete prediction payload;
- generation command/script identity and commit;
- explicit `prediction_ready` boolean.

## Fail-closed classification

- Missing immutable parameter/grid provenance -> `NOT_YET_TESTABLE`.
- Physical branch violation -> `OUTSIDE_DOMAIN` for that frozen parameter point.
- Malformed/non-deterministic payload -> infrastructure or `INVALID_FOR_SCIENCE`, never model `FAIL`.
- A valid, frozen prediction artifact is required before Gate-1 scientific evaluation can occur.

## Current state

- `mapping_ready = true`;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific support contribution: `+0/+0`.

Next action is provenance recovery of the exact legacy alpha/beta tangent steps and matched solver settings, followed by deterministic prediction generation. No downstream angular or observational gate may be used to tune these choices.
