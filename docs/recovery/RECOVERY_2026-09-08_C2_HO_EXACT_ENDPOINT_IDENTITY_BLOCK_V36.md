# DSIR immutable recovery — C2 Exp073HO exact-endpoint identity block — V36

Date: 2026-09-08. Scope: **DSIR only**. RTK/RQIR excluded.

## Preserved scientific authority

All authority preserved by V35 remains unchanged. In particular `WW_S3_S3` remains `SCIENTIFIC_AUTHORITY_ADMITTED`. C2 remains `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Exp073HM `34227557134 / 102065303554` and Exp073HN `34228937213 / 102069878872` remain support-only PASS (`SUPPORT_PLUS_0_PLUS_0`).

## Exp073HO terminal consumption

Frozen producer head `841e431d55aadbdc0ea972902be6da5ffa0125bf`, run `34229170304`, actual job `102070681656`, completed `FAILURE`.

The following stages succeeded before failure:

- frozen runtime binding verification;
- reconstruction/build of the exact pinned post-HM solver;
- HN serializer build.

Failure occurred in `Execute frozen 28-request raw producer` on the first frozen solver request, before provenance receipt, artifact upload, aggregate creation, or raw-candidate boundary. Therefore no C2 raw record set exists from this run and no scientific values are authorized for inspection.

The original wrapper exited under `set -e` while solver stdout/stderr were redirected to ephemeral request-local files, so the exact first error was not surfaced in the original HO log. This observability defect is infrastructure/runtime `+0/+0`, not scientific FAIL.

## Exact hosted diagnostic

A hosted-only first-request diagnostic was added in commit `0d68fc61f58e5b7b9f46ca43f4ed32d7b4a34d92` and executed as run `34229365325`, job `102071344339`. It reconstructed the same pinned solver and exact post-HM patch chain and executed only the first unchanged frozen request `z=0.295`, `k=0.00067 Mpc^-1`. It created no packet set and no scientific authority.

The diagnostic reproduced CLASS exit 1 with the exact causal chain:

`perturb_init -> perturb_solve -> evolver_ndf15 -> dsir_c2_diag_arm_terminal`

and exact failure:

`condition (tau != dsir_c2_diag_tau_target) is true; DSIR C2 terminal tau is not the exact background_tau_of_z endpoint`.

This is `IMPLEMENTATION/RUNTIME_EXACT_ENDPOINT_IDENTITY_FAILURE +0/+0`, not scientific FAIL. It is not a scientific negative result because the producer boundary never created an admitted raw observation.

## Why v0.1 is not retried

The frozen patch requires bit-exact equality between the accepted NDF15 terminal time passed to the diagnostic hook and `background_tau_of_z` target. Runtime demonstrates that the current frozen implementation does not satisfy this identity for the first frozen coordinate.

The following rescues are forbidden: tolerance, rounding, nearest-time acceptance, interpolation, altered z/k, modified precision, changed baseline, changed hypothesis ID, or weakened provenance/ABI criteria.

Changing the post-HM source to canonicalize the terminal-time variable would change the frozen post-HM source SHA and the Exp073HO v0.1 implementation/runtime contract. Under the current guard mandate, frozen contracts may not be changed. Therefore no source repair is applied and Exp073HO v0.1 must not be rerun unchanged because it would deterministically repeat the same first-request failure.

Current classification: `BLOCKED_BY_FROZEN_IMPLEMENTATION_EXACT_ENDPOINT_IDENTITY +0/+0`.

## Exact next permitted transition

A further runtime attempt requires a **new prospectively versioned implementation contract/preregistration**, frozen before execution, that defines a bit-exact terminal-time canonicalization while preserving the same physical endpoint, equations, solver tolerances, model point, z/k grid, baseline, p8 settings, packet ABI, field order and provenance requirements. Such a version transition is outside the present no-contract-change repair authority and has not been performed here.

Until that prospective transition exists:

- `raw_record_set_admitted=false`;
- `decoded=false`;
- `mapped=false`;
- `prediction_ready=false`;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`;
- new scientific FAIL contribution = `0`.

No self-hosted/home heavy run is required or authorized for this block.
