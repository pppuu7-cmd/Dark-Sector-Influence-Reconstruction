# DSIR-4 C2 IDE observation-hook source-site audit v0.1

Date: 2026-09-07

Scope: `C2_IDE_LOCAL_TANGENT_CONE` only.

Status: **SOURCE-SITE FEASIBILITY PASS / IMPLEMENTATION NOT YET AUTHORIZED / +0/+0**.

This audit advances the prospectively frozen Exp073GM observation-only hook without generating or viewing any C2 numerical prediction. It is not `prediction_ready=true` and is not a scientific model PASS/FAIL.

## Pinned authority inspected

- solver: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`;
- file: `source/perturbations.c`;
- file blob at pinned commit: `92a48331658c5941ed4eb43b0e98ee78e39b8385`;
- predecessor static eligibility: Exp073GL run `34093619964`, job `101652242887`, PASS after matcher-only repair.

## Exact runtime site

The pinned `perturb_einstein(...)` signature contains `double k`, `double tau`, `double *y`, and `struct perturb_workspace *ppw`.

At entry it derives native quantities directly from the already-current background workspace:

```c
k2 = k*k;
a = ppw->pvecback[pba->index_bg_a];
a2 = a * a;
a_prime_over_a = ppw->pvecback[pba->index_bg_H]*a;
```

It then calls:

```c
perturb_total_stress_energy(ppr,pba,pth,ppt,index_md,k,y,ppw)
```

The helper constructs the current-gauge total-matter fields and assigns:

```c
ppw->delta_m = delta_rho_m/rho_m;
ppw->theta_m = rho_plus_p_theta_m/rho_plus_p_m;
```

Only later in the same `perturb_einstein` scalar branch does the native CLASS gauge-independent transformation mutate `ppw->delta_m`:

```c
ppw->delta_m += 3.*a*H*ppw->theta_m/k2;
```

and, in synchronous gauge, later mutates `ppw->theta_m` by the metric shift.

Therefore an observation-only diagnostic read placed **after `perturb_total_stress_energy(...)` returns and before the first metric/gauge transformation of `ppw->delta_m` or `ppw->theta_m`** has simultaneous read access to:

- current conformal time `tau`;
- physical solver wavenumber `k`;
- native `a` and `H` from the same background workspace;
- pre-transform `ppw->delta_m`;
- pre-transform `ppw->theta_m`;
- all branch/background entries already present in `ppw->pvecback` needed for IDE positivity diagnostics.

No second background calculation is required.

## Important convention check

The pinned CLASS gauge-independent matter correction is exactly the pressureless-matter specialization

`Delta_m = delta_m + 3 a H theta_m/k^2`.

This is compatible with the frozen C2 observable bridge only when the `m` partition is the pressureless total-matter partition used by the pinned helper. It must **not** be silently reinterpreted as the full residual source `X = T_idm + T_iv`; the interacting vacuum contribution belongs to the C2 residual mapping but is not a pressureless matter species in this `Delta_m` observable coordinate.

This distinction is now frozen for the C2 extraction implementation. Changing the matter partition requires a new prospective interface version before numerical predictions are viewed.

## Observation-only implementation constraints

A valid Exp073GM patch must satisfy all of the following before any numerical generation:

1. patch only the pinned solver tree above;
2. read values at the exact pre-transform runtime site established here;
3. append diagnostics only; no write to `ppw`, `y`, `pvecback`, `pvecmetric`, approximation flags, derivatives, precision fields, species sums, integration state, or branch state;
4. do not call `background_at_tau`, `thermodynamics_at_z`, or any second cosmology calculation from the hook;
5. do not read downstream `index_tp_delta_m` as the pre-transform input;
6. record `tau,k,a,H,delta_m,theta_m` plus the frozen physical-branch diagnostics and model-point identity;
7. use the same compiled diagnostic path for matched C0 and C2;
8. emit no scientific gate decision from the hook itself;
9. prove source-equation equivalence between instrumented and uninstrumented trees modulo diagnostic-only additions;
10. pass a build/static audit before numerical prediction generation is enabled.

## Result

`SOURCE_SITE_FEASIBLE = true`.

The exact hook location and required native quantities are source-supported at the pinned commit. No solver mutation is required to expose the frozen bridge inputs.

Current state remains:

- `mapping_ready = true`;
- `source_site_ready = true`;
- actual diagnostic patch identity = absent;
- build/no-mutation audit = absent;
- deterministic prediction artifact = absent;
- `prediction_ready = false`;
- `G_DOMAIN_MAPPING = NOT_YET_TESTABLE`;
- scientific contribution = `+0/+0`.

Next permitted step: commit an actual diagnostic-only patch plus a hosted static/build equivalence audit. Numerical C2 generation remains forbidden until that audit passes.