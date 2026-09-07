# DSIR authoritative recovery — latest

Updated: 2026-09-07. Scope: **DSIR only**. Never mix RTK or RQIR.

Newest immutable authority note: `docs/recovery/RECOVERY_2026-09-07_EXP073FW_COMPARATOR_NAMESPACE_REPAIR_AND_CHECKPOINT_ONLY_RESUME_V16.md` (creation commit `e71e5990ca976922e3c759c5645c24d566a044a3`). Earlier recovery notes remain immutable history.

## Preserved authority

Wm_S1 Track-A exact PASS and admitted Wm_S2/Wm_S3 remain preserved. WW admitted authorities include `S0_S0`, `S0_S1`, `S0_S2`, `S0_S3`, `S1_S1`, `S1_S2`, `S1_S3`. `WW_S2_S2` is **NOT ADMITTED**.

## Exp073FW terminal result and preserved checkpoints

Exp073FW run `34135965569`, head `f7e925e782983824b7e916ce8437fcf924ec5760`, is terminal `INFRASTRUCTURE/IMPLEMENTATION_FAILURE +0/+0`, not scientific FAIL. Hosted audit `101786894169` succeeded; home job `101786993129` completed both replica chains then failed in terminal comparator; provenance admission `101817055237` was skipped.

First causal error: `fail-closed receipt identity mismatch A:checkpoint_namespace`. The comparator wrapper omitted hyphenated transform `ww-s1-s1 -> ww-s2-s2` although the actual receipts correctly use `checkpoints/exp073fw-ww-s2-s2-{a,b}-v0-1`.

Artifact `10027545256` was independently downloaded; GitHub digest and recomputed ZIP SHA256 both equal `0be01af5b522821fcdcd52be9fb2ef4ae5849efd2c4e439b9d7ad8462765cfb4`. Both A and B complete durable chains are present. Both canonical `<f8 [39,12288] EE<-EE` arrays are 3,833,856 bytes and SHA256 `3daa7894648cc44d3ee822fe5f9b02aa0ccb756b11abfa0852a08b57d4ba75c9`; independent exact array comparison is true, both finite, max absolute difference `0.0`. Receipts preserve same-field `S2->S2`, ordered `[2,2]`, source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, and exact `19,327,352,832`-byte file-backed MCM proof.

These facts are preserved evidence, but `WW_S2_S2` authority is not created until the frozen comparator and Exp073FX provenance admission complete successfully.

## Prospective repair

Minimal comparator repair commit `ced70da68cd148cfba4c7dec33b8140989557bee`; repaired blob `b5b828bd71eaf6da360c8ebfa279888165531e49`. It adds only missing hyphenated checkpoint-namespace transformation plus fail-closed namespace invariants. Frozen arithmetic, source semantics, science domain, threshold/tolerance policy and acceptance criteria are unchanged.

Workflow binding/static regression commit `3835072cf580fc0a0950794385c028012f60a5cb` freezes that blob and audits both A/B S2S2 namespace literals. Raw hosted audit token is `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_6`, support `+0/+0`.

## Authoritative current heavy process

Exp073FW recovery run **`34145888831`**, head **`3835072cf580fc0a0950794385c028012f60a5cb`**.

- hosted audit job **`101817723744`**: SUCCESS, raw `PASS_EXP073FW_HOSTED_LAUNCH_AUDIT_V0_6`;
- home-science job **`101817765818`**: IN_PROGRESS at latest reconciliation;
- owner: `DSIR-HOME-PC-2` / `win-ws338`;
- durable root: `~/.cache/dsir/exp073fw-ww-s2-s2-filebacked-ab-v0-1`;
- both A and B are already complete and verified; expensive replica computation must not be repeated unless fail-closed restore verification rejects a checkpoint.

Exact next action: terminal-consume `34145888831`; validate comparator output, restore provenance, uploaded artifact digest and then Exp073FX admission. Only frozen Exp073FX may create `WW_S2_S2` authority. A genuine exact A/B mismatch would be scientific FAIL; implementation/infrastructure failure remains repair/resume `+0/+0`.

The FW workflow still has a temporary path-scoped push trigger used for recovery launch. Do not edit it while `34145888831` is active; restore dispatch-only semantics at a safe terminal transition.

## Independent C2 support frontier

C2 remains `mapping_ready=true`, `prediction_ready=false`, `G_DOMAIN_MAPPING=NOT_YET_TESTABLE`, scientific `+0/+0`. Exact z `[0.295,0.51,0.706,0.934,1.317,1.491,2.33]`, k `[0.00067,0.00201,0.0067,0.0201] Mpc^-1`; no interpolation/smoothing/averaging/tolerance/effective-coordinate/fiducial-P rescue.

Exp073GW/GX remain raw-validated support. Exp073GY was prospectively preregistered at `200382a02ff3db9285f3bfe6de0d29d3cb86b422` before workflow `8671ab882d0ef32723668c7683685410bcad244a`; run `34141294357 / 101803642167` raw-validated `PASS_EXP073GY_C2_IDE_RUNTIME_PACKET_SET_ADMISSION_BOUNDARY_V0_1`, classification `SUPPORT_PLUS_0_PLUS_0`, with no scientific record set/model authority created.

The next meaningful C2 step is real runtime generation/admission of the complete 28-packet set under frozen GW/GX/GY provenance. It remains BLOCKED while the current FW job owns home. Do not replace this prerequisite with additional metadata-only scaffolding.

## Global frozen boundaries

Unless prospectively superseded by explicit repository authority: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; exact-threshold ambiguity `numerically_unresolved`; no tolerance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P shortcut.