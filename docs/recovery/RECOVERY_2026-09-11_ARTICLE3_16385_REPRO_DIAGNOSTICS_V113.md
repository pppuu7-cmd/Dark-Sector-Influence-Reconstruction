# DSIR recovery V113 — 16385 reproducibility diagnostics closed, science still active

Date: 2026-09-11. Scope: **DSIR only**. This immutable note supersedes V112 for current-front recovery while preserving V112 and all earlier notes as historical authority.

## Frozen scientific frontier
Exp073JM canonical 4097→8193 remains independently verified `COMMON_GRID_FOURTH_REFINEMENT_NOT_CONVERGED_PLUS_0_PLUS_0`, max relative component difference `0.01070806986822778` versus strict `<1e-3`. Frozen `REL_TOL=1e-3`, `h=1e-4`, native kpd20, centered-cubic interpolation, exact physical domain/masks/107-row accounting, invalid fraction `<=0.05`, retained `>=15`, unsupported=0 and lookup ceiling `1e-12` are unchanged. Covariance restriction remains unauthorized and Wm_S3 remains unopened.

The singular authoritative canonical 8193→16385 scientific-support run remains active: workflow `post-jm-next-support-canonical-8193-to-16385-v0-1`, run/job `34555022975 / 103125734913`, head `c56940a0093fc6769b9a48cb3d5056b70075130c`. All authority/resource identities, frozen numerical stack, CAMB/CLASS-IV build, DES/Layer-A/BOSS inputs are PASS; the step `Execute frozen canonical 8193 to 16385 support refinement with telemetry` is still `IN_PROGRESS`. Do not duplicate it or inspect partial scientific values for tuning.

## Newly closed +0/+0 numerical diagnostics
Durable combined authority: `docs/dsir4/authority/LAYERB_16385_REPRO_AND_NOISE_DIAGNOSTICS_V0_1.json`, creation commit `12aa3d29aef760b5bcf2ae50520e75d2e0b07781`.

### Cross-VM canonical-16385 numerical reproducibility
Run `34556173778`, head `79dd7a1fcb70157b2955f6d83cc302578ccface0`; probe jobs `103129226488` and `103129226591`; compare job `103133339788`. Comparison artifact `10183110033`, ZIP SHA256 `169c5d03f5dceeba444c87f830a99d24ffeda845c65344db51f4a96a44309be1`, `comparison.json` SHA256 `9d56c990ff54e9ebaf326257a72bec5c712ac25d38d4d583e27c357d80f7a40f`.

Classification: `LAYERB_16385_CROSS_VM_NUMERIC_REPRO_DIAGNOSTIC_PASS_PLUS_0_PLUS_0`. Raw sampled role operands were not bitwise identical across VMs, but their maximum symmetric relative difference was only `1.494084432755005e-15` and maximum absolute difference `2.7284841053187847e-12`. Pilot derivative responses differed by at most `3.285358946556587e-11` symmetric relative and `9.094947017729282e-09` absolute. The current full 16385 scientific result was not read; no scientific authority or next-rung authorization was created.

### Intra-VM canonical-16385 repeatability
Source run `34557144684`, head `58839fbc7efd594572d3a63a0b019c080196a687`, role jobs `103132094675 / 103132094630 / 103132094483 / 103132094595`. Event-driven aggregate run/job `34557921258 / 103134458183`, artifact `10183242971`, ZIP SHA256 `b063651e237ac5954cdcf95670c4cb913199c8ef8c70bebb71108c77dcb56eaf`, `aggregate.json` SHA256 `dc175a82f698782178ce6e3a4520ba27c6994f7bf4a13ee13032bb72dc90501a`.

Classification: `LAYERB_16385_INTRA_VM_REPEATABILITY_AGGREGATE_DIAGNOSTIC_PASS_PLUS_0_PLUS_0`. All four roles were bitwise repeatable across two same-VM constructions: global max absolute difference `0.0`, global max symmetric relative difference `0.0`, with max-one-live and no scientific traversal. This is strong execution-repeatability evidence, not a scientific convergence result.

### Pre-result finite-difference/noise budget
Run `34557228533`, head `6df3df9c314360dccb340991a21e3580fdb249b1`. Amplification job/artifact `103132351219 / 10182994471`, ZIP SHA256 `cc9aa2908fa94b849c2edf51e241ca39786ae998bb3ce2aef8b6cf5ea8b208c7`, JSON SHA256 `1ff3907f3b2d10870efc5d6ad7291833ed4c2e4d6c3c8cdb919fb16969c49616`. Correlation Monte Carlo job/artifact `103132351356 / 10182995486`, ZIP SHA256 `c387ccb94f6ab62e606ab06db554c77efe59ab9963029f6df4e3760520d509c2`, JSON SHA256 `2783741de80169a915578858d19a8844464fe917f27044c334b30182a2a60390`.

Both classify as interpretation-only `PASS_PLUS_0_PLUS_0`. At frozen `h=1e-4`, finite-difference amplification can in principle convert raw operand perturbations at roughly `1e-7` to `1e-6` scale (depending derivative scale and correlation) into percent-level derivative disagreement. However, the measured cross-VM raw-operand variability above is only about `1e-15` relative at the sampled points, far too small by itself to explain the historical ~`1e-2` plateau. Therefore ordinary cross-VM nondeterminism is strongly disfavored as the dominant cause; structured grid-to-grid/solver discrepancy or another mechanism remains possible.

## Interpretation boundary
These diagnostics were frozen and executed without reading the current 8193→16385 scientific result. They may guide a future plateau/root-cause decision stage only if the active frozen classifier returns NOT_CONVERGED. They do not alter `h`, tolerance, grids, masks, interpolation, estimator, stopping rule, covariance authority or Wm_S3 status, and they do not authorize 32769.

## Current compute lanes
At this recovery freeze, the only scientifically authoritative active heavy lane is `34555022975 / 103125734913` (`IN_PROGRESS`). The cross-VM, intra-VM and noise-budget lanes are terminal and fully consumed. Their event-driven aggregation/compare artifacts are durable. No self-hosted/home runner ownership is required.

## Exact next actions
1. Keep `34555022975` singular and terminal-consume its artifact/validator receipt as soon as it finishes.
2. If independently verified CONVERGED, activate only the already prospectively frozen and static-audited fresh post-16385 closure adapter; do not reuse the old direct-JM helper as-is.
3. If independently verified NOT_CONVERGED, do not invent or launch 32769. Enter a separately prospective numerical plateau/root-cause decision stage, using the closed response-blind reproducibility/conditioning authorities only as interpretation inputs.
4. If infrastructure-invalid, repair only the first causal execution/provenance defect while preserving all frozen science and closed authorities.

## Readiness
`ARTICLE3_REPOSITORY_READINESS = 68%`; funnel-freeze readiness `=67%` pending the independently validated terminal 8193→16385 scientific-support result and a permitted downstream transition.
