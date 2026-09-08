# DSIR authoritative recovery — latest

Updated: 2026-09-08. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-08_C2_HW_REFERENCE_PASS_HX_TANGENT_PLAN_FRONT_V43.md` (creation commit `a0244f2594a9590867d77d0ca62d5273983a8db9`). Earlier recovery notes remain immutable history.

## Preserved scientific authority

All prior DSIR scientific authority remains unchanged. Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. Scientifically admitted `WW_S3_S3` remains run `34218457380 / 102035691774`, GA artifact `10051382493`, digest `sha256:a192f50de34dc74f575b86e8ff1e6f7c92b9a9bb009d9d0ea6ff4ff6208f4109`.

No C2 scientific/model authority exists.

## C2 authority through reference common coordinate

- HT `34235038323 / 102090438079`: validated `RAW_RUNTIME_CANDIDATE_PLUS_0_PLUS_0`, artifact `10061693504`, raw aggregate SHA256 `905d01d986e38baca0924937e7bd54db901a53853ffd138427e892fe25039fb4`.
- HU `34242025242 / 102114346415`: validated `RAW_RECORD_SET_ADMITTED_PLUS_0_PLUS_0`, authority blob `dbcc251cb6534112929c937deb9da6323d3be4f7`.
- HV `34242333899 / 102115404956`: validated `DECODED_RECORD_SET_PLUS_0_PLUS_0`, artifact `10062495891`, digest `sha256:8ea9cf3baca04f181b97f58f19f04c798bfb14b02af271580c83e82f2900c49e`, decoded JSONL SHA256 `95c5b71d5bbbe3492f5bddccaea572644ff84823b244c3c3bc46fd18b389d552`, authority blob `36df02975587d7c1b456cee982b01210185dbda2`.
- HW `34242852819 / 102117188431`: validated `REFERENCE_DELTAM_BRIDGE_PLUS_0_PLUS_0`, artifact `10062705321`, digest `sha256:7ea327f0d6e29e4b415c9f66201b266e9015d46a383e8867de94b05665517c00`, bridge JSONL SHA256 `2b6eb07c99273292bcb2cf929295071e401e81ed51cfe3f4c3b19d5a395518fb`, authority blob `69d617ebfc5c8184b602718d3dbf1a0cec228e1e`.

Current C2 boundary: `raw_record_set_admitted=true`, `decoded=true`, `mapped_reference_coordinate=true`, `tangent_response_ready=false`, `prediction_ready=false`, `scientific_model_authority_created=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`.

## Current frontier — Exp073HX tangent-runtime plan static audit v0.1

HX is prospectively frozen before any nonzero tangent runtime. Exact plan: 9 nonzero model points × 7 z × 4 admitted k = 252 requests, model-major then z-major/k-minor. Reference `(0,0)` is not recomputed.

- prereg `docs/dsir4/prereg/EXP073HX_C2_TANGENT_RUNTIME_PLAN_STATIC_AUDIT_V0_1.md`, commit `63940da8955cddeba4e8f0f6cb3ac766baac6088`, blob `e00d972504abb2ec102f9fc09f0e57af1bccf33e`;
- workflow `.github/workflows/exp073hx-c2-tangent-runtime-plan-static-audit-v0-1.yml`, implementation commit `24ee69be8574e4a5976e1bd4371e8bc69bbf4957`, blob `55b4d60d454c8f4c42f3646cfedb4cebf57deeaa`;
- binding/head commit `dd25da6aa9363c3a279e894595106b472b2375ad`;
- run `34243153985`, job `102118219475`;
- runner owner GitHub-hosted `ubuntu-24.04`; self-hosted/home heavy owner none;
- state at pointer update: `IN_PROGRESS`.

Expected token `PASS_EXP073HX_C2_TANGENT_RUNTIME_PLAN_STATIC_AUDIT_V0_1`. HX ceiling is support `+0/+0`; tangent runtime/science do not start in HX.

## Exact next transition

On HX terminal, inspect raw log. Only exact PASS permits a separately prospectively frozen tangent raw-runtime producer over the exact 252-request plan, reusing the validated HT exact-endpoint/serializer lineage and preserving complete per-model-point durable units. No reference recomputation or tolerance/rounding/effective-coordinate rescue is permitted.

Global frozen DSIR boundaries remain unchanged: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.
