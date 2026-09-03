# Exp073BU v0.1 fresh-PCL implementation static audit — PASS

Date: 2026-09-04
Scope: DSIR only; RTK/RQIR excluded.
Accounting: `+0/+0`; no Wm_S3 scientific authority is created here.

## Implementation

Standalone helper: `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py`
Implementation commit: `e6ffda3b5c558c964cf486d78a792d40bf9c76e5`
Hosted static-audit workflow commit/head: `04b0b29cbed039de6520eb6a738f78bdc9785885`
Helper SHA256 measured by hosted audit: `99f3129838c06ccbb6629bd6bd36d524d35f2bdc70efeee492b381fa567d4b52`
Preregistration SHA256 measured by hosted audit: `4a7be4440e51197ef7811832b7ae00690750a57b4af3f4f9f0b3530ffe902622`

## Hosted audit

Run/job: `33816258925` / `100848963246`
Conclusion: SUCCESS; raw audit receipt consumed.
Raw token: `PASS_EXP073BU_FRESH_PCL_HOSTED_STATIC_AUDIT_V0_1`
Artifact: `9916627301`
Artifact digest: `sha256:35e4ace8514a3614bc697ceb398268789a9db7e81d049b1910ca7a428dccd65d`

The audit machine-checked:

- Python syntax/AST;
- no imports from historical Exp073CR/CQ/CM/CL/AZ helpers;
- no historical Wm_S3 PCL/window/checkpoint/reference numerical literals;
- exact bound R1 artifact identity and S3 record/occupancy hashes;
- exact bound redMaGiC lens hash and `mask>0.5` weighted semantics;
- fresh spin-0 lens / spin-2 S3 `NmtField` mask-ALM path;
- fresh `healpy.alm2cl` PCL construction;
- PyMaster 2.7 binding;
- canonical `<f8 [12288]` complete-stage persistence;
- explicit receipt flags forbidding historical numerical reference/import and other-replica reads.

## Classification

**PASS — static fresh-PCL implementation gate, `+0/+0`.**

This establishes that the source-side complete-stage PCL implementation is prospectively compatible with the frozen Exp073BU contract. It does not establish numerical PCL output, Wm_S3 window authority, or A/B repeatability.

## Next permitted implementation gate

Bind the validated Exp073CR ll3-range arithmetic as source-code lineage only, never numerical lineage. Before scientific execution, prove machine-checkably that the BU kernel preserves the exact per-shard operation order and does not read any historical Exp073CR/CQ/CM numerical payload. Then assemble a BU-only driver that computes all 39 bands from each replica's fresh PCL, with complete-band/checkpoint units for the lighter domain and exact ll3 shards for the heavy tail, isolated namespaces A/B, exactly 8 outer workers where applicable, nested threads=1, durability-before-refill, and final exact comparator after both receipts are durable.
