# DSIR recovery V78 — Exp073JK validated not converged; Exp073JL running

Date: 2026-09-10. Scope: **DSIR only**. Never mix RTK or RQIR.

## Preserved authority

All prior admitted DSIR authority remains unchanged. Repaired Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`; its historical atomic native production-vs-dense maximum remains `0.9998247463807295 > REL_TOL=1e-3`. Exp073JI remains validated full-support feasibility with all 107 inherited rows retained, zero unsupported targets and native-kpd10-vs20 discrepancy 0.0 on the guarded shared lattice. Exp073JJ remains validated support-only `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0` with maximum `0.037280144773915974`. Covariance restriction remains unauthorized. Wm_S3 remains unopened.

## Exp073JK terminal validation

Authoritative workflow/run/job:
- workflow `exp073jk-article3-layerb-common-grid-second-refinement-convergence-v0-1`
- run `34495159732`
- job `102931623100`
- launch head `6490000bd63b68f651c328382a36db03c42c8ccc`
- conclusion `success`

The prospectively frozen numerical result is `COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`.

Observed facts:
- guarded base N=1024 / 1025 requested nodes versus base N=2048 / 2049 requested nodes;
- CLASS native `k_per_decade_for_pk=20.0` fixed for both suites despite inherited slot labels 10/20;
- maximum atomic coarse-vs-fine relative component difference `0.016330535730270664 > 1e-3`;
- JJ-to-JK reduction factor `2.2828488538078164`;
- exact-ln(k)-spacing interpretation gives empirical order approximately `1.1899964460080732`;
- invalid-row count 0, invalid fraction 0.0, retained rows 107/107;
- unsupported target evaluations 0 in both suites;
- finite/nonzero status unchanged, row labels unchanged, BOSS dense-z status unchanged;
- maximum requested-node coordinate mismatch `1.6531028205966003e-16 <= 1e-12`.

Independent artifact verification completed after the run became terminal:
- artifact ID `10160083225`;
- Actions ZIP digest and independently recomputed ZIP SHA256 both `a58bedd36365bf8d7a99627b1a39d2bc83f3dae41e3d9a6d3351617caa00dd99`;
- `exp073jk_result.json` SHA256 `53aeb88118c004be659755cf1cffa49bed347fe02193f3ef6c2729e102e31181`;
- `capacity_patch.json` SHA256 `a0646cff6e8b18814646c9b82ec571c93fc687db62e54e9f71c7333c78f19035`.

Durable authority: `docs/dsir4/authority/EXP073JK_ARTICLE3_LAYERB_COMMON_GRID_SECOND_REFINEMENT_NOT_CONVERGED_V0_1.json`, creation commit `bfa641eab5050fb891a3e754fed8eb30ef12586f`.

Interpretation boundary: JK is a valid numerical non-convergence result, not infrastructure failure. It remains support-only +0/+0 and does not authorize covariance restriction, Wm_S3, model authority or manuscript claims.

## Current process — Exp073JL

Exp073JL is the prospectively frozen immediately next sequential resolution test:
- coarse guarded base N=2048 -> 2049 requested nodes;
- fine guarded base N=4096 -> 4097 requested nodes;
- native CLASS kpd=20 for both;
- unchanged centered-cubic Lagrange interpolation in ln(k);
- unchanged finite-difference h=1e-4;
- unchanged `REL_TOL=1e-3`;
- unchanged 107-row inherited support, atom traversal, physical domain and masks.

Preregistration: `docs/dsir4/prereg/EXP073JL_ARTICLE3_LAYERB_COMMON_GRID_THIRD_REFINEMENT_CONVERGENCE_V0_1.md`, creation commit `608fbf5fd9912b9f0244283d940a7adfecc41ac8`.

Implementation: `ci/exp073jl_article3_layerb_common_grid_third_refinement_convergence_v0_1.py`, creation commit `43e1d74e8216c1ff66bfe4d0eed372673d0e5b1b`.

Workflow/launch head: `.github/workflows/exp073jl-article3-layerb-common-grid-third-refinement-convergence-v0-1.yml`, commit `d556db87763637dd90ed919dbe5d85ef95b4beb1`.

Authoritative run/job: `34497160814 / 102938434376` on GitHub-hosted `ubuntu-24.04`. Last observed state: IN_PROGRESS; prospective JL contract and JK/JI authority enforcement passed; frozen numerical-stack installation was in progress. Self-hosted ownership none; checkpoint N/A.

Response-blind pre-result infrastructure audit from the JK iteration showed a 4097-node `.17g` `k_output_values` serialization around 89918 characters. Exp073JL therefore prospectively enlarges infrastructure-only capacities to `_MAX_NUMBER_OF_K_FILES_=4608` and `_ARGUMENT_LENGTH_MAX_=131072`, with exact provenance. No physics, observable, interpolation, threshold, mask or judged domain changes.

JL is support-only +0/+0 in every valid outcome.

## Exact next action

Terminal-consume `34497160814`; inspect raw logs; independently verify artifact ZIP/result/capacity hashes; classify only against the frozen JL contract.

If JL converges (`max atomic relative component difference <1e-3` with all support/status gates intact), preserve JL as support-only authority and prospectively freeze a separate **scientific Layer-B numerical rerun** using a predeclared converged shared-grid architecture. Do not reuse the support gate itself as scientific authority.

If JL is valid NOT_CONVERGED, preserve the negative result and only then prospectively freeze the next sequential refinement gate, with adequate infrastructure capacity and no change to `REL_TOL`, h, interpolation, masks or physical domain.

If JL fails infrastructure, repair only the first causal infrastructure defect while preserving the frozen JL scientific contract.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; h=1e-4; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
