# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HY_RAW_CANDIDATE_HZ_ADMISSION_FRONT_V45.md` (creation commit `c3d7e3d2b8852eef035ae9094f465cc7d83940ff`). Earlier recovery notes remain immutable history.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. No C2 scientific/model authority exists.

## Preserved C2 reference authority
HT raw candidate, HU raw-set admission, HV exact ABI decode and HW reference `Delta_m` bridge remain validated. Reference boundary is `raw_record_set_admitted=true`, `decoded=true`, `mapped_reference_coordinate=true`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Exp073HY consumed
HY run `34243515299`, head `ca3b6a1de8ff96dfc0525ef8485f1ad57e2976b8` is terminal SUCCESS across all nine model units plus manifest verifier. Raw logs and independently downloaded artifacts verify the prospectively frozen nine nonzero model points; each artifact has exactly 28 distinct 64-byte packets, exact z-major/k-minor 1792-byte reassembly, exact receipt/source/run/head/job binding, matching GitHub ZIP SHA256 and aggregate SHA256. HY is classified `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0` only. No decode/mapping/derivative/prediction/scientific authority is created.

Exact nine aggregate SHA256 values and artifact IDs/digests are frozen in V45 and `docs/dsir4/prereg/EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1.md`.

## Current frontier — Exp073HZ tangent raw-set provenance admission v0.1
- prereg creation commit `308a4acd0a4cc5dcc16175235dc2659a8c59cc37`, blob `a4be5047b2968e8b9bc844a3d2bdbd2bc3e6e966`;
- workflow/head commit `edaa94d42b18f45a6e0659dc23399793e0228830`;
- run `34248477503`, job `102136488451`;
- GitHub-hosted ubuntu-24.04; home/self-hosted runner free;
- state at pointer update: IN_PROGRESS.

HZ is provenance/admission only. Expected PASS token: `PASS_EXP073HZ_C2_TANGENT_RAW_SET_PROVENANCE_ADMISSION_V0_1`. On PASS only: `tangent_raw_set_admitted=true`, while `decoded=false`, `mapped=false`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Exact next transition
Consume HZ terminal raw log. On exact PASS, prospectively freeze a separate deterministic tangent ABI decode gate; do not compute tangent derivatives yet. On FAIL, diagnose only the first causal infrastructure/provenance mismatch and preserve the already validated HY artifacts.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
