# DSIR current-process ledger

Updated: 2026-09-04

Repository, immutable recovery notes, validated Actions logs/artifacts and durable checkpoints are authoritative. DSIR only; RTK/RQIR excluded.

## Active processes
- **No self-hosted heavy process is currently authorized by this ledger.**
- DSIR-HOME-PC ownership: **FREE**.
- Exp073BU numerical execution is **not yet activated**.
- The latest support-only hosted staging run `33815944381` / job `100848002128` is terminal SUCCESS and has been consumed against its raw receipt.
- Historical mislabelled connectivity probe run `33813694199` is terminal CANCELLED and creates no live ownership conflict.

## Prospective scientific gate — Exp073BU v0.1
- purpose: fresh-independent-PCL exact A/B successor for missing `Wm_S3` angular authority
- preregistration: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`
- preregistration commit: `e1a0332c128c87049fb8699018a3a3e71c9c5321`
- expected PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`
- intended namespaces: `checkpoints/exp073bu-wm-s3-a-v0-1`, `checkpoints/exp073bu-wm-s3-b-v0-1`
- state: **PREREGISTERED / FROZEN INPUT STAGING PASS / FRESH-PCL IMPLEMENTATION REQUIRED / SCIENTIFIC IMPLEMENTATION NOT YET AUDITED OR ACTIVATED**

## Newly closed frozen-input staging gate
Support workflow: `.github/workflows/exp073bu-input-staging-closure-v0-1.yml`
Implementation/head: `00b8a2c25ec4e50ae1027a1a2141a0023a033ab9`
Run/job: `33815944381` / `100848002128`
Raw token: `PASS_EXP073BU_FROZEN_INPUT_STAGING_CLOSURE_V0_1`
Artifact: `9916526843`
Artifact digest: `sha256:74307daaf5e7cece0ce2be2fa68edef8bc63c2e7f2439f20375ccac3dde97b69`
Immutable recovery: `recovery/2026-09-04_exp073bu_frozen_input_staging_closure_pass.md`, commit `60e5fcefbba9ab5701be207e88e6806426d6675e`.
Classification: **input/provenance PASS `+0/+0`; Wm_S3 scientific authority delta = none**.

The hosted job independently downloaded bound Exp073R1 artifact `9720335366` from run `33270843577`; GitHub reported exact artifact SHA256 `ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`. Inside it the job verified S3 record bytes/SHA `16,786,564` / `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec` and occupancy bytes/SHA `25,165,824` / `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

The same hosted job fetched the repository-frozen first-party DES redMaGiC URL previously validated by Exp073S0 run `33086762750` / job `98568401949` / head `82c5804b1fcbbdc100f09a9878643ddc51975d8e` and reverified lens bytes/SHA `104,595,840` / `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`.

Therefore the prior external-input locator gap is closed without browser/search discovery and without importing historical Wm_S3 numerical windows.

## Connectivity support result preserved
Corrected self-hosted connectivity probe run `33813773616`, job `100841253278`, head `20741f82249363294e835d0cf01ebbdfddc6f6e3` passed with raw token `PASS_EXP073BU_SELFHOSTED_CONNECTIVITY_PROBE_V0_1`; it observed runner `DSIR-HOME-PC`, Linux/X64, 8 online CPUs. This is infrastructure-only and creates no science authority. Earlier run `33813694199` targeted a nonexistent custom label and is terminal CANCELLED.

## Exact next implementation gate
Implement and hosted-audit the fresh replica-local input-to-PCL path. Each replica must independently:

`bound R1 S3 pixel records -> exact dense S3 count map` and `frozen first-party redMaGiC FITS -> exact weighted lens mask -> fresh NaMaster/PyMaster 2.7 fields/workspace/PCL -> complete-stage durable replica-local PCL checkpoint -> exact 8-core ll3 shards -> complete 39-band canonical array -> durable receipt`.

The implementation must not import any Exp073CR/CQ/CM numerical Wm_S3 array/PCL/hash/reference target or the other replica's outputs. A and B remain isolated. If fresh PCL generation cannot be durably checkpointed at a complete-stage boundary, no home run is allowed until redesigned.

After implementation: machine-checkable hosted static audit -> freeze fingerprint/source head -> fresh zero-live-heavy-run reconciliation -> explicit activation -> exactly one DSIR-HOME-PC owner process.

## Frozen recovered inputs and science semantics
- Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`
- S3 rows `4,196,641`; record SHA `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`; unique pixels `2,943,132`; occupancy SHA `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`
- lens bytes `104595840`, SHA `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`, retain original weights iff `mask>0.5`
- DES NSIDE=4096, RING/C, ell `0..12287`, 39 bands, Wm `TE<-TE`, canonical `<f8 [39,12288]`
- exact A/B comparison requires canonical SHA256 equality and `numpy.array_equal`; no tolerance rescue

## Preserved resource authority — Exp073CR v0.3
- run/job/head `33771269117` / `100701857748` / `023fcfa28f0eb904656c76e55c55d821e50c8155`
- raw token `PASS_EXP073CR_V0_3_WM_S3_LL3_SHARDED_8CORE_RESOURCE`
- checkpoint `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `db8221278798ea56b579a3dc96565fef4497bb7f`
- fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`
- CPU fraction `0.9623990689242612 >= 0.90`; swap increase `0 KiB`; 64 shards; exact resource reconstruction PASS
- artifact `9903527609`, digest `sha256:28f6141e641726351b6dd804c07db28b6c4152de5a71a0c0b098b539a6bc0256`
- classification **RESOURCE PASS `+0/+0`**, not Wm_S3 science

## Historical governance and boundaries
- authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd`: Exp073X2 P=`INFRASTRUCTURE_INCOMPLETE`, Q=`SCIENTIFIC_REPEATABILITY_FAIL`; Exp073AF rule 10 => `BLOCK_PRODUCTION`; old Exp073AA Wm_S3 route never acquired authority.
- Exp073BT v0.3 remains Q5 incomplete infrastructure/source-linkage diagnostic `+0/+0`.
- Wm_S1 Track-A exact PASS preserved; admitted Wm_S2 authority preserved; Wm_S3 authority absent.
- `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.
- Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.
