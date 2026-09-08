# DSIR research log — Exp073HO first runtime failure diagnostic

Date: 2026-09-08. Scope: DSIR only.

Preserved scientific authority is unchanged. WW_S3_S3 remains SCIENTIFIC_AUTHORITY_ADMITTED. C2 remains prediction_ready=false, scientific_model_authority_created=false, G_DOMAIN_MAPPING=NOT_YET_TESTABLE.

## Upstream support consumed

Exp073HM run 34227557134 / job 102065303554 completed SUCCESS. Exp073HN run 34228937213 / job 102069878872 completed SUCCESS and emitted PASS_EXP073HN_C2_REFERENCE_RUNTIME_DRIVER_SERIALIZER_STATIC_AUDIT_V0_1 with classification SUPPORT_PLUS_0_PLUS_0, request_plan_count=28, coordinate_order=z-major/k-minor, serializer_64_byte_abi_verified=true, cosmological_run_started=false, real_runtime_payload_created=false.

## Exp073HO terminal state

Frozen runtime producer commit/head: 841e431d55aadbdc0ea972902be6da5ffa0125bf. Run 34229170304 / job 102070681656 completed FAILURE.

Frozen binding verification SUCCESS. Exact post-HM solver reconstruction and HN serializer build SUCCESS. Failure occurred in step `Execute frozen 28-request raw producer` immediately at the first solver invocation, before any terminal aggregate/provenance receipt/artifact/admission boundary was produced. The wrapper redirected solver stdout/stderr into an ephemeral per-request directory and exited under `set -e` before surfacing those diagnostics, so the exact runtime error text was not preserved by run 34229170304.

Classification: INFRASTRUCTURE/RUNTIME_OBSERVABILITY_FAILURE +0/+0. This is not a scientific FAIL. No raw record set was admitted; decoded=false; mapped=false; prediction_ready=false; scientific_model_authority_created=false; G_DOMAIN_MAPPING=NOT_YET_TESTABLE.

No retry with altered coordinates, tolerances, baseline, precision, hypothesis ID or scientific logic is permitted.

## Safe diagnostic isolation and exact cause

Added hosted-only exact first-request diagnostic workflow in commit 0d68fc61f58e5b7b9f46ca43f4ed32d7b4a34d92. Diagnostic run 34229365325 / job 102071344339 reconstructed the same pinned solver and exact post-HM patch chain, then executed only the first frozen request z=0.295, k=0.00067 Mpc^-1 with unchanged baseline and p8 precision while surfacing stdout/stderr. It created no packet set and no scientific authority.

The diagnostic deterministically reproduced CLASS exit 1 with the exact fail-closed chain:

- perturb_init -> perturb_solve -> evolver_ndf15 -> dsir_c2_diag_arm_terminal;
- terminal error: `condition (tau != dsir_c2_diag_tau_target) is true; DSIR C2 terminal tau is not the exact background_tau_of_z endpoint`.

Therefore the physical solver did not produce an admitted endpoint record. This is an implementation/runtime exact-endpoint identity failure, not a scientific model FAIL. It is also not INVALID_FOR_SCIENCE evidence to be decoded: no raw candidate exists.

Pinned NDF15 sets terminal h as `tfinal - t` when within the terminal stretch, while the patched diagnostic contract requires bit-exact `tnew == background_tau_of_z target`. The observed run shows that the frozen patched implementation does not satisfy its own exact-endpoint identity at runtime for the first frozen coordinate.

A repair by tolerance, rounding, nearest-time acceptance, interpolation, or altered coordinate is explicitly forbidden. A prospective source change that canonicalizes terminal time identity would change the frozen post-HM source SHA / implementation contract and therefore is not applied under the current no-contract-change guard. Exp073HO remains BLOCKED_BY_FROZEN_IMPLEMENTATION_EXACT_ENDPOINT_IDENTITY +0/+0 until a separately authorized prospective contract/version transition is frozen before execution.

No competing heavy/self-hosted run is active. Do not rerun Exp073HO v0.1 unchanged: it will deterministically repeat the same first-request failure.
