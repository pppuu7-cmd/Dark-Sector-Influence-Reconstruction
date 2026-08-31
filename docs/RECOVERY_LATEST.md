# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable hosted artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
2. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
3. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
4. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
5. `experiments/073bw_article3_streaming_general_coupling_exact_equivalence_v0_1_prereg.md`
6. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Scientific authority state

- **Exp073BJ** run `33379013167` remains terminal Track-A exact Wm_S1 authority PASS; final authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ** remains the permanent historical hosted exact-repeatability scientific FAIL.
- Exp073BA remains infrastructure/execution incomplete.
- Exp073BD remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE` and is forbidden downstream.
- No frozen scientific readiness increment is authorized by BV/BW/BZ or performance QA.

## Exp073BV terminal exact source lineage

Hosted run `33420824723`, job `99582473539`, head `6010f094782a277017cbf0bb2a9af63331bb3282`.

Artifact `9768866582`, digest `sha256:33f013a8c7c06ce2f5f68e62a324b80f2b1911ff2a3cd3ff89a6af4add179cc5`.

Frozen label:

`BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`

The immutable receipt binds hosted NaMaster 2.7 to official upstream v2.7 commit `24365fa59a38c15732f4f37e8b29265b75c442d5`, confirms byte-identical `pymaster/nmtlib.py`, the same top-level `_nmtlib` extension object, and a global runtime `drc3jj` symbol. BV is nonclassifying `+0/+0`.

## Exp073BW terminal exact streaming equivalence

Hosted run `33435082122`, head `bdb10b6647661dabc14d24f995dfd8808e86beda`.

Artifact `9774112002`, digest `sha256:67b929eac0cbfe168b0a55410afcc2665c1d2e437abb602b992ca3a1a83bf536`.

Frozen label:

`BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`

All 18 frozen cases passed exact full-matrix vs stock equality, exact streaming-compressed vs stock-compressed equality, and exact 1-thread/2-thread/repeat equality. Cases cover the Wm signature `(0,2,0,2)`, both WW signatures `(2,2,2,2)` and `(2,-2,2,-2)`, `lmax=24,63,127`, and both frozen dyadic PCL families. Classifying comparisons use exact array and canonical `<f8` SHA equality only; all recorded `max_abs_diff` values are `0.0`. BW is nonclassifying `+0/+0`.

## Exp073BZ terminal remote-checkpoint durability QA

Hosted run `33441962503`, head `d263ae64ba4423af6380e91d52d8901c1df435b3` completed successfully.

Jobs:

- home checkpoint writer `99652059232`: success;
- hosted failover reader `99652226100`: success.

Home receipt artifact `9776581747`, digest `sha256:809b24b9e1c76158ba50af9883048eff537a15a2d075cd7f7792ae59901f43e2`, records branch `checkpoints/exp073bx-v0-1`, completed bands `[0,1,2]` and matrix SHA `1d42b89e8719cd75850103041edba0e8d2f038e384a711a31b6512ceaff0cb1e`.

Hosted failover artifact `9776592370`, digest `sha256:2b5cbb49bbf0ca16679f63bd6aee8150e06cf617054b1afe8936dac10b778dd8`, restored all 3/3 bands and returned `array_equal=true`, `sha_equal=true`, with identical expected/restored matrix SHA. Frozen inherited status: `BX_Q1_REMOTE_CHECKPOINT_FAILOVER_PASS`.

BZ is NONCLASSIFYING infrastructure/durability QA only, `+0/+0`. It establishes that a future long streaming successor can prospectively persist completed bands remotely and recover exact bytes after runner loss. Checkpointing may not alter arithmetic order, scientific comparator semantics, or acceptance criteria.

## Independent performance QA

Self-hosted Wigner scaling run `33437417184` completed successfully; artifact `9775001946`, digest `sha256:a2132539a8c5dd144fdb513415e538d25ee71deb3c90351c47b1c04fdb4ea520`.

At `lmax=308` all tested thread counts `1,2,4,6,8,10` retained exact identical output SHA; peak observed speedup was about `2.2828x` at 8 threads. This remains performance QA only and `+0/+0`.

## Frozen Article-3 boundaries and G7 order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order remains:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

Prospectively preregister a separate **full-scale checkpoint-capable streaming Track-A execution/authority successor** bound to immutable BV Q1, BW Q1 and BZ checkpoint/failover QA lineage, the exact BW helper/code lineage and frozen compilation flags. It may use full DES geometry (`NSIDE=4096`, true ell `0..12287`, 39 bands), but Exp073BD cannot be used as comparator or authority.

The successor must freeze before execution: independent replicas; exact compact comparator; exact finalizer path; canonical `<f8 [39,12288]` payload; checkpoint-boundary arithmetic invariance; infrastructure timeout/cancellation/incomplete before two valid comparator inputs distinguished from complete exact scientific mismatch. No tolerance, ULP, rounding, averaging, majority vote or preferred-replica rescue.

- ✅ Exp073BJ exact Track-A Wm_S1 authority PASS preserved.
- ✅ Exp073BV terminal `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`.
- ✅ Exp073BW terminal `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`.
- ✅ Exp073BZ remote checkpoint/failover exact-byte QA PASS, `+0/+0`.
- ✅ independent self-hosted performance QA completed, `+0/+0`.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
