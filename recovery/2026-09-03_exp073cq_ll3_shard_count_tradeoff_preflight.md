# Exp073CQ contingency — ll3 shard-count tradeoff preflight

Date: 2026-09-03
Status: NON-AUTHORITATIVE PREFLIGHT ONLY; +0/+0

This analysis does not modify frozen Exp073CQ v0.1. It refines prospective scheduling choices only for a NEW post-CQ successor if the actual CQ outcome later requires one.

Using the deterministic frozen-kernel operation proxy described in `recovery/2026-09-03_exp073cq_operation_count_tail_refinement.md`, candidate complete `ll3` shards were allocated proportionally to per-band work and each band's boundaries were chosen by equal cumulative proxy quantiles.

## Predicted scheduling tradeoff

For eight outer workers, natural deterministic band/shard submission order gives:

| Total shards | Per-band allocation 29..38 | Proxy utilization | Mean predicted numerical CPU / shard | Predicted numerical span |
|---:|---|---:|---:|---:|
| 32 | `1,1,2,2,3,3,4,5,5,6` | 0.9053 | 1415.5 s | 1.74 h |
| 40 | `1,2,2,3,3,4,5,6,7,7` | 0.9378 | 1132.4 s | 1.68 h |
| 48 | `2,2,2,3,4,5,6,7,8,9` | 0.9636 | 943.7 s | 1.63 h |
| **64** | **`2,3,4,4,5,6,8,9,11,12`** | **0.9767** | **707.8 s** | **1.61 h** |
| 80 | `3,4,4,5,7,8,10,11,13,15` | 0.9824 | 566.2 s | 1.60 h |
| 96 | `3,4,5,6,8,10,12,14,16,18` | 0.9961 | 471.8 s | 1.58 h |
| 128 | `4,6,7,9,11,13,15,18,21,24` | 0.9918 | 353.9 s | 1.59 h |

All numbers are preflight model predictions, not measured resource results.

A descending-cost LPT queue improves the modeled figures further, but a future authoritative gate should prefer a simple deterministic scheduler unless LPT ordering itself is prospectively frozen and audited.

## Preferred contingency baseline

**64 complete ll3 shards** is the current preferred research baseline, not a frozen choice. Rationale:

- modeled utilization ~97.7%, leaving substantial margin above a 90% target;
- only 64 durable shard pushes instead of 128;
- mean shard compute ~708 s, so Git transport/checkpoint latency should be small relative to numerical work under normal conditions;
- work units remain numerous enough to keep eight workers fed and suppress the high-band tail;
- each shard remains an independently complete deterministic checkpoint unit permitted by the universal checkpoint policy.

32 shards has too little margin (~90.5%). 40 already clears the target in the model but leaves limited robustness. 48 is plausible; 64 provides a better margin/transport compromise. 80/96/128 gain little predicted wall-time relative to their larger checkpoint count.

Any future preregistration must recompute/freeze exact 64-shard boundaries, run bitwise equivalence against the frozen complete-band helper, and measure real CPU/swap/transport behavior. This preflight itself grants no authority.
