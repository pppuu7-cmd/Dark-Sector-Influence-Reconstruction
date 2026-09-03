# Exp073CQ contingency — 128-shard exact-safe ll3 candidate preflight

Date: 2026-09-03
Status: NON-AUTHORITATIVE CANDIDATE ONLY; NOT PREREGISTERED; NOT AUTHORIZED
Scientific/resource credit: +0/+0

This file does not alter frozen Exp073CQ v0.1 or run `33742582807`. It is a candidate architecture only for a NEW successor if the actual CQ outcome later requires one. CQ terminal telemetry/final token outranks every estimate here.

## Cost model

Use the frozen helper loop geometry for signature `(0,2,0,2)` and `lmax=12287`.
For each `(ll2,ll3)` pair define a deterministic work proxy

`2*nfin_drc3jj(ll2,ll3) + n_l1_accum(ll2,ll3)`

corresponding to the two Wigner calls plus the explicit ascending `l1` loop. Sum this exactly over a candidate `(band,ll3_lo,ll3_hi)` shard while preserving the frozen band `ll2` interval.

Calibration on real Exp073CP bands 24..28 gives a stable CPU/proxy coefficient; this proxy is used only to equalize work, never as a scientific observable or a replacement for measured CPU telemetry.

## Candidate shard counts

Target total: 128 complete deterministic shards over numerical bands 29..38.
Allocate shard counts proportional to exact operation proxy using largest-remainder integer allocation:

- band 29: 4 shards
- band 30: 6 shards
- band 31: 7 shards
- band 32: 9 shards
- band 33: 11 shards
- band 34: 13 shards
- band 35: 15 shards
- band 36: 18 shards
- band 37: 21 shards
- band 38: 24 shards

Total = 128.

## Candidate ll3 boundaries

Every interval is half-open `[ll3_lo,ll3_hi)` and covers only `ll3>=2`; output indices 0 and 1 remain the same exact zeros as in the frozen complete-band helper.

- band 29: `[2, 4378, 6912, 9464, 12288]`
- band 30: `[2, 3704, 5375, 7016, 8664, 10404, 12288]`
- band 31: `[2, 3592, 5095, 6455, 7816, 9224, 10710, 12288]`
- band 32: `[2, 3309, 4679, 5745, 6761, 7789, 8852, 9952, 11096, 12288]`
- band 33: `[2, 3114, 4404, 5394, 6233, 7036, 7857, 8697, 9559, 10443, 11352, 12288]`
- band 34: `[2, 2967, 4195, 5138, 5939, 6655, 7326, 7996, 8678, 9372, 10080, 10801, 11537, 12288]`
- band 35: `[2, 2843, 4020, 4930, 5712, 6410, 7047, 7637, 8200, 8760, 9328, 9903, 10487, 11078, 11679, 12288]`
- band 36: `[2, 2651, 3755, 4623, 5367, 6030, 6632, 7188, 7708, 8197, 8660, 9108, 9551, 9996, 10445, 10899, 11358, 11821, 12288]`
- band 37: `[2, 2489, 3560, 4398, 5111, 5741, 6313, 6840, 7332, 7794, 8231, 8647, 9045, 9427, 9795, 10153, 10506, 10858, 11212, 11568, 11927, 12288]`
- band 38: `[2, 2416, 3454, 4254, 4930, 5525, 6064, 6559, 7021, 7454, 7864, 8254, 8627, 8984, 9328, 9660, 9981, 10292, 10594, 10888, 11175, 11457, 11735, 12012, 12288]`

These boundaries are generated from equal cumulative operation-proxy quantiles independently within each band. They are not frozen and may be changed before any future preregistration if an exact hosted regression reveals a better deterministic partition.

## Balance result

Across all 128 candidate shards:

- smallest shard proxy / mean proxy ~= `0.9268`;
- largest shard proxy / mean proxy ~= `1.1136`;
- largest / smallest shard proxy ~= `1.2016`.

Greedy dynamic scheduling of these 128 shards across eight workers gives operation-proxy utilization approximately:

- natural band/shard order: `0.9918`;
- descending-cost LPT order: `0.9984`.

These are scheduler geometry estimates, not measured CPU resource PASSes. They show that the candidate has ample theoretical headroom above the frozen 0.90 target, unlike the ten indivisible whole-band CQ tasks.

## Exactness requirements for any future implementation

A future successor may use these or revised boundaries only if prospectively frozen after CQ outcome consumption and after hosted exact-regression PASS. It must:

1. split by disjoint output `ll3` ranges only, never by the `ll2` summation dimension;
2. for each fixed `ll3`, preserve the identical ascending `ll2`, identical `drc3jj` calls, identical ascending `l1`, identical `acc += xi`, and identical final division by the full frozen band width;
3. produce canonical `<f8` shard payloads with SHA256, exact `(band,ll3_lo,ll3_hi)`, source/PCL/helper/compiler lineage and contract fingerprint;
4. checkpoint only complete shards under a NEW namespace;
5. reassemble complete bands by placement/concatenation only, with no floating-point reduction across shards;
6. bitwise-compare assembled known bands against frozen complete-band outputs under the same NaMaster 2.7 and compiler-FP restrictions before home dispatch;
7. still measure actual eight-core compute-active CPU fraction and swap in the eventual frozen resource gate.

No authority is created by this candidate preflight.
