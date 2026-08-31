# DSIR recovery checkpoint — streaming successor design while Exp073BJ computes

**Date:** 2026-08-31  
**Classification:** nonclassifying execution-design research, `+0/+0`.  
**Scope:** DSIR only.

## Current classifying control plane

Exp073BJ run `33379013167` remains the only active heavy Track-A Wm_S1 control plane. Compact A/B jobs `99446854065` and `99446854363` remain inside the full-scale two-thread compact computation after prospective freeze and exact BI/AZ binding PASS. Do not duplicate or modify BJ.

## New local result

The existing low-memory implementation still materializes a full dense `G = get_general_coupling_matrix(...)` before deterministic compression.

At frozen `L=12288`:

- `G` has `150,994,944` float64 entries = `1.125 GiB` payload;
- compact `A` has `479,232` float64 entries = `3.65625 MiB`;
- dense-to-compact payload ratio is about `315.08x`.

The public Python interface returns the complete dense `[nl,nl]` matrix, so Python-side slicing cannot make the current call genuinely streaming. A future blockwise successor requires a C-level row/block generator or a separately validated equivalent implementation.

## Exact streaming accumulation QA

New nonclassifying QA:

`ci/article3_streaming_compression_equivalence_qa_v0_1.py`

commit `12a9c86331df0cd7954f440c94f518d0c157ff42`.

Synthetic deterministic reference versus streaming blocks of sizes `1,3,17,64,127,256,1024` rows: all compact outputs are bit-for-bit identical and SHA-identical.

Exact float64 accumulator save/reload at intervals `1,2,7,31,100,257` rows: all outputs remain bit-for-bit identical.

This proves that block boundaries and exact checkpoint/reload do not alter the frozen fixed-order accumulation **provided the future row generator supplies exactly the same rows in the same ascending-ell order**. It does not prove C-level row-generation equivalence.

## Candidate future architecture

A separately preregistered successor, only after BJ terminal classification if needed, may compute one general-coupling row/block at a time, update the current frozen-band accumulator in strict ell order, checkpoint exact accumulator state and completed band hashes, and finally emit canonical `<f8 [39,12288]` A. Two complete independent replicas and exact comparator equality remain mandatory.

Never merge separately summed partial blocks because regrouping floating-point additions could change bits. Resume must restore the exact accumulator and continue at the next ell.

Full design:

`docs/ARTICLE3_STREAMING_GENERAL_COUPLING_SUCCESSOR_DESIGN_2026-08-31.md`

commit `c5527de60d60ec5de3d63ea5d06da497b4255835`.

## Significance

Even if BJ passes Wm_S1, the remaining Wm/WW tasks still need separate authority. A prospectively validated checkpointable generator could remove the six-hour hosted-run fragility for later windows without changing scientific definitions.

No readiness change: `Verified 52.0% | Draft/data 53.7%`. Exp073AQ remains permanent FAIL. Layer A/B, covariance/whitening, G7/G8/G9 remain unauthorized. No G8 jump.
