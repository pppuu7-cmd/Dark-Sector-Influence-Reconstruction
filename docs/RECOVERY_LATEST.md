# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_IC_CANDIDATE_ID_STABILITY_PASS_MAPPING_FRONT_V47.md` (creation commit `4b3c138105671e1a58df15673c0038979d77cae6`). Earlier recovery notes remain immutable history.

## Preserved scientific authority
All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`. No C2 prediction/model scientific authority exists.

## C2 tangent numerical authority
Reference HT/HU/HV/HW and tangent HZ/IA/IB-v0.2 remain preserved; IB v0.1 remains historical `IMPLEMENTATION_PROVENANCE_FAIL_PLUS_0_PLUS_0`, not scientific FAIL.

Exp073IC run `34249380208 / 102139612475`, artifact `10065344213`, ZIP SHA256 `e48b0fd4f7d80717231df60a5065d9f1eac37a13193951f17d01ee34761ff7dc`, canonical response SHA256 `e97ef98a5b137081df5937454f02576d30e726266e9c50733bf399a9be2b1907` passed as `TANGENT_RESPONSE_CANDIDATE_PLUS_0_PLUS_0`.

Exp073ID was frozen before inspecting IC inter-scale relationships. ID run `34249671091 / 102140579398`, head `9e6ba30de55a2fa3f63a6d47d22015aa6cfa2265`, artifact `10065453571`, ZIP SHA256 `e09efcb7095aedc0ad50d0aa7212cd4f1a44abf63cfc2fd5926906c390f7af77` passed the exact no-tolerance rule at all `56/56` coordinate-direction checks: `abs(D(1e-4)-D(1e-3)) <= abs(D(1e-3)-D(1e-2))`. Raw token `PASS_EXP073ID_C2_TANGENT_RESPONSE_MONOTONE_SCALE_STABILITY_ADMISSION_V0_1`; classification `TANGENT_RESPONSE_NUMERICALLY_ADMITTED_PLUS_0_PLUS_0`; `tangent_response_ready=true`, `admitted_base_step=1e-4`.

C2 boundary is now: `mapped_reference_coordinate=true`, `mapped_tangent_coordinate=true`, `response_candidate_created=true`, `tangent_response_ready=true`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current frontier — Exp073IE six-component residual mapping source audit v0.1
The frozen DSIR-4 mapping contract now controls the next transition. A model must have an explicit six-component residual mapping under `X_munu=M0^2G_munu-T_known_munu` before `G_DOMAIN_MAPPING` can become testable.

Exp073IE prereg: `docs/dsir4/prereg/EXP073IE_C2_SIX_COMPONENT_RESIDUAL_MAPPING_SOURCE_AUDIT_V0_1.md`; creation commit `10120c2ba5e28362939fed379633ec77255b1699`; blob `35d2979d271934758aaa166a9e6280874c695c5e`. Workflow/head commit `83f997a52fe6c297599a3eaf04539c63e50a8b6f`; run `34250165394`, job `102142253548`; GitHub-hosted ubuntu-24.04; home/self-hosted runner free; state at pointer update: QUEUED.

IE is support-only. It audits exact pinned `kaeonikc/class_iv@ac627d54e9ce196a08878d1ba33999819925d19c` source and synchronous baseline for source evidence of all six residual components and the interaction convention. Even on PASS it may set only `six_component_source_mapping_ready=true`; `mapping_ready=false`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE` remain mandatory.

## Exact next transition
Consume IE terminal raw log. If all six source mappings are proven, freeze a separate versioned C2 mapping artifact/admission that binds formulas, source hashes, gauge, total-sector convention, certified domain and tangent-response provenance. If IE fails because a component is not source-proved, preserve ID numerical tangent authority and pursue only the smallest prospective extractor/derivation needed for that missing component.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
