# DSIR immutable recovery — 2026-09-04 — Exp073CD D1 / Exp073CE I1 / Exp073CF E1

Scope: DSIR only. RTK/RQIR excluded.

## Exp073CD v0.1
Raw job log for run/job `33834935589 / 100905384484`, head `514198bf15995424c56b174459dadab60e42fdbb`, emitted `D1_DES_SCALE_RESOURCE_CHECKPOINT_DESIGN_PASS`. This is support/resource PASS `+0/+0`, not Wm_S3 authority. No Actions artifact was produced; the validated raw job log is the receipt authority.

Frozen exact sizing: full-stock logical MCM `24576 x 24576` = `603979776` doubles = `4831838208` bytes = exactly `4.5 GiB`; complete row `196608` bytes; full window `[2,39,2,12288]` = `15335424` bytes; selected canonical TE `<f8 [39,12288]` = `3833856` bytes.

Frozen durable per-replica stages: `fresh_masks_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_te_complete -> replica_receipt_complete`; fail-closed SHA256/provenance/source-head/contract binding; separate A/B namespaces; no cross-replica numerical restore.

## Exp073CE hosted integration-contract static audit
Prereg `98f95349d04aeffa64eb14ab2d8300be45e7fd1d`; contract `6d6a4d7eb4b15e026100e81670cb3897396ba94a`; static audit `b0ad9af5f0312109708932b43531944ddfbe96c9`; workflow `6a9e08dde79145f8401100fb375dbede7b9bab07`; activation/head `0dc78e0a5155ac5f589941ae7d0cb89613305b49`.

Run/job `33839372369 / 100918343441` completed SUCCESS. Raw receipt emitted `I1_EXP073BU_INTEGRATED_DRIVER_STATIC_AUDIT_PASS`, contract fingerprint `b2359ecb8846c591639e9d4e2679585ba2888ef009d5e5959c011f36fd867b84`, accounting `+0/+0`, `wm_s3_authority_created=false`, `exp073bu_activated=false`. Artifact `9924372269`, digest `sha256:9fa5e0f2839341d16bb845ee7b6f04891fb3eca5a23cc15579d8ea2e0737092e`.

### Naming-governance finding
A later exact-tree/inventory audit exposed a pre-existing unrelated workflow `.github/workflows/exp073ce-memory-stable-wm-pcl-exact-selftest-v0-1.yml`. Thus label `Exp073CE` was not globally unique even though the earlier indexed collision search returned empty. Historical run/commit provenance remains immutable and the machine checks remain valid support evidence, but the label itself MUST NOT be used as a unique authority key. No scientific workload was launched from it. Future experiment labels must be checked against the exact recursive repository tree, not search indexing alone.

## Exp073CF executable-component inventory
Prereg `0964517f0f60b6c1369f3f2649518fdaf0e7bbab`; workflow `6eac2124c3942d68d918ef149ca11d436b496925`; activation/head `56ae01872478f72325b14feea244284ad35e9bbd`; run/job `33839467631 / 100918617192`; artifact `9924402381`, digest `sha256:269f181f5e4dd3a235e863716c169389cdbc43bf6416d7c863d6c5a808f9ca61`.

Raw receipt emitted `E1_EXECUTABLE_COMPONENT_SET_IDENTIFIED`, accounting `+0/+0`, `wm_s3_authority_created=false`, `exp073bu_activated=false`.

Key executable source blobs identified for a future integrated driver:
- fresh replica-local PCL: `ci/exp073bu_fresh_wm_s3_pcl_v0_1.py` blob `73ef04c479547dc8e2e89c9f511f1a55fae3ed64`;
- exact full-stock ncls=2 operation route: `ci/exp073bx_full_mcm_stock_order_v0_1.py` blob `ae0282cbbcdd298f00765d8de68545fe214cec0e`;
- stock write/persist -> mmap chain: `ci/exp073ca_stock_write_fits_to_mmap_exact_chain_v0_1.py` blob `d3c2e3a2ec42ddcb5811447499d80a4a1cfa3132`;
- OS mmap verification: `ci/exp073cc_verify_fits_memmap_backing_v0_1.py` blob `88d17ad76cabc1651df6b6035d897e9f42853ca5`;
- exact mmap downstream: `ci/exp073by_mmap_full_mcm_downstream_v0_1.py` blob `a22d14ad9ae7e81ba6dd35c61b9ab35a05617d76`;
- 8-worker checkpoint/resource architecture: `ci/exp073cr_wm_s3_ll3_sharded_resource_v0_1.py` blob `934c339bb01dd7f541e9191129bcdc8b3a7ad772`;
- checkpoint git-sync regression: `ci/test_dsir_checkpoint_git_sync_v0_2.sh` blob `39e90b4c1986f1972d43e9dce7b74f0082c39559`.

## Authority state
DSIR-HOME-PC remains FREE. Exp073BU scientific Wm_S3 A/B remains NOT ACTIVATED. Wm_S3 scientific authority remains absent. Frozen science boundaries unchanged. Next permitted work is a collision-free exact blob-binding/assembly gate, then hosted static audit of the executable integrated driver, then an explicit fresh no-competition check before any single checkpointed 8-core home scientific activation.
