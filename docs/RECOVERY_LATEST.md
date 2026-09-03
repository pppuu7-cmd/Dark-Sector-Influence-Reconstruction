# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-04  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 54.6%** (exact Draft/data `54.57142857142857%`).

Repository state, immutable recovery notes, validated GitHub Actions logs/artifacts and durable checkpoint branches outrank chat wording. Historical scientific/resource/infrastructure outcomes remain immutable. Frozen science boundaries are unchanged.

## Immediate frontier — Exp073BU v0.1 Wm_S3 fresh-independent-PCL A/B

Exp073CR v0.3 remains RESOURCE PASS `+0/+0`; Wm_S3 scientific angular authority remains absent.

Prospective successor:
- preregistration: `experiments/073bu_article3_wm_s3_fresh_independent_ab_exact_repeatability_v0_1_prereg.md`;
- preregistration commit: `e1a0332c128c87049fb8699018a3a3e71c9c5321`;
- preregistration recovery: `recovery/2026-09-04_exp073bu_wm_s3_fresh_ab_preregistered.md`, commit `2cb2128fcac1d435b4cb9ddf4d711a025a5fc956`;
- pre-implementation contamination audit: `recovery/2026-09-04_exp073bu_preimplementation_no_old_pcl_import_audit.md`, commit `e8d75c7ea1b04d88d2f1266129ce4d89b5170349`;
- process ledger authority: `docs/CURRENT_PROCESS.md`, latest update commit `9bc86d16a04547f15e73e5c5a1044b9e847e0cc3`;
- required PASS token: `PASS_EXP073BU_WM_S3_FRESH_AB_EXACT_REPEATABILITY_V0_1`.

Current Exp073BU state: **PREREGISTERED / FRESH-PCL IMPLEMENTATION REQUIRED / NOT AUDITED / NOT ACTIVATED**.

Live Actions after preregistration remained **0 queued / 0 in-progress**; DSIR-HOME-PC is **FREE**. No numerical Exp073BU run has been launched.

## Newly closed pre-implementation audit

Direct numerical reuse of the validated Exp073CR driver is forbidden for Exp073BU science.

Code audit of `ci/exp073cr_wm_s3_ll3_sharded_resource_v0_1.py` establishes that its worker initializer consumes `root/upstream/pcl.npy`, while its seed path obtains that PCL and numerical reference-band arrays from the Exp073CQ terminal checkpoint. That is correct for the historical resource-equivalence gate but would violate the prospectively frozen Exp073BU requirement that A and B be fresh scientific executions.

Therefore Exp073BU must **not** import any Exp073CR/CQ/CM Wm_S3 numerical PCL, selected-window array, band payload, checkpoint payload, hash or historical equality target.

Reusable from Exp073CR is architecture only: exactly 8 outer workers where applicable, nested numerical-library threads=1, deterministic source-order shards, durability-before-refill, canonical `<f8` hashing, fail-closed receipt/restore checks, exact reassembly, telemetry and first-causal-failure persistence.

## Exact next permitted engineering/scientific gate

Recover and audit the repository path that creates the Wm coupling precursor/PCL directly from immutable upstream S3 and public lens-mask authorities. Then implement for each replica independently:

`fresh R1 S3 + fresh public lens mask -> fresh replica-local PCL complete-stage checkpoint -> 8-core exact ll3 shards -> complete 39-band canonical Wm_S3 array -> durable final receipt`.

Replica A and B must use isolated checkpoint/PCL state and cannot exchange arrays, hashes or other numerical outputs before both final receipts are durable.

After implementation:
1. hosted machine-checkable static audit of preregistration, implementation, source lineage, no-old-PCL firewall and checkpoint isolation;
2. freeze implementation fingerprint and exact source head;
3. fresh reconciliation requiring no competing queued/in-progress DSIR home workload;
4. explicit activation;
5. launch exactly one DSIR-HOME-PC owner process;
6. consume terminal A/B artifacts and classify only against the frozen exact comparator.

If fresh PCL generation cannot be safely checkpointed at a complete-stage boundary, **do not run Exp073BU on home** until redesigned.

## Frozen Exp073BU science contract

