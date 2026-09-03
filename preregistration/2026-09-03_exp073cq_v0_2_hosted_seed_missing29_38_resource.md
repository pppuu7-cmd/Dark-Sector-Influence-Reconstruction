# Exp073CQ v0.2 — hosted-seeded missing29-38 resource continuation

Status: prospectively frozen before seed/home execution. DSIR only. Article-3 delta `+0/+0`.

Purpose: repair Exp073CQ v0.1 infrastructure failure at parent-import without mutating that historical attempt and without recomputing Exp073CP bands 0..28.

Frozen authority:
- immutable parent namespace/head: `checkpoints/exp073cp-wm-s3-full39-resource-v0-1` / `025629d9bb7b113bd0548ff6a32c6ee5812ae245`;
- parent contract fingerprint: `32d15a39f1bcdcee0f9b9f88ebc8fd8f82eb850bb71eca4b51d95eb40f111efc`;
- exact imported/read-only bands: 0..28;
- numerical allowlist: exactly 29..38;
- successor namespace: `checkpoints/exp073cq-wm-s3-missing29-38-resource-v0-2`;
- parent import MUST be executed and durably pushed on GitHub-hosted runner before any self-hosted authorization;
- self-hosted workflow MUST restore that exact seeded successor head first and MUST NOT restore/import Exp073CP directly;
- exactly 8 outer numerical workers, max 8 in flight, nested BLAS/OpenMP/MKL/OpenBLAS threads=1;
- durable checkpoint immediately after every complete newly computed band;
- canonical dtype/shape `<f8 [12288]` per band and canonical final `<f8 [39,12288]`;
- exact first-8 array/SHA equivalence remains mandatory; no tolerance, rounding, smoothing or averaging rescue;
- CPU resource gate remains `cpu_fraction_of_8_compute >= 0.90` under the frozen new-bands-only metric;
- positive swap increase is FAIL;
- any exact mismatch is numerical/resource FAIL under this resource experiment, never repaired by tolerance;
- any transport/software/checkpoint defect is infrastructure incomplete `+0/+0` and must preserve all exact-valid durable units.

Hosted seed is not scientific computation and cannot create Wm_S3 authority. Home launch is forbidden until: (1) hosted seed exact PASS with durable successor head, and (2) post-seed hosted static/checkpoint audit PASS binding the exact driver/workflow/binding/seed head.

Frozen resource PASS token: `PASS_EXP073CQ_V0_2_WM_S3_MISSING29_38_8WORKER_HOSTED_SEEDED_RESOURCE`.
