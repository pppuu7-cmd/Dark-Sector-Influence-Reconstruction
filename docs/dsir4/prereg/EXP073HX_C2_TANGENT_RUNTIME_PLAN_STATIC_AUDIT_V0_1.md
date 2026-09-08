# Exp073HX — C2 tangent-runtime plan static audit v0.1

Status: **prospectively frozen before execution**. Scope: DSIR only. Classification ceiling `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Freeze and machine-check the exact nonzero C2 tangent model-point/request plan required by the already-frozen `C2_IDE_DELTAM_EXTRACTION_CONTRACT_V0_1.md`, before any nonzero tangent runtime is generated. HX runs no cosmology and inspects no nonzero tangent numerical result.

## Frozen tangent model points

Reference `(0,0)` is already admitted/decoded/mapped-reference by HT/HU/HV/HW and MUST NOT be recomputed by HX.

Nonzero model points, in exact canonical order:

1. `alpha_m1e4`: `(alpha,beta)=(-1e-4,0)`
2. `alpha_m1e3`: `(-1e-3,0)`
3. `alpha_m1e2`: `(-1e-2,0)`
4. `beta_p1e4`: `(0,+1e-4)`
5. `beta_m1e4`: `(0,-1e-4)`
6. `beta_p1e3`: `(0,+1e-3)`
7. `beta_m1e3`: `(0,-1e-3)`
8. `beta_p1e2`: `(0,+1e-2)`
9. `beta_m1e2`: `(0,-1e-2)`

These are exactly the frozen one-sided alpha and symmetric beta definitions. Derivative base step remains `1e-4`; HX does not calculate derivatives.

## Frozen coordinate plan

For each model point use exactly the already-admitted 7 z nodes and 4 in-domain physical-k nodes, z-major/k-minor:

z = `0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33`

k [Mpc^-1] = `0.00067, 0.00201, 0.0067, 0.0201`

Total nonzero runtime requests must therefore be exactly `9*7*4 = 252`, ordered model-major then z-major then k-minor. The excluded legacy `0.067 Mpc^-1` node is forbidden.

## Runtime architecture to authorize after HX PASS

The later producer must reuse the validated HT exact-endpoint observation/serializer lineage and pinned solver/config identities, changing only the prospectively frozen `(alpha,beta)` model-point inputs. It must preserve one exact native 64-byte record per coordinate, provenance receipts and no interpolation/tolerance/effective-coordinate rescue.

For recovery and nonduplication, the future runtime must write a complete durable unit per model point (28 records + receipt + aggregate digest) before marking that point complete. If executed self-hosted, it must use a dedicated checkpoint namespace and the repository heavy-compute standard; if GitHub-hosted, each model point may be an independent matrix job/artifact and canonical reassembly must be separate and fail-closed. No reference recomputation is permitted.

## PASS

Exact token `PASS_EXP073HX_C2_TANGENT_RUNTIME_PLAN_STATIC_AUDIT_V0_1`.

PASS boundaries:

- `classification=SUPPORT_PLUS_0_PLUS_0`
- `model_point_count=9`
- `requests_per_model=28`
- `total_requests=252`
- `reference_recomputed=false`
- `tangent_runtime_started=false`
- `tangent_response_ready=false`
- `prediction_ready=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`

Any plan/grid/order/binding mismatch is implementation/provenance `+0/+0`, never scientific FAIL.

## Next transition

Only HX raw-log PASS permits implementation/launch of a separately bound tangent raw-runtime producer over exactly these 252 requests.