# DSIR RECOVERY LATEST — live overlay

**Date:** 2026-08-24  
**Read after:** `docs/RECOVERY_MANUAL.md`

This short file is the live delta to the long recovery manual. The long manual contains the architecture and full derivations; this overlay records material progress made after that snapshot.

## Experiment 013 — pinned interacting-vacuum source convention

Upstream: `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c`.

The implementation explicitly uses

`Q = H (alpha rho_m + beta rho_v)`.

Its background therefore obeys

`d rho_m/d ln a = -(3+alpha) rho_m - beta rho_v`,

`d rho_v/d ln a = alpha rho_m + beta rho_v`.

Writing `y=(rho_m,rho_v)^T`, the system is `y'=M y` with

`M=[[-(3+alpha),-beta],[alpha,beta]]`.

The eigenmode exponents are

`lambda_+- = [-(alpha-beta+3) +- S]/2`,

`S=sqrt[(alpha+beta+3)^2-4 alpha beta]`,

matching the exact power laws implemented in upstream `background.c`.

At `alpha=beta=0`, `rho_m=rho_m0 a^-3`, `rho_v=rho_v0` exactly. Experiment 013 independently compared the transcribed analytic source solution with direct ODE integration: maximum tested normalized discrepancy ~`5.93e-12`; zero-coupling and eigenvalue checks are at machine precision.

**Status:** source-level PASS; full CLASS_IV Boltzmann regression still OPEN.

## Experiment 014 — pinned GDM zero-closure limit

Upstream: `s-ilic/gdm_class_public@4c87916aab5ca124a68f1dd16f31846fc13d1829`.

For all-zero GDM equation-of-state bins, upstream `rho_gdm_of_a` reduces to

`rho_gdm(a) = rho_gdm0 a^-3`.

The perturbation source defines

`Pi_nad=(cs2-ca2)[delta+3 Hconformal(1+w) theta/k^2]`.

The GDM equations are

`delta' = -(1+w)(theta+M_cont) + 3 Hconformal[(w-ca2)delta-Pi_nad]`,

`theta' = -(1-3ca2)Hconformal theta + k^2/(1+w)(ca2 delta+Pi_nad) + M_Euler - s2 k^2 shear`.

For `w=ca2=cs2=0`, `Pi_nad=0`; with zero shear these become the pressureless-CDM continuity/Euler equations. For dynamic shear upstream uses

`shear'=-3 Hconformal shear + (8/3) cv2/(1+w)(theta+M_shear)`;

therefore `cv2=0` preserves zero shear.

The leading adiabatic GDM initial conditions also become CDM at zero closure: `delta_gdm=3/4 delta_gamma` at leading radiation-era order, `theta_gdm=0`, `shear_gdm=0`.

### Crucial finite-start caveat
When GDM is enabled, the upstream initial-condition branch deliberately omits several standard CLASS matter-radiation corrections proportional to `omega*tau`; it requires `start_small_k_at_tau_c_over_tau_h <= 1e-6`. Consequently the full-solver zero-GDM gate must test **convergence as the start is moved earlier**, not require bitwise equality at one fixed finite start.

For the explicitly isolated photon-density term,

`delta_gamma_CLASS = -(k tau)^2/3 (1-omega tau/5) R`,

`delta_gamma_GDMbranch = -(k tau)^2/3 R`,

so the relative finite-start discrepancy from this term is exactly `omega tau/5` and vanishes linearly as the start is moved earlier. Experiment 014 verifies this scaling numerically.

**Status:** source-level PASS; full GDM_CLASS clean-room spectra regression OPEN.

## Clean-room full-solver gate

Workflow: `.github/workflows/gdm-zero-limit.yml`.

It clones the exact pinned GDM_CLASS commit on a clean Ubuntu GitHub runner, builds CLASS, runs a matched ordinary-CDM case and all-zero-GDM case, compares numerical `.dat` products, and preserves exact configs/logs/environment as an artifact.

The first full-solver run is **calibration-only**. Do not set a tolerance merely to make it pass. First measure the numerical floor and its dependence on the integration start, then freeze a tolerance and rerun as a hard regression gate.

## Exact next actions

1. Execute/read the clean-room GDM regression artifact.
2. Add a start-time sweep (at least several earlier start settings) and measure convergence of background, `P(k,z)`, and `C_ell` differences.
3. Freeze a justified GDM zero-limit tolerance; mark GDM-S1 PASS only then.
4. Build the analogous clean-room `class_iv` alpha=beta=0 regression and freeze its numerical tolerance.
5. Only after these passes should nonzero `cs2`, `cv2`, `w_gdm`, `alpha`, or `beta` be admitted to the six-family common response matrix.
6. G7 law discovery remains blocked until G3B and observational projection/whitening are sufficiently mature.

**Hard boundary remains unchanged: never modify or use RTK as a prior in this repository.**
