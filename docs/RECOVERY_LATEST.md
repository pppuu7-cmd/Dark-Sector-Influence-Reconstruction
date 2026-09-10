# DSIR authoritative recovery — latest

Updated: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-10_ARTICLE3_JK_NOT_CONVERGED_JL_RUNNING_V78.md`, creation commit `afbb75d95a7ce6ccaf11d07a8413c9a4e201fd7c`. Earlier notes remain immutable history.

## Preserved authority
Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; its original atomic native production-vs-dense maximum remains `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI remains validated full-support feasibility with all 107 rows, invalid fraction 0 and native-kpd10-vs20 shared-grid discrepancy 0.0. Exp073JJ remains validated support-only `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, maximum `0.037280144773915974`. Covariance restriction remains unauthorized; Wm_S3 remains unopened.

## Exp073JK validated not converged
Run/job `34495159732 / 102931623100`, head `6490000bd63b68f651c328382a36db03c42c8ccc`, is validated support-only `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Artifact `10160083225`; independently verified ZIP SHA256 `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`; result JSON SHA256 `53aeb88118c004be659755cf1cffa49bed347fe02193f3ef6c2729e102e31181`; capacity patch SHA256 `a0646cff6e8b18814646c9b82ec571c93fc687db62e54e9f71c7333c78f19035`; durable authority commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.

JK compared guarded base N=1024 (1025 requested) versus base N=2048 (2049 requested), native CLASS kpd=20 fixed for both. Maximum atomic relative component difference is `0.016330535730270664 > 1e-3`; JJ-to-JK reduction factor `2.2828488538078164`, interpretation-level empirical order ~`1.1899964460080732`. All 107 rows remain valid, unsupported targets 0, finite/nonzero/row-label/BOSS status unchanged and requested-node coordinate mismatch <=`1.6531028205966003e-16`. This is valid numerical non-convergence, not infrastructure failure.

## Current process — Exp073JL
Exp073JL prospectively tests the immediately next sequential resolution step: guarded base N=2048 (2049 requested) versus base N=4096 (4097 requested). It preserves exact Exp073IR support/traversal, pinned CLASS-IV/public `d_m`, native kpd=20 for both suites, centered-cubic ln(k), `h=1e-4`, `REL_TOL=1e-3`, masks and physical domain.

Preregistration commit `608fbf5fd9912b9f0244283d940a7adfecc41ac8`; implementation `43e1d74e8216c1ff66bfe4d0eed372673d0e5b1b`; workflow/launch head `d556db87763637dd90ed919dbe5d85ef95b4beb1`.

Authoritative workflow/run/job: `exp073jl-article3-layerb-common-grid-third-refinement-convergence-v0-1 / 34497160814 / 102938434376`; GitHub-hosted `ubuntu-24.04`; last observed state IN_PROGRESS after prospective JL contract and JK/JI authority enforcement passed. Self-hosted ownership none; checkpoint N/A.

Response-blind infrastructure capacities were prospectively enlarged only as required by the 4097-node serialization: `_MAX_NUMBER_OF_K_FILES_=4608`, `_ARGUMENT_LENGTH_MAX_=131072`. No scientific quantity or threshold changed.

JL is support-only +0/+0 in every valid outcome. Exact next action: terminal-consume `34497160814`, inspect raw logs, independently verify artifact ZIP/result/capacity hashes, classify against the frozen JL contract, and launch the next permitted nonduplicating gate in the same iteration when terminal.

Global frozen boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
