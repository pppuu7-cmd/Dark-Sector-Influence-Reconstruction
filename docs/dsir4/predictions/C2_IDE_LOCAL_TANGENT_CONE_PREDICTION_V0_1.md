# C2 IDE local tangent cone — DSIR-4 prediction artifact v0.1

Status: PROSPECTIVELY FROZEN after Exp073IF mapping admission PASS and before prediction admission/evaluation.

This is a versioned **local tangent prediction basis**, not an observational gate result. It creates no scientific PASS.

## Frozen hypothesis and mapping identity

- hypothesis_id: `C2_IDE_LOCAL_TANGENT_CONE`
- parameter origin: `alpha_idm_iv=0`, `beta_idm_iv=0`
- allowed local directions: alpha is the physically allowed left-sided ray (`alpha<=0` infinitesimally at the origin); beta is two-sided.
- mapping artifact: `docs/dsir4/mappings/C2_IDE_LOCAL_TANGENT_CONE_MAPPING_V0_1.md`
- mapping artifact git blob: `5f2b690e4f56fc0fd3109ff2bcdb53dd0eb806cc`
- mapping artifact SHA256: `7f660b6806494b00d17caed50b7cc66d01d9d02bc4cb1d66f333c1c12e1386df`
- mapping admission: Exp073IF run `34250714613`, job `102144147469`, exact token `PASS_EXP073IF_C2_RESIDUAL_MAPPING_ARTIFACT_ADMISSION_V0_1`.

## Numerical/code provenance

- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`
- baseline config: `configs/dsir4/c2/ide0_reference_v0_1.ini`, blob `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`, SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`.
- reference coordinate authority: Exp073HW run `34242852819`, artifact `10062705321`, ZIP SHA256 `7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`; reference bridge JSONL SHA256 `2b6eb07c99273292bcb2cf929295071e401e81ed51cfe3f4c3b19d5a395518fb`.
- admitted tangent authority: Exp073ID run `34249671091`, job `102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`; admitted finite-difference base step `h=1e-4`.
- tangent candidate source actually admitted by ID: Exp073IC run `34249380208`, artifact `10065344213`, response SHA256 `e97ef98a5b137081df5937454f02576d30e726266e9c50733bf399a9be2b1907`.

The admitted derivative definitions are exactly those executed in the frozen IC workflow:

- alpha left derivative: `dDelta_dalpha = (Delta(alpha=-h,beta=0)-Delta_ref)/(-h)`;
- beta symmetric derivative: `dDelta_dbeta = (Delta(alpha=0,beta=+h)-Delta(alpha=0,beta=-h))/(2*h)`;
- admitted `h=1e-4` only. The larger `1e-3` and `1e-2` steps remain convergence controls and are not prediction coefficients.

## Deterministic prediction payload

Canonical payload:
`docs/dsir4/predictions/C2_IDE_LOCAL_TANGENT_CONE_PREDICTION_BASIS_V0_1.jsonl`

- git blob: `b3c5dc5ec6aefb79f215c5e01d7baef566cc5251`
- SHA256: `2836a3665e6bab75587957228fbd3b9e152ef7d6e667966c308d81bf666c7c56`
- record count: `28`
- order: frozen `z-major / k-minor` request order `z00k00 ... z06k03`.
- each record contains exact binary64 hex encodings of `Delta_ref`, `dDelta/dalpha`, and `dDelta/dbeta`, plus literal `z` and `k`.

The local first-order response represented by each record is exactly

`Delta_pred(alpha,beta;z,k) = Delta_ref(z,k) + alpha*dDelta_dalpha(z,k) + beta*dDelta_dbeta(z,k)`.

This expression defines the hypothesis **only as a local tangent model** around the frozen origin. It does not authorize finite-distance extrapolation, nonlinear completion, or an arbitrary box in `(alpha,beta)`.

## Input assumptions, grid, domain, units

All cosmological assumptions are inherited unchanged from the frozen baseline config identity above; no nuisance refit is introduced here.

Grid literals in the payload are the already-admitted exact endpoint coordinates:
- z literals: `0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33`;
- k literals [Mpc^-1]: `0.00067, 0.00201, 0.0067, 0.0201`.

The certified mapping envelope remains `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`, but this v0.1 deterministic payload exists only at the 28 listed exact coordinates. No interpolation or extrapolation is admitted by this artifact.

`Delta_m`, `dDelta/dalpha`, and `dDelta/dbeta` use the solver-normalized linear perturbation convention inherited from the exact endpoint/bridge lineage; alpha and beta are the dimensionless CLASS-IV coupling parameters defined by the pinned solver keys `alpha_idm_iv` and `beta_idm_iv`.

## Regime / approximation boundary

- exact pinned synchronous implementation and already-admitted gauge-invariant/comoving `Delta_m` bridge;
- linear scalar perturbation regime;
- first-order local tangent approximation at `(0,0)` only;
- alpha left-sided, beta two-sided;
- no quasi-static/sub-horizon shortcut;
- no smoothing, averaging, tolerance rescue, effective coordinates, fiducial-P shortcut, interpolation, or extrapolation;
- no claim that a finite nonzero parameter point is represented beyond the local differential model.

## Status separation

A separate frozen admission must verify the exact mapping SHA256, payload SHA256, 28-record schema/order, derivative definitions, baseline provenance and local-regime restrictions. On admission this artifact may set `prediction_ready=true` only as a **local tangent prediction basis**.

Prediction admission remains support `+0/+0`:
- `mapping_ready=true` remains preserved;
- `prediction_ready` may become true only after admission;
- `numerically_evaluated=false` for any DSIR observational gate;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING=TESTABLE_NOT_EVALUATED` remains unchanged until a separate prospectively frozen scientific evaluation gate is executed.
