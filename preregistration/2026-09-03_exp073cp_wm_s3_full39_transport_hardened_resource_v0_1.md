# Exp073CP — Wm_S3 full-39 8-worker transport-hardened checkpoint resource qualification v0.1

Date: 2026-09-03
Status: PROSPECTIVELY FROZEN; HOME EXECUTION FORBIDDEN UNTIL POST-IMPLEMENTATION HOSTED STATIC AUDIT PASS AND ACTIVATION BINDING

## Motivation and historical boundary
Exp073CO v0.1 remains immutable. Its first home attempt reached the full39 compute step but checkpoint transport failed on a GitHub HTTPS/GnuTLS handshake during the first band durability push. The Python process then spent a long interval unwinding/waiting for already-submitted worker futures. A direct rerun failed earlier while restoring the immutable Exp073CM checkpoint because `dsir_checkpoint_git_sync_v0_2.sh::fetch_exact_head` used an un-retried `git fetch` and the same TLS transport failed.

Both Exp073CO attempts are infrastructure/checkpoint-control incomplete, `+0/+0`. They are NOT Wm_S3 scientific arithmetic failures and do not alter Exp073CN's historical CPU-target FAIL.

Exp073CP is a new resource/checkpoint/performance experiment. It may only repair transport robustness and bounded scheduling behavior. It cannot rescue or rewrite any historical result and cannot create Wm_S3 scientific authority by itself.

## Frozen scientific arithmetic
Exactly unchanged from Exp073CO:
- task `Wm_S3`, source bin 3, signature `(0,2,0,2)`;
- DES `NSIDE=4096`, RING/C;
- `ell=0..12287`, `L=12288`;
- all 39 frozen bands `0..38` with the authoritative edges already in DSIR;
- `Wm TE <- TE`;
- canonical little-endian `<f8`;
- inherited immutable Wm_S3 PCL SHA256 `ec34ee34311f3b02a16e118113b5b1acd1b961859caccd2c4387c0ae529cd72d`;
- inherited frozen reference bands `[0,8)` SHA256 `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`;
- exact `np.array_equal` and SHA equality only; no tolerance/ULP/rounding/averaging/smoothing/effective-ell/effective-z/effective-k/fiducial-P rescue.

## Frozen compute architecture
- exactly `8` outer worker processes;
- nested OMP/BLAS/MKL/OpenBLAS/BLIS/NUMEXPR threads pinned to `1`;
- dynamic complete-band scheduling over all 39 bands;
- at most 8 numerical band futures may be in flight at once;
- after a completed band is materialized locally, the scheduler may refill one worker slot before its remote durability postcheck so numerical occupancy can remain high, but it MUST NOT build an unbounded backlog;
- on irrecoverable checkpoint transport failure, queued futures are cancelled and active worker processes are terminated/bounded-aborted rather than intentionally waiting for the remaining 39-band queue;
- per-band arithmetic/order/compiler reproducibility flags remain unchanged.

## New transport contract — checkpoint sync v0.3
A new checkpoint transport implementation must be frozen and audited before home use. It must:
1. preserve fail-closed PRESENT/ABSENT/exact-head semantics from v0.2;
2. use bounded retries for `ls-remote`, branch `fetch`, and `push` transport operations;
3. use bounded per-attempt timeouts so a dead transport cannot block indefinitely;
4. after every successful branch fetch, verify the fetched commit equals the previously bound exact remote head and re-query the remote head; any semantic head race fails closed rather than retrying as if it were transport noise;
5. after every push attempt, independently re-query the remote head so response-loss after a successful push is recognized safely;
6. retries are allowed only while the previously bound remote state/head remains unchanged;
7. transport retries/timeouts never change checkpoint payloads, arithmetic, admission rules, or exact hashes.

HTTP/1.1 forcing is permitted as a transport-stability setting because it changes no repository/checkpoint semantics.

## Durable checkpoint contract
Dedicated new namespace: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1`.

Mandatory semantics:
- restore and exact-verify immutable Exp073CM upstream first;
- contract fingerprint binds source head, prereg commit, driver commit, workflow commit/binding, checkpoint-sync v0.3 implementation and all frozen resource/science parameters;
- every completed band payload is canonical `<f8 [12288]>` with exact SHA/provenance/ell identity;
- a band is admitted for resume only after exact remote durability postcheck;
- resume computes only missing/unadmitted bands;
- wrong head, corrupt payload, wrong band, contract mismatch or unknown exhausted transport fails closed;
- final telemetry and final receipt are also durably checkpointed.

## Frozen telemetry and PASS gates
The primary full-39 compute-active interval is from earliest numerical worker start to latest numerical worker end. Let `effective_cores = sum(worker numerical CPU seconds) / compute_active_wall_span`; `cpu_fraction_of_8_compute = effective_cores / 8`.

All are mandatory for PASS:
- all 39 band receipts exact-valid and finite;
- bands `[0,8)` exactly equal the frozen reference and canonical SHA equals `36ee9fca9fb276a30d8ebb97cb04fddc7e95cff18fb29248c033bb364ea2d8cf`;
- `cpu_fraction_of_8_compute >= 0.90` on the prospectively frozen full-39 segment;
- no positive swap increase during the defined numerical run;
- every admitted band and final state passes durable checkpoint exact postcheck;
- transport wall/retry diagnostics are recorded separately and cannot be used to alter the CPU formula;
- no post-hoc interval selection or tolerance rescue.

Frozen PASS token: `PASS_EXP073CP_WM_S3_FULL39_8WORKER_TRANSPORT_HARDENED_RESOURCE_V0_1`.

Negative classifications must distinguish exact mismatch, swap safety, CPU-target resource failure, and infrastructure/checkpoint-control incomplete. Every Exp073CP outcome is Article-3 `+0/+0`.

## Authorization order
1. freeze this preregistration;
2. implement checkpoint sync v0.3;
3. implement Exp073CP driver and workflow using the new namespace;
4. create immutable binding containing exact prereg/sync/driver/workflow commits;
5. run a NEW hosted post-implementation static/regression audit over the actual final files;
6. only hosted audit PASS may create activation authority;
7. immediately before home launch, verify no competing queued/in-progress DSIR Actions;
8. launch exactly one Exp073CP home run.

Full Wm_S3 scientific A/B production remains forbidden until a resource gate actually passes.
