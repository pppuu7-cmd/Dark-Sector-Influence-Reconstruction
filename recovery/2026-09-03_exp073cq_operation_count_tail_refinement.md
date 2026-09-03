# Exp073CQ operation-count tail refinement

Date: 2026-09-03
Status: NON-AUTHORITATIVE PREFLIGHT REFINEMENT ONLY
Scientific credit: +0/+0
Resource authority: none

This note refines only the rough timing estimates in `recovery/2026-09-03_exp073cq_tail_imbalance_ll3_shard_contingency_analysis.md`. It does NOT modify, cancel, reinterpret, rescue, or supersede frozen Exp073CQ v0.1 or its run `33742582807`. The actual CQ terminal telemetry/final token remains the sole authority.

## Deterministic operation-count proxy

The frozen helper `ci/exp073ca_stream_general_coupling_range_v0_1.c` performs, for every `(ll2,ll3)` pair, two `drc3jj` calls for signature `(0,2,0,2)` plus the explicit ascending `l1` accumulation. For the valid frozen signature, the Wigner recurrence length for each call is determined by the same `(ll2,ll3)` geometry. A deterministic proxy was therefore computed directly from the frozen band edges as

`proxy_band = sum_{ll2 in band} sum_{ll3=2}^{12287} [2*nfin_drc3jj(ll2,ll3) + n_l1_accum(ll2,ll3)]`,

where `n_l1_accum` includes the `lmax=12287` clipping used by the helper. This proxy models loop-work geometry rather than fitting a free high-band power law.

## Calibration on real completed bands

For Exp073CP bands 24..28, the observed CPU seconds divided by this deterministic proxy are tightly clustered:

- minimum coefficient: `1.4852514425663915e-08 s/proxy-unit`;
- maximum coefficient: `1.5317522257399004e-08 s/proxy-unit`;
- through-origin least-squares coefficient: `1.5040969205507953e-08 s/proxy-unit`.

The coefficient spread is only about +/-1.5% around the fitted value (about 3.1% full range), substantially tighter than the earlier simple width*midpoint extrapolation.

Using this calibrated operation proxy gives the following non-authoritative predicted CPU seconds for missing bands 29..38:

- 29: `1575.8 s`
- 30: `1968.2 s`
- 31: `2457.4 s`
- 32: `3040.5 s`
- 33: `3739.0 s`
- 34: `4551.6 s`
- 35: `5479.2 s`
- 36: `6485.7 s`
- 37: `7527.1 s`
- 38: `8472.8 s`.

These are forecasts, not measurements and not frozen results.

## Refined scheduling implication

Under the actual frozen Exp073CQ ascending dynamic scheduler, bands 29..36 occupy the first eight slots; band 37 starts at the first vacancy and band 38 at the second. Using the calibrated operation proxy:

- predicted numerical span: `10441.0 s` = about `2.90 h`;
- predicted total worker CPU: `45297.4 s`;
- predicted `cpu_fraction_of_8_compute`: about `0.5423`.

Thus the earlier rough `~5.2 h` timeout estimate is superseded by this more structure-aware preflight: a six-hour timeout is presently not the leading expected blocker. The leading expected blocker remains severe tail imbalance from ten unequal indivisible bands.

Even an idealized cost-aware LPT ordering of these same ten indivisible predicted band costs has utilization only about `0.6683`. The trivial largest-task lower bound on makespan gives the same proxy ceiling here. Therefore, under this calibrated operation model, merely reordering whole bands cannot plausibly reach the frozen `>=0.90` gate.

This is still a preflight prediction. If actual Exp073CQ telemetry contradicts it, the frozen CQ telemetry wins.

## Consequence for a future successor only

If, and only if, Exp073CQ later reaches exact completion but returns CPU/resource FAIL, the preferred prospective successor remains exact-safe `ll3` sharding rather than whole-band reordering:

- disjoint `(band,ll3_lo,ll3_hi)` complete deterministic chunks;
- preserve the exact ascending `ll2` and `l1` arithmetic for each output `ll3`;
- no arithmetic reduction between shards; band assembly by placement/concatenation only;
- many more than 8 ready work units during heavy computation;
- complete-shard SHA/provenance checkpoints under a new namespace;
- hosted bitwise-equivalence regression against frozen complete-band outputs before any self-hosted launch.

No Wm_S3 scientific authority and no resource PASS is created by this note.
