# DSIR G7 checkpoint — Exp073R1 six-hour infrastructure boundary and deterministic sharding

Date: 2026-08-28

## Observed result

Exp073R1 run `33108733415` ended `completed/cancelled` at approximately the GitHub-hosted six-hour job boundary. The scientific assertion step never ran. Therefore this run is classified **INFRASTRUCTURE INCOMPLETE**, not scientific FAIL.

The last fully reported progress checkpoint was `29,360,128 / 136,930,995` rows with selected counts `[796529, 853083, 880179, 437409]`. The cancellation artifact `9670978026` (`sha256:aa460204934de07877b9c2b13b64b439535dbb4d03cc53e1981baef0864503f1`) contains four pixel-index records whose byte sizes are exactly four times those counts. This partial artifact is retained as provenance only and is **not** promoted to a scientific or R1 PASS result.

## Infrastructure-only repair

The monolithic transport implementation is replaced by an eight-shard deterministic execution layer. Shards partition the frozen row interval `[0,136930995)` into exact, disjoint, contiguous integer ranges. Every shard preserves the same source/metacal row decoding, selection

`zbin_mcal == t AND dec >= -90 AND dec <= -35 AND flags_select == 0`

and the same HEALPix mapper (`nside=4096`, RING, celestial lon/lat). Each shard records range SHA256 values and exact selected-row pixel-index streams, but evaluates no support fraction, covariance, nuisance tangent, quotient/null relation, or G8 input.

The merge stage requires all eight shards, verifies exact contiguous full-row coverage and every record SHA256/length, concatenates records strictly in global row order, reconstructs each mask, then reconstructs it a second time from the merged record and requires identical selected counts, unique-pixel counts and mask SHA256. Exact release-object identity remains bound to the previously completed full-stream checksum result `PASS_REMAINING_DESY1_RELEASE_CHECKSUM_BINDING_EXP073P2`, including the frozen source and metacal SHA256 digests. The genuine Exp073R0 PASS run `33103083736` is also rebound before merge.

This changes only execution topology needed to fit the hosted-run time boundary. It does **not** change a frozen scientific acceptance criterion or Exp073P semantics.

## Gate ordering

`validated physical forward/power-input bridges -> Exp073R1 reproduction prerequisite -> Exp073P physical support-validity classification -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> fresh G8 withheld family`.

Until the sharded merge emits `PASS_DESY1_FULL_ONEPASS_WEAK_LENSING_MASK_EXP073R1`, Exp073P and every downstream stage remain blocked.
