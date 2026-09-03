# DSIR immutable recovery correction — Exp073CR v0.3 driver lineage

Date: 2026-09-03
Scope: DSIR only.

This note prospectively corrects one documentation-only ambiguity in the immediately preceding recovery note `recovery/2026-09-03_exp073cq_v0_2_resource_fail_and_exp073cr_v0_3_launch.md`. It changes no code, checkpoint, resource contract, arithmetic, threshold or scientific authority.

The authoritative Exp073CR v0.3 binding file `experiments/073cr_wm_s3_ll3_sharded_binding_v0_3.json` and durable seed `checkpoint/contract.json` both bind the v0.3 driver to **`365fd7a8527b2dafe4785f95fa104276788c11d1`**. That is the sole authoritative driver commit for v0.3 runtime verification.

The similar string `365fd7a8527b2dafe478160c9cfd28484169e48ca` appearing in the preceding recovery note came from a stale/incorrect summary transcription and MUST NOT be used as driver authority.

Preserved v0.3 frozen lineage:
- preregistration `fb10a589ee5ac03f478160c9cfd28484169e48ca`;
- driver `365fd7a8527b2dafe4785f95fa104276788c11d1`;
- self-hosted workflow `85993d73565c3fc4d1389cc942bc69073b89d89e`;
- hosted seed audit workflow `5f5a7a060b17e11b0f53453d6ca6898cda00d2fd`;
- binding `0e0d13a6f7736eb56689d57c3557410007ec48d2`;
- static audit `312a526997dde0a43a58fa64b5ce6f051d2df9d8`;
- seed head `cb408d4edb2a73413db8d3181e9cb1680dc19276`;
- seed fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`.

Classification remains resource/checkpoint/static provenance `+0/+0`; Wm_S3 scientific authority remains absent.
