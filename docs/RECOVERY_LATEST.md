# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HV_DECODE_PASS_HW_REFERENCE_BRIDGE_FRONT_V42.md` (creation commit `65f4ddf0701ece5fb60d656519c117da23581cfd`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

No C2 scientific/model authority exists.

## C2 admitted and decoded authority

Exp073HT `34235038323 / 102090438079` is validated `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`, artifact `10061693504`, ZIP digest `sha256:9f544297b90d1fed51c78d98be4737b97e2066b2a06b96bb314ccc9b9c3242d0`, aggregate `1792` bytes SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`.

Exp073HU `34242025242 / 102114346415` is raw-log validated `RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`; authority blob `dbcc251cb6534112929c937deb9da6323d3be4f7`.

Exp073HV `34242333899 / 102115404956`, head `0687ca5ac973dc50340090213ceaaff70ecc6e04`, is raw-log/artifact validated `DECODED_RECORD_SET_PLUS_0_PLUS_0`. Artifact `10062495891` digest `sha256:8ea9cf3baca04f181b97f58f19f04c798bfb14b02af271580c83e82f2900c49e`; canonical exact-hex decoded JSONL SHA256 `95c5b71d5bbbe3492f5bddccaea572644ff84823b244c3c3bc46fd18b389d552`. Durable decode authority blob `36df02975587d7c1b456cee982b01210185dbda2`.

Current C2 boundary is `raw_record_set_admitted=true`, `decoded=true`, `mapped=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current frontier — Exp073HW reference Delta_m bridge v0.1

HW is prospectively frozen from the pre-existing C2 bridge `Delta_m=delta_m+3*a*H*theta_m/k^2` for pressureless matter, using pre-transform native decoded variables exactly once.

- prereg `docs/dsir4/prereg/EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1.md`, commit `70bd7fb5dbe43fffa10394f245ea38ca4864ee15`, blob `017ecaa735398e8e1515003c1a8092d61f5e284a`;
- workflow `.github/workflows/exp073hw-c2-reference-deltam-bridge-v0-1.yml`, implementation commit `ab4f764418566a39c03a002eee9e2703b76aadf5`, blob `19ef77c74162462843c66c7350c59d354a5727d9`;
- binding/head commit `0cc263daa9dafe22fecb29aa640a034caee1db3e`;
- run `34242852819`, job `102117188431`;
- GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner none;
- state at pointer update: `IN_PROGRESS`; frozen binding and bridge-contract checks passed.

HW is reference `(alpha,beta)=(0,0)` only. Its PASS ceiling is `REFERENCE_DELTAM_BRIDGE_PLUS_0_PLUS_0`; it cannot create tangent response, prediction-ready state, G-domain decision or scientific authority.

Expected token: `PASS_EXP073HW_C2_REFERENCE_DELTAM_BRIDGE_V0_1`.

## Exact next transition

On HW terminal state, consume raw log and artifact, verify digest/receipt/28-row canonical bridge output and frozen arithmetic/provenance. Only then record reference-bridge authority. The next permitted scientific branch is prospectively frozen generation/admission of nonzero alpha/beta tangent records plus matched-reference response construction required by the original C2 extraction contract; no downstream gate may use HW alone as a prediction.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
