# DSIR immutable recovery — Exp073EN terminal candidate PASS; Exp073EO runtime repair

Date: 2026-09-06. Scope: DSIR only; RTK/RQIR excluded.

## Exp073EN terminal evidence
Authoritative workflow run `33994398927`, self-hosted job `101382229273`, head `4d1cbd504067a64a94b038292793e5e8bffba911` completed SUCCESS. Workflow SUCCESS is not itself science authority.

Terminal artifact `9980311204` (`exp073en-ww-s0-s0-filebacked-fullres-network-retry-evidence-v0-2`) has GitHub digest `sha256:54db5c1c213a041616111071c23ce2710e88c0f085efc9e625dd51538e71dd49`; an independent artifact ZIP SHA256 recomputation matched exactly.

The raw terminal receipt classifies Exp073EN as `SCIENTIFIC_CANDIDATE_PASS_PENDING_PROVENANCE_ADMISSION` and emits token `PASS_EXP073EN_WW_S0_S0_FILEBACKED_AB_EXACT_REPEATABILITY_8CORE_V0_1`. Frozen source head `de83e20a68f79ccf25b89b0d33eb4206e294c757`, contract fingerprint `b7845df5ce4bc2bd730461476b7ff0831512003ceb5b3558436005c9876bd251`, NaMaster head `24365fa59a38c15732f4f37e8b29265b75c442d5`, hosted Exp073EM artifact/digest and storage patch SHA256 all match preregistered identities.

Replicas A and B each retain the complete ordered six-stage durable chain: `fresh_s0_mask_complete -> fresh_workspace_mcm_complete -> mcm_fits_verified -> full_window_complete -> selected_ee_complete -> replica_receipt_complete`. Both selected `EE<-EE` payloads are canonical `<f8 [39,12288]`, finite, and independently recompute SHA256 `244f8f831ac7041af00f9cddca0ea93a04298fb0b1b029af5030376ce93da647`; bytewise comparison and the frozen `numpy.array_equal` comparison both pass exactly. Full-window hashes also agree (`525f4a9dd1f1da6a9d3e0f2b8fb58a4e3e8b9e977117d30ff9a7b120069d65a2`). No tolerance rescue is present.

Both adapter receipts prove file-backed MCM operation with `rows=49152`, regular-file mmap-backed base chains and exact canonical MCM SHA256 `efc00569a53bfb6cb71894d79b19abea5005c3a1042d735a56becd6db82c68da`. Post-receipt prune receipts preserve hashes and show huge workspace/canonical files were removed only after complete replica receipt. Exp073EN does **not** itself create `WW_S0_S0` authority; admission remains exclusively reserved to Exp073EO.

## Exp073EO activation and first causal failure
Prospectively frozen prereg blob remains `490e1f44a7d7bb9b42dc00a72e0b39961da1692a`; auditor blob remains `4403d3e140acd14f0b95a31a8b2851f3229c1da3`; real-artifact consumer blob remains `704395173f10d69b4496e1422884fc71097c2919`.

A hosted-only real-artifact workflow was prepared at commit `856c71c3319f0709e3dfd8d8748f4c8f259f6455` and activated at head `0fea64f57440055bcce6d4d9b54b5efb67a019b8`. Run/job `34005282438 / 101411204812` bound all frozen identities, passed live GitHub metadata binding and independently rechecked the EN ZIP digest, then failed before auditor execution with the first causal error `ModuleNotFoundError: No module named 'numpy'`. This is `INFRASTRUCTURE_RUNTIME_DEPENDENCY +0/+0`, not a scientific or provenance FAIL.

The smallest prospective repair changed only the hosted workflow runtime: install and verify `numpy==2.3.3`; frozen prereg, auditor, consumer, EN artifact, source, contract and acceptance logic are unchanged. Repair commit `b2bb1c456b36304bc998bdadbebba05f034c37e9`; reactivation head `1b25f43c69e630d108bb984ad1916b407dc02002`.

## Current process
Exp073EO repaired run `34005304226`, job `101411264696`, hosted-only, is the sole active admission process at this recovery write. Home runner ownership is released by terminal Exp073EN; no competing self-hosted DSIR work has been launched. Exp073EL v0.2 remains blocked until a real Exp073EO PASS creates `WW_S0_S0` authority.

Exact next action: terminal-consume run `34005304226`. Only token `PASS_EXP073EO_WW_S0_S0_FILEBACKED_PROVENANCE_ADMISSION_V0_1` with raw receipt/artifact verification may admit `WW_S0_S0`; otherwise classify the first causal failure fail-closed without rewriting Exp073EN candidate evidence.
