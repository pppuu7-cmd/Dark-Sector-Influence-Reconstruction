# Exp073GF — DSIR-4 LambdaCDM/GR baseline mapping static audit v0.1

Frozen prospectively: 2026-09-06. Scope: DSIR only. Support-only; no scientific model authority may be created.

## Frozen inputs
- mapping artifact blob: `9d438b385db5bc2cd07cfaa3c9088f5baa79dd6b`
- validator blob: `bcd081c1d8cde8dd89ff545ca20504dfc8a9aef5`
- parent mapping contract blob: `03fd11d8536b9743eb82f92f9a0d5386444079ed`
- frozen DSIR domain: `0.295<=z<=2.33`, `0<k<=0.06664762008318016 Mpc^-1`

## Gate
The hosted audit must verify exact blob identities and validate the symbolic GR + pressureless CDM + exact-Lambda mapping under the explicit convention that `T_known` contains baryons, photons, and standard neutrinos, while CDM and Lambda remain in `X_munu`.

All six required residual components must be explicit. Lambda perturbations, CDM/Lambda isotropic pressure perturbations, and CDM/Lambda anisotropic stress must be represented as structural zeros where specified, never as omitted or `NOT_YET_MAPPED`. The mapping must require no quasi-static or sub-horizon approximation, remain linear-scalar for perturbations, and preserve the frozen DSIR z/k domain.

This gate only establishes `mapping_ready=true`. It must preserve `prediction_ready=false`, `numerically_evaluated=false`, `scientific_gate_status=NOT_YET_TESTABLE`, and `scientific_model_authority_created=false`.

Exact success token: `PASS_EXP073GF_DSIR4_LCDM_GR_MAPPING_STATIC_AUDIT_V0_1`.
Classification on success: `SUPPORT_PLUS_0_PLUS_0`.
