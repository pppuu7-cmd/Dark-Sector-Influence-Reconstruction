# Exp073HM — C2 mPk native-theta observer guard audit v0.1

Status: **PROSPECTIVELY FROZEN BEFORE IMPLEMENTATION EXECUTION**. Scope: DSIR only. PASS ceiling: `SUPPORT_PLUS_0_PLUS_0`.

## Purpose

Correct only the observation guard that would otherwise reject the immutable legacy `output=mPk` baseline even though pinned CLASS computes native `ppw->theta_m` whenever the total-matter delta source is enabled.

This is not a scientific acceptance-criterion change. No runtime result has been generated. The change is frozen before cosmological execution.

## Frozen source proof

Pinned CLASS `ac627d54e9ce196a08878d1ba33999819925d19c` must statically prove all of:

1. `has_pk_matter` sets `ppt->has_source_delta_m = _TRUE_`;
2. `perturb_total_stress_energy` initializes/accumulates `rho_plus_p_theta_m` whenever `has_source_delta_m || has_source_theta_m`;
3. it assigns `ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m` under the same OR condition;
4. HJ/HB captures `ppw->delta_m` and `ppw->theta_m` before the downstream gauge transformation;
5. the legacy baseline remains exactly `output = mPk`; no nCl/RSD output is added to satisfy the observer.

## Frozen repair semantics

Starting from exact HJ final `source/perturbations.c` SHA256 `f1a5619ea2dfb60e4e236349485dcffb58c1c2ef96358bd59b8a1207d77248d2`, replace exactly one observer guard:

from requiring both `ppt->has_source_delta_m == _TRUE_` and `ppt->has_source_theta_m == _TRUE_`

to requiring only `ppt->has_source_delta_m == _TRUE_`.

The diagnostic error text must state that the native mPk delta-m source path is required. No equation, total-stress accumulation, endpoint selection, z/k literal, accepted-ynew hook, source capture, background read, precision, baseline parameter or serializer ABI may change.

## Hosted audit

A deterministic post-HJ patch script must be committed after this preregistration and bound by exact Git blob in the workflow before execution. Hosted audit must reconstruct HI + HB + HJ exactly, verify HJ source SHA, apply the HM guard patch once, static-audit the five source-proof conditions above, prove no count increase of `background_at_tau(`, `background_tau_of_z(`, `perturb_sources_at_tau(` or `interp_from_dif(` relative to HJ, run `git diff --check`, and compile the full solver.

It MUST NOT execute `./class`, create a cosmological output, record payload, decode/map fields or claim model authority.

Exact PASS token:

`PASS_EXP073HM_C2_MPK_NATIVE_THETA_OBSERVER_GUARD_AUDIT_V0_1`

with `classification=SUPPORT_PLUS_0_PLUS_0`, `mpk_native_delta_enables_theta_path_verified=true`, `observer_guard_corrected=true`, `diagnostic_producer_compile_verified=true`, `cosmological_run_started=false`, `record_payload_created=false`, `runtime_record_count=0`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

Any failure is implementation/infrastructure `+0/+0`, never scientific model FAIL.
