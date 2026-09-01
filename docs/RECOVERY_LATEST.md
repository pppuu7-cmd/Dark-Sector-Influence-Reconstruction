# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cc_q1_corrected_lifetime_exact_equivalence_pass.md`
2. `recovery/2026-09-01_exp073cb_helper_rss_semantics_audit.md`
3. `recovery/2026-09-01_exp073ca_attempt3_infra_incomplete_exp073cb_hosted_memory_qa_active.md`
4. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
5. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
6. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
7. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
8. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current overnight frontier

- Home runner is **OFFLINE/LOCKED** until the user explicitly re-enables it.
- Exp073CA attempt3 run `33448843621`: replica A job `99673921219` terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and must not be revived overnight.
- Frozen Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`.
- Compile, checkpoint preflight/restore, heavy 39-band streaming, exact compact comparator and finalizer did not run in replica A.
- At the Exp073CC terminal recording checkpoint there were zero `in_progress` DSIR runs and Exp073CA attempt3 was the sole queued run.

## Exp073CC terminal corrected-lifetime exact-equivalence QA

Prospectively frozen hosted-only, synthetic/nonclassifying QA. Frozen lineage:
- prereg `f451a272bfa060441a523334c48edae20ffa8603`;
- helper `583770e3607edb9f0d8168f68e89015c7913205d`;
- workflow `c1c44deca56423caa54f61cd8ea70575ea23f02f`;
- binding `377bb66f79fe598c8f0b10248bda3c1fb7104a45`;
- trigger/head `1622efc76f02876de1871123938d07936fe40cb6`.

Hosted run `33475627726`, job `99754170638` is terminal success. Immutable artifact `9788075152`, digest `sha256:08b0e29e93e9eddaabe7f23de618a7a68b152b2115eb0e1727d7f3d0af8de5d9`.

Frozen classification: **`CC_Q1_EXACT_EQUIVALENCE_PASS`**.

All frozen NSIDE 64/128/256 cases were complete and finite and passed both `np.array_equal` and canonical `<f8` SHA-256 equality. Exact shared SHAs were respectively:
- NSIDE 64: `451f7ca38df2e533468d17b1cf7cecb449f58cc9713652d605393a5359a745d5`;
- NSIDE 128: `eeb8e5041d42e39bffe4d807421623c4f963d7058a1140cbb7d27518f8c7b47e`;
- NSIDE 256: `7989e075acea10cd62abc3ec26530fa4b006c77212121c058ee51c3344f9c707`.

Independent-process peak RSS simultaneous -> corrected sequential was:
- NSIDE 64: 117652 -> 116392 KiB;
- NSIDE 128: 130908 -> 125888 KiB;
- NSIDE 256: 183124 -> 164204 KiB.

RSS is diagnostic/nonclassifying; largest observed reduction was about 10.33% at NSIDE=256. Do not extrapolate these small/medium hosted measurements into a claim that full DES NSIDE=4096 fits under the 6 GiB WSL cap. Full-scale SHT workspace remains unmeasured.

Exp073CC is `+0/+0` and closes no real-survey/scientific gate. It only establishes exact implementation-equivalence for the corrected one-target-at-a-time lifetime on the frozen hosted geometries, removing that implementation-equivalence objection to a future prospectively frozen infrastructure successor.

## Memory-stability audit

For DES `NSIDE=4096`, `NPIX=201,326,592`: one float64 real-space map is 1.500 GiB; one complex128 mask-alm payload through ell=12287 is about 1.12509 GiB. The current simultaneous Exp073AZ Wm PCL lifetime retains two source maps, two NaMaster field-owned float64 masks, and two mask alms, already about 8.25 GiB before SHT workspace and process overhead. A 6 GiB WSL memory cap is therefore structurally unsafe for that lifetime pattern.

A sequential lifetime-only construction is now supported by Exp073CC exact-equivalence QA on NSIDE 64/128/256, but full-scale memory safety is not yet demonstrated.

## Exp073CB terminal and helper audit

Exp073CB run `33464547851`, job `99721585397` remains **`CB_Q3_INFRASTRUCTURE_INCOMPLETE`**: prospective freeze/binding passed, but setup failed because PyPI exposed no `pymaster==2.7`; numerical/comparator/RSS stages never ran. `+0/+0`.

The frozen CB helper cannot be reused for RSS evidence because its `a,_=masks(nside)` / `_,b=masks(nside)` pattern keeps the unwanted companion mask live through `_`. Exp073CC prospectively corrected this by generating only the requested target mask at each sequential stage.

## Preserved scientific authority

- **Exp073BJ** run `33379013167` remains terminal Track-A exact Wm_S1 authority PASS; final authority artifact `9758841785`, digest `sha256:a7d5b30e0a8ba4ce6d8437db82982f69f41c01ac6a58c6cb121d4cbbb2c4f008`.
- **Exp073AQ** remains permanent historical hosted exact-repeatability scientific FAIL.
- **Exp073BD** remains `P3 PROVISIONAL_INCOMPLETE_NO_DOWNSTREAM_USE`, forbidden downstream.
- **Exp073BV** remains `BV_Q1_EXACT_SOURCE_LINEAGE_CONFIRMED`, artifact `9768866582`.
- **Exp073BW** remains `BW_Q1_FULL_AND_STREAM_COMPRESSED_EXACT_EQUIVALENCE_PASS`, artifact `9774112002`.
- **Exp073BZ** remains remote checkpoint/failover exact-byte PASS, hosted failover artifact `9776592370`.

No tolerance, ULP, rounding, averaging, smoothing, majority vote or preferred-replica rescue is permitted.

## Frozen Article-3 boundaries and order

Never alter post hoc: `0.295 <= z <= 2.33`; `0 < k <= 0.06664762008318016 Mpc^-1`; Layer-A `operator_f_invalid <= 0.05`; Layer-B invalid-row fraction `<=0.05`; retained dimension `>=15`; DES `NSIDE=4096`; true ell `0..12287`; 39 bands; Wm `TE <- TE`; WW `EE <- EE`; canonical selected window `<f8 [39,12288]`; no effective ell/z/k or fiducial-P shortcut; exact-threshold ambiguity remains `numerically_unresolved`.

Required order:

`validated physical forward/power-input bridges -> preregistered physical support-validity mask -> Layer A/Layer B prerequisites -> covariance restriction/whitening -> nuisance tangent rank/SVD -> quotient/relation/null control -> actual G7 authorization -> fresh G8 withheld family`.

No G8 jump.

## Exact next gate

While home runner remains locked, do not touch or revive Exp073CA replica B. The next scientifically permitted work is **hosted/read-only full-scale memory-budget/source-lifetime analysis**, especially conservative accounting or synthetic scaling of NaMaster/healpy SHT workspace for the exact production path. Any hosted scaling probe must be prospectively frozen and remains `+0/+0`; it may refine infrastructure planning but cannot close the real-survey Wm_S2 gate.

Only after the user explicitly re-enables the home runner may a separately prospectively frozen Exp073CA infrastructure successor use the Exp073CC-supported sequential lifetime repair. Such a successor must preserve frozen scientific inputs/comparators/thread policy/checkpoint semantics and the <=60 s nonclassifying heartbeat rule.

- ✅ Exp073CC = `CC_Q1_EXACT_EQUIVALENCE_PASS`; immutable artifact `9788075152`.
- ✅ Exp073BJ exact Track-A Wm_S1 authority PASS preserved.
- ✅ Exp073BV/BW/BZ prerequisite authority preserved.
- 🟡 Exp073CA remains infrastructure incomplete; self-hosted replica B queued but locked out.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
