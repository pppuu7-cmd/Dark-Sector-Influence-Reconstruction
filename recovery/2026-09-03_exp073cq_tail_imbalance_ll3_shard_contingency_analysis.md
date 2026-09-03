# Exp073CQ tail-imbalance and exact-safe ll3-shard contingency analysis

Date: 2026-09-03
Status: NON-AUTHORITATIVE PREFLIGHT / CONTINGENCY ANALYSIS ONLY
Scientific credit: +0/+0
Resource authority: none

## Scope and historical boundary

This note does not modify, reinterpret, cancel, rescue, or supersede frozen Exp073CQ v0.1. Exp073CQ run `33742582807` remains the only authorized continuation and is currently queued for the self-hosted runner. Its frozen criteria, implementation binding, PASS/FAIL tokens, and checkpoint semantics remain unchanged.

This note is only a prospective contingency analysis for a NEW successor if Exp073CQ later terminates with CPU/resource FAIL or infrastructure incompleteness. No conclusion here may be substituted for the actual frozen Exp073CQ final receipt.

## Parent evidence used

Exp073CP durable parent head `025629d9bb7b113bd0548ff6a32c6ee5812ae245` contains exact complete bands `0..28` under contract fingerprint `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`.

Frozen band edges inherited from the Exp073CN/CO/CP numerical lineage are:

`[0,30,60,90,120,150,180,210,240,272,309,351,398,452,513,582,661,750,852,967,1098,1247,1416,1608,1826,2073,2354,2673,3035,3446,3914,4444,5047,5731,6508,7390,8392,9529,10821,12288]`.

Thus the Exp073CQ compute-only allowlist `29..38` has intervals:

- 29: `[3446,3914)` width 468
- 30: `[3914,4444)` width 530
- 31: `[4444,5047)` width 603
- 32: `[5047,5731)` width 684
- 33: `[5731,6508)` width 777
- 34: `[6508,7390)` width 882
- 35: `[7390,8392)` width 1002
- 36: `[8392,9529)` width 1137
- 37: `[9529,10821)` width 1292
- 38: `[10821,12288)` width 1467.

Observed Exp073CP complete-band worker telemetry already shows rapidly increasing cost while each worker itself remains close to one fully occupied CPU:

- band 24 `[1826,2073)`: CPU 478.4293764 s, wall 480.452266769 s;
- band 26 `[2354,2673)`: CPU 795.798575 s, wall 800.003064664 s;
- band 27 `[2673,3035)`: CPU 992.7503937 s, wall 998.030043344 s;
- band 28 `[3035,3446)`: CPU 1236.1418038 s, wall 1242.54937292 s.

The local worker CPU/wall ratios are therefore approximately 0.996, indicating that the remaining utilization problem is predominantly work-granularity / tail imbalance rather than a worker failing to consume its assigned core.

## Why complete-band scheduling is likely structurally insufficient

The frozen C helper `ci/exp073ca_stream_general_coupling_range_v0_1.c` computes a band by nested loops over band `ll2`, all output `ll3`, Wigner evaluation, and an inner `l1` sum. For high bands the dominant operation count grows approximately with band width times a characteristic `ll2`, consistent with the observed acceleration of cost in bands 24..28.

A simple preflight extrapolation using the observed high-band CPU scaling and exact frozen widths predicts an increasing sequence for bands 29..38. Under the frozen Exp073CQ scheduler, bands 29..36 are submitted first and 37/38 can only enter after earlier complete bands free two worker slots. With eight workers and only ten indivisible work units, the final two very expensive bands necessarily create a long tail.

Using a rough high-band fit `CPU ~= c * width * midpoint` with `c` calibrated from completed bands 24/26/27/28 gives an ascending-scheduler preflight utilization of about 0.45. This is an extrapolation, not an Exp073CQ result. Even a cost-aware idealized LPT assignment of the same ten indivisible predicted band costs remains only about 0.51. Therefore merely reordering complete bands is not expected to make a frozen `cpu_fraction_of_8_compute >= 0.90` gate attainable.