Upstream S3 authority:
- Exp073R1 run/job/head `33270843577` / `99148916507` / `ef783ca941fb9b9b5f5eae537986c56ff06e6536`;
- R1 artifact `9720335366`, digest `sha256:ff87d8fc7d53b16b786a4eb3d6ffeb103676efb8a548223a187b9f59689f8abd`;
- selected rows `4,196,641`;
- pixel-record bytes `16,786,564`;
- pixel-record SHA256 `3996f2bacf29d46278773530058d4f5666c0d590bf6cebc06459659166bc60ec`;
- unique occupied pixels `2,943,132`;
- occupancy SHA256 `21e3776111de305c108463b02b0e3fd5e138cc97817d37e7b05330132d058094`.

Lens authority:
- `DES_Y1A1_3x2pt_redMaGiC_MASK_HPIX4096RING.fits`;
- bytes `104595840`;
- SHA256 `a519b8522f899e4c33267bb0749f9734f8b7fa760d195636456d370f809a3d55`;
- retain original positive weights iff `mask>0.5`.

Frozen angular semantics:
- NaMaster/PyMaster 2.7 lineage;
- DES `NSIDE=4096`, RING/C;
- ell `0..12287`;
- exact 39 frozen bands;
- Wm physical component `TE <- TE`;
- canonical C-order little-endian `<f8 [39,12288]`;
- A/B PASS requires both canonical SHA256 equality and `numpy.array_equal` over full arrays;
- no tolerance, ULP allowance, rounding, smoothing, averaging, effective ell/z/k or fiducial-P rescue.

Frozen outcomes: `PASS`, `SCIENTIFIC_REPEATABILITY_FAIL`, `INFRASTRUCTURE_INCOMPLETE`, `BLOCKED`. `numerically_unresolved` is reserved for inherited downstream exact-threshold ambiguity, not for rescuing an A/B array mismatch.

## Historical authority gap preserved

Authority-gap audit commit `1f80751ca1cde9614b7ce8b167d8b4201af117fd` remains controlling history:
- Exp073X2 P = `INFRASTRUCTURE_INCOMPLETE`;
- Exp073X2 Q = `SCIENTIFIC_REPEATABILITY_FAIL`;
- Exp073AF rule 10 => `BLOCK_PRODUCTION`;
- old Exp073AA Wm_S3 route never established authority.

Exp073BU is a new prospective successor, not a revival/rescue.

## Preserved resource authority — Exp073CR v0.3

- run/job/head `33771269117` / `100701857748` / `023fcfa28f0eb904656c76e55c55d821e50c8155`;
- raw token `PASS_EXP073CR_V0_3_WM_S3_LL3_SHARDED_8CORE_RESOURCE`;
- checkpoint `checkpoints/exp073cr-wm-s3-ll3-sharded-resource-v0-3` / `db8221278798ea56b579a3dc96565fef4497bb7f`;
- fingerprint `3eb54728878e5913fcb39b9e6411480c413d6a5a6a968c67e623f1fa48e6ec29`;
- artifact `9903527609`, digest `sha256:28f6141e641726351b6dd804c07db28b6c4152de5a71a0c0b098b539a6bc0256`;
- CPU fraction `0.9623990689242612 >= 0.90`, swap increase `0 KiB`, 64 shards, exact resource reconstruction PASS;
- classification **RESOURCE PASS `+0/+0`**, never Wm_S3 science authority.

## Other preserved state

Exp073BT v0.3 remains Q5 incomplete nonclassifying source-linkage/infrastructure diagnostic `+0/+0`: run `33794449690`, job `100778710837`, artifact `9908640902`, digest `sha256:e3fc8d1f390101900d35f90e03f0317f62675e23a6971fb01aff4bc233f86dd9`.

Wm_S1 Track-A exact PASS and admitted Wm_S2 authority remain preserved. Wm_S3 authority remains absent.

Frozen global boundaries remain: `0.295<=z<=2.33`; `0<k<=0.06664762008318016 Mpc^-1`; Layer-A operator_f_invalid `<=0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES NSIDE=4096; ell `0..12287`; 39 bands; Wm `TE<-TE`; WW `EE<-EE`; canonical `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity `numerically_unresolved`; no tolerance/rounding/smoothing/averaging rescue.

Article-3 readiness remains **Verified 52.0% | Draft/data 54.6%**.