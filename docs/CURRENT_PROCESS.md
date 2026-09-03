# DSIR current-process ledger

Updated: 2026-09-04

Repository, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active processes
- **No self-hosted heavy process is currently authorized by this ledger.**
- Live Actions after Exp073BU preregistration: **0 queued / 0 in-progress**.
- DSIR-HOME-PC ownership: **FREE**.
- Exp073BU numerical execution is **not yet activated**. Do not launch home compute until fresh-PCL implementation + hosted static audit + explicit activation are frozen.

## Prospective scientific gate — Exp073BU v0.1
- purpose: fresh-independent-PCL exact A/B successor for missing `Wm_S3` angular authority
- preregistration: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`
- preregistration commit: `e1a0332c128c87049fb8699018a3a3e71c9c5321`
- preregistration recovery: `recovery/2026-09-04_exp073bu_wm_s3_fresh_ab_preregistered.md`, commit `2cb2128fcac1d435b4cb9ddf4d711a025a5fc956`
- pre-implementation contamination audit: `recovery/2026-09-04_exp073bu_preimplementation_no_old_pcl_import_audit.md`, commit `e8d75c7ea1b04d88d2f1266129ce4d89b5170349`
- expected PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`
- intended namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`
- current state: **PREREGISTERED / FRESH-PCL IMPLEMENTATION REQUIRED / NOT AUDITED / NOT ACTIVATED**

## Newly closed implementation audit
Direct reuse of `ci/exp073cr_wm_s3_ll3_sharded_resource_v0_1.py` is **forbidden for Exp073BU science**. The CR driver initializes workers from `root/upstream/pcl.npy`; its seed obtains that PCL and numerical reference bands from the Exp073CQ terminal checkpoint. That is valid for the historical resource-equivalence gate but violates Exp073BU's prospective prohibition on importing Exp073CR/CQ/CM numerical Wm_S3 payloads.

Reusable from Exp073CR: 8 outer workers, nested threads=1, deterministic source-order shards, durability-before-refill, canonical `<f8` hashing, fail-closed receipts/restores, exact reassembly, telemetry and first-causal-failure persistence.

Not reusable as science input: historical `upstream/pcl.npy`, reference bands, their hashes, or equality to those arrays.

## Exact next implementation gate
Recover/audit the repository code path that creates the Wm pseudo-C_ell/coupling precursor directly from immutable S3 and lens-mask authorities. For each replica independently implement:

`fresh R1 S3 + fresh public lens mask -> fresh replica-local PCL complete-stage checkpoint -> 8-core exact ll3 shards -> full 39-band canonical array -> durable final receipt`.

A and B must have isolated PCL/checkpoint state and cannot exchange numerical outputs before both final receipts are durable. If fresh PCL generation cannot be safely checkpointed at a complete-stage boundary, no home run is allowed until redesigned.

After implementation: machine-checkable hosted static audit -> freeze fingerprint/source head -> fresh zero-live-heavy-run reconciliation -> explicit activation -> exactly one DSIR-HOME-PC owner process.

## Frozen recovered inputs
- Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- S3 rows `4,196,641`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique pixels `2,943,132`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`
- lens bytes `104595840`, SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`, retain original weights iff `mask>0.5`
- DES NSIDE=4096, RING/C, ell `0..12287`, 39 bands, Wm `TE<-TE`, canonical `<f8 [39,12288]`
- exact A/B comparison requires SHA256 equality and `numpy.array_equal`; no tolerance rescue

## Preserved resource authority — Exp073CR v0.3
- run/job/head `33771269117` / `100701857748` / `023fcfa28f0eb904656c76e55c55d821e50c8155`
- raw token `PASS_EXP073CR_V0_3_WM_S3_LL3_SHARDED_8CORE_RESOURCE`
- checkpoint `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `db8221278798ea56b579a3dc96565fef4497bb7f`
- fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- CPU fraction `0.9623990689242612 >= 0.90`; swap increase `0 KiB`; 64 shards; exact resource reconstruction PASS
- artifact `9903527609`, digest `sha256:28f6141e641726351b6dd804c07db28b6c4152de5a71a0c0b098b539a6bc0256`
- classification **RESOURCE PASS `+0/+0`**, not Wm_S3 science

## Historical governance
- authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`: Exp073X2 P=`INFRASTRUCTURE_INCOMPLETE`, Q=`SCIENTIFIC_REPEATABILITY_FAIL`; Exp073AF rule 10 => `BLOCK_PRODUCTION`; old Exp073AA Wm_S3 route never acquired authority.
- Exp073BT v0.3 remains Q5 incomplete infrastructure/source-linkage diagnostic `+0/+0`: run `33794449690`, job `100778710837`, artifact `9908640902`, digest `sha256:e3fc8d1f390101900d35f90e03f0317f62675e23a6971fb01aff4bc233f86dd9`.
- historical outcomes remain immutable.

## Preserved science boundaries/accounting
- Wm_S1 Track-A exact PASS preserved; admitted Wm_S2 authority preserved; Wm_S3 authority absent.
- `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.