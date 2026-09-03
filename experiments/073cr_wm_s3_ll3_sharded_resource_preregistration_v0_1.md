# Exp073CR v0.1 preregistration — Wm_S3 ll3-sharded 8-core resource qualification

Date: 2026-09-03
Classification scope: resource/performance/control only, scientific credit `+0/+0`.

## Historical parent and reason for successor

Exp073CQ v0.2 is terminal **RESOURCE/PERFORMANCE FAIL +0/+0**, not scientific FAIL. Authoritative run `33752799918`, home job `100640079011`, artifact `9897551836`, terminal checkpoint `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`, contract fingerprint `87b58bf120510bec50b21851d7ff21269689db6dcdd906cb3a14102e4a4f5f97`. Exact control and swap safety passed, but CPU fraction was `0.6638297425690942 < 0.90`.

Exp073CR is a new prospectively versioned resource architecture. It does not mutate, rescue or rewrite Exp073CQ.

## Frozen numerical object

Task remains Wm_S3 compact general-coupling `A`, not the final bandpower window `W`.

Frozen science/arithmetic remains:
- source bin 3;
- signature `(0,2,0,2)`;
- `L=12288`, `lmax=12287`;
- Wm `TE <- TE`;
- same immutable PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`;
- canonical `<f8` rows;
- no tolerance, ULP, rounding, smoothing, averaging, pseudoinverse or arithmetic rescue.

The only permitted numerical restructuring is to split the **independent output ll3 domain** of complete bands 29..38. For each fixed ll3, the frozen ll2 ordering, both `drc3jj` calls, ascending l1 accumulation, `xi` multiplication and `acc += xi` recurrence must remain unchanged. Shard assembly is placement/concatenation only and performs no arithmetic reduction across shards.

## Frozen shard geometry and ordering

Candidate file: `experiments/073cr_wm_s3_ll3_sharded_resource_candidate_v0_1.json`.
Candidate creation commit: `d27deaec49f175ac17267fce94bfe2214a02ab6d`.
Expected candidate file SHA256: `15d8f15ae63cec84052f727c8f826e84aeb582671a95c152c565098c32a2c5b5`.

Exactly 64 complete ll3 shards cover bands 29..38 with allocation:
`3,3,4,5,6,7,8,9,9,10` shards respectively.

The run order is prospectively frozen as descending exact integer operation proxy
`sum 3*(min(ll2+ll3,lmax)-abs(ll2-ll3)+1)`, ties by `(band,ll3_lo,ll3_hi)`.
The exact serialized 64-entry heavy-first queue SHA256 must equal
`3ba315d9bc24883ef746d92e785e0a040f9b13e751f59dda9a93e825a6390db4`.
No result-dependent timing feedback may alter this order.

Research-only preflight predicted heavy-first list-scheduling utilization `0.9918607445989314`; this is not an acceptance result.

## Frozen implementation invariants

- exactly 8 visible logical CPUs on the self-hosted runner;
- exactly 8 persistent outer process workers;
- at most 8 numerical shards in flight;
- `OMP_NUM_THREADS=1`, `OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `BLIS_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`, `VECLIB_MAXIMUM_THREADS=1`, `OMP_DYNAMIC=FALSE`;
- each persistent worker loads immutable PCL, `_nmtlib` path and helper ABI once;
- helper is `ci/exp073cr_stream_band_ll3_range_v0_1.c`, creation commit `bb856b8c49eea804fea73807c3eef53cc20ff3fa`;
- compiler flags must include `-O2 -shared -fPIC -fopenmp -fno-fast-math -fno-associative-math -ffp-contract=off -fno-tree-vectorize`;
- a newly completed shard is stored canonically, SHA-checked and pushed durably before that worker slot is refilled;
- restore accepts only complete shards matching the frozen contract fingerprint, candidate SHA, exact `(band,ll3_lo,ll3_hi)`, helper symbol, dtype, shape and payload SHA;
- dedicated checkpoint namespace: `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-1`;
- no competing DSIR home task is permitted.

## Hosted seed and reference rule

The home runner MUST NOT import Exp073CQ directly. A GitHub-hosted seed stage must exact-restore the immutable Exp073CQ v0.2 terminal head `32bf0d1bdbcc2480f8b77f936ea6dc1f425812b0`, verify its fingerprint/status/provenance, and create the Exp073CR checkpoint seed containing:
- immutable PCL;
- exact complete-band reference payloads for bands 29..38 copied from CQ terminal checkpoint;
- SHA-bound receipts and Exp073CR contract.

These CQ payloads are used only as **resource-equivalence references**. They do not become Wm_S3 scientific authority.

## Mandatory hosted pre-execution gate

Before any home execution, a hosted workflow must:
1. compile the authoritative Exp073CR helper under frozen FP flags and verify the required exported symbol;
2. verify candidate SHA and heavy-first queue SHA;
3. exact-restore and validate the Exp073CR hosted seed;
4. run bitwise ll3 regression using authoritative helper/code against immutable complete-band references for multiple bands/partitions, requiring `np.array_equal`, canonical SHA equality, finite values and no first difference;
5. statically audit 8-worker/nested=1, durability-before-refill, exact restore/reassembly, no tolerance rescue, dedicated namespace and source/binding provenance;
6. emit an explicit PASS token. Green workflow status alone is insufficient.

Research-only regression run `33754644074` / job `100646005106` / artifact `9892971697` already found bitwise equality on bands 0,7,15 under two partition schemes, but remains +0/+0 and cannot replace this authoritative hosted gate.

## Frozen terminal acceptance

After all 64 shards are durably complete, reconstruct complete bands 29..38 by exact placement. For **every** band 29..38 require:
- canonical `<f8 [12288]`;
- finite;
- `np.array_equal(reconstructed, hosted_seed_reference)`;
- canonical SHA256 equality.

Resource telemetry is computed from all 64 durable shard receipts so resume is deterministic:
- active wall = latest numerical shard end minus earliest numerical shard start;
- sum worker numerical CPU = sum of all shard `worker_cpu_seconds`;
- effective cores = sum CPU / active wall;
- `cpu_fraction_of_8_compute = effective_cores / 8`;
- require `cpu_fraction_of_8_compute >= 0.90`;
- require positive swap increase = 0 KiB.

PASS requires exact equality of all ten complete bands, finite/canonical outputs, zero positive swap increase, all 64 durable shards, valid provenance/contract, and CPU fraction >=0.90.

Any exact mismatch is an **exact resource-equivalence FAIL +0/+0** and is not rescued. CPU below 0.90 is **resource/performance FAIL +0/+0**. Swap increase >0 is **resource safety FAIL +0/+0**. Infrastructure/transport/software failure before a valid final receipt is **infrastructure incomplete +0/+0** and must preserve durable shards for a prospective resume repair.

No Exp073CR result can by itself create Wm_S3 angular scientific authority. Only a validated Exp073CR resource PASS permits preregistration of the separate fresh-independent-PCL Wm_S3 A/B scientific successor and deterministic finalizer.
