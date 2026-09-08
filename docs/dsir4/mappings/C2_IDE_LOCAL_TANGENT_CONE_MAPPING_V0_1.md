# C2 IDE local tangent cone — DSIR-4 residual mapping artifact v0.1

Status: PROSPECTIVELY FROZEN after Exp073IE source-audit PASS and before any DSIR-4 mapping admission or prediction gate.

This artifact is bookkeeping/mapping infrastructure only. It creates no observational or scientific PASS.

## Identity and provenance

- hypothesis_id: `C2_IDE_LOCAL_TANGENT_CONE`
- residual convention: `X_munu = M0^2 G_munu - T_known_munu`
- common residual convention blob: `9ab68fe254891a076e24757de724e32e2190bfb6`
- model mapping contract blob: `03fd11d8536b9743eb82f92f9a0d5386444079ed`
- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`
- pinned solver source SHA256: `background.c=7a6ad5d44c316c886fc15c3439e04217c6c480f0dc251e8080aa64643ce1c6fc`; `perturbations.c=61e73ed7d5b785ea5f49620e782c58ec552d2735640a1c1241d5ef354e7e0cbe`
- baseline config: `configs/dsir4/c2/ide0_reference_v0_1.ini`; blob `cd2beb01ce6575f97f2e3203226ed6d4f048dcaa`; SHA256 `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`
- gauge/basis: exact pinned CLASS synchronous-gauge implementation.
- source readiness: Exp073IE run `34250165394`, job `102142253548`, PASS token `PASS_EXP073IE_C2_SIX_COMPONENT_RESIDUAL_MAPPING_SOURCE_AUDIT_V0_1`.
- admitted numerical tangent response: Exp073ID run `34249671091`, job `102140579398`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77`, admitted base step `1e-4`.

## T_known and sector-total convention

`T_known` is the frozen DSIR-4 ordinary sector: baryons, photons, frozen standard-neutrino sector and any explicitly frozen ordinary calibration terms. Candidate dark matter `idm_iv` and interacting vacuum `iv` are excluded from `T_known`; the authoritative C2 residual is their **total** stress-energy.

The pinned internal transfer convention is

`Q = alpha_idm_iv * H * rho_idm_iv + beta_idm_iv * H * rho_iv`.

`Q` is sector bookkeeping/provenance only. It is not a seventh component of `X_munu`; internal transfer cancels from total dark-sector conservation.

## Six-component scalar residual mapping

In the exact pinned synchronous representation:

1. `background_density_like`: `rho_X = rho_idm_iv + rho_iv` — SOURCE_DERIVED.
2. `background_pressure_like`: `p_X = -rho_iv` — SOURCE_DERIVED; idm pressure is zero.
3. `scalar_density_perturbation`: `delta_rho_X = rho_idm_iv * delta_idm_iv` — SOURCE_DERIVED in the pinned synchronous solver representation; no independent vacuum-density perturbation state is defined.
4. `scalar_momentum_velocity`: `q_X = 0` — STRUCTURAL_ZERO in this pinned synchronous representation; the idm_iv velocity state is absent/vanishing in synchronous gauge and vacuum has `rho+p=0`.
5. `scalar_isotropic_pressure_perturbation`: `delta_p_X = 0` — STRUCTURAL_ZERO in this pinned implementation; the IDE stress-energy block adds no pressure-perturbation term and no independent iv perturbation state exists.
6. `scalar_anisotropic_stress`: `pi_X = 0` — STRUCTURAL_ZERO in this pinned implementation; the IDE block adds no shear/anisotropic-stress term.

These formulas are solver/gauge-bound to the pinned C2 implementation. They are not asserted for arbitrary interacting-vacuum prescriptions.

## Observable-response basis binding

Gauge-specific raw variables are not compared across solvers. The already-admitted C2 response lineage uses the frozen comoving/gauge-invariant density bridge

`Delta_m = delta_m + 3*a*H*theta_m/k^2`

for the pressureless matter response, with the exact endpoint extraction/decode/mapping lineage preserved by Exp073HT/HU/HV/HW and tangent HZ/IA/IB-v0.2/IC/ID authorities recorded in recovery. This mapping artifact does not recompute or alter that response.

## Certified coordinate domain

The certified DSIR-4 coordinate domain for this mapping is exactly:

- `z_min = 0.295`
- `z_max = 2.33`
- `k_min_exclusive_mpc_inv = 0`
- `k_max_mpc_inv = 0.06664762008318016`

No effective `z`, effective `k`, interpolation rescue or extrapolation is allowed.

## Regime and branch conditions

- linear scalar perturbation regime of the pinned CLASS implementation;
- synchronous gauge exactly as frozen in the C2 baseline;
- local tangent hypothesis around the admitted C2 reference, with admitted numerical derivative base step `1e-4` and the prospectively frozen tested alpha/beta tangent directions already represented by the admitted tangent-response lineage;
- only solver states for which the pinned implementation completes and returns finite exact-endpoint records are within numerical support;
- the reference/tangent mapping preserves the previously audited physical-sign evidence (`rho_idm_iv > 0`, `rho_iv >= 0`) where recorded; this artifact does not extrapolate those signs to uncomputed parameter points;
- no quasi-static, sub-horizon, smoothing, rounding, averaging or fiducial-P approximation is introduced by this mapping artifact.

The mapping is certified as a representation over the frozen z/k domain for the pinned hypothesis/version. This does not certify observational viability over that domain and does not create a prediction artifact.

## Status separation

This artifact may become `mapping_ready=true` only after a separate frozen admission verifies its exact identity, six-component completeness, source bindings, domain and tangent provenance. Even after such admission:

- `prediction_ready=false` until a separate versioned prediction artifact exists;
- `scientific_model_authority_created=false`;
- `G_DOMAIN_MAPPING` may become `TESTABLE_NOT_EVALUATED`, never PASS solely from this mapping artifact.
