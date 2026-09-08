# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HZ_IA_PASS_IBV02_MAP_PASS_IC_RESPONSE_FRONT_V46.md` (creation commit `f352ccb2ad11652a2b512c275bb6244a276332b7`). Earlier recovery notes remain immutable history.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. No C2 scientific/model authority exists.

## Preserved C2 chain
Reference HT/HU/HV/HW remains validated. Tangent HY was independently consumed and HZ run `34248477503 / 102136488451` admitted the nine raw model artifacts. IA run `34248722000 / 102137324616`, artifact `10065081303`, ZIP SHA256 `6bf115c76d538f0691c1fcfa9d9a26721b9b593f26aceb2a7a59bdb7cc9aa0ce` exactly decoded all tangent packets and passed as `TANGENT_DECODED_RECORD_SET_PLUS_0_PLUS_0`.

IB v0.1 run `34248841106 / 102137736842` is preserved historically as `IMPLEMENTATION_PROVENANCE_FAIL_PLUS_0_PLUS_0`: its source expression did not explicitly preserve HW's frozen operation order, although independent audit and v0.2 regression found exactly 0/252 resulting binary64 differences. This is not a scientific FAIL.

IB v0.2 is the authoritative mapped tangent result: prereg blob `69c8e313cbe95ee426ba23112d63548c9ab26556`; run `34249229753`, job `102139059309`, head `f2196c40d1608aa66b20bf4431ce3e7763970a38`, artifact `10065286473`, ZIP SHA256 `965e921224f516e76e9cf2d2ac84ed51a5027b97d79c73c87620d55a83011201`; raw PASS `PASS_EXP073IB_C2_TANGENT_DELTAM_COMMON_COORDINATE_MAP_V0_2`. It executes exact HW order `hconf=a*H`, `velocity_term=3.0*hconf*theta_m/(k*k)`, `Delta_m=delta_m+velocity_term`; regression exact-equality count 252. Classification `TANGENT_MAPPED_COMMON_COORDINATE_PLUS_0_PLUS_0`; `mapped_tangent_coordinate=true`, `tangent_response_ready=false`.

## Current frontier — Exp073IC tangent finite-difference response candidate v0.1
- prereg creation commit `7d94f9f9bfaa3b320250c7b046d2a6c7a37309b5`, blob `9e1235a48a4288bb2083d69084f1cae7d79847bb`;
- workflow/head commit `f3475f5d409a50c31fb1eda3870837542797e091`;
- run `34249380208`, job `102139612475`;
- GitHub-hosted ubuntu-24.04; home/self-hosted runner free;
- state at pointer update: QUEUED.

IC calculates only deterministic response candidates from frozen HX definitions: alpha one-sided negative and beta symmetric at exact h=`1e-4,1e-3,1e-2`, with `1e-4` base and larger scales controls. No stability threshold, scale selection, extrapolation, smoothing, prediction or scientific authority is permitted. Expected PASS: `PASS_EXP073IC_C2_TANGENT_FINITE_DIFFERENCE_RESPONSE_CANDIDATE_V0_1`; even on PASS `tangent_response_ready=false` until a separate prospectively frozen stability/admission gate.

## Exact next transition
Consume IC terminal raw log and artifact. If exact candidate PASS, freeze the stability/admission rule **before inspecting scale relations for acceptance**. Never choose a favorable scale or threshold post hoc. On infrastructure/provenance failure, repair only the first causal defect while preserving HW/IA/IB v0.2 authority.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
