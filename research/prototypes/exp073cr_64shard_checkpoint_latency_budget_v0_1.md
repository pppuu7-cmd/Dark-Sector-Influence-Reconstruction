# Exp073CR 64-shard checkpoint-latency budget v0.1

Status: NON-AUTHORITATIVE PREFLIGHT ONLY  
Scientific/resource credit: `+0/+0`  
This note does not modify or predict the frozen classification of Exp073CQ v0.2.

## Calibration

Use the deterministic frozen-kernel operation proxy from `exp073cr_64shard_balanced_candidate_v0_1.json` and calibrate seconds/proxy against immutable Exp073CP complete-band worker CPU telemetry for bands 24..28:

- band 24: 478.4293764 CPU s;
- band 25: 628.5257759 CPU s;
- band 26: 795.7985750 CPU s;
- band 27: 992.7503937 CPU s;
- band 28: 1236.1418038 CPU s.

The corresponding proxy-to-CPU calibration varies by about 1.4% RMS around the mean in this high-band range. Applying the mean calibration to the proposed 64 complete ll3 shards gives predicted numerical shard durations approximately:

- mean: 590.70 s;
- minimum: 515.15 s;
- maximum: 640.05 s.

These are planning estimates, not frozen measurements.

## Fail-closed synchronous durability model

Assume exactly 8 outer workers and candidate-order list scheduling. After each complete shard, its worker slot is not refilled until that shard's canonical payload/receipt has been durably pushed and exact-postchecked. Other already-running workers may continue.

Using the calibrated per-shard durations, predicted numerical utilization as a function of a constant per-shard synchronous durability latency is:

| durability latency per shard | predicted numerical utilization |
|---:|---:|
| 0 s | 0.97775 |
| 5 s | 0.97069 |
| 10 s | 0.96376 |
| 20 s | 0.95012 |
| 30 s | 0.92366 |
| ~38.99 s | ~0.90000 |
| 60 s | 0.84903 |
| 120 s | 0.60494 |

Thus the proposed 64-shard granularity has a modeled average synchronous checkpoint-latency budget of about **39 seconds per completed shard** before the frozen-style 90% CPU target becomes structurally endangered.

This supports keeping remote durability before refill rather than weakening checkpoint safety. It also implies that persistent 60-120 second transport stalls on most shards would require a different prospectively frozen transport architecture or coarser shards; such stalls must never be hidden by changing the CPU interval post hoc.

## Governance

Before any self-hosted Exp073CR successor:

1. hosted bitwise regression against immutable Exp073CP complete-band payloads must PASS;
2. exact shard boundaries and scheduling order must be prospectively frozen;
3. durability latency must be separately telemetered;
4. no completed shard may be treated as durable before exact remote postcheck;
5. no tolerance/ULP/rounding rescue is permitted;
6. actual CPU/resource classification must use the prospectively frozen metric and observed telemetry, never this estimate.
