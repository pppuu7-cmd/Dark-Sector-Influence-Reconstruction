# DSIR RECOVERY LATEST — authoritative live pointer

**Updated:** 2026-09-01  
**Scope:** DSIR only; RTK/RQIR excluded.  
**Article-3 readiness:** **Verified 52.0% | Draft/data 53.7%**.

Repository state and immutable GitHub Actions artifacts outrank chat wording. Synthetic/infrastructure/provenance/numerical/performance QA gives `+0/+0` unless a frozen ledger explicitly states otherwise.

## Read first

1. `recovery/2026-09-01_exp073cb_helper_rss_semantics_audit.md`
2. `recovery/2026-09-01_exp073ca_attempt3_infra_incomplete_exp073cb_hosted_memory_qa_active.md`
3. `recovery/2026-09-01_exp073bz_remote_checkpoint_failover_pass.md`
4. `recovery/2026-08-31_exp073bv_q1_exp073bw_q1_streaming_equivalence_terminal.md`
5. `recovery/2026-08-31_exp073bj_exact_authority_pass_structure_diagnostic.md`
6. `recovery/2026-08-31_exp073aq_wm_s1_repeatability_fail_authority.md`
7. `docs/ARTICLE3_DUAL_READINESS_ACCOUNTING_2026-08-31.md`

## Current overnight frontier

- Home runner is **OFFLINE/LOCKED** until the user explicitly re-enables it.
- Exp073CA attempt3 run `33448843621`: replica A job `99673921219` terminal infrastructure failure during fresh Wm_S2 PCL; replica B job `99673921530` remains queued self-hosted and must not be revived overnight.
- Frozen Exp073CA classification remains `INFRASTRUCTURE_EXECUTION_INCOMPLETE_NO_SCIENTIFIC_CLASSIFICATION_EXP073CA`, `+0/+0`.
- Compile, checkpoint preflight/restore, heavy 39-band streaming, exact compact comparator and finalizer did not run in replica A.

## Memory-stability audit

For DES `NSIDE=4096`, `NPIX=201,326,592`: one float64 real-space map is 1.500 GiB; one complex128 mask-alm payload through ell=12287 is about 1.12509 GiB. The current simultaneous Exp073AZ Wm PCL lifetime retains two source maps, two NaMaster field-owned float64 masks, and two mask alms, already about 8.25 GiB before SHT workspace and process overhead. A 6 GiB WSL memory cap is therefore structurally unsafe for that lifetime pattern.

A sequential lifetime-only construction is the current infrastructure repair hypothesis. It must preserve the same transforms and exact PCL bytes and may not change scientific criteria.

## Exp073CB hosted synthetic exact-equivalence/RSS QA

Prospectively frozen NONCLASSIFYING hosted-only QA; no self-hosted runner use.

Frozen lineage:
- prereg `5b63330f5273fc9186bc9921f5d4702aaecb7c3a`;
- helper `c6d792f7b57fa38ca9017e6335046919bb33d94f`;
- workflow `7deadbeeafac479a059708efbfaa69e70f356470`;
- binding `1bb95adc8205aa74c78b91c46a5765f811effbaa`;
- trigger/head `07242a550fc856a6bd4621ba887866d735b96334`.

Hosted run `33464547851`, job `99721585397` is terminal failure. Prospective freeze/binding passed; environment setup failed because PyPI currently exposes no `pymaster==2.7` release. Frozen numerical cases, exact comparator and RSS stages never ran; no valid comparator inputs/artifact payload exist.

Frozen classification: **`CB_Q3_INFRASTRUCTURE_INCOMPLETE`**. This is `+0/+0`, not mismatch evidence and not a scientific result.

### Subsequent helper-semantics audit

The exact frozen CB helper cannot be reused unchanged for the intended RSS claim. Its `masks(nside)` routine allocates both masks on every call, while `sequential(nside)` uses `a,_=masks(nside)` and later `_,b=masks(nside)`. In Python `_` remains a normal live reference, so each supposedly discarded companion mask remains resident. Therefore CB's frozen `sequential` mode does not implement the intended one-target-mask-at-a-time lifetime.

This does **not** alter CB attempt1's terminal `CB_Q3_INFRASTRUCTURE_INCOMPLETE` classification because the numerical/RSS cases never ran. It does invalidate the previously proposed plan to make a conda-only successor while reusing the frozen helper unchanged for RSS evidence.

A new prospective hosted-only experiment must use single-target mask generation (e.g. separate lens/source generators or equivalent) while freezing the same transforms, one-thread policy, `hp.alm2cl`, independent-process RSS measurement, `np.array_equal`, and canonical `<f8` SHA-256 exact comparator. This remains synthetic/nonclassifying `+0/+0` QA.

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

While home runner remains locked: prospectively freeze a **new hosted-only corrected-lifetime PCL QA**. It must generate only the requested target mask at each sequential stage, provision NaMaster 2.7 via the proven conda-forge route, preserve one-thread execution, use independent processes for RSS, and require exact `np.array_equal` plus canonical `<f8` SHA equality. Complete exact mismatch is an implementation-equivalence FAIL for this prerequisite; setup/execution failure before valid comparator inputs is infrastructure incomplete. Every outcome remains `+0/+0` and cannot close a real-survey gate.

Before any trigger, re-check all queued/in-progress Actions. Do not touch or revive Exp073CA replica B overnight. A future home-runner repair/full-scale successor is not permitted until the user explicitly re-enables the home runner.

- ✅ Exp073BJ exact Track-A Wm_S1 authority PASS preserved.
- ✅ Exp073BV/BW/BZ prerequisite authority preserved.
- 🟡 Exp073CA remains infrastructure incomplete; self-hosted replica B queued but locked out.
- ❌ Exp073CB attempt1 = `CB_Q3_INFRASTRUCTURE_INCOMPLETE` due missing PyPI 2.7 distribution.
- ❌ Frozen CB helper is unsuitable for the intended one-target-at-a-time RSS claim; no conda-only reuse for RSS evidence.
- ❌ Exp073AQ permanent historical scientific FAIL preserved.
- ❌ Exp073BD remains provisional and forbidden downstream.
- ❌ Layer A/B, covariance/whitening, nuisance SVD, quotient/relation/null, G7/G8/G9 unauthorized.

**Verified: 52.0% | Draft/data: 53.7%**
