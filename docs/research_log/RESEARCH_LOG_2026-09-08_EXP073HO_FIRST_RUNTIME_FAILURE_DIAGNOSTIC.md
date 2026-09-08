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

## Safe diagnostic isolation

Added hosted-only exact first-request diagnostic workflow in commit 0d68fc61f58e5b7b9f46ca43f4ed32d7b4a34d92. Diagnostic run 34229365325 / job 102071344339 reconstructs the same pinned solver and exact post-HM patch chain, then executes only the first frozen request z=0.295, k=0.00067 Mpc^-1 with unchanged baseline and p8 precision while surfacing stdout/stderr. It creates no packet set and no scientific authority.

At log creation this diagnostic job is IN_PROGRESS in the solver reconstruction step. No competing self-hosted heavy process exists. Do not launch another HO producer until this diagnostic reaches terminal state and the technical cause is isolated.
