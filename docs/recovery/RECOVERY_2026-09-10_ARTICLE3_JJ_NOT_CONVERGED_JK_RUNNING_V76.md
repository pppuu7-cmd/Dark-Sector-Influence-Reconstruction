# DSIR recovery V76 — Exp073JJ not converged; Exp073JK second refinement running

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority
Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: original retained 107 coordinate rows, atomic native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction unauthorized. Historical Exp073CM remains resource/performance `+0/+0`; Wm_S3 remains unopened.

Validated Exp073JI full-support feasibility remains support-only `GUARD_NODE_FULL_SUPPORT_FEASIBLE_PLUS_0_PLUS_0`: all 107 rows retained, invalid-row fraction 0, unsupported target evaluations 0, kpd10-vs20 maximum relative component difference 0.0 on the guarded shared-grid architecture.

## Newly closed — Exp073JJ
Validated support-only classification `COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`. Run/job `34492300395 / 102921844345`, head `f47683ebda4f00e536c2e630930d3e3b76fed80f`, raw token `PASS_EXP073JJ_COMMON_GRID_RESOLUTION_REFINEMENT_NOT_CONVERGED_V0_1`.

Artifact `10158706262`; GitHub-upload digest and independently downloaded ZIP SHA256 `079c08b7b8d62a775f5111b5696c41dd60babb2449b9f129d2518d1324908d14`; result JSON SHA256 `a62a2f7f756789f7502dd5a076137b73d6537235b605ad5a3c1a0a7e0f244494`; capacity-patch JSON SHA256 `f306503afab4b24bcbf03a7adf96841da986e1d8bb0486c873a267632254645c`. Durable authority commit `283a86b3c66bd431c53cfbe1419bf475d6c3ffe1`.

JJ compares guarded shared lattices base N=512 (513 requested) and base N=1024 (1025 requested), with CLASS native `k_per_decade_for_pk=20` fixed for both suites, unchanged centered-cubic ln(k) interpolation and inherited full atomic support. Result: maximum atomic coarse-vs-fine relative component difference `0.037280144773915974 > 0.001`; finite/nonzero status unchanged; row labels unchanged; BOSS dense-z status unchanged. Unsupported target evaluations 0; invalid rows 0; invalid-row fraction 0; retained rows 107. Requested-node coordinate mismatch remained below `1.653e-16`.

Interpretation: the shared-grid architecture is fully feasible and support-preserving, but N=1024 is not yet demonstrably resolution-converged against N=512 at the frozen threshold. This is a valid negative numerical convergence result, not an infrastructure failure. It creates no scientific/covariance/Wm_S3 authority.

## Current process — Exp073JK
Purpose: measure the immediately next shared-grid refinement step, comparing guarded base N=1024 (1025 requested nodes) to guarded base N=2048 (2049 requested nodes), while keeping every physical and numerical rule unchanged.

Prospective preregistration commit `5340e0964f13ad0fbcba6360c55bdef1b1c1c165`; implementation commit `fc940f4b974a0fe91a317931a9a0395d9b99ea56`; workflow/launch head `6490000bd63b68f651c328382a36db03c42c8ccc`.

Frozen JK rules: same exact Exp073IR parent lineage and 53 DES + 54 BOSS retained rows; same atom traversal; pinned CLASS-IV `ac627d54e9ce196a08878d1ba33999819925d19c`; same public gauge-invariant `d_m`; native CLASS kpd fixed to 20 for both suites; centered-cubic Lagrange interpolation in ln(k); finite-difference `h=1e-4`; `REL_TOL=1e-3`; same target range and JI geometry SHA `79bae6f3015ccf524402d7f0f357070a903126bfa8d3bd3f4cac5902afef093a`.

Infrastructure-only capacity is prospectively enlarged to `_MAX_NUMBER_OF_K_FILES_=2304` and `_ARGUMENT_LENGTH_MAX_=65536`, with one-replacement and pre/post SHA provenance mandatory. No equation, observable, mask, estimator, threshold or physical domain changes are permitted.

Authoritative workflow/run/job: `exp073jk-article3-layerb-common-grid-second-refinement-convergence-v0-1 / 34495159732 / 102931623100`. GitHub-hosted `ubuntu-24.04`; self-hosted ownership none; checkpoint N/A. Last observed state IN_PROGRESS: prospective JK contract and JJ/JI authority enforcement passed; frozen numerical/build stack installation in progress.

JK is support-only `+0/+0` in every valid outcome. If max atomic 1024-vs-2048 difference is `<1e-3` with all inherited support/status invariants, classify converged and only then design a separate prospectively frozen scientific Layer-B rerun. If not converged, record the empirical JJ-to-JK reduction factor and prospectively freeze the next resolution step without tolerance rescue.

Exact next action: terminal-consume run `34495159732`; inspect raw logs; independently verify artifact ZIP/result/capacity hashes; classify against the frozen JK contract; if terminal valid, launch the next permitted nonduplicating gate in the same iteration.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; judged `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging/effective-coordinate/fiducial-P rescue.
