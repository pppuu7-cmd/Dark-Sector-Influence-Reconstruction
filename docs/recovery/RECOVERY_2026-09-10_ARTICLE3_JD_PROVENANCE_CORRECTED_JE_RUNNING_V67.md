# DSIR recovery V67 — Exp073JD provenance corrected; Exp073JE running

Date: 2026-09-10. Scope: DSIR only. Never mix RTK or RQIR.

## Preserved scientific authority
All prior admitted DSIR scientific authority remains unchanged. Repaired Exp073IR run/job `34432102035 / 102729564736` remains `NUMERICALLY_UNRESOLVED_EXP073IR`: 0 invalid rows, `f_B=0`, retained 107, exact native production-vs-dense maximum `0.9998247463807295 > REL_TOL=1e-3`; covariance restriction remains unauthorized. No tolerance, rounding, smoothing, averaging, effective-coordinate or fiducial-P rescue is permitted.

Historical Exp073CM remains resource/performance `+0/+0`, not Wm_S3 scientific arithmetic authority. Wm_S3 remains unopened.

## Exp073JD — validated support result, provenance correction only
Exp073JD run/job `34472918931 / 102856790715`, head `00994fba5f77100a3ffff11f205abb3be5e1a1dc`, artifact `10150322510`, raw token `PASS_EXP073JD_EXACT_K_ORIGINAL_PAIR_OBSERVED_V0_1`, remains support-only `EXACT_K_ORIGINAL_PAIR_OBSERVED_PLUS_0_PLUS_0`.

An independent re-download exposed a provenance metadata defect in authority V0_1: its recorded artifact ZIP and result-JSON SHA256 values were incorrect. Scientific observations, run/job/artifact identity, raw token and classification were correct. V0_1 is preserved as immutable history; corrected provenance authority V0_2 was added in commit `1fcc02d6d252d3f47184be565218cf29355c3c8c`.

Correct verified hashes:
- GitHub artifact digest = `sha256:310939a4b4ef8d75cb027630e5f43f88003ab92045c0af6e83ab83764bcb6365`;
- independently downloaded ZIP SHA256 = `310939a4b4ef8d75cb027630e5f43f88003ab92045c0af6e83ab83764bcb6365`;
- contained `exp073jd_result.json` SHA256 = `ba26c2a89a41d67e65bbf0b630659fccae33d85a7d05c2d0d4d493f8b33dfccb`.

The raw artifact confirms exact internal-k responses are identical across kpd 10 and 20 at both historical worst probes: alpha-left `11.514018402323245`, beta-symmetric `1.9210920856949087`, with exact relative discrepancy `0.0` and coordinate mismatch `0.0`. This does not retroactively PASS Exp073IR.

## Current process — Exp073JE shared fixed-k grid scaling diagnostic
A separate DSIR process prospectively preregistered and launched Exp073JE after validating the JD numerical result. Repository authority wins over stale chat state.

- preregistration commit: `2cb38664443bd17dfc2d304c1ecb21ed32b0e1dd`;
- implementation commit: `67ce16ca1e92adbb98117dd5786fd179e793c929`;
- launch/head commit: `257ef3295e09870df02e681275f828c9bceab8bf`;
- workflow: `exp073je-article3-layerb-shared-fixed-k-grid-scaling-v0-1`;
- run/job: `34474514433 / 102861967751`;
- runner ownership: GitHub-hosted `ubuntu-24.04`; home/self-hosted ownership none;
- checkpoint namespace: N/A (hosted support diagnostic);
- expected classification: support-only `SHARED_FIXED_K_GRID_SCALING_OBSERVED_PLUS_0_PLUS_0` or fail-closed `INVALID_INFRA_PLUS_0_PLUS_0` according to the frozen JE contract;
- last observed state: IN_PROGRESS; contract/lineage and frozen Python stack completed, pinned CLASS-IV build in progress.

JE uses shared model-invariant physical-k grids with N in `{64,128,256}`, the original kpd `{10,20}` cross-check, frozen `h=1e-4` and historical `REL_TOL=1e-3`; it is diagnostic only and cannot authorize Layer-B science or covariance restriction.

## Exact next action
Terminal-consume run `34474514433`: inspect raw job log and artifact, verify source patch scope, hashes, fixed-node coordinate provenance, raw token and every frozen scaling-candidate condition. If a valid smallest N satisfies both exact-reference error and kpd10-vs-kpd20 discrepancy `<1e-3` for both probes, nominate that N only for a separately prospectively frozen full-support feasibility/audit. Otherwise continue numerical mechanism isolation without tolerance rescue.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; `REL_TOL=1e-3`; finite-difference `h=1e-4`; exact-threshold ambiguity `numerically_unresolved`.
