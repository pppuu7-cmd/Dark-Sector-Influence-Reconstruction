# DSIR-4 C2 IDE prediction provenance recovery v0.1

Date: 2026-09-07

Scope: `C2_IDE_LOCAL_TANGENT_CONE` only.

Status: **PROVENANCE_RECOVERED / PREDICTION_NOT_YET_READY / +0/+0**. This record does not create `prediction_ready`, `G_DOMAIN_MAPPING=PASS`, or a scientific model verdict.

## Immutable legacy source recovered

The exact validated legacy IDE tangent-cone artifact remains available:

- workflow run: `32760042765`;
- job: `97536488223` (`ide-jacobian`), terminal SUCCESS;
- artifact id: `9532491954`;
- artifact name: `ide-tangent-cone-127f50b25817484329d98e3dd3729e3fb113153b`;
- artifact head branch/SHA: `research/ide-jacobian-manifold` / `e2e331c914159fc1a8513166fb7ceb0250b14a49`;
- PR merge checkout observed in raw job log: `127f50b25817484329d98e3dd3729e3fb113153b`;
- pinned solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- GitHub artifact digest: `sha256:408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- independently downloaded ZIP SHA256: `408322a2ee79907dd98cdd0e532daaed1e1aeeb1b633f42ab5321cb32149ab6d`;
- ZIP size: `10488299` bytes.

The independent ZIP hash exactly matches the GitHub artifact digest.

## Exact frozen tangent definitions recovered

Reference point:

- `(alpha,beta)=(0,0)` from `external_iv/ide0.ini`.

Alpha physical tangent:

- sampled steps `h in {1e-4,1e-3,1e-2}`;
- physical direction is the one-sided `alpha=-h` ray;
- positive-alpha counterparts are outside the calibrated physical branch because full-history `rho_iv>=0` fails;
- the legacy tangent-cone geometry uses `base_step=1e-4` and defines the alpha derivative as left-sided at zero.

Beta tangent:

- sampled symmetric steps `beta=+/-h`, `h in {1e-4,1e-3,1e-2}`;
- the legacy tangent-cone geometry uses `base_step=1e-4` and the central derivative at zero.

No new step size is introduced here.

## Exact baseline cosmology recovered

From the validated artifact `external_iv/ide0.ini`:

- `h = 0.67`;
- `T_cmb = 2.7255`;
- `omega_b = 0.0224`;
- `N_ur = 3.046`;
- `omega_cdm = 0.1200`;
- `f_idm_iv = 1`;
- `f_iv = 1`;
- `Omega_dcdmdr = 0`;
- `N_ncdm = 0`;
- `Omega_k = 0`;
- `Omega_fld = 0`;
- `Omega_scf = 0`;
- `Omega_idm_dr = 0`;
- `YHe = 0.2404`;
- recombination `RECFAST`;
- reionization `reio_none`;
- scalar adiabatic mode in synchronous gauge;
- analytic primordial spectrum with `k_pivot=0.05`, `A_s=2.10e-9`, `n_s=0.965`, `alpha_s=0`;
- `P_k_max_h/Mpc = 0.25`.

Exact redshift nodes:

`[0.295, 0.51, 0.706, 0.934, 1.317, 1.491, 2.33]`.

Legacy tangent-extraction k nodes were recorded in `h/Mpc` as:

`[0.001, 0.003, 0.01, 0.03, 0.1] h/Mpc`.

With the frozen `h=0.67`, their exact numerical conversion under `k[Mpc^-1] = h * k[h/Mpc]` is:

`[0.00067, 0.00201, 0.0067, 0.0201, 0.067] Mpc^-1`.

The final legacy node `0.067 Mpc^-1` lies **outside** the current DSIR frozen upper domain `0.06664762008318016 Mpc^-1`; it must not be silently rounded or admitted. The first four converted legacy nodes lie inside the current domain. This observation does not define a replacement grid.

## Exact precision preset recovered

Validated artifact `external_iv/dsir_ide_p8.pre` contains:

- `k_step_sub = 0.0010`;
- `k_step_super = 0.000003`;
- `k_step_super_reduction = 0.1`;
- `start_small_k_at_tau_c_over_tau_h = 1e-6`;
- `start_large_k_at_tau_h_over_tau_k = 0.05`;
- `tight_coupling_trigger_tau_c_over_tau_h = 0.005`;
- `tight_coupling_trigger_tau_c_over_tau_k = 0.008`;
- `start_sources_at_tau_c_over_tau_h = 0.006`;
- `tol_perturb_integration = 3e-10`;
- `perturb_sampling_stepsize = 0.00035`;
- `radiation_streaming_approximation = 2`;
- `radiation_streaming_trigger_tau_over_tau_k = 240`;
- `radiation_streaming_trigger_tau_c_over_tau = 100`;
- `ur_fluid_approximation = 2`;
- `ur_fluid_trigger_tau_over_tau_k = 50`.

The pinned class_iv source required the already-recorded compile-only repair that removed exactly one premature closing brace in `source/background.c`; no physics expression was altered by that repair.

## Independent member hashes

For audit/recovery, SHA256 of selected ZIP members from the independently downloaded artifact:

- `ide_jacobian_manifold.json`: `3801dacd970db8880d14ae5e9f20fd472b0391df52c6c89db3a9de87e40181d3`;
- `ide_tangent_cone_geometry.json`: `bbf29ba0d7206619b651685349e45a771a4c6347b16ef2201cc4e73f50eb01e7`;
- `external_iv/ide0.ini`: `0a68f4af6ead7ee69c75f1867f60914a40d4f7ff1219b965a0ae38186ca5c65c`;
- `external_iv/a_m1em4.ini`: `e5862721d7d06e097cafdde2b395638597fde78790d45cb06440d1bfe4037d54`;
- `external_iv/b_p1em4.ini`: `e828b1c84f2f6ee0514188661ce372fa07ae1f2bf25764577ffa7294ceca1e0d`;
- `external_iv/b_m1em4.ini`: `19bd4f5b2f7276f0339a82c32cc951d501469498e03588be58304469185b4a75`;
- `external_iv/dsir_ide_p8.pre`: `463a3960d6a955c1e2a561e988562a1fc5486b0b79f120eb634ccca6f86002f9`.

## Critical observable-interface finding

The legacy artifact is **not** itself a valid DSIR-4 prediction artifact for the frozen observable bridge.

Its raw job log and `ide_jacobian_manifold.json` explicitly define legacy `r_Delta` as

`ln(P_model/P_zero_interaction)`

from CLASS `mPk` outputs. The current C2 prediction-freeze checklist requires the already-frozen same-solver common response construction based on the gauge-aware matter response

`Delta_m = delta_m + 3 (1+w_m) Hconf theta_m/k^2`

followed by the matched model/reference power response. Therefore the old `r_Delta` array must **not** be relabelled as the new DSIR-4 `Delta_m` prediction.

This is a provenance/interface distinction, not a scientific failure of C2.

## Fail-closed current state

Recovered successfully:

- exact reference point;
- exact alpha/beta finite-difference hierarchy and base step;
- physical alpha branch orientation;
- exact baseline cosmology;
- exact p8 precision preset;
- exact legacy z and k nodes and unit conversion;
- exact solver commit and artifact digest.

Still required before `prediction_ready=true`:

1. a prospectively frozen generation/extraction implementation that obtains the common `Delta_m` response from the same pinned solver lineage without relabelling legacy raw `mPk` response;
2. an explicitly frozen output k-grid inside `0 < k <= 0.06664762008318016 Mpc^-1` with no rounding or rescue of the legacy `0.067 Mpc^-1` node;
3. deterministic prediction serialization and payload SHA256;
4. per-point physical branch mask proving `rho_idm>0` and `rho_iv>=0` over the required history;
5. a hosted/static provenance audit before any scientific gate consumes the resulting prediction.

Current status remains:

- `mapping_ready = true`;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific contribution `+0/+0`.

No downstream WW result or observational gate was consulted to choose or alter C2 scientific acceptance criteria.