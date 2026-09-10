# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JI_FEASIBLE_JJ_RESOLUTION_RUNNING_V75.md`, creation commit `831c1ee06e286241689a080cfda120676757c499`.

## Newly closed
- Repaired Exp073IR `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`; exact convergence maximum `0.9998247463807295 > 1e-3`; 0 invalid rows, f_B=0, retained 107; covariance unauthorized.
- Exp073JH `34487047656 / 102903883547` is validated support-only `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`; failure was only finite centered-cubic boundary support.
- Exp073JI `34488466425 / 102908710275` is validated support-only `GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0`; artifact `10156878354`; independently verified ZIP SHA256 `f8492ca04ff3b159ffe28003d28c3756e428e9851f4a3af56e6f343666d1b0de`; result SHA256 `c076af1fd5207d69c3fdc00f944ca2099aa4a4e82e31d0d0ce2877f3b679310a`; durable authority commit `bba2701467e8fce6bf41369c23e64be4d16f78f9`.
- JI geometry requires lower guards 0, upper guards 1, total requested nodes 513, and preserves the N=512 base lattice bitwise. Unsupported evaluations 0; kpd10-vs20 max relative difference 0.0; invalid rows 0; retained 107.

## Current authoritative process — Exp073JJ
- workflow: `exp073jj-article3-layerb-common-grid-resolution-refinement-convergence-v0-1`;
- run ID: `34492300395`;
- job ID: `102921844345`;
- branch/head: `main / f47683ebda4f00e536c2e630930d3e3b76fed80f`;
- preregistration commit: `aaf5ccb8860b95310bb19450cf5af533383e897b`;
- implementation commit: `f9b4ddf8fd778098c9874469ea328c6b93a56149`;
- workflow/launch commit: `f47683ebda4f00e536c2e630930d3e3b76fed80f`;
- checkpoint namespace / last durable checkpoint: N/A (GitHub-hosted support-only convergence audit);
- start/registration: `2026-09-10T14:55:55Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- current state: IN_PROGRESS at last inspection;
- last completed gate: prospective JJ contract and exact JI authority enforcement SUCCESS;
- current step at last inspection: install frozen numerical/build stack;
- architecture: coarse guarded shared physical-k lattice = 513 nodes; fine guarded shared physical-k lattice = 1025 nodes; native CLASS kpd fixed to 20 for both; centered cubic in ln(k);
- expected classifications: `COMMON_GRID_RESOLUTION_REFINEMENT_CONVERGED_PLUS_0_PLUS_0`, `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, or infrastructure invalid;
- scientific effect: always +0/+0; no Layer-B/covariance/model/Wm_S3 authority.

### Exact next transitions
Terminal valid CONVERGED: independently verify raw log and artifact ZIP/result/capacity hashes; then only prospectively freeze a separate scientific Layer-B rerun using a predeclared guarded shared-grid architecture. JJ itself never authorizes covariance.

Terminal valid NOT_CONVERGED: preserve as +0/+0 and isolate the shared-grid resolution/interpolation mechanism without weakening REL_TOL, h, physical domain, atomization or source definitions.

Infrastructure invalid: diagnose the first causal defect, make the smallest infrastructure-only repair, add a reproducible regression where practical, and resume without altering frozen science.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; REL_TOL=1e-3; h=1e-4; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.