The same extrapolation gives a compute-span order of `1.9e4 s`, close enough to the existing six-hour job timeout that timeout risk should also be treated as a resource-architecture concern, not evidence against the numerical kernel. This estimate is non-authoritative.

## Exact-safe finer-grained architecture

The correct prospective refinement is to split work by disjoint `ll3` output ranges, NOT by `ll2` summation ranges.

For one frozen band and one fixed `ll3`, the original arithmetic is:

1. initialize `acc[ll3] = 0`;
2. visit `ll2 = lo, lo+1, ..., hi-1` in that exact order;
3. for each `(ll2,ll3)`, evaluate the same `drc3jj` inputs and the same ascending `l1` loop;
4. perform the same `acc[ll3] += xi` recurrence;
5. divide by the same frozen band width.

Different `ll3` outputs write disjoint accumulator elements. Therefore a worker assigned a complete deterministic `ll3` slice can preserve the exact per-output `ll2` and `l1` order. Reassembling disjoint `ll3` slices is placement/concatenation only; there is no floating-point reduction across slices and therefore no new summation-order ambiguity.

By contrast, splitting one band's `ll2` interval and later summing partial band accumulators would alter floating-point grouping and is not exact-safe without a stronger proof; that route is rejected for the prospective successor.

## drc3jj independence audit

NaMaster source inspected at public commit `479864f7425cfb8d3a6e9ccedb0649ae833a928c`, `src/utils.c`. The normal `drc3jj` computation uses local scalar state plus the caller-provided output array `thrcof`. No mutable per-call accumulator shared between valid `drc3jj` invocations is used in the normal computational path. NaMaster has global error-policy state, but valid frozen inputs do not use it as numerical accumulation state.

This supports, but does not by itself constitute, the required bitwise equivalence proof. A NEW successor must still run a hosted exact-regression test comparing the proposed ll3-sharded helper against the frozen complete-band helper on already-known bands before any home dispatch.

## Prospective ll3 shard design

If a future successor is authorized after Exp073CQ outcome consumption:

- keep the same frozen PCL, edges, signature, dtype, compiler FP restrictions and NaMaster 2.7 environment;
- define complete deterministic shard units as `(band, ll3_lo, ll3_hi)`;
- preserve ascending `ll2` and ascending `l1` arithmetic for every fixed output `ll3`;
- use approximately 8-16 ll3 shards per heavy band initially (80-160 work units over bands 29..38), then freeze exact boundaries before execution;
- schedule shards dynamically across exactly eight outer processes with nested numerical threads = 1;
- store canonical shard payload + SHA256 + exact band/ll3 interval + contract fingerprint;
- durable-checkpoint only complete shard boundaries under a NEW `checkpoints/*` namespace;
- fail closed on any shard provenance/SHA mismatch or unknown transport state;
- assemble a band only after every frozen shard is exact-valid; assembly must be concatenation/placement only;
- compare each assembled band bitwise against a frozen complete-band reference for a hosted regression subset before self-hosted qualification;
- retain exact first-8 reference SHA, finite-output, swap=0 and compute-active CPU-fraction criteria prospectively;
- never mutate historical Exp073CQ or prior FAIL/incomplete records.

The universal self-hosted checkpoint policy explicitly permits complete deterministic `chunk` boundaries, so prospectively frozen ll3 chunks are governance-compatible if all required SHA/provenance/restore rules are implemented.

## Decision rule

Do nothing to frozen Exp073CQ while it is queued/running. Consume its actual terminal checkpoint, telemetry, diagnostic record and final token first.

- If Exp073CQ PASSes, this contingency is not needed for the current gate.
- If Exp073CQ reaches exact completion but CPU fraction is below 0.90, classify the historical CQ result permanently as resource/performance FAIL +0/+0, then preregister a NEW ll3-sharded resource successor.
- If Exp073CQ is infrastructure/software/checkpoint incomplete, preserve all durable newly completed bands and use the first captured diagnostic exception to decide whether the next successor is transport/control repair or ll3-sharded resource redesign.

No scientific Wm_S3 authority is created by this note.
