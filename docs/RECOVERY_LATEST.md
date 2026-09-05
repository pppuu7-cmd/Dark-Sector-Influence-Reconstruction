# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-05
**Scope:** DSIR only; RTK/RQIR excluded.

Repository state, immutable recovery notes, validated Actions raw logs/artifacts and durable checkpoints outrank chat wording. Historical outcomes remain immutable. Frozen science boundaries remain unchanged.

## Preserved scientific authority
Wm_S1 Track-A exact PASS, admitted Wm_S2 and Wm_S3 exact scientific PASS remain preserved. Historical Exp073CM resource/performance FAIL `+0/+0`, Exp073BU runner-loss infrastructure `+0/+0`, and Exp073DT attempts 1–3 external runner shutdowns remain unchanged. Current scientific target is `WW_S0_S0`.

Frozen frontier: `Wm_S1 -> Wm_S2 -> Wm_S3 -> WW_S0_S0 -> WW_S0_S1 -> WW_S0_S2 -> WW_S0_S3 -> WW_S1_S1 -> WW_S1_S2 -> WW_S1_S3 -> WW_S2_S2 -> WW_S2_S3 -> WW_S3_S3`.

## Current authoritative heavy process — Exp073DT attempt 4
Run `33940588308`, attempt 4; hosted preflight `101288015425` SUCCESS; self-hosted science `101288014666` **QUEUED**. Frozen head `c450aef42d96eb0bfe0b4c78d5a0fdc850d9a2cd`; source authority `de83e20a68f79ccf25b89b0d33eb4206e294c757`; contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`; durable root `$HOME/.cache/dsir/exp073dt-ww-s0-s0-ab-v0-1`; A/B namespaces `checkpoints/exp073dq-ww-s0-s0-a-v0-1`, `checkpoints/exp073dq-ww-s0-s0-b-v0-1`; expected token `PASS_EXP073DT_WW_S0_S0_EXACT_REPEATABILITY_8CORE_V0_1`. **DSIR-HOME-PC RESERVED BY Exp073DT attempt 4.** No competing self-hosted heavy process may launch.

Exp073EB remains mandatory support-only provenance closure: DT workflow SUCCESS alone cannot create WW_S0_S0 authority; raw A/B exact validation and full six-stage checkpoint-provenance PASS are also required.

## Distinct-field exact-adapter investigation
Exp073DU/DW remain qualifier FAIL `+0/+0`; Exp073DX excluded FITS orientation; Exp073ED excluded low-level/public BPW tensor layout; Exp073EE established formula mismatch; Exp073EF localized mismatch before solve.

Exp073EG `BIN_ONLY_MISMATCH +0/+0` established manual P/bin non-exactness while Q/unbin was exact. Exp073EH `OFFICIAL_BIN_SUBSTITUTION_STILL_MISMATCH +0/+0` established that official P/Q plus NumPy inversion still do not reproduce public BPW bitwise. Exp073EI `SOLVER_OPERATOR_MISMATCH +0/+0` established NumPy inverse is not bitwise equal to the official public decoupling operator; run/job `33988714617 / 101366943002`, artifact `9975963572`, verified ZIP SHA `52a77c087744e941bc27efb271cdf3047099aa1f5e7092f5296dda9733459def`.

### Exp073EJ — terminal `PUBLIC_DECOUPLE_BPW_MISMATCH +0/+0`
Run/job `33988827671 / 101367245475`; artifact `9975998092`; GitHub and independently downloaded ZIP SHA256 `2c5b1ff36a50680aaa9c6aa46e05fc4803ea09abd1e213fa6e41f55d97548e17`. Frozen token `COMPLETE_EXP073EJ_PUBLIC_DECOUPLE_BPW_MISMATCH_V0_1`. Official `decouple_cell` composed columnwise over the serialized->reloaded MCM is not bitwise equal to public `get_bandpower_windows()`: SHA `ba4e386e7c06d89a1942e9ded5c38827278c97278ed470d22f4f428d3ecd95df` versus `70df69ed48c7fb4b8706cc69dbc08a56272c791892394b357e14111f813681b7`. Diagnostic-only max difference `8.326672684688674e-17` cannot rescue exactness. Therefore neither algebraic reconstruction nor alternate public-operation composition is admissible for exact BPW authority under current evidence.

## Active support/readiness gate — Exp073EK
Exp073EK was prospectively frozen after EJ terminal consumption. It treats direct public PyMaster 2.7 `get_bandpower_windows()` as the sole candidate exact adapter operation: serialize one distinct S0->S1 workspace, independently reload twice, call only public BPW, extract exact `EE<-EE` `[0,:,0,:]`, and require full and selected SHA256 plus `numpy.array_equal` identity.

Prereg commit/blob `2072f683ba0a0d26a70762e5424c8cff564c1b2d / 8ace7b91e0607552cab2e2a9e6cf20c2c5e24621`; implementation commit/blob `c4c587ccd62341b9eb89dac168c2abf6ae6f15a8 / b3fcdf5acfe0d5818657bd1f2885c91c2903a877`; workflow commit `fc9cd10556870119cbdea2d790218f6d23cce0f1`; activation head `51f8a7d7dd481e79b734ba174bffa29236f2fc0b`; run `33988956806` **QUEUED** at latest observation. Frozen outcomes `DIRECT_PUBLIC_BPW_ADAPTER_EXACT` or `DIRECT_PUBLIC_BPW_ADAPTER_FAIL`, both support-only `+0/+0` and no WW authority.

On EK PASS, direct reload + public BPW becomes the only qualified exact cross-workspace adapter candidate and must still pass a separate prospectively frozen full-resolution resource/readiness gate before Exp073DV activation. On EK FAIL, the cross-workspace exact adapter remains blocked.

Exp073DV remains `PREPARED_NOT_ACTIVATED`, additionally blocked on valid WW_S0_S0 authority/provenance closure.

## Frozen science/execution boundaries
`0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

## Exact next gates
1. Do not launch another self-hosted task while Exp073DT attempt 4 is queued/in_progress.
2. Consume Exp073EK immediately when terminal. On PASS, prospectively freeze a full-resolution resource/readiness gate for direct public BPW without changing science; on FAIL, retain cross-workspace block.
3. When Exp073DT `33940588308 / 101288014666` becomes terminal, consume raw artifact/digest, exact A/B evidence and Exp073EB provenance before any WW_S0_S0 authority.
4. Keep Exp073DV inactive until both WW_S0_S0 and exact-adapter prerequisites pass.
