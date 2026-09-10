# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JF_IMPORT_REPAIR_RERUNNING_V71.md`, creation commit `f223905c0a501aa5d6b6624353945f29e6f37647`.

## Newly closed
- Repaired Exp073IR `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`; exact convergence maximum `0.9998247463807295 > 1e-3`; 0 invalid rows, f_B=0, retained 107; covariance unauthorized.
- Exp073JE `34474978911 / 102863474356` is validated support-only `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0`, artifact `10151168583`, independently verified ZIP SHA256 `cf2e70a8bb35dcdb782d49fe5a29b908f6897169d6fe2c055c9b92eb1bfa01af`; durable authority commit `169da05db02bdeee7cccb3a62bd5aad4ca275cad`.
- Exp073JF attempt 1 `34480017627 / 102880180988` is infrastructure/software failure `+0/+0`: all prerequisite/build steps succeeded, then direct script import failed with `ModuleNotFoundError: No module named 'ci'` before numerical execution/artifact creation.
- Smallest import-only repair commit `1cd0692454e238162be0235f56e49453b4f40999`; workflow/import-regression launch commit `2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`.

## Current authoritative process — repaired Exp073JF
- workflow: `exp073jf-article3-layerb-shared-fixed-k-grid-extended-density-v0-1`;
- run ID: `34480349238`;
- job ID: `102881291672`;
- branch/head: `main / 2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`;
- preregistration commit: `34136c87f49bf990d16670ca984c239194056db2`;
- implementation original commit: `579dab75cd78d19ca05cb406c2c8852b52bc7f3e`;
- import-only repair commit: `1cd0692454e238162be0235f56e49453b4f40999`;
- workflow/launch commit: `2e5e43de2abaec3be93f5fe1a2fbe909b6e86048`;
- checkpoint namespace / last durable checkpoint: N/A (GitHub-hosted support diagnostic);
- start/registration: `2026-09-10T13:04:03Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- current state: IN_PROGRESS at last inspection;
- expected support classifications: `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0` or `INVALID_INFRA_PLUS_0_PLUS_0`;
- frozen diagnostic: N={384,512}, same shared geomspace physical-k domain, same two historical probes, exact kpd={10,20}, exact h=1e-4, unchanged REL_TOL=1e-3;
- scientific effect: always +0/+0; no Layer-B/covariance/model/Wm_S3 authority.

### Exact next transitions
Terminal valid observation: independently verify raw log and artifact ZIP/result hashes. If at least one N is a frozen scaling candidate, nominate the smallest N only for a new prospectively frozen full-support feasibility audit. If neither qualifies, declare the tested simple global geomspace density architecture numerically inadequate through current exact capacity and continue with interpolation phase/curvature or another grid-invariant mechanism diagnostic.

Infrastructure invalid: diagnose the first causal defect and repair only the support diagnostic. Never alter Exp073IR science, REL_TOL=1e-3, h=1e-4, k/z domains, source definitions, atomization or covariance firewall.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.
