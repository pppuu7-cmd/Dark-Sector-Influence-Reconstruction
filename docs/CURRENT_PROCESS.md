# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

Newest immutable recovery authority: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JG_VALIDATED_JH_FULL_SUPPORT_RUNNING_V73.md`, creation commit `b75e430e1194ff5d8b16a7b29b55879a4bc15db0`.

## Newly closed
- Repaired Exp073IR `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`; exact convergence maximum `0.9998247463807295 > 1e-3`; 0 invalid rows, f_B=0, retained 107; covariance unauthorized.
- Exp073JF repaired run `34480349238 / 102881291672` is validated support-only `SHARED_FIXED_K_GRID_EXTENDED_DENSITY_OBSERVED_PLUS_0_PLUS_0`; artifact `10153458465`; independently verified ZIP SHA256 `f71c1603f46e622a6c71ebab6733d30e9633cc92e9dc50a98cecdf364b28fffb`; no N=384/512 scaling candidate.
- Exp073JG `34485992147 / 102900288767` is validated support-only `LOCAL_INTERPOLATION_CURVATURE_OBSERVED_PLUS_0_PLUS_0`; artifact `10155745915`; independently verified ZIP SHA256 `e3282ea5f145a273aff63cd70ff74e23cbf6f19960bb83f8390c2c855ae70dbb`; result SHA256 `3e9cd6c4395e4fc67fafd4805b8e1a0ade7e6f4239a1234be50910ff021869cf`; durable authority commit `da6f566b67872ac505c44181446b015ddffbed4c`.
- JG higher-order candidates: quadratic-left, quadratic-right and centered cubic. At N=512 all have exact kpd10-vs20 equality and both historical exact-k probe errors below unchanged 1e-3. Centered cubic errors `(alpha,beta)=(1.2105247820888992e-07,0.00016088505716613062)`.

## Current authoritative process — Exp073JH
- workflow: `exp073jh-article3-layerb-full-support-grid-invariant-feasibility-v0-1`;
- run ID: `34487047656`;
- job ID: `102903883547`;
- branch/head: `main / 0834a45f5e767d411ce694d081069403ea6fd908`;
- preregistration commit: `57065961d9b49290ccdfd6f23f6e5290c4d7a292`;
- implementation commit: `88d669ee567e85c5363d09db32fa2bcb9ceb08ab`;
- workflow/launch commit: `0834a45f5e767d411ce694d081069403ea6fd908`;
- checkpoint namespace / last durable checkpoint: N/A (GitHub-hosted full-support feasibility audit);
- start/registration: `2026-09-10T14:08:02Z`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- current state: IN_PROGRESS at last inspection;
- last completed gate: prospective contract/JG-authority enforcement SUCCESS;
- current step at last inspection: frozen numerical/build-stack installation;
- architecture: structurally selected balanced `N512_SHARED_PHYSICAL_K_CUBIC_CENTERED_LN_K_V0_1`;
- expected classifications: `FULL_SUPPORT_GRID_INVARIANT_FEASIBLE_PLUS_0_PLUS_0`, `FULL_SUPPORT_GRID_INVARIANT_NOT_FEASIBLE_PLUS_0_PLUS_0`, or infrastructure invalid;
- scientific effect: always +0/+0; no Layer-B/covariance/model/Wm_S3 authority.

### Exact next transitions
Terminal valid FEASIBLE: independently verify raw log and artifact ZIP/result hashes; only then prospectively freeze a separate complete Layer-B scientific rerun using the candidate architecture. JH itself never authorizes covariance.

Terminal valid NOT_FEASIBLE: inspect unsupported target counts, row labels and convergence; prospectively isolate boundary/grid mechanism without changing REL_TOL, density as rescue, z/k domain, atomization or source definitions.

Infrastructure invalid: diagnose first causal defect, make smallest infrastructure-only repair, add a regression where practical and rerun without altering frozen science.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective ell/z/k/fiducial-P shortcut.
