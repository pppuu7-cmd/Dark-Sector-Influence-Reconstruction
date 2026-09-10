# DSIR current-process ledger

Updated: 2026-09-10. Scope: **DSIR only**; RTK/RQIR excluded.

## Preserved scientific authority
Exp073IR remains `NUMERICALLY_UNRESOLVED_EXP073IR`, native-grid max `0.9998247463807295`, retained 107; covariance restriction unauthorized; Wm_S3 unopened. Exp073JI remains support-only feasible; Exp073JJ/JK remain support-only NOT_CONVERGED at `0.037280144773915974` / `0.016330535730270664`. Frozen `REL_TOL=1e-3`, `h=1e-4`, science domain/masks/traversal and anti-rescue rules unchanged. Exp073JP separately retains support-only `PREDICTION_ARTIFACT_ADMITTED_PLUS_0_PLUS_0`.

JO v0.2 exact PASS receipts remain preserved: history_slot10 artifact `10164136352`, ZIP SHA256 `0a06f375ba59f4da33172d3d9f742af7b29c82263c600c2e7696fd6676af41cc`; cache_roundtrip_slot10 artifact `10164156389`, ZIP SHA256 `5facd22fbf6edca62b0ff37e7457d411d232525aeead20738de8cb68c9bca735`.

## Consumed infrastructure failures
JO v0.3 run `34512184648`, head `f82bb38b5ed4f9de45be9b8ce2bdae10d9040d52`: third fresh-tail job `103026063803` passed all frozen guards/build, then received hosted-runner shutdown in exact numerical phase; no artifact -> `INVALID_INFRA_PLUS_0_PLUS_0`. Same monolithic 4097-node hosted architecture is retired.

JO v0.4 first run `34529306755`, head `fcc76f00e9a6f3b95f65ac5bd3b36aba9d18c8d6`: static-equivalence failed before shards because numpy was missing -> infrastructure/software `+0/+0`. Minimal dependency-only repair commit `29be760cf0a78c99b19fd887fc8a4a7dda5a2c31`.

## Current authoritative process
Exp073JO v0.4 per-model sharded recovery. Prereg commit `e509c0d8d9557dd0f945ae575c2229fa4ab7e3a3`; helper commit/blob `0b27e9496e49882053ce86a8430fed9b3bcacc3a / 9afb076a0744dd30d4e45d4090d16ef23cc501fa`; workflow run `34529375485`, branch/head `main / 29be760cf0a78c99b19fd887fc8a4a7dda5a2c31`, GitHub-hosted `ubuntu-24.04`, home/self-hosted ownership none.

Static-equivalence job `103046059313` is exact SUCCESS, including `PASS_EXP073JO_V04_STATIC_RECONSTRUCTION_EQUIVALENCE`. GitHub dependency chaining has launched all eight production durable shards; all are currently IN_PROGRESS after frozen identity + dependency installation, in exact pinned capacity-patched CLASS-IV build or later:
- after_history/reference `103046120028`;
- fresh_tail/reference `103046120038`;
- after_history/beta_minus `103046120044`;
- after_history/alpha_minus `103046120090`;
- fresh_tail/beta_plus `103046120104`;
- after_history/beta_plus `103046120108`;
- fresh_tail/alpha_minus `103046120154`;
- fresh_tail/beta_minus `103046120215`.

Each complete model shard artifact is the durable unit. No shard may be inferred from workflow success alone; terminal shards require raw-log + artifact/hash/provenance verification. Failed shards may be rerun individually after causal diagnosis without recomputing verified siblings.

## Exact next transition
When shards terminate, consume every successful receipt independently. If all 8 are valid, let the encoded aggregate reconstruct exact frozen `(4,2)` responses and enforce `np.array_equal` plus finite/positive mask identity; then independently verify aggregate hashes. Valid aggregate PASS remains support-only `+0/+0` and may unlock exactly one checkpointed JL recovery. Valid exact aggregate FAIL is a negative JO result. Infrastructure failure triggers only smallest shard-level repair/recovery. JL checkpoint namespace `checkpoints/exp073jo-jl-response-v0-1` remains blocked pending JO aggregate PASS. Valid recovered JL CONVERGED -> only JN; NOT_CONVERGED -> only JM; infrastructure invalid -> neither.
