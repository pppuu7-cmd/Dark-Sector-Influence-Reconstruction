# DSIR immutable recovery — Exp073BU pre-implementation old-PCL contamination audit

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Classification: implementation/provenance audit `+0/+0`.

## Question

Can the already validated Exp073CR 8-core ll3-sharded resource driver be reused directly for the newly preregistered Exp073BU fresh-independent Wm_S3 A/B scientific gate?

## Direct code audit

No.

`ci/exp073cr_wm_s3_ll3_sharded_resource_v0_1.py` is explicitly a resource-equivalence driver. Its worker initialization loads `root/'upstream/pcl.npy'`, and its seed path obtains that PCL by `validate_parent(parent)` from the Exp073CQ terminal checkpoint. The same seed also imports Exp073CQ reference-band numerical arrays. Exp073CR then shards the deterministic ll3 transform of that pre-existing PCL and compares reconstructed bands against the imported reference arrays.

This is correct for the frozen Exp073CR resource gate, but it is **not** a valid fresh scientific input path for Exp073BU.

The Exp073BU preregistration commit `e1a0332c128c87049fb8699018a3a3e71c9c5321` prospectively forbids any Exp073CR/CQ/CM numerical Wm_S3 array, band value, hash, checkpoint payload or partial result as a scientific input/reference/target. Therefore directly wrapping the CR driver would contaminate A/B with historical Wm_S3 numerical authority and violate the fresh-independent contract before any comparison.

## Preserved reusable architecture

The following Exp073CR mechanisms remain reusable as implementation patterns, after rebinding them to fresh per-replica inputs:

- exactly 8 outer `ProcessPoolExecutor` workers when the ll3 transform is used;
- nested BLAS/OpenMP/MKL/OpenBLAS thread pins to 1;
- source-order deterministic shard identities;
- durability-before-refill;
- canonical `<f8` payload hashing;
- fail-closed receipt validation;
- exact canonical reassembly;
- dedicated checkpoint namespaces;
- CPU/swap/resource telemetry;
- first-causal-failure diagnostic persistence.

What is **not** reusable for Exp073BU science is the CR/CQ numerical seed: `upstream/pcl.npy`, imported band references, or equality to those historical arrays.

## Required implementation architecture before audit/activation

Each Exp073BU replica A/B must first create its own fresh pre-ll3/PCL state from the exact immutable R1 S3 count-mask records plus the exact public lens mask under the frozen NaMaster 2.7, NSIDE=4096, RING/C contract. That fresh pre-ll3 state must itself become a complete durable stage with canonical SHA256, contract fingerprint and provenance receipt before any ll3 shards are dispatched.

The two replicas must use distinct fresh-PCL checkpoint stages/namespaces and may not import one another's PCL or hashes before both final receipts are complete. If fresh PCL generation cannot be made safely checkpointable, Exp073BU must not run on home until redesigned.

After each fresh replica PCL is durably frozen, the validated CR ll3 shard scheduler may be adapted to consume only that replica-local PCL and to assemble all 39 bands without historical reference-band comparison. Scientific comparison is only A-vs-B at the terminal comparator.

## Immediate next engineering gate

Locate/recover the repository code path that produces the Wm pseudo-C_ell / coupling precursor directly from the exact S3 and lens masks without importing historical Wm_S3 numerical output. Audit that path for deterministic canonical output and safe complete-stage checkpointing. Then implement:

`fresh masks -> fresh replica-local PCL checkpoint -> 8-core exact ll3 shards -> full 39-band replica array -> durable final receipt`

for A and B separately, followed by the frozen exact A/B comparator.

No numerical home run is authorized before this implementation is statically audited and explicitly activated.

## Accounting

No science result and no readiness change. Wm_S3 authority remains absent; Article-3 readiness remains Verified 52.0% | Draft/data 54.6%.