# Exp073JP — C2 local tangent prediction artifact admission v0.1

Date frozen: 2026-09-10. Scope: DSIR-4 `G_DOMAIN_MAPPING` capability only.

Status: PROSPECTIVELY FROZEN AFTER THE C2 PREDICTION BASIS WAS CREATED AND BEFORE THIS ADMISSION GATE IS EXECUTED. SUPPORT-ONLY `+0/+0`.

## Purpose and ceiling

Admit the already-frozen deterministic local tangent prediction basis for hypothesis `C2_IDE_LOCAL_TANGENT_CONE`. This gate verifies artifact identity, exact 28-record geometry/order/schema, binary64 payload validity, derivative-definition provenance, baseline/solver provenance, mapping admission, and local-regime restrictions.

It MUST NOT evaluate any Article-III observational data, covariance, whitening, nuisance quotient, relation/null statistic, Wm_S3, likelihood, model score, or final-model gate. It creates no scientific PASS/FAIL for C2.

## Frozen upstream identities

- Exp073IF mapping admission run/job: `34250714613 / 102144147469`.
- exact Exp073IF PASS token: `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.
- Exp073IF prereg Git blob: `52677fe6b0d73d62d01c1f39e8b434ceda0f7e01`.
- admitted mapping artifact Git blob: `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`.
- admitted mapping artifact SHA256: `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`.
- prediction description Git blob: `7e244010ca65050d0c8edff8fe90a9583845a568`.
- canonical prediction basis Git blob: `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`.
- canonical prediction basis SHA256: `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`.
- basis record count: exactly `28`.
- baseline config Git blob: `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`.
- baseline config SHA256: `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`.
- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.
- pinned solver source SHA256: `background.c=7a6ad5d44c316c886fc15c3439e04217c6c480f0dc251e8080aa64643ce1c6fc`; `perturbations.c=61e73ed7d5b785ea5f49620e782c58ec552d2735640a1c1241d5ef354e7e0cbe`.
- reference coordinate authority: Exp073HW run `34242852819`, artifact `10062705321`, ZIP SHA256 `7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`.
- admitted tangent authority: Exp073ID run/job `34249671091 / 102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`.
- tangent candidate source: Exp073IC run `34249380208`, artifact `10065344213`, response SHA256 `e97ef98a5b137081df5937454f02576d30e726266e9c50733bf399a9be2b1907`.
- admitted finite-difference base step: exactly `h=1e-4`.

## Frozen payload geometry and order

The only admitted coordinates are the Cartesian product, in exact z-major / k-minor order:

- z literals: `0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33`;
- k literals [Mpc^-1]: `0.00067, 0.00201, 0.0067, 0.0201`;
- request IDs exactly `z00k00, z00k01, ... z06k03` matching that order.

Every JSONL record must contain exactly the fields:
`request_id`, `z_literal`, `k_literal`, `Delta_ref_hex`, `dDelta_dalpha_hex`, `dDelta_dbeta_hex`.

Every three numerical payload strings must parse with Python `float.fromhex`, be finite binary64 numbers, and round-trip exactly through `float.hex()`.

No interpolation, extrapolation, coordinate substitution, effective z/k, smoothing, averaging, clipping, or record dropping is permitted.

## Frozen local prediction definition

Only the following first-order local tangent expression is admitted:

`Delta_pred(alpha,beta;z,k) = Delta_ref(z,k) + alpha*dDelta_dalpha(z,k) + beta*dDelta_dbeta(z,k)`.

Derivative provenance is fixed to:

- alpha left derivative: `(Delta(alpha=-h,beta=0)-Delta_ref)/(-h)`;
- beta symmetric derivative: `(Delta(alpha=0,beta=+h)-Delta(alpha=0,beta=-h))/(2*h)`;
- `h=1e-4` only.

Alpha is an infinitesimal physically allowed left-sided ray at the origin; beta is two-sided. The admitted object is only a local tangent basis around `(alpha,beta)=(0,0)`. No finite-distance nonlinear completion or arbitrary parameter box is admitted.

## Exact admission decision

PASS requires all of the following:

1. exact frozen Git-blob identities above;
2. exact payload SHA256 and 28 records;
3. exact z/k/request-id order and exact six-field schema;
4. all three binary64 payload values per record are finite and exact hex-round-trippable;
5. prediction description contains the exact mapping/payload identities, derivative definitions, solver/baseline provenance and local-regime/anti-rescue restrictions;
6. Exp073IF upstream mapping admission identity is bound and its exact PASS token is independently verified from the frozen GitHub Actions run/job log;
7. no observational/downstream artifact is read by this admission workflow.

PASS token:
`PASS_EXP073JP_C2_LOCAL_TANGENT_PREDICTION_ARTIFACT_ADMISSION_V0_1`

On PASS only:
- `classification=PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`
- `mapping_ready=true`
- `prediction_ready=true`
- `prediction_scope=LOCAL_TANGENT_BASIS_ONLY`
- `numerically_evaluated=false`
- `scientific_model_authority_created=false`
- `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED`
- `covariance_restriction_authorized=false`
- `Wm_S3_opened=false`

Any mismatch is fail-closed as `INVALID_INFRA_PLUS_0_PLUS_0`; it cannot change any scientific gate status.

## Readiness interpretation

If independently verified, this admission closes only the frozen readiness-telemetry submilestone “deterministic prediction-ready artifact route that can actually enter Gate 1 without post-hoc tuning”. Under `docs/DSIR_READINESS_TELEMETRY_V0_1.md`, overall funnel-to-freeze readiness may then increase by exactly 3 points. Article-III readiness does not increase from this support-only admission.
